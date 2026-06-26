# YML BLOCKED ITEMS

Gerado em: `2026-06-26T19:52:53Z`  
Commit auditado: `154b8b6d2e1766fa8e630ad143b02c1d4bb34ca0`

| classe | item | evidência | status | desbloqueio |
|---|---|---|---|---|
| BLOQUEADO | Promoção científica `real_validated` global | critérios completos não foram executados nesta auditoria documental | blocked | executar pipeline real completo com checksums, métricas, baseline e claim boundary |
| LACUNA | Consumidor explícito para YAML data_config | `YML_FILE_LEDGER.tsv` mostra `scripts chamados=TOKEN_VAZIO` para data_config | metadata_ready | adicionar `consumed_by` ou mapa de consumidor por manifest |
| RISCO | Permissões de escrita | workflows com `contents: write` registrados no ledger | requer justificativa | condicionar commit/push a input boolean e documentar razão operacional |
| RISCO | Mock CI | `dha-fisher-ci.yml` gera `results/dha/mock_catalog.csv` | controlado por rótulo | manter fora de claims reais |
| NÃO VERIFICADO | Execução científica full remota | esta auditoria não executou GitHub Actions hospedado | NÃO VERIFICADO | disparar workflow manual e anexar run_id/logs |

## RLL vs ΛCDM

O artefato atual melhora rastreabilidade e reprodutibilidade. Ele não estabelece superioridade do RLL. Quando AIC/BIC favorecerem ΛCDM, isso deve ser declarado.
