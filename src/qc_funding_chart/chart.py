"""Data selection, rendering, and annotations for the funding bubble chart."""

from __future__ import annotations

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import Circle, Ellipse, Polygon

from .regions import COUNTRY_POSITIONS, REGIONS

NAME_COL = "Country / Entity"
VALUE_COL = "highest confidence figure USD Millions"
TYPE_COL = "Type"

EXPECTED_COLUMNS = {
    "Rank", NAME_COL, VALUE_COL, "Type", "ssource-link", "observations",
}

EXCLUDED_ENTITIES = {
    "Confirmed global total", "Europe (confirmed)", "Asia-Pacific (confirmed)",
    "Americas (confirmed)", "European Union (Flagship)",
}

REGION_COLORS = {
    "Americas": "#159bd7",
    "Europe": "#f04462",
    "Asia": "#f28b20",
    "APAC": "#8050d7",
}

LABEL_OFFSETS = {
    "United States": (-22, 3), "Canada": (12, 7), "Brazil": (10, -2),
    "United Kingdom": (-22, 9), "Netherlands": (-12, 14), "Germany": (13, 8),
    "Switzerland": (13, -3), "Austria": (13, -10), "Italy": (-13, -11),
    "Russia": (9, 8), "India": (5, -10), "China": (11, 0),
    "Japan": (8, 7), "South Korea": (11, -6), "Singapore": (8, 0),
    "Australia": (11, 0),
}

REGION_HALOS = {
    "Americas": (-104, 30, 76, 93),
    "Europe": (17, 43, 64, 67),
    "Asia": (94, 36, 104, 78),
    "APAC": (132, -19, 63, 51),
}

REGION_HEADING_POSITIONS = {
    "Americas": (-159, 66), "Europe": (-29, 73), "Asia": (111, 72), "APAC": (151, 0),
}

LEADER_LINE_COUNTRIES = {
    "United Kingdom", "Netherlands", "Germany", "Switzerland", "Austria", "Italy",
    "Canada", "Brazil", "Russia", "India", "South Korea", "Singapore", "Australia",
}

CONTINENTS = [
    [(-168, 70), (-148, 73), (-128, 68), (-117, 60), (-102, 56), (-91, 49), (-82, 25), (-98, 8), (-112, 15), (-126, 28), (-145, 48)],
    [(-53, 82), (-22, 78), (-30, 60), (-47, 58), (-61, 68)],
    [(-81, 12), (-66, 8), (-50, 2), (-35, -8), (-42, -27), (-56, -56), (-68, -35), (-75, -10)],
    [(-12, 70), (10, 72), (32, 67), (48, 61), (70, 60), (94, 56), (119, 52), (145, 48), (165, 35), (148, 19), (130, 5), (111, 9), (92, 21), (73, 28), (57, 38), (40, 35), (27, 44), (10, 42), (-2, 52)],
    [(-17, 35), (10, 37), (33, 25), (42, 5), (29, -18), (17, -35), (4, -34), (-7, -12), (-16, 9)],
    [(63, 30), (82, 27), (95, 10), (110, 5), (120, 18), (105, 28), (87, 34)],
    [(130, 46), (143, 43), (146, 34), (138, 30), (132, 38)],
    [(112, -11), (132, -10), (153, -18), (151, -39), (132, -44), (115, -31)],
    [(47, -13), (51, -16), (49, -26), (46, -22)],
]

FACETS = [
    [(-155, 60), (-128, 68), (-139, 45)], [(-128, 68), (-102, 56), (-115, 40)],
    [(-115, 40), (-102, 56), (-91, 49)], [(-98, 8), (-81, 12), (-68, -5)],
    [(-68, -5), (-50, 2), (-56, -22)], [(-56, -22), (-42, -27), (-56, -56)],
    [(-2, 52), (10, 42), (27, 44)], [(10, 42), (40, 35), (29, 20)],
    [(27, 44), (48, 61), (57, 38)], [(57, 38), (73, 28), (92, 21)],
    [(92, 21), (111, 9), (130, 5)], [(70, 60), (94, 56), (92, 40)],
    [(92, 40), (119, 52), (130, 35)], [(4, -34), (17, -35), (29, -18)],
    [(115, -31), (132, -44), (151, -39)],
]


def fmt_usd_millions(value: float | None) -> str:
    if value is None or pd.isna(value):
        return "no comparable total"
    if value >= 1000:
        return f"${value / 1000:.2f}B"
    return f"${value:.0f}M"


def load_funding_data(csv_path: Path) -> pd.DataFrame:
    if not csv_path.is_file():
        raise FileNotFoundError(f"CSV not found: {csv_path.resolve()}")
    df = pd.read_csv(csv_path, encoding="utf-8-sig")
    missing = EXPECTED_COLUMNS.difference(df.columns)
    if missing:
        raise ValueError(f"CSV is missing expected columns: {sorted(missing)}")
    return df


