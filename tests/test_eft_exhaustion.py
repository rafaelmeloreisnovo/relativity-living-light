from __future__ import annotations

from pathlib import Path

from rll.eft_exhaustion import RLLParameters, TOKEN_VAZIO, e2_rll_a, run_exhaustion


def test_e2_rll_closes_to_unity_today() -> None:
    params = RLLParameters(alpha=0.02, k=8.0, a_t=0.6)
    assert abs(float(e2_rll_a(1.0, params)) - 1.0) < 1e-12


def test_exhaustion_emits_token_vazio_and_artifacts(tmp_path: Path) -> None:
    report = run_exhaustion(RLLParameters(alpha=0.01), tmp_path, n_grid=64)
    assert report["final_decision"] in {"REJEITADO COMO EFT", f"INCONCLUSIVO ({TOKEN_VAZIO})"}
    assert TOKEN_VAZIO in report["observational_validation"]["DESI DR2"]
    assert (tmp_path / "eft_reconstruction.csv").exists()
    assert (tmp_path / "eft_exhaustion_report.json").exists()
