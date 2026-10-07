# -*- coding: utf-8 -*-
"""
보고서 데이터 그림 생성 (컨테이너에 한글 폰트가 없어 그림 내부 레이블은 영어).

  fig_operating_points.png      : 학습/미관측 운전점 분포 (원본 코드 메타데이터)
  fig_measurement_order.png     : tek 번호(측정 순서)와 라벨 — 측정 블록 구조
  fig_synthetic_protocols.png   : 평가 프로토콜별 파일 단위 정확도 (합성 데이터 — 메커니즘 예시)
  fig_synthetic_gain.png        : 센서 이득 오차 민감도 (합성 데이터 — 메커니즘 예시)

사용법: python make_figures.py  (같은 보고서 폴더의 data/*.csv 를 읽음)
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).resolve().parent
DATA = HERE.parent / "data"

# dataviz 기본 팔레트(라이트 모드) — 범주 1~3 슬롯, 텍스트/표면 토큰
BLUE, ORANGE, AQUA = "#2a78d6", "#eb6834", "#1baf7a"
INK, INK2, GRID, SURF = "#0b0b0b", "#52514e", "#e4e3df", "#fcfcfb"

plt.rcParams.update({
    "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF,
    "axes.edgecolor": GRID, "axes.labelcolor": INK2, "xtick.color": INK2, "ytick.color": INK2,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6, "axes.spines.top": False,
    "axes.spines.right": False, "font.size": 9, "axes.titlesize": 10, "axes.titlecolor": INK,
    "legend.frameon": False,
})


def load_meta():
    d = pd.read_csv(DATA / "active_file_metadata.csv")
    d["tek"] = d["file_key"].str[3:].astype(int)
    d["aged"] = (d["label"] == "노화").astype(int)
    group = {"TRAIN": "Train (1-condition axes)", "TRAIN_2C_OUTER": "Train (2-condition outer)",
             "UNSEEN_1C": "Unseen 1-condition", "UNSEEN_2C": "Unseen 2-condition",
             "UNSEEN_3C": "Unseen 3-condition"}
    d["group"] = d["role"].map(group)
    return d


STYLE = {  # 색(학습=파랑, 미관측=주황) + 마커 모양으로 이중 부호화
    "Train (1-condition axes)": dict(c=BLUE, marker="o", s=46),
    "Train (2-condition outer)": dict(c=BLUE, marker="s", s=46),
    "Unseen 1-condition": dict(c=ORANGE, marker="^", s=52),
    "Unseen 2-condition": dict(c=ORANGE, marker="D", s=40),
    "Unseen 3-condition": dict(c=ORANGE, marker="X", s=58),
}


def fig_operating_points(d):
    pts = d.drop_duplicates(["group", "fundamental_frequency_hz", "switching_frequency_hz",
                             "output_fundamental_voltage_v"])
    pairs = [("fundamental_frequency_hz", "switching_frequency_hz", "f0 [Hz]", "fsw [kHz]"),
             ("fundamental_frequency_hz", "output_fundamental_voltage_v", "f0 [Hz]", "V1 line-line rms [V]"),
             ("switching_frequency_hz", "output_fundamental_voltage_v", "fsw [kHz]", "V1 line-line rms [V]")]
    fig, axes = plt.subplots(1, 3, figsize=(11.5, 3.6))
    for ax, (x, y, xl, yl) in zip(axes, pairs):
        for g, st in STYLE.items():
            s = pts[pts["group"] == g]
            xv = s[x] / (1000 if x == "switching_frequency_hz" else 1)
            yv = s[y] / (1000 if y == "switching_frequency_hz" else 1)
            ax.scatter(xv, yv, label=g, edgecolors=SURF, linewidths=1.5, zorder=3, **st)
        ax.set_xlabel(xl)
        ax.set_ylabel(yl)
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", bbox_to_anchor=(0.5, -0.12), ncol=5, fontsize=8)
    fig.suptitle("Operating points of active files (train80.py metadata): every unseen point lies inside "
                 "the training range", y=1.02, fontsize=10, color=INK)
    fig.text(0.01, -0.19, "R-axis files (R1/R3/R4) have no R value in the code; reference and R-axis files "
             "overlap at (60 Hz, 8 kHz, 100 V).", fontsize=8, color=INK2)
    fig.tight_layout()
    fig.savefig(HERE / "fig_operating_points.png", dpi=170, bbox_inches="tight")
    plt.close(fig)


def fig_measurement_order(d):
    rows = ["Train (1-condition axes)", "Train (2-condition outer)", "Unseen 1-condition",
            "Unseen 2-condition", "Unseen 3-condition"]
    blocks = [("A", 14, 48), ("B", 124.5, 140), ("C", 141, 162), ("D", 162.5, 183.5), ("E", 217, 239)]
    fig, (axl, axr) = plt.subplots(1, 2, figsize=(11.5, 3.6), sharey=True,
                                   gridspec_kw={"width_ratios": [1, 3], "wspace": 0.05})
    for ax, (lo_x, hi_x) in [(axl, (12, 50)), (axr, (120, 241))]:
        for name, lo, hi in blocks:
            if lo >= lo_x and hi <= hi_x:
                ax.axvspan(lo, hi, color=GRID, alpha=0.6, zorder=0, lw=0)
                ax.text((lo + hi) / 2, len(rows) - 0.45, f"block {name}", ha="center", va="bottom",
                        fontsize=8, color=INK2)
        for i, r in enumerate(rows):
            s = d[d["group"] == r]
            for aged, color, marker, lab in [(0, BLUE, "o", "Normal"), (1, ORANGE, "^", "Aged")]:
                t = s[s["aged"] == aged]
                ax.scatter(t["tek"], [i] * len(t), c=color, marker=marker, s=44, edgecolors=SURF,
                           linewidths=1.2, zorder=3, label=lab if (i == 0 and ax is axr) else None)
        ax.set_xlim(lo_x, hi_x)
    axl.spines["right"].set_visible(False)
    axr.spines["left"].set_visible(False)
    axr.tick_params(left=False)
    axl.set_yticks(range(len(rows)))
    axl.set_yticklabels(rows)
    axl.set_ylim(-0.6, len(rows) + 0.15)
    fig.text(0.5, -0.03, "Oscilloscope file number tek#### (assumed measurement order; axis broken between 50 and 120; "
             "gray bands = inferred measurement blocks)", ha="center", fontsize=8, color=INK2)
    axr.legend(loc="lower center", bbox_to_anchor=(0.5, -0.32), ncol=2, fontsize=8)
    fig.suptitle("Labels were recorded in contiguous blocks; all eight 3-condition test files share block D "
                 "with three training pairs", fontsize=10, color=INK, y=1.0)
    fig.savefig(HERE / "fig_measurement_order.png", dpi=170, bbox_inches="tight")
    plt.close(fig)


def fig_synthetic_protocols():
    r = pd.read_csv(DATA / "synthetic_validation_results.csv")
    proto = [
        ("E1_within", "INTERNAL_TEST", "Internal TEST\n(same files)"),
        ("E1_within", "UNSEEN_ALL", "Unseen files\n(interpolation)"),
        ("E2_loco", "HELD_OUT_PAIR", "Leave-one-\ncondition-pair-out"),
        ("E3_permutation", "INTERNAL_TEST(vs permuted labels)", "Internal TEST,\nlabels randomly flipped"),
        ("E3_permutation", "UNSEEN_ALL(vs true labels)", "Unseen, model trained\non flipped labels"),
    ]
    models = [("CNN", BLUE), ("RF", ORANGE), ("RFspec_shape", AQUA)]
    names = {"CNN": "CNN (original)", "RF": "RF raw (original)", "RFspec_shape": "RF on spectrum shape (aux.)"}
    fig, ax = plt.subplots(figsize=(10.5, 3.8))
    w = 0.26
    for j, (m, col) in enumerate(models):
        vals = []
        for exp, ts, _ in proto:
            s = r[(r["experiment"] == exp) & (r["model"] == m) & (r["test_set"] == ts)]
            vals.append(s["file_majority_acc"].mean() * 100 if len(s) else float("nan"))
        xs = [i + (j - 1) * (w + 0.02) for i in range(len(proto))]
        ax.bar(xs, vals, width=w, color=col, label=names[m], zorder=3)
        for x, v in zip(xs, vals):
            ax.text(x, v + 1.2, f"{v:.0f}", ha="center", va="bottom", fontsize=7, color=INK2)
    ax.axhline(50, color=INK2, lw=0.8, ls="--", zorder=2)
    ax.text(-0.48, 51, "chance (50%)", fontsize=7, color=INK2, ha="left")
    ax.set_xticks(range(len(proto)))
    ax.set_xticklabels([p[2] for p in proto], fontsize=8)
    ax.set_ylabel("File-level accuracy [%]")
    ax.set_ylim(0, 112)
    ax.legend(loc="upper right", ncol=3, fontsize=8, bbox_to_anchor=(1.0, 1.13))
    ax.set_title("SYNTHETIC data — evaluation-protocol mechanism only, NOT lab performance",
                 fontsize=10, loc="left", pad=22)
    fig.savefig(HERE / "fig_synthetic_protocols.png", dpi=170, bbox_inches="tight")
    plt.close(fig)


def fig_synthetic_gain():
    r = pd.read_csv(DATA / "synthetic_validation_results.csv")
    gains = [0.8, 0.9, 0.95, 1.0, 1.05, 1.1, 1.2]
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    for m, col, mk, lab in [("CNN", BLUE, "o", "CNN (original)"), ("RF", ORANGE, "^", "RF raw (original)"),
                            ("RFspec_shape", AQUA, "s", "RF on spectrum shape (aux.)")]:
        ys = []
        for g in gains:
            if g == 1.0:
                s = r[(r["experiment"] == "E1_within") & (r["model"] == m) & (r["test_set"] == "UNSEEN_ALL")]
            else:
                s = r[(r["experiment"] == "E6_gain") & (r["model"] == m) & (r["test_set"] == f"GAIN_x{g}")]
            ys.append(s["file_majority_acc"].mean() * 100)
        ax.plot(gains, ys, color=col, marker=mk, lw=2, ms=6, label=lab, zorder=3)
        ax.annotate(lab, (gains[-1], ys[-1]), xytext=(6, 0), textcoords="offset points",
                    fontsize=7, color=INK2, va="center")
    ax.set_xlabel("Ripple sensor gain applied to unseen files (1.0 = calibrated)")
    ax.set_ylabel("File-level accuracy [%]")
    ax.set_ylim(40, 105)
    ax.set_xlim(0.78, 1.33)
    ax.legend(loc="lower right", fontsize=7)
    ax.set_title("SYNTHETIC — amplitude-preserving input makes the CNN gain-sensitive", fontsize=9, loc="left")
    fig.savefig(HERE / "fig_synthetic_gain.png", dpi=170, bbox_inches="tight")
    plt.close(fig)


if __name__ == "__main__":
    meta = load_meta()
    fig_operating_points(meta)
    fig_measurement_order(meta)
    fig_synthetic_protocols()
    fig_synthetic_gain()
    print("saved:", sorted(p.name for p in HERE.glob("*.png")))
