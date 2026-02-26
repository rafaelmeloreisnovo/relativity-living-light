#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "[1/4] Gerando dados sintéticos do Structure-D"
python -m data.pipelines.structure_d.make_example_data

echo "[2/4] Rodando comparação Structure-D"
python -m data.pipelines.structure_d.run_all

echo "[3/4] Rodando validação real RLL vs ΛCDM"
python docs/rll_validation_real.py

echo "[4/4] Rodando preview do modelo de duas radiações"
python docs/rll_two_radiation_model.py

echo "Concluído. Artefatos esperados:"
echo "- results/structure_d/model_comparison.csv"
echo "- results/RLL_chi2_results.csv"
echo "- results/two_radiation_model_preview.csv"
echo "- figs/paper/RLL_validacao_real.png"
