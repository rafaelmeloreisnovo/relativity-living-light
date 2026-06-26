# WORKFLOW REFACTOR AUDIT

Gerado em: `2026-06-26T20:26:23Z`  
Commit auditado: `3a48ed3fb4e86daf43b471337bfcdf9bdbb85fea`

## Inventário pré-alteração obrigatório

- `git status --short`: `M .github/workflows/repo-real-inventory.yml
 M .github/workflows/validacao_real.yml
 M CAMINHOS_VALIDACAO_NOVOS.yml
 M data/observational_sources.yml
 M data/raw/RAW_DATA_MANIFEST.yml
 M data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_observer_2006_sample.meta.yml
 M data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.meta.yml
 M data/real/bootstrap/canonical_route_checklist.yml
 M data/real/bootstrap/dense_behavior_feature_orchestration.yml
 M data/real/bootstrap/real_data_requirements_bootstrap.yml
 M data/real/bootstrap/real_observational_seed_v0.yml
 M data/real/bootstrap/real_observational_seed_v1.yml
 M data/real/cosmology/DESI_BAO_MATH_ARTIFACTS.yml
 M data/real/cosmology/RLL_COSMO_VALIDATION_MATRIX.yml
 M data/real/orbital_dynamics/angular_momentum_shape_sources.yml
 M data/real/orbital_dynamics/orbital_shape_angular_momentum_seed_v1.yml
 M data/real_sources/rll_pantheon_real_validation.iml.yml
 M data/results/desi_dr2_bao_zml.yml
 M data/rll_latentes/examples/invalid_missing_falsifier.yml
 M data/rll_latentes/examples/valid_minimal.yml
 M data/strong_lensing_imf/strong_lensing_imf_benchmark_seed_2026.yml
 M docs/pipelines/validation_paths/CAMINHOS_VALIDACAO_NOVOS.yml
 M knowledge_ecosystem/reference_seed_sources.yml
 M knowledge_ecosystem/source_search_queue.yml
 M rll_equation_registry.yml
 M rll_inovacao_tecnologica_watch.yml
 M tools/generate_yml_audit_docs.py
 M tools/inventory_config.yml
 M validacao_real/data/desi_dr2_bao.yml
 M validacao_real/data/hz_cosmic_chronometers.yml
 M validacao_real/fetched/desi_dr2_bao.yml
 M validacao_real/fetched/hz_cosmic_chronometers.yml
 M validacao_real/sources.yml
?? tests/test_write_workflow_guards.py`
- `git rev-parse HEAD`: `3a48ed3fb4e86daf43b471337bfcdf9bdbb85fea`
- Total YAML/YML: `67`
- Total workflows: `27`

## Validações executadas

| comando | exit_code | resultado |
|---|---:|---|
| `git status --short` | 0 | `?? tests/test_write_workflow_guards.py` |
| `git rev-parse HEAD` | 0 | `3a48ed3fb4e86daf43b471337bfcdf9bdbb85fea` |
| `python3 -c from pathlib import Path
import yaml,sys
failed=False
files=sorted([*Path('.').rglob('*.yml'),*Path('.').rglob('*.yaml')])
for p in files:
    try: yaml.safe_load(p.read_text(encoding='utf-8')); print('OK\t'+str(p))
    except Exception as e: failed=True; print('FAIL\t'+str(p)+'\t'+str(e))
sys.exit(1 if failed else 0)` | 0 | `OK	validacao_real/sources.yml` |
| `bash -lc python3 -m py_compile $(find scripts data/pipelines validacao_real tools -name "*.py" 2>/dev/null)` | 0 | `TOKEN_VAZIO` |
| `bash -lc find scripts -name "*.sh" -print0 2>/dev/null | xargs -0 -r bash -n` | 0 | `TOKEN_VAZIO` |
| `python3 tools/audit_github_workflows.py --strict` | 0 | `Workflow audit OK: executable workflows are isolated and validation data is externalized.` |

## Workflows auditados

