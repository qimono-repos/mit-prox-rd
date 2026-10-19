# MIT xPRO Quantum Computing R&D

Research notes, sources, funding data, and reproducible code for the MIT xPRO QCFx1 Week 3 quantum-funding infographic.

## Generate the chart

Python 3.11+ and [uv](https://docs.astral.sh/uv/) are required.

```bash
uv sync
uv run qc-funding-chart
```

Default output: `assets/quantum_funding_2026_geographic_bubble_chart.png`.

Use custom paths:

```bash
uv run qc-funding-chart --data assets/quantum_funding_updated.csv --output assets/my-chart.png
```

## Package layout

- `src/qc_funding_chart/chart.py`: CSV loading, country and regional bubble rendering, title, notes, and signature.
- `src/qc_funding_chart/regions.py`: geographic layout coordinates and four regional groupings.
- `src/qc_funding_chart/cli.py`: command-line interface.
- `assets/quantum_funding_updated.csv`: funding dataset used by the project.
- `quantum_funding_chart.ipynb`: historical notebook and design exploration.
- `REFERENCES.md`: cited sources.

## Regional bubbles and accounting

The visualization places four translucent regional bubbles behind the national bubbles:

- **Americas:** United States, Canada, Brazil.
- **Europe:** United Kingdom, Netherlands, Germany, Switzerland, Austria, Italy.
- **Asia:** Russia, China, Japan, South Korea, India.
- **APAC:** Singapore and Australia.

Regional figures are sums of listed countries for which the CSV supplies comparable annual/annualized numbers. China is excluded from the Asia subtotal because its value is a high-uncertainty cumulative estimate. The EU Quantum Flagship aggregate is not added as another European country because it can overlap national spending. Blank values mean the dataset does not provide a comparable figure; they are not treated as zero or filled with guesses.

Bubble **area** is proportional to the represented amount. Country positions are approximate infographic positions, not geographic boundary data.

## Data caveats

- The U.S. figure selects the FY2024 enacted row when multiple fiscal-year rows exist.
- Multi-year programs may be annualized estimates, not actual expenditures in a single fiscal year.
- China appears as a separate cumulative-estimate callout, not on the national annual bubble scale.
- The package reads the CSV rather than maintaining an independent set of funding numbers.
- See `REFERENCES.md` and the CSV `ssource-link` and `observations` fields before interpreting values.

This chart is a reproducible research visualization, not a government accounting statement.
