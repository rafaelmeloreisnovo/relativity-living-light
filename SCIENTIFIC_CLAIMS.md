# SCIENTIFIC_CLAIMS

This document hardens claim boundaries for the repository and separates claim types without changing scientific assertions already present.

## 1) Conceptual claims
- RLL is presented as a conceptual framework combining geometric, informational, and phenomenological layers.
- The project organizes multi-domain intuition (language, geometry, entropy, cognition, cosmology) into a shared modeling vocabulary.
- Conceptual content is hypothesis-generating and is not, by itself, empirical evidence.

## 2) Mathematical claims
- Equations and symbolic systems in repository manuscripts define candidate dynamics and mappings (e.g., toroidal/state maps, iterative recurrences, entropy-like constructions).
- Mathematical consistency of notation does not imply empirical validity.
- Any theorem-level claim requires an explicit proof artifact and assumptions section.

## 3) Synthetic-data claims
- Synthetic pipelines can validate code-path behavior, parameter recovery in controlled settings, and regression stability.
- Synthetic agreement is interpreted only as internal consistency under generated assumptions.
- Synthetic outcomes must not be promoted as real-world superiority claims.

## 4) Partial-real claims
- Partial-real tests (e.g., subsets, proxy datasets, reduced likelihood flows) can indicate feasibility and ingestion correctness.
- Partial-real results are intermediate and cannot by themselves establish full cosmological model preference.

## 5) Real-validated claims
- Real-validated status requires full declared input datasets, provenance, reproducible commands, and reportable metrics.
- Claims about model preference versus ΛCDM require real-data metrics that are reproducible in this repository.
- **Policy**: do not claim “RLL beats ΛCDM” unless those metrics are present, current, and independently rerunnable.

## 6) Guardrails for publication and communication
- Always label outputs as conceptual, mathematical, synthetic, partial-real, or real-validated.
- Prefer conservative wording when evidence is incomplete.
- Keep historical/archive files intact, while routing core conclusions through reproducible real-data artifacts.


## 7) Threshold-based Pantheon interpretation boundary
- The `model_comparison.json` thresholds classify **model-comparison evidence only** (AIC/BIC/chi2 deltas under explicit guardrails).
- These thresholds do **not** establish a new cosmological model or a definitive replacement of ΛCDM.
- Any broader cosmological conclusion requires external validation across independent datasets and reproducible cross-checks.

## 8) Direct Model Attack / Falsifiability Checks
- For this repository, ΛCDM is the baseline comparator and default reference model for stress tests.
- RLL is only conditionally preferred when predefined Pantheon+ thresholds are passed under complete and valid metrics.
- Mixed, conflicting, invalid, or incomplete evidence is classified as inconclusive or LCDM-preferred.
- Passing Pantheon+ alone is insufficient to establish a cosmological replacement claim.
- External datasets are required for broader claims, including BAO, CMB, DESI, H(z), and independent supernova compilations.
