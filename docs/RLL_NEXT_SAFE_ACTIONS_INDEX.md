# RLL — Next Safe Actions Index

**Status:** índice de próximos atos seguros para continuidade sem perguntas repetidas.  
**Regra:** executar sem nova confirmação apenas ações documentais, auditoriais, organizacionais ou preparatórias que não alterem dados, fórmulas, claims ou resultados canônicos.

---

## 1. Estado atual da estrada

| Documento | Estado | Papel |
|---|---|---|
| `docs/RLL_ESTRADA_CANONICA_EXECUCAO.md` | criado | regra-mãe de execução |
| `docs/RLL_ROBUST_FIT_CHECKLIST.md` | criado | checklist robust fit |
| `docs/RLL_CLAIM_GATE_LEDGER.md` | criado | claims permitidos/proibidos |
| `docs/RLL_PAPER_READY_ROUTE.md` | criado | rota de manuscrito |
| `docs/RLL_CURRENT_RESULTS_PAPER_TABLE.md` | criado | tabela paper do smoke atual |
| `docs/RLL_OUTPUT_STEM_CLI_GAP.md` | criado | lacuna para não sobrescrever canônico |
| `docs/RLL_ABLATION_MATRIX.md` | criado | matriz de testes/ablações |
| `docs/RLL_FIGURE_TABLE_MANIFEST.md` | criado | mapa de figuras/tabelas |

---

## 2. Próximos atos seguros — fila A

Podem ser executados sem nova pergunta porque não alteram ciência nem output canônico.

| Ordem | Ato | Arquivo sugerido | Motivo |
|---:|---|---|---|
| A1 | Criar diagrama Mermaid do pipeline claim-gated | `docs/RLL_PIPELINE_CLAIM_GATE_DIAGRAM.md` | figura F1 do paper |
| A2 | Criar nota executiva de 1 página | `docs/RLL_EXECUTIVE_ONE_PAGE.md` | leitura rápida para banca/parceiro |
| A3 | Criar tabela de riscos e mitigação | `docs/RLL_RISK_REGISTER.md` | governança científica |
| A4 | Criar mapa de publicação/suplemento | `docs/RLL_SUPPLEMENT_PACKAGE_MAP.md` | organizar entrega acadêmica |
| A5 | Criar issue/plano para output stem CLI | GitHub issue ou doc | preparar mudança segura |
| A6 | Criar checklist de PR antes de robust fit | `docs/RLL_PRE_ROBUST_FIT_PR_CHECKLIST.md` | impedir sobrescrita |

---

## 3. Próximos atos condicionados — fila B

Podem ser feitos depois que a lacuna `TOKEN_VAZIO_CLI_OUTPUT_STEM` for fechada.

| Ordem | Ato | Condição |
|---:|---|---|
| B1 | Implementar `STRUCTURE_D_JOINT_OUTPUT_STEM` | confirmação ou PR específico |
| B2 | Criar wrapper robust fit | saída versionada garantida |
| B3 | Rodar smoke reproduzível sem sobrescrever canônico | output stem funcional |
| B4 | Rodar seeds 1..10 maxiter=100 | output versionado |
| B5 | Agregar tabela robusta | outputs robustos existentes |
| B6 | Gerar figura de frequência `Os0=0.0` | robust fit completo |

---

## 4. Próximos atos bloqueados — fila C

Exigem dado externo, backend ou mudança científica/estrutural.

| Ordem | Ato | Bloqueio |
|---:|---|---|
| C1 | Pantheon+ completo | `TOKEN_VAZIO_DATASET` |
| C2 | CMB compressed covariance completa | `TOKEN_VAZIO_COVARIANCE` |
| C3 | CLASS/CAMB growth benchmark | `TOKEN_VAZIO_BACKEND` |
| C4 | MCMC/nested sampling | `TOKEN_VAZIO_POSTERIOR` |
| C5 | Reavaliar `claim_allowed=true` | todos os gates completos |

---

## 5. Decisão operacional

Próximo ato automático recomendado:

```text
A1 = Criar docs/RLL_PIPELINE_CLAIM_GATE_DIAGRAM.md
```

Justificativa:

- não altera dados;
- não altera fórmula;
- não altera resultados;
- não altera claim;
- cria Figura F1 do paper;
- melhora leitura acadêmica e executiva.

---

## 6. R3

```text
F_ok   = índice de próximos atos seguros criado; filas A/B/C separadas.
F_gap  = diagramas e pacote executivo ainda pendentes.
F_next = criar diagrama Mermaid do pipeline claim-gated.
```
