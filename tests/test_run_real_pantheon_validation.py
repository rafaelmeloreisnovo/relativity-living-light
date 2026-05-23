from __future__ import annotations

import math

from scripts.run_real_pantheon_validation import _normalize_model_comparison, interpret_model_comparison, validate_model_comparison_payload


def test_interpret_inconclusive_when_aic_or_bic_missing() -> None:
    out = interpret_model_comparison({"delta_aic_rll_minus_lcdm": None, "delta_bic_rll_minus_lcdm": -3.0})
    assert out["interpretation_label"] == "inconclusive"


def test_interpret_lcdm_preferred_when_any_positive_delta() -> None:
    out = interpret_model_comparison({"delta_aic_rll_minus_lcdm": 0.1, "delta_bic_rll_minus_lcdm": -4.0, "delta_chi2_rll_minus_lcdm": -1.0})
    assert out["interpretation_label"] == "lcdm_preferred"


def test_interpret_rll_preferred_tentative() -> None:
    out = interpret_model_comparison({"delta_aic_rll_minus_lcdm": -2.5, "delta_bic_rll_minus_lcdm": -2.2, "delta_chi2_rll_minus_lcdm": 0.0})
    assert out["interpretation_label"] == "rll_preferred_tentative"


def test_interpret_rll_preferred_strong() -> None:
    out = interpret_model_comparison({"delta_aic_rll_minus_lcdm": -10.0, "delta_bic_rll_minus_lcdm": -10.1, "delta_chi2_rll_minus_lcdm": -0.5})
    assert out["interpretation_label"] == "rll_preferred_strong"


def test_normalize_model_comparison_required_metrics_and_formulas(monkeypatch, tmp_path) -> None:
    summary = {
        "pipeline": "pantheon_oficial_prova_observacional",
        "dataset": "pantheon+",
        "generated_at": "2026-05-21T00:00:00+00:00",
        "n_obs": 1701,
        "rll": {"chi2": 10.0},
        "lcdm": {"chi2": 11.0},
    }
    f1 = tmp_path / "lcparam_full_long_zhel.txt"
    f2 = tmp_path / "Pantheon+SH0ES_STAT+SYS.cov"
    f1.write_text("a")
    f2.write_text("b")
    import scripts.run_real_pantheon_validation as m
    monkeypatch.setattr(m, "_pantheon_files", lambda: [f1, f2])
    payload = _normalize_model_comparison(summary, command_used="python scripts/run_real_pantheon_validation.py")
    validate_model_comparison_payload(payload)

    assert payload["k_rll"] == 5
    assert payload["k_lcdm"] == 2
    assert payload["AIC_rll"] == payload["chi2_rll"] + 2 * payload["k_rll"]
    assert payload["AIC_lcdm"] == payload["chi2_lcdm"] + 2 * payload["k_lcdm"]
    assert math.isclose(payload["BIC_rll"], payload["chi2_rll"] + payload["k_rll"] * math.log(payload["n_obs"]))
    assert math.isclose(payload["BIC_lcdm"], payload["chi2_lcdm"] + payload["k_lcdm"] * math.log(payload["n_obs"]))
    assert payload["delta_chi2_rll_minus_lcdm"] == payload["chi2_rll"] - payload["chi2_lcdm"]
    assert payload["delta_aic_rll_minus_lcdm"] == payload["AIC_rll"] - payload["AIC_lcdm"]
    assert payload["delta_bic_rll_minus_lcdm"] == payload["BIC_rll"] - payload["BIC_lcdm"]
    assert payload["interpretation_label"] in {"inconclusive", "lcdm_preferred", "rll_preferred_tentative", "rll_preferred_strong"}
    assert payload["claim_boundary"] == "No superiority claim unless real-data metrics pass predefined thresholds."


def test_aic_bic_use_distinct_parameter_counts_for_models(monkeypatch, tmp_path) -> None:
    summary = {
        "n_obs": 1701,
        "rll": {"chi2": 100.0},
        "lcdm": {"chi2": 100.0},
    }
    f1 = tmp_path / "lcparam_full_long_zhel.txt"
    f2 = tmp_path / "Pantheon+SH0ES_STAT+SYS.cov"
    f1.write_text("a")
    f2.write_text("b")
    import scripts.run_real_pantheon_validation as m
    monkeypatch.setattr(m, "_pantheon_files", lambda: [f1, f2])

    payload = _normalize_model_comparison(summary, command_used="python scripts/run_real_pantheon_validation.py")
    expected_delta_aic = 2 * (5 - 2)
    expected_delta_bic = (5 - 2) * math.log(summary["n_obs"])

    assert payload["AIC_rll"] - payload["AIC_lcdm"] == expected_delta_aic
    assert math.isclose(payload["BIC_rll"] - payload["BIC_lcdm"], expected_delta_bic)


def test_normalize_fails_without_real_data_files(monkeypatch) -> None:
    import scripts.run_real_pantheon_validation as m
    monkeypatch.setattr(m, "_pantheon_files", lambda: [m.ROOT / "data" / "pantheon" / "missing.txt"])
    try:
        _normalize_model_comparison({"n_obs": 10, "rll": {"chi2": 1.0}, "lcdm": {"chi2": 2.0}}, command_used="cmd")
        assert False, "expected FileNotFoundError"
    except FileNotFoundError:
        pass


def test_retain_existing_artifact_when_real_inputs_missing(tmp_path, monkeypatch) -> None:
    import scripts.run_real_pantheon_validation as m
    target = tmp_path / "model_comparison.json"
    target.write_text('{"status":"old"}')
    monkeypatch.setattr(m, "MODEL_COMPARISON_JSON", target)
    assert m._retain_existing_artifact("missing real data") is True


def test_do_not_retain_when_no_previous_artifact(tmp_path, monkeypatch) -> None:
    import scripts.run_real_pantheon_validation as m
    target = tmp_path / "model_comparison.json"
    monkeypatch.setattr(m, "MODEL_COMPARISON_JSON", target)
    assert m._retain_existing_artifact("missing real data") is False
