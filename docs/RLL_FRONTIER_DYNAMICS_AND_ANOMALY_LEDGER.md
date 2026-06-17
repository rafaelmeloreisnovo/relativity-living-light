# RLL — Frontier Dynamics and Anomaly Ledger

**Status:** documento-mãe acadêmico, técnico e conservador para posicionar RLL na fronteira contemporânea da cosmologia observacional.  
**Escopo:** formalismo, quadro epistemológico, mapa de acoplamentos, parâmetros, anomalias, hipóteses e fila de testes.  
**Regra:** este documento não altera dados brutos, fórmulas computacionais, resultados canônicos ou `claim_allowed=false`.

---

## Abstract

This ledger positions Relativity Living Light (RLL) as a candidate phenomenological model of effective transition/emergent dark-energy dynamics. The repository currently contains an auditable real-data validation stack comparing LCDM, wCDM, CPL/w0waCDM and RLL under a claim-gated workflow. The current canonical result is a smoke/sanity joint likelihood run, not a final cosmological fit. In that run, CPL/w0waCDM is favored, while RLL collapses to the LCDM-like limit through `Os0=0.0`, incurring information-criterion penalties because of its larger parameter count.

The purpose of this document is to formalize the scientific object now present in the repository: not a confirmed cosmological theory, but a falsifiable computational research program. The document defines the semantic field, mathematical operators, inverse/forward tests, anomaly couplings, emergent frontier comparisons, and post-smoke validation requirements necessary before any strong physical claim can be considered.

---

## 1. Executive academic position

The strongest academically valid statement is:

> RLL is a testable phenomenological transition model that should be evaluated as a member of the broader family of dynamical/emergent dark-energy parameterizations, against LCDM, wCDM, CPL/w0waCDM, GEDE, early/late dark-energy variants, scalar-field reconstructions and coupled dark-sector models, using real-data likelihoods, robustness matrices, posterior inference, ablation studies, effective-function reconstructions and explicit claim gates.

The strongest currently invalid statement is:

> RLL is confirmed or has already replaced LCDM/CPL.

Current repository evidence supports the first statement and blocks the second.

---

## 2. State of the repository object

### 2.1 What exists

```text
hypothesis        = RLL effective transition / living-light cosmological ansatz
implementation    = joint real-data likelihood pipeline
comparators       = LCDM, wCDM, CPL/w0waCDM, RLL
data axes         = H(z), DESI DR2 BAO, fsigma8 proxy, CMB shift partial
metrics           = chi2, AIC, AICc, BIC, N, k, dof
claim policy      = claim_allowed=false until gates pass
safe execution    = output-stem wrapper for versioned robust fits
```

### 2.2 Current canonical smoke result

```text
CPL/w0waCDM = preferred in the current smoke run
RLL         = not preferred
RLL Os0     = 0.0
claim       = blocked
run type    = smoke/sanity, not final cosmological fit
```

### 2.3 What this means

The current result does not falsify every possible RLL family. It falsifies only the claim that the current implementation, current bounds, current datasets and current low-iteration smoke execution already outperform the relevant baselines. The result is therefore a diagnostic state, not a terminal scientific conclusion.

---

## 3. Conceptual taxonomy

| Term | Technical meaning | RLL relevance | Claim risk |
|---|---|---|---|
| dynamical dark energy | time/redshift-dependent equation of state | core comparison class | high if asserted without posterior |
| emergent dark energy | dark-energy density or effect emerges near a transition epoch | closest conceptual family | medium/high |
| transition model | model with characteristic redshift and width | direct RLL architecture | medium |
| CPL/w0waCDM | two-parameter redshift dynamics `w(a)=w0+wa(1-a)` | strongest current baseline | low; standard comparator |
| GEDE | generalized emergent dark-energy model | natural RLL sibling | medium |
| EDE | early dark energy before recombination | adjacent if RLL becomes early-time | high |
| coupled dark sector | energy exchange between dark energy and dark matter | relevant for growth/S8 | high |
| cosmic birefringence | CMB polarization rotation by parity-violating field | only relevant if photon coupling is defined | very high |
| cosmic dawn anomaly | early luminous galaxies/JWST | only relevant if high-z growth/age module exists | very high |
| BBN/lithium problem | primordial abundance mismatch | only relevant if RLL modifies early expansion | very high |

