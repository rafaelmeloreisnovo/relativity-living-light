# Route Defibrillation Policy

Status: operational recovery policy  
Claim level: `claim_allowed=false`

---

## Purpose

This policy defines what to do when a route fails, changes, receives unexpected data, or produces a negative result.

The goal is not to force success. The goal is to keep the route scientifically alive without turning uncertainty into false claim.

---

## General rule

```text
If a route breaks, freeze the claim, preserve the raw data, record the failure, and decide whether to repair, downgrade, or falsify the route.
```

---

## Failure classes

| Class | Meaning | Required action |
|---|---|---|
| `parser_failure` | file exists but cannot be read | preserve raw file, add parser incident |
| `metadata_gap` | source, license, date or sha missing | keep TOKEN_VAZIO, block metric |
| `baseline_gap` | metric exists without comparison model | block claim, add baseline requirement |
| `uncertainty_gap` | no error model | block claim, add uncertainty requirement |
| `negative_metric` | result does not support route | update negative results ledger |
| `source_volatility` | source or interpretation changed | preserve old source, add volatility note |
| `frame_or_unit_mismatch` | coordinate frame, epoch or unit mismatch | repair metadata before changing formula |

---

## Route-specific response

### Orbital route

```text
If residual jumps:
  check frame
  check epoch
  check units
  check TDB/UTC
  check central body
  then update negative ledger if still inconsistent
```

### Compact-remnant route

```text
If posterior does not support mass-gap hypothesis:
  record overlap probability
  record baseline
  keep result as negative or neutral
  do not force interpretation
```

### High-z SMBH route

```text
If growth is feasible under standard assumptions:
  mark route as non-anomalous
  preserve result
  do not claim tension
```

### Gaia / wandering compact route

```text
If luminous or non-BH alternative fits:
  downgrade dark compact interpretation
  preserve candidate as alternative-model test
```

---

## Safe conclusion

A failed route is not wasted. It becomes a negative result, a boundary condition, or a better measurement target.
