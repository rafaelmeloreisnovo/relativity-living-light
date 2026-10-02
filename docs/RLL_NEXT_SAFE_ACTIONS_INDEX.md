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

Podem ser executados sem nova pergunta porque não alteram ciência nem output canônico. A verificação do estado atual encontrou A1–A4 já presentes; as linhas abaixo ficam como manutenção dos artefatos existentes, não como tarefas de criação.

| Ordem | Ato | Arquivo sugerido | Motivo |
|---:|---|---|---|
| A1 | Revisar o diagrama Mermaid existente do pipeline claim-gated | `docs/RLL_PIPELINE_CLAIM_GATE_DIAGRAM.md` | arquivo já presente; manter aderência ao pipeline atual |
| A2 | Revisar a nota executiva existente | `docs/RLL_EXECUTIVE_ONE_PAGE.md` | arquivo já presente; atualizar só com evidência atual |
| A3 | Revisar o registro de riscos existente | `docs/RLL_RISK_REGISTER.md` | arquivo já presente; manter mitigação e status rastreáveis |
| A4 | Revisar o mapa de publicação/suplemento existente | `docs/RLL_SUPPLEMENT_PACKAGE_MAP.md` | arquivo já presente; atualizar quando mudar o pacote |
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

Próximo ato seguro recomendado:

```text
A7 = Após revisão/merge da rota de perfis, rodar literature_session com um arXiv ID e revisar o artifact pendente antes de incluir qualquer edge no grafo canônico.
```

Condições:

- o preview é somente um artifact, sem publicação em GitHub Pages;
- o intake guarda resposta Atom e SHA-256;
- as relações declaradas pelo pesquisador permanecem `RELATIONAL_PENDING` e `claim_allowed=false`;
- não há monitoramento agendado do arXiv neste corte.

## 6. R3

```text
F_ok   = filas A/B/C mantidas; A1-A4 conferidos como arquivos existentes.
F_gap  = Pages real não verificado; relações arXiv novas ainda exigem revisão humana.
F_next = revisar e executar uma intake manual pelo perfil de literatura após a rota ser aceita.
```
