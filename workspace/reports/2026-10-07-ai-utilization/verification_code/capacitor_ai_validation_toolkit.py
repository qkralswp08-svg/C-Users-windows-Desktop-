# -*- coding: utf-8 -*-
"""
커패시터 노화진단 AI 코드 검증 도구 (원본 코드 비수정 / 원본 함수 재사용)

목적
----
원본 학습 코드(…train80.py)의 데이터 로딩·window 생성·정규화·모델 생성·학습 함수를
그대로 import 해서 사용하되, "평가 프로토콜"만 바꿔 다음을 검증한다.

  E1 within      : 원본과 동일한 파일 내부 window 70/20/10 분할 (재현 기준선)
  E2 loco        : Leave-One-Condition-Pair-Out — 학습조건 쌍(정상+노화 파일) 하나를 통째로 test
  E3 permutation : 학습 파일 라벨을 '조건쌍 단위'로 무작위 뒤집어 학습 → 내부 TEST 가 여전히 높으면
                   내부 TEST 는 노화가 아니라 '녹화 파일 식별'을 측정하고 있다는 증거
  E4 baselines   : 운전조건 scalar 만 / 리플 진폭(rms)만 / 스펙트럼 모양만 으로 unseen 예측
  E5 noise       : unseen window 에 백색잡음(SNR 40~10 dB) 추가 시 정확도
  E6 gain        : unseen 리플에 센서 이득 오차(×0.8~1.2) 적용 시 정확도
  E7 seeds       : 동일 분할에서 모델 초기화 seed 만 바꿨을 때 성능 분산

원본 파일은 읽기 전용으로 import 만 한다(경로 상수는 원본 main()과 같은 방식으로 모듈 속성만 덮어씀).
CNN/LSTM/MLP 는 TensorFlow 가 있을 때만 실행된다. RF 와 보조 진단 모델(RFspec*)은 scikit-learn 만 필요.

사용 예
-------
python -I capacitor_ai_validation_toolkit.py --code "<원본 train80.py>" --data-root "<TXT 폴더>" \
    --out "<결과 폴더>" --models RF CNN --combination A1 --experiments all --seeds 3

주의: window-level 정확도는 같은 파일의 window 끼리 독립이 아니므로, 결론은 파일/케이스 단위
지표(file_majority, case_pair_correct)와 그 신뢰구간을 우선해서 판단한다.
"""
import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score, confusion_matrix

EXPERIMENTS = ["within", "loco", "permutation", "baselines", "noise", "gain", "seeds"]


