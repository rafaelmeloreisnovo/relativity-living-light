# RLL Certainty Calculation Boundary

> Escopo: separar o que pode ser calculado com certeza operacional do que exige nova rodada, covariância, MCMC, benchmark ou revisão acadêmica.

---

## 1. O que posso calcular com certeza agora

A partir de `results/structure_d/joint_real_likelihood.csv`, é seguro calcular:

1. **Ranking de modelos por AICc e BIC**.
2. **Delta AICc/BIC do RLL contra CPL**.
3. **Se `N-k=dof` está coerente**.
4. **Se todos os modelos estão presentes**: LCDM, wCDM, CPL, RLL.
5. **Se `H0` está igual em todos os modelos**, indicando fix/prior/borda que precisa ser declarado.
6. **Se `Os0` colapsou para zero**, indicando que o parâmetro autoral RLL não foi exigido pelos dados naquela rodada.
7. **Qual componente de chi2 contribui mais** quando colunas `chi2_*` estão presentes.
8. **Se um claim deve ser permitido, parcial ou bloqueado** por regras explícitas.

---

## 2. O que não posso calcular com certeza só da tabela

1. Verdade física do RLL.
2. Robustez bayesiana posterior.
3. Correção completa de covariância.
4. Validade de crescimento sem CLASS/CAMB.
5. Claim Pantheon+ sem raw files, covariância e hash.
6. Claim CMB forte com prior diagonal/proxy.
7. Superioridade acadêmica sem ablação H0/r_d/CPL/neutrinos/growth.

---

## 3. Decisão operacional: “faz bem aos dados?”

A resposta deve seguir esta árvore:

```text
Se RLL delta AICc <= 0 e delta BIC <= 0 contra CPL:
    RLL faz bem nesta tabela, PASS_LIMITED
Senão se RLL delta AICc > 0 ou delta BIC > 0 contra CPL:
    RLL não faz melhor que CPL, CLAIM_BLOCKED
Se Os0 = 0:
    bloquear claim autoral RLL, mesmo que background pareça parecido
Se H0_all_equal = True:
    marcar warning de prior/fix/borda
Se covariância/Pantheon/CMB/growth ausentes:
    limitar claim a PARTIAL ou CLAIM_BLOCKED
```

---

## 4. Comando aplicado

```bash
python3 tools/scan_rll_model_evidence.py
```

Saída resumida:

```text
claim_status=...
best_by_AICc=...
best_by_BIC=...
H0_all_equal=...
```

Saídas graváveis:

```text
results/audit/rll_model_evidence_scan.json
results/audit/rll_model_evidence_scan.md
```

---

## 5. Estado esperado da tabela atual

Com os valores atualmente versionados em `joint_real_likelihood.csv`:

```text
CPL_w0waCDM_joint_real é melhor por AICc e BIC.
RLL tem AICc e BIC maiores que CPL.
RLL tem Os0 = 0.0.
H0 = 60.0 em todos os modelos.
```

Resposta segura:

> Nesta rodada, RLL não faz melhor que CPL nos dados usados; o claim autoral fica bloqueado porque `Os0` colapsa para zero e CPL vence por AICc/BIC.

Mas também:

> Isso não prova que RLL é falso em geral; prova apenas que esta rodada, com esta política de dados/priors/covariância, não sustenta claim positivo.

---

## 6. Retroalimentação

```text
F_ok   = cálculo seguro definido e scanner aplicado
F_gap  = relatórios ainda precisam consumir scan JSON
F_next = rodar ablações para descobrir se a perda vem de H0, r_d, covariância, neutrinos, growth ou forma RLL
```
