# RLL energy-momentum bridge and FNext gate

The energy-momentum bridge implements the pure calculations used by SGP/FNext:

- `pressure_density(P) = P/c^2`;
- `A_lost = rho_before - rho_rest_after`;
- `A_transition = rho_radiation + rho_kinetic + rho_thermal + P/c^2 + rho_field`;
- `F_gap = A_lost - A_transition`.

Uncertainties are propagated in quadrature under an independence assumption. Complete uncertainty propagation requires uncertainties for all seven ledger fields. If any uncertainty is absent, the bridge may still compute `F_gap` from measured values but marks `uncertainty_status: incomplete`.

FNext returns a machine-readable gate with the RLL-minus-LCDM deltas, `F_gap`, score fields, claim boundary, and reason. Because no physically justified normalization for adding `F_gap` to chi-square and information-criterion deltas has been defined, a scalar score is blocked with `score_status: blocked_until_normalization_defined` whenever all terms exist. Without a complete measured ledger, `F_gap` and `score` remain `null`.

FNext is diagnostic and is not a claim engine. It never authorizes scientific superiority language by itself.
