# Public Astronomy Catalog Fetcher

Status: `source_fetcher / exploratory_astronomy / not_cosmology_validation`

## Purpose

`scripts/fetch_public_astronomy_catalog_samples.py` fetches small public astronomy catalog samples and writes explicit provenance metadata.

It is useful for exploratory astronomy, pipeline testing, schema normalization, and public-catalog demonstrations.

It is **not** a cosmology likelihood and must not be used as evidence that RLL, dark matter, dark energy, ΛCDM alternatives, or CMB claims are validated.

## Default outputs

```text
scripts/fetch_public_astronomy_catalog_samples.py
```

Default command:

```bash
python scripts/fetch_public_astronomy_catalog_samples.py --sdss-limit 200 --osc-limit 200
```

Expected outputs when network fetches succeed:

```text
data/real/astronomy/sdss_galaxy_sample.json
data/real/astronomy/open_supernova_catalog_sample.json
data/provenance/public_astronomy_catalog_fetch_manifest.json
```

## Source classes

| Output | State | Meaning | Claim boundary |
|---|---|---|---|
| `sdss_galaxy_sample.json` | `REAL_CATALOG_SAMPLE` | SDSS DR16 catalog rows from a bounded SQL query | catalog sample only; not dark-matter/dark-energy validation |
| `open_supernova_catalog_sample.json` | `REAL_AGGREGATED_CATALOG` | Open Supernova Catalog object metadata | not Pantheon+, DES, Union, SH0ES, or cosmology likelihood |
| `cmb_power_spectrum_template.json` | `SYNTHETIC_TEMPLATE` | illustrative CMB-like template if explicitly requested | written only under `data/examples`, never `data/real` |
| `cmb_local_input.*` | `USER_SUPPLIED_LOCAL_FILE_NOT_VERIFIED_BY_THIS_TOOL` | optional local CMB file copied with provenance warning | not verified Planck likelihood/covariance/official release |

## CMB rule

Generated CMB points are never real data.

The script may write an illustrative template only if requested explicitly:

```bash
python scripts/fetch_public_astronomy_catalog_samples.py --skip-sdss --skip-osc --include-cmb-template
```

That template must be written under:

```text
data/examples/cmb_power_spectrum_template.json
```

It must not be written under:

```text
data/real/**
```

A real CMB analysis requires a declared official source, version, data vector, covariance/likelihood semantics, masks, nuisance treatment, and reproducible command path. This fetcher does not provide those requirements.

## Removed/blocked heuristics

The fetcher does **not** create real measurements for:

- stellar mass inferred from a rough magnitude rule;
- morphology inferred from magnitude threshold;
- dark matter evidence;
- dark energy evidence;
- CMB likelihood reproduction.

If any derived heuristics are added later, they must be explicitly marked as:

```text
DERIVED_HEURISTIC / NOT_VALIDATION_INPUT
```

## Blocked claims

The following claims are blocked by design:

```text
RLL is validated.
Dark matter is measured by this script.
Dark energy is confirmed by this script.
CMB likelihood is reproduced.
SDSS/OSC samples validate cosmology.
```

## Allowed statement

The safe statement is:

> Public astronomy catalog samples were fetched and normalized with provenance metadata.

## Validator

Run:

```bash
python tools/validate_public_astronomy_catalog_fetcher.py
```

The validator checks that:

1. the fetcher exists;
2. generated CMB templates are directed to `data/examples`, not `data/real`;
3. blocked validation claims are present as blocked claims rather than promoted claims;
4. documentation preserves the `not_cosmology_validation` boundary.

## Scientific status

`CLAIM_BLOCKED`

This fetcher increases public-data handling capacity. It does not change the current scientific conclusion of the repository.