---

## 4. Mathematical core

### 4.1 Forward map

The forward validation map is:

```math
\theta \longrightarrow E(z) \longrightarrow \{H(z),D_M(z),D_H(z),D_V(z),\mu(z),f\sigma_8(z)\}\longrightarrow \chi^2,AIC,AICc,BIC
```

For RLL:

```math
\theta_{RLL}=(H_0,\Omega_m,\Omega_\Lambda,O_{s0},z_t,w_t,\Omega_bh^2,\sigma_8)
```

with a logistic transition:

```math
f(z;z_t,w_t)=\frac{1}{1+\exp((z-z_t)/w_t)}
```

and an effective superposition term of the form:

```math
S(z)=O_{s0}\left[f(z)+(1-f(z))(1+z)^3\right]
```

Thus, if:

```math
O_{s0}=0
```

then:

```math
S(z)=0
```

and the RLL layer becomes inactive in the background expansion. This is precisely the critical diagnostic of the current smoke run.

---

## 5. Inverse reconstruction

The inverse problem starts from data-constrained expansion and reconstructs an effective dark-energy sector.

```math
E^2(z)=H^2(z)/H_0^2
```

Assuming known radiation and matter contributions:

```math
\rho_{DE,eff}(z)\propto E^2(z)-\Omega_m(1+z)^3-\Omega_r(1+z)^4
```

The effective equation of state is:

```math
w_{eff}(z)=-1+\frac{1+z}{3}\frac{d\ln\rho_{DE,eff}(z)}{dz}
```

This implies the next key RLL diagnostic:

```text
compute w_eff_RLL(z)
compare against w_CPL(z)
compare against GEDE-like w(z)
```

The comparison must be functional, not only scalar by AIC/BIC.

---

## 6. Antiderivative layer

Cosmological distances are integral observables. Therefore small differences in `H(z)` may become visible through accumulated distance quantities.

```math
D_C(z)=c\int_0^z\frac{dz'}{H(z')}
```

A direct RLL/CPL antiderivative comparator is:

```math
\Delta D_C^{RLL-CPL}(z)=c\int_0^z\left[\frac{1}{H_{RLL}(z')}-\frac{1}{H_{CPL}(z')}\right]dz'
```

This should be computed together with:

```text
Delta D_M(z)
Delta D_H(z)
Delta D_V(z)
Delta mu(z)
```

because BAO and SN are primarily distance/integral tests.

---

## 7. Derivative layer

The deceleration parameter:

```math
q(z)=-1+\frac{1+z}{H(z)}\frac{dH}{dz}
```

The jerk/statefinder layer can also be used:

```math
j(z)=\frac{\dddot{a}}{aH^3}
```

RLL should be compared against LCDM/CPL/GEDE in:

```text
q(z)
j(z)
w_eff(z)
transition redshift of acceleration
curvature of H(z)
```

These derivative diagnostics can expose whether RLL is merely LCDM-like or possesses a distinct dynamical signature.

---

## 8. Logarithmic inversion of the RLL transition

The logistic form permits a logit transformation:

```math
f(z)=\frac{1}{1+e^{(z-z_t)/w_t}}
```

Therefore:

```math
\ln\left(\frac{1-f}{f}\right)=\frac{z-z_t}{w_t}
```

and:

```math
z=z_t+w_t\ln\left(\frac{1-f}{f}\right)
```

This motivates an overlooked diagnostic:

```text
reconstruct effective transition fraction f_eff(z)
plot logit(f_eff) versus z
check whether the relation is approximately linear
```

If the reconstructed effective transition is logit-linear, the RLL logistic ansatz gains structural support. If not, the current logistic form may be too rigid.

---

## 9. Parameter pathology and boundary audit

