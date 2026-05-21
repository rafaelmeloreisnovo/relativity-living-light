# FALSIFIABILITY_PROTOCOL

This protocol defines explicit conditions under which Relativity Living Light (RLL) is weakened or rejected, without altering the project's scientific claims.

## 1) Scope
- Applies to claims presented as empirical/model-performance statements.
- Does not invalidate conceptual exploration by itself.

## 2) Pre-registered minimum conditions for a valid real-data claim
A real-data claim is valid only if all are satisfied:
1. Required real datasets are present and checksum-verified.
2. Commands and parameters are reproducibly specified.
3. Outputs include machine-readable metrics.
4. Comparison baseline (ΛCDM) is run on equivalent data and preprocessing.

## 3) Weakening conditions (claim must be downgraded)
Any of the following weakens strong model-preference claims to exploratory status:
- Missing or unverified required input files.
- Partial-real pipeline used as if full-real evidence.
- Non-reproducible command path or undocumented manual intervention.
- Metric reporting without uncertainty/context.

## 4) Rejection conditions (claim must be rejected)
Reject a specific empirical claim if any condition holds:
- Reproducible reruns fail to recover reported metrics within declared tolerance.
- Data leakage, target leakage, or post-hoc tuning invalidates comparison fairness.
- ΛCDM baseline is absent, incompatible, or measured under different protocol.
- Statistical evidence reverses the claimed direction (e.g., RLL no longer preferred under declared metric set).

## 5) Explicit prohibition
- Do **not** state that RLL outperforms/beats ΛCDM unless real-data metrics in this repository support that statement under reproducible conditions.

## 6) Recommended reporting template
- Claim category: conceptual / mathematical / synthetic / partial-real / real-validated.
- Dataset manifest + SHA256.
- Exact command(s).
- Metric table with uncertainty.
- Pass/fail against falsifiability criteria above.
