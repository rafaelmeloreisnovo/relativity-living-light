from __future__ import annotations

import json
import math
from pathlib import Path

from data.pipelines.structure_d.synthetic_real_boundary import CLAIM_BOUNDARY, INTERPRETATION_LABELS


def test_model_comparison_artifact_contract() -> None:
    payload = json.loads(Path("data/results/model_comparison.json").read_text(encoding="utf-8"))
    assert payload["dataset_type"] == "real_observational"
    assert payload["claim_boundary"] == CLAIM_BOUNDARY
    assert payload["k_rll"] == 5
    assert payload["k_lcdm"] == 2
    assert payload["AIC_rll"] == payload["chi2_rll"] + 2 * payload["k_rll"]
    assert payload["AIC_lcdm"] == payload["chi2_lcdm"] + 2 * payload["k_lcdm"]
    assert payload["BIC_rll"] == payload["chi2_rll"] + payload["k_rll"] * math.log(payload["n_obs"])
    assert payload["BIC_lcdm"] == payload["chi2_lcdm"] + payload["k_lcdm"] * math.log(payload["n_obs"])
    assert payload["delta_chi2_rll_minus_lcdm"] == payload["chi2_rll"] - payload["chi2_lcdm"]
    assert payload["delta_aic_rll_minus_lcdm"] == payload["AIC_rll"] - payload["AIC_lcdm"]
    assert payload["delta_bic_rll_minus_lcdm"] == payload["BIC_rll"] - payload["BIC_lcdm"]
    assert payload["interpretation_label"] in INTERPRETATION_LABELS
    assert payload["claim_allowed"] is False
    assert all(item["dataset_type"] == "real_observational" for item in payload["inputs"])