| workflow | workflow_dispatch | permissions | concurrency | timeout | scripts inexistentes | artefatos | riscos |
|---|---:|---|---:|---|---|---|---|
| `.github/workflows/START_MANUAL_HERE.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `start-manual-here-${{ github.run_id }}:artifacts/manual-start/` | `FATO_VERIFICADO` |
| `.github/workflows/academic-parameter-governance.yml` | True | `{"contents": "read"}` | False | LACUNA:validate-academic-parameter-registry | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `RISCO_BOUNDARY_TERMS_ROTULADOS` |
| `.github/workflows/canonical-route-artifacts.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `canonical-route-artifacts:data/real/bootstrap/canonical_route_checklist.yml | docs/science/CANONICAL_ROUTE_CHECKLIST.md | docs/science/TACTICAL_ROUTE_ORCHESTRATOR.md | docs/science/ROUTE_DEFIBRILLATION_POLICY.md | docs/science/PEER_REVIEW_READINESS_STATUS.md | docs/science/ROADMAP_NEXT_ACTIONS.md | data/raw/RAW_DATA_MANIFEST.yml | data/results/bootstrap/raw_data_manifest_status.json | data/results/bootstrap/raw_data_manifest_status.tsv | docs/science/RAW_DATA_MANIFEST_STATUS.md | data/real/orbital_dynamics/orbital_shape_angular_momentum_seed_v1.csv | data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.csv | data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.meta.yml | data/results/orbital_dynamics/orbital_state_vector_v2_validation.json | docs/science/ORBITAL_STATE_VECTOR_V2_REPORT.md | , route-artifact-checklist:data/real/bootstrap/canonical_route_checklist.yml | docs/science/CANONICAL_ROUTE_CHECKLIST.md | , route-artifact-raw-custody:data/raw/RAW_DATA_MANIFEST.yml | data/results/bootstrap/raw_data_manifest_status.json | data/results/bootstrap/raw_data_manifest_status.tsv | docs/science/RAW_DATA_MANIFEST_STATUS.md | docs/science/RAW_DATA_MANIFEST_GUIDE.md | , route-artifact-orbital-v2:data/real/orbital_dynamics/orbital_shape_angular_momentum_seed_v1.csv | data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.csv | data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.meta.yml | data/results/orbital_dynamics/orbital_state_vector_v2_validation.json | docs/science/ORBITAL_STATE_VECTOR_V2_REPORT.md | , route-artifact-orchestration-docs:docs/science/TACTICAL_ROUTE_ORCHESTRATOR.md | docs/science/ROUTE_DEFIBRILLATION_POLICY.md | docs/science/PEER_REVIEW_READINESS_STATUS.md | docs/science/ROADMAP_NEXT_ACTIONS.md | ` | `RISCO_BOUNDARY_TERMS_ROTULADOS` |
| `.github/workflows/claim-boundary-quality-gates.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `RISCO_BOUNDARY_TERMS_ROTULADOS` |
| `.github/workflows/convention-check.yml` | False | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `RISCO_BOUNDARY_TERMS_ROTULADOS` |
| `.github/workflows/dense-feature-matrix.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `dense-feature-matrix:data/results/bootstrap/dense_behavior_features.json | data/results/bootstrap/dense_behavior_features.tsv | docs/science/DENSE_BEHAVIOR_FEATURES_REPORT.md | ` | `FATO_VERIFICADO` |
| `.github/workflows/desi-dr2-bao-validation.yml` | True | `{"contents": "read"}` | False | LACUNA:desi-dr2-bao | `TOKEN_VAZIO` | `desi-dr2-bao-covariance-chi2:results/desi_dr2_bao_covariance_chi2.json` | `FATO_VERIFICADO` |
| `.github/workflows/dha-fisher-ci.yml` | False | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `dha-fisher-forecast:results/dha/fisher_forecast_reference.json, ln1pz-extractor:results/dha/ln1pz_fit.csv | results/dha/ln1pz_fit_summary.json | , desi-dha-extractor:results/dha/desi_dha_pipeline_summary.json` | `RISCO_BOUNDARY_TERMS_ROTULADOS` |
| `.github/workflows/formulas-artifacts-validation.yml` | True | `{"contents": "read"}` | False | LACUNA:formulas-manifest | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `RISCO_BOUNDARY_TERMS_ROTULADOS` |
| `.github/workflows/formulas-artifacts.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `formulas-artifacts:artifacts/formulas` | `FATO_VERIFICADO` |
| `.github/workflows/iml_artifact.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `iml-artifact:artifacts/iml/iml_artifact.json` | `RISCO_BOUNDARY_TERMS_ROTULADOS` |
| `.github/workflows/orbital-shape-angular-momentum-validation.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `orbital-shape-angular-momentum-validation:data/real/orbital_dynamics/orbital_shape_angular_momentum_seed_v1.csv | data/real/orbital_dynamics/orbital_shape_angular_momentum_seed_v1.yml | data/results/orbital_dynamics/angular_momentum_shape_validation.json | docs/science/ORBITAL_SHAPE_ANGULAR_MOMENTUM_V1_REPORT.md | ` | `FATO_VERIFICADO` |
| `.github/workflows/orbital-state-vector-v2.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `orbital-state-vector-v2:data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.csv | data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.meta.yml | data/results/orbital_dynamics/orbital_state_vector_v2_validation.json | docs/science/ORBITAL_STATE_VECTOR_V2_REPORT.md | ` | `FATO_VERIFICADO` |
| `.github/workflows/python-tests.yml` | False | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `RISCO_BOUNDARY_TERMS_ROTULADOS` |
| `.github/workflows/raw-data-manifest-status.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `raw-data-manifest-status:data/results/bootstrap/raw_data_manifest_status.json | data/results/bootstrap/raw_data_manifest_status.tsv | docs/science/RAW_DATA_MANIFEST_STATUS.md | ` | `FATO_VERIFICADO` |
| `.github/workflows/real-data-bootstrap-validation.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `real-data-bootstrap-scan:data/results/bootstrap/real_data_bootstrap_summary.json | data/results/bootstrap/real_data_bootstrap_ledger.tsv | docs/science/REAL_DATA_BOOTSTRAP_SCAN_REPORT.md | ` | `FATO_VERIFICADO` |
| `.github/workflows/real-data-complete-execution.yml` | True | `{"contents": "write"}` | True | OK | `TOKEN_VAZIO` | `real-data-complete-${{ github.run_id }}:artifacts/real-data-complete/` | `RISCO_CONTENTS_WRITE` |
| `.github/workflows/real-data-contract-ci.yml` | True | `"TOKEN_VAZIO"` | False | LACUNA:real-data-contract | `TOKEN_VAZIO` | `real-data-contract-${{ github.run_id }}:artifacts/real-data-contract/` | `LACUNA_PERMISSIONS` |
| `.github/workflows/real-seed-ingestion-plan.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `real-seed-ingestion-plan:data/results/bootstrap/real_seed_ingestion_plan.json | data/results/bootstrap/real_seed_ingestion_plan.tsv | docs/science/REAL_SEED_INGESTION_PLAN.md | ` | `FATO_VERIFICADO` |
| `.github/workflows/real-seed-validation-v0.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `real-seed-validation-v0:data/results/compact_objects/remnant_boundary_validation.json | data/results/compact_objects/wandering_bh_validation.json | data/results/kinematics/historical_impulse_validation.json | data/results/high_z_smbh/seed_validation.json | data/results/bootstrap/real_seed_validation_index.json | docs/science/REAL_SEED_VALIDATION_V0_INDEX.md | ` | `FATO_VERIFICADO` |
| `.github/workflows/repo-real-inventory.yml` | True | `{"contents": "write"}` | True | OK | `TOKEN_VAZIO` | `repo-real-inventory-${{ github.run_id }}:docs/DOCUMENTATION_FULL_INVENTORY.md | docs/REAL_NUMBERS_REPORT.md | docs/YML_WORKFLOWS_INDEX.md | data/results/repo_inventory.json | data/results/repo_inventory.tsv | data/results/repo_inventory_summary.json | data/results/repo_inventory_checksums.sha256 | ` | `RISCO_CONTENTS_WRITE` |
| `.github/workflows/rll-book-data-pipeline.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `rll-book-pipeline-${{ github.run_id }}-${{ inputs.book_scope }}-${{ inputs.dataset_group }}-${{ inputs.mode }}:artifacts/rll-pipeline/` | `FATO_VERIFICADO` |
| `.github/workflows/rll-data-pipeline.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `rll-pipeline-${{ github.run_id }}-${{ inputs.dataset_group }}-${{ inputs.mode }}:artifacts/rll-pipeline/` | `FATO_VERIFICADO` |
| `.github/workflows/rll-real-data-orchestrator.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `rll-real-run-${{ github.run_id }}:artifacts/rll-real-run/` | `FATO_VERIFICADO` |
| `.github/workflows/unified-geometry.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `unified-geometry-text-artifacts:results/unified_geometry/shapes.csv | results/unified_geometry/manifest.json | ` | `RISCO_BOUNDARY_TERMS_ROTULADOS` |
| `.github/workflows/validacao_real.yml` | True | `{"contents": "write"}` | True | OK | `TOKEN_VAZIO` | `validacao-real-artifacts:validacao_real/fetched/ | validacao_real/results/ | ` | `RISCO_CONTENTS_WRITE` |
| `.github/workflows/yml-syntax-validation.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `RISCO_BOUNDARY_TERMS_ROTULADOS` |

## Linguagem científica obrigatória

FATO_VERIFICADO: o artefato atual melhora rastreabilidade e reprodutibilidade por inventário, parser YAML, py_compile e ledger de hashes.  
LACUNA: esta auditoria documental não estabelece superioridade do RLL.  
ACAO_RECOMENDADA: quando AIC/BIC favorecerem ΛCDM, isso deve ser declarado nos relatórios científicos.
