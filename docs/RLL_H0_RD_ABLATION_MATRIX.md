# RLL H0/r_d Ablation Matrix

> Matriz operacional gerada a partir da issue #423.  
> Escopo: tornar explícitas as políticas de `H0` e `r_d` antes de interpretar RLL contra CPL/w0waCDM.

---

## Runs obrigatórias

| run_id | H0_policy | H0_prior | rd_policy | rd_fixed_value_mpc | claim_boundary |
|---|---|---|---|---:|---|
| `h0_broad_free__rd_fixed_for_all` | broad_free | broad/free/no_external_H0_prior | fixed_for_all | 147.78 | sensitivity_only_until_covariance_MCMC_and_CLASS_CAMB_gates_are_satisfied |
| `h0_broad_free__rd_derived_for_all` | broad_free | broad/free/no_external_H0_prior | derived_for_all | TOKEN_VAZIO | sensitivity_only_until_covariance_MCMC_and_CLASS_CAMB_gates_are_satisfied |
| `h0_planck_prior__rd_fixed_for_all` | planck_prior | Planck2018 | fixed_for_all | 147.78 | sensitivity_only_until_covariance_MCMC_and_CLASS_CAMB_gates_are_satisfied |
| `h0_planck_prior__rd_derived_for_all` | planck_prior | Planck2018 | derived_for_all | TOKEN_VAZIO | sensitivity_only_until_covariance_MCMC_and_CLASS_CAMB_gates_are_satisfied |
| `h0_shoes_local_prior__rd_fixed_for_all` | shoes_local_prior | SH0ES_local_distance_ladder | fixed_for_all | 147.78 | sensitivity_only_until_covariance_MCMC_and_CLASS_CAMB_gates_are_satisfied |
| `h0_shoes_local_prior__rd_derived_for_all` | shoes_local_prior | SH0ES_local_distance_ladder | derived_for_all | TOKEN_VAZIO | sensitivity_only_until_covariance_MCMC_and_CLASS_CAMB_gates_are_satisfied |

---

## Arquivos canônicos

```text
data/inputs/cosmology_joint/h0_rd_ablation_matrix.json
data/inputs/cosmology_joint/h0_rd_ablation_matrix.csv
tools/make_h0_rd_ablation_matrix.py
```

---

## Regra de interpretação

Cada run precisa gerar uma tabela com:

```text
model, chi2, AIC, AICc, BIC, N, k, dof,
H0_policy, rd_policy, H0, rd, Os0,
Delta_AICc_RLL_CPL, Delta_BIC_RLL_CPL, claim_status
```

Depois disso, cada tabela deve ser varrida por:

```bash
python3 tools/run_rll_academic_claim_governance.py --input results/structure_d/ablation/<run_id>.csv
```

---

## Fronteira de claim

Se `Os0` continuar zero e CPL continuar melhor por AICc/BIC em todas as políticas, a conclusão negativa fica mais estável.

Se RLL melhorar apenas em uma política, a conclusão é **sensibilidade dependente**, não prova.

Se RLL superar CPL por AICc/BIC, ainda assim o status máximo é `PASS_LIMITED` até covariância, MCMC e CLASS/CAMB.
