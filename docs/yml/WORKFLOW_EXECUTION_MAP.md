# WORKFLOW EXECUTION MAP

Gerado em: `2026-06-26T20:06:17Z`
Commit auditado: `623c7be20f0952cd5769615032f8d2d68a1a23e8`

## Mapa workflow -> job -> step -> script/comando

### `.github/workflows/START_MANUAL_HERE.yml`

- name: `START MANUAL HERE - YML Interoperability Orchestrator`
- permissions: `{"contents": "read"}`
- inputs: `book_scope, dataset_group, mode, pipeline_scope, real_data_source, run_data_preparation_probe, run_profile, strict_mode, validate_data_yml, validate_workflows`
- artifacts: `start-manual-here-${{ github.run_id }}:artifacts/manual-start/`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `manual-start` | `Install dependencies` | `TOKEN_VAZIO` | `python -m pip install --upgrade pip pip install pyyaml numpy pandas scipy matplotlib requests astropy` | `TOKEN_VAZIO` |
| `manual-start` | `Build selected execution plan` | `TOKEN_VAZIO` | `mkdir -p artifacts/manual-start cat > artifacts/manual-start/SELECTION_PLAN.md <<PLAN # START MANUAL HERE - Selection Plan - run_profile: ${{ inputs.run_profile }} - pipeline_scope: ${{ inputs.pipeline_scope }} - dataset` | `TOKEN_VAZIO` |
| `manual-start` | `Validate YAML parse (workflows + data)` | `TOKEN_VAZIO` | `python - <<'PY' import glob import yaml files = [] workflow_files = [] if "${{ inputs.validate_workflows }}" == "true": workflow_files = sorted(set(glob.glob('.github/workflows/*.yml') + glob.glob('.github/workflows/*.ya` | `TOKEN_VAZIO` |
| `manual-start` | `Validate workflow directory hygiene` | `TOKEN_VAZIO` | `python3 tools/audit_github_workflows.py --strict` | `tools/audit_github_workflows.py` |
| `manual-start` | `Validate interoperability contracts` | `TOKEN_VAZIO` | `python - <<'PY' import yaml from pathlib import Path strict = "${{ inputs.strict_mode }}" == "true" def load(path): with open(path, 'r', encoding='utf-8') as fh: return yaml.safe_load(fh) src = load('data/observational_s` | `TOKEN_VAZIO` |
| `manual-start` | `Data preparation probe for analysis formalization` | `TOKEN_VAZIO` | `mkdir -p artifacts/manual-start/probe if [ "${{ inputs.pipeline_scope }}" = "real_validation" ]; then (cd validacao_real && python3 fetch_real_data.py) if [ "${{ inputs.mode }}" = "compute" ] \|\| [ "${{ inputs.mode }}" = ` | `scripts/rll_pipeline.py` |
| `manual-start` | `Build methodology summary` | `TOKEN_VAZIO` | `cat > artifacts/manual-start/METHODOLOGY_SUMMARY.md <<EOF_SUM # Methodology Summary This run formalized YAML and pipeline selection with explicit controls: - Scope: ${{ inputs.pipeline_scope }} - Book scope: ${{ inputs.b` | `TOKEN_VAZIO` |
| `manual-start` | `Final summary` | `TOKEN_VAZIO` | `echo "START_MANUAL_HERE.YML finished with validation + methodology formalization."` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/academic-parameter-governance.yml`

- name: `Academic Parameter Governance`
- permissions: `{"contents": "read"}`
- inputs: `TOKEN_VAZIO`
- artifacts: `TOKEN_VAZIO`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `validate-academic-parameter-registry` | `Validate registry JSON and academic governance invariants` | `TOKEN_VAZIO` | `python3 tools/validate_academic_parameter_registry.py` | `tools/validate_academic_parameter_registry.py` |
| `validate-academic-parameter-registry` | `Scan current RLL model evidence table` | `TOKEN_VAZIO` | `python3 tools/scan_rll_model_evidence.py --no-write` | `tools/scan_rll_model_evidence.py` |
| `validate-academic-parameter-registry` | `Run integrated academic claim governance wrapper` | `TOKEN_VAZIO` | `python3 tools/run_rll_academic_claim_governance.py --no-write` | `tools/run_rll_academic_claim_governance.py` |
| `validate-academic-parameter-registry` | `Validate H0/r_d ablation matrix generator` | `TOKEN_VAZIO` | `python3 tools/make_h0_rd_ablation_matrix.py --no-write` | `tools/make_h0_rd_ablation_matrix.py` |
| `validate-academic-parameter-registry` | `Validate outcome action protocol for all possible statuses` | `TOKEN_VAZIO` | `python3 tools/apply_rll_outcome_protocol.py --no-write --status CLAIM_BLOCKED python3 tools/apply_rll_outcome_protocol.py --no-write --status PASS_LIMITED python3 tools/apply_rll_outcome_protocol.py --no-write --status P` | `tools/apply_rll_outcome_protocol.py` |
| `validate-academic-parameter-registry` | `Print claim boundary reminder` | `TOKEN_VAZIO` | `echo "PASS: registry, evidence scanner, governance wrapper, ablation matrix and outcome protocol checks completed." echo "Reminder: this gate validates provenance, calculable evidence, ablation policy, outcome routing an` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |

### `.github/workflows/canonical-route-artifacts.yml`

