#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${REPO_ROOT}"

WITH_TWO_RAD=0
BAYES=0

REQUIRED_OUTPUTS=(
  "results/structure_d/model_comparison.csv"
  "results/structure_d/covariance_usage.csv"
  "results/structure_d/error_mode_usage.csv"
  "results/structure_d/rll_regime_summary.csv"
  "results/structure_d/reproduction_contract.json"
  "results/RLL_chi2_results.csv"
  "figs/paper/RLL_validacao_real.png"
)

for arg in "$@"; do
  case "$arg" in
    --with-two-rad)
      WITH_TWO_RAD=1
      ;;
    --bayes)
      BAYES=1
      ;;
    -h|--help)
      cat <<'USAGE'
Uso: scripts/run_repro_all.sh [--with-two-rad] [--bayes]

Executa o pipeline de reprodutibilidade:
  [1/4] python -m data.pipelines.structure_d.make_example_data
  [2/4] python -m data.pipelines.structure_d.run_all [--bayes]
  [3/4] PYTHONPATH=. python docs/rll_validation_real.py
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
if [[ "$BAYES" -eq 1 ]]; then
  python -m data.pipelines.structure_d.run_all --bayes
  REQUIRED_OUTPUTS+=("results/structure_d/bayes_evidence_bic_proxy.csv")
  REQUIRED_OUTPUTS+=("results/structure_d/bayes_factor_interpretation.csv")
else
  python -m data.pipelines.structure_d.run_all
fi

echo "[3/4] Rodando validação em dados reais..."
PYTHONPATH=. python docs/rll_validation_real.py

if [[ "$WITH_TWO_RAD" -eq 1 ]]; then
  echo "[4/4] Rodando modelo com duas radiações (opcional)..."
  python docs/rll_two_radiation_model.py
else
  echo "[4/4] Etapa opcional ignorada (use --with-two-rad para habilitar)."
fi

if [[ "$WITH_TWO_RAD" -eq 1 ]]; then
  REQUIRED_OUTPUTS+=("results/two_radiation_model_preview.csv")
fi

echo "[5/5] Validando artefatos canônicos..."
missing=0
for artifact in "${REQUIRED_OUTPUTS[@]}"; do
  if [[ ! -f "$artifact" ]]; then
    echo "  ❌ ausente: $artifact"
    missing=1
  else
    echo "  ✅ ok: $artifact"
  fi
done

if [[ "$missing" -ne 0 ]]; then
  echo "Falha: artefatos obrigatórios ausentes." >&2
  exit 1
fi

cat > results/reproduction_contract_canonical.json <<EOF
{
  "command": "scripts/run_repro_all.sh$( [[ "$WITH_TWO_RAD" -eq 1 ]] && printf ' --with-two-rad' )$( [[ "$BAYES" -eq 1 ]] && printf ' --bayes' )",
  "steps": [
    "python -m data.pipelines.structure_d.make_example_data",
    "python -m data.pipelines.structure_d.run_all$( [[ "$BAYES" -eq 1 ]] && printf ' --bayes' )",
    "PYTHONPATH=. python docs/rll_validation_real.py",
    "$( [[ "$WITH_TWO_RAD" -eq 1 ]] && printf 'python docs/rll_two_radiation_model.py' || printf 'optional_step_skipped' )"
  ],
  "required_outputs": [
$(for artifact in "${REQUIRED_OUTPUTS[@]}"; do printf '    "%s",\n' "$artifact"; done | sed '$s/,$//')
  ]
}
EOF

echo "  ✅ contract: results/reproduction_contract_canonical.json"

cat <<'EOF_MSG'
Pipeline concluído.
Artefatos esperados:
- results/structure_d/* (saídas do pipeline Structure-D)
- results/RLL_chi2_results.csv (validação em dados reais)
- figs/paper/RLL_validacao_real.png (figura de validação)
- results/Hz_data_real.csv e results/BAO_data_real.csv
- results/reproduction_contract_canonical.json
- results/two_radiation_model_preview.csv (se --with-two-rad)
EOF_MSG
