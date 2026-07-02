# Claim-Gated Architecture — Relativity Living Light

## Status

`formal_architecture / operational_governance / claim_boundary`

## Scope

This document defines the safe architecture for `instituto-Rafael/relativity-living-light`.

It is designed for onboarding, audit, CI coordination and repository maintenance.

## Claim boundary

Architecture is not scientific validation.

This document does not validate RLL, does not prove cosmology, does not declare superiority against LCDM/wCDM/CPL, and does not validate cross-repository integration.

## Executive view

The repository is organized as a falsifiable and auditable research program.

Core value:

```text
hypothesis -> data -> baseline -> metric -> uncertainty -> falsifier -> claim gate
```

## Logical structure

```text
/
├── README.md
├── ARCHITECTURE.md
├── .github/workflows/
├── data/
│   ├── real/
│   ├── real/cosmology/
│   ├── real_sources/
│   └── results/
├── docs/
│   ├── audits/
│   ├── architecture/
│   ├── real_data/
│   ├── epistemic_analogies/
│   ├── complementary_studies/
│   └── yml/
├── scripts/
├── src/rll/
├── tests/
├── tools/
├── results/
└── artifacts/
```

## Main layers

| Layer | Purpose | Gate |
|---|---|---|
| Documentation | explain state, method, architecture | claim boundary |
| Data | store committed real inputs and manifests | source/hash/schema |
| Scripts | compute, import, plan and emit artifacts | tests/watchdog |
| Tools | validate registries and docs | structural checks |
| Tests | preserve behavior | pytest |
| Workflows | run gates and upload artifacts | read-only permissions |
| Audits | review coherence and claims | evidence state |

## Data architecture

Real data flow:

```text
data/real/**
  -> scripts/compute_rll_real_pipeline.py
  -> artifacts/real-data-contract/
      -> MANIFEST.json
      -> COMPUTE_REPORT.md
      -> tables/*.csv
      -> TAGS.json
      -> WATCHDOG.json
      -> CHECKSUMS.sha256
```

Raw JSON flow:

```text
registry entry
  -> validate registry
  -> import raw JSON
  -> emit raw copy, manifest and checksum
  -> keep promotion blocked
```

## Operational registries

| Registry | Function |
|---|---|
| real source manifest | source and provenance control |
| variance registry | uncertainty and covariance policy |
| raw JSON registry | permitted imports and expected shape |
| cross-repo relationship registry | beta integration map with evidence states |

## CI architecture

Baseline workflow pattern:

```yaml
permissions:
  contents: read

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  validate:
    runs-on: ubuntu-latest
    timeout-minutes: 5
```

Workflow classes:

| Workflow class | Allowed claim |
|---|---|
| registry validation | registry is structurally valid |
| real-data contract | artifact contract executed |
| raw JSON import tests | importer preserves failsafe behavior |
| cross-repo registry check | relationships remain evidence-gated |
| robust-fit planning tests | planning is safe; fit was not necessarily run |

## Cross-repository integration

Relations with `ChipQuantum` and `termux-app-rafacodephi` must remain beta until verified in the owning repository.

Rule:

```text
relationship -> evidence state -> verification -> small fix -> test -> artifact -> claim gate
```

Do not use RLL documentation alone to change external repositories.

## Epistemic states

| State | Meaning |
|---|---|
| VERIFIED | evidence checked |
| VERIFIED_LIMITED | evidence checked with limited scope |
| DECLARED_BY_AUTHOR | declared but not independently proven |
| HYPOTHESIS | plausible but unverified |
| TOKEN_VAZIO | required evidence missing |
| CLAIM_BLOCKED | cannot be promoted |
| CONTRADICTION | evidence contradicts claim |

## RACI

| Area | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Repository architecture | technical maintainer | repo owner | auditor | contributors |
| Real data | pipeline maintainer | scientific owner | data reviewer | users |
| Claims | scientific author/reviewer | scientific owner | epistemic auditor | public |
| CI | workflow maintainer | repo owner | CI auditor | contributors |
| Registries | technical librarian | repo owner | auditor | contributors |
| Cross-repo | integrator | owners of involved repos | auditors | users |

## Quick start

```bash
python -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt pytest pyyaml
```

Useful checks:

```bash
python tools/docs_inventory.py --check
python tools/validate_real_cosmology_inputs_yml.py
python tools/validate_real_dataset_variance_registry.py
python tools/validate_cross_repo_relationship_registry.py
```

Focused tests:

```bash
python -m pytest -q tests/test_structure_d_robust_fit_matrix.py
python -m pytest -q tests/test_cross_repo_relationship_registry.py
```

## Roadmap

### Phase 1

```text
consolidate architecture
validate registries
reduce inflated language
preserve claim boundaries
```

### Phase 2

```text
verify one cross-repo relationship at a time
open issues only with evidence
strengthen covariance/error policy
run robust-fit only on explicit request
```

### Phase 3

```text
robust fit seeds 1..10
compare LCDM/wCDM/CPL/RLL
add covariance where available
use growth/fsigma8/lensing as discriminators
publish result with claim gate
```

## Success criteria

This architecture is successful if it:

```text
orients contributors
reduces path ambiguity
blocks inflated language
connects registries, CI and claims
preserves negative results
keeps scientific validation separate from operational validation
```
