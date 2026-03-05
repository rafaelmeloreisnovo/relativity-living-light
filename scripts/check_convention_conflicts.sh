#!/usr/bin/env bash
set -euo pipefail

# Detecta padrões textuais potencialmente contraditórios com a norma canônica:
# f(z)=1/(1+exp((z-z_t)/w_t)) e mapeamento canônico f=1->DE, f=0->DM

RISK_REGEX='1\s*[→>-]+\s*DE.{0,80}0\s*[→>-]+\s*DM|f\s*\(\s*z\s*\)\s*->?\s*1.{0,80}DE.{0,80}f\s*\(\s*z\s*\)\s*->?\s*0.{0,80}DM'
LOGISTIC_REGEX='f\s*\(\s*z\s*\)\s*=\s*1\s*/\s*\(\s*1\s*\+\s*exp\s*\(\s*\(\s*z\s*-\s*z[_t]?\s*\)\s*/\s*w[_t]?\s*\)\s*\)'

if command -v rg >/dev/null 2>&1; then
  list_files() {
    rg --files -g '*.md' -g '*.tex'
  }
  has_match() {
    local regex="$1" file="$2"
    rg -n -i "$regex" "$file" >/dev/null 2>&1
  }
  print_matches() {
    local regex="$1" file="$2"
    rg -n -i "$regex" "$file" || true
  }
else
  list_files() {
    find . -type f \( -name '*.md' -o -name '*.tex' \) -print | sed 's#^./##'
  }
  has_match() {
    local regex="$1" file="$2"
    grep -n -E -i "$regex" "$file" >/dev/null 2>&1
  }
  print_matches() {
    local regex="$1" file="$2"
    grep -n -E -i "$regex" "$file" || true
  }
fi

files="$(list_files)"

status=0
while IFS= read -r file; do
  [[ -z "$file" ]] && continue
  if has_match "$RISK_REGEX" "$file" && has_match "$LOGISTIC_REGEX" "$file"; then
    echo "[CONTRADICTION_RISK] $file"
    print_matches "$RISK_REGEX|$LOGISTIC_REGEX" "$file"
    status=1
  fi
done <<< "$files"

if [[ "$status" -ne 0 ]]; then
  echo "Falha: encontrados padrões de risco de contradição com a norma canônica."
  exit 1
fi

echo "OK: nenhuma contradição textual de risco detectada."
