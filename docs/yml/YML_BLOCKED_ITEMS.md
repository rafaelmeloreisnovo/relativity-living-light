# YML BLOCKED ITEMS

Gerado em: `2026-06-26T20:06:17Z`  
Commit auditado: `623c7be20f0952cd5769615032f8d2d68a1a23e8`

| classe | item | evidência | status | desbloqueio |
|---|---|---|---|---|
| BLOQUEADO | Promoção científica `real_validated` global | critérios completos não foram executados nesta auditoria documental | blocked | executar pipeline real completo com checksums, métricas, baseline e claim boundary |
| LACUNA | Consumidor explícito para YAML data_config | `YML_FILE_LEDGER.tsv` mostra `scripts chamados=TOKEN_VAZIO` para data_config | metadata_ready | adicionar `consumed_by` ou mapa de consumidor por manifest |
| RISCO | Permissões de escrita | workflows com `contents: write` registrados no ledger | requer justificativa | condicionar commit/push a input boolean e documentar razão operacional |
| RISCO | Mock CI | `dha-fisher-ci.yml` gera `results/dha/mock_catalog.csv` | controlado por rótulo | manter fora de claims reais |
| NÃO VERIFICADO | Execução científica full remota | esta auditoria não executou GitHub Actions hospedado | NÃO VERIFICADO | disparar workflow manual e anexar run_id/logs |

## RLL vs ΛCDM

O artefato atual melhora rastreabilidade e reprodutibilidade. Ele não estabelece superioridade do RLL. Quando AIC/BIC favorecerem ΛCDM, isso deve ser declarado.
