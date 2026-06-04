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


def test_rd_drag_is_derived_from_parameter_changes() -> None:
    baseline = joint.rd_drag_mpc(67.7, 0.31, 0.02236)
    shifted = joint.rd_drag_mpc(73.0, 0.31, 0.02236)

    assert np.isfinite(baseline)
    assert np.isfinite(shifted)
    assert baseline != shifted
