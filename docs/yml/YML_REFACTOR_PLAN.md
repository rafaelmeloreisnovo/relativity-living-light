# YML REFACTOR PLAN

Plano de refatoração com separação entre o que é **seguro agora** (behavior-
neutral) e o que exige decisão do mantenedor.

## Padrão-alvo de workflow (aplicado quando seguro)

```yaml
permissions:
  contents: read            # mínimo; só sobe para write onde há commit/push

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: false # pipelines que commitam não devem ser cancelados no meio

jobs:
  <job>:
    runs-on: ubuntu-latest
    timeout-minutes: <N>     # rede de segurança contra runner pendurado
```

## Aplicação por workflow

| Workflow | permissions antes | ação | timeout | concurrency |
|---|---|---|---|---|
| START_MANUAL_HERE | ausente | + `contents: read` | +45 | + |
| convention-check | ausente | + `contents: read` | +15 | + |
| dha-fisher-ci | ausente | + `contents: read` | +30 | + |
| formulas-artifacts | ausente | + `contents: read` | +20 | + |
| iml_artifact | ausente | + `contents: read` | +20 | + |
| python-tests | ausente | + `contents: read` | +20 | + |
| unified-geometry | ausente | + `contents: read` | +20 | + |
| real-data-complete-execution | `contents: write` | manter (justificado) | +60 | já tem |
| repo-real-inventory | `contents: write` | manter (commita inventário) | +30 | + |
| rll-book-data-pipeline | job `contents: write` | manter | +45 | + |
| rll-data-pipeline | job `contents: write` | manter | +45 | + |
| rll-real-data-orchestrator | job `contents: write` | manter | +60 | + |
| validacao_real | `contents: write` | manter (commita resultados) | +30 | + |

Justificativa de `contents: write` (mantido): cada um desses workflows tem
passo `git commit`/`git push` real (inventário, artefatos leves, resultados de
validação). Reduzir para `read` quebraria a função documentada → não alterado.

## Fora deste PR (sensível)
- Dedupe de `CAMINHOS_VALIDACAO_NOVOS.yml` (arquivo versionado).
- Pin por SHA das actions.
- Renomeação de `mock_catalog.csv`.
Ver `YML_NEXT_ACTIONS.md`.
