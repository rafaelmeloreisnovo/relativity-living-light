#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${REPO_ROOT}"

WITH_TWO_RAD=0

for arg in "$@"; do
  case "$arg" in
    --with-two-rad)
      WITH_TWO_RAD=1
      ;;
    -h|--help)
      cat <<'USAGE'
Uso: scripts/run_repro_all.sh [--with-two-rad]

Executa o pipeline de reprodutibilidade:
  [1/4] python -m data.pipelines.structure_d.make_example_data
  [2/4] python -m data.pipelines.structure_d.run_all
  [3/4] python docs/rll_validation_real.py
  [4/4] (opcional com --with-two-rad) python docs/rll_two_radiation_model.py
USAGE
      exit 0
      ;;
    *)
      echo "Erro: argumento não reconhecido: $arg" >&2
      echo "Use --help para ver o uso." >&2
      exit 1
      ;;
  esac
done

echo "[1/4] Gerando dados de exemplo (Structure-D)..."
python -m data.pipelines.structure_d.make_example_data

echo "[2/4] Executando pipeline completo Structure-D..."
python -m data.pipelines.structure_d.run_all

echo "[3/4] Rodando validação em dados reais..."
mkdir -p /mnt/user-data/outputs
python docs/rll_validation_real.py

if [[ "$WITH_TWO_RAD" -eq 1 ]]; then
  echo "[4/4] Rodando modelo com duas radiações (opcional)..."
  python docs/rll_two_radiation_model.py
else
  echo "[4/4] Etapa opcional ignorada (use --with-two-rad para habilitar)."
fi

cat <<'EOF_MSG'
Pipeline concluído.
Artefatos esperados:
- results/structure_d/* (saídas do pipeline Structure-D)
- /mnt/user-data/outputs/RLL_chi2_results.csv (validação em dados reais)
- /mnt/user-data/outputs/RLL_validacao_real.png (figura de validação)
- /mnt/user-data/outputs/Hz_data_real.csv e /mnt/user-data/outputs/BAO_data_real.csv
- results/two_radiation_model_preview.csv (se --with-two-rad)
EOF_MSG
