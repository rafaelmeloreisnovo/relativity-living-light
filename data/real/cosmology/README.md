# Data README — Cosmology (Real)

Status: metadata_only / fetch-ready via orchestrator

## Fontes
- DESI DR2 BAO — https://www.desi.lbl.gov/
- Pantheon+ SNe Ia — https://github.com/PantheonPlusSH0ES/DataRelease
- Planck 2018 chains (PLA) — https://pla.esac.esa.int/
- H(z) cosmic chronometers — doi:10.48550/arXiv.1604.01410
- fσ8 constraints — doi:10.48550/arXiv.1801.01590

## Limitações
- Sem download de chains/dados pesados por padrão.
- Modo compute permanece stub até processamento reproduzível real.

## Orquestração GitHub Actions
- Workflow: `.github/workflows/rll-real-data-orchestrator.yml`
- Script de ingestão: `scripts/fetch_real_sources.py`
- Artefatos principais:
  - `artifacts/rll-real-run/raw/SOURCES.json`
  - `artifacts/rll-real-run/raw/cosmology_curated/CURATED_SOURCES.json`
  - `artifacts/rll-real-run/raw/cosmology_curated/Hz_data_real.csv`
  - `artifacts/rll-real-run/raw/cosmology_curated/BAO_data_real.csv`
  - `artifacts/rll-real-run/raw/cosmology_curated/CMB_shift_real.json`
