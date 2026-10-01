"""
3D operating-condition map (Train vs Unseen/Test) for train80.py.

- Axes cross at the nominal point (f0 = 60 Hz, fsw = 8 kHz, V = 100 V).
- Each axis has one arrowhead at its END, pointing in the increasing direction.
- To spread the crowded test region, each half-axis uses a signed power scale
  (SPREAD_GAMMA < 1 expands the region near nominal). Tick labels show real values.
  Set SPREAD_GAMMA = 1.0 for a plain linear (piecewise) scale.
- Points at the same (f0, fsw, V) (e.g. 10/22/47 ohm at nominal) are fanned out
  around the true position and tied back with a leader line.
- Every point has an ID; the table on the right lists the actual values.

The condition list mirrors CONDITION_EXPERIMENTS / TWO_CONDITION_* /
THREE_CONDITION_TEST_FILES in train80.py (normal/aged pairs share one point).
Single-condition files have no load_resistance_ohm in train80.py; their R is
set here from the experiment notes (R1 = 47, R4 = 10, others = 22 ohm).
"""

import os
from collections import OrderedDict

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

# ----------------------------------------------------------------------------
# Settings
# ----------------------------------------------------------------------------
OUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "3d_projection.png")
SPREAD_GAMMA = 0.6          # 1.0 = linear, < 1 spreads points near nominal
VIEW_ELEV, VIEW_AZIM = 22, -150   # viewed from the f0 = 30 Hz / fsw = 2 kHz quadrant
STACK_SIZES = (1900, 560, 150)    # marker sizes for points sharing one position (back -> front)
STACK_LABEL_OFFSET = np.array([0.0, 0.30, 0.50])    # label placed in empty space + leader line
LABEL_SIDE = {}                   # per-ID label position override: "left"/"right" (default: above)

NOMINAL = {"f0": 60.0, "fsw": 8.0, "V": 100.0}          # Hz, kHz, V
AXIS_RANGE = {"f0": (30.0, 90.0), "fsw": (2.0, 14.0), "V": (50.0, 200.0)}
AXIS_TICKS = {
    "f0": [30, 40, 45, 50, 90],
    "fsw": [2, 4, 5, 6, 7, 14],
    "V": [50, 110, 125, 135, 150, 200],
}
AXIS_LABEL = {"f0": "f0 [Hz]", "fsw": "fsw [kHz]", "V": "Output fundamental voltage [V]"}

SPLIT_COLOR = {"Train": "#1f77b4", "Unseen/Test": "#ff7f0e"}
R_MARKER = OrderedDict([(10, "o"), (22, "s"), (32, "^"), (47, "*")])
R_SIZE = {10: 150, 22: 130, 32: 160, 47: 320}   # stacking order uses this ranking

# (split, f0 [Hz], fsw [kHz], V [V], R [ohm], group, file keys normal/aged)
CONDITIONS = [
    # --- 1-condition TRAIN (CONDITION_EXPERIMENTS train_files) ---
    ("Train", 60, 14, 100, 22, "fsw1", "tek0228/0219"),
    ("Train", 60, 2, 100, 22, "fsw4", "tek0127/0135"),
    ("Train", 90, 8, 100, 22, "f0_1", "tek0227/0220"),
    ("Train", 30, 8, 100, 22, "f0_4", "tek0128/0133"),
    ("Train", 60, 8, 50, 22, "v_1", "tek0129/0132"),
    ("Train", 60, 8, 200, 22, "v_4", "tek0226/0223"),
    ("Train", 60, 8, 100, 47, "R1", "tek0225/0224"),
    ("Train", 60, 8, 100, 10, "R4", "tek0138/0137"),
    # --- 2-condition outer TRAIN ---
    ("Train", 40, 4, 100, 32, "2c outer1", "tek0163/0173"),
    ("Train", 40, 8, 135, 32, "2c outer2", "tek0164/0174"),
    ("Train", 60, 4, 135, 32, "2c outer3", "tek0165/0175"),
    # --- 1-condition UNSEEN ---
    ("Unseen/Test", 60, 8, 100, 22, "reference, R3", "tek0017/0041, tek0025/0033"),
    ("Unseen/Test", 60, 5, 100, 22, "fsw3", "tek0021/0045"),
    ("Unseen/Test", 45, 8, 100, 22, "f0_3", "tek0126/0134"),
    ("Unseen/Test", 60, 8, 125, 22, "v_3", "tek0152/0161"),
    # --- 2-condition TEST ---
    ("Unseen/Test", 45, 5, 100, 32, "2c case1, case7", "tek0153/0150, tek0170/0180"),
    ("Unseen/Test", 50, 6, 100, 32, "2c case2", "tek0234/0237"),
    ("Unseen/Test", 45, 8, 125, 32, "2c case3, case8", "tek0154/0151, tek0171/0181"),
    ("Unseen/Test", 50, 8, 115, 32, "2c case4", "tek0146/0159"),
    ("Unseen/Test", 60, 5, 125, 32, "2c case5, case9", "tek0143/0157, tek0172/0182"),
    ("Unseen/Test", 60, 6, 115, 32, "2c case6", "tek0145/0160"),
    # --- 3-condition TEST ---
    ("Unseen/Test", 50, 6, 110, 32, "3c case1", "tek0166/0176"),
    ("Unseen/Test", 50, 7, 115, 32, "3c case2", "tek0167/0177"),
    ("Unseen/Test", 45, 6, 120, 32, "3c case3", "tek0168/0178"),
    ("Unseen/Test", 45, 5, 125, 32, "3c case4", "tek0169/0179"),
]


