# Structure D — AGN Feedback Bridge

Status: promoted from historical intake  
Claim: `claim_allowed=false`

## Hypothesis

AGN and quasar activity can heat gas, suppress star formation and alter late-time structure observables. In Structure D, this is represented as a phenomenological suppression route, not as a confirmed physical replacement for ΛCDM.

## Minimal phenomenological form

Let:

```text
rho_AGN(z) = effective AGN/quasar density proxy
E(z)       = injected energy proxy
S(z)       = suppression factor
```

A simplified windowed suppression can be written as:

```math
S(z) = 1 - \alpha\,g(z; z_{peak}, width)
```

where `alpha`, `z_peak` and `width` are fit/effective parameters.

## Observables needed

```text
f_sigma8(z)
S8 / weak lensing
quasar/AGN environment clustering
star formation history
BAO/H(z) background comparison
```

## Correct language

Use:

```text
RLL-like/AGN route is tested against ΛCDM and other baselines.
The metric improves or worsens after parameter penalty.
The claim remains blocked unless predefined gates pass.
```

Do not use:

```text
AGN feedback makes RLL win.
RLL proves new cosmology.
The model beats ΛCDM without AIC/BIC/baseline qualification.
```

## Operational locations

```text
data/pipelines/structure_d/feedback_agn.py
data/pipelines/structure_d/growth.py
data/pipelines/structure_d/models.py
results/structure_d/model_comparison.csv
results/structure_d/rll_regime_summary.csv
```

## Safe conclusion

AGN feedback is a legitimate astrophysical hypothesis to test through growth, lensing and clustering observables. It is not a claim of victory without data, uncertainty, baseline and metric gates.
