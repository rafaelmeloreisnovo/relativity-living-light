from __future__ import annotations

import csv
from pathlib import Path

from rll.eft_exhaustion import (
    ArtifactInputs,
    RLLParameters,
    ScanConfig,
    TOKEN_VAZIO,
    e2_rll_a,
    load_observational_evidence,
    parameter_exhaustion_grid,
    run_exhaustion,
)

import numpy as np


def test_e2_rll_closes_to_unity_today() -> None:
    params = RLLParameters(alpha=0.02, k=8.0, a_t=0.6)
    assert abs(float(e2_rll_a(1.0, params)) - 1.0) < 1e-12


def test_exhaustion_emits_token_vazio_and_artifacts(tmp_path: Path) -> None:
    report = run_exhaustion(RLLParameters(alpha=0.01), tmp_path, n_grid=64)
    assert report["final_decision"] in {
        "REJEITADO COMO EFT",
        f"INCONCLUSIVO ({TOKEN_VAZIO})",
    }
    assert TOKEN_VAZIO in report["observational_validation"]["DESI DR2"]
    assert (tmp_path / "eft_reconstruction.csv").exists()
    assert (tmp_path / "eft_exhaustion_report.json").exists()
    assert (tmp_path / "eft_exhaustion_report.md").exists()
    assert (tmp_path / "parameter_scan.csv").exists()
    assert "finite_scan" in report["parameter_exhaustion"]


def test_observational_evidence_uses_materialized_model_comparison(
    tmp_path: Path,
) -> None:
    comparison = tmp_path / "model_comparison.csv"
    with comparison.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["model", "chi2_total", "aic", "bic"])
        writer.writeheader()
        writer.writerow({"model": "LCDM", "chi2_total": "10", "aic": "16", "bic": "20"})
        writer.writerow({"model": "RLL", "chi2_total": "9", "aic": "13", "bic": "18"})

    evidence = load_observational_evidence(
        ArtifactInputs(model_comparison_csv=comparison)
    )

    lcdm = evidence["model_comparison"]["RLL_vs_LCDM"]
    assert lcdm["delta_aic_rll_minus_baseline"] == -3.0
    assert lcdm["decision_by_delta_aic"] == "favorável"
    assert evidence["datasets"]["model_comparison_csv"] == "materialized"


def test_parameter_exhaustion_grid_records_finite_truncation() -> None:
    rows, summary = parameter_exhaustion_grid(
        RLLParameters(alpha=0.01),
        np.linspace(1.0e-3, 1.0, 16),
        ScanConfig(alpha_max=0.02, k_max=4.0, samples_per_axis=3),
    )

    assert len(rows) == 27
    assert summary["grid_points"] == 27
    assert summary["non_identifiable_points"] > 0
    assert TOKEN_VAZIO in summary["truncation_notice"]
