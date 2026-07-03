# WORKFLOW REFACTOR AUDIT

Gerado em: `2026-07-03T16:02:54Z`  
Commit auditado: `929807336098e7edb7cfa2194dc2986fb6458deb`

## Inventário pré-alteração obrigatório

- `git status --short`: `?? RLL_JSON_EVOLUTION_WATCHER.yml
?? artifacts/EVOLUTION_TRAIL.jsonl
?? data/failsafe/
?? results/evolution_watcher_manifest.json
?? schemas/fingerprints/
?? tests/test_bootstrap_failsafe.py
?? tests/test_evolution_watcher_config.py
?? tests/test_rll_json_watcher.py
?? tools/bootstrap_failsafe.py
?? tools/rll_json_watcher.py`
- `git rev-parse HEAD`: `929807336098e7edb7cfa2194dc2986fb6458deb`
- Total YAML/YML: `110`
- Total workflows: `39`

## Validações executadas

| comando | exit_code | resultado |
|---|---:|---|
| `git status --short` | 0 | `?? tools/rll_json_watcher.py` |
| `git rev-parse HEAD` | 0 | `929807336098e7edb7cfa2194dc2986fb6458deb` |
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
| `.github/workflows/RLL-CI.yml` | True | `"TOKEN_VAZIO"` | False | LACUNA:rll | `TOKEN_VAZIO` | `rll-scientific-results:validation_outputs/` | `LACUNA_PERMISSIONS, RISCO_BOUNDARY_TERMS_ROTULADOS` |
| `.github/workflows/RLL_SCIENTIFIC.yml` | False | `"TOKEN_VAZIO"` | False | LACUNA:rll-validation | `TOKEN_VAZIO` | `rll-validation-results:validation_outputs/` | `LACUNA_PERMISSIONS` |
| `.github/workflows/START_MANUAL_HERE.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `start-manual-here-${{ github.run_id }}:artifacts/manual-start/` | `FATO_VERIFICADO` |
| `.github/workflows/academic-parameter-governance.yml` | True | `{"contents": "read"}` | False | LACUNA:validate-academic-parameter-registry | `TOKEN_VAZIO` | `academic-parameter-governance-policy-${{ github.run_id }}-${{ github.job }}:artifacts/workflow-policy/academic-parameter-governance/${{ github.job }}/` | `FATO_VERIFICADO` |
| `.github/workflows/android-build.yml` | True | `"TOKEN_VAZIO"` | False | LACUNA:android | `TOKEN_VAZIO` | `rll-debug-apk:app/build/outputs/apk/debug/*.apk, rll-validation-unsigned-apk:app/build/outputs/apk/validationUnsigned/*.apk, rll-release-apk-signed:app/build/outputs/apk/release/*.apk, rll-release-aab-signed:app/build/outputs/bundle/release/*.aab` | `LACUNA_PERMISSIONS, RISCO_BOUNDARY_TERMS_ROTULADOS` |
| `.github/workflows/bayes_analysis.yml` | False | `"TOKEN_VAZIO"` | False | OK | `TOKEN_VAZIO` | `resultados-bayesianos:data/bayes_result.json | figs/model_comparison.png | figs/posterior_epsilon.png | ` | `LACUNA_PERMISSIONS, RISCO_BOUNDARY_TERMS_ROTULADOS` |
| `.github/workflows/calc-data.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `${{ github.event.inputs.output_name }}:_audit/processed/` | `FATO_VERIFICADO` |
| `.github/workflows/canonical-route-artifacts.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `canonical-route-artifacts:data/real/bootstrap/canonical_route_checklist.yml | docs/science/CANONICAL_ROUTE_CHECKLIST.md | docs/science/TACTICAL_ROUTE_ORCHESTRATOR.md | docs/science/ROUTE_DEFIBRILLATION_POLICY.md | docs/science/PEER_REVIEW_READINESS_STATUS.md | docs/science/ROADMAP_NEXT_ACTIONS.md | data/raw/RAW_DATA_MANIFEST.yml | data/results/bootstrap/raw_data_manifest_status.json | data/results/bootstrap/raw_data_manifest_status.tsv | docs/science/RAW_DATA_MANIFEST_STATUS.md | data/real/orbital_dynamics/orbital_shape_angular_momentum_seed_v1.csv | data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.csv | data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.meta.yml | data/results/orbital_dynamics/orbital_state_vector_v2_validation.json | docs/science/ORBITAL_STATE_VECTOR_V2_REPORT.md | , route-artifact-checklist:data/real/bootstrap/canonical_route_checklist.yml | docs/science/CANONICAL_ROUTE_CHECKLIST.md | , route-artifact-raw-custody:data/raw/RAW_DATA_MANIFEST.yml | data/results/bootstrap/raw_data_manifest_status.json | data/results/bootstrap/raw_data_manifest_status.tsv | docs/science/RAW_DATA_MANIFEST_STATUS.md | docs/science/RAW_DATA_MANIFEST_GUIDE.md | , route-artifact-orbital-v2:data/real/orbital_dynamics/orbital_shape_angular_momentum_seed_v1.csv | data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.csv | data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.meta.yml | data/results/orbital_dynamics/orbital_state_vector_v2_validation.json | docs/science/ORBITAL_STATE_VECTOR_V2_REPORT.md | , route-artifact-orchestration-docs:docs/science/TACTICAL_ROUTE_ORCHESTRATOR.md | docs/science/ROUTE_DEFIBRILLATION_POLICY.md | docs/science/PEER_REVIEW_READINESS_STATUS.md | docs/science/ROADMAP_NEXT_ACTIONS.md | ` | `FATO_VERIFICADO` |
| `.github/workflows/claim-boundary-quality-gates.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `claim-boundary-quality-gates-policy-${{ github.run_id }}-${{ github.job }}:artifacts/workflow-policy/claim-boundary-quality-gates/${{ github.job }}/` | `FATO_VERIFICADO` |
| `.github/workflows/convention-check.yml` | False | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `RISCO_BOUNDARY_TERMS_ROTULADOS` |
| `.github/workflows/dense-feature-matrix.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `dense-feature-matrix:data/results/bootstrap/dense_behavior_features.json | data/results/bootstrap/dense_behavior_features.tsv | docs/science/DENSE_BEHAVIOR_FEATURES_REPORT.md | ` | `FATO_VERIFICADO` |
| `.github/workflows/desi-dr2-bao-validation.yml` | True | `{"contents": "read"}` | False | LACUNA:desi-dr2-bao | `TOKEN_VAZIO` | `desi-dr2-bao-covariance-chi2:results/desi_dr2_bao_covariance_chi2.json` | `FATO_VERIFICADO` |
| `.github/workflows/dha-fisher-ci.yml` | False | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `dha-fisher-forecast:results/dha/fisher_forecast_reference.json, ln1pz-extractor:results/dha/ln1pz_fit.csv | results/dha/ln1pz_fit_summary.json | , desi-dha-extractor:results/dha/desi_dha_pipeline_summary.json` | `RISCO_BOUNDARY_TERMS_ROTULADOS` |
| `.github/workflows/formulas-artifacts-validation.yml` | True | `{"contents": "read"}` | False | LACUNA:formulas-manifest | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `RISCO_BOUNDARY_TERMS_ROTULADOS` |
| `.github/workflows/formulas-artifacts.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `formulas-artifacts:artifacts/formulas` | `FATO_VERIFICADO` |
| `.github/workflows/iml_artifact.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `iml-artifact:artifacts/iml/iml_artifact.json` | `RISCO_BOUNDARY_TERMS_ROTULADOS` |
| `.github/workflows/import-data.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `${{ github.event.inputs.output_name }}:_audit/raw/` | `RISCO_BOUNDARY_TERMS_ROTULADOS` |
| `.github/workflows/orbital-shape-angular-momentum-validation.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `orbital-shape-angular-momentum-validation:data/real/orbital_dynamics/orbital_shape_angular_momentum_seed_v1.csv | data/real/orbital_dynamics/orbital_shape_angular_momentum_seed_v1.yml | data/results/orbital_dynamics/angular_momentum_shape_validation.json | docs/science/ORBITAL_SHAPE_ANGULAR_MOMENTUM_V1_REPORT.md | ` | `FATO_VERIFICADO` |
| `.github/workflows/orbital-state-vector-v2.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `orbital-state-vector-v2:data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.csv | data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.meta.yml | data/results/orbital_dynamics/orbital_state_vector_v2_validation.json | docs/science/ORBITAL_STATE_VECTOR_V2_REPORT.md | ` | `FATO_VERIFICADO` |
| `.github/workflows/python-tests.yml` | False | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `RISCO_BOUNDARY_TERMS_ROTULADOS` |
| `.github/workflows/raw-data-manifest-status.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `raw-data-manifest-status:data/results/bootstrap/raw_data_manifest_status.json | data/results/bootstrap/raw_data_manifest_status.tsv | docs/science/RAW_DATA_MANIFEST_STATUS.md | ` | `FATO_VERIFICADO` |
| `.github/workflows/real-data-bootstrap-validation.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `real-data-bootstrap-scan:data/results/bootstrap/real_data_bootstrap_summary.json | data/results/bootstrap/real_data_bootstrap_ledger.tsv | docs/science/REAL_DATA_BOOTSTRAP_SCAN_REPORT.md | ` | `FATO_VERIFICADO` |
| `.github/workflows/real-data-complete-execution.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `real-data-complete-${{ github.run_id }}:artifacts/real-data-complete/` | `FATO_VERIFICADO` |
| `.github/workflows/real-data-contract-ci.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `real-data-contract-${{ github.run_id }}:artifacts/real-data-contract/` | `FATO_VERIFICADO` |
| `.github/workflows/real-seed-ingestion-plan.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `real-seed-ingestion-plan:data/results/bootstrap/real_seed_ingestion_plan.json | data/results/bootstrap/real_seed_ingestion_plan.tsv | docs/science/REAL_SEED_INGESTION_PLAN.md | ` | `FATO_VERIFICADO` |
| `.github/workflows/real-seed-validation-v0.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `real-seed-validation-v0:data/results/compact_objects/remnant_boundary_validation.json | data/results/compact_objects/wandering_bh_validation.json | data/results/kinematics/historical_impulse_validation.json | data/results/high_z_smbh/seed_validation.json | data/results/bootstrap/real_seed_validation_index.json | docs/science/REAL_SEED_VALIDATION_V0_INDEX.md | ` | `FATO_VERIFICADO` |
| `.github/workflows/repo-real-inventory.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `repo-real-inventory-${{ github.run_id }}:docs/DOCUMENTATION_FULL_INVENTORY.md | docs/REAL_NUMBERS_REPORT.md | docs/YML_WORKFLOWS_INDEX.md | data/results/repo_inventory.json | data/results/repo_inventory.tsv | data/results/repo_inventory_summary.json | data/results/repo_inventory_checksums.sha256 | data/results/repo_inventory_commit_policy.txt | ` | `FATO_VERIFICADO` |
| `.github/workflows/rll-book-data-pipeline.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `rll-book-pipeline-${{ github.run_id }}-${{ inputs.book_scope }}-${{ inputs.dataset_group }}-${{ inputs.mode }}:artifacts/rll-pipeline/, rll-book-data-pipeline-policy-${{ github.run_id }}-${{ github.job }}:artifacts/workflow-policy/rll-book-data-pipeline/${{ github.job }}/` | `FATO_VERIFICADO` |
| `.github/workflows/rll-data-pipeline.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `rll-pipeline-${{ github.run_id }}-${{ inputs.dataset_group }}-${{ inputs.mode }}:artifacts/rll-pipeline/` | `FATO_VERIFICADO` |
| `.github/workflows/rll-real-data-orchestrator.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `rll-real-run-${{ github.run_id }}:artifacts/rll-real-run/` | `RISCO_BOUNDARY_TERMS_ROTULADOS` |
| `.github/workflows/six-sigma-real-data-controls.yml` | False | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `six-sigma-real-data-controls-policy-${{ github.run_id }}-${{ github.job }}:artifacts/workflow-policy/six-sigma-real-data-controls/${{ github.job }}/` | `FATO_VERIFICADO` |
| `.github/workflows/unified-geometry.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `unified-geometry-text-artifacts:results/unified_geometry/shapes.csv | results/unified_geometry/manifest.json | ` | `RISCO_BOUNDARY_TERMS_ROTULADOS` |
| `.github/workflows/validacao_real.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `validacao-real-artifacts:validacao_real/fetched/ | validacao_real/results/ | , validacao_real-policy-${{ github.run_id }}-${{ github.job }}:artifacts/workflow-policy/validacao_real/${{ github.job }}/` | `FATO_VERIFICADO` |
| `.github/workflows/validate-academic-correlation-package.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `RISCO_BOUNDARY_TERMS_ROTULADOS` |
| `.github/workflows/validate-cross-repo-relationship-registry.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `RISCO_BOUNDARY_TERMS_ROTULADOS` |
| `.github/workflows/validate-real-dataset-variance-registry.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `validate-real-dataset-variance-registry-policy-${{ github.run_id }}-${{ github.job }}:artifacts/workflow-policy/validate-real-dataset-variance-registry/${{ github.job }}/` | `FATO_VERIFICADO` |
| `.github/workflows/validate-schema-contracts.yml` | True | `{"contents": "read"}` | False | OK | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `RISCO_BOUNDARY_TERMS_ROTULADOS` |
| `.github/workflows/validate-sequence-metrics.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `validate-sequence-metrics-policy-${{ github.run_id }}-${{ github.job }}:artifacts/workflow-policy/validate-sequence-metrics/${{ github.job }}/` | `FATO_VERIFICADO` |
| `.github/workflows/yml-syntax-validation.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `yml-syntax-validation-${{ github.run_id }}:artifacts/yml-syntax-validation/` | `FATO_VERIFICADO` |

## Linguagem científica obrigatória

FATO_VERIFICADO: o artefato atual melhora rastreabilidade e reprodutibilidade por inventário, parser YAML, py_compile e ledger de hashes.  
LACUNA: esta auditoria documental não estabelece superioridade do RLL.  
ACAO_RECOMENDADA: quando AIC/BIC favorecerem ΛCDM, isso deve ser declarado nos relatórios científicos.
