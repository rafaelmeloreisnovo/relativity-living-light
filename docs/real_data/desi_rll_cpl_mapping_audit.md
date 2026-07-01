# DESI DR2 / RLL CPL-mapping audit

Status: conservative compatibility downgrade for the RLL retrofeedback loop.

## Audit finding

DESI DR2 motivates testing dynamical-dark-energy likelihoods and favors a CPL region with `w0 > -1` and `wa < 0`. The current RLL logistic mapping around `a = 1`, however, gives `wa > 0` for positive transition width.

Therefore, any previous or future phrasing of “high compatibility” between the current RLL mapping and DESI DR2 must be downgraded to:

`QUALITATIVE_HYPOTHESIS / QUANTITATIVE_TEST_REQUIRED`

## Claim boundary

- DESI DR2 does not confirm RLL in the current repository state.
- The current RLL→CPL mapping is not yet quantitatively compatible without further model clarification.
- If RLL is bounded to `w ∈ [-1,0]`, it does not directly reproduce phantom-crossing claims such as Scherer+2025.
- DESI DR2 motivates joint-likelihood testing; it does not authorize a validation, confirmation, or superiority claim.

Preferred boundary statement:

> Current real-data evidence supports additional testing and pipeline hardening, not a scientific validation claim. Pantheon+ alone does not require the extra RLL sector; DESI DR2 motivates joint-likelihood testing, but the current RLL→CPL mapping is not yet quantitatively compatible without further model clarification.