| Parameter | Current smoke signal | Interpretation | Required audit |
|---|---|---|---|
| `H0` | lower bound | possible prior/bound/r_d/CMB degeneracy | profile likelihood and bound expansion |
| `Omega_m` | high relative to Planck-like baseline | possible compensation among BAO/CMB/growth | ablation by dataset |
| `Omega_Lambda` | high/effective in LCDM/RLL smoke | closure interpretation required | flat/effective/curved policy audit |
| `Omega_b h^2` | upper bound in several models | likely r_d/BAO degeneracy | Planck prior and r_d ablation |
| `sigma8` | low relative to Planck-like baseline | growth proxy/backend limitation | CLASS/CAMB and S8 posterior |
| `w` | near -1 | wCDM adds little | compare against LCDM penalty |
| `w0` | boundary in CPL | CPL victory may be boundary-driven | expand bounds and robust seeds |
| `wa` | strong negative evolution | possible dynamical signal | posterior and dataset dependence |
| `Os0` | zero in RLL | RLL layer inactive | profile in Os0 and forced Os0>0 tests |
| `zt` | finite but inactive if Os0=0 | not physically interpretable yet | interpret only when Os0>0 |
| `wt` | finite but inactive if Os0=0 | not physically interpretable yet | interpret only when Os0>0 |

---

## 10. Effective degrees of freedom question

When `Os0=0`, parameters `zt` and `wt` are formally present but physically inactive. This raises a nontrivial statistical question:

```text
Should information criteria use nominal k or effective k when a parameter subspace becomes non-identifiable?
```

This is not a license to adjust metrics post hoc. It is a required identifiability study.

Required analysis:

```text
profile likelihood in Os0
Fisher/Hessian rank near Os0=0
posterior mass at the boundary
Bayesian evidence with priors
comparison of nominal k vs effective-k diagnostics as supplement only
```

---

## 11. Frontier anomaly coupling ledger

| Frontier topic | Coupling to RLL | Required formal object | Current state |
|---|---|---|---|
| DESI dynamical dark energy | direct background expansion | RLL vs CPL/GEDE likelihood | partial |
| thawing/emergent/mirage classes | conceptual and functional | w_eff class comparison | missing |
| GEDE | direct emergent sibling | GEDE baseline | TOKEN_VAZIO_GEDE_BASELINE |
| EDE/Hubble tension | early-universe coupling | r_s/r_d/CMB full analysis | TOKEN_VAZIO_EDE_COUPLING |
| coupled dark sector | growth/S8 coupling | modified growth equations | TOKEN_VAZIO_DARK_COUPLING |
| S8 tension | growth amplitude | CLASS/CAMB backend and weak-lensing data | TOKEN_VAZIO_BACKEND |
| cosmic birefringence | photon/parity coupling | EB/TB/beta prediction | TOKEN_VAZIO_BIREFRINGENCE |
| JWST cosmic dawn | high-z growth/age | halo/star-formation interface | TOKEN_VAZIO_COSMIC_DAWN |
| BBN/lithium | early expansion/nuclear rates | BBN compatibility | TOKEN_VAZIO_BBN_COMPATIBILITY |
| UDG/dark galaxies | halo formation | structure formation module | TOKEN_VAZIO_HALO_RESPONSE |

---

## 12. Viscosity of exploratory dynamics

Define model-response viscosity as resistance of a model's inferred structure to changes in dataset composition.

Parameter viscosity:

```math
\eta_{\theta_i}=\frac{|\Delta\theta_i|}{|\Delta D|}
```

Metric viscosity:

```math
\eta_{M}=\frac{|\Delta IC|}{|\Delta D|}
```

RLL-specific activation viscosity:

```math
\eta_{O_{s0}}=\frac{|\Delta O_{s0}|}{|\Delta D|}
```

Interpretation:

```text
Os0=0 in all seeds/datasets        => RLL remains viscosity-locked to LCDM-like limit
Os0>0 only in geometry-only fits    => RLL captures geometric tension but not full consistency
Os0>0 in robust multi-probe fits    => RLL becomes physically competitive
```

---

## 13. Required test hierarchy

### Stage 0 — CI and reproducibility

```text
pytest PASS
py_compile PASS
safe output-stem wrapper used
no canonical overwrite
```

### Stage 1 — Robust fit

```text
seeds = 1..10
maxiter >= 100
same data axes
same r_d policy
record all outputs
```

### Stage 2 — Boundary audit

```text
H0 boundary frequency
Ob_h2 boundary frequency
w0 boundary frequency
Os0=0 frequency
```

