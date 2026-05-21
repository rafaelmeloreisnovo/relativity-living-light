from __future__ import annotations

from scripts.run_real_pantheon_validation import _normalize_model_comparison


def test_normalize_model_comparison_schema() -> None:
    summary = {
        "pipeline": "pantheon_oficial_prova_observacional",
        "dataset": "pantheon+",
        "generated_at": "2026-05-21T00:00:00+00:00",
        "n_obs": 1701,
        "rll": {"chi2": 10.0, "AIC": 20.0, "BIC": 30.0, "best_fit_params": {"Om0": 0.3}, "log_likelihood": -5.0},
        "lcdm": {"chi2": 11.0, "AIC": 15.0, "BIC": 18.0, "best_fit_params": {"Om0": 0.29}, "log_likelihood": -5.5},
    }

    payload = _normalize_model_comparison(summary)

    assert payload["dataset"] == "pantheon+"
    assert payload["n_obs"] == 1701
    assert payload["source"] == "data/results/pantheon_fit_summary.json"
    assert payload["covariance_used"] is True
    assert payload["models"]["rll"]["k_params"] == 5
    assert payload["models"]["lcdm"]["k_params"] == 2
    assert payload["models"]["rll"]["log_likelihood"] == -5.0
    assert payload["models"]["lcdm"]["best_fit_params"] == {"Om0": 0.29}
    assert payload["delta"]["delta_chi2_rll_minus_lcdm"] == -1.0
    assert payload["delta"]["delta_aic_rll_minus_lcdm"] == 5.0
    assert payload["delta"]["delta_bic_rll_minus_lcdm"] == 12.0
    assert payload["delta"]["claim_boundary"] == "No superiority claim unless real-data metrics pass predefined thresholds."
    assert payload["source_summary"].endswith("data/results/pantheon_fit_summary.json")


def test_normalize_model_comparison_delta_null_when_metrics_absent() -> None:
    summary = {
        "n_obs": 1701,
        "rll": {"best_fit": {"Om0": 0.3}},
        "lcdm": {"best_fit": {"Om0": 0.29}},
    }
    payload = _normalize_model_comparison(summary)
    assert payload["models"]["rll"]["k_params"] == 5
    assert payload["models"]["lcdm"]["k_params"] == 2
    assert payload["delta"]["delta_chi2_rll_minus_lcdm"] is None
    assert payload["delta"]["delta_aic_rll_minus_lcdm"] is None
    assert payload["delta"]["delta_bic_rll_minus_lcdm"] is None
    assert "interpretation_guardrail" in payload["delta"]
