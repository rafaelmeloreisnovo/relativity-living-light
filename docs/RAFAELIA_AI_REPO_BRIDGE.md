# RAFAELIA AI repository bridge

Status date: 2026-06-25

## Repository roles

| Repository | Role |
|---|---|
| `rafaelmeloreisnovo/Rafaelia_Private` | private corpus, symbolic invariants, Ethica, BitStack and ZIPRAF base |
| `rafaelmeloreisnovo/CONVERSATIONS_CHUNKS_PRIVATE` | conversation chunks, memory bridge, manifests, chunk summaries and temporal corpus maps |
| `rafaelmeloreisnovo/GAIA_phi` | deterministic core, hashing, vecdb, manifests, guard and C/Python engines |
| `rafaelmeloreisnovo/llamaRafaelia` | local inference/runtime layer in C/C++ and RMRCTI primary source path |
| `instituto-Rafael/relativity-living-light` | scientific validation, real data, loaders, CI and claim gates |

## Stack reading

```text
Private corpus -> conversation chunks -> deterministic scanner -> deterministic core -> local inference -> scientific validation
```

## Temporal corpus bridge

The conversation corpus must not be treated as a single file to read fully in every session.

```text
Google Takeout / conversations.json
  -> chunk manifest
  -> hash check
  -> RMRCTI scan
  -> bitstack/jsonl + csv
  -> coupled report
  -> compressed summary
  -> global timeline map
  -> formula/link
  -> claim gate
```

Poetic language is preserved as a didactic layer, but evidence remains separated:

```text
metaphor/parabola -> technical translation -> deterministic artifact -> claim boundary
```

## Formula bridge

The formulas artifact is represented by:

```text
data/formulas/FORMULAS_ARTIFACTS_MANIFEST.json
data/formulas/FORMULA_INDEX_CONTRACT.json
scripts/validate_formulas_manifest.py
scripts/validate_formula_index_contract.py
scripts/materialize_formula_index.py
.github/workflows/formulas-artifacts-validation.yml
```

The current verified manifest records 486 formulas, 53 sources and three categories: `geral`, `cosmology_metrics`, `integridade_e_criptografia`.

## External convergence bridge

External publications may be used as **independent convergence references** only when they pass through the same claim boundary discipline.

Current registered convergence documents:

```text
docs/CONVERGENCIAS_INDEPENDENTES_RAFAELIA_RLL.md
docs/CONVERGENCIA_ETH_HLS_TRANSICOES_FASE.md
```

Bridge rule:

```text
external source -> technical reading -> bounded analogy -> claim boundary -> own validation or TOKEN_VAZIO
```

Convergence scale:

```text
3 convergences -> technical note and traceability
8 convergences -> registry matrix and prioritization
9 convergences -> combinatorial regime; stronger gate, not stronger claim
```

For the Higgs-like stiffness / ETH case, the permitted interpretation is narrow:

```text
complex dissipative component -> measurable deviation -> emergent stiffness near phase transition
```

This does **not** validate RAFAELIA, BITRAF, T7 or RLL cosmology. It only records a controlled analogy for treating noise/dissipation as a state variable in transition models.

## Operational rules

Formula gate:

```text
formula -> category -> source -> gate -> loader/test/result -> claim or TOKEN_VAZIO
```

Conversation gate:

```text
chunk -> offset/hash -> RMRCTI metrics -> anomaly flag -> summary/map -> formula/link or TOKEN_VAZIO
```

External convergence gate:

```text
paper/news -> source metadata -> technical extraction -> analogy label -> claim boundary -> validation path or TOKEN_VAZIO
```

Convergence registry gate:

```text
convergence candidate -> independence check -> source/artifact -> metric need -> claim_state
```

## Claim boundary

- A formula is not proof by itself.
- A metaphor is not proof by itself.
- A conversation chunk is not proof by itself.
- An external analogy is not proof by itself.
- A convergence count is not proof by itself.
- A claim is only promoted when linked to source, deterministic artifact, test/CI and result.

## Next integrations

1. Import full `formulas.json` or artifact ZIP when safe.
2. Generate stable formula IDs using `scripts/materialize_formula_index.py`.
3. Map formula IDs to claim gates and result artifacts.
4. Link cosmology formulas to RLL loaders.
5. Link guard formulas to GAIA_phi and Rafaelia_Private.
6. Link local runtime prompts to llamaRafaelia.
7. Link conversation chunks to RMRCTI reports and global timeline maps.
8. Keep external convergence notes separated from validation claims.
9. Use the convergence registry to prioritize evidence collection without promoting untested claims.
