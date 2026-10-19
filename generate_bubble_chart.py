#!/usr/bin/env python3
"""
Generate the 2026 geographic bubble chart of public quantum-technology funding.

Based on the latest project CSV. Bubble sizes scale with annual or annualized
figures. Positions are approximate geographic locations. China is shown as a
special exception (cumulative estimate, different visual treatment).
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Polygon
import numpy as np

# Load data
df = pd.read_csv("assets/quantum_funding_updated.csv")

# Annual / annualized country-level figures (US = FY2024 enacted)
values = {
    "United States": 1006,
    "Canada": 38.5,
    "Brazil": 5.5,
    "United Kingdom": 330,
    "Germany": 848,
    "Netherlands": 85,
    "Switzerland": 23,
    "Austria": 24,
    "Italy": 36,
    "India": 90,
    "South Korea": 140,
    "Japan": 241,
    "Singapore": 44,
    "Australia": None,
    "China": 15000,  # special cumulative estimate
}

# Approximate geographic positions (longitude-like x, latitude-like y)
pos = {
    "Canada": (-105, 57),
    "United States": (-99, 37),
    "Brazil": (-52, -10),
    "United Kingdom": (-3, 54),
    "Netherlands": (5, 53),
    "Germany": (11, 51),
    "Switzerland": (8, 47),
    "Austria": (14, 47),
    "Italy": (12, 42),
    "India": (79, 22),
    "South Korea": (128, 36),
    "Japan": (139, 37),
    "Singapore": (104, 1.3),
    "Australia": (134, -25),
    "China": (105, 35),
}

label_pos = {
    "Canada": (-119, 64),
    "United States": (-115, 25),
    "Brazil": (-60, -22),
    "United Kingdom": (-18, 66),
    "Netherlands": (-5, 68),
    "Germany": (24, 58),
    "Switzerland": (-8, 38),
    "Austria": (25, 38),
    "Italy": (8, 30),
    "India": (65, 12),
    "South Korea": (148, 46),
    "Japan": (152, 28),
    "Singapore": (112, -8),
    "Australia": (145, -38),
    "China": (118, 48),
}

def main():
    fig, ax = plt.subplots(figsize=(16, 9), dpi=180)
    fig.patch.set_facecolor("#fbfaf6")
    ax.set_facecolor("#fbfaf6")

    # Subtle grid
    for x in [-120, -60, 0, 60, 120]:
        ax.axvline(x, color="#e8e4db", lw=0.8, zorder=0)
    for y in [-30, 0, 30, 60]:
        ax.axhline(y, color="#e8e4db", lw=0.8, zorder=0)

    # Simplified continent outlines
    continents = [
        [(-165, 72), (-135, 72), (-110, 65), (-95, 55), (-82, 50), (-75, 35), (-100, 10), (-120, 20), (-145, 45)],
        [(-80, 12), (-50, 8), (-35, -10), (-45, -35), (-60, -55), (-72, -25)],
        [(-10, 70), (35, 70), (65, 60), (100, 55), (140, 50), (160, 35), (130, 5), (100, 10), (70, 25), (45, 35), (25, 45), (5, 40), (-10, 55)],
        [(112, -12), (153, -15), (154, -38), (130, -45), (114, -30)],
    ]
    for coords in continents:
        ax.add_patch(Polygon(coords, closed=True, facecolor="#eeece5", edgecolor="#d8d4ca", linewidth=1.0, zorder=1))

    # Bubbles
    max_v = max(v for v in values.values() if v is not None and v < 5000)
    for country, v in values.items():
        if country not in pos:
            continue
        x, y = pos[country]
        if v is None:
            ax.scatter([x], [y], s=120, marker="o", facecolors="none", edgecolors="#6b7280",
                       linewidths=1.8, zorder=4)
            continue
        if country == "China":
            radius = 8.5
            color = "#f6e8d4"
            edge = "#b96b26"
            alpha = 0.85
        else:
            radius = 2.2 + 9.5 * np.sqrt(v / max_v)
            color = "#69c7d7"
            edge = "#00a9c0"
            alpha = 0.72
        ax.add_patch(Circle((x, y), radius=radius, facecolor=color, edgecolor=edge,
                            linewidth=1.6, alpha=alpha, zorder=3))

        if v >= 200 and country != "China":
            ax.text(x, y, f"{v:,.0f}", ha="center", va="center", fontsize=10.5,
                    color="#17333a", weight="bold", zorder=5)
            ax.text(x, y + 3.8, country, ha="center", va="center", fontsize=9,
                    color="#17333a", weight="bold", zorder=6)
        elif country == "China":
            ax.text(x, y, "≈15,000", ha="center", va="center", fontsize=11,
                    color="#7d4519", weight="bold", zorder=5)
            ax.text(x, y + 5.5, "China\n(cumulative)", ha="center", va="center", fontsize=9,
                    color="#7d4519", weight="bold", zorder=6)
        else:
            lx, ly = label_pos.get(country, (x, y))
            label = f"{country}\n{v:,.1f}" if v < 10 else f"{country}\n{v:,.0f}"
            ax.annotate(label, xy=(x, y), xytext=(lx, ly), ha="center", va="center", fontsize=8.8,
                        color="#174b68", weight="medium",
                        arrowprops=dict(arrowstyle="-", color="#00a9c0", lw=0.9, shrinkA=1, shrinkB=2),
                        zorder=6)

    # Titles
    fig.text(0.04, 0.94, "No small effort — 2026 update", fontsize=26, weight="bold", color="#282b2d")
    fig.text(0.04, 0.895, "Estimated annual or annualized public quantum-technology funding (USD millions)", fontsize=13, color="#34383b")
    fig.text(0.04, 0.86, "Bubble area scales with the figure. Positions are approximate geographic locations.", fontsize=10.5, color="#5c6063")

    # China caveat
    fig.text(0.72, 0.18, "CHINA — SPECIAL EXCEPTION\n≈ US$15B cumulative estimate\nthrough ~2024 • high uncertainty\nNot comparable to annual figures",
             ha="center", va="center", fontsize=9.5, color="#7d4519",
             bbox=dict(boxstyle="round,pad=0.6", facecolor="#f6e8d4", edgecolor="#b96b26", linewidth=1.4),
             zorder=9)

    # Footnotes
    fig.text(0.04, 0.08, "US shown at FY2024 enacted ($1,006M). Multi-year programs are annualized estimates, not actual annual spending.",
             fontsize=8.8, color="#5c6063")
    fig.text(0.04, 0.055, "Australia: outlined marker only (no comparable national total in dataset). Sources: latest project CSV + linked national programs.",
             fontsize=8.5, color="#5c6063")

    ax.set_xlim(-175, 185)
    ax.set_ylim(-60, 85)
    ax.axis("off")
    plt.subplots_adjust(left=0.03, right=0.98, top=0.82, bottom=0.16)

    out = "assets/quantum_funding_2026_geographic_bubble_chart.png"
    plt.savefig(out, bbox_inches="tight", facecolor=fig.get_facecolor(), dpi=180)
    plt.close()
    print(f"Chart saved to {out}")

if __name__ == "__main__":
    main()
