# RLL Latent Theses and Recent-Data Crosswalk

**Status:** formal professional roadmap  
**Claim level:** `claim_allowed=false`  
**Registry:** `data/real_sources/rll_latent_theses_registry.yml`  
**Purpose:** convert recent-paper alignment and repository signals into testable, falsifiable, non-inflated thesis routes.

---

## 1. Executive summary

The current scientific value of RLL is not a confirmed cosmological discovery. Its value is a structured, auditable and claim-gated research program with latent theses that can be tested against real public data and adversary baselines.

The current canonical cosmology artifact remains a smoke/sanity run. It reports `claim_allowed=false`, uses `maxiter=3`, and currently favors CPL/w0waCDM over RLL. RLL collapses to the LCDM-like limit through `Os0=0.0` and is penalized by information criteria because it carries more parameters without improving chi2.

Therefore, the correct professional framing is:

```text
RLL is a falsifiable candidate program with latent test routes; it is not currently a confirmed or preferred cosmological model.
```

---

## 2. Current repository facts

| Item | Current state | Consequence |
|---|---|---|
| Joint real-data smoke artifact | exists | can compare LCDM/wCDM/CPL/RLL in a limited run |
| `claim_allowed` | `false` | no strong scientific claim allowed |
| Best current smoke baseline | CPL/w0waCDM | RLL must beat CPL, not only LCDM |
| RLL diagnostic | `Os0=0.0` | RLL sector inactive in smoke result |
| Pantheon+ complete route | incomplete or route-limited | broad cosmology claim blocked |
| CMB block | compressed CMB shift | not a full Planck likelihood |
| Growth block | fσ8 input exists | needs CLASS/CAMB or equivalent benchmark |
| Compact-remnant route | prioritized in dashboard | may be the most practical next non-cosmology route |

---

## 3. Recent-data crosswalk policy

Recent papers and datasets are not proofs of RLL. They are used only to select the next falsifiable tests.

| External context family | Why it matters | RLL-safe interpretation |
|---|---|---|
| DESI DR2 BAO / dynamic dark energy | strengthens the need to compare against CPL/w0waCDM | RLL must compete against CPL, not claim DESI confirmation |
| Pantheon+/DESY5/SNe | constrains late-time expansion and H0-related claims | incomplete SN materialization blocks broad claims |
| Planck/ACT/CMB | anchors early-universe constraints | CMB shift is only compressed evidence |
| fσ8/S8/lensing | can break background degeneracies | growth is a critical discriminator |
| GW standard sirens | CMB-independent late-universe route | candidate future test, not present evidence |
| LVK/GWOSC compact remnants | public posterior samples can test mass-gap metrics | practical route for falsifiable non-cosmology result |
| JWST/Chandra high-z SMBHs | tests seed/growth scenarios | classifier thesis only until baselines exist |
| Gaia/OGLE astrometry | tests dark/compact/wandering candidates | candidate triage route, not population proof |

---

## 4. Latent theses

### LT-001 — RLL dynamic-transition sector versus CPL

**Thesis:** test whether an RLL dynamic-transition sector can remain active with `Os0 > 0` and survive chi2/AIC/AICc/BIC comparison against LCDM, wCDM and CPL under robust real-data fits.

**Current fact:** smoke result has `Os0=0.0`; RLL is not preferred.

**Main falsifier:** if RLL remains LCDM-like or worse than CPL under multi-seed robust fits and comparable covariance/error policy, strong cosmology claims remain blocked.

**Next action:** robust fit with seeds `1..10`, `maxiter>=100`, no overwrite of canonical smoke artifact.

---

### LT-002 — Growth-sector discriminator

**Thesis:** growth observables may discriminate RLL from CPL/interacting-dark-energy degeneracies better than background distances alone.

**Current fact:** fσ8 input exists, but growth benchmark is not claim-ready.

**Main falsifier:** if RLL cannot produce distinguishable or better growth behavior than CPL/adversary baselines after CLASS/CAMB or equivalent benchmarking, the growth thesis remains blocked.

**Next action:** implement external growth benchmark and compare fσ8/S8/lensing metrics.

---

### LT-003 — CMB-independent late-universe RLL test with standard sirens

**Thesis:** RLL can be tested as a late-universe transition model using GW standard sirens + BAO + SNe without immediately relying on full Planck likelihood.

