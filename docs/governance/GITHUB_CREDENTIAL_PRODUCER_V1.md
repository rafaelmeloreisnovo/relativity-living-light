# RLL — Producer Credential Boundary V1 (2026-10-25)

**CANDIDATE_HOLD**. Relativity Living Light is a producer of source/scientific artifacts, not the owner of all cross-repository administrative credentials.

Architectural route: `RLL producer → RafGitTools bounded executor → Mapa typed registry → source-specific evidence`.

- Do not copy `PAT_ACTIONS`, `PAT_ENV`, `RAFAELIA_ADMIN_TOKEN`, app private keys or an unlimited admin PAT into RLL workflows.
- Built-in `GITHUB_TOKEN` read-only by default for normal CI; any extra permission requires an individual job's justification.
- Cross-repo requests use an explicitly allowlisted, short-lived GitHub App installation token under RafGitTools control, with destination repo/operation/exact HEAD pinned; **no global admin PAT**.
- In the sampled `START_MANUAL_HERE.yml` and `rll-governance-quality-gate.yml`, no `secrets.<PAT_NAME>` binding was observed. This is **not** an exhaustive scan of RLL workflows nor proof no secret exists.
- Admin GitHub settings changes remain with a protected manual owner route, never with scientific output/regular PR runners. Reject token passing to PRs from forks or unchecked inputs.

Next: audited metadata-only read of RLL Actions/Environment secrets in GitHub provider settings; verify effective permissions without revealing values; run negative tests before any active workflow modification. `claim_allowed=false`; no training, merge or public token distribution.

Machine pointer: `data/governance/github_credential_producer_v1.json`. Rollback: draft PR, append-only receipts; no workflow changed.
