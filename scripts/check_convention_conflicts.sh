#!/usr/bin/env bash
set -euo pipefail

# Detecta padrões textuais potencialmente contraditórios com a norma canônica:
# f(z)=1/(1+exp((z-z_t)/w_t)) e mapeamento canônico f=1->DE, f=0->DM

RISK_REGEX='1\s*[→>-]+\s*DE.{0,80}0\s*[→>-]+\s*DM|f\s*\(\s*z\s*\)\s*->?\s*1.{0,80}DE.{0,80}f\s*\(\s*z\s*\)\s*->?\s*0.{0,80}DM'
LOGISTIC_REGEX='f\s*\(\s*z\s*\)\s*=\s*1\s*/\s*\(\s*1\s*\+\s*exp\s*\(\s*\(\s*z\s*-\s*z[_t]?\s*\)\s*/\s*w[_t]?\s*\)\s*\)'

if command -v rg >/dev/null 2>&1; then
  files=$(rg --files -g '*.md' -g '*.tex')
  find_matches() {
    rg -n -i "$1" "$2" >/dev/null 2>&1
  }
  dump_matches() {
    rg -n -i "$1" "$2" || true
  }
else
  files=$(find . -type f \( -name '*.md' -o -name '*.tex' \) -print | sed 's#^\./##')
  find_matches() {
    grep -E -i -n "$1" "$2" >/dev/null 2>&1
  }
  dump_matches() {
    grep -E -i -n "$1" "$2" || true
  }
fi

status=0
while IFS= read -r file; do
  [[ -z "$file" ]] && continue
  if find_matches "$RISK_REGEX" "$file" && find_matches "$LOGISTIC_REGEX" "$file"; then
    echo "[CONTRADICTION_RISK] $file"
    dump_matches "$RISK_REGEX|$LOGISTIC_REGEX" "$file"
    status=1
  fi
done <<< "$files"

if [[ "$status" -ne 0 ]]; then
  echo "Falha: encontrados padrões de risco de contradição com a norma canônica."
  exit 1
fi

echo "OK: nenhuma contradição textual de risco detectada."
