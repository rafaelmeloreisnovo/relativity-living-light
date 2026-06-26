# RLL — Paper-Ready Route

**Status:** rota conservadora para transformar o repositório em manuscrito técnico sem overclaim.  
**Princípio:** publicar o que o pipeline sustenta, não o que a hipótese deseja.

---

## 1. Título conservador sugerido

```text
Relativity Living Light (RLL): a reproducible claim-gated framework for testing a logistic cosmological transition against LCDM, wCDM and CPL baselines
```

Alternativa em português:

```text
Relativity Living Light (RLL): um framework reprodutível com gates de claim para testar uma transição cosmológica logística contra LCDM, wCDM e CPL
```

---

## 2. Tese publicável atual

A tese segura não é que RLL venceu.

A tese segura é:

> RLL foi transformado em hipótese computacional auditável, com pipeline de comparação contra baselines cosmológicos, fronteira explícita entre dados reais/sintéticos, ledger de lacunas e bloqueio de claims fortes até validação robusta.

---

## 3. Abstract provisório

> We present Relativity Living Light (RLL), a phenomenological cosmological transition hypothesis implemented as a reproducible, claim-gated validation framework. The repository separates conceptual motivation, executable calculations, real and synthetic data boundaries, missing-calculation ledgers, and statistical comparison against LCDM, wCDM and CPL/w0waCDM baselines. Current joint real-data runs are treated conservatively as smoke/sanity tests: CPL/w0waCDM is favored in the present preliminary execution, while RLL remains a testable candidate with strong claims blocked until robust multi-seed fits, complete covariance treatment, Pantheon+ materialization, CMB compressed likelihood completion and external growth benchmarking are available. The main contribution is methodological: converting a speculative cosmological model into an auditable object with explicit falsifiability, provenance and claim-control gates.

---

## 4. Estrutura do artigo

### 1. Introduction

- Problema: comparação de modelos cosmológicos além de LCDM.
- Risco metodológico: overclaim, dados sintéticos, ausência de covariância, comparação injusta.
- Proposta: RLL como hipótese + pipeline claim-gated.

### 2. Model definition

- Definir RLL logistic transition.
- Separar hipótese física de parametrização fenomenológica.
- Explicar `Os0`, `zt`, `wt`.
- Definir baselines: LCDM, wCDM, CPL/w0waCDM.

### 3. Data and provenance

- DESI DR2 BAO.
- H(z) / cosmic chronometers.
- fσ8 / growth.
- CMB shift.
- Pantheon+ como pendente se não materializado.
- Real vs synthetic boundary.

### 4. Likelihood and model comparison

- `chi2` diagonal.
- `chi2` com covariância.
- `AIC`, `AICc`, `BIC`.
- `N`, `k`, `dof`.
- Critérios de claim.

### 5. Preliminary results

- Declarar smoke/sanity status.
- Mostrar tabela LCDM/wCDM/CPL/RLL.
- Explicar CPL como adversário principal.
- Explicar `Os0=0.0` sem declarar descarte definitivo.

### 6. Robustness plan

- Seeds.
- Maxiter.
- Ablations.
- Posterior/MCMC/nested sampling.
- Pantheon+.
- CLASS/CAMB.

### 7. Falsifiability and limitations

- O que derruba RLL.
- O que mantém RLL como candidato.
- O que falta para claim forte.
- `TOKEN_VAZIO` como ferramenta de governança.

### 8. Conclusion

- Contribuição metodológica.
- Estado científico conservador.
- Próximos testes.

---

## 5. Figuras necessárias

| Figura | Conteúdo | Status |
|---|---|---|
| Fig. 1 | Diagrama do pipeline claim-gated | pendente |
| Fig. 2 | RLL transition `f(z)` para parâmetros canônicos | pendente |
| Fig. 3 | `E(z)` / `H(z)` comparando LCDM, CPL, RLL | pendente |
| Fig. 4 | BAO residuals por modelo | pendente |
| Fig. 5 | `w_eff_RLL(z)` vs `w_CPL(z)` | pendente |
| Fig. 6 | Robust fit stability por seed | `TOKEN_VAZIO_ROBUST_FIT` |
| Fig. 7 | Claim gate matrix | pendente |

---

## 6. Tabelas necessárias

| Tabela | Conteúdo | Status |
|---|---|---|
| T1 | parâmetros dos modelos e `k` | necessário |
| T2 | datasets e proveniência | necessário |
| T3 | resultados smoke atuais | existente/precisa consolidar |
| T4 | robust fit seeds 1..10 | `TOKEN_VAZIO_ROBUST_FIT` |
| T5 | ablations | `TOKEN_VAZIO_ABLATION` |
| T6 | claims permitidos/proibidos | criado em ledger |
| T7 | limitações e próximos testes | necessário |

---

## 7. Frase de contribuição

> This work contributes not by claiming a confirmed replacement for LCDM, but by presenting a reproducible and falsifiable framework that prevents premature claims while enabling systematic testing of an RLL logistic transition against standard and dynamic dark-energy baselines.

Em português:

> Este trabalho contribui não por declarar uma substituição confirmada para o LCDM, mas por apresentar um framework reprodutível e falsificável que impede claims prematuros enquanto permite testar sistematicamente uma transição logística RLL contra baselines padrão e de energia escura dinâmica.

---

## 8. Como não queimar o artigo

Evitar:

- linguagem messiânica em seções técnicas;
- declarar descoberta antes do robust fit;
- tratar lacuna como evidência;
- ocultar que CPL vence no smoke atual;
- comparar apenas com LCDM;
- publicar sem explicar `claim_allowed=false`;
- misturar dado sintético com dado observacional.

Preservar:

- autoria e anterioridade;
- hipótese e motivação;
- pipeline;
- rastreabilidade;
- falsificabilidade;
- honestidade de resultado.

---

## 9. Próximas tarefas para tornar paper-ready

1. Consolidar tabela dos resultados atuais em formato paper.
2. Rodar robust fit com seeds 1..10.
3. Gerar tabela de estabilidade.
4. Gerar figura `w_eff_RLL(z)` vs `w_CPL(z)`.
5. Materializar ou registrar formalmente Pantheon+ como limitação.
6. Completar CMB compressed covariance ou limitar claims.
7. Validar growth com CLASS/CAMB ou registrar backend ausente.
8. Escrever manuscrito conservador.
9. Preparar suplemento reprodutível.
10. Registrar versão/tag do estado submetido.

---

## 10. R3

```text
F_ok   = rota paper-ready definida com tese conservadora e estrutura de manuscrito.
F_gap  = faltam figuras, tabelas robustas, Pantheon+/CMB/growth completos e posterior.
F_next = consolidar resultados atuais em tabela paper sem alterar resultados canônicos.
```
