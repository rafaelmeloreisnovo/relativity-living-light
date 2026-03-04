#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUN_ALL_PY="$REPO_ROOT/data/pipelines/structure_d/run_all.py"
RESULTS_DIR="$REPO_ROOT/results/structure_d"

if [[ ! -f "$RUN_ALL_PY" ]]; then
  echo "Erro: arquivo não encontrado: $RUN_ALL_PY"
  exit 1
fi

mapfile -t required_outputs < <(
  python3 - "$RUN_ALL_PY" <<'PY'
import ast
import sys
from pathlib import Path

run_all_path = Path(sys.argv[1])
source = run_all_path.read_text(encoding="utf-8")
module = ast.parse(source, filename=str(run_all_path))

required = None
for node in module.body:
    if isinstance(node, ast.Assign):
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id == "REQUIRED_OUTPUTS":
                required = ast.literal_eval(node.value)
                break
    if required is not None:
        break

if required is None:
    raise SystemExit("Erro: REQUIRED_OUTPUTS não encontrado em run_all.py")

for item in required:
    print(item)
PY
)

if [[ ${#required_outputs[@]} -eq 0 ]]; then
  echo "Erro: REQUIRED_OUTPUTS está vazio."
  exit 1
fi

echo "[structure_d] Verificando saídas obrigatórias em: $RESULTS_DIR"
echo "[structure_d] Arquivos esperados (REQUIRED_OUTPUTS):"
for file in "${required_outputs[@]}"; do
  echo "  - $file"
done

missing=()
for file in "${required_outputs[@]}"; do
  path="$RESULTS_DIR/$file"
  if [[ -f "$path" ]]; then
    echo "[OK] $file"
  else
    echo "[MISSING] $file"
    missing+=("$file")
  fi
done

if [[ ${#missing[@]} -gt 0 ]]; then
  echo
  echo "Falha: arquivos obrigatórios ausentes em results/structure_d:"
  for file in "${missing[@]}"; do
    echo "  - $file"
  done
  exit 1
fi

echo "Sucesso: todos os arquivos obrigatórios de structure_d estão presentes."
