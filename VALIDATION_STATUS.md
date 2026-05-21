# VALIDATION STATUS — Relativity Living Light (RLL)

Date (UTC): 2026-05-21

## What runs

- **Unit/integration tests**: `pytest -q` runs successfully after compatibility fix for NumPy 2.x (`48 passed`).
- **CLI synthetic flow**: `rll run --data synthetic --model rll` runs end-to-end and writes artifacts in `results/structure_d/`.
- **Editable install (offline-compatible)**: `pip install -e . --no-build-isolation` works in restricted-network environments.

## What fails

- **Default editable install command in docs**: `pip install -e .` can fail in restricted environments because build isolation tries to fetch `setuptools>=68` from network.
- **CLI real+bayes example**: `rll run --data real --model rll --with-bayes --with-covariance` fails if Pantheon+ files are absent (`data/pantheon/lcparam_full_long_zhel.txt`).
- **CLI real (non-bayes) runtime in this environment**: command starts but did not produce observable terminal output before session timeout; treat as **not validated end-to-end here**.

## What is synthetic

- `--data synthetic` pipeline (`data/pipelines/structure_d/run_all.py`) uses synthetic/default profile and produces comparative metrics (RLL-like vs LCDM-like) without mandatory external survey ingestion.

## What is real

- `docs/panteon_likelihood.py` is intended for **real Pantheon+** validation and requires external files under `data/pantheon/`.
- `docs/rll_validation_real.py` is intended for **real-data validation** workflows; execution completeness depends on local dataset/materialization conditions.

## What still needs external validation

1. Full Pantheon+ ingestion and successful run with documented data provenance/hash.
2. Reproducible real-data runs for all declared cosmology blocks (Pantheon+, BAO/H(z), and any CMB shift usage) with versioned artifacts.
3. Public, auditable dataset-fetch recipe that does not depend on manual placement only.
4. Cross-machine reproducibility report (same inputs, same outputs within tolerance).

## Reproducibility improvements included in this patch

- Fixed CLI orchestration for synthetic flow by executing `data/pipelines/structure_d/run_all.py` as a module context, preventing relative-import crashes.
- Added safe module execution argument isolation so `rll` CLI arguments do not leak into downstream module parsers.
- Replaced removed NumPy API `np.trapz` with `np.trapezoid` for NumPy 2.x compatibility.

## Main cosmological model equations (as implemented/documented)

- Expansion law (RLL effective form):
  \[
  E^2(a)=\Omega_r a^{-4}+\Omega_m a^{-3}+\Omega_\Lambda
  +\Omega_{s0}[f(a)+(1-f)a^{-3}]
  +\Omega_{B0}a^{-4}+\Omega_{P0}a^{-4}
  \]
- Transition function:
  \[
  f(z)=\frac{1}{1+\exp((z-z_t)/w_t)}
  \]

(Equation wording is documented in README and operationally mirrored by RLL-vs-ΛCDM scripts/pipelines.)
