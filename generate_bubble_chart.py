#!/usr/bin/env python3
"""Backward-compatible wrapper for the packaged chart generator.

Preferred usage from the repository root:
    uv run qc-funding-chart

This script remains available for users accustomed to the original entry point:
    uv run python generate_bubble_chart.py
"""
from qc_funding_chart.cli import main


if __name__ == "__main__":
    main()
