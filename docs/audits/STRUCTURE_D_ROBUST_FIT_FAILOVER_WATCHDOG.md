# Structure-D Robust Fit Failover Watchdog

## Status

`operational_excellence / dry_run_default / claim_boundary`

## Purpose

This audit note documents the operational guard added around Structure-D robust-fit matrix planning.

The guard coordinates versioned output stems for seed/maxiter runs while preserving the canonical smoke artifacts.

## Code path

```text
scripts/run_structure_d_robust_fit_matrix.py
```

## Default behavior

The runner defaults to dry-run planning.

```bash
python scripts/run_structure_d_robust_fit_matrix.py
```

It does not run robust fit unless explicitly called with:

```bash
--execute
```

## Safe output pattern

Planned stems follow:

```text
joint_real_likelihood_seed_<seed>_maxiter_<maxiter>
```

The canonical smoke stem remains blocked:

```text
joint_real_likelihood
```

## Existing-output policy

The runner supports three policies when planned artifacts already exist:

```text
fail   -> block the plan before execution
suffix -> allocate *_failover_<n> stems
skip   -> skip conflicting runs
```

## Watchdog fields

The emitted payload includes:

```text
watchdog.overall_status
watchdog.unique_output_stems
watchdog.canonical_stem_blocked
watchdog.existing_output_policy
watchdog.existing_output_conflicts
watchdog.failover_actions
```

## Rollback / failsafe

When `--plan-output` replaces an existing JSON plan, a `.bak` backup is preserved.

The likelihood outputs continue to rely on the atomic-write behavior already implemented in the Structure-D likelihood module.

## Tests

```text
tests/test_structure_d_robust_fit_matrix.py
```

The tests cover safe stems, duplicate blocking, canonical stem blocking, existing-output fail/suffix/skip policies, watchdog fields and rollback backup behavior.

## Claim boundary

This is operational infrastructure only.

It does not run robust fit by default, does not validate RLL, does not compare model superiority, does not alter scientific results and does not promote any cosmological claim.
