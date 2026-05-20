# Runaway SMBH as Robustness Stress-Test Index (RLL)

## Role in framework
Runaway supermassive black-hole systems are treated as **extreme-astrophysics stress tests**, not direct probes of dark-energy acceleration.

## Proposed robustness term
\[
\mathcal{R}_{anom}=\sum_i w_i\left|\frac{O_i-M_i}{\sigma_i}\right|,
\]
with example feature set:
\[
\mathcal{A}_{BH}=\{v_{BH}, M_{BH}, L_{wake}, z, \dot{M}_\star, \text{line ratios}\}.
\]

## Integration policy
- Keep anomaly penalties separate from primary expansion likelihood.
- Use as secondary model-risk control against overfitting.
- Report weights and normalizations explicitly.

## Bibliography
See `jwst_runaway_smbh` in [`data/observational_sources.yml`](../data/observational_sources.yml).