# ---------------------------------------------------------------------------
# 원본 모듈 로딩
# ---------------------------------------------------------------------------
def load_original(code_path, data_root):
    sys.dont_write_bytecode = True  # 원본 폴더에 __pycache__ 를 만들지 않음
    spec = importlib.util.spec_from_file_location("capacitor_original", str(code_path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    if data_root:
        for cfg in mod.CONDITION_EXPERIMENTS.values():
            cfg["train_data_dir"] = str(data_root)
            cfg["unseen_data_dir"] = str(data_root)
        mod.TWO_CONDITION_DATA_DIR = str(data_root)
        mod.THREE_CONDITION_DATA_DIR = str(data_root)
    return mod


def strip_state(name):
    name = re.sub(r"[_\s-]*(normal|aged|정상|노화(?:_?2)?)[_\s-]*unseen$", "", str(name), flags=re.I)
    return re.sub(r"[_\s-]*(normal|aged|정상|노화(?:_?2)?)$", "", name, flags=re.I)


def build_files(mod):
    """원본 함수로 메타데이터와 window 를 만든다. 반환: 파일 단위 dict 리스트."""
    base_train = mod.collect_metadata(mod.INTEGRATED_CONDITIONS, "train")
    extra = mod.load_two_condition_outer_train_metadata()
    train_meta = mod.merge_extra_training_metadata(base_train, extra)
    tests = {
        "1C": mod.collect_metadata(mod.INTEGRATED_CONDITIONS, "unseen"),
        "2C": mod.load_two_condition_test_metadata(),
        "3C": mod.load_three_condition_test_metadata(),
    }
    mod.validate_metadata_splits(train_meta, {k: v for k, v in tests.items()})
    files = []
    for role, frame in [("TRAIN", train_meta)] + list(tests.items()):
        if frame is None or frame.empty:
            continue
        for _, meta in frame.iterrows():
            Xw, Xi, Iin, Xc, y, _ = mod.build_windows_for_file(meta)
            files.append({
                "role": role, "uid": meta["file_uid"], "key": meta["file_key"],
                "label": int(meta["label"]), "axis": meta["condition_axis"],
                "name": meta["condition_name"],
                "f0": float(meta["fundamental_frequency_hz"]),
                "fsw": float(meta["switching_frequency_hz"]),
                "v1": float(meta["output_fundamental_voltage_v"]),
                "Xw": Xw, "Xi": Xi, "Iin": Iin, "Xc": Xc, "y": y,
            })
    assign_pairs(files)
    return files


def assign_pairs(files):
    """정상/노화 조건쌍 식별. 이름 기반으로 묶고, 한쪽 라벨만 있는 그룹은 같은 축·같은 (f0,fsw,V1)의
    반대 라벨 그룹과 병합한다(예: v_4_normal / v_3_aged 처럼 이름이 어긋난 경우)."""
    for f in files:
        f["pair"] = f"{f['role']}::{f['axis']}::{strip_state(f['name'])}"
    groups = {}
    for f in files:
        groups.setdefault(f["pair"], []).append(f)
    single = {k: v for k, v in groups.items() if len({x["label"] for x in v}) == 1}
    used = set()
    for k, v in single.items():
        if k in used:
            continue
        a = v[0]
        for k2, v2 in single.items():
            if k2 == k or k2 in used:
                continue
            b = v2[0]
            if (b["role"] == a["role"] and b["axis"] == a["axis"] and b["label"] != a["label"]
                    and (b["f0"], b["fsw"], b["v1"]) == (a["f0"], a["fsw"], a["v1"])):
                for x in v2:
                    x["pair"] = k
                used.update({k, k2})
                break


# ---------------------------------------------------------------------------
# 데이터셋 조립 / 정규화 / 학습 (원본 함수 사용)
# ---------------------------------------------------------------------------
def assemble(parts, label_override=None):
    """parts: [(file_dict, index_array)]"""
    keys = [("X_wave_raw", "Xw"), ("X_current_raw", "Xi"), ("X_input_current_raw", "Iin"),
            ("X_control_raw", "Xc")]
    ds = {dst: np.concatenate([f[src][idx] for f, idx in parts], axis=0) for dst, src in keys}
    ys = []
    for f, idx in parts:
        lab = f["label"] if label_override is None else label_override.get(f["uid"], f["label"])
        ys.append(np.full(len(idx), lab, dtype=np.int64))
    ds["y"] = np.concatenate(ys)
    ds["files"] = np.concatenate([[f["uid"]] * len(idx) for f, idx in parts])
    ds["pairs"] = np.concatenate([[f["pair"]] * len(idx) for f, idx in parts])
    ds["true_y"] = np.concatenate([np.full(len(idx), f["label"]) for f, idx in parts])
    return ds


def all_idx(f):
    return np.arange(len(f["y"]))


def spectral_features(xw, fs=100_000.0, n_bands=48, shape_only=False):
    """보조 진단 모델용 log 대역 에너지 (원본 모델과 별개)."""
    x = xw[..., 0]
    win = np.hanning(x.shape[1])
    spec = np.abs(np.fft.rfft(x * win, axis=1)) ** 2
    freqs = np.fft.rfftfreq(x.shape[1], 1 / fs)
    edges = np.geomspace(50.0, fs / 2, n_bands + 1)
    bands = np.stack([spec[:, (freqs >= lo) & (freqs < hi)].sum(axis=1)
                      for lo, hi in zip(edges[:-1], edges[1:])], axis=1) + 1e-20
    if shape_only:
        bands = bands / bands.sum(axis=1, keepdims=True)
    return np.log10(bands)


def train_and_predict(mod, model_type, combo, train_ds, val_ds, test_sets, workdir, seed=None):
    """원본 normalize/train/predict 함수로 학습 후 각 test set 확률을 반환."""
    workdir.mkdir(parents=True, exist_ok=True)
    if model_type.startswith("RFspec") or model_type in {"COND_ONLY", "AMP_ONLY"}:
        return _aux_model(model_type, train_ds, test_sets, seed)
    mod.activate_combination(combo)
    stats = mod.fit_preprocessor(train_ds)
    norm = lambda d: mod.apply_preprocessor(dict(d), *stats)
    datasets = {"TRAIN": norm(train_ds), "VALIDATION": norm(val_ds)}
    saved_seed = mod.SPLIT_SEED
    if seed is not None:
        mod.SPLIT_SEED = int(seed)  # train_model 내부 set_global_seed / RF random_state 에만 영향
    try:
        model, _, _ = mod.train_model(model_type, datasets, workdir)
    finally:
        mod.SPLIT_SEED = saved_seed
    out = {}
    for name, ds in test_sets.items():
        out[name] = mod.predict_probabilities(model, norm(ds), model_type)
    if mod.tf is not None and model_type != "RF":
        mod.tf.keras.backend.clear_session()
    return out


def _aux_model(model_type, train_ds, test_sets, seed):
    rs = 42 if seed is None else int(seed)

    def feats(ds):
        if model_type == "RFspec":
            return spectral_features(ds["X_wave_raw"])
        if model_type == "RFspec_shape":
            return spectral_features(ds["X_wave_raw"], shape_only=True)
        if model_type == "COND_ONLY":
            return ds["X_control_raw"]
        if model_type == "AMP_ONLY":
            rms = np.sqrt(np.mean(ds["X_wave_raw"][..., 0] ** 2, axis=1, keepdims=True))
            return np.hstack([np.log10(rms + 1e-12), ds["X_control_raw"]])
        raise ValueError(model_type)

    if model_type == "AMP_ONLY":
        mu = feats(train_ds).mean(0)
        sd = feats(train_ds).std(0) + 1e-9
        clf = LogisticRegression(max_iter=2000, class_weight="balanced")
        clf.fit((feats(train_ds) - mu) / sd, train_ds["y"])
        return {n: _proba(clf, (feats(d) - mu) / sd) for n, d in test_sets.items()}
    clf = RandomForestClassifier(n_estimators=200, class_weight="balanced", random_state=rs, n_jobs=-1)
    clf.fit(feats(train_ds), train_ds["y"])
    return {n: _proba(clf, feats(d)) for n, d in test_sets.items()}


def _proba(clf, x):
    raw = clf.predict_proba(x)
    p = np.zeros((len(x), 2))
    p[:, np.asarray(clf.classes_, dtype=int)] = raw
    return p


# ---------------------------------------------------------------------------
# 지표
# ---------------------------------------------------------------------------
def wilson(k, n, z=1.96):
    if n == 0:
        return (np.nan, np.nan)
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - h) / d, (c + h) / d)


