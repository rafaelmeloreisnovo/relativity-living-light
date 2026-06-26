# RLL Data-Fit Decision Tree

> Pergunta: “faz bem meus dados?”  
> Resposta operacional: só depois de medir contra CPL/w0waCDM, com k, covariância e claim boundary.

---

## Decision tree

```text
START
  |
  |-- CSV existe e tem LCDM, wCDM, CPL, RLL?
  |       |-- não -> CLAIM_BLOCKED: baseline ausente
  |       |-- sim
  |
  |-- N-k=dof consistente em todas as linhas?
  |       |-- não -> CLAIM_BLOCKED: tabela inconsistente
  |       |-- sim
  |
  |-- CPL presente?
  |       |-- não -> CLAIM_BLOCKED: sem baseline dinâmico padrão
  |       |-- sim
  |
  |-- RLL Delta AICc <= 0 e Delta BIC <= 0 contra CPL?
  |       |-- sim -> PASS_LIMITED: faz bem nesta tabela, ainda limitado por covariância/MCMC
  |       |-- não
  |
  |-- RLL Os0 = 0?
  |       |-- sim -> CLAIM_BLOCKED: parâmetro autoral colapsou
  |       |-- não -> CLAIM_BLOCKED: pior que CPL nesta rodada
  |
  |-- H0 igual em todos os modelos?
          |-- sim -> WARNING: rodar ablação H0/r_d
          |-- não -> continuar ablação normal
```

---

## Safe answer format

```text
Nesta rodada, o modelo [X] é melhor por AICc/BIC.
RLL Delta AICc vs CPL = [...]
RLL Delta BIC vs CPL = [...]
Os0 = [...]
H0_all_equal = [...]
claim_status = [...]
```

---

## Forbidden answer format

```text
RLL está provado.
RLL vence a cosmologia.
RLL faz bem aos dados sem comparar com CPL.
```

---

## Required command

```bash
python3 tools/scan_rll_model_evidence.py
```

---

## Current expected answer from versioned table

```text
Nesta rodada, CPL/w0waCDM é melhor por AICc e BIC.
RLL fica pior que CPL.
Os0 = 0.0.
H0 é igual em todos os modelos.
claim_status = CLAIM_BLOCKED.
```

Isso responde “faz bem meus dados?” de forma segura:

> Nesta rodada específica, não. O RLL não faz melhor que CPL nos dados usados; o resultado exige ablação H0/r_d e revisão de covariância antes de qualquer claim positivo.
