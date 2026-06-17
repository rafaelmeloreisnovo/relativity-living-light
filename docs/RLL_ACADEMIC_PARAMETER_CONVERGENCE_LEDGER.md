# RLL Academic Parameter Convergence Ledger

> Cadeia de custódia documental — 2026-06-17  
> Escopo: agregar somente parâmetros cosmológicos e nuisance parameters já fundamentados na literatura acadêmica, sem encaixe artificial de números e sem tratar parâmetros autorais RLL como constantes externas.

---

## 1. Regra central

Este ledger existe para impedir três erros:

1. **Plágio conceitual ou textual** — relatórios devem parafrasear e citar, não copiar prosa de artigos.
2. **Encaixe artificial de número** — nenhum parâmetro deve ser adicionado só para melhorar AIC/BIC.
3. **Mistura entre ciência externa e hipótese RLL** — parâmetros como `H0`, `Omega_b h^2`, `r_d`, `sigma8`, `w0`, `wa`, `N_eff` e `Sigma m_nu` são literatura/observação/modelo padrão; `Os0`, `zt`, `wt` são autorais RLL e devem permanecer separados.

A fonte computacional canônica correspondente é:

```text
data/inputs/cosmology_joint/parameter_origin_registry.json
```

---

## 2. Camadas de parâmetros

| Camada | Função | Exemplos | Pode ser chamado de “comprovado”? |
|---|---|---|---|
| Consenso/base | Base do modelo cosmológico e observáveis principais | `H0`, `Omega_m`, `Omega_b h^2`, `Omega_c h^2`, `r_d`, `theta_*`, `sigma8` | Sim, como parâmetro/observável estabelecido; valores dependem de dataset/prior. |
| Extensão padrão | Extensões acadêmicas usadas para testar ΛCDM | `w`, `w0`, `wa`, `Omega_k`, `N_eff`, `Sigma m_nu`, `S8` | Sim, como extensão academicamente aceita; não como evidência automática. |
| Nuisance observacional | Calibração/covariância de datasets | `M_B`, `C_SN`, `C_BAO`, `R_shift` | Sim, como componente de likelihood/calibração; não como física RLL. |
| RLL autoral | Hipótese fenomenológica Rafael/RLL | `Os0`, `zt`, `wt` | Não como parâmetro externo; sim como parâmetro autoral a ser testado. |

---

## 3. Parâmetros reais que devem entrar no ecossistema RLL

### 3.1 Expansão e orçamento de energia

| Parâmetro | Papel acadêmico | Integração correta no RLL | Referências |
|---|---|---|---|
| `H0` | Taxa de expansão atual. | Livre ou prior; nunca preso em borda sem relatório. Rodar no mínimo: sem prior, Planck, SH0ES e prior largo. | Planck2018; SH0ES2021; PantheonPlus2022; DESI_DR2_2025 |
| `h` | `H0/100`; converte densidades físicas. | Derivado de `H0`; necessário para `Omega_b h^2` e `Omega_c h^2`. | Planck2018 |
| `Omega_m` | Densidade total de matéria hoje. | Livre ou derivado; deve incluir neutrinos massivos se `Sigma m_nu` estiver ativo. | Planck2018; PantheonPlus2022; DESI_DR2_2025 |
| `Omega_b h^2` | Densidade física de bárions. | Prior/fit quando `r_d` for derivado. | Planck2018 |
| `Omega_c h^2` | Densidade física de matéria escura fria. | Prior/fit; não substituir silenciosamente por `Omega_m`. | Planck2018 |
| `Omega_r` | Densidade de radiação. | Derivar de `T_CMB`, `N_eff` e política de neutrinos. | Planck2018 |
| `Omega_k` | Curvatura FLRW. | Fixo plano por padrão ou livre para todos os modelos na mesma rodada. | Planck2018; CAMB1999; CLASS2011 |

---

### 3.2 BAO / régua padrão