def score(ds, proba, against="true_y"):
    y = ds[against]
    pred = np.argmax(proba, axis=1)
    frame = pd.DataFrame({"file": ds["files"], "pair": ds["pairs"], "y": y, "pred": pred})
    cm = confusion_matrix(y, pred, labels=[0, 1])
    with np.errstate(invalid="ignore", divide="ignore"):
        rec_aged = cm[1, 1] / cm[1].sum() if cm[1].sum() else np.nan
        rec_norm = cm[0, 0] / cm[0].sum() if cm[0].sum() else np.nan
        prec_aged = cm[1, 1] / cm[:, 1].sum() if cm[:, 1].sum() else np.nan
    f1_aged = (2 * prec_aged * rec_aged / (prec_aged + rec_aged)
               if np.isfinite(prec_aged) and np.isfinite(rec_aged) and (prec_aged + rec_aged) > 0 else np.nan)
    by_file = frame.groupby("file").agg(y=("y", "first"), pair=("pair", "first"),
                                        aged_ratio=("pred", "mean"))
    by_file["file_pred"] = (by_file["aged_ratio"] >= 0.5).astype(int)
    by_file["file_correct"] = (by_file["file_pred"] == by_file["y"]).astype(int)
    by_pair = by_file.groupby("pair").agg(n_files=("y", "size"), n_labels=("y", "nunique"),
                                          all_correct=("file_correct", "min"))
    full_pairs = by_pair[by_pair["n_labels"] == 2]
    k, n = int(by_file["file_correct"].sum()), int(len(by_file))
    lo, hi = wilson(k, n)
    return {
        "window_acc": float((frame["y"] == frame["pred"]).mean()),
        "window_balanced_acc": float(balanced_accuracy_score(y, pred)) if len(set(y)) > 1 else np.nan,
        "recall_aged": float(rec_aged), "recall_normal": float(rec_norm),
        "f1_aged": float(f1_aged) if f1_aged == f1_aged else np.nan,
        "tn": int(cm[0, 0]), "fp": int(cm[0, 1]), "fn": int(cm[1, 0]), "tp": int(cm[1, 1]),
        "file_majority_acc": k / n if n else np.nan, "file_n": n,
        "file_acc_ci95_low": lo, "file_acc_ci95_high": hi,
        "case_pair_correct": float(full_pairs["all_correct"].mean()) if len(full_pairs) else np.nan,
        "case_pairs_n": int(len(full_pairs)),
        "single_label_cases": int((by_pair["n_labels"] == 1).sum()),
    }


