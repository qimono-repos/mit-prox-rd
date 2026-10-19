# Chart package

Reusable chart implementation.

Run from the repository root:

```bash
uv sync
uv run qc-funding-chart
```

Customize input and output paths:

```bash
uv run qc-funding-chart --data assets/quantum_funding_updated.csv --output assets/my-chart.png
```

Regional groupings live in `regions.py`; data selection, rendering, and chart annotations live in `chart.py`.
