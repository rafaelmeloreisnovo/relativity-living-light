#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUN_ALL_PY="$REPO_ROOT/data/pipelines/structure_d/run_all.py"
DATASETS_CONFIG="$REPO_ROOT/data/pipelines/structure_d/datasets_config.json"

if [[ ! -f "$RUN_ALL_PY" ]]; then
  echo "missing file: $RUN_ALL_PY"
  exit 1
fi

if [[ ! -f "$DATASETS_CONFIG" ]]; then
  echo "missing file: $DATASETS_CONFIG"
  exit 1
fi

python3 - "$RUN_ALL_PY" "$DATASETS_CONFIG" <<'PY'
import ast
import json
import sys
from pathlib import Path

run_all_path = Path(sys.argv[1])
config_path = Path(sys.argv[2])
module = ast.parse(run_all_path.read_text(encoding="utf-8"), filename=str(run_all_path))
model_dataset_keys = None
real_profile = "structure_d_real_validation"

for node in module.body:
    if not isinstance(node, ast.Assign):
        continue
    for target in node.targets:
        if isinstance(target, ast.Name) and target.id == "MODEL_BY_DATASET":
            if not isinstance(node.value, ast.Dict):
                raise SystemExit("MODEL_BY_DATASET must be a literal dict")
            model_dataset_keys = []
            for key_node in node.value.keys:
                if isinstance(key_node, ast.Constant) and isinstance(key_node.value, str):
                    model_dataset_keys.append(key_node.value)
                else:
                    raise SystemExit("MODEL_BY_DATASET keys must be literal strings")
        if isinstance(target, ast.Name) and target.id == "REAL_PROFILE":
            real_profile = ast.literal_eval(node.value)

if model_dataset_keys is None:
    raise SystemExit("MODEL_BY_DATASET not found in run_all.py")

cfg = json.loads(config_path.read_text(encoding="utf-8"))
profiles = cfg.get("profiles", {})
if not profiles:
    raise SystemExit("datasets_config.json has no profiles")

covered = set(model_dataset_keys)
missing_rows = []
skipped = []

for profile_name, profile_data in profiles.items():
    active = profile_data.get("active_datasets", [])
    if profile_name == real_profile or profile_name.startswith("structure_d_real_"):
        skipped.append(profile_name)
        continue
    for dataset_id in active:
        if dataset_id not in covered:
            missing_rows.append((profile_name, dataset_id))

if missing_rows:
    print("profiles with active datasets not covered by MODEL_BY_DATASET:")
    for profile_name, dataset_id in missing_rows:
        print(f"- profile={profile_name} dataset={dataset_id}")
    raise SystemExit(1)

print("OK: classic profiles have MODEL_BY_DATASET coverage")
print(f"classic_profiles_checked={len(profiles) - len(skipped)}")
print(f"dedicated_real_profiles_skipped={len(skipped)}")
print(f"datasets_covered={len(covered)}")
PY