# ---------------------------------------------------------------------------
# 실험
# ---------------------------------------------------------------------------
def within_split(mod, train_files):
    tr, va, te = [], [], []
    for f in train_files:
        a, b, c = mod.split_train_validation_test_indices(len(f["y"]), f["uid"])
        tr.append((f, a)); va.append((f, b)); te.append((f, c))
    return tr, va, te


def unseen_sets(files):
    sets = {}
    for role in ("1C", "2C", "3C"):
        parts = [(f, all_idx(f)) for f in files if f["role"] == role]
        if parts:
            sets[f"UNSEEN_{role}"] = assemble(parts)
    all_parts = [(f, all_idx(f)) for f in files if f["role"] != "TRAIN"]
    sets["UNSEEN_ALL"] = assemble(all_parts)
    return sets


def run(args):
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    mod = load_original(args.code, args.data_root)
    if args.epochs:
        mod.EPOCHS = int(args.epochs)
    combo = next(c for c in mod.INPUT_COMBINATIONS if c[0] == args.combination)
    files = build_files(mod)
    train_files = [f for f in files if f["role"] == "TRAIN"]
    exps = EXPERIMENTS if "all" in args.experiments else args.experiments
    rows = []

    inv = pd.DataFrame([{k: f[k] for k in ("role", "key", "uid", "label", "axis", "name", "pair",
                                           "f0", "fsw", "v1")} | {"windows": len(f["y"])} for f in files])
    inv.to_csv(out / "file_inventory.csv", index=False, encoding="utf-8-sig")

    def record(exp, model, test_name, metrics, **extra):
        row = {"experiment": exp, "model": model, "combination": combo[0], "test_set": test_name}
        row.update(extra)
        row.update(metrics)
        rows.append(row)
        print(json.dumps({k: (round(v, 4) if isinstance(v, float) else v) for k, v in row.items()},
                         ensure_ascii=False))

    tr, va, te = within_split(mod, train_files)
    train_ds, val_ds, test_ds = assemble(tr), assemble(va), assemble(te)
    unseen = unseen_sets(files)
    models = list(args.models) + list(args.aux_models)

    # E1 within-file (원본 재현)
    if "within" in exps or "noise" in exps or "gain" in exps:
        for model in models:
            sets = {"INTERNAL_TEST": test_ds, **unseen}
            noisy = {}
            if "noise" in exps:
                rng = np.random.default_rng(0)
                for snr in (40, 30, 20, 10):
                    d = dict(unseen["UNSEEN_ALL"])
                    x = d["X_wave_raw"].copy()
                    p = np.mean(x ** 2, axis=(1, 2), keepdims=True)
                    x = x + rng.normal(size=x.shape) * np.sqrt(p / 10 ** (snr / 10))
                    x = x - x.mean(axis=1, keepdims=True)  # 원본 window 전처리(DC 제거)와 일치
                    d["X_wave_raw"] = x.astype(np.float32)
                    noisy[f"NOISE_SNR{snr}dB"] = d
            if "gain" in exps:
                for g in (0.8, 0.9, 0.95, 1.05, 1.1, 1.2):
                    d = dict(unseen["UNSEEN_ALL"])
                    d["X_wave_raw"] = (d["X_wave_raw"] * g).astype(np.float32)
                    noisy[f"GAIN_x{g}"] = d
            probs = train_and_predict(mod, model, combo, train_ds, val_ds, {**sets, **noisy},
                                      out / "work" / f"within_{model}")
            for name, p in probs.items():
                exp = "E1_within" if name in sets else ("E5_noise" if "NOISE" in name else "E6_gain")
                record(exp, model, name, score({**sets, **noisy}[name], p))

    # E2 LOCO (조건쌍 단위 hold-out)
    if "loco" in exps:
        pairs = sorted({f["pair"] for f in train_files})
        for model in models:
            for held in pairs:
                rest = [f for f in train_files if f["pair"] != held]
                tr2, va2, te2 = within_split(mod, rest)
                # 남은 학습 파일의 원본 TEST(10%) window 는 학습에 합치고, VALIDATION(20%)만 조기종료용으로 둔다
                tr2 = [(f, np.concatenate([a, c])) for (f, a), (_, c) in zip(tr2, te2)]
                test_parts = [(f, all_idx(f)) for f in train_files if f["pair"] == held]
                probs = train_and_predict(mod, model, combo, assemble(tr2), assemble(va2),
                                          {"HELD_OUT_PAIR": assemble(test_parts)},
                                          out / "work" / f"loco_{model}")
                record("E2_loco", model, "HELD_OUT_PAIR", score(assemble(test_parts), probs["HELD_OUT_PAIR"]),
                       held_out_pair=held)

    # E3 조건쌍 단위 라벨 무작위 뒤집기
    if "permutation" in exps:
        pairs = sorted({f["pair"] for f in train_files})
        for model in models:
            for rep in range(args.permutations):
                rng = np.random.default_rng(1000 + rep)
                flip = {p: bool(rng.integers(0, 2)) for p in pairs}
                if not any(flip.values()):
                    flip[pairs[0]] = True
                override = {f["uid"]: (1 - f["label"]) if flip[f["pair"]] else f["label"] for f in train_files}
                ptr, pva, pte = (assemble(x, label_override=override) for x in within_split(mod, train_files))
                probs = train_and_predict(mod, model, combo, ptr, pva, {"INTERNAL_TEST": pte, **unseen},
                                          out / "work" / f"perm_{model}")
                frac = float(np.mean(list(flip.values())))
                record("E3_permutation", model, "INTERNAL_TEST(vs permuted labels)",
                       score(pte, probs["INTERNAL_TEST"], against="y"), rep=rep, flipped_pair_fraction=frac)
                record("E3_permutation", model, "INTERNAL_TEST(vs true labels)",
                       score(pte, probs["INTERNAL_TEST"]), rep=rep, flipped_pair_fraction=frac)
                record("E3_permutation", model, "UNSEEN_ALL(vs true labels)",
                       score(unseen["UNSEEN_ALL"], probs["UNSEEN_ALL"]), rep=rep, flipped_pair_fraction=frac)

    # E4 단순 기준선
    if "baselines" in exps:
        for model in ("COND_ONLY", "AMP_ONLY", "RFspec", "RFspec_shape"):
            probs = train_and_predict(mod, model, combo, train_ds, val_ds, {"INTERNAL_TEST": test_ds, **unseen},
                                      out / "work" / "baselines")
            for name, p in probs.items():
                record("E4_baseline", model, name, score({"INTERNAL_TEST": test_ds, **unseen}[name], p))

    # E7 seed 분산
    if "seeds" in exps:
        for model in models:
            for s in range(args.seeds):
                probs = train_and_predict(mod, model, combo, train_ds, val_ds, {"INTERNAL_TEST": test_ds, **unseen},
                                          out / "work" / f"seed_{model}", seed=100 + s)
                for name, p in probs.items():
                    record("E7_seeds", model, name, score({"INTERNAL_TEST": test_ds, **unseen}[name], p), seed=100 + s)

    result = pd.DataFrame(rows)
    result.to_csv(out / "validation_results.csv", index=False, encoding="utf-8-sig")
    summarize(result, out)
    return result


