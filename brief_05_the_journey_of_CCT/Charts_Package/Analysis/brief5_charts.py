"""
Brief 5 chart generation.
Four charts at 300 DPI in the established editorial palette.
Palette matches Briefs 3 and 4 (ink, burnt, amber, cream, red, greys).

Output PNGs: charts/01_transfer_adequacy.png, 02_coverage_share.png,
             03_real_value_trajectory.png, 05_outcome_hierarchy.png
Data source: charts/data/chart{N}_*.csv
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.ticker import PercentFormatter

# ================================================================
# PALETTE (same as Briefs 3 and 4)
# ================================================================
INK      = "#14171a"
BURNT    = "#c05621"
AMBER    = "#d69e2e"
CREAM    = "#faf7f2"
PAPER    = "#ffffff"
RED      = "#a83232"
GREY_DK  = "#4a4a4a"
GREY_MD  = "#8a8a8a"
GREY_LT  = "#cfcfcf"

DPI = 300
BASE = Path(__file__).resolve().parent
DATA = BASE / "data"
OUT  = BASE

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.edgecolor": INK,
    "axes.labelcolor": INK,
    "xtick.color": INK,
    "ytick.color": INK,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.titleweight": "bold",
    "axes.titlelocation": "left",
    "figure.facecolor": PAPER,
    "axes.facecolor": PAPER,
    "savefig.facecolor": PAPER,
    "savefig.bbox": "tight",
    "savefig.dpi": DPI,
})


def _title_block(ax, title, subtitle=None):
    """Standard title block: bold title left-aligned; subtitle grey below."""
    ax.set_title(title, fontsize=14, color=INK, pad=18, loc="left")
    if subtitle:
        ax.text(0, 1.02, subtitle, transform=ax.transAxes,
                fontsize=10, color=GREY_DK, ha="left", va="bottom")


def _source_line(fig, text):
    """Small source line at bottom-left."""
    fig.text(0.02, 0.005, text, fontsize=7.5, color=GREY_MD, ha="left")


# ================================================================
# CHART 1: Transfer adequacy across programmes
# ================================================================
def chart_1_transfer_adequacy():
    df = pd.read_csv(DATA / "chart1_transfer_adequacy.csv")
    df = df.sort_values("transfer_usd_month", ascending=True).reset_index(drop=True)

    # Label combines programme + country
    df["label"] = df["programme"] + " (" + df["country"] + ")"

    # Colour rule: above threshold amber; below threshold burnt; Nigeria highlighted red
    THRESHOLD_USD = 20
    def _bar_color(row):
        if "Nigeria" in row["country"]:
            return RED
        return AMBER if row["transfer_usd_month"] >= THRESHOLD_USD else BURNT
    colors = df.apply(_bar_color, axis=1).tolist()

    fig, ax = plt.subplots(figsize=(10.5, 6.5))
    bars = ax.barh(df["label"], df["transfer_usd_month"], color=colors,
                   edgecolor=INK, linewidth=0.6)

    # Reference line at USD 20 adequacy threshold
    ax.axvline(THRESHOLD_USD, color=INK, linestyle="--", linewidth=1.2, alpha=0.75)
    ax.text(THRESHOLD_USD + 1.5, len(df) - 0.4,
            "Adequacy threshold\n(20% of consumption,\nBastagli et al. 2016)",
            fontsize=8.5, color=INK, va="top")

    # Value labels at bar end
    for i, (v, lab) in enumerate(zip(df["transfer_usd_month"], df["label"])):
        ax.text(v + 1, i, f"USD {v:.1f}", va="center", fontsize=8.5, color=INK)

    # Annotation on Nigeria NASSP-HUP real 2026
    real_row = df.index[df["programme"] == "NASSP-HUP real 2026"]
    if len(real_row):
        idx = real_row[0]
        ax.annotate(
            "Real value 2026, below USD 4",
            xy=(df.at[idx, "transfer_usd_month"], idx),
            xytext=(35, idx - 0.05),
            fontsize=8.5, color=RED,
            arrowprops=dict(arrowstyle="->", color=RED, lw=0.8),
        )

    ax.set_xlabel("USD per household per month", fontsize=10, color=INK)
    ax.set_xlim(0, max(df["transfer_usd_month"].max() + 25, 80))
    ax.set_ylabel("")
    ax.tick_params(axis="y", labelsize=9)
    ax.grid(axis="x", color=GREY_LT, linewidth=0.5, alpha=0.6)
    ax.set_axisbelow(True)

    _title_block(ax,
        "Transfer size across CCT programmes, USD per household per month",
        "Nigeria's NASSP-HUP sits below the adequacy threshold. Real value in 2026 is below USD 4.")

    # Legend
    handles = [
        mpatches.Patch(color=AMBER, label="At or above adequacy threshold"),
        mpatches.Patch(color=BURNT, label="Below adequacy threshold"),
        mpatches.Patch(color=RED,   label="Nigeria (NASSP-HUP and COPE)"),
    ]
    ax.legend(handles=handles, loc="lower right", frameon=False, fontsize=8.5)

    _source_line(fig,
        "Source: Brief 5 country sources (Bastagli et al. 2016; F1 Fiszbein & Schady 2009; "
        "F4a IEG 2024; UNICEF Transfer Project). Values are nominal at last documented year.")
    plt.savefig(OUT / "01_transfer_adequacy.png")
    plt.close()
    print("Wrote 01_transfer_adequacy.png")


# ================================================================
# CHART 2: Coverage as share of population
# ================================================================
def chart_2_coverage_share():
    df = pd.read_csv(DATA / "chart2_coverage_share.csv")
    df = df.sort_values("population_share_pct", ascending=True).reset_index(drop=True)
    df["label"] = df["programme"] + " (" + df["country"] + ")"

    # Nigeria bars distinguished
    def _bar_color(row):
        if "achieved" in row["programme"]:
            return RED
        if "target" in row["programme"]:
            return AMBER  # aspirational
        return INK
    colors = df.apply(_bar_color, axis=1).tolist()
    # For target bar, use hatched style via edgecolor
    edgecolors = [
        AMBER if "target" in p else INK for p in df["programme"]
    ]

    fig, ax = plt.subplots(figsize=(10.5, 6.5))
    bars = ax.barh(df["label"], df["population_share_pct"], color=colors,
                   edgecolor=edgecolors, linewidth=1.0)

    # Value labels
    for i, v in enumerate(df["population_share_pct"]):
        ax.text(v + 0.6, i, f"{v:.0f}%", va="center", fontsize=8.5, color=INK)

    # Callout on Nigeria achieved
    achieved_idx = df.index[df["programme"] == "NASSP-HUP achieved"]
    if len(achieved_idx):
        idx = achieved_idx[0]
        ax.annotate(
            "1.8M households, below 2%",
            xy=(df.at[idx, "population_share_pct"], idx),
            xytext=(15, idx - 0.05),
            fontsize=8.5, color=RED,
            arrowprops=dict(arrowstyle="->", color=RED, lw=0.8),
        )

    ax.set_xlabel("Share of national population covered (%)", fontsize=10, color=INK)
    ax.xaxis.set_major_formatter(PercentFormatter(decimals=0))
    ax.set_xlim(0, max(df["population_share_pct"].max() + 10, 70))
    ax.set_ylabel("")
    ax.tick_params(axis="y", labelsize=9)
    ax.grid(axis="x", color=GREY_LT, linewidth=0.5, alpha=0.6)
    ax.set_axisbelow(True)

    _title_block(ax,
        "Cash transfer coverage as share of national population",
        "Nigeria's achieved coverage sits with Ghana and Kenya. The scale-up target would move it toward the Latin American range.")

    handles = [
        mpatches.Patch(color=INK,   label="Other programmes"),
        mpatches.Patch(color=RED,   label="Nigeria NASSP-HUP achieved"),
        mpatches.Patch(color=AMBER, label="Nigeria NASSP-SU target (aspirational)"),
    ]
    ax.legend(handles=handles, loc="lower right", frameon=False, fontsize=8.5)

    _source_line(fig,
        "Source: Brief 5 country sources; F4a IEG 2024; F4b NASSP-SU PAD 2024. "
        "JSY shown as annual flow (one-time payment per delivery).")
    plt.savefig(OUT / "02_coverage_share.png")
    plt.close()
    print("Wrote 02_coverage_share.png")


# ================================================================
# CHART 3: Nigeria real-value trajectory versus comparators
# ================================================================
def chart_3_real_value_trajectory():
    df = pd.read_csv(DATA / "chart3_real_value_trajectory.csv")

    fig, ax = plt.subplots(figsize=(10.5, 6.5))

    # Comparators, muted
    ax.plot(df["year"], df["ct_ovc_kenya"],
            color=GREY_DK, linewidth=1.6, linestyle="-",
            label="Kenya CT-OVC (indexed)")
    ax.plot(df["year"], df["bolsa_brazil"],
            color=BURNT, linewidth=1.6, linestyle=":",
            label="Brazil Bolsa Familia")
    ax.plot(df["year"], df["leap_ghana"],
            color=GREY_MD, linewidth=1.6, linestyle="--",
            label="Ghana LEAP")
    ax.plot(df["year"], df["prospera_mexico"],
            color=AMBER, linewidth=1.6, linestyle="-.",
            label="Mexico Prospera (replaced 2019)")

    # Nigeria, thick red line
    ax.plot(df["year"], df["nassp_hup_nigeria"],
            color=RED, linewidth=3.2, marker="o", markersize=5,
            label="Nigeria NASSP-HUP")

    # Adequacy threshold reference
    ax.axhline(20, color=INK, linestyle="--", linewidth=1.0, alpha=0.6)
    ax.text(2016, 21, "Adequacy threshold (USD 20)",
            fontsize=8.5, color=INK, va="bottom")

    # Annotations
    ax.annotate("Nigeria set NGN 5,000 in 2016.\nNo indexation clause.",
                xy=(2016, 12.17), xytext=(2016.4, 30),
                fontsize=8.5, color=RED,
                arrowprops=dict(arrowstyle="->", color=RED, lw=0.8))

    ax.annotate("January 2024 suspension, 12.5 months",
                xy=(2024, 4.2), xytext=(2020.5, 12),
                fontsize=8.5, color=RED,
                arrowprops=dict(arrowstyle="->", color=RED, lw=0.8))

    ax.annotate("Lula restructuring (Bolsa)",
                xy=(2023, 42), xytext=(2019.5, 48),
                fontsize=8.5, color=BURNT,
                arrowprops=dict(arrowstyle="->", color=BURNT, lw=0.8))

    ax.set_xlabel("Year", fontsize=10, color=INK)
    ax.set_ylabel("Real transfer value, USD per household per month\n(2016 base year)",
                  fontsize=10, color=INK)
    ax.set_xlim(2015.5, 2026.5)
    ax.set_ylim(0, 60)
    ax.grid(axis="both", color=GREY_LT, linewidth=0.5, alpha=0.6)
    ax.set_axisbelow(True)

    _title_block(ax,
        "Real-value trajectory of cash transfers, 2016 to 2026",
        "Nigeria's NASSP-HUP shows a monotone decline unmatched by any comparator.")

    ax.legend(loc="upper right", frameon=False, fontsize=8.5)

    _source_line(fig,
        "Source: Brief 5 country sources; NBS Food CPI; F4a IEG 2024; F4b NASSP-SU PAD 2024. "
        "Values estimated where indexation not documented.")
    plt.savefig(OUT / "03_real_value_trajectory.png")
    plt.close()
    print("Wrote 03_real_value_trajectory.png")


# ================================================================
# CHART 5: Outcome hierarchy (evidence strength by domain)
# ================================================================
def chart_5_outcome_hierarchy():
    df = pd.read_csv(DATA / "chart5_outcome_hierarchy.csv")
    df = df.sort_values("evidence_strength_score", ascending=True).reset_index(drop=True)

    # Colour by strength (4=amber, 3=amber, 2=burnt, 1=red)
    color_map = {4: AMBER, 3: AMBER, 2: BURNT, 1: RED}
    colors = [color_map[s] for s in df["evidence_strength_score"]]

    fig, ax = plt.subplots(figsize=(12.5, 6.2))
    bars = ax.barh(df["outcome_domain"], df["evidence_strength_score"],
                   color=colors, edgecolor=INK, linewidth=0.6, height=0.55)

    # Effect summary at bar end (short, no strength prefix)
    for i, row in df.iterrows():
        # Truncate effect range for readability
        eff = row["effect_size_range"]
        if len(eff) > 68:
            eff = eff[:65] + "..."
        ax.text(row["evidence_strength_score"] + 0.08, i, "  " + eff,
                va="center", fontsize=9, color=INK)

    # Nigeria targets indicator placed FAR RIGHT, outside bar zone, coloured
    NIGERIA_COL_X = 8.9  # right of bar zone
    for i, row in df.iterrows():
        v = row["nigeria_targets_this"]
        if v == "yes":
            ax.text(NIGERIA_COL_X, i, "★ Nigeria targets this domain",
                    va="center", fontsize=9, color=RED, ha="left", weight="bold")
        elif v == "partial":
            ax.text(NIGERIA_COL_X, i, "◐ Nigeria targets partially",
                    va="center", fontsize=9, color=BURNT, ha="left")
        else:
            ax.text(NIGERIA_COL_X, i, "○ Not targeted by Nigeria",
                    va="center", fontsize=9, color=GREY_MD, ha="left")

    ax.set_xlim(0, 14.5)
    ax.set_xticks([])
    ax.set_ylabel("")
    ax.tick_params(axis="y", labelsize=10.5)
    ax.spines["bottom"].set_visible(False)
    ax.spines["left"].set_color(INK)

    _title_block(ax,
        "CCT effect hierarchy by outcome domain",
        "Nigeria's NASSP-HUP targets education access and health utilisation, the two domains where the instrument works most.")

    handles = [
        mpatches.Patch(color=AMBER, label="Strong evidence base"),
        mpatches.Patch(color=BURNT, label="Moderate evidence base"),
        mpatches.Patch(color=RED,   label="Weakest evidence base"),
    ]
    ax.legend(handles=handles, loc="lower right", frameon=False, fontsize=8.5)

    _source_line(fig,
        "Source: Brief 5 Section 10A synthesis of Bastagli et al. 2016, "
        "Baird et al. 2011, and country-level evidence tabulated in the source matrix.")
    plt.savefig(OUT / "05_outcome_hierarchy.png")
    plt.close()
    print("Wrote 05_outcome_hierarchy.png")


if __name__ == "__main__":
    chart_1_transfer_adequacy()
    chart_2_coverage_share()
    chart_3_real_value_trajectory()
    chart_5_outcome_hierarchy()
    print("\nAll charts saved to:", OUT)