- name: `Canonical Route Artifacts`
- permissions: `{"contents": "read"}`
- inputs: `export_mode`
- artifacts: `canonical-route-artifacts:data/real/bootstrap/canonical_route_checklist.yml | docs/science/CANONICAL_ROUTE_CHECKLIST.md | docs/science/TACTICAL_ROUTE_ORCHESTRATOR.md | docs/science/ROUTE_DEFIBRILLATION_POLICY.md | docs/science/PEER_REVIEW_READINESS_STATUS.md | docs/science/ROADMAP_NEXT_ACTIONS.md | data/raw/RAW_DATA_MANIFEST.yml | data/results/bootstrap/raw_data_manifest_status.json | data/results/bootstrap/raw_data_manifest_status.tsv | docs/science/RAW_DATA_MANIFEST_STATUS.md | data/real/orbital_dynamics/orbital_shape_angular_momentum_seed_v1.csv | data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.csv | data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.meta.yml | data/results/orbital_dynamics/orbital_state_vector_v2_validation.json | docs/science/ORBITAL_STATE_VECTOR_V2_REPORT.md | , route-artifact-checklist:data/real/bootstrap/canonical_route_checklist.yml | docs/science/CANONICAL_ROUTE_CHECKLIST.md | , route-artifact-raw-custody:data/raw/RAW_DATA_MANIFEST.yml | data/results/bootstrap/raw_data_manifest_status.json | data/results/bootstrap/raw_data_manifest_status.tsv | docs/science/RAW_DATA_MANIFEST_STATUS.md | docs/science/RAW_DATA_MANIFEST_GUIDE.md | , route-artifact-orbital-v2:data/real/orbital_dynamics/orbital_shape_angular_momentum_seed_v1.csv | data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.csv | data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.meta.yml | data/results/orbital_dynamics/orbital_state_vector_v2_validation.json | docs/science/ORBITAL_STATE_VECTOR_V2_REPORT.md | , route-artifact-orchestration-docs:docs/science/TACTICAL_ROUTE_ORCHESTRATOR.md | docs/science/ROUTE_DEFIBRILLATION_POLICY.md | docs/science/PEER_REVIEW_READINESS_STATUS.md | docs/science/ROADMAP_NEXT_ACTIONS.md | `

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/claim-boundary-quality-gates.yml`

- name: `Claim Boundary Quality Gates`
- permissions: `{"contents": "read"}`
- inputs: `TOKEN_VAZIO`
- artifacts: `TOKEN_VAZIO`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `claim-boundary-quality-gates` | `Install package and test dependencies` | `TOKEN_VAZIO` | `python -m pip install --upgrade pip python -m pip install -e . python -m pip install pytest` | `TOKEN_VAZIO` |
| `claim-boundary-quality-gates` | `Compile validation scripts` | `TOKEN_VAZIO` | `python -m py_compile scripts/validation/check_claim_boundary.py python -m py_compile scripts/validation/check_seed_artifact_contracts.py python -m py_compile scripts/validation/real_seed_utils.py python -m py_compile scr` | `scripts/validation/check_claim_boundary.py, scripts/validation/check_seed_artifact_contracts.py, scripts/validation/real_seed_utils.py, scripts/validation/validate_orbital_shape_angular_momentum.py` |
| `claim-boundary-quality-gates` | `Run claim boundary gate` | `TOKEN_VAZIO` | `python scripts/validation/check_claim_boundary.py` | `scripts/validation/check_claim_boundary.py` |
| `claim-boundary-quality-gates` | `Run artifact contract checks` | `TOKEN_VAZIO` | `python scripts/validation/check_seed_artifact_contracts.py` | `scripts/validation/check_seed_artifact_contracts.py` |
| `claim-boundary-quality-gates` | `Run unit tests` | `TOKEN_VAZIO` | `python -m pytest -q tests` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |

### `.github/workflows/convention-check.yml`

- name: `Convention Consistency Check`
- permissions: `{"contents": "read"}`
- inputs: `TOKEN_VAZIO`
- artifacts: `TOKEN_VAZIO`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `check-conventions` | `Install ripgrep` | `TOKEN_VAZIO` | `sudo apt-get update && sudo apt-get install -y ripgrep` | `TOKEN_VAZIO` |
| `check-conventions` | `Check structure_d required outputs` | `TOKEN_VAZIO` | `bash scripts/check_structure_d_required_outputs.sh` | `scripts/check_structure_d_required_outputs.sh` |
| `check-conventions` | `Check structure_d dataset/model coverage` | `TOKEN_VAZIO` | `bash scripts/check_structure_d_model_dataset_coverage.sh` | `scripts/check_structure_d_model_dataset_coverage.sh` |
| `check-conventions` | `Validate canonical convention consistency` | `TOKEN_VAZIO` | `scripts/check_convention_conflicts.sh` | `scripts/check_convention_conflicts.sh` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |

### `.github/workflows/dense-feature-matrix.yml`

- name: `Dense Feature Matrix`
- permissions: `{"contents": "read"}`
- inputs: `TOKEN_VAZIO`
- artifacts: `dense-feature-matrix:data/results/bootstrap/dense_behavior_features.json | data/results/bootstrap/dense_behavior_features.tsv | docs/science/DENSE_BEHAVIOR_FEATURES_REPORT.md | `

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `build-dense-feature-matrix` | `Compile builder` | `TOKEN_VAZIO` | `python -m py_compile scripts/data_scan/build_dense_behavior_features.py` | `scripts/data_scan/build_dense_behavior_features.py` |
| `build-dense-feature-matrix` | `Build dense feature matrix` | `TOKEN_VAZIO` | `python scripts/data_scan/build_dense_behavior_features.py` | `scripts/data_scan/build_dense_behavior_features.py` |
| `build-dense-feature-matrix` | `Display dense feature report` | `TOKEN_VAZIO` | `cat docs/science/DENSE_BEHAVIOR_FEATURES_REPORT.md` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/desi-dr2-bao-validation.yml`

