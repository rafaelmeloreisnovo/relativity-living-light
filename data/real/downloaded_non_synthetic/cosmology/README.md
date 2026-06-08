# Downloaded Non-Synthetic Cosmology Data

This directory stores lightweight real-data material downloaded by `scripts/fetch_real_sources.py` and committed as an explicit non-synthetic input option for CI/manual validation.

It is not a production replacement for bulk DESI/Planck portals; heavy products remain portal-selected and manifest-driven.

## Files

- `desi_dr2_results_i_arxiv.html` — 84766 bytes, sha256 `3eb18773acd00ea7a77f68efd79f1964ec2392ce78121c2aef63989135914c3f`
- `download_manifest.json` — 1059 bytes, sha256 `0529f22d74b24a0b6fca2c680260944bf2b3344a6a135a1baafec9d9987d7268`
- `pantheon_plus_sh0es_readme.md` — 148 bytes, sha256 `aebbe5d60292a548f008173b122073622f1f1c113af65ee988d29c53f51aa677`


## Attribution and redistribution boundary

- `desi_dr2_results_i_arxiv.html` is a lightweight cached copy of the public arXiv abstract page `https://arxiv.org/abs/2503.14738`, retained only for reproducible source-signature validation and citation traceability. Treat the paper text, metadata, and arXiv page assets as third-party material; do not modify authorship, DOI/arXiv identifiers, or license notices.
- `pantheon_plus_sh0es_readme.md` is sourced from `https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/main/README.md`; keep upstream attribution and use the upstream repository for authoritative bulk data.
- If a source license, robots policy, or upstream redistribution term changes, replace the committed cache with manifest-only references or CI artifacts rather than silently promoting stale copies.

## Contract

- Use workflow input `real_data_source=materialized` to require freshly materialized workflow data.
- Use `real_data_source=repo` to force committed real inputs under `data/real`.
- Use `real_data_source=auto` to prefer materialized inputs and fall back only to committed real inputs.
- Synthetic/mock/example files must not be promoted through this directory.
