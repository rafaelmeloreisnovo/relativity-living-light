from __future__ import annotations

import numpy as np
import pandas as pd

from data.pipelines.structure_d import joint_real_likelihood as joint


def test_desi_covariance_materializes_committed_dm_dh_blocks() -> None:
    points = pd.read_csv(joint.DESI_POINTS_PATH)
    summary = pd.read_csv(joint.DESI_COV_SUMMARY_PATH)

    cov = joint.build_desi_covariance(points, summary)

    assert cov.shape == (13, 13)
    assert np.allclose(np.diag(cov), points["sigma"].astype(float).to_numpy() ** 2)
    lrg1 = points.index[points["covariance_block"] == "DESI_DR2_LRG1_DM_DH"].tolist()
    assert len(lrg1) == 2
    assert cov[lrg1[0], lrg1[1]] == cov[lrg1[1], lrg1[0]]
    assert cov[lrg1[0], lrg1[1]] < 0.0


def test_joint_evaluation_uses_all_four_real_axes() -> None:
    inputs = joint.load_joint_inputs()
    vector = np.array([67.7, 0.31, 0.69, 0.0224, 0.8], dtype=float)

    components = joint.evaluate_components(joint.MODEL_LCDM, vector, inputs)

    assert set(components) == {"Hz", "DESI_DR2_BAO", "fsigma8", "CMB_shift", "total"}
    assert components["total"] == components["Hz"] + components["DESI_DR2_BAO"] + components["fsigma8"] + components["CMB_shift"]
    assert np.isfinite(components["total"])


def test_joint_real_models_include_wcdm_and_cpl_on_same_inputs() -> None:
    inputs = joint.load_joint_inputs()
    wcdm_vector = np.array([67.7, 0.31, 0.69, -1.0, 0.0224, 0.8], dtype=float)
    cpl_vector = np.array([67.7, 0.31, 0.69, -1.0, 0.0, 0.0224, 0.8], dtype=float)

    wcdm_components = joint.evaluate_components(joint.MODEL_WCDM, wcdm_vector, inputs)
    cpl_components = joint.evaluate_components(joint.MODEL_CPL, cpl_vector, inputs)

    assert np.isfinite(wcdm_components["total"])
    assert np.isfinite(cpl_components["total"])
    assert joint.MODEL_PARAM_NAMES[joint.MODEL_WCDM] == ("H0", "Om", "OL", "w", "Ob_h2", "sigma8")
    assert joint.MODEL_PARAM_NAMES[joint.MODEL_CPL] == ("H0", "Om", "OL", "w0", "wa", "Ob_h2", "sigma8")


def test_joint_inputs_require_parameter_registry_and_covariance_readiness() -> None:
    inputs = joint.load_joint_inputs()

    assert inputs["parameter_registry"]["schema"] == "rll.parameter_origin_registry.v1"
    assert inputs["desi_covariance_info"]["ready"] is True
    assert inputs["desi_covariance_info"]["mode"] in {"official_full", "block_summary"}


def test_rd_drag_is_derived_from_parameter_changes() -> None:
    baseline = joint.rd_drag_mpc(67.7, 0.31, 0.02236)
    shifted = joint.rd_drag_mpc(73.0, 0.31, 0.02236)

    assert np.isfinite(baseline)
    assert np.isfinite(shifted)
    assert baseline != shifted


def test_committed_joint_real_json_exposes_dataset_type_claim_boundary_and_fnext() -> None:
    import json
    from pathlib import Path

    payload = json.loads(Path("results/structure_d/joint_real_likelihood.json").read_text(encoding="utf-8"))
    assert payload["dataset_type"] == "real_observational"
    assert payload["claim_boundary"] == "No superiority claim unless real-data metrics pass predefined thresholds."
    assert payload["claim_allowed"] is False
    assert payload["publication_language"] == "RLL is a candidate effective dynamic-transition cosmology under real-data evaluation."
    assert payload["fnext"]["status"] == "not_measured"
    assert payload["fnext"]["F_gap"] is None
    assert payload["fnext"]["score"] is None
    assert payload["fnext"]["claim_allowed"] is False
    assert not any("synthetic" in value or "fixtures" in value for value in payload["datasets"].values())
