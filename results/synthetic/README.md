# Synthetic results

Outputs produced from synthetic, mock, demo, example, or fixture inputs belong here and must carry `dataset_type` plus `claim_allowed: false` when serialized as JSON.

Synthetic results are allowed for:

- code regression checks;
- diagnostic plots;
- failover/rollback tests;
- numerical sanity checks.

Synthetic results are not allowed for scientific model-comparison claims. Legacy mock figures or catalogs outside this directory must be listed in `data/synthetic/LEGACY_SYNTHETIC_MANIFEST.json` until they can be migrated safely with compatibility aliases.
