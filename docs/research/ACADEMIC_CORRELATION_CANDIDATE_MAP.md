# Academic Correlation Candidate Map

## Status

`research_map / heuristic_correlation / claim_boundary`

## Purpose

This document records academic and mathematical correlation candidates for RLL/RAFAELIA without promoting them as scientific proof.

It exists to help Codex and human reviewers convert broad relational intuition into small testable units.

## Claim boundary

```text
claim_allowed=false
correlation_is_not_validation=true
analogy_is_not_evidence=true
result_without_derivation=TOKEN_VAZIO_PROOF_PATH
self_reference_is_traceability_not_proof=true
```

This file does not validate RLL, RAFAELIA, cosmology, graph theory, chaos theory, number theory, theology, metaphysics or any physical claim. It only maps candidate relations that must be tested or blocked.

## External source anchors consulted

| Anchor | Why it matters here | Boundary |
|---|---|---|
| DESI DR2 BAO cosmological constraints, arXiv:2503.14738 | Modern data combination reopens dynamical dark-energy discussion with w0/wa language. | Does not validate RLL; it defines an adversarial comparison context. |
| Planck 2018 cosmological parameters, arXiv:1807.06209 | Planck remains a strong Lambda-CDM anchor and CMB baseline. | CMB shift summaries are not full Planck likelihoods. |
| FAIR Guiding Principles, Scientific Data 2016 | Supports machine-actionable metadata, provenance and reuse. | FAIR metadata does not equal scientific truth. |
| Adaptive dynamical networks / chaos literature | Provides vocabulary for adaptive graph dynamics, synchronization and slow chaos. | Similar vocabulary does not prove RAFAELIA. |
| Lean/Isabelle/formal proof assistant literature | Supports a path from statement/result to formal proof obligation. | A formalization plan is not a formal proof. |
| COPE authorship and AI guidance | Supports separating human authorship from AI assistance. | Governance guidance is not legal advice. |

## Core rule

```text
A relation can become useful only when it receives:
source -> formal statement -> metric -> baseline -> test -> contradiction check -> uncertainty status -> claim boundary.
```

Without that chain, the relation remains:

```text
RELATIONAL_PENDING / TOKEN_VAZIO_PROOF_PATH
```

## Candidate axes

### AXIS-01 — DESI/CPL/RLL dynamic dark-energy corridor

```yaml
axis_id: AXIS-01
relation_type: cosmology_background_relation
external_anchor: DESI DR2 BAO + CMB + SNe dynamical dark-energy discussion
repo_anchor:
  - data/results/model_comparison.json
  - results/structure_d/joint_real_likelihood.json
  - docs/RLL_CURRENT_RESULTS_PAPER_TABLE.md
candidate_question: >-
  Does any robust RLL parameter region with Os0 > 0 become competitive against LCDM,
  wCDM and CPL/w0waCDM under real-data baselines?
claim_allowed: false
claim_blocked:
  - RLL confirmed
  - RLL beats CPL
  - RLL solves dark energy
proof_obligation:
  - robust seeds
  - posterior or bootstrap
  - Pantheon+/DES/DESY5 route
  - BAO covariance
  - Planck/CMB compressed or full-likelihood boundary
  - negative ledger link
```

### AXIS-02 — Growth discriminator: background degeneracy is not enough

```yaml
axis_id: AXIS-02
relation_type: growth_structure_discriminator
candidate_question: >-
  If RLL is background-degenerate with CPL, can growth observables distinguish it?
required_observables:
  - f_sigma8
  - S8
  - weak_lensing
  - CLASS_or_CAMB_growth_backend
claim_allowed: false
claim_blocked:
  - background fit proves physics
  - H(z)/BAO alone resolves the mechanism
```

### AXIS-03 — Adaptive graph dynamics / RAFAELIA lattice

```yaml
axis_id: AXIS-03
relation_type: adaptive_dynamical_network_analogy
repo_anchor:
  - data/formulas/RAFAELIA_FORMAL_UNIFIED_CORE.md
candidate_question: >-
  Can RAFAELIA be expressed as a graph/lattice dynamical system with explicit
  state variables, update rules, stability criteria and invariants?
claim_allowed: false
claim_blocked:
  - neuroscience claim
  - physics claim
  - consciousness claim
proof_obligation:
  - symbol table
  - dimensional/domain constraints
  - invariant tests
  - Lyapunov or stability proxy
  - simulation seeds
  - synthetic-only boundary
```

### AXIS-04 — Chaos, bifurcation and synchronization vocabulary

```yaml
axis_id: AXIS-04
relation_type: chaos_theory_candidate
candidate_question: >-
  Do RAFAELIA/RLL toy dynamics show measurable bifurcation, synchronization,
  attractor or Lyapunov-like behavior under defined update rules?
claim_allowed: false
required_tests:
  - deterministic seed control
  - phase-space output
  - parameter sweep
  - recurrence/stability report
  - chaos metric declared before interpretation
```

### AXIS-05 — Proof path obligation: Bhaskara/result without derivation

```yaml
axis_id: AXIS-05
relation_type: formal_proof_obligation
principle: >-
  A numerical or symbolic result without derivation is not a proof; it is a
  result token with TOKEN_VAZIO_PROOF_PATH.
example_language: >-
  If only the final number appears, the path is missing. The claim must store
  the derivation path or remain blocked.
claim_allowed: false
codex_task:
  - create proof_obligation registry
  - map formula -> assumptions -> derivation -> test -> output
  - optionally target Lean/Isabelle only after informal derivation is stable
```

### AXIS-06 — Base-zero/base-one notation and leading-zero semantics

```yaml
axis_id: AXIS-06
relation_type: notation_semantics
user_seed: "000123, 123, tudo esta base0 no 1"
interpretation_boundary: >-
  Treat this as a notation/representation hypothesis, not numerology or proof.
formal_question: >-
  Which transformations preserve numeric value, which preserve representation,
  and which encode state/position/identity?
claim_allowed: false
required_tests:
  - grammar for numeric strings
  - value equivalence tests: 000123 == 123 in base-10 value
  - representation non-equivalence tests: "000123" != "123" as string/state
  - base/indexing convention declaration: zero-indexed vs one-indexed
```

### AXIS-07 — Whitehead/Russell-style proof-length caution

```yaml
axis_id: AXIS-07
relation_type: proof_depth_caution
principle: >-
  Simple-looking statements may require long formal paths. Do not replace
  derivation with confidence.
claim_allowed: false
blocked_shortcut: "obvious_result_as_proof"
```

### AXIS-08 — Hidden relation mining / heuristic graph

```yaml
axis_id: AXIS-08
relation_type: heuristic_relation_mining
candidate_question: >-
  Can the repository map latent, oblique, inverse, paradoxical, derivative,
  antiderivative and graph relations without promoting them prematurely?
claim_allowed: false
required_artifacts:
  - relation_graph.json
  - candidate list
  - edge types
  - negative edge ledger
  - contradiction check
  - review packet
```

## Codex implementation principle

Codex should not implement broad claims directly. It should implement small gates:

```text
1. registry
2. schema
3. validator
4. one package
5. tests
6. CI check
7. review note
```

## Minimal next package

The first package should be:

```text
results/relational_validation/packages/ACADEMIC_CORR_001/
```

Its role is to store this map as `RELATIONAL_PENDING`, not as validation.

## Final rule

```text
Magical-looking relation -> candidate edge.
Candidate edge -> proof obligation.
Proof obligation -> test package.
Test package -> metric/baseline/uncertainty.
Only then can a claim move state.
```
