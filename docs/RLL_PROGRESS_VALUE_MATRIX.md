# RLL progress and value matrix

Status date: 2026-06-23

## Epistemic rule

This document separates implemented engineering from potential value. It does not claim RLL is physically confirmed.

## Current stack

| Layer | Status | Evidence path | Value now | Gate |
|---|---|---|---|---|
| Background RLL | implemented | `src/rll/class_rll_background.c` | technical foundation | compare against CLASS/CAMB background |
| f sigma 8 real data | implemented | `data/real/cosmology/fsigma8_growth.csv` | falsification gate | covariance/MCMC |
| Growth chi2 | implemented | `scripts/check_rll_growth.py` | model screening | full covariance |
| Linear perturbation kernel | implemented | `src/rll/rll_perturbation_kernel.py` | first perturbation layer | scale-dependent perturbations |
| Transfer bridge | contract | `src/rll/rll_transfer_bridge_contract.json` | integration surface | native transfer table |
| CLASS/CAMB handoff | contract | `src/rll/class_transfer_adapter_contract.json` | backend integration plan | actual backend patch |
| CMB Cl exact | TOKEN_VAZIO | none | no claim | Boltzmann hierarchy |
| Nonlinear P(k) exact | TOKEN_VAZIO | none | no claim | Halofit/HMcode/native nonlinear layer |

## Academic value

| Vertent | Value | Strength | Risk |
|---|---|---|---|
| Reproducible pipeline | high | scripts + docs + tests | needs CI status |
| Alternative cosmology hypothesis | medium | falsifiable against LCDM/w0wa/CPL | current evidence not decisive |
| Pedagogical symbolic framework | medium | maps metaphors to test gates | not proof by itself |
| Computational cosmology bridge | high potential | background + perturbation + handoff | must integrate backend |
| Publication readiness | candidate | methods and provenance improving | needs full likelihood and reviewer language |

## Market/application value

| Market route | Potential | Why | Monetization gate |
|---|---|---|---|
| Scientific software | niche high | cosmology codes are used for parameter estimation | validated backend + citation package |
| HPC/AI for science | medium/high | workflow can become benchmark/falsification suite | scalable runs + reproducibility |
| Space/sensing analytics | speculative | cosmology/inference methods can transfer to signal pipelines | domain-specific dataset and customers |
| Education/research tooling | medium | clear TOKEN_VAZIO methodology and audit trail | course/notebook/product packaging |
| IP/consulting | low/medium now | implementation and documentation are assets | proof of performance and users |

## Valuation bands

These are not company valuations. They are maturity bands:

| Stage | Description | Market value class |
|---|---|---|
| Research artifact | code + docs + falsification gates | low direct value, high learning value |
| Validated scientific package | tests + CI + benchmark vs CLASS/CAMB | academic/citation value |
| Adopted tool | external users + docs + releases | niche software value |
| Commercial service | paying users or contracts | market value measurable |
| Defensible IP/product | unique validated method + demand | strategic value |

## Current honest score

| Axis | Score | Notes |
|---|---:|---|
| Engineering completeness | 55/100 | background, growth, kernel, contracts done |
| Scientific validation | 35/100 | real f sigma 8 started, CMB not done |
| Academic defensibility | 45/100 | good falsifiability language, needs backend/MCMC |
| Market readiness | 20/100 | no users/revenue yet |
| IP/provenance | 60/100 | GitHub commits and explicit gates |
| Claim safety | 80/100 | TOKEN_VAZIO boundaries are strong |

## Next gates

1. Native transfer table generation.
2. CLASS/CAMB backend patch.
3. CMB Cl comparison.
4. Nonlinear P(k) via Halofit/HMcode or validated native layer.
5. MCMC with covariance and model selection.
6. Release tag and ASCL/Zenodo style citation package.