### Stage 3 — Ablation matrix

```text
Hz only
DESI+Hz
without CMB shift
without fsigma8
DESI+Hz+CMB
DESI+Hz+growth
SN/Pantheon+ when materialized
```

### Stage 4 — Functional comparison

```text
w_eff_RLL(z)
w_CPL(z)
w_GEDE(z)
q(z)
D_C(z)
Delta distance curves
```

### Stage 5 — Posterior inference

```text
MCMC or nested sampling
Bayesian evidence
credible intervals
posterior boundary mass
model comparison beyond AIC/BIC
```

### Stage 6 — Claim review

```text
claim_allowed remains false unless:
  robust fit passes
  RLL competitive against CPL/GEDE
  posterior supports active Os0
  data ablations remain stable
  external growth/CMB/SN gates are resolved
```

---

## 14. Academic interpretation matrix

| Outcome | Scientific meaning | Claim status |
|---|---|---|
| `Os0=0` always | current RLL redundant with LCDM in tested regime | no victory claim |
| `Os0>0` only in DESI+Hz | geometry-only transitional signal | exploratory claim only |
| RLL approximates CPL `w(z)` | compact/logistic representation of dynamical DE | candidate claim |
| RLL beats CPL in robust ICs | strong model-comparison signal | conditional claim |
| RLL beats CPL with posterior evidence | publishable competitive result | claim review |
| RLL requires coupling for growth | background model incomplete | open model extension |
| RLL fails all ablations | current parameterization disfavored | falsification of current form |

---

## 15. Professional claim language

Allowed:

```text
RLL is a candidate effective transition model under real-data evaluation.
RLL is currently not preferred in the canonical smoke run.
CPL/w0waCDM is the strongest immediate baseline.
The current RLL implementation collapses to an inactive Os0=0 boundary in the smoke run.
The next scientific step is robust seed/maxiter evaluation and functional reconstruction.
```

Blocked:

```text
RLL is confirmed.
RLL solves dark energy.
RLL resolves H0 or S8 tension.
RLL explains JWST cosmic dawn or cosmic birefringence.
RLL replaces LCDM/CPL.
```

---

## 16. References and frontier anchors

1. Planck Collaboration. *Planck 2018 results. VI. Cosmological parameters.* A&A / arXiv:1807.06209.
2. Pantheon+ Collaboration. *The Pantheon+ Analysis: Cosmological Constraints.* arXiv:2202.04077.
3. DESI Collaboration / Lodha et al. *DESI 2024: Constraints on Physics-Focused Aspects of Dark Energy using DESI DR1 BAO Data.* arXiv:2405.13588.
4. You, Wang & Yang. *Dynamical Dark Energy Implies a Coupled Dark Sector: Insights from DESI DR2 via a Data-Driven Approach.* arXiv:2504.00985.
5. Petri, Marra & von Marttens. *Dark Degeneracy in DESI DR2: Interacting or Evolving Dark Energy?* arXiv:2508.17955.
6. Capozziello et al. *Evidence for Dynamical Dark Energy using DESI DR2 Lyman-alpha Forest.* arXiv:2510.21976.
7. Poulin et al. *Impact of ACT DR6 and DESI DR2 for Early Dark Energy and the Hubble tension.* arXiv:2505.08051.
8. Riess et al. *JWST Observations Reject Unrecognized Crowding of Cepheid Photometry as an Explanation for the Hubble Tension at 8 sigma Confidence.* arXiv:2401.04773.
9. Sullivan et al. *Planck PR4 (NPIPE) map-space cosmic birefringence.* arXiv:2502.07654.
10. Ferrara. *The eventful life of GS-z14-0, the most distant galaxy at redshift z=14.32.* arXiv:2405.20370.

---

## 17. R3

```text
F_ok   = frontier dynamics/anomaly ledger created; RLL is formally positioned as a testable emergent/dynamical dark-energy candidate.
F_gap  = robust fit, GEDE baseline, w_eff reconstruction, posterior, Pantheon+/CMB/growth completion remain open.
F_next = implement scripts to compute w_eff_RLL(z), w_CPL(z), q(z), and dynamic-viscosity matrices from versioned robust-fit outputs.
```