# ----------------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------------
def to_norm(key, value):
    """Real value -> normalized axis coordinate (nominal = 0, range ends = +-1)."""
    lo, hi = AXIS_RANGE[key]
    nom = NOMINAL[key]
    t = (value - nom) / ((hi - nom) if value >= nom else (nom - lo))
    return np.sign(t) * np.abs(t) ** SPREAD_GAMMA


class Arrow3D(FancyArrowPatch):
    """Arrow drawn in 3D data coords; the head is rendered in screen space."""

    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
        xs3d, ys3d, zs3d = self._verts3d
        xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        return np.min(zs)


def main():
    plt.rcParams.update({"font.size": 10})
    fig = plt.figure(figsize=(16, 10), dpi=150)
    ax = fig.add_axes([0.0, 0.02, 0.66, 0.92], projection="3d")
    ax.set_proj_type("ortho")
    ax.view_init(elev=VIEW_ELEV, azim=VIEW_AZIM)
    ax.set_axis_off()
    ax.computed_zorder = False

    L = 1.30  # axis half-length in normalized units (range ends are at +-1)
    lim = 1.42
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(-lim, lim)
    ax.set_box_aspect((1, 1, 1), zoom=1.45)

    # ---- axes: x = f0, y = fsw, z = V -----------------------------------
    axis_dirs = {"f0": np.array([1, 0, 0]), "fsw": np.array([0, 1, 0]), "V": np.array([0, 0, 1])}
    for key, d in axis_dirs.items():
        p0, p1 = -L * d, L * d
        ax.plot(*zip(p0, p1), color="0.25", lw=1.6, zorder=1)
        arrow = Arrow3D(*zip(0.97 * p1, 1.14 * p1), mutation_scale=22, lw=1.6,
                        arrowstyle="-|>", color="0.2", shrinkA=0, shrinkB=0)
        ax.add_artist(arrow)
        if key == "V":
            ax.text(*(1.12 * p1 + np.array([0.12, -0.12, 0])), AXIS_LABEL[key], fontsize=13,
                    fontweight="bold", ha="left", va="center")
        else:
            ax.text(*(1.30 * p1), AXIS_LABEL[key], fontsize=13, fontweight="bold",
                    ha="center", va="center")

        # ticks (range ends + selected values + nominal)
        ticks = sorted(set(AXIS_TICKS[key]) | {AXIS_RANGE[key][0], AXIS_RANGE[key][1]})
        perp = np.array([0, 0, 1]) if key != "V" else np.array([1, -1, 0]) / np.sqrt(2)
        for tv in ticks:
            c = to_norm(key, tv) * d
            ax.plot(*zip(c - 0.025 * perp, c + 0.025 * perp), color="0.25", lw=1.2)
            if key == "V":  # right of the axis, clear of the markers on it
                ax.text(*(c + np.array([0.06, -0.06, 0])), f"{tv:g}", fontsize=8.5,
                        color="0.2", ha="left", va="center")
            else:
                ax.text(*(c - 0.075 * perp), f"{tv:g}", fontsize=8.5, color="0.2",
                        ha="center", va="top")

    
    # ---- points -------------------------------------------------------------
    groups = OrderedDict()
    for idx, row in enumerate(CONDITIONS, start=1):
        split, f0, fsw, v, r = row[:5]
        key = (f0, fsw, v)
        groups.setdefault(key, []).append((idx, row))

    for (f0, fsw, v), members in groups.items():
        base = np.array([to_norm("f0", f0), to_norm("fsw", fsw), to_norm("V", v)])

        # vertical projection line to the V = nominal plane + foot marker
        if abs(base[2]) > 1e-9:
            ax.plot([base[0]] * 2, [base[1]] * 2, [0, base[2]],
                    ls="--", lw=0.9, color="0.45", zorder=2)
        if abs(base[0]) > 1e-9 and abs(base[1]) > 1e-9:
            ax.plot([base[0], base[0]], [0, base[1]], [0, 0], ls=":", lw=0.8, color="0.6")
            ax.plot([0, base[0]], [base[1], base[1]], [0, 0], ls=":", lw=0.8, color="0.6")
        if abs(base[2]) > 1e-9 or (abs(base[0]) > 1e-9 and abs(base[1]) > 1e-9):
            ax.scatter(*base[:2], 0, s=10, color="0.45", zorder=3)

        if len(members) > 1:
            members = sorted(members, key=lambda m: -R_SIZE[m[1][4]])
            # same position: stack at the true point, largest behind -> smallest in front
            for k, (idx, (split, _, _, _, r, _, _)) in enumerate(members):
                ax.scatter(*base, s=STACK_SIZES[k], marker=R_MARKER[r], color=SPLIT_COLOR[split],
                           edgecolor="k", linewidth=1.2, depthshade=False, zorder=6 + k)
            ids = ", ".join(str(idx) for idx, _ in members)
            if not base.any():
                ids += "\n(nominal 60 Hz / 8 kHz / 100 V)"
            lbl = base + STACK_LABEL_OFFSET
            ax.plot(*zip(base, lbl), color="0.35", lw=0.8, zorder=5)
            ax.text(*lbl, ids, fontsize=8.5, fontweight="bold",
                    ha="right", va="bottom", zorder=10,
                    bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none", alpha=0.75))
            continue

        idx, (split, _, _, _, r, _, _) = members[0]
        ax.scatter(*base, s=R_SIZE[r], marker=R_MARKER[r], color=SPLIT_COLOR[split],
                   edgecolor="k", linewidth=1.0, depthshade=False, zorder=6)
        side = LABEL_SIDE.get(idx, "top")
        if side == "right":
            lpos, ha, va = base + np.array([0.09, 0.09, 0]), "left", "center"
        elif side == "left":
            lpos, ha, va = base + np.array([-0.07, 0.07, 0]), "right", "center"
        else:
            lpos, ha, va = base + np.array([0, 0, 0.075]), "center", "bottom"
        ax.text(*lpos, str(idx), fontsize=8.5, fontweight="bold", ha=ha, va=va, zorder=7,
                bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none", alpha=0.75))

    # ---- legends --------------------------------------------------------------
    split_handles = [Line2D([], [], marker="o", ls="", markersize=10, markerfacecolor=c,
                            markeredgecolor="k", label=s) for s, c in SPLIT_COLOR.items()]
    r_handles = [Line2D([], [], marker=m, ls="", markersize=11 if r != 47 else 14,
                        markerfacecolor="lightgray", markeredgecolor="k",
                        label=f"R = {r} Ω") for r, m in R_MARKER.items()]
    leg1 = fig.legend(handles=split_handles, title="Data split", loc="upper left",
                      bbox_to_anchor=(0.01, 0.93), frameon=True)
    fig.legend(handles=r_handles, title="Load resistance", loc="upper left",
               bbox_to_anchor=(0.01, 0.80), frameon=True)
    fig.add_artist(leg1)

    # ---- condition table --------------------------------------------------------
    tax = fig.add_axes([0.63, 0.04, 0.36, 0.88])
    tax.set_axis_off()
    cells, colors = [], []
    for idx, (split, f0, fsw, v, r, name, _) in enumerate(CONDITIONS, start=1):
        cells.append([str(idx), "Train" if split == "Train" else "Test",
                      f"{f0:g}", f"{fsw:g}", f"{v:g}", f"{r:g}", name])
        tint = "#dbe8f5" if split == "Train" else "#ffe6cc"
        colors.append([tint] * 7)
    table = tax.table(cellText=cells, cellColours=colors,
                      colLabels=["ID", "Split", "f0\n[Hz]", "fsw\n[kHz]", "V\n[V]", "R\n[Ω]", "Condition"],
                      colWidths=[0.07, 0.11, 0.1, 0.1, 0.1, 0.09, 0.43],
                      loc="upper center", cellLoc="center")
    table.auto_set_font_size(False)
    table.set_fontsize(8.5)
    table.scale(1, 1.32)
    for (row, col), cell in table.get_celld().items():
        cell.set_edgecolor("0.75")
        if row == 0:
            cell.set_facecolor("0.9")
            cell.set_text_props(fontweight="bold")
        if col == 6 and row > 0:
            cell.set_text_props(ha="left")
            cell.PAD = 0.03

    scale_note = ("linear" if SPREAD_GAMMA == 1.0
                  else f"each half-axis scaled |x|^{SPREAD_GAMMA:g} around nominal to spread points")
    fig.suptitle("3D Operating Conditions (Train vs Unseen/Test)", fontsize=17, y=0.975)
    fig.text(0.33, 0.925, f"Axes cross at nominal (60 Hz, 8 kHz, 100 V); {scale_note}. "
             "Dashed: projection onto V = 100 V plane.", ha="center", fontsize=9, color="0.35")

    fig.savefig(OUT_PATH, bbox_inches="tight", facecolor="white")
    print(f"saved: {OUT_PATH}")


if __name__ == "__main__":
    main()
