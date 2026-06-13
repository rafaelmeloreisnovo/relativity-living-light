# WORKFLOW EXECUTION MAP

Mapa `workflow → job → step → comando → script → existência/compilação`.
Todos os scripts abaixo foram verificados como **EXISTENTES** (`-f`) e o
conjunto Python compila com `py_compile` (exit 0). Sem inferência.

## Workflows GitHub Actions (13)

### START_MANUAL_HERE.yml — orquestrador manual (`workflow_dispatch`)
- `tools/audit_github_workflows.py --strict` — EXISTS, exec exit 0
- `scripts/rll_pipeline.py` — EXISTS
- `validacao_real/{fetch_real_data,compute_validation,make_figures,render_report}.py` — EXISTS
- `docs/pipelines/validation_paths/CAMINHOS_VALIDACAO_NOVOS.yml` (lido) — EXISTS
- artefato: `artifacts/manual-start/` (upload-artifact@v4). permissions: era ausente → `contents: read`.

### convention-check.yml — PR/push(main)
- `scripts/check_structure_d_required_outputs.sh` — EXISTS
- `scripts/check_structure_d_model_dataset_coverage.sh` — EXISTS
- `scripts/check_convention_conflicts.sh` — EXISTS
- (linha comentada: `tools/docs_inventory.py --check`)

### dha-fisher-ci.yml — PR/push(main)
- `pytest tests/test_dha_fisher.py tests/test_ln1pz_extractor.py tests/test_desi_dha_extractor.py` — testes EXISTS
- gera `results/dha/mock_catalog.csv` (mock **rotulado**, CI-only)
- `scripts/run_ln1pz_extractor.py`, `scripts/run_desi_dha_pipeline.py`, `scripts/export_dha_forecast.py` — EXISTS
- artefatos: `dha-fisher-forecast`, `ln1pz-extractor`, `desi-dha-extractor`

### formulas-artifacts.yml — push(**)/PR/dispatch
- `tools/formula_artifact_builder.py --root . --outdir artifacts/formulas` — EXISTS
- artefato: `formulas-artifacts` (`if-no-files-found: error`)

### iml_artifact.yml — dispatch
- `tools/iml/iml_pipeline.py` — EXISTS; `data/iml/daise_input.example.json` — EXISTS
- artefato: `iml-artifact`

### python-tests.yml — push/PR(main)
- `pytest -q` — runner de testes

### real-data-complete-execution.yml — dispatch (`contents: write`, tem concurrency)
- valida presença de: `docs/real_data/REAL_DATA_REQUIRED_INPUTS.md`,
  `RLL_REAL_DATA_INGESTION_REPORT_2026.md`,
  `data/real/rll_real_sources_manifest_2026.yml`,
  `data/real/cosmology_observational_seed_2026.csv` (+`.provenance.json`),
  `data/pipelines/structure_d/datasets_config.json` — **todos EXISTS**
- `scripts/download_real_cosmology_inputs.sh` — EXISTS
- `scripts/verify_pantheon_inputs.py` — EXISTS
- `tools/verify_real_source_signatures.py`, `tools/real_data_materialization_audit.py` — EXISTS
- `python -m data.pipelines.structure_d.run_all_real` — módulo EXISTS (`run_all_real.py`)
- `scripts/run_real_pantheon_validation.py` — EXISTS
- claim boundary explícito em `env.CLAIM_BOUNDARY`; checksums sha256 finais

### repo-real-inventory.yml — dispatch/push(main) (`contents: write`)
- inventário inline (git ls-files + sha256), grava `data/results/repo_inventory.{json,tsv}` e docs índice; commit+push

### rll-book-data-pipeline.yml — dispatch (job `contents: write`)
- `tools/docs_inventory.py` (+`--check`) — EXISTS
- `scripts/rll_pipeline.py` — EXISTS; checksums; commit leve opcional

### rll-data-pipeline.yml — dispatch (job `contents: write`)
- `tools/docs_inventory.py`, `scripts/rll_pipeline.py` — EXISTS; checksums; commit leve opcional

### rll-real-data-orchestrator.yml — dispatch (job `contents: write`)
- `tools/docs_inventory.py --check` — EXISTS
- `scripts/fetch_real_sources.py` — EXISTS
- `scripts/compute_rll_real_pipeline.py` — EXISTS
- `scripts/generate_rll_plots.py` — EXISTS
- `scripts/rll_pipeline.py`, `tools/iml/iml_pipeline.py`, `tools/formula_artifact_builder.py` — EXISTS

### unified-geometry.yml — dispatch/push(path)
- `scripts/unified_geometry_system.py --a 1.0 --r 1.0 --R 2.0` — EXISTS
- artefatos: `results/unified_geometry/{shapes.csv,manifest.json}`

### validacao_real.yml — dispatch (`contents: write`)
- `validacao_real/{fetch_real_data,compute_validation,make_figures,render_report}.py` — EXISTS, **executado neste runner, exit 0**
- commita `validacao_real/{fetched,results}`

## Data/config YAML consumidos por workflows (rastreabilidade)

| YAML | Consumido por |
|---|---|
| `data/observational_sources.yml` | START_MANUAL_HERE (interoperabilidade) |
| `data/real/cosmology/RLL_COSMO_VALIDATION_MATRIX.yml` | START_MANUAL_HERE |
| `data/real/cosmology/DESI_BAO_MATH_ARTIFACTS.yml` | START_MANUAL_HERE |
| `docs/pipelines/validation_paths/CAMINHOS_VALIDACAO_NOVOS.yml` | START_MANUAL_HERE (probe) |
| `validacao_real/sources.yml` (+ `data/*.yml`, `fetched/*.yml`) | validacao_real, fetch/compute |
| `data/real/rll_real_sources_manifest_2026.yml` | real-data-complete-execution |

LACUNA registrada: workflows não consomem diretamente `rll_equation_registry.yml`,
`rll_inovacao_tecnologica_watch.yml`, `data/strong_lensing_imf/…`,
`data/rll_latentes/…`, `data/results/desi_dr2_bao_zml.yml`,
`data/real_sources/*.iml.yml`, `tools/inventory_config.yml`,
`CAMINHOS_VALIDACAO_NOVOS.yml` (raiz). São catálogos/registries de referência
(reference_only) — ver boundary audit.
