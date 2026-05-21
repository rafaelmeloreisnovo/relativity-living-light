from __future__ import annotations

from scripts.run_real_pantheon_validation import _normalize_model_comparison, interpret_model_comparison


def test_interpret_inconclusive_when_aic_or_bic_missing() -> None:
    out = interpret_model_comparison({"delta_aic_rll_minus_lcdm": None, "delta_bic_rll_minus_lcdm": -3.0})
    assert out["interpretation_label"] == "inconclusive"


def test_interpret_lcdm_preferred_when_any_positive_delta() -> None:
    out = interpret_model_comparison({
        "delta_aic_rll_minus_lcdm": 0.1,
        "delta_bic_rll_minus_lcdm": -4.0,
        "delta_chi2_rll_minus_lcdm": -1.0,
    })
    assert out["interpretation_label"] == "lcdm_preferred"


def test_interpret_rll_preferred_tentative() -> None:
    out = interpret_model_comparison({
        "delta_aic_rll_minus_lcdm": -2.5,
        "delta_bic_rll_minus_lcdm": -2.2,
        "delta_chi2_rll_minus_lcdm": -0.01,
    })
    assert out["interpretation_label"] == "rll_preferred_tentative"


def test_interpret_rll_preferred_strong() -> None:
    out = interpret_model_comparison({
        "delta_aic_rll_minus_lcdm": -10.0,
        "delta_bic_rll_minus_lcdm": -10.1,
        "delta_chi2_rll_minus_lcdm": -0.5,
    })
    assert out["interpretation_label"] == "rll_preferred_strong"


def test_normalize_model_comparison_schema_and_guardrails() -> None:
    summary = {
        "pipeline": "pantheon_oficial_prova_observacional",
        "dataset": "pantheon+",
        "generated_at": "2026-05-21T00:00:00+00:00",
        "n_obs": 1701,
        "rll": {"chi2": 10.0, "AIC": 20.0, "BIC": 30.0, "best_fit_params": {"Om0": 0.3}, "log_likelihood": -5.0},
        "lcdm": {"chi2": 11.0, "AIC": 15.0, "BIC": 18.0, "best_fit_params": {"Om0": 0.29}, "log_likelihood": -5.5},
    }

    payload = _normalize_model_comparison(summary)
    delta = payload["delta"]

    assert payload["dataset"] == "pantheon+"
    assert payload["n_obs"] == 1701
    assert payload["source"] == "data/results/pantheon_fit_summary.json"
    assert payload["source_summary"].endswith("data/results/pantheon_fit_summary.json")
    assert payload["covariance_used"] is True
    assert payload["models"]["rll"]["k_params"] == 5
    assert payload["models"]["lcdm"]["k_params"] == 2
    assert payload["models"]["rll"]["log_likelihood"] == -5.0
    assert payload["models"]["lcdm"]["best_fit_params"] == {"Om0": 0.29}
    assert delta["delta_chi2_rll_minus_lcdm"] == -1.0
    assert delta["delta_aic_rll_minus_lcdm"] == 5.0
    assert delta["delta_bic_rll_minus_lcdm"] == 12.0
    assert delta["thresholds_used"] == {
        "aic_tentative": 2.0,
        "aic_strong": 10.0,
        "bic_tentative": 2.0,
        "bic_strong": 10.0,
        "chi2_improvement_min": 0.0,
    }
    assert delta["claim_boundary"] == "No superiority claim unless real-data metrics pass predefined thresholds."


def test_normalize_model_comparison_delta_null_when_metrics_absent() -> None:
    summary = {
        "n_obs": 1701,
        "rll": {"best_fit": {"Om0": 0.3}},
        "lcdm": {"best_fit": {"Om0": 0.29}},
    }
    payload = _normalize_model_comparison(summary)
    assert payload["delta"]["delta_chi2_rll_minus_lcdm"] is None
    assert payload["delta"]["delta_aic_rll_minus_lcdm"] is None
    assert payload["delta"]["delta_bic_rll_minus_lcdm"] is None
    assert payload["delta"]["interpretation_label"] == "inconclusive"
