#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUN_ALL_PY="$REPO_ROOT/data/pipelines/structure_d/run_all.py"
DATASETS_CONFIG="$REPO_ROOT/data/pipelines/structure_d/datasets_config.json"

if [[ ! -f "$RUN_ALL_PY" ]]; then
  echo "Erro: arquivo não encontrado: $RUN_ALL_PY"
  exit 1
fi

if [[ ! -f "$DATASETS_CONFIG" ]]; then
  echo "Erro: arquivo não encontrado: $DATASETS_CONFIG"
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
    if isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "MODEL_BY_DATASET":
                if not isinstance(node.value, ast.Dict):
                    raise SystemExit("Erro: MODEL_BY_DATASET precisa ser dict literal")
                model_dataset_keys = []
                for key_node in node.value.keys:
                    if isinstance(key_node, ast.Constant) and isinstance(key_node.value, str):
                        model_dataset_keys.append(key_node.value)
                    else:
                        raise SystemExit("Erro: chaves de MODEL_BY_DATASET devem ser strings literais")
            if isinstance(target, ast.Name) and target.id == "REAL_PROFILE":
                real_profile = ast.literal_eval(node.value)

if model_dataset_keys is None:
    raise SystemExit("Erro: MODEL_BY_DATASET não encontrado em run_all.py")

cfg = json.loads(config_path.read_text(encoding="utf-8"))
profiles = cfg.get("profiles", {})
if not profiles:
    raise SystemExit("Erro: datasets_config.json sem campo profiles")

covered = set(model_dataset_keys)
missing_rows = []
for profile_name, profile_data in profiles.items():
    if profile_name == real_profile:
        continue
    active = profile_data.get("active_datasets", [])
    for dataset_id in active:
        if dataset_id not in covered:
            missing_rows.append((profile_name, dataset_id))

if missing_rows:
    print("Falha: profiles com datasets ativos sem cobertura em MODEL_BY_DATASET:")
    for profile_name, dataset_id in missing_rows:
        print(f"  - profile={profile_name} dataset={dataset_id}")
    print("\nDica: adicione o dataset em MODEL_BY_DATASET ou mova o profile para fluxo dedicado.")
    raise SystemExit(1)

print("Sucesso: todos os datasets ativos dos profiles clássicos têm cobertura em MODEL_BY_DATASET.")
print(f"Profiles verificados: {len([p for p in profiles if p != real_profile])}")
print(f"Datasets cobertos em MODEL_BY_DATASET: {len(covered)}")
PY
