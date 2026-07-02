# Codex Academic Correlation Implementation Plan

## Status

`codex_task_plan / academic_correlation / claim_boundary`

## Purpose

This document converts broad academic, mathematical and heuristic correlation requests into small Codex-ready implementation tasks.

## Claim boundary

```text
claim_allowed=false
implementation_plan=true
scientific_validation=false
proof=false
```

This plan does not validate any scientific, mathematical or physical claim. It tells Codex how to build infrastructure that can later test claims.

## Current package

```text
results/relational_validation/packages/ACADEMIC_CORR_001/
```

Initial files:

```text
package.yml
relation_graph.json
```

Source map:

```text
docs/research/ACADEMIC_CORRELATION_CANDIDATE_MAP.md
```

## Immediate Codex tasks

### Task 1 — Schema

Create:

```text
schemas/relational_validation_package.schema.json
schemas/relation_graph.schema.json
```

Acceptance:

```text
- package.yml validates required fields;
- relation_graph.json validates nodes and edges;
- claim_allowed must be false unless manually reviewed;
- no metric-free package can move beyond RELATIONAL_PENDING.
```

### Task 2 — Validator

Create:

```text
tools/validate_academic_correlation_package.py
```

Acceptance:

```text
- confirms source paths exist;
- confirms graph nodes/edges are non-empty;
- blocks RELATIONAL_CONVERGENCE_CANDIDATE if metrics are TOKEN_VAZIO;
- blocks proof claims if proof path is TOKEN_VAZIO_PROOF_PATH;
- exits nonzero on schema failure.
```

### Task 3 — Proof-obligation registry

Create:

```text
docs/yml/PROOF_OBLIGATION_REGISTRY.yml
```

Minimum fields:

```yaml
claim_or_formula_id:
statement:
assumptions:
derivation_path:
source_paths:
test_paths:
formalization_target:
proof_state:
claim_allowed:
claim_blocked:
next_gate:
```

Acceptance:

```text
- result without derivation is TOKEN_VAZIO_PROOF_PATH;
- numerical equality is separated from representation equality;
- formal proof target is optional and cannot replace informal derivation.
```

### Task 4 — Numeric representation tests

Create tests for the base-zero/base-one seed:

```text
tests/test_numeric_representation_semantics.py
```

Acceptance:

```text
- int("000123") == int("123") under base 10;
- "000123" != "123" as representation;
- zero-indexed and one-indexed conventions must be declared before comparison;
- leading zeros may encode representation state but not new numeric value by default.
```

### Task 5 — RAFAELIA symbol table

Create:

```text
docs/formulas/RAFAELIA_SYMBOL_TABLE.md
```

Acceptance:

```text
- separates state, threshold, phase, entropy and Heaviside symbols;
- records domain constraints such as nonnegative or signed state;
- marks unknown dimensions as TOKEN_VAZIO_DIMENSION;
- does not promote neuroscience or physics claims.
```

### Task 6 — Academic-correlation CI check

Create:

```text
.github/workflows/validate-academic-correlation-package.yml
```

Acceptance:

```text
- permissions: contents: read;
- timeout-minutes <= 10;
- validates package and graph only;
- does not run heavy cosmology;
- does not auto-promote ledger states.
```

## Safe ordering

```text
1. schemas
2. validator
3. tests for notation semantics
4. proof-obligation registry
5. RAFAELIA symbol table
6. CI check
7. first tested axis package
8. ledger update only after tests pass and human review
```

## Forbidden shortcuts

```text
- Do not treat paper similarity as endorsement.
- Do not treat analogy as proof.
- Do not treat final numeric result as derivation.
- Do not treat self-reference as circular proof.
- Do not treat metadata as validation.
- Do not treat representation equality as value equality without declaring semantics.
```

## Final rule for Codex

```text
Implement gates, not conclusions.
Build validators, not victories.
Convert intuition into testable packages, not public claims.
```
