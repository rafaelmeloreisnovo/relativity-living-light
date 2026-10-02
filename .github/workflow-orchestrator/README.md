# Workflow Orchestrator Catalog

This directory defines the bounded set of workflows that the RLL session dispatcher may launch.

- `session.yml` is the only session entry point. It declares seven profiles and loads explicit manifest directories.
- `workflows/` contains the allowlisted manifests. The canonical session does not set `workflow_files` and does not discover every root workflow.
- `tools/workflow_orchestrator.py` dispatches selected manifests by stage and waits for each run before continuing.

## Capacity and profile routing

| Profile | Scope | Configured maximum |
|---|---|---:|
| `quick_session` | YAML syntax gate | 20 min |
| `real_data_session` | manual preflight + controlled real-data workflows | 165 min |
| `science_session` | formula, IML, academic package and research preview | 75 min |
| `literature_session` | academic package, optional one-paper arXiv intake and Jekyll preview | 15 min |
| `pages_preview_session` | same source graph rendered as a Jekyll preview artifact | 15 min |
| `frontier_session` | isolated frontier workflow | 190 min |
| `full_session` | all allowlisted bounded workflows except frontier | 260 min |

The session remains sequential with a stage barrier and `max_in_flight: 1`. A focused profile avoids waiting for unrelated categories. The parent job timeout is 320 minutes: 60 minutes above the largest configured profile budget and below GitHub Actions' documented 360-minute job limit.

## Research and publication boundary

The academic workflow validates the existing relation package, can fetch one arXiv metadata record when given an ID, preserves the raw Atom response and its SHA-256, and builds a Jekyll preview. Optional relation targets and their note are caller-declared candidate edges. They remain `RELATIONAL_PENDING` and `claim_allowed: false`.

The preview is uploaded as a workflow artifact only. This route does not enable Pages deployment, poll arXiv, infer scientific relations, merge researcher identities by name, or send messages to researchers. The raw API response, generated candidate, build revision, run ID and input-file digests are kept in the receipt artifacts.

## Schema evolution

- `rll.workflow_orchestrator.catalog.v1`: historical monolithic catalog.
- `rll.workflow_orchestrator.catalog.v2`: `session.yml` plus explicitly loaded manifest directories.

Operational manifests describe execution. Validated knowledge stays in a domain registry or result artifact with source, checksum, method, metric, baseline and epistemic state.
