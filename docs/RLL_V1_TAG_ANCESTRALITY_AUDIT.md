# RLL v1.0.0 Tag Ancestrality Audit

Status: documentary audit, read-only evidence basis.

Scope: preserve what is actually evidenced in the public `v1.0.0` tag and separate it from later 2026 validation work.

## 1. Executive finding

The public tag `v1.0.0` / commit `0b3f4cb06efaa11008b37de519de581268bca5c0`, dated `2025-09-19T06:58:20Z`, already contains a documented RLL cosmological formulation in `README.md`.

This is evidence of **documentary and mathematical anteriority** for the base RLL structure relative to later 2026 DESI/CPL/AICc/joint-real validation work.

This does **not** prove that RLL is physically correct.

This does **not** prove that no later refinement or tuning happened.

It does prove that the base RLL idea and a Friedmann-extension formula were already publicly present before the later DESI materialization and modern model-selection pipeline.

## 2. Evidence snapshot

Repository: `instituto-Rafael/relativity-living-light`

Tag/ref: `v1.0.0`

Commit: `0b3f4cb06efaa11008b37de519de581268bca5c0`

Author shown by GitHub connector: `rafaelmeloreisnovo`

Commit timestamp: `2025-09-19T06:58:20Z`

File read at tag: `README.md`

## 3. What existed in the v1.0.0 README

The tag README contains the heading:

```text
Relativity Living Light — Unified Photonic Superposition Model (v4)
```

It states that photonic superposition is proposed as a dynamic energy component that transitions from a dark-energy-like expansive behavior to a matter-like attractive behavior.

It states that this state is modulated by cosmic magnetic fields and plasma conditions, and that it extends the Friedmann equation.

The equation recorded in the tag includes:

```text
E^2(a) = Ω_r a^-4 + Ω_m a^-3 + Ω_Λ
       + Ω_s0 [ f(a) + (1-f) a^-3 ]
       + Ω_B0 a^-4
       + Ω_P0 a^-4
```

The README describes the `Ω_s0 [ f(a) + (1-f) a^-3 ]` block as a superposition transition from dark-energy-like behavior to matter-like behavior.

## 4. Observables already listed in v1.0.0

The tag README lists observational/test directions:

| Observable / test direction | Status in v1.0.0 README |
|---|---|
| `H(z)` ratio | present |
| `Δμ` residuals | present |
| energy fractions | present |
| `f(z)` and `w_eff(z)` | present |
| entropy-margin H ratio | present |
| entropy-margin `Δμ` | present |
| structure growth `fσ8(z)` | present |
| rotation curve demo | present |
| cluster lensing demo | present |

## 5. What appears later in the repository timeline

A separate commit search for `DESI` shows that DESI-specific work appears later, in 2026.

Observed later milestones include:

| Date range | Later work |
|---|---|
| 2026-02-25 | RLL × DESI term-to-observable mapping |
| 2026-03-03 | quantitative external validation bridge / CPL↔RLL mapping |
| 2026-05-20 | DESI BAO math artifacts and validation matrices |
| 2026-05-31 | DESI DR2 BAO primary points materialization |
| 2026-06-01 | BAO comparator updated to DESI DR2 primary |
| 2026-06-04 | DESI DR2 BAO measurements/covariance materialization |
| 2026-06-13 | joint-real likelihood with LCDM, wCDM, CPL, RLL, AICc and claim gate |

## 6. What this proves

This proves:

1. The RLL name and base cosmological direction existed in a public tag in September 2025.
2. A Friedmann-extension-like equation existed in that tag.
3. The equation already contained `Ω_s0`, `f(a)`, a DE→matter superposition block, magnetic and plasma terms.
4. The README already listed observables such as `H(z)`, `Δμ`, `w_eff`, `fσ8`, rotation curves and lensing.
5. DESI-specific validation/materialization appears later in the visible commit trail.

## 7. What this does not prove

This does not prove:

1. RLL is physically correct.
2. RLL beats ΛCDM, wCDM or CPL.
3. No later parameter refinement happened.
4. No later post-hoc adjustment happened.
5. The tag contained a complete reproducible scientific pipeline.
6. The tag contained all raw datasets, rendered figures, CSVs or mobile execution logs.

## 8. Correct claim language

Allowed:

> The public `v1.0.0` tag from September 2025 documents an RLL base formulation with an explicit Friedmann-extension term, `Ω_s0`, `f(a)`, DE→matter transition language, magnetic/plasma extensions and planned observables. Later DESI/CPL/AICc validation work appears in 2026.

Forbidden:

> RLL is confirmed.

Forbidden:

> RLL beat ΛCDM/CPL because the formula is old.

Forbidden:

> The tag alone proves there was no later tuning.

## 9. Operational meaning

The tag is a chain-of-custody anchor.

The scientifically correct interpretation is:

```text
RLL base formulation existed publicly in 2025
→ modern DESI/CPL/AICc validation matured in 2026
→ current joint-real results must be interpreted as tests of an earlier hypothesis, not as proof of final correctness.
```

## 10. Next audit steps

1. Compare `v1.0.0` against current `main`.
2. Locate first commits for each parameter: `Ω_s0`, `f(a)`, `z_t`, `w_t`, magnetic term, plasma term.
3. Locate first commits for CSV outputs and image artifacts referenced by the tag README.
4. Locate DOI/Zenodo package and verify whether it matches the tag snapshot.
5. Build a non-post-hoc formulation ledger with three states:
   - verified in tag;
   - verified after tag;
   - TOKEN_VAZIO.
