# Real-data references for `cosmology_observational_seed_2026.csv`

This file records only concrete source references used by the seed CSV. It does not assert RLL superiority and does not replace full dataset ingestion.

## Claim boundary

`No superiority claim unless real-data metrics pass predefined thresholds.`

## Observational H(z) seed rows

| source_id | reference | observed quantity | value used | status |
|---|---|---|---:|---|
| `cc_borghi_2021_lega_c` | arXiv:2110.04304 / DOI:10.48550/arXiv.2110.04304 | H(z=0.75) | 98.8 ± 33.6 km/s/Mpc | real observed seed |
| `cc_jiao_2022_lega_c_full_spectrum` | arXiv:2205.05701 / DOI:10.48550/arXiv.2205.05701 | H(z=0.80) | 113.1 km/s/Mpc with asymmetric uncertainty | real observed seed |
| `cc_tomasetti_2025_clusters` | arXiv:2512.02109 / DOI:10.48550/arXiv.2512.02109 | H(z=0.542) | 66.0 km/s/Mpc with broad asymmetric uncertainty | real observed seed / low-weight control |

## Source-summary rows

| source_id | reference | concrete fact used | status |
|---|---|---|---|
| `desi_dr2_bao_2025` | arXiv:2503.14738 / DOI:10.48550/arXiv.2503.14738 / Phys. Rev. D 112, 083515 (2025) | DESI DR2 BAO source summary; full BAO table and covariance still required before chi2 | source summary, not fit data |

## Explicit lacunae

- Pantheon+SH0ES files are not committed here because the runner expects the official external files under `data/pantheon/`.
- DESI DR2 BAO is not yet a chi2-ready dataset here because the measurement table and covariance/correlation matrix are not committed in this step.
- Planck 2018 is not treated as raw ingested data in this seed layer.

## Operational rule

If a value is not present in a cited source or in a committed file, it must remain absent. Do not fill with synthetic, guessed or statistically inferred values.
