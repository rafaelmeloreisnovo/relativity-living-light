# WORKFLOW EXECUTION MAP

Gerado em: `2026-06-13T06:12:53Z`
Commit auditado: `c8eb1047ada81ee2a1f6eb4c917ae707fdee8e4f`

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

### `.github/workflows/python-tests.yml`

- name: `Python tests`
- permissions: `{"contents": "read"}`
- inputs: `TOKEN_VAZIO`
- artifacts: `TOKEN_VAZIO`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `test` | `Install package and test dependencies` | `TOKEN_VAZIO` | `python -m pip install --upgrade pip pip install -e . python -m pip install pytest` | `TOKEN_VAZIO` |
| `test` | `Run tests` | `TOKEN_VAZIO` | `pytest -q` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/setup-python@v5` | `TOKEN_VAZIO` |

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

### `.github/workflows/repo-real-inventory.yml`

- name: `repo-real-inventory`
- permissions: `{"contents": "write"}`
- inputs: `TOKEN_VAZIO`
- artifacts: `TOKEN_VAZIO`

| job | step | working-directory | comando | scripts detectados |
|---|---|---|---|---|
| `inventory` | `Generate real inventory from git tracked files` | `TOKEN_VAZIO` | `set -euo pipefail mkdir -p docs data/results python3 - <<'PY' from __future__ import annotations import csv, hashlib, json, math, os, subprocess from collections import Counter, defaultdict from datetime import datetime,` | `TOKEN_VAZIO` |
| `inventory` | `Commit generated real inventory` | `TOKEN_VAZIO` | `set -euo pipefail git config user.name "github-actions[bot]" git config user.email "41898282+github-actions[bot]@users.noreply.github.com" git add docs/DOCUMENTATION_FULL_INVENTORY.md docs/REAL_NUMBERS_REPORT.md docs/YML` | `TOKEN_VAZIO` |
| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `actions/checkout@v4` | `TOKEN_VAZIO` |

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
| `orchestrate` | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `python -m pip install --upgrade pip pip install numpy pandas scipy matplotlib requests astropy` | `TOKEN_VAZIO` |
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
| `scripts/check_structure_d_model_dataset_coverage.sh` | `True` | 74 | False | False | False | False | True | `0ff1934ae15fc3bbb824438e38daf5b8768ecd3b10648ddcd48544fa1c9397ad` |
| `scripts/check_structure_d_required_outputs.sh` | `True` | 72 | False | False | False | False | True | `ad980b2c79fba82b949f18b3bb0337ee34d0b40abcf1106e7d3d40efcec55684` |
| `scripts/compute_rll_real_pipeline.py` | `True` | 234 | True | True | True | True | True | `0631deffe52a6e6a66b343e7f5903efb7e83463653e1a75875dbc81752d231bd` |
| `scripts/download_real_cosmology_inputs.sh` | `True` | 96 | False | False | True | True | False | `4992ea82ab448ad775d65391021694a256a97e99e3e224556f4629a4a5b2e0a3` |
| `scripts/export_dha_forecast.py` | `True` | 23 | True | False | False | False | False | `5718403bbcafbac5369312542e8bda7f2a58bcbb7eb9887a9d87ada4897b941d` |
| `scripts/fetch_real_sources.py` | `True` | 310 | True | True | True | True | True | `2c6e606ac530ffef24efc4c5753d3a2bcc3cddf8d63e49fbe8bfa591256e4b2a` |
| `scripts/generate_rll_plots.py` | `True` | 25 | True | False | False | False | True | `e67151201d5735e4111f38415f91664f3d946b704b2bed29b23258085af03a5a` |
| `scripts/rll_pipeline.py` | `True` | 265 | True | True | False | True | True | `4c5b0165359e00da84efc162a5e157385e613e2fe6ad3aa47f7e1c426c4f0331` |
| `scripts/run_desi_dha_pipeline.py` | `True` | 29 | True | True | False | False | False | `807d6d435278ab80841acfef34bba13a5a9a40380bfef0b921384430ef487dfc` |
| `scripts/run_ln1pz_extractor.py` | `True` | 29 | True | True | False | False | False | `cff817d088572073e91ce546e3c41bdf847f75cdb5e61ae4ea9fedf5bfb6698f` |
| `scripts/run_real_pantheon_validation.py` | `True` | 290 | True | True | True | False | True | `7866fc213c097175d5bf8b6fdb2f0138dbe3abfa9f892f31f0200cd93332eea2` |
| `scripts/unified_geometry_system.py` | `True` | 120 | True | True | False | False | True | `e37b8de7fbc82ecccce19f613e86c1fc82b4566ca315ead35be54908eb5f59b6` |
| `scripts/verify_pantheon_inputs.py` | `True` | 86 | True | True | True | False | True | `91c8a358cc2320fe0d23d2955c29b9daeb6648baaadbe90a6414993da678ab4f` |
| `tests/test_desi_dha_extractor.py` | `True` | 11 | False | False | False | False | False | `056cef79bc6e86084747710dfd49da08e2296bc5bf29ce4c805841ea093bc009` |
| `tests/test_dha_fisher.py` | `True` | 22 | False | False | False | False | False | `54612a5ab5bbf91096be8d6f0c45405afc6b3eb3a779df67f11cf727d66acfe0` |
| `tests/test_ln1pz_extractor.py` | `True` | 32 | False | False | False | False | False | `99f07f4c1fe823b5fe9491605cb6eebd8f21e64e6480387bf7e205acd1d04416` |
| `tools/audit_github_workflows.py` | `True` | 133 | True | True | False | False | True | `926fd3360f0357ea8412e8d7318ad5b19b0802bad0911f211699ddf027c17b14` |
| `tools/docs_inventory.py` | `True` | 468 | True | True | True | True | True | `0aa544eeab88e77e04bb825247884d91597ca0cbc6a69d4fb0633f101a573fa8` |
| `tools/formula_artifact_builder.py` | `True` | 51 | True | True | False | False | False | `adc0f0eae76f4dfba28e2dbe4f449d27fe3433f80d8a1c7853dfbef98c3eb548` |
| `tools/iml/iml_pipeline.py` | `True` | 43 | True | True | True | False | False | `73dfa54829abaf7df43a453501ad3ae38dad571f588222315831d141a0b1daa1` |
| `tools/real_data_materialization_audit.py` | `True` | 252 | True | False | True | True | False | `6c00d159876f9765d44112e5786424d55b72052514b78aa95437ec50e9d1669c` |
| `tools/verify_real_source_signatures.py` | `True` | 238 | True | False | True | True | False | `725719b5cb87832a6798d185704da5b931cbd789db7d597c1315b693f4754171` |
| `validacao_real/compute_validation.py` | `True` | 254 | True | False | False | False | True | `59b80b7442a20e3f012366bf9adb46d78ff390579e7eec144e7441d82b67dfeb` |
| `validacao_real/fetch_real_data.py` | `True` | 83 | True | False | False | False | True | `54b0ab69d4fdbdfe28fbdc617688c30d3ace2ad6328788204c8781a0664ec28b` |
| `validacao_real/make_figures.py` | `True` | 147 | True | False | False | False | True | `67a904b17a99c899cc9597e702c80393e2f97a68b949d49073243c3c98b628bf` |
| `validacao_real/render_report.py` | `True` | 75 | True | False | False | False | True | `7dc4843df0a1f9e8b4fbe6f39d265375b8cc01dfaed87bf4bf899371784da276` |
