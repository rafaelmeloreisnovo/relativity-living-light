# RLL — Current Results Paper Table

**Status:** tabela paper-ready do artefato canônico atual.  
**Fonte primária:** `results/structure_d/joint_real_likelihood.json` e `results/structure_d/joint_real_likelihood.csv`.  
**Regra:** este documento é descritivo; não altera dados reais, fórmulas, outputs canônicos nem claims.

---

## 1. Identidade do artefato

| Campo | Valor |
|---|---|
| schema | `rll.joint_real_likelihood.v2` |
| created_utc | `2026-06-13T02:53:51Z` |
| optimizer | `scipy.optimize.differential_evolution` |
| seed | `42` |
| tol | `0.001` |
| maxiter LCDM | `3` |
| maxiter wCDM | `3` |
| maxiter CPL | `3` |
| maxiter RLL | `3` |
| N | `64` |
| dataset_type | `real_observational` |
| claim_allowed | `false` |
| interpretation_label | `lcdm_preferred` |
| rd_policy | `derived_power_law_from_H0_Om_Ob_h2_for_all_models` |

**Interpretação:** esta execução é `smoke/sanity test`, não fit cosmológico final.

---

## 2. Datasets usados

| Bloco | Caminho | Papel |
|---|---|---|
| Hz | `data/real/Hz_data_real.csv` | expansão H(z) |
| DESI DR2 BAO primary | `data/real/cosmology/desi_dr2_bao_primary_points.csv` | BAO |
| DESI DR2 BAO covariance | `data/real/desi_dr2_bao_covariance.csv` | covariância BAO oficial/materializada |
| fsigma8 | `data/real/cosmology/fsigma8_growth_real.csv` | crescimento / estrutura |
| CMB shift | `data/real/CMB_shift_real.json` | CMB compressed parcial |
| parameter registry | `data/inputs/cosmology_joint/parameter_origin_registry.json` | origem dos parâmetros |

---

## 3. Tabela principal para manuscrito

| Modelo | chi2 | AIC | AICc | BIC | N | k | dof | Status nesta execução |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| LCDM | 84.48241222580135 | 94.48241222580135 | 95.51689498442204 | 105.27682764259971 | 64 | 5 | 59 | baseline |
| wCDM | 83.71037717797158 | 95.71037717797158 | 97.1840613884979 | 108.66367567812961 | 64 | 6 | 58 | melhora chi2 levemente, mas piora ICs |
| CPL/w0waCDM | 62.071708706289364 | 76.07170870628937 | 78.07170870628937 | 91.18389028980707 | 64 | 7 | 57 | preferido no smoke atual |
| RLL | 84.48241222572261 | 100.48241222572261 | 103.10059404390444 | 117.75347689259999 | 64 | 8 | 56 | não preferido; colapsa para `Os0=0.0` |

---

## 4. Decomposição por blocos de chi2

| Modelo | chi2_Hz | chi2_DESI_DR2_BAO | chi2_fsigma8 | chi2_CMB_shift |
|---|---:|---:|---:|---:|
| LCDM | 19.430741008634875 | 20.575030662200746 | 23.630658522602975 | 20.845982032362752 |
| wCDM | 19.365634730204704 | 17.48883027438094 | 22.797439542715814 | 24.058472630670114 |
| CPL/w0waCDM | 19.220020703366146 | 12.082522240097463 | 18.87551935235649 | 11.893646410469268 |
| RLL | 19.43074096832219 | 20.575029041552828 | 23.630658584576636 | 20.84598363127095 |

**Leitura:** CPL reduz principalmente BAO, growth proxy e CMB shift no smoke atual. RLL fica praticamente idêntico ao LCDM quando `Os0=0.0`.

---

## 5. Parâmetros destacados

