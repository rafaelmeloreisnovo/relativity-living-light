from __future__ import annotations

import pytest

from data.pipelines.structure_d.energy_momentum_bridge import build_fnext_gate, compute_bridge_row, summarize_f_gap


def test_compute_bridge_row_conserves_measured_transition_terms() -> None:
    row = {
        "rho_before": 10.0,
        "rho_rest_after": 4.0,
        "rho_radiation": 1.0,
        "rho_kinetic": 2.0,
        "rho_thermal": 2.5,
        "pressure": 0.0,
        "rho_field": 0.5,
    }

    bridge = compute_bridge_row(row)

    assert bridge["A_lost"] == 6.0
    assert bridge["A_transition"] == 6.0
    assert bridge["F_gap"] == 0.0


def test_missing_transition_ledger_keeps_f_gap_unmeasured() -> None:
    gate = build_fnext_gate(
        [
            {"model": "LCDM", "chi2": 10.0, "AIC": 14.0, "BIC": 15.0},
            {"model": "RLL", "chi2": 9.0, "AIC": 15.0, "BIC": 17.0},
        ],
        "LCDM",
        "RLL",
    )

    assert gate["status"] == "waiting_for_measured_F_gap"
    assert gate["F_gap"] is None
    assert gate["score"] is None
    assert gate["delta_chi2_candidate_minus_baseline"] == -1.0
    assert gate["delta_AIC_candidate_minus_baseline"] == 1.0
    assert gate["delta_BIC_candidate_minus_baseline"] == 2.0


def test_fnext_score_uses_only_measured_f_gap_rows() -> None:
    gate = build_fnext_gate(
        [
            {"model": "LCDM", "chi2": 10.0, "AIC": 14.0, "BIC": 15.0},
            {"model": "RLL", "chi2": 9.0, "AIC": 15.0, "BIC": 17.0},
        ],
        "LCDM",
        "RLL",
        bridge_rows=[
            {
                "rho_before": 10.0,
                "rho_rest_after": 4.0,
                "rho_radiation": 1.0,
                "rho_kinetic": 2.0,
                "rho_thermal": 2.0,
                "pressure": 0.0,
                "rho_field": 0.5,
            }
        ],
    )

    assert gate["status"] == "complete"
    assert gate["F_gap"] == 0.5
    assert gate["score"] == pytest.approx(2.5)


def test_transition_ledger_rejects_incomplete_rows() -> None:
    with pytest.raises(ValueError, match="missing finite fields"):
        summarize_f_gap([{"rho_before": 1.0}])


def test_committed_joint_real_json_exposes_uninvented_fnext_gate() -> None:
    import json

    with open("results/structure_d/joint_real_likelihood.json", encoding="utf-8") as fp:
        payload = json.load(fp)

    assert payload["fnext"]["schema"] == "rll.energy_momentum_bridge.fnext.v1"
    assert payload["fnext"]["F_gap_status"] == "not_measured"
    assert payload["fnext"]["score"] is None
