# -*- coding: utf-8 -*-
"""
검증 도구 자체 점검용 '합성' 3상 인버터 DC-link 리플 데이터 생성기.

주의
----
* 이 파일이 만드는 데이터는 연구실 실측 데이터가 아니다. 검증 도구
  (capacitor_ai_validation_toolkit.py)와 원본 학습 코드의 분할/정규화/평가 구조가
  의도대로 동작하는지 확인하기 위한 합성 데이터이며, 여기서 나온 정확도 수치를
  연구실 모델의 성능으로 해석하면 안 된다.
* 회로 가정(2-level 3상 SPWM 인버터, RL 부하, Vs-Rs-Ls DC 전원, C+ESR DC-link)과
  모든 소자값은 임의 가정값이다. 연구실 인버터 토폴로지/정격은 원본 코드에서 확인되지 않는다.

출력 형식은 원본 코드의 load_current_and_ripple()이 읽는 4열 TXT와 같다.
  0열 time [s], 1열 a상 부하전류 [A], 2열 인버터 입력전류(i_inv) [A], 3열 DC-link 리플 전압 [V, AC 결합]

파일 목록(file_key, label, f0, fsw, V1)은 원본 코드의 활성 메타데이터를 ast로 읽어
그대로 생성한다(원본 모듈은 import 하지 않는다).

사용법
------
python -I synthetic_inverter_data.py --code <원본 train80.py 경로> --out <TXT 출력 폴더>
       [--duration 0.25] [--session-gain 0.0] [--seed 0]

--session-gain 을 0보다 크게 주면 '측정 세션(tek 번호 블록)마다 다른 프로브 이득'을
추가해, 라벨과 측정 순서가 교락된 상황(측정 교락)을 모사할 수 있다.
"""
import argparse
import ast
from pathlib import Path

import numpy as np
from scipy import signal

# ---------------------------------------------------------------------------
# 합성 회로 가정값 (임의)
# ---------------------------------------------------------------------------
VDC_SOURCE = 400.0          # DC 전원 전압 [V]
RS, LS = 0.5, 1.0e-3        # DC 전원 측 직렬 R [ohm], L [H]
C_NORMAL, ESR_NORMAL = 1.0e-3, 0.10   # 정상 커패시터 C [F], ESR [ohm]
C_AGED, ESR_AGED = 0.8e-3, 0.20       # 노화(EOL 기준 예: C -20 %, ESR x2) — 가정값
R_NOMINAL, L_NOMINAL = 32.0, 18.0e-3  # 2/3조건 목록에 기재된 R/L 을 공칭값으로 사용
R_AXIS_VALUES = {"R1": 20.0, "R3": 40.0, "R4": 50.0}  # 1조건 R축 값은 코드에 없음 → 가정
SIM_DT = 1.0e-6             # 내부 시뮬레이션 간격 [s]
FS_OUT = 100_000.0          # 출력 샘플링 [Hz] (원본 FS_NOMINAL 과 동일)
NOISE_V = 0.02              # 리플 측정 백색잡음 rms [V]
NOISE_I = 0.02              # 전류 측정 백색잡음 rms [A]


def read_active_file_list(code_path):
    """원본 코드의 리터럴 상수에서 활성(주석 아닌) 파일 항목을 추출한다."""
    tree = ast.parse(Path(code_path).read_text(encoding="utf-8"))
    consts = {}
    for node in tree.body:
        if (isinstance(node, ast.Assign) and len(node.targets) == 1
                and isinstance(node.targets[0], ast.Name)):
            name = node.targets[0].id
            if name in {"CONDITION_EXPERIMENTS", "TWO_CONDITION_OUTER_TRAIN_FILES",
                        "TWO_CONDITION_TEST_FILES", "THREE_CONDITION_TEST_FILES"}:
                consts[name] = ast.literal_eval(node.value)
    items = []
    for cfg in consts["CONDITION_EXPERIMENTS"].values():
        items.extend(cfg.get("train_files", []))
        items.extend(cfg.get("unseen_files", []))
    for name in ("TWO_CONDITION_OUTER_TRAIN_FILES", "TWO_CONDITION_TEST_FILES",
                 "THREE_CONDITION_TEST_FILES"):
        items.extend(consts.get(name, []))
    unique = {}
    for item in items:
        unique.setdefault(item["file_key"], item)
    return list(unique.values())


def load_resistance_for(item):
    if item.get("load_resistance_ohm") is not None:
        return float(item["load_resistance_ohm"]), float(item.get("load_inductor_mh", 18.0)) * 1e-3
    name = str(item.get("condition_name", ""))
    for key, value in R_AXIS_VALUES.items():
        if name.startswith(key + "_"):
            return value, L_NOMINAL
    return R_NOMINAL, L_NOMINAL


