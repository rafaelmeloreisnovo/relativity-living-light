# Real Data Source Registry

## Status

`SOURCE_REGISTERED / REAL_VALIDATED_BLOCKED`

## Purpose

This registry lists real public datasets that may be used for future RLL validation. It does not embed derived numerical results and does not validate scientific claims by itself.

## Operational rule

A source can move from `SOURCE_REGISTERED` to `INGESTED_VERIFIED` only after the repository records:

- public source URL or DOI;
- access date;
- downloaded artifact path;
- checksum or hash;
- ingestion command;
- schema validation;
- metric output;
- baseline or adversary;
- uncertainty or covariance policy when applicable;
- explicit claim boundary.

## Registered sources

| Source ID | Domain | Public source | Current state | Claim boundary |
|---|---|---|---|---|
| `DESI_DR1` | galaxy/quasar/star redshift survey | DESI DR1 public release / arXiv:2503.14745 | `SOURCE_REGISTERED` | Public source exists, but local artifact hash and ingestion output are required before validation. |
| `PANTHEON_PLUS_SH0ES` | Type Ia supernova distances | Pantheon+SH0ES public data release | `SOURCE_REGISTERED` | Source registration does not imply model fit or cosmological validation. |
| `PLANCK_2018_BASELINE` | CMB baseline cosmology | Planck 2018 legacy results / arXiv:1807.06205 | `SOURCE_REGISTERED` | Baseline parameters must be cited and version-pinned before use. |
| `COSMIC_CHRONOMETERS_HZ` | expansion history H(z) | cosmic chronometer literature and compilations | `SOURCE_REGISTERED` | Individual measurements require provenance, covariance policy and model-independence notes. |

## Non-promotion rule

`SOURCE_REGISTERED` is not `REAL_VALIDATED`.

The registry is an operational intake layer. It prevents real public sources from being mixed with mock, demo, placeholder or synthetic material.
