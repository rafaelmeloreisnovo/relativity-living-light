# RLL — Supplement Package Map

**Status:** mapa de pacote suplementar para paper, auditoria e reprodução.  
**Escopo:** organização documental; não altera dados, fórmulas, resultados ou claims.

---

## 1. Objetivo

Definir quais materiais devem acompanhar um manuscrito RLL conservador para permitir:

- reprodução;
- auditoria;
- leitura das limitações;
- separação real/sintético;
- verificação de claims;
- continuidade por laboratório, banca ou colaborador.

---

## 2. Pacote mínimo do paper

```text
paper/
  manuscript.md
  figures/
  tables/
  supplement/
  reproducibility/
  claim_gates/
  data_provenance/
```

Este mapa descreve o conteúdo lógico. A criação física desses diretórios deve ocorrer em PR dedicado se necessário.

---

## 3. Manuscrito principal

| Item | Fonte | Status |
|---|---|---|
| Título conservador | `docs/RLL_PAPER_READY_ROUTE.md` | definido |
| Abstract provisório | `docs/RLL_PAPER_READY_ROUTE.md` | definido |
| Contribuição | `docs/RLL_PAPER_READY_ROUTE.md` | definida |
| Resultado atual | `docs/RLL_CURRENT_RESULTS_PAPER_TABLE.md` | definido |
| Limitações | `docs/RLL_CLAIM_GATE_LEDGER.md` + este mapa | definido |
| Pipeline visual | `docs/RLL_PIPELINE_CLAIM_GATE_DIAGRAM.md` | criado |

---

## 4. Suplemento A — Modelo e equações

| Conteúdo | Arquivo-fonte sugerido | Status |
|---|---|---|
| Definição RLL | docs teóricos + `src/rll/cosmology_fairness.py` | parcial |
| Baselines LCDM/wCDM/CPL | `src/rll/cosmology_fairness.py` | implementado |
| Distâncias cosmológicas | `src/rll/cosmology_fairness.py` | implementado |
| AIC/AICc/BIC | likelihood/cosmology fairness | implementado |
| `w_eff_RLL(z)` | `src/rll/cosmology_fairness.py` | implementado |
| mapa de k/parâmetros | parameter registry | parcial |

---

## 5. Suplemento B — Dados e proveniência

| Conteúdo | Fonte | Status |
|---|---|---|
| Hz | `data/real/Hz_data_real.csv` | materializado |
| DESI DR2 BAO primary | `data/real/cosmology/desi_dr2_bao_primary_points.csv` | materializado |
| DESI DR2 covariance | `data/real/desi_dr2_bao_covariance.csv` | materializado |
| fsigma8 | `data/real/cosmology/fsigma8_growth_real.csv` | materializado/parcial por backend |
| CMB shift | `data/real/CMB_shift_real.json` | parcial |
| Pantheon+ | externo | TOKEN_VAZIO_DATASET |
| hashes | covariance/input manifest | parcial |

---

## 6. Suplemento C — Resultados atuais

| Conteúdo | Fonte | Status |
|---|---|---|
| JSON canônico | `results/structure_d/joint_real_likelihood.json` | existente |
| CSV canônico | `results/structure_d/joint_real_likelihood.csv` | existente |
| manifesto covariance | `results/structure_d/joint_real_likelihood_covariance_manifest.json` | existente |
| tabela paper | `docs/RLL_CURRENT_RESULTS_PAPER_TABLE.md` | criada |
| interpretação | `results/structure_d/joint_real_likelihood_readme.md` | existente |

---

## 7. Suplemento D — Robust fit futuro

| Conteúdo | Status | Bloqueio |
|---|---|---|
| seeds 1..10 | TOKEN_VAZIO_ROBUST_FIT | output versionado |
| maxiter>=100 | TOKEN_VAZIO_ROBUST_FIT | output versionado |
| agregador de seeds | TOKEN_VAZIO_ROBUST_FIT | script futuro |
| frequência `Os0=0.0` | TOKEN_VAZIO_ROBUST_FIT | robust fit |
| deltas contra CPL | TOKEN_VAZIO_ROBUST_FIT | robust fit |
| tabela de estabilidade | TOKEN_VAZIO_ROBUST_FIT | robust fit |

---

## 8. Suplemento E — Ablações

| Conteúdo | Fonte | Status |
|---|---|---|
| matriz de ablações | `docs/RLL_ABLATION_MATRIX.md` | criada |
| DESI+Hz | futuro | TOKEN_VAZIO_ABLATION |
| sem growth | futuro | TOKEN_VAZIO_ABLATION |
| sem CMB | futuro | TOKEN_VAZIO_ABLATION |
| `Os0>0` | futuro | TOKEN_VAZIO_ABLATION |
| `w_eff_RLL` vs `w_CPL` | futuro | TOKEN_VAZIO_ABLATION |

---

## 9. Suplemento F — Claims e riscos

| Conteúdo | Fonte | Status |
|---|---|---|
| claim gate | `docs/RLL_CLAIM_GATE_LEDGER.md` | criado |
| risk register | `docs/RLL_RISK_REGISTER.md` | criado |
| estrada canônica | `docs/RLL_ESTRADA_CANONICA_EXECUCAO.md` | criado |
| output stem gap | `docs/RLL_OUTPUT_STEM_CLI_GAP.md` | criado |
| next safe actions | `docs/RLL_NEXT_SAFE_ACTIONS_INDEX.md` | criado |

---

## 10. Checklist de submissão futura

Antes de qualquer submissão pública forte:

- [ ] título sem overclaim;
- [ ] abstract afirma pipeline e hipótese, não confirmação;
- [ ] tabela atual marcada como smoke;
- [ ] `claim_allowed=false` explicado;
- [ ] CPL incluído como comparador;
- [ ] limitações explícitas;
- [ ] dados sintéticos separados;
- [ ] hashes e comandos registrados;
- [ ] robust fit incluído ou marcado como ausente;
- [ ] Pantheon+/CMB/growth marcados conforme estado real.

---

## 11. R3

```text
F_ok   = mapa do pacote suplementar criado; paper agora tem estrutura de apoio auditável.
F_gap  = pacote físico ainda não montado; robust fit/dados/backends seguem pendentes.
F_next = criar checklist de PR antes do robust fit.
```
