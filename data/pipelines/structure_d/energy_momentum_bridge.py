"""Energy-momentum bridge accounting for the RLL SGP/FNext validation gate.

The functions in this module are deliberately local-first and falsifiable.  They
compute only quantities that are present in the supplied rows or in an explicit
model-comparison artifact.  They never invent a missing transition term: when a
measured transition ledger is absent, ``F_gap`` and the scalar ``FNext`` score are
reported as ``None`` with a machine-readable status.
"""

from __future__ import annotations

import math
from collections.abc import Iterable, Mapping
from typing import Any

C_M_PER_S = 299_792_458.0
REQUIRED_LEDGER_FIELDS = (
    "rho_before",
    "rho_rest_after",
    "rho_radiation",
    "rho_kinetic",
    "rho_thermal",
    "pressure",
    "rho_field",
)


def _finite_float(value: Any) -> float | None:
    if value is None:
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if not math.isfinite(number):
        return None
    return number


def compute_bridge_row(row: Mapping[str, Any], c_m_per_s: float = C_M_PER_S) -> dict[str, float]:
    """Compute A_lost, A_transition and F_gap for one measured ledger row."""

    values: dict[str, float] = {}
    missing = []
    for field in REQUIRED_LEDGER_FIELDS:
        parsed = _finite_float(row.get(field))
        if parsed is None:
            missing.append(field)
        else:
            values[field] = parsed
    if missing:
        raise ValueError(f"transition ledger row missing finite fields: {missing}")

    pressure_density = values["pressure"] / (float(c_m_per_s) ** 2)
    a_lost = values["rho_before"] - values["rho_rest_after"]
    a_transition = (
        values["rho_radiation"]
        + values["rho_kinetic"]
        + values["rho_thermal"]
        + pressure_density
        + values["rho_field"]
    )
    return {
        "A_lost": a_lost,
        "A_transition": a_transition,
        "pressure_density": pressure_density,
        "F_gap": a_lost - a_transition,
    }


def summarize_f_gap(rows: Iterable[Mapping[str, Any]] | None) -> dict[str, Any]:
    """Summarize measured F_gap rows without synthesizing absent data."""

    if rows is None:
        return {
            "status": "not_measured",
            "rows_used": 0,
            "F_gap": None,
            "note": "No transition ledger supplied; missing bridge term must be measured, not invented.",
        }

    computed = [compute_bridge_row(row) for row in rows]
    if not computed:
        return {
            "status": "not_measured",
            "rows_used": 0,
            "F_gap": None,
            "note": "Empty transition ledger; missing bridge term must be measured, not invented.",
        }

    total_gap = math.fsum(item["F_gap"] for item in computed)
    return {
        "status": "measured",
        "rows_used": len(computed),
        "F_gap": total_gap,
        "mean_F_gap": total_gap / len(computed),
        "components": computed,
    }


def _row_by_model(comparison_rows: Iterable[Mapping[str, Any]], model_name: str) -> Mapping[str, Any]:
    for row in comparison_rows:
        if row.get("model") == model_name:
            return row
    raise ValueError(f"model row not found: {model_name}")


def build_fnext_gate(
    comparison_rows: Iterable[Mapping[str, Any]],
    baseline_model: str,
    candidate_model: str,
    bridge_rows: Iterable[Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    """Build the SGP/FNext gate from model deltas plus optional F_gap ledger rows."""

    rows = list(comparison_rows)
    baseline = _row_by_model(rows, baseline_model)
    candidate = _row_by_model(rows, candidate_model)

    delta_chi2 = float(candidate["chi2"]) - float(baseline["chi2"])
    delta_aic = float(candidate["AIC"]) - float(baseline["AIC"])
    delta_bic = float(candidate["BIC"]) - float(baseline["BIC"])
    gap = summarize_f_gap(bridge_rows)
    f_gap = gap["F_gap"]
    score = None if f_gap is None else delta_chi2 + delta_aic + delta_bic + float(f_gap)

    return {
        "schema": "rll.energy_momentum_bridge.fnext.v1",
        "status": "complete" if score is not None else "waiting_for_measured_F_gap",
        "claim_boundary": "Diagnostic gate only; no superiority claim is implied.",
        "formula": "FNext = delta_chi2 + delta_AIC + delta_BIC + F_gap",
        "baseline_model": baseline_model,
        "candidate_model": candidate_model,
        "delta_chi2_candidate_minus_baseline": delta_chi2,
        "delta_AIC_candidate_minus_baseline": delta_aic,
        "delta_BIC_candidate_minus_baseline": delta_bic,
        "F_gap": f_gap,
        "F_gap_status": gap["status"],
        "F_gap_rows_used": gap["rows_used"],
        "score": score,
        "gap_detail": gap,
    }
