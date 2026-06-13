from __future__ import annotations

import numpy as np

from scripts.analysis import structure_d_effective_dynamics as dyn


def test_lcdm_effective_dark_density_has_constant_w_minus_one() -> None:
    z = np.linspace(0.0, 2.0, 101)
    e2 = 0.3 * (1.0 + z) ** 3 + dyn.joint.ORAD * (1.0 + z) ** 4 + 0.7

    rho_eff = dyn.effective_dark_density(e2, z, om=0.3)
    w_eff = dyn.w_eff_from_density(rho_eff, z)

    assert np.allclose(rho_eff, 0.7)
    assert np.allclose(w_eff, -1.0, atol=1.0e-10)


def test_q_from_e2_is_finite_for_lcdm_like_grid() -> None:
    z = np.linspace(0.0, 2.0, 101)
    e2 = 0.3 * (1.0 + z) ** 3 + dyn.joint.ORAD * (1.0 + z) ** 4 + 0.7

    q = dyn.q_from_e2(e2, z)

    assert np.all(np.isfinite(q))
    assert q[0] < 0.0
    assert q[-1] > 0.0


def test_comoving_distance_is_monotonic() -> None:
    z = np.linspace(0.0, 2.0, 101)
    e2 = 0.3 * (1.0 + z) ** 3 + dyn.joint.ORAD * (1.0 + z) ** 4 + 0.7

    dc = dyn.comoving_distance_mpc(e2, z, h0=70.0)

    assert dc[0] == 0.0
    assert np.all(np.diff(dc) > 0.0)


def test_safe_logit_is_monotonic_for_transition_fraction() -> None:
    z = np.linspace(0.0, 2.0, 101)
    f = dyn.joint.transition_f(z, zt=1.0, wt=0.2)
    logit = dyn._safe_logit(f)

    assert np.all(np.isfinite(logit))
    assert np.all(np.diff(logit) > 0.0)


def test_build_diagnostics_preserves_claim_boundary_semantics() -> None:
    payload = {
        "schema": "rll.joint_real_likelihood.v2",
        "claim_allowed": False,
        "rows": [
            {
                "model": dyn.joint.MODEL_LCDM,
                "H0": 70.0,
                "Om": 0.3,
                "OL": 0.7,
                "Ob_h2": 0.0224,
                "sigma8": 0.8,
            }
        ],
    }

    rows = dyn.build_diagnostics(payload, z_min=0.0, z_max=1.0, n_grid=11)

    assert len(rows) == 11
    assert rows[0]["model"] == dyn.joint.MODEL_LCDM
    assert rows[0]["D_C_Mpc"] == 0.0
    assert rows[0]["rll_transition_f"] is None
