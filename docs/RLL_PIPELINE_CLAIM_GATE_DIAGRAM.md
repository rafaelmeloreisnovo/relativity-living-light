# RLL — Pipeline Claim-Gated Diagram

**Status:** Figura F1 paper-ready em formato Markdown simples.  
**Escopo:** diagrama documental; não altera dados, fórmulas, resultados ou claims.

---

## 1. Figura F1 — Pipeline claim-gated

```text
[Hipótese RLL / transição logística]
        ↓
[Definição computacional executável]
        ↓
[Comparadores obrigatórios]
        ├─ LCDM
        ├─ wCDM
        ├─ CPL / w0waCDM
        └─ RLL
        ↓
[Inputs observacionais]
        ├─ Hz
        ├─ DESI DR2 BAO
        ├─ fsigma8
        ├─ CMB shift
        └─ Pantheon+ quando materializado
        ↓
[Joint likelihood]
        ↓
[Métricas]
        ├─ chi2
        ├─ AIC
        ├─ AICc
        ├─ BIC
        ├─ N
        ├─ k
        └─ dof
        ↓
[Gates]
        ├─ dados reais completos?
        ├─ covariâncias completas?
        ├─ CLASS/CAMB ou growth externo?
        ├─ robust fit com seeds?
        ├─ posterior/incertezas?
        ├─ RLL competitivo contra LCDM?
        └─ RLL competitivo contra CPL?
        ↓
[Decisão]
        ├─ se qualquer gate falha: claim_allowed=false
        └─ se todos os gates passam: claim pode ser reavaliado
```

---

## 2. Estados de verdade

```text
Conceito
  ↓ equação definida
Fórmula
  ↓ implementação executável
Código
  ↓ maxiter baixo / sanity run
Smoke
  ↓ seeds múltiplas + maxiter robusto
Robust fit
  ↓ blocos isolados
Ablation
  ↓ MCMC / nested / deep fit
Posterior
  ↓ gates completos
Claim condicionado
```

Qualquer falha em dataset, covariância, backend, robust fit, posterior ou comparação contra CPL retorna para:

```text
TOKEN_VAZIO → próxima medida → nova execução rastreável
```

---

## 3. Claim boundary visual

```text
Conceito não é prova.
Código não é universo.
Smoke não é fit final.
Fit sem covariância não é claim forte.
Dado sintético não confirma cosmologia.
TOKEN_VAZIO protege verdade futura.
```

---

## 4. Legenda paper-ready

> Figure F1. Claim-gated RLL validation pipeline. The framework separates hypothesis, executable model, real-data likelihood, model-comparison metrics, robustness checks and claim gates. Missing datasets, covariances, external growth backends or robust-fit evidence are represented as `TOKEN_VAZIO` states and force `claim_allowed=false` until resolved.

---

## 5. R3

```text
F_ok   = diagrama claim-gated criado para uso como Figura F1.
F_gap  = ainda faltam figuras quantitativas F2-F6 e robustas F7-F10.
F_next = criar nota executiva de uma página.
```
