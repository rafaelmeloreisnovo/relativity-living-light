# WORKFLOW REFACTOR AUDIT

Gerado em: `2026-06-13T06:12:53Z`  
Commit auditado: `c8eb1047ada81ee2a1f6eb4c917ae707fdee8e4f`

## Inventário pré-alteração obrigatório

- `git status --short`: `FATO_VERIFICADO_WORKTREE_LIMPA (git status --short executado antes das alterações retornou saída vazia)`
- `git rev-parse HEAD`: `c8eb1047ada81ee2a1f6eb4c917ae707fdee8e4f`
- Total YAML/YML: `35`
- Total workflows: `14`

## Validações executadas

| comando | exit_code | resultado |
|---|---:|---|
| `git status --short` | 0 | `FATO_VERIFICADO_WORKTREE_LIMPA (git status --short executado antes das alterações retornou saída vazia)` |
| `git rev-parse HEAD` | 0 | `c8eb1047ada81ee2a1f6eb4c917ae707fdee8e4f` |
| `python3 -c from pathlib import Path
import yaml,sys
failed=False
files=sorted([*Path('.').rglob('*.yml'),*Path('.').rglob('*.yaml')])
for p in files:
    try: yaml.safe_load(p.read_text(encoding='utf-8')); print('OK\t'+str(p))
    except Exception as e: failed=True; print('FAIL\t'+str(p)+'\t'+str(e))
sys.exit(1 if failed else 0)` | 0 | `OK	validacao_real/sources.yml` |
| `bash -lc python3 -m py_compile $(find scripts data/pipelines validacao_real -name "*.py" 2>/dev/null)` | 0 | `TOKEN_VAZIO` |
| `python3 tools/audit_github_workflows.py --strict` | 0 | `Workflow audit OK: executable workflows are isolated and validation data is externalized.` |

## Workflows auditados

| workflow | workflow_dispatch | permissions | concurrency | timeout | scripts inexistentes | artefatos | riscos |
|---|---:|---|---:|---|---|---|---|
| `.github/workflows/START_MANUAL_HERE.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `start-manual-here-${{ github.run_id }}:artifacts/manual-start/` | `FATO_VERIFICADO` |
| `.github/workflows/convention-check.yml` | False | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `RISCO_BOUNDARY_TERMS_ROTULADOS` |
| `.github/workflows/dha-fisher-ci.yml` | False | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `dha-fisher-forecast:results/dha/fisher_forecast_reference.json, ln1pz-extractor:results/dha/ln1pz_fit.csv | results/dha/ln1pz_fit_summary.json | , desi-dha-extractor:results/dha/desi_dha_pipeline_summary.json` | `RISCO_BOUNDARY_TERMS_ROTULADOS` |
| `.github/workflows/formulas-artifacts.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `formulas-artifacts:artifacts/formulas` | `FATO_VERIFICADO` |
| `.github/workflows/iml_artifact.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `iml-artifact:artifacts/iml/iml_artifact.json` | `RISCO_BOUNDARY_TERMS_ROTULADOS` |
| `.github/workflows/python-tests.yml` | False | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `RISCO_BOUNDARY_TERMS_ROTULADOS` |
| `.github/workflows/real-data-complete-execution.yml` | True | `{"contents": "write"}` | True | OK | `TOKEN_VAZIO` | `real-data-complete-${{ github.run_id }}:artifacts/real-data-complete/` | `RISCO_CONTENTS_WRITE` |
| `.github/workflows/repo-real-inventory.yml` | True | `{"contents": "write"}` | True | OK | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `RISCO_CONTENTS_WRITE` |
| `.github/workflows/rll-book-data-pipeline.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `rll-book-pipeline-${{ github.run_id }}-${{ inputs.book_scope }}-${{ inputs.dataset_group }}-${{ inputs.mode }}:artifacts/rll-pipeline/` | `FATO_VERIFICADO` |
| `.github/workflows/rll-data-pipeline.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `rll-pipeline-${{ github.run_id }}-${{ inputs.dataset_group }}-${{ inputs.mode }}:artifacts/rll-pipeline/` | `FATO_VERIFICADO` |
| `.github/workflows/rll-real-data-orchestrator.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `rll-real-run-${{ github.run_id }}:artifacts/rll-real-run/` | `FATO_VERIFICADO` |
| `.github/workflows/unified-geometry.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `unified-geometry-text-artifacts:results/unified_geometry/shapes.csv | results/unified_geometry/manifest.json | ` | `RISCO_BOUNDARY_TERMS_ROTULADOS` |
| `.github/workflows/validacao_real.yml` | True | `{"contents": "write"}` | True | OK | `TOKEN_VAZIO` | `validacao-real-artifacts:validacao_real/fetched/ | validacao_real/results/ | ` | `RISCO_CONTENTS_WRITE` |
| `.github/workflows/yml-syntax-validation.yml` | True | `{"contents": "read"}` | True | OK | `TOKEN_VAZIO` | `TOKEN_VAZIO` | `RISCO_BOUNDARY_TERMS_ROTULADOS` |

## Linguagem científica obrigatória

FATO_VERIFICADO: o artefato atual melhora rastreabilidade e reprodutibilidade por inventário, parser YAML, py_compile e ledger de hashes.  
LACUNA: esta auditoria documental não estabelece superioridade do RLL.  
ACAO_RECOMENDADA: quando AIC/BIC favorecerem ΛCDM, isso deve ser declarado nos relatórios científicos.