def summarize(result, out):
    if result.empty:
        return
    cols = ["window_acc", "window_balanced_acc", "file_majority_acc", "case_pair_correct"]
    summary = (result.groupby(["experiment", "model", "test_set"], dropna=False)[cols]
               .agg(["mean", "std", "count"]).round(4))
    summary.to_csv(out / "validation_summary.csv", encoding="utf-8-sig")
    with open(out / "validation_summary.md", "w", encoding="utf-8") as fh:
        fh.write("# 검증 실험 요약 (자동 생성)\n\n")
        fh.write("window 지표는 같은 파일 window 간 비독립이므로 파일/케이스 지표를 우선 해석할 것.\n\n")
        fh.write(summary.to_string())
        fh.write("\n")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--code", required=True, help="원본 학습 코드(.py) 경로 — 수정하지 않음")
    ap.add_argument("--data-root", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--models", nargs="*", default=["RF"], help="원본 모델: RF CNN LSTM MLP")
    ap.add_argument("--aux-models", nargs="*", default=["RFspec"],
                    help="보조 진단 모델: RFspec RFspec_shape (원본 비교 대상 아님)")
    ap.add_argument("--combination", default="A1")
    ap.add_argument("--experiments", nargs="+", default=["all"], choices=EXPERIMENTS + ["all"])
    ap.add_argument("--permutations", type=int, default=3)
    ap.add_argument("--seeds", type=int, default=3)
    ap.add_argument("--epochs", type=int, default=None)
    args = ap.parse_args(argv)
    run(args)


if __name__ == "__main__":
    sys.exit(main())
