# RAFAELIA AI repository bridge

Status date: 2026-06-23

## Repository roles

| Repository | Role |
|---|---|
| `rafaelmeloreisnovo/Rafaelia_Private` | private corpus, symbolic invariants, Ethica, BitStack and ZIPRAF base |
| `rafaelmeloreisnovo/GAIA_phi` | deterministic core, hashing, vecdb, manifests, guard and C/Python engines |
| `rafaelmeloreisnovo/llamaRafaelia` | local inference/runtime layer in C/C++ |
| `instituto-Rafael/relativity-living-light` | scientific validation, real data, loaders, CI and claim gates |

## Stack reading

```text
Private corpus -> deterministic core -> local inference -> scientific validation
```

## Formula bridge

The formulas upload is represented by:

```text
data/formulas/FORMULAS_ARTIFACTS_MANIFEST.json
scripts/validate_formulas_manifest.py
.github/workflows/formulas-artifacts-validation.yml
```

The current manifest records 486 formulas, 53 sources and three categories: `geral`, `cosmology_metrics`, `integridade_e_criptografia`.

## Operational rule

```text
formula -> category -> source -> gate -> loader/test/result -> claim or TOKEN_VAZIO
```

## Next integrations

1. Import full `formulas.json` when safe.
2. Generate stable formula IDs.
3. Map formula IDs to claim gates.
4. Link cosmology formulas to RLL loaders.
5. Link guard formulas to GAIA_phi and Rafaelia_Private.
6. Link local runtime prompts to llamaRafaelia.
