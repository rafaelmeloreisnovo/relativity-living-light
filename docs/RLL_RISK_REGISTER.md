# RLL — Scientific and Operational Risk Register

**Status:** registro de riscos científico-operacionais.  
**Escopo:** governança conservadora; não altera dados, fórmulas, resultados ou claims.

---

## 1. Objetivo

Registrar riscos que podem comprometer:

- rastreabilidade;
- interpretação científica;
- reprodutibilidade;
- publicação;
- comparação justa;
- proteção contra overclaim.

Cada risco deve ter:

```text
risco → impacto → contenção → próxima medida → estado
```

---

## 2. Registro principal

| ID | Risco | Probabilidade | Impacto | Nível | Contenção | Próxima medida | Estado |
|---|---|---:|---:|---:|---|---|---|
| R1 | Overclaim de vitória RLL | média | muito alto | crítico | `claim_allowed=false` | manter claim gate ledger | controlado |
| R2 | Confundir smoke test com fit final | alta | alto | crítico | rotular `maxiter=3` como smoke | robust fit seeds 1..10 | TOKEN_VAZIO_ROBUST_FIT |
| R3 | Sobrescrever resultado canônico | média | alto | alto | registrar output stem gap | implementar output versionado | TOKEN_VAZIO_CLI_OUTPUT_STEM |
| R4 | Ignorar CPL como adversário | média | alto | alto | CPL obrigatório | manter comparação LCDM/wCDM/CPL/RLL | controlado |
| R5 | RLL colapsar para LCDM por `Os0=0.0` | alta no smoke atual | alto | alto | documentar sem descartar estruturalmente | ablações + robust fit | aberto |
| R6 | Pantheon+ incompleto | média | alto | alto | marcar dataset vazio | materializar com hash/covariância | TOKEN_VAZIO_DATASET |
| R7 | CMB compressed parcial | média | alto | alto | bloquear claim forte | incluir covariância completa | TOKEN_VAZIO_COVARIANCE |
| R8 | Growth sem CLASS/CAMB | média | alto | alto | registrar backend ausente | instalar/validar externo | TOKEN_VAZIO_BACKEND |
| R9 | Penalização `k` incoerente | média | médio/alto | alto | registry de parâmetros | revisar k/nuisance por rota | aberto |
| R10 | Uso de sintético como prova externa | baixa/média | muito alto | crítico | real/synthetic boundary | manter bloqueio de claim | controlado |
| R11 | Documentação dispersa | média | médio | médio | índices canônicos | manter mapa de docs | em redução |
| R12 | Figura/tabela sem legenda de limitação | média | médio | médio | manifesto de figuras | exigir nota smoke/claim | aberto |
| R13 | Mudança de fórmula sem registro | baixa/média | muito alto | crítico | confirmação explícita | PR dedicado com rationale | bloqueado por regra |
| R14 | Ajuste post-hoc de parâmetros | média | muito alto | crítico | parameter registry | pré-registrar bounds/priors | aberto |
| R15 | Interpretação espiritual/metafórica invadir seção técnica | média | médio | médio | separar camadas | manter paper conservador | aberto |

---

## 3. Riscos por camada

### Camada A — Ciência

| Risco | Controle |
|---|---|
| RLL não competitivo contra CPL | aceitar resultado e investigar parametrização |
| RLL melhora chi2 mas piora BIC | registrar como evidência fraca, não vitória |
| Dados incompletos | `TOKEN_VAZIO_*` |
| Posterior ausente | sem claim forte |

### Camada B — Computação

| Risco | Controle |
|---|---|
| saída sobrescrita | output stem versionado |
| seeds não registradas | manifesto por execução |
| ambiente não registrado | registrar Python/NumPy/SciPy |
| falha de testes | bloquear fit robusto |

### Camada C — Publicação

| Risco | Controle |
|---|---|
| título forte demais | usar título conservador |
| abstract com overclaim | usar claim-gated language |
| tabelas sem status | adicionar nota smoke |
| ausência de limitações | seção explícita de falsificabilidade |

### Camada D — Governança

| Risco | Controle |
|---|---|
| lacuna escondida | ledger obrigatório |
| dado sintético confundido com real | boundary audit |
| arquivo canônico alterado | PR/checklist |
| claim permitido por narrativa | claim gate formal |

---

## 4. Critérios de severidade

| Nível | Definição |
|---|---|
| baixo | não afeta resultado nem claim |
| médio | afeta leitura, documentação ou reprodutibilidade local |
| alto | pode afetar comparação, métricas ou execução robusta |
| crítico | pode gerar falso claim, perda de rastreabilidade ou conclusão científica indevida |

---

## 5. Ações de mitigação imediata

| Ordem | Ação | Riscos reduzidos |
|---:|---|---|
| 1 | implementar output stem versionado | R2, R3 |
| 2 | rodar robust fit versionado | R2, R5 |
| 3 | criar agregador de seeds | R2, R5, R9 |
| 4 | executar ablações A1-A8 | R4, R5, R9 |
| 5 | materializar Pantheon+ | R6 |
| 6 | completar CMB covariance | R7 |
| 7 | validar CLASS/CAMB | R8 |
| 8 | gerar paper conservador | R1, R12, R15 |

---

## 6. R3

```text
F_ok   = riscos principais classificados e mitigação imediata definida.
F_gap  = riscos R3/R5/R6/R7/R8 seguem abertos até execução/código/dados externos.
F_next = criar mapa do pacote suplementar para paper e reprodutibilidade.
```
