"""Geographic positions and regional groupings used by the chart.

Coordinates are approximate infographic positions, not a GIS dataset.
"""

COUNTRY_POSITIONS = {
    "Canada": (-105, 57), "United States": (-99, 37), "Brazil": (-52, -10),
    "United Kingdom": (-3, 54), "Netherlands": (5, 53), "Germany": (11, 51),
    "Switzerland": (8, 47), "Austria": (14, 47), "Italy": (12, 42),
    "Russia": (90, 57), "India": (79, 22), "China": (104, 35),
    "South Korea": (128, 36), "Japan": (139, 37), "Singapore": (104, 1.3),
    "Australia": (134, -25),
}

LABEL_POSITIONS = {
    "Canada": (-119, 62), "United States": (-112, 28), "Brazil": (-57, -24),
    "United Kingdom": (-15, 65), "Netherlands": (-2, 67), "Germany": (21, 57),
    "Switzerland": (-5, 39), "Austria": (22, 39), "Italy": (10, 31),
    "Russia": (108, 64), "India": (69, 13), "China": (126, 27),
    "South Korea": (151, 46), "Japan": (151, 29), "Singapore": (111, -8),
    "Australia": (144, -37),
}

REGIONS = {
    "Americas": ["United States", "Canada", "Brazil"],
    "Europe": ["United Kingdom", "Netherlands", "Germany", "Switzerland", "Austria", "Italy"],
    "Asia": ["Russia", "China", "Japan", "South Korea", "India"],
    "APAC": ["Singapore", "Australia"],
}
