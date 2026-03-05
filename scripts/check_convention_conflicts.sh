#!/usr/bin/env bash
set -euo pipefail

# Detecta padrões textuais potencialmente contraditórios com a norma canônica:
# f(z)=1/(1+exp((z-z_t)/w_t)) e mapeamento canônico f=1->DE, f=0->DM

RISK_REGEX='1\s*[→>-]+\s*DE.{0,80}0\s*[→>-]+\s*DM|f\s*\(\s*z\s*\)\s*->?\s*1.{0,80}DE.{0,80}f\s*\(\s*z\s*\)\s*->?\s*0.{0,80}DM'
LOGISTIC_REGEX='f\s*\(\s*z\s*\)\s*=\s*1\s*/\s*\(\s*1\s*\+\s*exp\s*\(\s*\(\s*z\s*-\s*z[_t]?\s*\)\s*/\s*w[_t]?\s*\)\s*\)'

if command -v rg >/dev/null 2>&1; then
  list_files() { rg --files -g '*.md' -g '*.tex'; }
  search_in_file() { rg -n -i "$1" "$2"; }
else
  list_files() { find . -type f \( -name '*.md' -o -name '*.tex' \) | sed 's#^\./##'; }
  search_in_file() { grep -nEi "$1" "$2"; }
fi

files="$(list_files)"

status=0
while IFS= read -r file; do
  [[ -z "$file" ]] && continue
  if search_in_file "$RISK_REGEX" "$file" >/dev/null 2>&1 && search_in_file "$LOGISTIC_REGEX" "$file" >/dev/null 2>&1; then
    echo "[CONTRADICTION_RISK] $file"
    search_in_file "$RISK_REGEX|$LOGISTIC_REGEX" "$file" || true
    status=1
  fi
done <<< "$files"

if [[ "$status" -ne 0 ]]; then
  echo "Falha: encontrados padrões de risco de contradição com a norma canônica."
  exit 1
fi

echo "OK: nenhuma contradição textual de risco detectada."
