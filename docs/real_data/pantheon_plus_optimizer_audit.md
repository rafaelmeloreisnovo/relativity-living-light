# Pantheon+ optimizer/likelihood audit

Status: conservative audit note for reproducible real-data hardening.

## Boundary of the finding

The previous catastrophic RLL result in the Pantheon+ path is treated as likely optimizer/likelihood fragility, not as a physical conclusion. In particular, a numerical result that can be explained by false convergence, likelihood-semantics drift, covariance misuse, or calibrator handling mismatch is not evidence for or against a cosmological sector.

## Corrected interpretation

- Corrected Pantheon+ alone does not support requiring the extra RLL term.
- For this dataset, the fitted RLL extra sector collapses toward the ΛCDM limit rather than demonstrating a distinct preferred sector.
- No superiority claim is allowed: the repository must not state that RLL is validated, that RLL beats ΛCDM, or that Pantheon+ confirms RLL.
- Current real-data evidence supports additional testing and pipeline hardening, not a scientific validation claim.

## Implementation cross-check required

The Pantheon+ implementation should be cross-checked against official Pantheon+/CosmoSIS likelihood semantics before any scientific interpretation. The cross-check must include, at minimum:

1. covariance construction and ordering;
2. treatment of statistical plus systematic covariance;
3. calibrator/SN-anchor handling;
4. nuisance-parameter conventions;
5. data-vector column semantics and redshift conventions.

Until that cross-check is complete, Pantheon+ outputs in this repository are engineering audit artifacts, not validation claims.
