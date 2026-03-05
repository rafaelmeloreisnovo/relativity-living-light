"""Referência explícita de saídas textuais deste módulo/pipeline."""

TEXTUAL_OUTPUTS = [
    "data/inputs/structure_d/Hz.csv",
    "data/inputs/structure_d/fsigma8.csv",
    "data/inputs/structure_d/Hz_cov.csv",
    "data/inputs/structure_d/Hz_cov_matrix.csv",
    "data/inputs/structure_d/fsigma8_cov.csv",
    "data/inputs/structure_d/fsigma8_cov_matrix.csv",
]

import argparse
import os
import numpy as np
import pandas as pd

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
DATA = os.path.join(BASE_DIR, "data", "inputs", "structure_d")


def _build_covariance(errors, rng, max_correlation=0.35):
    std = np.asarray(errors, dtype=float)
    dim = std.size
    corr_noise = rng.uniform(-max_correlation, max_correlation, size=(dim, dim))
    corr = (corr_noise + corr_noise.T) / 2.0
    np.fill_diagonal(corr, 1.0)
    cov = np.outer(std, std) * corr
    return cov


def main(seed=42, generate_covariance=False):
    os.makedirs(DATA, exist_ok=True)
    rng = np.random.default_rng(seed)

    z_hz = np.array([0.1, 0.2, 0.4, 0.6, 0.8, 1.0, 1.5, 2.0])
    Hz_true = 70.0 * np.sqrt(0.3 * (1 + z_hz) ** 3 + 0.7)
    sig_hz = 3.0 + 2.0 * rng.random(len(z_hz))
    Hz_obs = Hz_true + rng.normal(0, sig_hz)
    pd.DataFrame({"z": z_hz, "Hz": Hz_obs, "sigma": sig_hz}).to_csv(os.path.join(DATA, "Hz.csv"), index=False)

    z_fs = np.array([0.1, 0.3, 0.5, 0.8, 1.0, 1.5, 2.0])
    Omz = (0.3 * (1 + z_fs) ** 3) / (0.3 * (1 + z_fs) ** 3 + 0.7)
    fs8_true = (Omz ** 0.55) * 0.8
    sig_fs = 0.03 + 0.03 * rng.random(len(z_fs))
    fs8_obs = fs8_true + rng.normal(0, sig_fs)
    pd.DataFrame({"z": z_fs, "fs8": fs8_obs, "sigma": sig_fs}).to_csv(os.path.join(DATA, "fsigma8.csv"), index=False)

    if generate_covariance:
        hz_cov = _build_covariance(sig_hz, rng)
        fs8_cov = _build_covariance(sig_fs, rng)

        pd.DataFrame({"z": z_hz, "Hz": Hz_obs}).to_csv(os.path.join(DATA, "Hz_cov.csv"), index=False)
        np.savetxt(os.path.join(DATA, "Hz_cov_matrix.csv"), hz_cov, delimiter=",")

        pd.DataFrame({"z": z_fs, "fs8": fs8_obs}).to_csv(os.path.join(DATA, "fsigma8_cov.csv"), index=False)
        np.savetxt(os.path.join(DATA, "fsigma8_cov_matrix.csv"), fs8_cov, delimiter=",")

    print("Example data written: data/inputs/structure_d/Hz.csv, data/inputs/structure_d/fsigma8.csv")
    if generate_covariance:
        print(
            "Covariance-mode data written: "
            "data/inputs/structure_d/Hz_cov.csv, "
            "data/inputs/structure_d/Hz_cov_matrix.csv, "
            "data/inputs/structure_d/fsigma8_cov.csv, "
            "data/inputs/structure_d/fsigma8_cov_matrix.csv"
        )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate synthetic Structure-D example datasets.")
    parser.add_argument("--seed", type=int, default=42, help="RNG seed for reproducible mock generation.")
    parser.add_argument(
        "--with-covariance",
        action="store_true",
        help="Also generate synthetic covariance matrices and CSVs compatible with error_model='covariance'.",
    )
    args = parser.parse_args()
    main(seed=args.seed, generate_covariance=args.with_covariance)
