# Structure D — Canonical Science Index

Status: canonical documentation layer  
Claim: `claim_allowed=false`

## Purpose

This directory is the canonical documentation home for material promoted from the historical `to_Add/RAFAELIA_COSMO_STRUCTURE_D/` intake bundle.

The operational implementation is not here. It lives in:

```text
data/pipelines/structure_d/   # Python implementation
data/inputs/structure_d/      # inputs and configs
results/structure_d/          # outputs
```

Compatibility wrappers may remain in `RAFAELIA_COSMO_STRUCTURE_D/`, but no new logic should be added there.

## Promoted documents

```text
docs/science/structure_d/EQUATIONS.md
docs/science/structure_d/AGN_FEEDBACK_BRIDGE.md
docs/science/structure_d/EVIDENCE_TRACEABILITY.md
```

## Claim boundary

```text
[OK] Structure D is an executable route for model comparison and traceability.
[OK] AGN feedback is represented as a phenomenological hypothesis.
[BLOQUEADO] This route does not prove RLL superiority.
[BLOQUEADO] Terms such as 'wins against LCDM' must be replaced by AIC/BIC/chi2 gate language.
```

## Official commands

```bash
python -m data.pipelines.structure_d.make_example_data
python -m data.pipelines.structure_d.run_all
```

For real validation:

```bash
python -m data.pipelines.structure_d.run_all --profile structure_d_real_validation
```

## Safe conclusion

Structure D is now organized as an operational pipeline plus canonical science documentation. Historical intake files remain reference-only and must not be used as the active source of truth.
