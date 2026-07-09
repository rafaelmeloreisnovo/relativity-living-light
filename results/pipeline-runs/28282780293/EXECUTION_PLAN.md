# Real Data Complete Execution

- execution_mode: full
- materialize_pantheon: true
- run_structure_d: true
- run_pantheon_validation: true
- strict_real_data: true
- commit_light_artifacts: true
- claim_boundary: No superiority claim unless real-data metrics pass predefined thresholds.

## Failsafe / failover / rollback
- Never promote mock/synthetic/example/placeholder files as real data.
- Download only from documented public primary sources.
- Write new run artifacts under artifacts/real-data-complete first.
- Commit only lightweight reports when explicitly requested.
- If a required real input is missing and strict mode is true, fail the workflow instead of fabricating data.