def select_country_values(df: pd.DataFrame) -> dict[str, float]:
    data = df.copy()
    data[VALUE_COL] = pd.to_numeric(data[VALUE_COL], errors="coerce")

    us_rows = data[data[NAME_COL].eq("United States")]
    us_2024 = us_rows[us_rows[TYPE_COL].astype(str).str.contains("FY2024 enacted", case=False, na=False)]
    selected = data[~data[NAME_COL].eq("United States")].copy()
    if not us_2024.empty:
        selected = pd.concat([selected, us_2024.iloc[[0]]], ignore_index=True)
    else:
        selected = pd.concat([selected, us_rows.iloc[[0]]], ignore_index=True)

    selected = selected[~selected[NAME_COL].isin(EXCLUDED_ENTITIES)]
    return dict(zip(selected[NAME_COL], selected[VALUE_COL]))


def region_total(region: str, country_values: dict[str, float]) -> float:
    members = [
        n for n in REGIONS[region]
        if n != "China" and not pd.isna(country_values.get(n, np.nan))
    ]
    return sum(float(country_values[n]) for n in members)


def create_chart(data_path: Path, output_path: Path) -> Path:
    df = load_funding_data(data_path)
    country_values = select_country_values(df)

    fig = plt.figure(figsize=(19, 12), dpi=170, facecolor="#fbfaf7")
    ax = fig.add_axes([0.035, 0.19, 0.93, 0.63])
    ax.set_facecolor("#fbfaf7")
    ink, muted = "#111b3c", "#59647b"
    ax.set_xlim(-178, 185)
    ax.set_ylim(-59, 83)
    ax.axis("off")

    for lon in [-120, -60, 0, 60, 120]:
        ax.axvline(lon, color="#e8e9ee", lw=0.65, zorder=0)
    for lat in [-30, 0, 30, 60]:
        ax.axhline(lat, color="#e8e9ee", lw=0.65, zorder=0)

    land, coast = "#e4e7eb", "#d2d8e0"
    for coords in CONTINENTS:
        ax.add_patch(Polygon(coords, closed=True, facecolor=land, edgecolor=coast,
                             linewidth=0.75, zorder=1, joinstyle="round"))
    for i, coords in enumerate(FACETS):
        ax.add_patch(Polygon(coords, closed=True,
                             facecolor=("#edf0f3" if i % 2 == 0 else "#dfe4e9"),
                             edgecolor="none", alpha=0.72, zorder=1.1))

    for region, (cx, cy, w, h) in REGION_HALOS.items():
        ax.add_patch(Ellipse((cx, cy), width=w, height=h,
                             facecolor=REGION_COLORS[region], edgecolor=REGION_COLORS[region],
                             linewidth=1.4, alpha=0.105, zorder=1.5))

    for region, (tx, ty) in REGION_HEADING_POSITIONS.items():
        total = region_total(region, country_values)
        ax.text(tx, ty, region, color=REGION_COLORS[region], fontsize=17,
                fontweight="bold", ha="left", va="center", zorder=7)
        ax.text(tx, ty - 5.1, fmt_usd_millions(total), color=REGION_COLORS[region],
                fontsize=15, fontweight="bold", ha="left", va="center", zorder=7)
        ax.text(tx, ty - 8.6, "listed countries" + (", excl. China" if region == "Asia" else ""),
                color=muted, fontsize=8.5, ha="left", va="center", zorder=7)

    available_values = [
        float(v) for n, v in country_values.items()
        if n in COUNTRY_POSITIONS and not pd.isna(v) and n != "China"
    ]
    max_value = max(available_values) if available_values else 1

    for region, countries in REGIONS.items():
        for country in countries:
            if country not in COUNTRY_POSITIONS:
                continue
            x, y = COUNTRY_POSITIONS[country]
            v = country_values.get(country, np.nan)
            color = REGION_COLORS[region]
            dx, dy = LABEL_OFFSETS[country]
            if pd.isna(v):
                ax.scatter([x], [y], s=110, facecolors="none", edgecolors=color,
                           linewidths=1.7, zorder=5)
                ax.annotate(f"{country}\nNo comparable total recorded", (x, y),
                            xytext=(x + dx, y + dy), textcoords="data", fontsize=8.2,
                            color=ink, ha="left" if dx >= 0 else "right", va="center",
                            arrowprops=dict(arrowstyle="-", color=color, lw=0.9),
                            zorder=8)
                continue
            if country == "China":
                radius = 8.3
            else:
                radius = 1.5 + 7.6 * math.sqrt(float(v) / max_value)
            ax.add_patch(Circle((x, y), radius=radius, facecolor=color,
                                edgecolor=color, linewidth=1.4, alpha=0.76, zorder=4))
            label_value = "≈$15B cumulative*" if country == "China" else fmt_usd_millions(float(v))
            if country in LEADER_LINE_COUNTRIES:
                ax.annotate(f"{country}\n{label_value}", (x, y), xytext=(x + dx, y + dy),
                            textcoords="data", fontsize=8.7, color=ink,
                            fontweight="bold", ha="left" if dx >= 0 else "right", va="center",
                            arrowprops=dict(arrowstyle="-", color=color, lw=0.9,
                                            shrinkA=1, shrinkB=2), zorder=8)
            else:
                ax.annotate(f"{country}\n{label_value}", (x, y), xytext=(x + dx, y + dy),
                            textcoords="data", fontsize=9.4, color=ink,
                            fontweight="bold", ha="left" if dx >= 0 else "right", va="center",
                            arrowprops=dict(arrowstyle="-", color=color, lw=1.0,
                                            shrinkA=1, shrinkB=2), zorder=8)

    fig.text(0.045, 0.945, "ESTIMATED PUBLIC FUNDING FOR QUANTUM TECHNOLOGIES",
             fontsize=23, fontweight="bold", color=ink, ha="left")
    fig.text(0.045, 0.908, "2026 snapshot", fontsize=20, fontweight="bold",
             color=ink, ha="left")
    fig.text(0.045, 0.878, "Estimated annual or annualized public funding (USD millions)",
             fontsize=12.5, color=muted, ha="left")
    fig.text(0.045, 0.855, "Multi-year budgets annualized where possible; figures are approximate.",
             fontsize=10, color=muted, ha="left")

    legend_ax = fig.add_axes([0.79, 0.845, 0.17, 0.12])
    legend_ax.set_xlim(0, 10)
    legend_ax.set_ylim(0, 10)
    legend_ax.axis("off")
    legend_ax.text(0.0, 9.5, "Bubble size guide", fontsize=9, color=muted, weight="bold")
    for r, label, yy in [(2.25, "$1B", 6.6), (1.55, "$250M", 3.6), (0.85, "$50M", 1.3)]:
        legend_ax.add_patch(Circle((3.0, yy), r, facecolor="none", edgecolor="#7d8798", lw=0.9))
        legend_ax.text(6.0, yy, label, fontsize=8.5, color=muted, va="center")

    listed_annual_total = sum(
        float(country_values[n]) for members in REGIONS.values() for n in members
        if n != "China" and not pd.isna(country_values.get(n, np.nan))
    )
    fig.text(0.045, 0.145, "WORLD TOTAL", fontsize=10, color=muted, weight="bold")
    fig.text(0.045, 0.108, f"≈ ${listed_annual_total / 1000:.2f}B per year",
             fontsize=22, color=ink, weight="bold")
    fig.text(0.045, 0.083, "Sum of listed annual / annualized country figures; China excluded.",
             fontsize=8.5, color=muted)

    legend_y = 0.145
    for (region, color), x in zip(REGION_COLORS.items(), [0.36, 0.49, 0.62, 0.75]):
        fig.patches.append(Circle((x, legend_y), radius=0.008, transform=fig.transFigure,
                                  facecolor=color, edgecolor=color, alpha=0.85))
        fig.text(x + 0.014, legend_y + 0.006, region, fontsize=9, color=ink, weight="bold",
                 ha="left", va="center")
        fig.text(x + 0.014, legend_y - 0.018, fmt_usd_millions(region_total(region, country_values)),
                 fontsize=9, color=color, weight="bold", ha="left", va="center")

    fig.text(0.045, 0.045,
             "Sources: U.S. NQI Annual Report FY2025; McKinsey quantum landscape; national strategy and ministry sources; The Quantum Insider.",
             fontsize=7.8, color=muted, ha="left")
    fig.text(0.045, 0.027,
             "Notes: multi-year commitments are annualized estimates, not necessarily annual appropriations or actual expenditure; regional sums include only listed country rows.",
             fontsize=7.4, color=muted, ha="left")
    fig.text(0.58, 0.027,
             "China: ~US$15B cumulative estimate through 2024, high uncertainty; not comparable to annual figures and excluded from totals.",
             fontsize=7.4, color=muted, ha="left")
    fig.text(0.955, 0.073, "Albert Gruning", fontsize=17, color="#242b3b",
             fontstyle="italic", ha="right")
    fig.text(0.955, 0.052, "R&D tech specialist at Qimono (TM)", fontsize=7.7,
             color=muted, ha="right")
    fig.text(0.955, 0.035, "Original report for MIT", fontsize=7.7,
             color=muted, ha="right")

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=170, facecolor=fig.get_facecolor())
    plt.close(fig)
    return output_path