| Modelo | H0 | Om | OL | Ob_h2 | sigma8 | w | w0 | wa | Os0 | zt | wt |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| LCDM | 60.0 | 0.37541381103514887 | 0.9771327179758683 | 0.026 | 0.6147302831680962 | — | — | — | — | — | — |
| wCDM | 60.0 | 0.3740141812825024 | 0.9497249070259529 | 0.026 | 0.6151824032688435 | -0.9725236468940587 | — | — | — | — | — |
| CPL/w0waCDM | 60.0 | 0.364109717761877 | 0.684511268689338 | 0.024058480593615865 | 0.6226074269985636 | — | -0.3 | -1.835701089847297 | — | — | — |
| RLL | 60.0 | 0.3754138109513542 | 0.9771327214966472 | 0.026 | 0.6147304340494005 | — | — | — | 0.0 | 0.48913585347939664 | 0.5725207843474277 |

---

## 6. Deltas contra LCDM

| Modelo | delta_chi2 | delta_AIC | delta_AICc | delta_BIC | Interpretação |
|---|---:|---:|---:|---:|---|
| wCDM - LCDM | -0.7720350478297746 | 1.2279649521702254 | 1.6671664040758571 | 3.386848035529894 | melhora chi2, mas penalização por k torna ICs piores |
| CPL - LCDM | -22.41070351951199 | -18.410703519511983 | -17.445186278132667 | -14.092937352792646 | preferido por chi2 e critérios de informação |
| RLL - LCDM | -7.87423459769343e-11 | 5.999999999921258 | 7.583699059482399 | 12.476649250000278 | chi2 indistinguível de LCDM, mas ICs piores por k maior |

---

## 7. Claim boundary do resultado atual

O resultado atual permite dizer:

> O pipeline conjunto real roda e compara LCDM, wCDM, CPL/w0waCDM e RLL sob o mesmo artefato. Na execução smoke atual, CPL/w0waCDM é preferido por chi2/AIC/AICc/BIC. RLL permanece candidato testável, mas não é preferido porque `Os0=0.0` desativa a camada RLL e o modelo é penalizado por parâmetros extras.

O resultado atual não permite dizer:

- RLL está confirmado;
- RLL vence LCDM;
- RLL vence CPL;
- RLL resolve energia escura;
- RLL resolve H0/S8;
- RLL deve ser descartado estruturalmente.

---

## 8. Notas de limitação

| Limitação | Estado | Consequência |
|---|---|---|
| `maxiter=3` | smoke/sanity | não prova convergência |
| Pantheon+ completo | `TOKEN_VAZIO_DATASET` se não materializado no joint | claim cosmológico amplo bloqueado |
| CMB compressed completo | `TOKEN_VAZIO_COVARIANCE` | CMB ainda parcial |
| growth externo | `TOKEN_VAZIO_BACKEND` | fsigma8/D+ ainda sem CLASS/CAMB |
| robust fit seeds 1..10 | `TOKEN_VAZIO_ROBUST_FIT` | ranking final não estabelecido |
| posterior/MCMC/nested | `TOKEN_VAZIO_POSTERIOR` | sem inferência robusta de incertezas |

---

## 9. Legenda paper-ready

```text
Table X. Preliminary joint real-data smoke comparison of LCDM, wCDM, CPL/w0waCDM and RLL. The run uses N=64 effective points and maxiter=3 for all models; therefore, results are interpreted as a sanity check rather than a final cosmological fit. CPL/w0waCDM is favored in this run. RLL collapses to the LCDM-like limit because Os0=0.0 and is penalized by AIC/AICc/BIC due to its larger parameter count. Strong claims remain blocked by the claim-gate policy.
```

---

## 10. R3

```text
F_ok   = tabela paper-ready consolidada a partir dos resultados canônicos existentes.
F_gap  = ainda faltam robust fit, ablações, posterior, Pantheon+, CMB covariance completa e growth externo.
F_next = registrar lacuna operacional de output_stem/CLI para impedir sobrescrita de resultado canônico em execução robusta.
```
