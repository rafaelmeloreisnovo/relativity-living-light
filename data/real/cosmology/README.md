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

## Materialização real adicional — crescimento `fσ8`

- `fsigma8_growth_real.csv` contém uma compilação real de medições de crescimento/RSD com colunas de proveniência por linha (`survey`, `method`, `reference`, `source_url`).
- O arquivo substitui a fixture suave `data/inputs/structure_d/fsigma8.csv` apenas nas rotas de validação real/joint; a fixture continua no repositório para testes e rollback.
- A auditoria `python tools/real_data_materialization_audit.py` registra essa rota como `fsigma8 → real_fsigma8` e `fsigma8_cov_synth → real_fsigma8`.

## Assinaturas/proveniência viva de fontes

- `real_source_signatures.json` é gerado por `python tools/verify_real_source_signatures.py`.
- O arquivo registra SHA256 local, amostra HTTP limitada, termos obrigatórios encontrados e status de revisão/failover por fonte.
- Uma fonte bloqueada permanece marcada como revisão necessária; isso não autoriza preencher dados ausentes.
