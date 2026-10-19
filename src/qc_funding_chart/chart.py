# Chart rendering logic is separated from the CLI so it can also be imported by notebooks.
from __future__ import annotations

import math
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import Circle, Polygon

from .regions import COUNTRY_POSITIONS, LABEL_POSITIONS, REGIONS

NAME = "Country / Entity"
VALUE = "highest confidence figure USD Millions"
TYPE = "Type"
REQUIRED = {NAME, VALUE, TYPE, "ssource-link", "observations"}
US_SELECT = "FY2024 enacted"

LAND = [
    [(-165,72),(-135,72),(-110,65),(-95,55),(-82,50),(-75,35),(-100,10),(-120,20),(-145,45)],
    [(-80,12),(-50,8),(-35,-10),(-45,-35),(-60,-55),(-72,-25)],
    [(-10,70),(35,70),(65,60),(100,55),(140,50),(160,35),(130,5),(100,10),(70,25),(45,35),(25,45),(5,40),(-10,55)],
    [(112,-12),(153,-15),(154,-38),(130,-45),(114,-30)],
]
REGION_STYLES = {
    "Americas": {"center":(-84,18), "label":(-127,72), "fill":"#8bdcf4", "edge":"#43bfe5"},
    "Europe": {"center":(8,49), "label":(0,76), "fill":"#ffc7d0", "edge":"#ff9bab"},
    "Asia": {"center":(106,34), "label":(126,72), "fill":"#ffe1a1", "edge":"#ffcb68"},
    "APAC": {"center":(121,-14), "label":(169,2), "fill":"#dec7ff", "edge":"#c7a2ff"},
}


def load_country_values(df: pd.DataFrame) -> dict[str, float | None]:
    """Pick one value per listed country. Blank/missing values remain None."""
    values: dict[str, float | None] = {}
    us = df[df[NAME].astype(str).str.strip().eq("United States")]
    chosen = us[us[TYPE].astype(str).str.contains(US_SELECT, case=False, na=False)]
    if chosen.empty:
        chosen = us
    raw = pd.to_numeric(chosen.iloc[0][VALUE], errors="coerce") if not chosen.empty else float("nan")
    values["United States"] = None if pd.isna(raw) else float(raw)
    for country in COUNTRY_POSITIONS:
        if country == "United States":
            continue
        rows = df[df[NAME].astype(str).str.strip().eq(country)]
        if rows.empty:
            values[country] = None
        else:
            raw = pd.to_numeric(pd.Series([rows.iloc[0][VALUE]]), errors="coerce").iloc[0]
            values[country] = None if pd.isna(raw) else float(raw)
    return values


def region_totals(values: dict[str, float | None]) -> dict[str, float | None]:
    """Subtotal listed countries only; exclude China and never treat blanks as zero."""
    result: dict[str, float | None] = {}
    for region, members in REGIONS.items():
        amounts = [values[c] for c in members if c != "China" and values.get(c) is not None]
        result[region] = float(sum(amounts)) if amounts else None
    return result


def _draw_land(ax: Any) -> None:
    for shape in LAND:
        ax.add_patch(Polygon(shape, closed=True, facecolor="#eeece5", edgecolor="#d8d4ca", linewidth=.8, zorder=1))


def _draw_regions(ax: Any, totals: dict[str, float | None]) -> None:
    max_total = max((v for v in totals.values() if v is not None), default=1.0)
    for region, amount in totals.items():
        if amount is None:
            continue
        style = REGION_STYLES[region]
        x, y = style["center"]
        radius = 22 * math.sqrt(amount / max_total)  # area proportional to subtotal
        ax.add_patch(Circle((x,y), radius, facecolor=style["fill"], edgecolor=style["edge"], linewidth=1.5, alpha=.28, zorder=2))
        note = {"Americas":"listed-country subtotal", "Europe":"listed countries; excludes EU aggregate", "Asia":"listed countries; excludes China estimate", "APAC":"Singapore + Australia"}[region]
        lx, ly = style["label"]
        ax.annotate(f"{region}\nUS${amount / 1000:.2f}B\n({note})", xy=(x,y+radius*.78), xytext=(lx,ly), ha="center", va="center", fontsize=9, weight="bold", color=style["edge"], arrowprops={"arrowstyle":"-","color":style["edge"],"lw":1}, zorder=10)


