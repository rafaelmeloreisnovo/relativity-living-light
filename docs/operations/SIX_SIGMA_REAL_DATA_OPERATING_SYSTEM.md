# Six Sigma Real Data Operating System

## Status

`governance_record / operational_control_layer`

## Purpose

This document defines an operational excellence system for dynamic real-data execution in the repository. It uses a Six Sigma / DMAIC structure to organize what the repository can do with real data through GitHub Actions without inflating scientific claims.

The repository already has a canonical execution path for real data. This document adds a higher-level operating model: define, measure, analyze, improve and control.

## Golden boundary

Autonomous CI may collect, check, calculate, package and upload artifacts. It must not declare scientific superiority unless predefined real-data metrics, baselines and claim boundaries are satisfied.

## DMAIC model

### Define

Define what must be done and what must not be claimed.

Critical-to-quality items:

- public real source is declared;
- source license or usage note is known when available;
- access date is recorded;
- local artifact path is stable;
- checksum is recorded;
- ingestion command is deterministic;
- schema validation exists;
- metric output exists;
- baseline or adversary is defined;
- uncertainty or covariance policy is explicit when applicable;
- claim boundary blocks overstatement.

### Measure

Measure repository readiness before claiming validation.

Minimum measures:

- number of registered real sources;
- number of sources with local artifacts;
- number of sources with checksums;
- number of sources with ingestion command;
- number of sources with metric outputs;
- number of sources with baseline comparison;
- number of blocked claims;
- CI artifact completeness.

### Analyze

Analyze gaps without inventing data.

Allowed states:

| State | Meaning |
|---|---|
| `SOURCE_REGISTERED` | Public source is known, but local materialization is incomplete. |
| `INGESTION_READY` | Download and schema plan exist. |
| `INGESTED_VERIFIED` | Local artifact and checksum are present and schema checks pass. |
| `METRIC_READY` | Reproducible metric was computed. |
| `BASELINE_COMPARED` | Metric was compared to a declared baseline or adversary. |
| `REAL_VALIDATED_LIMITED` | A bounded claim is allowed. |
| `CLAIM_BLOCKED` | Evidence is missing or contradictory. |

### Improve

Improve by adding automation in small gates:

1. source registry validation;
2. source materialization with checksum;
3. schema validation;
4. metric computation;
5. baseline comparison;
6. artifact upload;
7. optional lightweight commit only when explicitly requested;
8. inventory regeneration when repository-tracked files change.

### Control

Control prevents regression.

Control rules:

- CI must preserve artifacts even when validation fails.
- Commit of calculated outputs must be explicit, not automatic by default.
- Mock, demo, example, placeholder and synthetic paths must not be promoted as real data.
- Generated results must live under `artifacts/` first.
- Lightweight committed outputs, when enabled, must live under `results/pipeline-runs/<run_id>/`.
- Any workflow with `contents: write` must justify write access and keep it opt-in.
- Every real-data run must include a manifest and checksum report.

## Repository operating structure

Recommended layers:

```text
data/real/                         source registries and real-data manifests
data/real/cosmology/               real cosmology inputs and source manifests
docs/real_data/                    real-data execution documentation
docs/operations/                   operational excellence and control plans
artifacts/real-data-complete/      transient CI artifacts
results/pipeline-runs/<run_id>/    optional lightweight committed run summaries
tools/                             validators and audits
.github/workflows/                 execution and control gates
```

## Dynamic CI pattern

The operational path is:

```text
source registry
-> materialization command
-> checksum
-> schema check
-> metric computation
-> baseline/adversary comparison
-> artifact upload
-> optional committed summary
-> inventory update when tracked outputs change
```

## Definition of done

A real-data automation is operationally excellent only when:

- it can be run manually through Actions;
- it can fail safely;
- it uploads enough evidence to debug failure;
- it never fabricates missing data;
- it records claim boundaries;
- it separates raw sources from derived outputs;
- it makes commit of calculated artifacts optional;
- it can be audited by a manifest validator.

## Scientific boundary

This system improves repository execution quality. It does not prove RLL, does not validate cosmology by itself, and does not authorize superiority language without the required real-data gates.
