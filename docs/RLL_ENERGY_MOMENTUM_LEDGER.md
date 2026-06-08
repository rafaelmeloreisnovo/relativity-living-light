# RLL energy-momentum observational ledger

## Purpose

The ledger is the provenance layer for SGP/FNext energy-momentum accounting. It prevents absent observational terms from being silently treated as measured physics.

## Required fields

A complete measured ledger contains seven measured fields with units and provenance:

- `rho_before` in `J/m^3`;
- `rho_rest_after` in `J/m^3`;
- `rho_radiation` in `J/m^3`;
- `rho_kinetic` in `J/m^3`;
- `rho_thermal` in `J/m^3`;
- `pressure` in `Pa`;
- `rho_field` in `J/m^3`.

Each field carries `name`, `value`, `uncertainty`, `unit`, `source`, `doi_or_url`, `sha256` when a local measured file is used, `license`, `measured`, and `notes`.

## A_lost

`A_lost = rho_before - rho_rest_after`. It is the measured energy-density decrease between the pre-transition state and the post-transition rest component.

## A_transition

`A_transition = rho_radiation + rho_kinetic + rho_thermal + pressure/c^2 + rho_field`. It accounts for measured transition channels only.

## Why pressure enters as P/c²

Pressure has units of pascals, equivalent to `J/m^3`, but in the relativistic density accounting used by this bridge the pressure contribution is represented as an effective mass/energy-density term `P/c^2`. The conversion is explicit and must not be hidden.

## Radiation and thermal terms

Radiation and thermal content are energy forms, but they still require real observables, uncertainty, units, source, and license notes. Their physical plausibility does not authorize filling missing values.

## F_gap

`F_gap = A_lost - A_transition`. If the ledger is incomplete, `F_gap` must remain `null` and the status must be `not_measured`. This is correct behavior: a null bridge term is more honest than an invented closure term.

## Connection to FNext

FNext consumes the model-comparison deltas plus the measured `F_gap` status. FNext is diagnostic only. It can support interpretation when all inputs exist, but it cannot replace real-data model validation and cannot by itself set `claim_allowed` to `true`.

## Claim boundary

The ledger does not confirm RLL. It only records whether the energy-momentum terms required for a diagnostic bridge were measured. The active boundary remains: "No superiority claim unless real-data metrics pass predefined thresholds."
