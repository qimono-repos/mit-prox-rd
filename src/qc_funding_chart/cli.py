"""Command-line entry point for chart generation."""

from __future__ import annotations

import argparse
from pathlib import Path

from .chart import create_chart


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate the MIT xPRO quantum funding geographic bubble chart.")
    parser.add_argument("--data", default="assets/quantum_funding_updated.csv", help="Input funding CSV")
    parser.add_argument("--output", default="assets/quantum_funding_2026_geographic_bubble_chart.png", help="Output PNG path")
    args = parser.parse_args()
    output = create_chart(Path(args.data), Path(args.output))
    print(f"Chart written to {output.resolve()}")


if __name__ == "__main__":
    main()
