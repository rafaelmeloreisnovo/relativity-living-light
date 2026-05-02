from pathlib import Path

import numpy as np
import pandas as pd

from rll.ln1pz_extractor import run_catalog_extraction


def test_ln1pz_extractor_recovers_frequency(tmp_path: Path):
    rng = np.random.default_rng(7)
    z = np.linspace(0.1, 6.0, 500)
    ln1pz = np.log1p(z)

    true_a = 0.02
    true_w = 0.91
    true_phi = 0.4

    pk_baseline = 1_000.0 * np.exp(-z / 3.0)
    residual = true_a * np.cos(true_w * ln1pz + true_phi)
    noisy_residual = residual + rng.normal(0.0, 0.0015, size=z.size)
    pk_obs = pk_baseline * (1.0 + noisy_residual)

    in_csv = tmp_path / "catalog.csv"
    out_csv = tmp_path / "residuals.csv"
    pd.DataFrame({"z": z, "pk_obs": pk_obs, "pk_baseline": pk_baseline}).to_csv(in_csv, index=False)

    fit = run_catalog_extraction(in_csv, out_csv)

    assert abs(fit.omega - true_w) < 0.12
    assert abs(fit.amplitude - true_a) < 0.01
    assert fit.rmse < 0.005
    assert out_csv.exists()