| Parâmetro/observável | Papel acadêmico | Integração correta no RLL | Referências |
|---|---|---|---|
| `r_d` | Horizonte sonoro no arrasto; régua BAO. | Fixo para todos ou derivado para todos. Não misturar política por modelo. | Planck2018; DESI_DR2_2025 |
| `D_M/r_d` | BAO transversal. | Predição por modelo + covariância DESI. | DESI_DR2_2025 |
| `D_H/r_d` | BAO radial. | Predição por modelo + covariância DESI. | DESI_DR2_2025 |
| `D_V/r_d` | BAO isotrópico/legacy. | Usar apenas quando o dataset for isotrópico; não substituir anisotrópico moderno. | DESI_DR2_2025 |
| `C_BAO` | Covariância BAO. | Não conta em `k`, mas sua ausência bloqueia claim. | DESI_DR2_2025 |

---

### 3.3 Energia escura dinâmica

| Parâmetro | Papel acadêmico | Integração correta no RLL | Referências |
|---|---|---|---|
| `w` | Baseline wCDM constante. | Comparador obrigatório antes de atribuir ganho ao RLL. | ChevallierPolarski2001; Linder2003; DESI_DR2_2025 |
| `w0` | Valor atual na parametrização CPL/w0wa. | Fitar CPL separadamente; projeção RLL→`w0` só como diagnóstico derivado. | ChevallierPolarski2001; Linder2003; DESI_DR2_2025 |
| `wa` | Evolução temporal em CPL/w0wa. | Fitar CPL separadamente; não fundir com RLL sem contar `k`. | ChevallierPolarski2001; Linder2003; DESI_DR2_2025 |
| `w_eff(z)` | Diagnóstico físico/efetivo do modelo. | Para RLL, exportar grade e localizar cruzamentos de `w=-1` sem forçar resultado. | DESI_DR2_2025; DESI_Extended_DE_2025 |

---

### 3.4 CMB e parâmetros primordiais

| Parâmetro/observável | Papel acadêmico | Integração correta no RLL | Referências |
|---|---|---|---|
| `theta_*` | Escala acústica angular do CMB. | Usar com covariância/likelihood adequada; declarar se for compressed/diagonal. | Planck2018 |
| `R_shift` | Prior comprimido de distância CMB. | Parcial se sem covariância oficial completa. | Planck2018 |
| `ln(10^10 A_s)` | Amplitude primordial. | Necessário para CMB/growth, não para BAO/SN puro. | Planck2018 |
| `n_s` | Índice espectral. | Necessário para CMB/matter power; declarar fixo/prior/fit. | Planck2018 |
| `tau` | Profundidade óptica de reionização. | Necessário em likelihood CMB completa; não inventar em background-only. | Planck2018 |

---

### 3.5 Neutrinos e radiação efetiva

| Parâmetro | Papel acadêmico | Integração correta no RLL | Referências |
|---|---|---|---|
| `Sigma m_nu` | Soma das massas dos neutrinos. | Rodar política comum em todos os modelos; forte degenerescência com expansão/growth. | Planck2018; DESI_DR2_2025 |
| `N_eff` | Graus relativísticos efetivos. | Ativar quando variar radiação/régua sonora/CMB além do base model. | Planck2018 |

---

### 3.6 Crescimento de estrutura

| Parâmetro/observável | Papel acadêmico | Integração correta no RLL | Referências |
|---|---|---|---|
| `sigma8` | Amplitude de flutuações em 8 Mpc/h. | Livre/prior quando usar crescimento, RSD ou lensing. | Planck2018; CAMB1999; CLASS2011 |
| `S8` | Diagnóstico de lensing/growth. | Derivado usualmente como `sigma8 sqrt(Omega_m/0.3)`. | Planck2018 |
| `f sigma8(z)` | Observável RSD de crescimento. | Claim bloqueado até benchmark CLASS/CAMB ou marcado como proxy. | CLASS2011; CAMB1999; DESI_DR2_2025 |
| `D_+(z)` | Crescimento linear. | Se calculado por aproximação, declarar; para claim forte, comparar com CLASS/CAMB. | CLASS2011; CAMB1999 |

