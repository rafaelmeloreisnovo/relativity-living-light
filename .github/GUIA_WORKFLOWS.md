# Guia de Workflows — RLL

> Navegação rápida. Documentação completa: [`docs/workflows/INDICE_CANONICO.md`](../docs/workflows/INDICE_CANONICO.md)

## Pipeline Canônico (use este para execuções completas)

**`workflows/rll-pipeline-linear-completo.yml`** — 44 steps, 7 fases, gate determinístico único.

Inputs: `modo` (completo / apenas_ciencia / apenas_governanca / apenas_dados / dry_run)

## Checks Obrigatórios (não remover)

| Check | Workflow |
|-------|----------|
| `rll` | `RLL-CI.yml` → delega ao pipeline canônico |
| `test` | `python-tests.yml` |
| `validate-yaml` | `yml-syntax-validation.yml` |
| `check-conventions` | `convention-check.yml` |
| `build-formulas-artifacts` | `formulas-artifacts.yml` |
| `formulas-manifest` | `formulas-artifacts-validation.yml` |

## Decisão Rápida

| Objetivo | Workflow |
|----------|----------|
| Pipeline completo | `rll-pipeline-linear-completo.yml` (modo=completo) |
| Apenas ciência (fit+MCMC+Bayes) | `RLL-CI.yml` |
| Dados reais (fetch/validate) | `real-data-complete-execution.yml` |
| Análise Bayesiana standalone | `bayes_analysis.yml` |
| DESI BAO covariance | `desi-dr2-bao-validation.yml` |
| IML artifact | `iml_artifact.yml` |
| Inventário do repo | `repo-real-inventory.yml` |

## Workflows Auxiliares (prefira os canônicos acima)

- `validacao_real.yml` → use `real-data-complete-execution.yml`
- `START_MANUAL_HERE.yml` → use `real-data-complete-execution.yml` ou `rll-pipeline-linear-completo.yml`

## Articulação Interna

- Docs: [`docs/workflows/`](../docs/workflows/)
- Catálogo: [`.github/workflow-orchestrator/`](workflow-orchestrator/)
- Workflows pendentes: [`.github/To_add/`](To_add/)
