# WORKFLOW EXECUTION MAP

Gerado em: `2026-07-03T16:02:54Z`
Commit auditado: `929807336098e7edb7cfa2194dc2986fb6458deb`

## Mapa workflow -> job -> step -> script/comando

### `.github/workflows/RLL-CI.yml`

- name: `RLL Scientific CI Hardened`
- permissions: `"TOKEN_VAZIO"`
- inputs: `TOKEN_VAZIO`
- artifacts: `rll-scientific-results:validation_outputs/`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `rll` | `Install dependencies` | `TOKEN_VAZIO` | `pip install --upgrade pip pip install numpy pandas scipy emcee` | `TOKEN_VAZIO` |
| `rll` | `Prepare filesystem` | `TOKEN_VAZIO` | `mkdir -p validation_outputs mkdir -p data` | `TOKEN_VAZIO` |
| `rll` | `Set PYTHONPATH` | `TOKEN_VAZIO` | `echo "PYTHONPATH=." >> $GITHUB_ENV` | `TOKEN_VAZIO` |
| `rll` | `Run Bayesian calibration` | `TOKEN_VAZIO` | `python -m validation.bayes_rll python -m validation.bayes_compare` | `TOKEN_VAZIO` |
| `rll` | `Run LCDM baseline` | `TOKEN_VAZIO` | `python -m validation.run_lcdm` | `TOKEN_VAZIO` |
| `rll` | `Run RLL model` | `TOKEN_VAZIO` | `python -m validation.run_rll` | `TOKEN_VAZIO` |
| `rll` | `Compare models` | `TOKEN_VAZIO` | `python -m validation.compare_models` | `TOKEN_VAZIO` |
| `rll` | `Falsification test` | `TOKEN_VAZIO` | `python -m validation.check_falsification` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/RLL_SCIENTIFIC.yml`

- name: `RLL Scientific Validation Pipeline`
- permissions: `"TOKEN_VAZIO"`
- inputs: `TOKEN_VAZIO`
- artifacts: `rll-validation-results:validation_outputs/`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `rll-validation` | `Install dependencies` | `TOKEN_VAZIO` | `python -m pip install --upgrade pip pip install numpy scipy pandas matplotlib emcee astropy corner getdist` | `TOKEN_VAZIO` |
| `rll-validation` | `Load cosmological datasets` | `TOKEN_VAZIO` | `python validation/load_data.py` | `validation/load_data.py` |
| `rll-validation` | `Run ΛCDM baseline fit` | `TOKEN_VAZIO` | `python validation/run_lcdm.py --output validation_outputs/lcdm.json` | `validation/run_lcdm.py` |
| `rll-validation` | `Run RLL model (𝓡 = ΛCDM + β·𝓘)` | `TOKEN_VAZIO` | `python validation/run_rll.py --output validation_outputs/rll.json` | `validation/run_rll.py` |
| `rll-validation` | `Statistical comparison (χ² / AIC / BIC)` | `TOKEN_VAZIO` | `python validation/compare_models.py \ --lcdm validation_outputs/lcdm.json \ --rll validation_outputs/rll.json \ --output validation_outputs/comparison.json` | `validation/compare_models.py` |
| `rll-validation` | `Generate report plots` | `TOKEN_VAZIO` | `python validation/plot_results.py` | `validation/plot_results.py` |
| `rll-validation` | `Fail pipeline if RLL is invalid` | `TOKEN_VAZIO` | `python validation/check_falsification.py` | `validation/check_falsification.py` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

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
| `manual-start` | `Finalize canonical real-data policy checksums` | `TOKEN_VAZIO` | `set -euo pipefail ARTIFACT_DIR="artifacts/workflow-policy/START_MANUAL_HERE/${{ github.job }}" mkdir -p "$ARTIFACT_DIR" . tools/ci/real_data_workflow_policy.sh rll_real_data_write_claim_boundary "$ARTIFACT_DIR" rll_real_` | `tools/ci/real_data_workflow_policy.sh` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/academic-parameter-governance.yml`

