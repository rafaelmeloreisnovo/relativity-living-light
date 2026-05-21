from __future__ import annotations

from scripts.run_real_pantheon_validation import _normalize_model_comparison


def test_normalize_model_comparison_schema() -> None:
    summary = {
        "pipeline": "pantheon_oficial_prova_observacional",
        "n_obs": 1701,
        "rll": {"chi2": 10.0, "AIC": 20.0, "BIC": 30.0, "best_fit": {"Om0": 0.3}},
        "lcdm": {"chi2": 11.0, "AIC": 15.0, "BIC": 18.0, "best_fit": {"Om0": 0.29}},
    }

    payload = _normalize_model_comparison(summary)

    assert payload["n_obs"] == 1701
    assert payload["rll"]["n_params"] == 5
    assert payload["lcdm"]["n_params"] == 2
    assert payload["source_summary"].endswith("data/results/pantheon_fit_summary.json")