def simulate(f0, fsw, v1_ll_rms, r_load, l_load, cap, esr, duration, rng):
    n = int(round(duration / SIM_DT))
    t = np.arange(n) * SIM_DT
    m = v1_ll_rms * np.sqrt(2.0) / np.sqrt(3.0) / (VDC_SOURCE / 2.0)
    m = min(m, 1.0)
    theta0 = rng.uniform(0, 2 * np.pi)
    carrier = signal.sawtooth(2 * np.pi * fsw * t + rng.uniform(0, 2 * np.pi), width=0.5)
    states, phase_v = [], []
    for k in range(3):
        ref = m * np.sin(2 * np.pi * f0 * t + theta0 - 2 * np.pi * k / 3)
        states.append((ref > carrier).astype(np.float64))
    s = np.vstack(states)
    v_x0 = (s - 0.5) * VDC_SOURCE                 # 이상적 DC 전압 가정 (리플의 역영향 무시)
    v_n0 = v_x0.mean(axis=0)
    v_xn = v_x0 - v_n0
    a = np.exp(-r_load * SIM_DT / l_load)
    b = (1 - a) / r_load
    i_load = signal.lfilter([0.0, b], [1.0, -a], v_xn, axis=1)
    i_inv = np.sum(s * i_load, axis=0)
    # DC 측: x=[i_s, v_C], u=[Vs, i_inv], y=v_dc = v_C + ESR*(i_s - i_inv)
    A = np.array([[-(RS + esr) / LS, -1.0 / LS], [1.0 / cap, 0.0]])
    B = np.array([[1.0 / LS, esr / LS], [0.0, -1.0 / cap]])
    Cm = np.array([[esr, 1.0]])
    Dm = np.array([[0.0, -esr]])
    ad, bd, cd, dd, _ = signal.cont2discrete((A, B, Cm, Dm), SIM_DT, method="zoh")
    u = np.vstack([np.full(n, VDC_SOURCE), i_inv]).T
    x0 = np.array([np.mean(i_inv), VDC_SOURCE - RS * np.mean(i_inv)])
    _, y, _ = signal.dlsim((ad, bd, cd, dd, SIM_DT), u, t=t, x0=x0)
    v_dc = y[:, 0]
    step = int(round(1.0 / (FS_OUT * SIM_DT)))
    skip = int(0.05 / SIM_DT)                      # 초기 과도 50 ms 제거
    sl = slice(skip, None, step)
    t_out = t[sl] - t[skip]
    ripple = v_dc[sl] - np.mean(v_dc[sl])
    return t_out, i_load[0, sl], i_inv[sl], ripple


def session_of(file_key):
    num = int("".join(ch for ch in file_key if ch.isdigit()))
    return num // 10  # tek 번호 10개 단위를 하나의 측정 세션으로 가정


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--code", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--duration", type=float, default=0.25)
    ap.add_argument("--session-gain", type=float, default=0.0,
                    help="세션별 프로브 이득 오차의 표준편차(예: 0.05 = 5 %)")
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    rng = np.random.default_rng(args.seed)
    session_gain = {}
    for item in read_active_file_list(args.code):
        aged = str(item["label"]).startswith("노화") or str(item["label"]).lower() == "aged"
        cap, esr = (C_AGED, ESR_AGED) if aged else (C_NORMAL, ESR_NORMAL)
        r_load, l_load = load_resistance_for(item)
        t, i_a, i_inv, ripple = simulate(
            float(item["fundamental_frequency_hz"]), float(item["switching_frequency_hz"]),
            float(item["output_fundamental_voltage_v"]), r_load, l_load, cap, esr,
            args.duration, rng)
        sess = session_of(item["file_key"])
        if args.session_gain > 0:
            session_gain.setdefault(sess, 1.0 + rng.normal(0, args.session_gain))
            ripple = ripple * session_gain[sess]
        ripple = ripple + rng.normal(0, NOISE_V, ripple.shape)
        i_a = i_a + rng.normal(0, NOISE_I, i_a.shape)
        i_inv = i_inv + rng.normal(0, NOISE_I, i_inv.shape)
        data = np.column_stack([t, i_a, i_inv, ripple])
        np.savetxt(out / f"{item['file_key']}.txt", data, fmt="%.9e", delimiter="\t")
        print(f"{item['file_key']}: label={item['label']} f0={item['fundamental_frequency_hz']} "
              f"fsw={item['switching_frequency_hz']} V1={item['output_fundamental_voltage_v']} "
              f"R={r_load} ripple_rms={np.std(ripple):.4f} V samples={len(t)}")


if __name__ == "__main__":
    main()