---

### 3.7 Supernovas Ia

| Parâmetro/bloco | Papel acadêmico | Integração correta no RLL | Referências |
|---|---|---|---|
| `M_B` / `M_abs` | Calibração/offset absoluto de SNe Ia. | Nuisance; contar em `k` se fitted. | PantheonPlus2022; SH0ES2021 |
| `C_SN` | Covariância estatística+sistemática. | Não conta em `k`, mas ausência bloqueia claim Pantheon+. | PantheonPlus2022 |
| Cepheid/SH0ES calibration | Prior local de distância. | Usar como rodada separada, nunca misturada sem declarar. | SH0ES2021; PantheonPlus2022 |

---

## 4. Parâmetros autorais RLL: manter separados

| Parâmetro | Status correto | Regra |
|---|---|---|
| `Os0` | Autoral RLL | Conta em `k`; não é parâmetro externo. |
| `zt` | Autoral RLL | Conta em `k`; precisa prior bounds e sensibilidade. |
| `wt` | Autoral RLL | Conta em `k`; deve ser positivo e testado contra degenerescência. |

Esses parâmetros podem ser academicamente legítimos como **ansatz fenomenológico**, mas não podem ser apresentados como “comprovados”. O que é comprovado é a base observacional usada para testá-los.

---

## 5. Política de claim

### Permitido

> “RLL é testado contra ΛCDM, wCDM e CPL usando parâmetros cosmológicos estabelecidos e nuisance parameters declarados; parâmetros autorais são separados e penalizados em `k`.”

### Proibido

> “RLL usa parâmetros comprovados, portanto RLL está comprovado.”

### Correto

> “A base observacional e paramétrica é acadêmica; a hipótese RLL permanece em teste.”

---

## 6. Bibliografia operacional

- Planck2018 — Planck Collaboration, *Planck 2018 results. VI. Cosmological parameters*, arXiv:1807.06209, DOI: 10.1051/0004-6361/201833910.
- DESI_DR2_2025 — DESI Collaboration, *DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints*, arXiv:2503.14738.
- PantheonPlus2022 — Brout, Scolnic, Popovic, Riess et al., *The Pantheon+ Analysis: Cosmological Constraints*, arXiv:2202.04077.
- SH0ES2021 — Riess et al., *A Comprehensive Measurement of the Local Value of the Hubble Constant with 1 km/s/Mpc Uncertainty from HST and SH0ES*, arXiv:2112.04510.
- ChevallierPolarski2001 — Chevallier & Polarski, *Accelerating Universes with Scaling Dark Matter*, arXiv:gr-qc/0009008.
- Linder2003 — Linder, *Exploring the Expansion History of the Universe*, arXiv:astro-ph/0208512.
- CAMB1999 — Lewis, Challinor & Lasenby, *Efficient Computation of CMB anisotropies in closed FRW models*, arXiv:astro-ph/9911177.
- CLASS2011 — Blas, Lesgourgues & Tram, *The Cosmic Linear Anisotropy Solving System (CLASS) II: Approximation schemes*, arXiv:1104.2933.
- CosmoMC2002 — Lewis & Bridle, *Cosmological parameters from CMB and other data: a Monte-Carlo approach*, arXiv:astro-ph/0205436.
- Cobaya2020 — Torrado & Lewis, *Cobaya: Code for Bayesian Analysis of hierarchical physical models*, arXiv:2005.05290.

---

## 7. Próximo passo computacional

1. Validar JSON do registry.
2. Fazer o pipeline consumir `parameter_origin_registry.json` antes de reportar `k`, AIC, AICc e BIC.
3. Bloquear claim se qualquer dataset usado não tiver política de covariância declarada.
4. Rodar ablação:
   - base flat;
   - H0 livre/prior;
   - r_d fixo vs derivado;
   - CPL completo;
   - RLL com penalização explícita;
   - neutrinos/N_eff;
   - growth com CLASS/CAMB.

FIAT LUX — ciência integrada, sem colagem, sem número encaixado.
