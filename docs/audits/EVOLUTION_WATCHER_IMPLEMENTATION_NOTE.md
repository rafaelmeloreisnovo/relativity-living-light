# Evolution Watcher — Implementation Note

Status: `partially_implemented / claim_bounded`

## What this adds

The repository already specified an "RLL JSON Evolution Watcher" system
(`schemas/EVOLUTION_ROADMAP.md`, `schemas/evolution_event.schema.json`) but
had no working code for it. This change implements the local, network-free
core (Phases 0 and 1 of the roadmap) and registers the real cosmology data
sources already committed under `data/real/`.

```text
RLL_JSON_EVOLUTION_WATCHER.yml   -> central source registry
tools/bootstrap_failsafe.py      -> Phase 0: one-time per-source snapshot
tools/rll_json_watcher.py        -> Phase 1: fingerprint check + trail + rollback
tests/test_bootstrap_failsafe.py
tests/test_rll_json_watcher.py
tests/test_evolution_watcher_config.py
```

## Registered sources

`hz_cosmic_chronometers`, `desi_dr2_bao`, `pantheon_plus_shoes`,
`planck_2018_cmb`, `fsigma8_growth` — the same real-data inputs consumed by
`data.pipelines.structure_d.joint_real_likelihood`.

## How it works

- **Never fetches from the network and never overwrites a committed
  real-data file.** The git-tracked file under `data/real/` is always the
  source of truth; this tool only tracks its *history* (sha256 fingerprint,
  epistemic state, drift) over time.
- `bootstrap_failsafe.py` computes a fingerprint per source, writes a
  failsafe snapshot to `data/failsafe/<id>_FROZEN.json` and a fingerprint
  file to `schemas/fingerprints/<id>.sha256`, and appends a `BOOTSTRAP` event
  to `artifacts/EVOLUTION_TRAIL.jsonl`.
- `rll_json_watcher.py` re-fingerprints each source on every run and records
  `SKIP_EXISTING` (unchanged), `UPDATE` (`schema_drift=true`), or `FAILSAFE`
  (registered file missing). `--rollback` restores a source's tracked state
  from its failsafe snapshot; per the event schema's own rule, a rollback
  never re-promotes a source to `VERIFIED` — it downgrades to
  `DECLARED_BY_AUTHOR` so a human re-verifies it.
- Every event is validated against `schemas/evolution_event.schema.json`
  (via `jsonschema`) before being written.

## Run it

```bash
python tools/bootstrap_failsafe.py --config RLL_JSON_EVOLUTION_WATCHER.yml
python tools/rll_json_watcher.py --config RLL_JSON_EVOLUTION_WATCHER.yml --emit-summary
python tools/rll_json_watcher.py --config RLL_JSON_EVOLUTION_WATCHER.yml --source planck_2018_cmb --rollback
```

## What is intentionally not included in this change

- **CI/CD (roadmap Phase 2).** The staged workflow in
  `to_Add/data_evolution_watch.yml` auto-commits snapshots on a cron/push
  trigger using `permissions: contents: write`. A separate, unrelated change
  in this repository (`tools/audit_github_workflows.py`'s
  `audit_real_workflow_policy`) now requires any workflow that looks like a
  "real data" workflow to declare `permissions.contents: read` and avoid
  auto-commit, funneling real-data automation through one canonical
  read-only, artifact-uploading workflow instead. Promoting the staged
  workflow as-is would fail that gate and would conflict with the direction
  other concurrent work is already taking this area of the repo. Wiring the
  watcher into CI is left for a follow-up that adapts it to the canonical
  policy (dry-run/check mode, `actions/upload-artifact`, no push-back).
- **Orphan promotion (roadmap Phase 4)** — unrelated to real-data source
  tracking; not implemented here.

## Claim boundary

This is structural provenance infrastructure. Bootstrapping or watching a
source only means its local file is present, fingerprinted, and its history
is now traceable. It does not validate RLL, does not run any cosmological
fit, and does not confirm any scientific claim. Epistemic states
(`VERIFIED`, `DECLARED_BY_AUTHOR`, `TOKEN_VAZIO`, `CONTRADICTION`) describe
data-provenance tracking, not scientific truth.
