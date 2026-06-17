# RLL — Claim Gate Ledger

**Status:** ledger canônico de permissões, bloqueios e condições para claims científicos.  
**Regra:** claim forte só existe depois do gate; antes disso, existe hipótese testável, pipeline e resultado preliminar.

---

## 1. Claim policy raiz

```text
claim_allowed = false
```

Permanece `false` enquanto houver qualquer um destes estados:

- `TOKEN_VAZIO_DATASET`;
- `TOKEN_VAZIO_COVARIANCE`;
- `TOKEN_VAZIO_BACKEND`;
- `TOKEN_VAZIO_ROBUST_FIT`;
- `TOKEN_VAZIO_POSTERIOR`;
- `TOKEN_VAZIO_REPRODUCIBILITY`;
- piora persistente de AIC/AICc/BIC contra baselines relevantes;
- uso de dado sintético para claim externo;
- ausência de comparador CPL/w0waCDM.

---

## 2. Claims permitidos no estado atual

| Claim | Status | Linguagem segura |
|---|---|---|
| RLL é hipótese testável | permitido | “RLL permanece candidato testável.” |
| Há pipeline comparativo | permitido | “O repositório contém pipeline para comparação contra LCDM/wCDM/CPL/RLL.” |
| Há governança de claims | permitido | “Claims fortes são bloqueados por gates conservadores.” |
| Há dados reais parciais/materializados | permitido com escopo | “Há rotas com dados reais; cobertura completa ainda depende de gates.” |
| Resultado atual é smoke/sanity | permitido | “A execução atual deve ser interpretada como smoke test.” |
| CPL é adversário técnico principal | permitido | “CPL/w0waCDM deve ser baseline obrigatório.” |
| RLL colapsou para LCDM no smoke atual | permitido se baseado no artefato | “Nesta execução, `Os0=0.0` torna RLL praticamente equivalente ao limite LCDM.” |

---

## 3. Claims proibidos no estado atual

| Claim proibido | Motivo |
|---|---|
| “RLL está confirmado” | falta robust fit, posterior, datasets/covariâncias completos |
| “RLL vence LCDM” | resultado atual não sustenta vitória estatística robusta |
| “RLL vence CPL” | CPL é favorecido no smoke atual |
| “RLL resolve energia escura” | extrapola dados e métricas disponíveis |
| “RLL resolve tensão H0” | falta likelihood/diagnóstico formal completo |
| “RLL resolve S8” | falta growth externo robusto |
| “RLL substitui cosmologia padrão” | exigiria validação independente e publicação revisada |
| “Dado sintético confirma o modelo” | sintético valida pipeline, não universo |
| “TOKEN_VAZIO confirma a teoria” | lacuna é alvo de medição, não evidência |

---

## 4. Gates científicos

### Gate A — Dados

| Item | Estado exigido | Estado atual padrão |
|---|---|---|
| DESI DR2 BAO | materializado + covariância | verificar por manifesto |
| Cronômetros H(z) | materializado + proveniência | verificar por manifesto |
| Pantheon+ | light curve + covariância + hash | `TOKEN_VAZIO_DATASET` se ausente |
| CMB compressed | vetor + covariância + referência | `TOKEN_VAZIO_COVARIANCE` se parcial |
| fσ8/growth | dataset + benchmark externo | `TOKEN_VAZIO_BACKEND` se sem CLASS/CAMB |

### Gate B — Estatística

| Item | Exigido |
|---|---|
| `chi2` | por modelo e por bloco |
| `AIC` | com `k` documentado |
| `AICc` | obrigatório para amostra finita |
| `BIC` | obrigatório |
| `N` | pontos efetivos documentados |
| `k` | parâmetros livres/nuisance documentados |
| deltas | contra LCDM e CPL |
| seeds | múltiplas |
| maxiter | robusto, não apenas smoke |

### Gate C — Reprodutibilidade

| Item | Exigido |
|---|---|
| commit SHA | sim |
| comando exato | sim |
| ambiente | Python + libs |
| hash dos inputs | sim |
| hash dos outputs | sim |
| saída versionada | sim |
| não sobrescrever canônico | sim |

### Gate D — Falsificabilidade

| Item | Exigido |
|---|---|
| condição de derrota | explícita |
| condição de permanência | explícita |
| condição de claim | explícita |
| condição de descarte parcial | explícita |
| risco de overclaim | registrado |

---

## 5. Matriz de decisão de claim

| Situação | Decisão |
|---|---|
| RLL pior que LCDM em AIC/AICc/BIC | claim de vitória bloqueado |
| RLL igual a LCDM mas com k maior | claim de vitória bloqueado |
| CPL vence RLL | CPL vira adversário principal |
| RLL melhora chi2 mas piora BIC | claim fraco no máximo, sem vitória forte |
| RLL vence LCDM e CPL em chi2/AIC/AICc/BIC robusto | discutir claim condicionado aos demais gates |
| RLL vence apenas em dataset parcial | claim local, não cosmológico amplo |
| resultado depende de sintético | claim externo proibido |
| resultado depende de covariância ausente | claim bloqueado |

---

## 6. Linguagem para paper

### Abstract seguro

> Este trabalho apresenta o RLL como uma hipótese fenomenológica testável e um pipeline reprodutível para comparação com LCDM, wCDM e CPL/w0waCDM. O estado atual preserva gates conservadores de claim: resultados preliminares são tratados como smoke/sanity tests, lacunas de dados e covariâncias são marcadas como `TOKEN_VAZIO`, e claims fortes permanecem bloqueados até robustez estatística, datasets completos e validação externa.

### Contribuição segura

> A principal contribuição atual é metodológica: transformar uma hipótese cosmológica em objeto computacional auditável, com fronteiras explícitas entre conceito, cálculo, dado real, sintético, lacuna e claim científico.

---

## 7. Ledger vivo

| Gate | Estado | Próxima medida |
|---|---|---|
| robust fit | TOKEN_VAZIO_ROBUST_FIT | executar seeds 1..10 com maxiter >= 100 |
| Pantheon+ | TOKEN_VAZIO_DATASET | materializar arquivos e hashes |
| CMB covariance | TOKEN_VAZIO_COVARIANCE | incluir matriz comprimida completa |
| growth backend | TOKEN_VAZIO_BACKEND | validar com CLASS/CAMB ou equivalente |
| posterior | TOKEN_VAZIO_POSTERIOR | MCMC/nested/deep fit |
| CPL baseline | presente como requisito | manter obrigatório |
| claim_allowed | false | só reavaliar após gates completos |

---

## 8. R3

```text
F_ok   = claims permitidos/proibidos formalizados; gate conservador preservado.
F_gap  = robust fit, Pantheon+, CMB covariance, growth backend e posterior seguem pendentes.
F_next = criar rota paper-ready conservadora para transformar repo em manuscrito sem overclaim.
```