**Current fact:** no GW-siren route is materialized in the repository.

**Main falsifier:** if siren+BAO+SNe constraints prefer LCDM/CPL and RLL remains inactive or noncompetitive, this route remains blocked.

**Next action:** create standard-siren data contract and likelihood skeleton.

---

### LT-004 — Compact-remnant boundary and mass-gap overlap

**Thesis:** RLL-inspired transition metrics may be tested as a compact-remnant boundary hypothesis using LVK/GWOSC posterior samples.

**Current fact:** validation dashboard marks compact-remnant boundary as the recommended next route because it has a clearer metric and public data path.

**Main falsifier:** if posterior samples do not show reproducible boundary signal beyond standard population baselines, the thesis remains blocked.

**Next action:** ingest LVK/GWOSC posterior samples with checksum and compute `mass_gap_overlap_probability`.

---

### LT-005 — High-redshift SMBH seed-regime classifier

**Thesis:** RLL language can be operationalized as a classifier across early SMBH seed/growth regimes rather than as immediate cosmological proof.

**Current fact:** route exists at seed level; JWST/Chandra raw table and seed-growth baselines are missing.

**Main falsifier:** if standard light-seed, heavy-seed, direct-collapse or super-Eddington baselines explain the catalog without RLL-specific predictive improvement, the thesis remains a classifier experiment only.

**Next action:** build high-z SMBH source table schema and baseline grid.

---

### LT-006 — Wandering or dark compact-object triage

**Thesis:** an auditable triage pipeline can evaluate dark compact-object candidates using astrometric consistency, luminous-counterpart exclusion and contaminant probability.

**Current fact:** seed route exists; Gaia/OGLE/RV/light-curve data are not yet materialized.

**Main falsifier:** if candidates are explained by luminous counterparts, background AGN, stellar contamination or weak astrometric evidence, dark-compact claims remain blocked.

**Next action:** define candidate schema and raw data manifest.

---

## 5. Thesis ranking

| Rank | Thesis | Why |
|---:|---|---|
| 1 | LT-004 compact-remnant boundary | clearest public data path and metric |
| 2 | LT-001 RLL vs CPL robust cosmology | central to RLL, but technically heavier |
| 3 | LT-002 growth discriminator | critical for physical distinction |
| 4 | LT-003 standard sirens | high upside, dataset/likelihood not yet present |
| 5 | LT-005 high-z SMBH classifier | promising but baseline-heavy |
| 6 | LT-006 dark compact-object triage | useful, but raw-data and contamination controls needed |

---

## 6. Professional publication tracks

### Track A — conservative methodology paper

```text
RLL as a claim-gated falsifiable research program: current real-data smoke comparison, negative result and roadmap to robust tests.
```

Allowed now. This is the safest academic track.

### Track B — robust cosmology paper

```text
Testing an RLL transition sector against LCDM, wCDM and CPL under DESI/BAO/SN/CMB/growth data.
```

Not ready until robust fit, Pantheon+/SNe, CMB covariance, growth benchmark and posterior are complete.

### Track C — compact-remnant boundary paper

```text
A claim-gated compact-remnant boundary test using public GW posterior samples.
```

Potentially the most practical route for a publishable falsification-style result.

---

## 7. Formal claim language

Allowed:

```text
RLL has claim-gated latent theses and a reproducible scaffold for testing them against public data and adversary baselines.
```

Blocked:

```text
RLL is confirmed.
RLL beats LCDM/CPL.
DESI confirms RLL.
Planck validates RLL.
JWST or LVK confirms RLL.
A metaphor or registry is observational proof.
```

---

## 8. Operational next steps

1. Validate the latent-thesis registry in CI.
2. Keep `claim_allowed=false` until a specific thesis passes its data, metric, baseline and falsifier gates.
3. Prioritize `LT-004` for a practical public-data result.
4. Run `LT-001` robust fit only in versioned output directories.
5. Do not overwrite canonical smoke artifacts.
6. Preserve negative results as scientific evidence.

---

## 9. R3 summary

```text
F_ok   = RLL has formal latent theses, registry, falsifiers and publication tracks.
F_gap  = no latent thesis currently authorizes a strong scientific claim.
F_next = validate registry, then execute the highest-value route with raw data, baseline, metric and checksum.
```
