# stock-flow-library

A collection of books and papers containing system dynamics (stock-and-flow) models,
or models directly convertible to stocks and flows, curated as build cases for
[poietic-mcp](https://github.com/soobrosa/poietic-mcp).

- `system-dynamics-stock-flow-sources.md` — the annotated bibliography (books, papers,
  twelve convertible domains, collection status).
- `poietic-mcp-cases.md` — 48 build cases: stocks, flows, and key auxiliaries for each,
  re-specified with full stock/flow/auxiliary detail (fidelity-tagged `[full-text]` / `[canonical]`).
- `diagrams/` — original SVG stock-flow diagrams for 13 flagship cases, rendered by
  `gen_diagrams.py` (regenerate: `python3 gen_diagrams.py`).

| | |
|---|---|
| ![rework cycle](diagrams/rework_cycle.svg) | ![SIR](diagrams/sir.svg) |
| ![iron cycle](diagrams/iron_cycle.svg) | ![C-ROADS](diagrams/croads_carbon.svg) |

The PDFs themselves are **not committed** (copyright). To fetch the open-access subset:

```bash
./download.sh
```

Paywalled sources (Godley & Lavoie, Sterman 2000, Cooper 1980, etc.) must be obtained
via institutional access, Archive.org lending, or author request — see the status
section of the sources file for the full missing list and what worked/failed.
