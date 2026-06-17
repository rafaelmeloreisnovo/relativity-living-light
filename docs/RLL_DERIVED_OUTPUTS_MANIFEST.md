# RLL — Derived Outputs Manifest

**Status:** manifesto de outputs derivados para dinâmica efetiva e comparação funcional.  
**Escopo:** define artefatos esperados; não gera fit, não altera resultados canônicos, não muda claim policy.

---

## 1. Princípio

Todo output derivado deve indicar:

```text
source_artifact
created_utc
script
z_grid
quantities
claim_allowed=false
raw_datasets_modified=false
canonical_results_modified=false
```

---

## 2. Outputs de dinâmica efetiva

| Artefato | Origem | Script | Status |
|---|---|---|---|
| `results/structure_d/effective_dynamics/joint_real_likelihood_effective_dynamics.csv` | smoke canônico | `scripts/analysis/structure_d_effective_dynamics.py` | pendente de execução |
| `results/structure_d/effective_dynamics/joint_real_likelihood_effective_dynamics_manifest.json` | smoke canônico | `scripts/analysis/structure_d_effective_dynamics.py` | pendente de execução |
| `results/structure_d/effective_dynamics/*seed*_effective_dynamics.csv` | robust fits | `scripts/analysis/structure_d_effective_dynamics.py` | TOKEN_VAZIO_ROBUST_FIT |
| `results/structure_d/effective_dynamics/*seed*_effective_dynamics_manifest.json` | robust fits | `scripts/analysis/structure_d_effective_dynamics.py` | TOKEN_VAZIO_ROBUST_FIT |

---

## 3. Colunas esperadas

| Coluna | Significado |
|---|---|
| `model` | modelo cosmológico |
| `z` | redshift |
| `E` | expansão normalizada |
| `H` | taxa de expansão |
| `rho_de_eff` | densidade escura efetiva residual |
| `w_eff` | equação de estado efetiva |
| `q` | desaceleração |
| `D_C_Mpc` | distância comóvel |
| `rll_transition_f` | fração logística RLL |
| `rll_logit_f` | logit da transição RLL |

---

## 4. Outputs de comparação funcional futura

| Artefato | Função | Status |
|---|---|---|
| `results/structure_d/figures/rll_vs_cpl_w_eff.csv` | diferença `w_eff_RLL - w_CPL` | pendente |
| `results/structure_d/figures/rll_vs_cpl_q.csv` | diferença em `q(z)` | pendente |
| `results/structure_d/figures/rll_vs_cpl_distance_delta.csv` | diferença em `D_C(z)` | pendente |
| `results/structure_d/figures/rll_logit_transition.csv` | linearidade logit da transição | pendente |
| `results/structure_d/figures/boundary_frequency_by_seed.csv` | frequência de parâmetros na borda | TOKEN_VAZIO_ROBUST_FIT |
| `results/structure_d/figures/dynamic_viscosity_matrix.csv` | viscosidade por dataset/seed | TOKEN_VAZIO_ROBUST_FIT |

---

## 5. Gates

| Gate | Condição | Estado |
|---|---|---|
| CI | testes unitários passam | pendente |
| smoke effective dynamics | script roda no canônico | pendente |
| robust effective dynamics | script roda em seeds | TOKEN_VAZIO_ROBUST_FIT |
| CPL functional comparator | diferenças funcionais geradas | pendente |
| GEDE baseline | baseline implementado | TOKEN_VAZIO_GEDE_BASELINE |
| posterior | MCMC/nested | TOKEN_VAZIO_POSTERIOR |

---

## 6. R3

```text
F_ok   = manifesto de outputs derivados criado.
F_gap  = artefatos derivados ainda precisam ser gerados por execução local/CI.
F_next = criar comparador funcional RLL vs CPL a partir do CSV de dinâmica efetiva.
```