def create_chart(data_path: str | Path, output_path: str | Path) -> Path:
    """Create a PNG geographic funding chart from the repository CSV."""
    df = pd.read_csv(data_path)
    missing = REQUIRED - set(df.columns)
    if missing:
        raise ValueError(f"CSV missing required columns: {', '.join(sorted(missing))}")
    values = load_country_values(df)
    fig, ax = plt.subplots(figsize=(16,9), dpi=180)
    fig.patch.set_facecolor("#fbfaf6")
    ax.set_facecolor("#fbfaf6")
    for x in [-120,-60,0,60,120]: ax.axvline(x,color="#e8e4db",lw=.6,zorder=0)
    for y in [-30,0,30,60]: ax.axhline(y,color="#e8e4db",lw=.6,zorder=0)
    _draw_land(ax)
    _draw_regions(ax, region_totals(values))
    comparable = [v for k,v in values.items() if v is not None and k != "China"]
    maximum = max(comparable, default=1.0)
    for country,(x,y) in COUNTRY_POSITIONS.items():
        value = values.get(country)
        if country == "China":
            radius = 9.5
            ax.add_patch(Circle((x,y),radius,facecolor="#ff9b45",edgecolor="#e66a16",lw=1.6,alpha=.78,zorder=7))
            ax.annotate("China\n≈ US$15B\n(cumulative through 2024; uncertain,\nnot comparable to annual figures)",xy=(x+radius*.82,y),xytext=(126,18),ha="left",va="center",fontsize=9,color="#9a4b13",arrowprops={"arrowstyle":"-","color":"#e66a16","lw":1},zorder=12)
            continue
        if value is None:
            ax.scatter([x],[y],s=90,marker="o",facecolors="none",edgecolors="#64748b",lw=1.5,zorder=8)
            lx,ly=LABEL_POSITIONS[country]
            ax.annotate(f"{country}\n(no comparable figure in CSV)",xy=(x,y),xytext=(lx,ly),ha="center",va="center",fontsize=8,color="#4b5563",arrowprops={"arrowstyle":"-","color":"#64748b","lw":.8},zorder=12)
            continue
        radius=1.7+8.6*math.sqrt(value/maximum)
        if country in ("United States","Canada"): color="#139bb7"
        elif country=="Brazil": color="#248a43"
        elif country in ("United Kingdom","Netherlands","Germany","Switzerland","Austria","Italy"): color="#eb4d52"
        elif country in ("Russia","India","Japan","South Korea","Singapore"): color="#f47b21"
        else: color="#8156bd"
        ax.add_patch(Circle((x,y),radius,facecolor=color,edgecolor=color,lw=1.3,alpha=.82,zorder=7))
        lx,ly=LABEL_POSITIONS[country]
        val_label=f"US${value/1000:.2f}B" if value>=100 else f"US${value:.1f}M"
        ax.annotate(f"{country}\n{val_label}",xy=(x,y),xytext=(lx,ly),ha="center",va="center",fontsize=8.4,weight="bold",color="#252b31",arrowprops={"arrowstyle":"-","color":color,"lw":.8},zorder=12)

    fig.text(.045,.94,"ESTIMATED GOV SPENDING ON QC : 2026 snapshot",fontsize=22,weight="bold",color="#202326")
    fig.text(.045,.90,"(Multi annual budgets annualized where possible)",fontsize=13.5,color="#34383b")
    fig.text(.84,.91,"National spending\n(US$ billions per year)",fontsize=9.5,color="#50555a",ha="center")
    for amount,y in [(100,.84),(50,.81),(10,.78),(1,.755),(.1,.735)]:
        r=min(.0052*math.sqrt(amount),.055)
        fig.add_artist(plt.Circle((.92,y),r,transform=fig.transFigure,fill=False,edgecolor="#888",lw=.8))
        fig.text(.95,y,str(amount),fontsize=8,color="#666",va="center")
    annual_total=sum(v for k,v in values.items() if v is not None and k!="China")
    fig.text(.045,.15,f"Listed-country annual/annualized sum\n≈ US${annual_total/1000:.2f}B/year",fontsize=12,color="#1f2937",bbox={"boxstyle":"square,pad=.55","facecolor":"#fde9e9","edgecolor":"none"})
    fig.text(.045,.085,"Sources: repository CSV and linked sources. Figures are approximate; see observations column.",fontsize=8.2,color="#5c6063")
    fig.text(.48,.085,"Regional bubbles are listed-country subtotals. China is cumulative and excluded; EU aggregate is not added to Europe.\nBlank values mean no comparable figure was supplied, not zero.",fontsize=7.8,color="#5c6063")
    fig.text(.845,.07,"Albert Gruning",fontsize=15,style="italic",color="#151515",ha="center")
    fig.text(.845,.045,"R&D tech specialist at Qimono (TM).\nOriginal report for MIT.",fontsize=7.8,color="#50555a",ha="center")
    ax.set_xlim(-175,185); ax.set_ylim(-60,85); ax.axis("off")
    plt.subplots_adjust(left=.02,right=.98,top=.83,bottom=.20)
    output_path=Path(output_path)
    output_path.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(output_path,bbox_inches="tight",facecolor=fig.get_facecolor())
    plt.close(fig)
    return output_path
