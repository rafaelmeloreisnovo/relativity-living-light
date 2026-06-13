# YML BLOCKED / OPEN ITEMS

Itens que ficaram `BLOQUEADO`, `LACUNA` ou `TOKEN_VAZIO` — sem invenção.

## BLOQUEADO

| Item | Motivo | Como desbloquear |
|---|---|---|
| Superioridade científica do RLL | AIC/BIC favorecem ΛCDM nos dados reais correntes (Δχ²=−5.51) | requer dados/ajuste que reduzam χ² do RLL sem aumentar k além do que AIC/BIC toleram |
| Validação Pantheon+ neste runner | não executada nesta auditoria (foco em `validacao_real/`) | rodar `scripts/run_real_pantheon_validation.py` após materializar Pantheon+ |
| Structure-D real neste runner | não executada nesta auditoria | rodar `python -m data.pipelines.structure_d.run_all_real` |

## LACUNA

| Lacuna | Evidência |
|---|---|
| `timeout-minutes` ausente | 13/13 workflows (corrigido neste PR) |
| `concurrency` ausente | 12/13 workflows (corrigido neste PR) |
| `permissions` explícito ausente | 7 workflows (corrigido neste PR) |
| Pin de actions por SHA | 13/13 usam tags `@v4`/`@v5`, não SHA |
| YAML não consumido por workflow | registries de referência (ver execution map) — `reference_only`, não é erro |

## TOKEN_VAZIO

| Campo | Local |
|---|---|
| `sha256_depois` (arquivos não modificados) | `YML_FILE_LEDGER.tsv` — igual a `sha256_antes` para data/config não tocados |
| `no_fake_fill` | `data/real_sources/rll_real_orchestrator_inventory.iml.yml:110` — declarado pelo repo |

## Não-bloqueios confirmados (FATO_VERIFICADO)

- 34/34 YAML parseiam. 28/28 scripts referenciados existem e compilam.
- `tools/audit_github_workflows.py --strict` retorna exit 0.
- `validacao_real` executa fim-a-fim (exit 0) com fetch remoto real.
