# RLL Next Work Documentation Plan

Status: operational documentation plan.

Purpose: define the next documentation work after the `v1.0.0` ancestry audit, with strict separation between verified evidence, author declarations, and TOKEN_VAZIO.

## 1. Why this document exists

The `v1.0.0` tag demonstrates that the RLL base formulation existed publicly in September 2025.

Current 2026 work demonstrates later maturation:

- DESI linkage;
- BAO materialization;
- covariance handling;
- LCDM/wCDM/CPL/RLL comparison;
- AIC/AICc/BIC;
- claim boundary;
- joint-real likelihood.

The next work is to connect these two poles:

```text
2025 tag / formula / observables
→ early artifacts, figures, CSVs and possible mobile execution
→ 2026 real-data validation and model selection
```

## 2. Work packages

### WP1 — Tag snapshot inventory

Goal: audit the full `v1.0.0` tag snapshot.

Tasks:

1. List all files present in `v1.0.0`.
2. Classify each file:
   - formula;
   - image;
   - CSV/data;
   - script;
   - text/manifest;
   - generated output;
   - TOKEN_VAZIO.
3. Record path, size and hash when available.
4. Identify any files linked or implied by README but absent from the tag.

Deliverable:

```text
docs/RLL_V1_TAG_FILE_INVENTORY.md
```

### WP2 — Formula ancestry ledger

Goal: map the origin of each RLL mathematical component.

Components:

| Component | Target evidence |
|---|---|
| `Ω_s0` | first file/commit where present |
| `f(a)` | first file/commit where present |
| DE→matter superposition block | first file/commit where present |
| magnetic term `Ω_B0 a^-4` | first file/commit where present |
| plasma term `Ω_P0 a^-4` | first file/commit where present |
| `w_eff` | first file/commit where present |
| `fσ8` | first file/commit where present |
| rotation/lensing demos | first file/commit where present |

Deliverable:

```text
docs/RLL_FORMULA_ANCESTRY_LEDGER.md
```

### WP3 — Mobile / Termux provenance

Goal: verify or bound the claim that early calculations were executed on Rafael's own cellphone through a Termux-like environment.

Tasks:

1. Locate shell scripts, logs or generated output paths.
2. Search for mobile/Android/Termux indicators.
3. Link commands to outputs.
4. Hash outputs.
5. Mark everything as VERIFIED / DECLARED_BY_AUTHOR / TOKEN_VAZIO.

Deliverable:

```text
docs/RLL_MOBILE_TERMUX_PROVENANCE_REPORT.md
```

### WP4 — Image and CSV artifact provenance

Goal: connect README-listed figures/CSVs to actual files.

Target artifacts from `v1.0.0` README:

- H(z) ratio;
- Δμ residuals;
- energy fractions;
- `f(z)` and `w_eff(z)`;
- entropy-margin H ratio;
- entropy-margin Δμ;
- structure growth `fσ8(z)`;
- rotation curve demo;
- cluster lensing demo;
- CSVs for models, entropy, growth and curves.

Deliverable:

```text
docs/RLL_V1_IMAGE_CSV_PROVENANCE.md
```

### WP5 — Data-station map

Goal: formalize the author's "data stations" language into audit nodes.

Definition:

A data station is an execution/observation node linking:

```text
formula → input → script → output → figure/table → interpretation → claim gate
```

Deliverable:

```text
docs/RLL_DATA_STATIONS_MAP.md
```

Suggested station table:

| Station | Formula | Input | Script | Output | Claim status |
|---|---|---|---|---|---|
| H(z) | TOKEN_VAZIO | TOKEN_VAZIO | TOKEN_VAZIO | TOKEN_VAZIO | pending |
| Δμ | TOKEN_VAZIO | TOKEN_VAZIO | TOKEN_VAZIO | TOKEN_VAZIO | pending |
| energy fractions | TOKEN_VAZIO | TOKEN_VAZIO | TOKEN_VAZIO | TOKEN_VAZIO | pending |
| w_eff | TOKEN_VAZIO | TOKEN_VAZIO | TOKEN_VAZIO | TOKEN_VAZIO | pending |
| fσ8 | TOKEN_VAZIO | TOKEN_VAZIO | TOKEN_VAZIO | TOKEN_VAZIO | pending |
| rotation | TOKEN_VAZIO | TOKEN_VAZIO | TOKEN_VAZIO | TOKEN_VAZIO | demo/pending |
| lensing | TOKEN_VAZIO | TOKEN_VAZIO | TOKEN_VAZIO | TOKEN_VAZIO | demo/pending |

### WP6 — Non-post-hoc audit

Goal: establish whether the formula predates the later datasets/comparators.

Required evidence chain:

```text
first formula commit
→ first output artifact
→ first dataset commit
→ first comparison commit
→ first result commit
→ later modifications
```

Deliverable:

```text
docs/RLL_NON_POSTHOC_FORMULATION_AUDIT.md
```

## 3. Claim control

Allowed after current evidence:

> RLL base formulation, with a Friedmann-extension term and planned observables, existed publicly in `v1.0.0` in September 2025.

Allowed:

> Later 2026 work matures the project into DESI/CPL/AICc/joint-real validation.

Not allowed yet:

> The entire early computation chain has been verified as mobile/Termux-generated.

Not allowed:

> RLL is physically confirmed.

Not allowed:

> RLL beats CPL/ΛCDM because of tag anteriority.

## 4. Minimal local-audit checklist

A future local auditor should produce:

1. a full file inventory for `v1.0.0`;
2. a hash ledger for all files in the tag snapshot;
3. a keyword hit ledger for formula and provenance terms;
4. a list of absent but referenced files;
5. a list of generated images/CSVs if present;
6. a mobile-execution evidence ledger if any logs or paths exist;
7. a comparison table between `v1.0.0` and current `main`.

## 5. Final target

The final documentation suite should make this chain auditable:

```text
RLL v1.0.0 formula and observables
→ early artifact generation
→ mobile/Termux provenance, if evidenced
→ 2026 DESI/CPL/AICc validation
→ current claim_allowed=false scientific gate
```

The goal is not to overclaim.

The goal is to preserve the real chain of work.