- name: `Academic Parameter Governance`
- permissions: `{"contents": "read"}`
- inputs: `TOKEN_VAZIO`
- artifacts: `academic-parameter-governance-policy-${{ github.run_id }}-${{ github.job }}:artifacts/workflow-policy/academic-parameter-governance/${{ github.job }}/`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `validate-academic-parameter-registry` | `Validate registry JSON and academic governance invariants` | `TOKEN_VAZIO` | `python3 tools/validate_academic_parameter_registry.py` | `tools/validate_academic_parameter_registry.py` |
| `validate-academic-parameter-registry` | `Scan current RLL model evidence table` | `TOKEN_VAZIO` | `python3 tools/scan_rll_model_evidence.py --no-write` | `tools/scan_rll_model_evidence.py` |
| `validate-academic-parameter-registry` | `Run integrated academic claim governance wrapper` | `TOKEN_VAZIO` | `python3 tools/run_rll_academic_claim_governance.py --no-write` | `tools/run_rll_academic_claim_governance.py` |
| `validate-academic-parameter-registry` | `Validate H0/r_d ablation matrix generator` | `TOKEN_VAZIO` | `python3 tools/make_h0_rd_ablation_matrix.py --no-write` | `tools/make_h0_rd_ablation_matrix.py` |
| `validate-academic-parameter-registry` | `Validate outcome action protocol for all possible statuses` | `TOKEN_VAZIO` | `python3 tools/apply_rll_outcome_protocol.py --no-write --status CLAIM_BLOCKED python3 tools/apply_rll_outcome_protocol.py --no-write --status PASS_LIMITED python3 tools/apply_rll_outcome_protocol.py --no-write --status P` | `tools/apply_rll_outcome_protocol.py` |
| `validate-academic-parameter-registry` | `Print claim boundary reminder` | `TOKEN_VAZIO` | `echo "PASS: registry, evidence scanner, governance wrapper, ablation matrix and outcome protocol checks completed." echo "Reminder: this gate validates provenance, calculable evidence, ablation policy, outcome routing an` | `TOKEN_VAZIO` |
| `validate-academic-parameter-registry` | `Finalize canonical real-data policy checksums` | `TOKEN_VAZIO` | `set -euo pipefail ARTIFACT_DIR="artifacts/workflow-policy/academic-parameter-governance/${{ github.job }}" mkdir -p "$ARTIFACT_DIR" . tools/ci/real_data_workflow_policy.sh rll_real_data_write_claim_boundary "$ARTIFACT_DI` | `tools/ci/real_data_workflow_policy.sh` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/android-build.yml`

- name: `Android Build`
- permissions: `"TOKEN_VAZIO"`
- inputs: `TOKEN_VAZIO`
- artifacts: `rll-debug-apk:app/build/outputs/apk/debug/*.apk, rll-validation-unsigned-apk:app/build/outputs/apk/validationUnsigned/*.apk, rll-release-apk-signed:app/build/outputs/apk/release/*.apk, rll-release-aab-signed:app/build/outputs/bundle/release/*.aab`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `android` | `Install Android build components` | `TOKEN_VAZIO` | `sdkmanager "platforms;android-${ANDROID_COMPILE_SDK}" "build-tools;35.0.0" "ndk;${ANDROID_NDK_VERSION}" "cmake;${ANDROID_CMAKE_VERSION}"` | `TOKEN_VAZIO` |
| `android` | `Generate Gradle Wrapper JAR` | `TOKEN_VAZIO` | `scripts/bootstrap-gradle-wrapper.sh` | `scripts/bootstrap-gradle-wrapper.sh` |
| `android` | `Build debug unsigned APK` | `TOKEN_VAZIO` | `./gradlew --no-daemon :app:assembleDebug :app:assembleValidationUnsigned` | `TOKEN_VAZIO` |
| `android` | `Decode release keystore` | `TOKEN_VAZIO` | `mkdir -p "$RUNNER_TEMP/rll-signing" printf '%s' "${{ secrets.RLL_RELEASE_KEYSTORE_BASE64 }}" \| base64 --decode > "$RUNNER_TEMP/rll-signing/release.jks"` | `TOKEN_VAZIO` |
| `android` | `Build signed release APK and AAB` | `TOKEN_VAZIO` | `./gradlew --no-daemon :app:assembleRelease :app:bundleRelease` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-java@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `gradle/actions/setup-gradle@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `android-actions/setup-android@v3` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/bayes_analysis.yml`

- name: `Análise Bayesiana RLL vs ΛCDM`
- permissions: `"TOKEN_VAZIO"`
- inputs: `TOKEN_VAZIO`
- artifacts: `resultados-bayesianos:data/bayes_result.json | figs/model_comparison.png | figs/posterior_epsilon.png | `

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `run-bayes` | `Instalar dependências` | `TOKEN_VAZIO` | `python -m pip install --upgrade pip pip install numpy scipy matplotlib emcee dynesty tqdm` | `TOKEN_VAZIO` |
| `run-bayes` | `Executar pipeline Bayesiano` | `TOKEN_VAZIO` | `python src/run_full_analysis.py` | `src/run_full_analysis.py` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/calc-data.yml`

- name: `Calcular/Processar dados reais — guarded audit`
- permissions: `{"contents": "read"}`
- inputs: `input_path, output_name`
- artifacts: `${{ github.event.inputs.output_name }}:_audit/processed/`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `calc-audit` | `Install requirements` | `TOKEN_VAZIO` | `python -m pip install --upgrade pip && pip install pandas numpy` | `TOKEN_VAZIO` |
| `calc-audit` | `Run calculations in audit workspace` | `TOKEN_VAZIO` | `set -euo pipefail INPUT_PATH="${{ github.event.inputs.input_path }}" if [ ! -f "$INPUT_PATH" ]; then echo "Input file not found: $INPUT_PATH" >&2 echo "This guarded workflow does not fetch or commit raw data automaticall` | `scripts/calc_data.py` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/canonical-route-artifacts.yml`

- name: `Canonical Route Artifacts`
- permissions: `{"contents": "read"}`
- inputs: `export_mode`
- artifacts: `canonical-route-artifacts:data/real/bootstrap/canonical_route_checklist.yml | docs/science/CANONICAL_ROUTE_CHECKLIST.md | docs/science/TACTICAL_ROUTE_ORCHESTRATOR.md | docs/science/ROUTE_DEFIBRILLATION_POLICY.md | docs/science/PEER_REVIEW_READINESS_STATUS.md | docs/science/ROADMAP_NEXT_ACTIONS.md | data/raw/RAW_DATA_MANIFEST.yml | data/results/bootstrap/raw_data_manifest_status.json | data/results/bootstrap/raw_data_manifest_status.tsv | docs/science/RAW_DATA_MANIFEST_STATUS.md | data/real/orbital_dynamics/orbital_shape_angular_momentum_seed_v1.csv | data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.csv | data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.meta.yml | data/results/orbital_dynamics/orbital_state_vector_v2_validation.json | docs/science/ORBITAL_STATE_VECTOR_V2_REPORT.md | , route-artifact-checklist:data/real/bootstrap/canonical_route_checklist.yml | docs/science/CANONICAL_ROUTE_CHECKLIST.md | , route-artifact-raw-custody:data/raw/RAW_DATA_MANIFEST.yml | data/results/bootstrap/raw_data_manifest_status.json | data/results/bootstrap/raw_data_manifest_status.tsv | docs/science/RAW_DATA_MANIFEST_STATUS.md | docs/science/RAW_DATA_MANIFEST_GUIDE.md | , route-artifact-orbital-v2:data/real/orbital_dynamics/orbital_shape_angular_momentum_seed_v1.csv | data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.csv | data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.meta.yml | data/results/orbital_dynamics/orbital_state_vector_v2_validation.json | docs/science/ORBITAL_STATE_VECTOR_V2_REPORT.md | , route-artifact-orchestration-docs:docs/science/TACTICAL_ROUTE_ORCHESTRATOR.md | docs/science/ROUTE_DEFIBRILLATION_POLICY.md | docs/science/PEER_REVIEW_READINESS_STATUS.md | docs/science/ROADMAP_NEXT_ACTIONS.md | `

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `combined-artifact` | `Finalize canonical real-data policy checksums` | `TOKEN_VAZIO` | `set -euo pipefail ARTIFACT_DIR="artifacts/workflow-policy/canonical-route-artifacts/${{ github.job }}" mkdir -p "$ARTIFACT_DIR" . tools/ci/real_data_workflow_policy.sh rll_real_data_write_claim_boundary "$ARTIFACT_DIR" r` | `tools/ci/real_data_workflow_policy.sh` |
| `separated-artifacts` | `Finalize canonical real-data policy checksums` | `TOKEN_VAZIO` | `set -euo pipefail ARTIFACT_DIR="artifacts/workflow-policy/canonical-route-artifacts/${{ github.job }}" mkdir -p "$ARTIFACT_DIR" . tools/ci/real_data_workflow_policy.sh rll_real_data_write_claim_boundary "$ARTIFACT_DIR" r` | `tools/ci/real_data_workflow_policy.sh` |
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
- artifacts: `claim-boundary-quality-gates-policy-${{ github.run_id }}-${{ github.job }}:artifacts/workflow-policy/claim-boundary-quality-gates/${{ github.job }}/`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `claim-boundary-quality-gates` | `Install package and test dependencies` | `TOKEN_VAZIO` | `python -m pip install --upgrade pip python -m pip install -e . python -m pip install pytest` | `TOKEN_VAZIO` |
| `claim-boundary-quality-gates` | `Compile validation scripts` | `TOKEN_VAZIO` | `python -m py_compile scripts/validation/check_claim_boundary.py python -m py_compile scripts/validation/check_seed_artifact_contracts.py python -m py_compile scripts/validation/real_seed_utils.py python -m py_compile scr` | `scripts/validation/check_claim_boundary.py, scripts/validation/check_seed_artifact_contracts.py, scripts/validation/real_seed_utils.py, scripts/validation/validate_orbital_shape_angular_momentum.py` |
| `claim-boundary-quality-gates` | `Run claim boundary gate` | `TOKEN_VAZIO` | `python scripts/validation/check_claim_boundary.py` | `scripts/validation/check_claim_boundary.py` |
| `claim-boundary-quality-gates` | `Run artifact contract checks` | `TOKEN_VAZIO` | `python scripts/validation/check_seed_artifact_contracts.py` | `scripts/validation/check_seed_artifact_contracts.py` |
| `claim-boundary-quality-gates` | `Run unit tests` | `TOKEN_VAZIO` | `python -m pytest -q tests` | `TOKEN_VAZIO` |
| `claim-boundary-quality-gates` | `Finalize canonical real-data policy checksums` | `TOKEN_VAZIO` | `set -euo pipefail ARTIFACT_DIR="artifacts/workflow-policy/claim-boundary-quality-gates/${{ github.job }}" mkdir -p "$ARTIFACT_DIR" . tools/ci/real_data_workflow_policy.sh rll_real_data_write_claim_boundary "$ARTIFACT_DIR` | `tools/ci/real_data_workflow_policy.sh` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

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
| `build-dense-feature-matrix` | `Finalize canonical real-data policy checksums` | `TOKEN_VAZIO` | `set -euo pipefail ARTIFACT_DIR="artifacts/workflow-policy/dense-feature-matrix/${{ github.job }}" mkdir -p "$ARTIFACT_DIR" . tools/ci/real_data_workflow_policy.sh rll_real_data_write_claim_boundary "$ARTIFACT_DIR" rll_re` | `tools/ci/real_data_workflow_policy.sh` |
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
| `desi-dr2-bao` | `Finalize canonical real-data policy checksums` | `TOKEN_VAZIO` | `set -euo pipefail ARTIFACT_DIR="artifacts/workflow-policy/desi-dr2-bao-validation/${{ github.job }}" mkdir -p "$ARTIFACT_DIR" . tools/ci/real_data_workflow_policy.sh rll_real_data_write_claim_boundary "$ARTIFACT_DIR" rll` | `tools/ci/real_data_workflow_policy.sh` |
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
| `dha-fisher` | `Build mock catalog for ln(1+z) extraction` | `TOKEN_VAZIO` | `mkdir -p results/dha python - <<'PY2' import numpy as np, pandas as pd z = np.linspace(0.1, 6.0, 500) ln1pz = np.log1p(z) pk_baseline = 1000.0 * np.exp(-z/3.0) residual = 0.02 * np.cos(0.91 * ln1pz + 0.4) pk_obs = pk_bas` | `TOKEN_VAZIO` |
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

### `.github/workflows/import-data.yml`

- name: `Importar dados reais — guarded audit`
- permissions: `{"contents": "read"}`
- inputs: `output_name, real_data_url`
- artifacts: `${{ github.event.inputs.output_name }}:_audit/raw/`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `import-audit` | `Install requirements` | `TOKEN_VAZIO` | `python -m pip install --upgrade pip && pip install requests pandas` | `TOKEN_VAZIO` |
| `import-audit` | `Run synthetic detector as report-only guard` | `TOKEN_VAZIO` | `if [ -f scripts/detect_synthetic.py ]; then python scripts/detect_synthetic.py --report-only else echo "scripts/detect_synthetic.py not found; skipping report-only guard" fi` | `scripts/detect_synthetic.py` |
| `import-audit` | `Import explicit public data URL into audit workspace` | `TOKEN_VAZIO` | `set -euo pipefail mkdir -p _audit/raw python scripts/import_data.py --out _audit/raw/data.json --url "${{ github.event.inputs.real_data_url }}" python - <<'PY' from pathlib import Path import hashlib, json p = Path('_aud` | `scripts/import_data.py` |
| `import-audit` | `Finalize canonical real-data policy checksums` | `TOKEN_VAZIO` | `set -euo pipefail ARTIFACT_DIR="artifacts/workflow-policy/import-data/${{ github.job }}" mkdir -p "$ARTIFACT_DIR" . tools/ci/real_data_workflow_policy.sh rll_real_data_write_claim_boundary "$ARTIFACT_DIR" rll_real_data_a` | `tools/ci/real_data_workflow_policy.sh` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v4` | `TOKEN_VAZIO` |
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
| `validate-orbital-shape-angular-momentum` | `Finalize canonical real-data policy checksums` | `TOKEN_VAZIO` | `set -euo pipefail ARTIFACT_DIR="artifacts/workflow-policy/orbital-shape-angular-momentum-validation/${{ github.job }}" mkdir -p "$ARTIFACT_DIR" . tools/ci/real_data_workflow_policy.sh rll_real_data_write_claim_boundary "` | `tools/ci/real_data_workflow_policy.sh` |
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
| `orbital-state-vector-v2` | `Finalize canonical real-data policy checksums` | `TOKEN_VAZIO` | `set -euo pipefail ARTIFACT_DIR="artifacts/workflow-policy/orbital-state-vector-v2/${{ github.job }}" mkdir -p "$ARTIFACT_DIR" . tools/ci/real_data_workflow_policy.sh rll_real_data_write_claim_boundary "$ARTIFACT_DIR" rll` | `tools/ci/real_data_workflow_policy.sh` |
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
| `scan-real-data-bootstrap` | `Finalize canonical real-data policy checksums` | `TOKEN_VAZIO` | `set -euo pipefail ARTIFACT_DIR="artifacts/workflow-policy/real-data-bootstrap-validation/${{ github.job }}" mkdir -p "$ARTIFACT_DIR" . tools/ci/real_data_workflow_policy.sh rll_real_data_write_claim_boundary "$ARTIFACT_D` | `tools/ci/real_data_workflow_policy.sh` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/real-data-complete-execution.yml`

- name: `Real Data Complete Execution`
- permissions: `{"contents": "read"}`
- inputs: `execution_mode, materialize_pantheon, retention_days, run_pantheon_validation, run_structure_d, strict_real_data`
- artifacts: `real-data-complete-${{ github.run_id }}:artifacts/real-data-complete/`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `real-data-complete` | `Install runtime dependencies` | `TOKEN_VAZIO` | `set -euo pipefail python -m pip install --upgrade pip python -m pip install numpy pandas scipy matplotlib pyyaml requests jsonschema` | `TOKEN_VAZIO` |
| `real-data-complete` | `Create run plan and five-level repository inventory` | `TOKEN_VAZIO` | `set -euo pipefail mkdir -p "$RUN_DIR" "$RUN_DIR/reports" "$RUN_DIR/checks" cat > "$RUN_DIR/EXECUTION_PLAN.md" <<PLAN # Real Data Complete Execution - execution_mode: ${{ inputs.execution_mode }} - materialize_pantheon: $` | `TOKEN_VAZIO` |
| `real-data-complete` | `Validate real-data registry without rewriting committed data` | `TOKEN_VAZIO` | `set -euo pipefail python - <<'PY' \| tee "artifacts/real-data-complete/reports/real_data_policy_check.log" from pathlib import Path required = [ Path('docs/real_data/REAL_DATA_REQUIRED_INPUTS.md'), Path('docs/real_data/RL` | `TOKEN_VAZIO` |
| `real-data-complete` | `Materialize Pantheon+SH0ES official inputs` | `TOKEN_VAZIO` | `set -euo pipefail if [ "${{ inputs.materialize_pantheon }}" = "true" ]; then bash scripts/download_real_cosmology_inputs.sh \| tee "$RUN_DIR/reports/download_real_cosmology_inputs.log" else echo "Pantheon+ materialization` | `scripts/download_real_cosmology_inputs.sh` |
| `real-data-complete` | `Verify Pantheon+ inputs with strict failover` | `TOKEN_VAZIO` | `set -euo pipefail if python scripts/verify_pantheon_inputs.py --json > "$RUN_DIR/reports/pantheon_inputs.json"; then echo "Pantheon+ verification OK" \| tee "$RUN_DIR/reports/pantheon_inputs.status" else echo "Pantheon+ v` | `scripts/verify_pantheon_inputs.py` |
| `real-data-complete` | `Run real-source signature verification and materialization audit` | `TOKEN_VAZIO` | `set -euo pipefail python tools/verify_real_source_signatures.py \| tee "$RUN_DIR/reports/real_source_signature_verification.log" python tools/real_data_materialization_audit.py \| tee "$RUN_DIR/reports/real_data_materializ` | `tools/real_data_materialization_audit.py, tools/verify_real_source_signatures.py` |
| `real-data-complete` | `Run Structure-D real validation` | `TOKEN_VAZIO` | `set -euo pipefail python -m data.pipelines.structure_d.run_all_real \| tee "$RUN_DIR/reports/structure_d_real_validation.log" cp results/structure_d/model_comparison_real.csv "$RUN_DIR/reports/" \|\| true cp results/structu` | `TOKEN_VAZIO` |
| `real-data-complete` | `Run Pantheon+ real validation` | `TOKEN_VAZIO` | `set -euo pipefail if python scripts/run_real_pantheon_validation.py > "$RUN_DIR/reports/run_real_pantheon_validation.log" 2>&1; then echo "Pantheon+ real validation OK" \| tee "$RUN_DIR/reports/run_real_pantheon_validatio` | `scripts/run_real_pantheon_validation.py` |
| `real-data-complete` | `Build final report, checksums, and rollback manifest` | `TOKEN_VAZIO` | `set -euo pipefail mkdir -p "$RUN_DIR" python - <<'PY' import json from pathlib import Path root = Path('artifacts/real-data-complete') reports = sorted(str(path.relative_to(root)) for path in (root / 'reports').glob('*')` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/real-data-contract-ci.yml`

- name: `Real Data Contract CI`
- permissions: `{"contents": "read"}`
- inputs: `real_data_source`
- artifacts: `real-data-contract-${{ github.run_id }}:artifacts/real-data-contract/`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `real-data-contract` | `Install contract dependencies` | `TOKEN_VAZIO` | `python -m pip install --upgrade pip python -m pip install -r requirements.txt pytest pyyaml` | `TOKEN_VAZIO` |
| `real-data-contract` | `Generate and check inventory in CI workspace` | `TOKEN_VAZIO` | `set -euo pipefail python3 tools/docs_inventory.py python3 tools/docs_inventory.py --check` | `tools/docs_inventory.py` |
| `real-data-contract` | `Validate real cosmology YAML contract` | `TOKEN_VAZIO` | `python3 tools/validate_real_cosmology_inputs_yml.py` | `tools/validate_real_cosmology_inputs_yml.py` |
| `real-data-contract` | `Validate real dataset variance registry` | `TOKEN_VAZIO` | `python3 tools/validate_real_dataset_variance_registry.py` | `tools/validate_real_dataset_variance_registry.py` |
| `real-data-contract` | `Compute pipeline from committed real data` | `TOKEN_VAZIO` | `set -euo pipefail SOURCE="${{ github.event.inputs.real_data_source \|\| 'repo' }}" python3 scripts/compute_rll_real_pipeline.py \ --output-dir artifacts/real-data-contract \ --real-data-dir data/real \ --data-source "$SOUR` | `scripts/compute_rll_real_pipeline.py` |
| `real-data-contract` | `Validate contract outputs` | `TOKEN_VAZIO` | `set -euo pipefail test -s artifacts/real-data-contract/MANIFEST.json test -s artifacts/real-data-contract/COMPUTE_REPORT.md test -s artifacts/real-data-contract/tables/Hz_processed.csv test -s artifacts/real-data-contrac` | `TOKEN_VAZIO` |
| `real-data-contract` | `Run focused real-data tests` | `TOKEN_VAZIO` | `python -m pytest -q tests/test_compute_rll_real_pipeline_contract.py tests/test_desi_dr2_bao_materialized.py tests/test_structure_d_robust_fit_matrix.py` | `tests/test_compute_rll_real_pipeline_contract.py, tests/test_desi_dr2_bao_materialized.py, tests/test_structure_d_robust_fit_matrix.py` |
| `real-data-contract` | `Run raw JSON import tests` | `TOKEN_VAZIO` | `python -m pytest -q tests/test_import_raw_json_dataset_basic.py tests/test_import_raw_json_dataset_invalid.py tests/test_import_raw_json_dataset_rollback.py tests/test_import_raw_json_dataset_array.py` | `tests/test_import_raw_json_dataset_array.py, tests/test_import_raw_json_dataset_basic.py, tests/test_import_raw_json_dataset_invalid.py, tests/test_import_raw_json_dataset_rollback.py` |
| `real-data-contract` | `Finalize canonical real-data policy checksums` | `TOKEN_VAZIO` | `set -euo pipefail ARTIFACT_DIR="artifacts/workflow-policy/real-data-contract-ci/${{ github.job }}" mkdir -p "$ARTIFACT_DIR" . tools/ci/real_data_workflow_policy.sh rll_real_data_write_claim_boundary "$ARTIFACT_DIR" rll_r` | `tools/ci/real_data_workflow_policy.sh` |
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
| `build-real-seed-ingestion-plan` | `Finalize canonical real-data policy checksums` | `TOKEN_VAZIO` | `set -euo pipefail ARTIFACT_DIR="artifacts/workflow-policy/real-seed-ingestion-plan/${{ github.job }}" mkdir -p "$ARTIFACT_DIR" . tools/ci/real_data_workflow_policy.sh rll_real_data_write_claim_boundary "$ARTIFACT_DIR" rl` | `tools/ci/real_data_workflow_policy.sh` |
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
| `real-seed-validation-v0` | `Finalize canonical real-data policy checksums` | `TOKEN_VAZIO` | `set -euo pipefail ARTIFACT_DIR="artifacts/workflow-policy/real-seed-validation-v0/${{ github.job }}" mkdir -p "$ARTIFACT_DIR" . tools/ci/real_data_workflow_policy.sh rll_real_data_write_claim_boundary "$ARTIFACT_DIR" rll` | `tools/ci/real_data_workflow_policy.sh` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/repo-real-inventory.yml`

- name: `repo-real-inventory`
- permissions: `{"contents": "read"}`
- inputs: `TOKEN_VAZIO`
- artifacts: `repo-real-inventory-${{ github.run_id }}:docs/DOCUMENTATION_FULL_INVENTORY.md | docs/REAL_NUMBERS_REPORT.md | docs/YML_WORKFLOWS_INDEX.md | data/results/repo_inventory.json | data/results/repo_inventory.tsv | data/results/repo_inventory_summary.json | data/results/repo_inventory_checksums.sha256 | data/results/repo_inventory_commit_policy.txt | `

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `inventory` | `Generate real inventory from canonical tool` | `TOKEN_VAZIO` | `set -euo pipefail python3 tools/docs_inventory.py` | `tools/docs_inventory.py` |
| `inventory` | `Build inventory checksums and commit policy note` | `TOKEN_VAZIO` | `set -euo pipefail sha256sum docs/DOCUMENTATION_FULL_INVENTORY.md docs/REAL_NUMBERS_REPORT.md docs/YML_WORKFLOWS_INDEX.md data/results/repo_inventory.json data/results/repo_inventory.tsv data/results/repo_inventory_summar` | `TOKEN_VAZIO` |
| `inventory` | `Finalize canonical real-data policy checksums` | `TOKEN_VAZIO` | `set -euo pipefail ARTIFACT_DIR="artifacts/workflow-policy/repo-real-inventory/${{ github.job }}" mkdir -p "$ARTIFACT_DIR" . tools/ci/real_data_workflow_policy.sh rll_real_data_write_claim_boundary "$ARTIFACT_DIR" rll_rea` | `tools/ci/real_data_workflow_policy.sh` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/rll-book-data-pipeline.yml`

- name: `RLL Book Data Pipeline`
- permissions: `{"contents": "read"}`
- inputs: `book_scope, commit_artifacts, dataset_group, flush_artifact, mode, retention_days`
- artifacts: `rll-book-pipeline-${{ github.run_id }}-${{ inputs.book_scope }}-${{ inputs.dataset_group }}-${{ inputs.mode }}:artifacts/rll-pipeline/, rll-book-data-pipeline-policy-${{ github.run_id }}-${{ github.job }}:artifacts/workflow-policy/rll-book-data-pipeline/${{ github.job }}/`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `pipeline` | `Prepare artifact directory` | `TOKEN_VAZIO` | `if [ "${{ inputs.flush_artifact }}" = "true" ]; then rm -rf artifacts/rll-pipeline fi mkdir -p artifacts/rll-pipeline` | `TOKEN_VAZIO` |
| `pipeline` | `Docs inventory` | `TOKEN_VAZIO` | `python3 tools/docs_inventory.py python3 tools/docs_inventory.py --check` | `tools/docs_inventory.py` |
| `pipeline` | `Run canonical pipeline` | `TOKEN_VAZIO` | `python3 scripts/rll_pipeline.py \ --book-scope "${{ inputs.book_scope }}" \ --dataset-group "${{ inputs.dataset_group }}" \ --mode "${{ inputs.mode }}" \ --output-dir artifacts/rll-pipeline` | `scripts/rll_pipeline.py` |
| `pipeline` | `Runtime files + checksums` | `TOKEN_VAZIO` | `date -u +"%Y-%m-%dT%H:%M:%SZ" > artifacts/rll-pipeline/RUN_UTC.txt echo "${GITHUB_SHA}" > artifacts/rll-pipeline/COMMIT_SHA.txt printf '%s\n' "Commit is opt-in only via separate write-permission job; artifact upload is t` | `TOKEN_VAZIO` |
| `pipeline` | `Finalize canonical real-data policy checksums` | `TOKEN_VAZIO` | `set -euo pipefail ARTIFACT_DIR="artifacts/workflow-policy/rll-book-data-pipeline/${{ github.job }}" mkdir -p "$ARTIFACT_DIR" . tools/ci/real_data_workflow_policy.sh rll_real_data_write_claim_boundary "$ARTIFACT_DIR" rll_` | `tools/ci/real_data_workflow_policy.sh` |
| `commit-lightweight-artifacts` | `Commit lightweight artifacts` | `TOKEN_VAZIO` | `set -euo pipefail RUN_DIR="results/pipeline-runs/${{ github.run_id }}" mkdir -p "${RUN_DIR}" rsync -av --prune-empty-dirs \ --include='*/' \ --include='*.md' --include='*.json' --include='*.txt' --include='*.sha256' \ --` | `TOKEN_VAZIO` |
| `commit-lightweight-artifacts` | `Finalize canonical real-data policy checksums` | `TOKEN_VAZIO` | `set -euo pipefail ARTIFACT_DIR="artifacts/workflow-policy/rll-book-data-pipeline/${{ github.job }}" mkdir -p "$ARTIFACT_DIR" . tools/ci/real_data_workflow_policy.sh rll_real_data_write_claim_boundary "$ARTIFACT_DIR" rll_` | `tools/ci/real_data_workflow_policy.sh` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/download-artifact@v4` | `TOKEN_VAZIO` |
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
| `run` | `Runtime metadata` | `TOKEN_VAZIO` | `date -u +"%Y-%m-%dT%H:%M:%SZ" > artifacts/rll-pipeline/RUN_UTC.txt echo "${GITHUB_SHA}" > artifacts/rll-pipeline/COMMIT_SHA.txt printf '%s\n' "Commit is opt-in only via separate write-permission job; artifact upload is t` | `TOKEN_VAZIO` |
| `commit-lightweight-artifacts` | `Commit lightweight artifacts` | `TOKEN_VAZIO` | `set -euo pipefail RUN_DIR="results/pipeline-runs/${{ github.run_id }}" mkdir -p "$RUN_DIR" rsync -av --prune-empty-dirs \ --include='*/' \ --include='*.md' --include='*.json' --include='*.txt' --include='*.sha256' \ --ex` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/download-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/rll-real-data-orchestrator.yml`

- name: `RLL Real Data Orchestrator`
- permissions: `{"contents": "read"}`
- inputs: `book_scope, dataset_group, fetch_desi, fetch_igrf14, fetch_nmdb, fetch_omni, fetch_pantheon, fetch_planck, fetch_spenvis_reference, fetch_wmm2025, mode, pipeline_scope, real_data_source, retention_days, run_formulas, run_iml, run_plots`
- artifacts: `rll-real-run-${{ github.run_id }}:artifacts/rll-real-run/`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `orchestrate` | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `python -m pip install --upgrade pip pip install numpy pandas scipy matplotlib requests astropy pyyaml` | `TOKEN_VAZIO` |
| `orchestrate` | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `mkdir -p artifacts/rll-real-run/{raw,processed,plots,tables,book,iml,formulas,diagnostics,reports}` | `TOKEN_VAZIO` |
| `orchestrate` | `Refresh and validate repository inventory` | `TOKEN_VAZIO` | `set -euo pipefail python3 tools/docs_inventory.py \| tee artifacts/rll-real-run/docs_inventory_refresh.log python3 tools/docs_inventory.py --check \| tee artifacts/rll-real-run/docs_inventory_check.log` | `tools/docs_inventory.py` |
| `orchestrate` | `Fetch declared sources only when explicitly enabled` | `TOKEN_VAZIO` | `python3 scripts/fetch_real_sources.py \ --dataset-group "${{ inputs.dataset_group }}" \ --mode "${{ inputs.mode }}" \ --output-dir artifacts/rll-real-run \ ${{ inputs.fetch_igrf14 && '--fetch-igrf14' \|\| '--no-fetch-igrf1` | `scripts/fetch_real_sources.py` |
| `orchestrate` | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `python3 scripts/compute_rll_real_pipeline.py --output-dir artifacts/rll-real-run --data-source "${{ inputs.real_data_source }}"` | `scripts/compute_rll_real_pipeline.py` |
| `orchestrate` | `Run gap scan and RLL diagnostic artifacts` | `TOKEN_VAZIO` | `set -euo pipefail mkdir -p artifacts/rll-real-run/diagnostics artifacts/rll-real-run/tables artifacts/rll-real-run/reports python3 tools/scan_missing_placeholders.py \ --out-json artifacts/rll-real-run/diagnostics/missin` | `scripts/map_rll_to_w0wa_eff.py, scripts/run_h0_grid_expansion.py, tools/scan_missing_placeholders.py, tools/validate_to_add_migration.py` |
| `orchestrate` | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `python3 scripts/generate_rll_plots.py` | `scripts/generate_rll_plots.py` |
| `orchestrate` | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `python3 scripts/rll_pipeline.py --book-scope "${{ inputs.book_scope }}" --dataset-group "${{ inputs.dataset_group }}" --mode "${{ inputs.mode == 'full' && 'compute' \|\| inputs.mode }}" --output-dir artifacts/rll-real-run` | `scripts/rll_pipeline.py` |
| `orchestrate` | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `printf '{"dados":[1,2,3,4],"coerencia_in":0.7,"coerencia0":0.5,"entropia0":0.5,"estado":"ACTIVE"}\n' > artifacts/rll-real-run/iml/input.json python3 tools/iml/iml_pipeline.py --input artifacts/rll-real-run/iml/input.json` | `tools/iml/iml_pipeline.py` |
| `orchestrate` | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `python3 tools/formula_artifact_builder.py --outdir artifacts/rll-real-run/formulas` | `tools/formula_artifact_builder.py` |
| `orchestrate` | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `date -u +"%Y-%m-%dT%H:%M:%SZ" > artifacts/rll-real-run/RUN_UTC.txt git rev-parse HEAD > artifacts/rll-real-run/COMMIT_SHA.txt printf '%s\n' "This orchestrator is artifact-only. Commit artifacts through a reviewed PR, not` | `TOKEN_VAZIO` |
| `orchestrate` | `Finalize canonical real-data policy checksums` | `TOKEN_VAZIO` | `set -euo pipefail ARTIFACT_DIR="artifacts/workflow-policy/rll-real-data-orchestrator/${{ github.job }}" mkdir -p "$ARTIFACT_DIR" . tools/ci/real_data_workflow_policy.sh rll_real_data_write_claim_boundary "$ARTIFACT_DIR" ` | `tools/ci/real_data_workflow_policy.sh` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/six-sigma-real-data-controls.yml`

- name: `Six Sigma Real Data Controls`
- permissions: `{"contents": "read"}`
- inputs: `TOKEN_VAZIO`
- artifacts: `six-sigma-real-data-controls-policy-${{ github.run_id }}-${{ github.job }}:artifacts/workflow-policy/six-sigma-real-data-controls/${{ github.job }}/`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `six-sigma-real-data-controls` | `Validate Six Sigma real-data controls` | `TOKEN_VAZIO` | `python tools/validate_six_sigma_real_data_controls.py` | `tools/validate_six_sigma_real_data_controls.py` |
| `six-sigma-real-data-controls` | `Check documentation inventory` | `TOKEN_VAZIO` | `python3 tools/docs_inventory.py --check` | `tools/docs_inventory.py` |
| `six-sigma-real-data-controls` | `Finalize canonical real-data policy checksums` | `TOKEN_VAZIO` | `set -euo pipefail ARTIFACT_DIR="artifacts/workflow-policy/six-sigma-real-data-controls/${{ github.job }}" mkdir -p "$ARTIFACT_DIR" . tools/ci/real_data_workflow_policy.sh rll_real_data_write_claim_boundary "$ARTIFACT_DIR` | `tools/ci/real_data_workflow_policy.sh` |
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
- permissions: `{"contents": "read"}`
- inputs: `commit_results, note`
- artifacts: `validacao-real-artifacts:validacao_real/fetched/ | validacao_real/results/ | , validacao_real-policy-${{ github.run_id }}-${{ github.job }}:artifacts/workflow-policy/validacao_real/${{ github.job }}/`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `validate` | `Install minimal deps` | `TOKEN_VAZIO` | `pip install pyyaml matplotlib` | `TOKEN_VAZIO` |
| `validate` | `Fetch/materialize declared data anchors with explicit fallback boundary` | `validacao_real` | `python3 fetch_real_data.py` | `validacao_real/fetch_real_data.py` |
| `validate` | `Check fallback provenance boundary` | `TOKEN_VAZIO` | `set -euo pipefail python - <<'PY' import json from pathlib import Path manifest = json.loads(Path('validacao_real/fetched/manifest.json').read_text(encoding='utf-8')) boundary = manifest.get('claim_boundary', '') require` | `TOKEN_VAZIO` |
| `validate` | `Compute validation (chi2 / AIC / BIC / falsifiability)` | `validacao_real` | `python3 compute_validation.py` | `validacao_real/compute_validation.py` |
| `validate` | `Generate figures` | `validacao_real` | `python3 make_figures.py` | `validacao_real/make_figures.py` |
| `validate` | `Render documentation from artifacts` | `validacao_real` | `python3 render_report.py` | `validacao_real/render_report.py` |
| `validate` | `Build artifact checksums` | `TOKEN_VAZIO` | `set -euo pipefail find validacao_real/fetched validacao_real/results -type f -print0 \| sort -z \| xargs -0 -r sha256sum > validacao_real/results/CHECKSUMS.sha256` | `TOKEN_VAZIO` |
| `validate` | `Finalize canonical real-data policy checksums` | `TOKEN_VAZIO` | `set -euo pipefail ARTIFACT_DIR="artifacts/workflow-policy/validacao_real/${{ github.job }}" mkdir -p "$ARTIFACT_DIR" . tools/ci/real_data_workflow_policy.sh rll_real_data_write_claim_boundary "$ARTIFACT_DIR" rll_real_dat` | `tools/ci/real_data_workflow_policy.sh` |
| `commit-results` | `Commit results back to repo only by explicit opt-in` | `TOKEN_VAZIO` | `set -euo pipefail git config user.name "github-actions[bot]" git config user.email "41898282+github-actions[bot]@users.noreply.github.com" git add validacao_real/fetched validacao_real/results if git diff --cached --quie` | `TOKEN_VAZIO` |
| `commit-results` | `Finalize canonical real-data policy checksums` | `TOKEN_VAZIO` | `set -euo pipefail ARTIFACT_DIR="artifacts/workflow-policy/validacao_real/${{ github.job }}" mkdir -p "$ARTIFACT_DIR" . tools/ci/real_data_workflow_policy.sh rll_real_data_write_claim_boundary "$ARTIFACT_DIR" rll_real_dat` | `tools/ci/real_data_workflow_policy.sh` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/download-artifact@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/validate-academic-correlation-package.yml`

- name: `Validate Academic Correlation Package`
- permissions: `{"contents": "read"}`
- inputs: `TOKEN_VAZIO`
- artifacts: `TOKEN_VAZIO`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `validate-academic-correlation-package` | `Install lightweight dependencies` | `TOKEN_VAZIO` | `python -m pip install --upgrade pip PyYAML` | `TOKEN_VAZIO` |
| `validate-academic-correlation-package` | `Validate academic correlation package` | `TOKEN_VAZIO` | `python tools/validate_academic_correlation_package.py` | `tools/validate_academic_correlation_package.py` |
| `validate-academic-correlation-package` | `Run focused tests` | `TOKEN_VAZIO` | `python -m pytest -q tests/test_academic_correlation_package_validator.py tests/test_numeric_representation_semantics.py` | `tests/test_academic_correlation_package_validator.py, tests/test_numeric_representation_semantics.py` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |

### `.github/workflows/validate-cross-repo-relationship-registry.yml`

- name: `Validate Cross-Repo Relationship Registry`
- permissions: `{"contents": "read"}`
- inputs: `TOKEN_VAZIO`
- artifacts: `TOKEN_VAZIO`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `validate-cross-repo-relationship-registry` | `Validate registry` | `TOKEN_VAZIO` | `python tools/validate_cross_repo_relationship_registry.py` | `tools/validate_cross_repo_relationship_registry.py` |
| `validate-cross-repo-relationship-registry` | `Run registry tests` | `TOKEN_VAZIO` | `python -m pytest -q tests/test_cross_repo_relationship_registry.py` | `tests/test_cross_repo_relationship_registry.py` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |

### `.github/workflows/validate-real-dataset-variance-registry.yml`

- name: `Validate Real Dataset Variance Registry`
- permissions: `{"contents": "read"}`
- inputs: `TOKEN_VAZIO`
- artifacts: `validate-real-dataset-variance-registry-policy-${{ github.run_id }}-${{ github.job }}:artifacts/workflow-policy/validate-real-dataset-variance-registry/${{ github.job }}/`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `validate-real-dataset-variance-registry` | `Validate registry structure` | `TOKEN_VAZIO` | `python tools/validate_real_dataset_variance_registry.py` | `tools/validate_real_dataset_variance_registry.py` |
| `validate-real-dataset-variance-registry` | `Finalize canonical real-data policy checksums` | `TOKEN_VAZIO` | `set -euo pipefail ARTIFACT_DIR="artifacts/workflow-policy/validate-real-dataset-variance-registry/${{ github.job }}" mkdir -p "$ARTIFACT_DIR" . tools/ci/real_data_workflow_policy.sh rll_real_data_write_claim_boundary "$A` | `tools/ci/real_data_workflow_policy.sh` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/validate-schema-contracts.yml`

- name: `Validate Schema Contracts`
- permissions: `{"contents": "read"}`
- inputs: `TOKEN_VAZIO`
- artifacts: `TOKEN_VAZIO`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `validate-schema-contracts` | `Validate root schema claim boundaries` | `TOKEN_VAZIO` | `python tools/validate_schemas_claim_boundary.py` | `tools/validate_schemas_claim_boundary.py` |
| `validate-schema-contracts` | `Run schema validator tests` | `TOKEN_VAZIO` | `python -m pytest -q tests/test_schemas_claim_boundary.py` | `tests/test_schemas_claim_boundary.py` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |

### `.github/workflows/validate-sequence-metrics.yml`

- name: `Validate sequence metrics calculator`
- permissions: `{"contents": "read"}`
- inputs: `TOKEN_VAZIO`
- artifacts: `validate-sequence-metrics-policy-${{ github.run_id }}-${{ github.job }}:artifacts/workflow-policy/validate-sequence-metrics/${{ github.job }}/`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `validate-sequence-metrics` | `Run targeted tests` | `TOKEN_VAZIO` | `python -m pytest -q tests/test_calculate_sequence_metrics.py` | `tests/test_calculate_sequence_metrics.py` |
| `validate-sequence-metrics` | `Finalize canonical real-data policy checksums` | `TOKEN_VAZIO` | `set -euo pipefail ARTIFACT_DIR="artifacts/workflow-policy/validate-sequence-metrics/${{ github.job }}" mkdir -p "$ARTIFACT_DIR" . tools/ci/real_data_workflow_policy.sh rll_real_data_write_claim_boundary "$ARTIFACT_DIR" r` | `tools/ci/real_data_workflow_policy.sh` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

### `.github/workflows/yml-syntax-validation.yml`

- name: `YAML Syntax Validation Gate`
- permissions: `{"contents": "read"}`
- inputs: `TOKEN_VAZIO`
- artifacts: `yml-syntax-validation-${{ github.run_id }}:artifacts/yml-syntax-validation/`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `validate-yaml` | `Install PyYAML` | `TOKEN_VAZIO` | `python -m pip install --upgrade pip pyyaml` | `TOKEN_VAZIO` |
| `validate-yaml` | `Validate every YAML file with a real parser` | `TOKEN_VAZIO` | `mkdir -p artifacts/yml-syntax-validation python - <<'PY' from pathlib import Path import json import yaml import sys import hashlib out_dir = Path('artifacts/yml-syntax-validation') out_dir.mkdir(parents=True, exist_ok=T` | `TOKEN_VAZIO` |
| `validate-yaml` | `Validate workflow isolation (repo audit tool)` | `TOKEN_VAZIO` | `mkdir -p artifacts/yml-syntax-validation set +e python3 tools/audit_github_workflows.py --strict \| tee artifacts/yml-syntax-validation/workflow_audit.log status=${PIPESTATUS[0]} python - <<PY import json from pathlib imp` | `tools/audit_github_workflows.py` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/upload-artifact@v4` | `TOKEN_VAZIO` |

## Scripts chamados por workflows

| script | existe | linhas | main | argparse | checksum | termo boundary | erro explícito | sha256 |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `scripts/bootstrap-gradle-wrapper.sh` | `True` | 24 | False | False | False | False | False | `2cc8f527626c93ea9e88099386380d5dbe014a67daeed5639873f9bffa24671b` |
| `scripts/calc_data.py` | `True` | 62 | True | True | False | True | True | `51bea4266bb8cacbb5af8c0c8f11ffed6f7a4b23c265fdade556c6841947d49f` |
| `scripts/check_convention_conflicts.sh` | `True` | 47 | False | False | False | False | False | `ea5f6c1e04d29db39afefd37f461203aa3868f2d28f97265d8658b8c54f266d3` |
| `scripts/check_desi_dr2_bao_covariance.py` | `True` | 133 | True | True | False | False | True | `25337be7feb5fc620bc607eb65b508ea76812112e9a86139d61851c8673d2774` |
| `scripts/check_structure_d_model_dataset_coverage.sh` | `True` | 77 | False | False | False | False | True | `335c71a5b8b04925eab3b142215bc5e1c98b3255a5f0f626e185c4d2d9241b5b` |
| `scripts/check_structure_d_required_outputs.sh` | `True` | 72 | False | False | False | False | True | `ad980b2c79fba82b949f18b3bb0337ee34d0b40abcf1106e7d3d40efcec55684` |
| `scripts/compute_rll_real_pipeline.py` | `True` | 421 | True | True | True | True | True | `35bb1dec24e1446656452ace08e2bcd04df5b8e70509c4df942d7946edddaf59` |
| `scripts/data_scan/build_dense_behavior_features.py` | `True` | 223 | True | False | True | True | True | `3713cde17ecc3f14e20876ffc16868a96f92c161bb9f69964458e6ea7245cde8` |
| `scripts/data_scan/build_raw_data_manifest_status.py` | `True` | 171 | True | False | True | True | True | `ef80beab6c4e9e13366a31404f7b1ea5cbac86548172b13700e8a1d12379e441` |
| `scripts/data_scan/build_real_seed_ingestion_plan.py` | `True` | 198 | True | False | True | True | True | `06375c67a2281da0c712aba3e90fcbe2cbcef49a74797136b43296196056aa4e` |
| `scripts/data_scan/fetch_horizons_mars_state_vector.py` | `True` | 140 | True | False | True | True | True | `31d21ead694019cfd415d0867c2a94d14611d39cc68346cc4e9c50b78c68f77a` |
| `scripts/data_scan/scan_real_data_bootstrap.py` | `True` | 264 | True | True | True | True | True | `9f95fdb094ff2c99d22f457fed9fc835e032e376ca3c4cb5b9711435cb6c5ec0` |
| `scripts/detect_synthetic.py` | `True` | 70 | True | True | False | True | False | `630d51332abd8aeb7878495eec419dd724cb2a35c3284df63f2fd401e39fe2bb` |
| `scripts/download_real_cosmology_inputs.sh` | `True` | 96 | False | False | True | True | False | `4992ea82ab448ad775d65391021694a256a97e99e3e224556f4629a4a5b2e0a3` |
| `scripts/export_dha_forecast.py` | `True` | 23 | True | False | False | False | False | `5718403bbcafbac5369312542e8bda7f2a58bcbb7eb9887a9d87ada4897b941d` |
| `scripts/fetch_real_sources.py` | `True` | 310 | True | True | True | True | True | `2c6e606ac530ffef24efc4c5753d3a2bcc3cddf8d63e49fbe8bfa591256e4b2a` |
| `scripts/generate_rll_plots.py` | `True` | 25 | True | False | False | False | True | `e67151201d5735e4111f38415f91664f3d946b704b2bed29b23258085af03a5a` |
| `scripts/import_data.py` | `True` | 76 | True | True | False | False | True | `858cfbfd41367c2d6cf688117329d3df490cc441ec37aa7a824deb31dae9ade3` |
| `scripts/map_rll_to_w0wa_eff.py` | `True` | 126 | True | True | False | False | True | `10b36651a7e217db7e737cf91b63cac98cbe6494f935cf55e918efb745ffd078` |
| `scripts/materialize_formula_index.py` | `True` | 118 | True | True | True | True | True | `5ddbab5d531c83d2ce6c71f8159ceebf5c8d5755daab2e4264d0be591e9e142c` |
| `scripts/rll_pipeline.py` | `True` | 265 | True | True | False | True | True | `4c5b0165359e00da84efc162a5e157385e613e2fe6ad3aa47f7e1c426c4f0331` |
| `scripts/run_desi_dha_pipeline.py` | `True` | 29 | True | True | False | False | False | `807d6d435278ab80841acfef34bba13a5a9a40380bfef0b921384430ef487dfc` |
| `scripts/run_h0_grid_expansion.py` | `True` | 166 | True | True | False | False | True | `375af92e9022388801b523fa37a79915a2ae40bf02537ab34801e3b01a438980` |
| `scripts/run_ln1pz_extractor.py` | `True` | 29 | True | True | False | False | False | `cff817d088572073e91ce546e3c41bdf847f75cdb5e61ae4ea9fedf5bfb6698f` |
| `scripts/run_real_pantheon_validation.py` | `True` | 385 | True | True | True | False | True | `23da65099760dfb8a32b135f7bb99aded56146a55e066ae2dbd9ade5283ca0ec` |
| `scripts/smoke_desi_dr2_bao_covariance_loader.py` | `True` | 35 | True | False | False | False | False | `a76fd5d1499094cabce27bc6c77614960a786303bb407430b48734c8f55c4b40` |
| `scripts/unified_geometry_system.py` | `True` | 120 | True | True | False | False | True | `e37b8de7fbc82ecccce19f613e86c1fc82b4566ca315ead35be54908eb5f59b6` |
| `scripts/validate_formula_index_contract.py` | `True` | 16 | False | False | False | False | False | `b2c5c0379deb67e4883310ed117133fdc6311479900fffdaea3e7ac6ca5716e4` |
| `scripts/validate_formulas_manifest.py` | `True` | 33 | False | False | True | False | False | `f179806e3f03eaa87831dd3e8deaffa6485c5e64121158283c756ca8cf035f7d` |
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
| `scripts/verify_pantheon_inputs.py` | `True` | 101 | True | True | True | False | True | `73b4b0701caf3100a252ca0fef530f83166a6e5d444cf410e3a6cb3842e4e036` |
| `src/run_full_analysis.py` | `True` | 212 | True | False | False | True | False | `6b1f51d489ff120079aeff32a9131d611f126564a9e97e61fa7b458fc60bbfab` |
| `tests/test_academic_correlation_package_validator.py` | `True` | 22 | False | False | False | False | False | `9900756d2ff4395f0044b21ee9ab0ccf043d6bfb21f2a33f867e02675e743e84` |
| `tests/test_calculate_sequence_metrics.py` | `True` | 59 | False | False | False | True | True | `a43a69da5fd8d12bc21da3790cf53ced46392f913762c0da31c063fe940e974a` |
| `tests/test_compute_rll_real_pipeline_contract.py` | `True` | 136 | False | False | True | True | False | `651bc731bf343a4a3e73811c738622fe75e23e73764b54f3217c7b50413921d8` |
| `tests/test_cross_repo_relationship_registry.py` | `True` | 41 | False | False | False | False | False | `416908cf8837b9f45af63caf0d72eadd1b7205d7ca6f4dbda62f59298b4d6fd7` |
| `tests/test_desi_dha_extractor.py` | `True` | 11 | False | False | False | False | False | `056cef79bc6e86084747710dfd49da08e2296bc5bf29ce4c805841ea093bc009` |
| `tests/test_desi_dr2_bao_covariance_loader.py` | `True` | 38 | True | False | False | False | False | `bf166aa39a7ae145a74b0cc5b82af9281575d157fae8c92acf818e1a0ba7194f` |
| `tests/test_desi_dr2_bao_materialized.py` | `True` | 37 | False | False | False | False | False | `4cc0249fe150adb866989be7bcb3cb9d615ed998418bf7a55c3a0ae9792696c4` |
| `tests/test_dha_fisher.py` | `True` | 22 | False | False | False | False | False | `54612a5ab5bbf91096be8d6f0c45405afc6b3eb3a779df67f11cf727d66acfe0` |
| `tests/test_import_raw_json_dataset_array.py` | `True` | 18 | False | False | False | False | False | `a643f44052d15a4783ee7be0f0876e494ae730b13ff4366687936df485395814` |
| `tests/test_import_raw_json_dataset_basic.py` | `True` | 27 | False | False | True | False | False | `a9c44efc102a006965d17baa7867695e9b5b25bc9330090c7e31436d6d1e305e` |
| `tests/test_import_raw_json_dataset_invalid.py` | `True` | 24 | False | False | False | False | True | `29cb7c3218c98a05001d353fcf82bddb8ac8edc975a13a15551a811aa9c630c4` |
| `tests/test_import_raw_json_dataset_rollback.py` | `True` | 23 | False | False | False | False | False | `d0e3fcfbec2940f8072beaf3703687515b781d2ad43d38673f91cba2c31f47b5` |
| `tests/test_ln1pz_extractor.py` | `True` | 32 | False | False | False | False | False | `99f07f4c1fe823b5fe9491605cb6eebd8f21e64e6480387bf7e205acd1d04416` |
| `tests/test_numeric_representation_semantics.py` | `True` | 31 | False | False | False | False | False | `06b30a25c34e1af61db80a47b6c3eae28d2889003379f328bd87e54f7442f4fa` |
| `tests/test_schemas_claim_boundary.py` | `True` | 27 | False | False | False | False | False | `a3fc9a9a92dd495ad26835abdb5fa80dcb8dd03001207853f741a7b1044f73d1` |
| `tests/test_structure_d_robust_fit_matrix.py` | `True` | 115 | False | False | False | False | False | `a317362084d35a9bdff1e937d5755a378f7079893d665589abb5787af11f305c` |
| `tools/apply_rll_outcome_protocol.py` | `True` | 355 | True | True | False | True | True | `096e814399af199e2ac7319c0127ce307f7350f4fde1a213d1fb3b4034c9d158` |
| `tools/audit_github_workflows.py` | `True` | 182 | True | True | True | True | True | `bce18d161278410b9491c26328da42c2db62ab192ac8df641f4023036eeaa716` |
| `tools/ci/real_data_workflow_policy.sh` | `True` | 32 | False | False | True | True | False | `25ab729d133049fbdf53aec81b1394a3ecaa61d909909b1b0e65d623f2beac82` |
| `tools/docs_inventory.py` | `True` | 470 | True | True | True | True | True | `a47657bad2c32fa66d9820e55f0db25172b6668bcc71f53637053634ebfd121f` |
| `tools/formula_artifact_builder.py` | `True` | 51 | True | True | False | False | False | `adc0f0eae76f4dfba28e2dbe4f449d27fe3433f80d8a1c7853dfbef98c3eb548` |
| `tools/iml/iml_pipeline.py` | `True` | 43 | True | True | True | False | False | `73dfa54829abaf7df43a453501ad3ae38dad571f588222315831d141a0b1daa1` |
| `tools/make_h0_rd_ablation_matrix.py` | `True` | 148 | True | True | False | True | False | `e3cfd4b334184335ec8c3136e39f7fcda22573bf5758214e9d6b998fa52259f4` |
| `tools/real_data_materialization_audit.py` | `True` | 252 | True | False | True | True | False | `6c00d159876f9765d44112e5786424d55b72052514b78aa95437ec50e9d1669c` |
| `tools/run_rll_academic_claim_governance.py` | `True` | 170 | True | True | False | True | True | `b4ba4037d81d903974cfc2b3038e521fc8a41ddab9ec3ec7437785c3909031fd` |
| `tools/scan_missing_placeholders.py` | `True` | 204 | True | True | True | True | True | `96a6baa33e1d57c4e908b672319a4fa584b42a7dc4121ff985d9501f810968a6` |
| `tools/scan_rll_model_evidence.py` | `True` | 432 | True | True | False | True | True | `eb1581008d79aa89dae2f1c0b7e52d716c4c609ff91b1037c834fd21a486c870` |
| `tools/validate_academic_correlation_package.py` | `True` | 235 | True | True | False | True | True | `d0f485700bf72cafe9669da7af641142b6d1a58d19a540bcdd4c0655602c3e71` |
| `tools/validate_academic_parameter_registry.py` | `True` | 170 | True | False | False | False | True | `772155c21ccf3995292130bfd7246545a4c9c00c3426c64e8f091aedd5e54424` |
| `tools/validate_cross_repo_relationship_registry.py` | `True` | 111 | True | False | False | True | True | `60a14a772df88cbb3b58d522ea66a75bac4650b670de4925516c3466c201a64b` |
| `tools/validate_real_cosmology_inputs_yml.py` | `True` | 201 | True | False | False | True | True | `d16d59390dba1068db97db1b6cd317762a94971a1bb0850a91cc17e586f83245` |
| `tools/validate_real_dataset_variance_registry.py` | `True` | 68 | True | False | False | False | True | `b14c1f21ea94d82f38701d1edde5d1f81fe0f9985da4275fdfa2948be908d71b` |
| `tools/validate_schemas_claim_boundary.py` | `True` | 95 | True | False | False | False | True | `fa0da2f8671a0aa1adb0c124e8af76dae3dbf71d2763879abc2a0cd668599f01` |
| `tools/validate_six_sigma_real_data_controls.py` | `True` | 59 | True | False | True | False | True | `f9792c03f83584cb1207701ae4007ad48abf0d03ea7daf38830896abe9f862bb` |
| `tools/validate_to_add_migration.py` | `True` | 109 | True | False | False | True | True | `55785d17ea9cfad968854baebacee3effd5e99d112063d8eea8843b92ff88671` |
| `tools/verify_real_source_signatures.py` | `True` | 245 | True | False | True | True | False | `b99542ae13ff07580b4546ce878af8272c5d65f419f277d28b3dbf5a142d2f05` |
| `validacao_real/compute_validation.py` | `True` | 254 | True | False | False | False | True | `59b80b7442a20e3f012366bf9adb46d78ff390579e7eec144e7441d82b67dfeb` |
| `validacao_real/fetch_real_data.py` | `True` | 108 | True | False | False | False | True | `7f8b45032839cb98f03cc9c9d21c7344f7448f6fae3f724a9cfd0b4b03def587` |
| `validacao_real/make_figures.py` | `True` | 147 | True | False | False | False | True | `67a904b17a99c899cc9597e702c80393e2f97a68b949d49073243c3c98b628bf` |
| `validacao_real/render_report.py` | `True` | 75 | True | False | False | False | True | `7dc4843df0a1f9e8b4fbe6f39d265375b8cc01dfaed87bf4bf899371784da276` |
| `validation/check_falsification.py` | `True` | 19 | False | False | False | False | False | `f7f391f21291660e19d05b57dd8c39b57c94fc058e40470727ae7c9cbfae11ef` |
| `validation/compare_models.py` | `True` | 38 | True | False | False | False | False | `78d03391f066770760362457ff3c6157ef818f19fbd8cca7072e589e398b2e68` |
| `validation/load_data.py` | `True` | 50 | False | False | False | True | True | `a024b22eae89ad54647f44b3431520f12368a04d412acff4849926cefab61424` |
| `validation/plot_results.py` | `True` | 36 | True | False | False | True | True | `44d938f4f3847c91297dab8fc54db568e9ba49012b8ad383335e0bda2da673cd` |
| `validation/run_lcdm.py` | `True` | 27 | True | False | False | False | False | `7080916cc36202f5b91b7153643ca02c6e7c49feea8162a2d23e0aefc93c24a3` |
| `validation/run_rll.py` | `True` | 27 | True | False | False | False | False | `a03389171a5d9fa2f4d3b7d72520dd2495ba19ae837a8b70a43111211446a2af` |