- name: `DESI DR2 BAO validation`
- permissions: `{"contents": "read"}`
- inputs: `TOKEN_VAZIO`
- artifacts: `desi-dr2-bao-covariance-chi2:results/desi_dr2_bao_covariance_chi2.json`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `desi-dr2-bao` | `Verify ARM64 runner` | `TOKEN_VAZIO` | `test "$(uname -m)" = "aarch64"` | `TOKEN_VAZIO` |
| `desi-dr2-bao` | `Install DESI DR2 BAO test dependencies` | `TOKEN_VAZIO` | `python -m pip install --upgrade pip python -m pip install pytest` | `TOKEN_VAZIO` |
| `desi-dr2-bao` | `Validate DESI DR2 BAO loader without external deps` | `TOKEN_VAZIO` | `python scripts/smoke_desi_dr2_bao_covariance_loader.py` | `scripts/smoke_desi_dr2_bao_covariance_loader.py` |
| `desi-dr2-bao` | `Validate DESI DR2 BAO loader tests` | `TOKEN_VAZIO` | `python tests/test_desi_dr2_bao_covariance_loader.py` | `tests/test_desi_dr2_bao_covariance_loader.py` |
| `desi-dr2-bao` | `Run DESI DR2 BAO covariance chi2 smoke` | `TOKEN_VAZIO` | `python scripts/check_desi_dr2_bao_covariance.py` | `scripts/check_desi_dr2_bao_covariance.py` |
| `desi-dr2-bao` | `Show DESI DR2 BAO result` | `TOKEN_VAZIO` | `cat results/desi_dr2_bao_covariance_chi2.json` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/dha-fisher-ci.yml`

- name: `DHA Fisher Validation`
- permissions: `{"contents": "read"}`
- inputs: `TOKEN_VAZIO`
- artifacts: `dha-fisher-forecast:results/dha/fisher_forecast_reference.json, ln1pz-extractor:results/dha/ln1pz_fit.csv | results/dha/ln1pz_fit_summary.json | , desi-dha-extractor:results/dha/desi_dha_pipeline_summary.json`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `dha-fisher` | `Install dependencies` | `TOKEN_VAZIO` | `python -m pip install --upgrade pip pip install -e . pip install pytest` | `TOKEN_VAZIO` |
| `dha-fisher` | `Run DHA Fisher and ln(1+z) extractor tests` | `TOKEN_VAZIO` | `pytest -q tests/test_dha_fisher.py tests/test_ln1pz_extractor.py tests/test_desi_dha_extractor.py` | `tests/test_desi_dha_extractor.py, tests/test_dha_fisher.py, tests/test_ln1pz_extractor.py` |
| `dha-fisher` | `Build mock catalog for ln(1+z) extraction` | `TOKEN_VAZIO` | `python - <<'PY2' import numpy as np, pandas as pd z = np.linspace(0.1, 6.0, 500) ln1pz = np.log1p(z) pk_baseline = 1000.0 * np.exp(-z/3.0) residual = 0.02 * np.cos(0.91 * ln1pz + 0.4) pk_obs = pk_baseline * (1.0 + residu` | `TOKEN_VAZIO` |
| `dha-fisher` | `Run ln(1+z) extractor` | `TOKEN_VAZIO` | `python scripts/run_ln1pz_extractor.py --input results/dha/mock_catalog.csv --output results/dha/ln1pz_fit.csv --summary results/dha/ln1pz_fit_summary.json` | `scripts/run_ln1pz_extractor.py` |
| `dha-fisher` | `Run DESI/BOSS DHA extractor pipeline` | `TOKEN_VAZIO` | `python scripts/run_desi_dha_pipeline.py --output results/dha/desi_dha_pipeline_summary.json` | `scripts/run_desi_dha_pipeline.py` |
| `dha-fisher` | `Generate deterministic DHA forecast artifact` | `TOKEN_VAZIO` | `python scripts/export_dha_forecast.py` | `scripts/export_dha_forecast.py` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/formulas-artifacts-validation.yml`

- name: `Formulas artifacts validation`
- permissions: `{"contents": "read"}`
- inputs: `TOKEN_VAZIO`
- artifacts: `TOKEN_VAZIO`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `formulas-manifest` | `Validate formulas manifest` | `TOKEN_VAZIO` | `python scripts/validate_formulas_manifest.py` | `scripts/validate_formulas_manifest.py` |
| `formulas-manifest` | `Validate formula index contract` | `TOKEN_VAZIO` | `python scripts/validate_formula_index_contract.py` | `scripts/validate_formula_index_contract.py` |
| `formulas-manifest` | `Compile materializer` | `TOKEN_VAZIO` | `python -m py_compile scripts/materialize_formula_index.py` | `scripts/materialize_formula_index.py` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |

### `.github/workflows/formulas-artifacts.yml`

- name: `formulas-artifacts`
- permissions: `{"contents": "read"}`
- inputs: `TOKEN_VAZIO`
- artifacts: `formulas-artifacts:artifacts/formulas`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `build-formulas-artifacts` | `Generate formula artifacts from docs and legacy markdown` | `TOKEN_VAZIO` | `python tools/formula_artifact_builder.py --root . --outdir artifacts/formulas` | `tools/formula_artifact_builder.py` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/iml_artifact.yml`

- name: `IML Artifact Generator`
- permissions: `{"contents": "read"}`
- inputs: `daise_input_path, steps`
- artifacts: `iml-artifact:artifacts/iml/iml_artifact.json`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `build-iml-artifact` | `Ensure input exists` | `TOKEN_VAZIO` | `mkdir -p data/iml if [ ! -f "${{ github.event.inputs.daise_input_path }}" ]; then cp data/iml/daise_input.example.json data/iml/daise_input.json fi` | `TOKEN_VAZIO` |
| `build-iml-artifact` | `Run IML pipeline` | `TOKEN_VAZIO` | `python tools/iml/iml_pipeline.py \ --input "${{ github.event.inputs.daise_input_path }}" \ --output "artifacts/iml/iml_artifact.json" \ --steps "${{ github.event.inputs.steps }}"` | `tools/iml/iml_pipeline.py` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/orbital-shape-angular-momentum-validation.yml`

- name: `Orbital Shape Angular Momentum Validation`
- permissions: `{"contents": "read"}`
- inputs: `TOKEN_VAZIO`
- artifacts: `orbital-shape-angular-momentum-validation:data/real/orbital_dynamics/orbital_shape_angular_momentum_seed_v1.csv | data/real/orbital_dynamics/orbital_shape_angular_momentum_seed_v1.yml | data/results/orbital_dynamics/angular_momentum_shape_validation.json | docs/science/ORBITAL_SHAPE_ANGULAR_MOMENTUM_V1_REPORT.md | `

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `validate-orbital-shape-angular-momentum` | `Compile validator` | `TOKEN_VAZIO` | `python -m py_compile scripts/validation/validate_orbital_shape_angular_momentum.py` | `scripts/validation/validate_orbital_shape_angular_momentum.py` |
| `validate-orbital-shape-angular-momentum` | `Run orbital shape angular momentum validation` | `TOKEN_VAZIO` | `python scripts/validation/validate_orbital_shape_angular_momentum.py` | `scripts/validation/validate_orbital_shape_angular_momentum.py` |
| `validate-orbital-shape-angular-momentum` | `Display results` | `TOKEN_VAZIO` | `cat data/results/orbital_dynamics/angular_momentum_shape_validation.json echo "---" cat docs/science/ORBITAL_SHAPE_ANGULAR_MOMENTUM_V1_REPORT.md` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/orbital-state-vector-v2.yml`

- name: `Orbital State Vector V2`
- permissions: `{"contents": "read"}`
- inputs: `TOKEN_VAZIO`
- artifacts: `orbital-state-vector-v2:data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.csv | data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.meta.yml | data/results/orbital_dynamics/orbital_state_vector_v2_validation.json | docs/science/ORBITAL_STATE_VECTOR_V2_REPORT.md | `

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `orbital-state-vector-v2` | `Compile scripts` | `TOKEN_VAZIO` | `python -m py_compile scripts/data_scan/fetch_horizons_mars_state_vector.py python -m py_compile scripts/validation/validate_orbital_state_vector_v2.py` | `scripts/data_scan/fetch_horizons_mars_state_vector.py, scripts/validation/validate_orbital_state_vector_v2.py` |
| `orbital-state-vector-v2` | `Fetch Horizons Mars vectors` | `TOKEN_VAZIO` | `python scripts/data_scan/fetch_horizons_mars_state_vector.py` | `scripts/data_scan/fetch_horizons_mars_state_vector.py` |
| `orbital-state-vector-v2` | `Validate orbital state-vector v2` | `TOKEN_VAZIO` | `python scripts/validation/validate_orbital_state_vector_v2.py` | `scripts/validation/validate_orbital_state_vector_v2.py` |
| `orbital-state-vector-v2` | `Display orbital v2 report` | `TOKEN_VAZIO` | `cat docs/science/ORBITAL_STATE_VECTOR_V2_REPORT.md` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/python-tests.yml`

- name: `Python tests`
- permissions: `{"contents": "read"}`
- inputs: `TOKEN_VAZIO`
- artifacts: `TOKEN_VAZIO`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `test` | `Install package and test dependencies` | `TOKEN_VAZIO` | `python -m pip install --upgrade pip python -m pip install -r requirements.txt pytest pyyaml` | `TOKEN_VAZIO` |
| `test` | `Run tests` | `TOKEN_VAZIO` | `pytest -q` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |

### `.github/workflows/raw-data-manifest-status.yml`

- name: `Raw Data Manifest Status`
- permissions: `{"contents": "read"}`
- inputs: `TOKEN_VAZIO`
- artifacts: `raw-data-manifest-status:data/results/bootstrap/raw_data_manifest_status.json | data/results/bootstrap/raw_data_manifest_status.tsv | docs/science/RAW_DATA_MANIFEST_STATUS.md | `

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `build-raw-data-manifest-status` | `Compile status builder` | `TOKEN_VAZIO` | `python -m py_compile scripts/data_scan/build_raw_data_manifest_status.py` | `scripts/data_scan/build_raw_data_manifest_status.py` |
| `build-raw-data-manifest-status` | `Build raw data manifest status` | `TOKEN_VAZIO` | `python scripts/data_scan/build_raw_data_manifest_status.py` | `scripts/data_scan/build_raw_data_manifest_status.py` |
| `build-raw-data-manifest-status` | `Display raw data manifest status` | `TOKEN_VAZIO` | `cat data/results/bootstrap/raw_data_manifest_status.json echo "---" cat docs/science/RAW_DATA_MANIFEST_STATUS.md` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/real-data-bootstrap-validation.yml`

- name: `Real Data Bootstrap Validation`
- permissions: `{"contents": "read"}`
- inputs: `mode`
- artifacts: `real-data-bootstrap-scan:data/results/bootstrap/real_data_bootstrap_summary.json | data/results/bootstrap/real_data_bootstrap_ledger.tsv | docs/science/REAL_DATA_BOOTSTRAP_SCAN_REPORT.md | `

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `scan-real-data-bootstrap` | `Show repository state` | `TOKEN_VAZIO` | `git rev-parse HEAD git status --short` | `TOKEN_VAZIO` |
| `scan-real-data-bootstrap` | `Install YAML parser` | `TOKEN_VAZIO` | `python -m pip install --upgrade pip python -m pip install pyyaml` | `TOKEN_VAZIO` |
| `scan-real-data-bootstrap` | `Compile scanner` | `TOKEN_VAZIO` | `python -m py_compile scripts/data_scan/scan_real_data_bootstrap.py` | `scripts/data_scan/scan_real_data_bootstrap.py` |
| `scan-real-data-bootstrap` | `Run real-data bootstrap scan` | `TOKEN_VAZIO` | `python scripts/data_scan/scan_real_data_bootstrap.py --repo .` | `scripts/data_scan/scan_real_data_bootstrap.py` |
| `scan-real-data-bootstrap` | `Display scan summary` | `TOKEN_VAZIO` | `cat data/results/bootstrap/real_data_bootstrap_summary.json echo "---" cat docs/science/REAL_DATA_BOOTSTRAP_SCAN_REPORT.md` | `TOKEN_VAZIO` |
| `scan-real-data-bootstrap` | `Strict mode claim gate` | `TOKEN_VAZIO` | `python - <<'PY' import json from pathlib import Path p = Path('data/results/bootstrap/real_data_bootstrap_summary.json') data = json.loads(p.read_text()) if data.get('missing_ledgers', 0) or data.get('blocked_ledgers', 0` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/real-data-complete-execution.yml`

- name: `Real Data Complete Execution`
- permissions: `{"contents": "write"}`
- inputs: `commit_light_artifacts, execution_mode, materialize_pantheon, retention_days, run_pantheon_validation, run_structure_d, strict_real_data`
- artifacts: `real-data-complete-${{ github.run_id }}:artifacts/real-data-complete/`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `real-data-complete` | `Install runtime dependencies` | `TOKEN_VAZIO` | `set -euo pipefail python -m pip install --upgrade pip python -m pip install numpy pandas scipy matplotlib pyyaml requests` | `TOKEN_VAZIO` |
| `real-data-complete` | `Create run plan and five-level repository inventory` | `TOKEN_VAZIO` | `set -euo pipefail mkdir -p "$RUN_DIR" "$RUN_DIR/reports" "$RUN_DIR/checks" cat > "$RUN_DIR/EXECUTION_PLAN.md" <<PLAN # Real Data Complete Execution - execution_mode: ${{ inputs.execution_mode }} - materialize_pantheon: $` | `TOKEN_VAZIO` |
| `real-data-complete` | `Validate real-data registry without rewriting committed data` | `TOKEN_VAZIO` | `set -euo pipefail python - <<'PY' \| tee "artifacts/real-data-complete/reports/real_data_policy_check.log" from pathlib import Path required = [ Path('docs/real_data/REAL_DATA_REQUIRED_INPUTS.md'), Path('docs/real_data/RL` | `TOKEN_VAZIO` |
| `real-data-complete` | `Materialize Pantheon+SH0ES official inputs` | `TOKEN_VAZIO` | `set -euo pipefail if [ "${{ inputs.materialize_pantheon }}" = "true" ]; then bash scripts/download_real_cosmology_inputs.sh \| tee "$RUN_DIR/reports/download_real_cosmology_inputs.log" else echo "Pantheon+ materialization` | `scripts/download_real_cosmology_inputs.sh` |
| `real-data-complete` | `Verify Pantheon+ inputs with strict failover` | `TOKEN_VAZIO` | `set -euo pipefail if python scripts/verify_pantheon_inputs.py --json > "$RUN_DIR/reports/pantheon_inputs.json"; then echo "Pantheon+ verification OK" \| tee "$RUN_DIR/reports/pantheon_inputs.status" else echo "Pantheon+ v` | `scripts/verify_pantheon_inputs.py` |
| `real-data-complete` | `Run real-source signature verification and materialization audit` | `TOKEN_VAZIO` | `set -euo pipefail python tools/verify_real_source_signatures.py \| tee "$RUN_DIR/reports/real_source_signature_verification.log" python tools/real_data_materialization_audit.py \| tee "$RUN_DIR/reports/real_data_materializ` | `tools/real_data_materialization_audit.py, tools/verify_real_source_signatures.py` |
| `real-data-complete` | `Run Structure-D real validation` | `TOKEN_VAZIO` | `set -euo pipefail python -m data.pipelines.structure_d.run_all_real \| tee "$RUN_DIR/reports/structure_d_real_validation.log" cp results/structure_d/model_comparison_real.csv "$RUN_DIR/reports/" \|\| true cp results/structu` | `TOKEN_VAZIO` |
| `real-data-complete` | `Run Pantheon+ real validation` | `TOKEN_VAZIO` | `set -euo pipefail if python scripts/run_real_pantheon_validation.py > "$RUN_DIR/reports/run_real_pantheon_validation.log" 2>&1; then echo "Pantheon+ real validation OK" \| tee "$RUN_DIR/reports/run_real_pantheon_validatio` | `scripts/run_real_pantheon_validation.py` |
| `real-data-complete` | `Build final report, checksums, and rollback manifest` | `TOKEN_VAZIO` | `set -euo pipefail mkdir -p "$RUN_DIR" python - <<'PY' import json from pathlib import Path root = Path('artifacts/real-data-complete') reports = sorted(str(path.relative_to(root)) for path in (root / 'reports').glob('*')` | `TOKEN_VAZIO` |
| `real-data-complete` | `Commit lightweight artifacts` | `TOKEN_VAZIO` | `set -euo pipefail DEST="results/pipeline-runs/${{ github.run_id }}" mkdir -p "$DEST" rsync -av --prune-empty-dirs \ --include='*/' \ --include='*.md' --include='*.json' --include='*.csv' --include='*.txt' --include='*.sh` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/real-data-contract-ci.yml`

- name: `Real Data Contract CI`
- permissions: `"TOKEN_VAZIO"`
- inputs: `real_data_source`
- artifacts: `real-data-contract-${{ github.run_id }}:artifacts/real-data-contract/`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `real-data-contract` | `Install contract dependencies` | `TOKEN_VAZIO` | `python -m pip install --upgrade pip python -m pip install -r requirements.txt pytest pyyaml` | `TOKEN_VAZIO` |
| `real-data-contract` | `Check generated inventory is current` | `TOKEN_VAZIO` | `python3 tools/docs_inventory.py --check` | `tools/docs_inventory.py` |
| `real-data-contract` | `Compute pipeline from committed real data` | `TOKEN_VAZIO` | `set -euo pipefail SOURCE="${{ github.event.inputs.real_data_source \|\| 'repo' }}" python3 scripts/compute_rll_real_pipeline.py \ --output-dir artifacts/real-data-contract \ --real-data-dir data/real \ --data-source "$SOUR` | `scripts/compute_rll_real_pipeline.py` |
| `real-data-contract` | `Validate contract outputs` | `TOKEN_VAZIO` | `set -euo pipefail test -s artifacts/real-data-contract/MANIFEST.json test -s artifacts/real-data-contract/COMPUTE_REPORT.md test -s artifacts/real-data-contract/tables/Hz_processed.csv test -s artifacts/real-data-contrac` | `TOKEN_VAZIO` |
| `real-data-contract` | `Run focused real-data tests` | `TOKEN_VAZIO` | `python -m pytest -q tests/test_compute_rll_real_pipeline_contract.py tests/test_desi_dr2_bao_materialized.py` | `tests/test_compute_rll_real_pipeline_contract.py, tests/test_desi_dr2_bao_materialized.py` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/real-seed-ingestion-plan.yml`

- name: `Real Seed Ingestion Plan`
- permissions: `{"contents": "read"}`
- inputs: `TOKEN_VAZIO`
- artifacts: `real-seed-ingestion-plan:data/results/bootstrap/real_seed_ingestion_plan.json | data/results/bootstrap/real_seed_ingestion_plan.tsv | docs/science/REAL_SEED_INGESTION_PLAN.md | `

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `build-real-seed-ingestion-plan` | `Show repository state` | `TOKEN_VAZIO` | `git rev-parse HEAD git status --short` | `TOKEN_VAZIO` |
| `build-real-seed-ingestion-plan` | `Compile ingestion plan builder` | `TOKEN_VAZIO` | `python -m py_compile scripts/data_scan/build_real_seed_ingestion_plan.py` | `scripts/data_scan/build_real_seed_ingestion_plan.py` |
| `build-real-seed-ingestion-plan` | `Build real seed ingestion plan` | `TOKEN_VAZIO` | `python scripts/data_scan/build_real_seed_ingestion_plan.py` | `scripts/data_scan/build_real_seed_ingestion_plan.py` |
| `build-real-seed-ingestion-plan` | `Display ingestion plan` | `TOKEN_VAZIO` | `cat data/results/bootstrap/real_seed_ingestion_plan.json echo "---" cat docs/science/REAL_SEED_INGESTION_PLAN.md` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/real-seed-validation-v0.yml`

- name: `Real Seed Validation v0`
- permissions: `{"contents": "read"}`
- inputs: `TOKEN_VAZIO`
- artifacts: `real-seed-validation-v0:data/results/compact_objects/remnant_boundary_validation.json | data/results/compact_objects/wandering_bh_validation.json | data/results/kinematics/historical_impulse_validation.json | data/results/high_z_smbh/seed_validation.json | data/results/bootstrap/real_seed_validation_index.json | docs/science/REAL_SEED_VALIDATION_V0_INDEX.md | `

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `real-seed-validation-v0` | `Show repository state` | `TOKEN_VAZIO` | `git rev-parse HEAD git status --short` | `TOKEN_VAZIO` |
| `real-seed-validation-v0` | `Compile validation scripts` | `TOKEN_VAZIO` | `python -m py_compile scripts/validation/real_seed_utils.py python -m py_compile scripts/validation/validate_compact_remnant_boundary.py python -m py_compile scripts/validation/validate_dark_lens_candidates.py python -m p` | `scripts/validation/real_seed_utils.py, scripts/validation/run_real_seed_validations.py, scripts/validation/validate_compact_remnant_boundary.py, scripts/validation/validate_dark_lens_candidates.py, scripts/validation/validate_high_z_smbh_seeds.py, scripts/validation/validate_historical_impulse_candidates.py` |
| `real-seed-validation-v0` | `Run all real seed validations` | `TOKEN_VAZIO` | `python scripts/validation/run_real_seed_validations.py` | `scripts/validation/run_real_seed_validations.py` |
| `real-seed-validation-v0` | `Display real seed validation index` | `TOKEN_VAZIO` | `cat data/results/bootstrap/real_seed_validation_index.json echo "---" cat docs/science/REAL_SEED_VALIDATION_V0_INDEX.md` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/repo-real-inventory.yml`

- name: `repo-real-inventory`
- permissions: `{"contents": "write"}`
- inputs: `TOKEN_VAZIO`
- artifacts: `repo-real-inventory-${{ github.run_id }}:docs/DOCUMENTATION_FULL_INVENTORY.md | docs/REAL_NUMBERS_REPORT.md | docs/YML_WORKFLOWS_INDEX.md | data/results/repo_inventory.json | data/results/repo_inventory.tsv | data/results/repo_inventory_summary.json | `

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `inventory` | `Generate real inventory from canonical tool` | `TOKEN_VAZIO` | `set -euo pipefail python3 tools/docs_inventory.py` | `tools/docs_inventory.py` |
| `inventory` | `Commit generated real inventory` | `TOKEN_VAZIO` | `set -euo pipefail git config user.name "github-actions[bot]" git config user.email "41898282+github-actions[bot]@users.noreply.github.com" git add docs/DOCUMENTATION_FULL_INVENTORY.md docs/REAL_NUMBERS_REPORT.md docs/YML` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/rll-book-data-pipeline.yml`

- name: `RLL Book Data Pipeline`
- permissions: `{"contents": "read"}`
- inputs: `book_scope, commit_artifacts, dataset_group, flush_artifact, mode, retention_days`
- artifacts: `rll-book-pipeline-${{ github.run_id }}-${{ inputs.book_scope }}-${{ inputs.dataset_group }}-${{ inputs.mode }}:artifacts/rll-pipeline/`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `pipeline` | `Prepare artifact directory` | `TOKEN_VAZIO` | `if [ "${{ inputs.flush_artifact }}" = "true" ]; then rm -rf artifacts/rll-pipeline fi mkdir -p artifacts/rll-pipeline` | `TOKEN_VAZIO` |
| `pipeline` | `Docs inventory` | `TOKEN_VAZIO` | `python3 tools/docs_inventory.py python3 tools/docs_inventory.py --check` | `tools/docs_inventory.py` |
| `pipeline` | `Run canonical pipeline` | `TOKEN_VAZIO` | `python3 scripts/rll_pipeline.py \ --book-scope "${{ inputs.book_scope }}" \ --dataset-group "${{ inputs.dataset_group }}" \ --mode "${{ inputs.mode }}" \ --output-dir artifacts/rll-pipeline` | `scripts/rll_pipeline.py` |
| `pipeline` | `Runtime files + checksums` | `TOKEN_VAZIO` | `date -u +"%Y-%m-%dT%H:%M:%SZ" > artifacts/rll-pipeline/RUN_UTC.txt echo "${GITHUB_SHA}" > artifacts/rll-pipeline/COMMIT_SHA.txt (cd artifacts/rll-pipeline && find . -type f ! -name CHECKSUMS.sha256 -print0 \| sort -z \| xa` | `TOKEN_VAZIO` |
| `pipeline` | `Commit lightweight artifacts` | `TOKEN_VAZIO` | `RUN_DIR="results/pipeline-runs/${{ github.run_id }}" mkdir -p "${RUN_DIR}" rsync -av --prune-empty-dirs \ --include='*/' \ --include='*.md' --include='*.json' --include='*.txt' --include='*.sha256' \ --exclude='*' \ arti` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/rll-data-pipeline.yml`

- name: `RLL Data Pipeline`
- permissions: `{"contents": "read"}`
- inputs: `commit_artifacts, dataset_group, flush_artifact, mode, retention_days`
- artifacts: `rll-pipeline-${{ github.run_id }}-${{ inputs.dataset_group }}-${{ inputs.mode }}:artifacts/rll-pipeline/`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `run` | `Prepare artifact directory` | `TOKEN_VAZIO` | `if [ "${{ inputs.flush_artifact }}" = "true" ]; then rm -rf artifacts/rll-pipeline; fi mkdir -p artifacts/rll-pipeline` | `TOKEN_VAZIO` |
| `run` | `Docs inventory` | `TOKEN_VAZIO` | `python3 tools/docs_inventory.py python3 tools/docs_inventory.py --check` | `tools/docs_inventory.py` |
| `run` | `Execute RLL pipeline` | `TOKEN_VAZIO` | `python3 scripts/rll_pipeline.py --dataset-group "${{ inputs.dataset_group }}" --mode "${{ inputs.mode }}" --output-dir artifacts/rll-pipeline` | `scripts/rll_pipeline.py` |
| `run` | `Runtime metadata` | `TOKEN_VAZIO` | `date -u +"%Y-%m-%dT%H:%M:%SZ" > artifacts/rll-pipeline/RUN_UTC.txt echo "${GITHUB_SHA}" > artifacts/rll-pipeline/COMMIT_SHA.txt (cd artifacts/rll-pipeline && find . -type f ! -name CHECKSUMS.sha256 -print0 \| sort -z \| xa` | `TOKEN_VAZIO` |
| `run` | `Commit lightweight artifacts` | `TOKEN_VAZIO` | `RUN_DIR="results/pipeline-runs/${{ github.run_id }}" mkdir -p "$RUN_DIR" rsync -av --prune-empty-dirs \ --include='*/' \ --include='*.md' --include='*.json' --include='*.txt' --include='*.sha256' \ --exclude='*' \ artifa` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/rll-real-data-orchestrator.yml`

- name: `RLL Real Data Orchestrator`
- permissions: `{"contents": "read"}`
- inputs: `book_scope, commit_light_artifacts, dataset_group, fetch_desi, fetch_igrf14, fetch_nmdb, fetch_omni, fetch_pantheon, fetch_planck, fetch_spenvis_reference, fetch_wmm2025, mode, pipeline_scope, real_data_source, retention_days, run_formulas, run_iml, run_plots`
- artifacts: `rll-real-run-${{ github.run_id }}:artifacts/rll-real-run/`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `orchestrate` | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `python -m pip install --upgrade pip pip install numpy pandas scipy matplotlib requests astropy pyyaml` | `TOKEN_VAZIO` |
| `orchestrate` | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `mkdir -p artifacts/rll-real-run/{raw,processed,plots,tables,book,iml,formulas}` | `TOKEN_VAZIO` |
| `orchestrate` | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `python3 tools/docs_inventory.py --check` | `tools/docs_inventory.py` |
| `orchestrate` | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `python3 scripts/fetch_real_sources.py \ --dataset-group "${{ inputs.dataset_group }}" \ --mode "${{ inputs.mode }}" \ --output-dir artifacts/rll-real-run \ ${{ inputs.fetch_igrf14 && '--fetch-igrf14' \|\| '--no-fetch-igrf1` | `scripts/fetch_real_sources.py` |
| `orchestrate` | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `python3 scripts/compute_rll_real_pipeline.py --output-dir artifacts/rll-real-run --data-source "${{ inputs.real_data_source }}"` | `scripts/compute_rll_real_pipeline.py` |
| `orchestrate` | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `python3 scripts/generate_rll_plots.py` | `scripts/generate_rll_plots.py` |
| `orchestrate` | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `python3 scripts/rll_pipeline.py --book-scope "${{ inputs.book_scope }}" --dataset-group "${{ inputs.dataset_group }}" --mode "${{ inputs.mode == 'full' && 'compute' \|\| inputs.mode }}" --output-dir artifacts/rll-real-run` | `scripts/rll_pipeline.py` |
| `orchestrate` | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `printf '{"dados":[1,2,3,4],"coerencia_in":0.7,"coerencia0":0.5,"entropia0":0.5,"estado":"ACTIVE"}\n' > artifacts/rll-real-run/iml/input.json python3 tools/iml/iml_pipeline.py --input artifacts/rll-real-run/iml/input.json` | `tools/iml/iml_pipeline.py` |
| `orchestrate` | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `python3 tools/formula_artifact_builder.py --outdir artifacts/rll-real-run/formulas` | `tools/formula_artifact_builder.py` |
| `orchestrate` | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `date -u +"%Y-%m-%dT%H:%M:%SZ" > artifacts/rll-real-run/RUN_UTC.txt git rev-parse HEAD > artifacts/rll-real-run/COMMIT_SHA.txt find artifacts/rll-real-run -type f -print0 \| sort -z \| xargs -0 sha256sum > artifacts/rll-rea` | `TOKEN_VAZIO` |
| `orchestrate` | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `DEST="results/pipeline-runs/${{ github.run_id }}" mkdir -p "$DEST" rsync -av --include='*/' --include='*.md' --include='*.json' --include='*.csv' --include='*.txt' --include='*.sha256' --include='*.png' --exclude='*' art` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/unified-geometry.yml`

- name: `unified-geometry`
- permissions: `{"contents": "read"}`
- inputs: `TOKEN_VAZIO`
- artifacts: `unified-geometry-text-artifacts:results/unified_geometry/shapes.csv | results/unified_geometry/manifest.json | `

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `build-text-artifacts` | `Run unified geometry generator` | `TOKEN_VAZIO` | `python scripts/unified_geometry_system.py --a 1.0 --r 1.0 --R 2.0` | `scripts/unified_geometry_system.py` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/validacao_real.yml`

- name: `Validacao Real RLL`
- permissions: `{"contents": "write"}`
- inputs: `note`
- artifacts: `validacao-real-artifacts:validacao_real/fetched/ | validacao_real/results/ | `

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `validate` | `Install minimal deps` | `TOKEN_VAZIO` | `pip install pyyaml matplotlib` | `TOKEN_VAZIO` |
| `validate` | `Fetch real data (portal with embedded fallback)` | `validacao_real` | `python3 fetch_real_data.py` | `validacao_real/fetch_real_data.py` |
| `validate` | `Compute validation (chi2 / AIC / BIC / falsifiability)` | `validacao_real` | `python3 compute_validation.py` | `validacao_real/compute_validation.py` |
| `validate` | `Generate figures` | `validacao_real` | `python3 make_figures.py` | `validacao_real/make_figures.py` |
| `validate` | `Render documentation from artifacts` | `validacao_real` | `python3 render_report.py` | `validacao_real/render_report.py` |
| `validate` | `Commit results back to repo` | `TOKEN_VAZIO` | `git config user.name "github-actions[bot]" git config user.email "41898282+github-actions[bot]@users.noreply.github.com" git add validacao_real/fetched validacao_real/results git commit -m "validacao_real: automated run ` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/yml-syntax-validation.yml`

- name: `YAML Syntax Validation Gate`
- permissions: `{"contents": "read"}`
- inputs: `TOKEN_VAZIO`
- artifacts: `TOKEN_VAZIO`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `validate-yaml` | `Install PyYAML` | `TOKEN_VAZIO` | `python -m pip install --upgrade pip pyyaml` | `TOKEN_VAZIO` |
| `validate-yaml` | `Validate every YAML file with a real parser` | `TOKEN_VAZIO` | `python - <<'PY' from pathlib import Path import yaml, sys, hashlib files = sorted( p for p in [*Path('.').rglob('*.yml'), *Path('.').rglob('*.yaml')] if '.git/' not in str(p) ) failed = 0 for p in files: raw = p.read_byt` | `TOKEN_VAZIO` |
| `validate-yaml` | `Validate workflow isolation (repo audit tool)` | `TOKEN_VAZIO` | `python3 tools/audit_github_workflows.py --strict` | `tools/audit_github_workflows.py` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |

## Scripts chamados por workflows

| script | existe | linhas | main | argparse | checksum | termo boundary | erro explícito | sha256 |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `scripts/check_convention_conflicts.sh` | `True` | 47 | False | False | False | False | False | `ea5f6c1e04d29db39afefd37f461203aa3868f2d28f97265d8658b8c54f266d3` |
| `scripts/check_desi_dr2_bao_covariance.py` | `True` | 133 | True | True | False | False | True | `25337be7feb5fc620bc607eb65b508ea76812112e9a86139d61851c8673d2774` |
| `scripts/check_structure_d_model_dataset_coverage.sh` | `True` | 74 | False | False | False | False | True | `0ff1934ae15fc3bbb824438e38daf5b8768ecd3b10648ddcd48544fa1c9397ad` |
| `scripts/check_structure_d_required_outputs.sh` | `True` | 72 | False | False | False | False | True | `ad980b2c79fba82b949f18b3bb0337ee34d0b40abcf1106e7d3d40efcec55684` |
| `scripts/compute_rll_real_pipeline.py` | `True` | 330 | True | True | True | True | True | `dd16ed6eddfc8fdd864eab20a909c9438f23b645efeb5a64c06c4cfadbd6b0ee` |
| `scripts/data_scan/build_dense_behavior_features.py` | `True` | 223 | True | False | True | True | True | `3713cde17ecc3f14e20876ffc16868a96f92c161bb9f69964458e6ea7245cde8` |
| `scripts/data_scan/build_raw_data_manifest_status.py` | `True` | 171 | True | False | True | True | True | `ef80beab6c4e9e13366a31404f7b1ea5cbac86548172b13700e8a1d12379e441` |
| `scripts/data_scan/build_real_seed_ingestion_plan.py` | `True` | 198 | True | False | True | True | True | `06375c67a2281da0c712aba3e90fcbe2cbcef49a74797136b43296196056aa4e` |
| `scripts/data_scan/fetch_horizons_mars_state_vector.py` | `True` | 140 | True | False | True | True | True | `31d21ead694019cfd415d0867c2a94d14611d39cc68346cc4e9c50b78c68f77a` |
| `scripts/data_scan/scan_real_data_bootstrap.py` | `True` | 264 | True | True | True | True | True | `9f95fdb094ff2c99d22f457fed9fc835e032e376ca3c4cb5b9711435cb6c5ec0` |
| `scripts/download_real_cosmology_inputs.sh` | `True` | 96 | False | False | True | True | False | `4992ea82ab448ad775d65391021694a256a97e99e3e224556f4629a4a5b2e0a3` |
| `scripts/export_dha_forecast.py` | `True` | 23 | True | False | False | False | False | `5718403bbcafbac5369312542e8bda7f2a58bcbb7eb9887a9d87ada4897b941d` |
| `scripts/fetch_real_sources.py` | `True` | 310 | True | True | True | True | True | `2c6e606ac530ffef24efc4c5753d3a2bcc3cddf8d63e49fbe8bfa591256e4b2a` |
| `scripts/generate_rll_plots.py` | `True` | 25 | True | False | False | False | True | `e67151201d5735e4111f38415f91664f3d946b704b2bed29b23258085af03a5a` |
| `scripts/materialize_formula_index.py` | `True` | 118 | True | True | True | True | True | `5ddbab5d531c83d2ce6c71f8159ceebf5c8d5755daab2e4264d0be591e9e142c` |
| `scripts/rll_pipeline.py` | `True` | 265 | True | True | False | True | True | `4c5b0165359e00da84efc162a5e157385e613e2fe6ad3aa47f7e1c426c4f0331` |
| `scripts/run_desi_dha_pipeline.py` | `True` | 29 | True | True | False | False | False | `807d6d435278ab80841acfef34bba13a5a9a40380bfef0b921384430ef487dfc` |
| `scripts/run_ln1pz_extractor.py` | `True` | 29 | True | True | False | False | False | `cff817d088572073e91ce546e3c41bdf847f75cdb5e61ae4ea9fedf5bfb6698f` |
| `scripts/run_real_pantheon_validation.py` | `True` | 290 | True | True | True | False | True | `7866fc213c097175d5bf8b6fdb2f0138dbe3abfa9f892f31f0200cd93332eea2` |
| `scripts/smoke_desi_dr2_bao_covariance_loader.py` | `True` | 35 | True | False | False | False | False | `a76fd5d1499094cabce27bc6c77614960a786303bb407430b48734c8f55c4b40` |
| `scripts/unified_geometry_system.py` | `True` | 120 | True | True | False | False | True | `e37b8de7fbc82ecccce19f613e86c1fc82b4566ca315ead35be54908eb5f59b6` |
| `scripts/validate_formula_index_contract.py` | `True` | 16 | False | False | False | False | False | `b2c5c0379deb67e4883310ed117133fdc6311479900fffdaea3e7ac6ca5716e4` |
| `scripts/validate_formulas_manifest.py` | `True` | 19 | False | False | True | False | False | `6fc40508e3dfb6ab1df2ca8925a6801f8563fbe9997bee1b42fc481ef17c392a` |
| `scripts/validation/check_claim_boundary.py` | `True` | 64 | True | False | False | False | True | `c1a03a5157074d1b621394caa554bacc8eb33b47365cd89e0c4fe34b9b3d0425` |
| `scripts/validation/check_seed_artifact_contracts.py` | `True` | 64 | True | False | False | True | True | `76979ed687e064db11589536e71a8ceecd0597b494f5d41af8778609c016dbdf` |
| `scripts/validation/real_seed_utils.py` | `True` | 118 | False | False | False | True | True | `424ac4a2cf2f6591ffd2b94b2e07d8b8f024a817190a6f62a9f7429044e4c792` |
| `scripts/validation/run_real_seed_validations.py` | `True` | 115 | True | False | True | True | True | `265d76433d0f6b44f1bc924c5f1da64e543fca65b7a33f7dd9f07ded25ad357d` |
| `scripts/validation/validate_compact_remnant_boundary.py` | `True` | 78 | True | False | False | True | True | `aae40ab5ba791e3744c13377bc422ef41a8eedebaf508eb2b6d4b76f2bd635a7` |
| `scripts/validation/validate_dark_lens_candidates.py` | `True` | 61 | True | False | False | True | True | `007e14239401a52464206272e8d80adf3a632b19b3f62d0e4909233796746dd9` |
| `scripts/validation/validate_high_z_smbh_seeds.py` | `True` | 71 | True | False | False | False | True | `444abd65d998a12ec289255f9c60a43a10c3df99d5bcec81bd23cbe0db9fa51a` |
| `scripts/validation/validate_historical_impulse_candidates.py` | `True` | 51 | True | False | False | False | True | `f59770e83e0eef5eef9f02c0d46b3d5a2b0fd39957e37f6ff8a2e2bb56cae308` |
| `scripts/validation/validate_orbital_shape_angular_momentum.py` | `True` | 164 | True | False | False | False | True | `1d0c90f0f9c024f7eb5a46c9b564ff114515012babf83120e1ef6055a93e4135` |
| `scripts/validation/validate_orbital_state_vector_v2.py` | `True` | 154 | True | False | False | True | True | `569818ede4940980515dd142e96c86d8d5817803426f73d5af55052b01573f92` |
| `scripts/verify_pantheon_inputs.py` | `True` | 86 | True | True | True | False | True | `91c8a358cc2320fe0d23d2955c29b9daeb6648baaadbe90a6414993da678ab4f` |
| `tests/test_compute_rll_real_pipeline_contract.py` | `True` | 106 | False | False | False | True | False | `7e8566a08f2e9375d895a942f0c35de933a23f68547660d523aae6168915ae22` |
| `tests/test_desi_dha_extractor.py` | `True` | 11 | False | False | False | False | False | `056cef79bc6e86084747710dfd49da08e2296bc5bf29ce4c805841ea093bc009` |
| `tests/test_desi_dr2_bao_covariance_loader.py` | `True` | 38 | True | False | False | False | False | `bf166aa39a7ae145a74b0cc5b82af9281575d157fae8c92acf818e1a0ba7194f` |
| `tests/test_desi_dr2_bao_materialized.py` | `True` | 37 | False | False | False | False | False | `4cc0249fe150adb866989be7bcb3cb9d615ed998418bf7a55c3a0ae9792696c4` |
| `tests/test_dha_fisher.py` | `True` | 22 | False | False | False | False | False | `54612a5ab5bbf91096be8d6f0c45405afc6b3eb3a779df67f11cf727d66acfe0` |
| `tests/test_ln1pz_extractor.py` | `True` | 32 | False | False | False | False | False | `99f07f4c1fe823b5fe9491605cb6eebd8f21e64e6480387bf7e205acd1d04416` |
| `tools/apply_rll_outcome_protocol.py` | `True` | 355 | True | True | False | True | True | `096e814399af199e2ac7319c0127ce307f7350f4fde1a213d1fb3b4034c9d158` |
| `tools/audit_github_workflows.py` | `True` | 133 | True | True | False | False | True | `926fd3360f0357ea8412e8d7318ad5b19b0802bad0911f211699ddf027c17b14` |
| `tools/docs_inventory.py` | `True` | 470 | True | True | True | True | True | `a47657bad2c32fa66d9820e55f0db25172b6668bcc71f53637053634ebfd121f` |
| `tools/formula_artifact_builder.py` | `True` | 51 | True | True | False | False | False | `adc0f0eae76f4dfba28e2dbe4f449d27fe3433f80d8a1c7853dfbef98c3eb548` |
| `tools/iml/iml_pipeline.py` | `True` | 43 | True | True | True | False | False | `73dfa54829abaf7df43a453501ad3ae38dad571f588222315831d141a0b1daa1` |
| `tools/make_h0_rd_ablation_matrix.py` | `True` | 148 | True | True | False | True | False | `e3cfd4b334184335ec8c3136e39f7fcda22573bf5758214e9d6b998fa52259f4` |
| `tools/real_data_materialization_audit.py` | `True` | 252 | True | False | True | True | False | `6c00d159876f9765d44112e5786424d55b72052514b78aa95437ec50e9d1669c` |
| `tools/run_rll_academic_claim_governance.py` | `True` | 170 | True | True | False | True | True | `b4ba4037d81d903974cfc2b3038e521fc8a41ddab9ec3ec7437785c3909031fd` |
| `tools/scan_rll_model_evidence.py` | `True` | 432 | True | True | False | True | True | `eb1581008d79aa89dae2f1c0b7e52d716c4c609ff91b1037c834fd21a486c870` |
| `tools/validate_academic_parameter_registry.py` | `True` | 170 | True | False | False | False | True | `772155c21ccf3995292130bfd7246545a4c9c00c3426c64e8f091aedd5e54424` |
| `tools/verify_real_source_signatures.py` | `True` | 238 | True | False | True | True | False | `725719b5cb87832a6798d185704da5b931cbd789db7d597c1315b693f4754171` |
| `validacao_real/compute_validation.py` | `True` | 254 | True | False | False | False | True | `59b80b7442a20e3f012366bf9adb46d78ff390579e7eec144e7441d82b67dfeb` |
| `validacao_real/fetch_real_data.py` | `True` | 83 | True | False | False | False | True | `54b0ab69d4fdbdfe28fbdc617688c30d3ace2ad6328788204c8781a0664ec28b` |
| `validacao_real/make_figures.py` | `True` | 147 | True | False | False | False | True | `67a904b17a99c899cc9597e702c80393e2f97a68b949d49073243c3c98b628bf` |
| `validacao_real/render_report.py` | `True` | 75 | True | False | False | False | True | `7dc4843df0a1f9e8b4fbe6f39d265375b8cc01dfaed87bf4bf899371784da276` |
