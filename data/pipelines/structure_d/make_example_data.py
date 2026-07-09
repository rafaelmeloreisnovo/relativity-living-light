"""Referência explícita de saídas textuais deste módulo/pipeline."""

TEXTUAL_OUTPUTS = [
    'data/inputs/structure_d/Hz.csv',
    'data/inputs/structure_d/fsigma8.csv',
    'data/synthetic/structure_d/Hz_cov.csv',
    'data/synthetic/structure_d/Hz_cov_matrix.csv',
    'data/synthetic/structure_d/fsigma8_cov.csv',
    'data/synthetic/structure_d/fsigma8_cov_matrix.csv',
    'data/synthetic/structure_d/mock_data_contract.json',
    'data/inputs/structure_d/mock_data_contract.json',
]

import argparse
import json
import os
import shutil
from datetime import datetime, timezone

import numpy as np
import pandas as pd

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
DATA = os.path.join(BASE_DIR, "data", "inputs", "structure_d")
SYNTHETIC_DATA = os.path.join(BASE_DIR, "data", "synthetic", "structure_d")
CONTRACT_RELATIVE_PATH = "data/synthetic/structure_d/mock_data_contract.json"
LEGACY_CONTRACT_RELATIVE_PATH = "data/inputs/structure_d/mock_data_contract.json"


def write_csv_checked(df, output_path):
    try:
        df.to_csv(output_path, index=False)
    except OSError as exc:
        raise OSError(f"Falha ao escrever arquivo CSV: {output_path}") from exc

    if (not os.path.exists(output_path)) or os.path.getsize(output_path) <= 0:
        raise RuntimeError(
            f"Arquivo CSV inválido após escrita (ausente ou vazio): {output_path}"
        )

def _write_covariance_products(z_values, values, sigma_values, csv_name, matrix_name):
    n_points = len(z_values)
    corr = np.eye(n_points)
    for i in range(n_points):
        if i + 1 < n_points:
            corr[i, i + 1] = 0.12
            corr[i + 1, i] = 0.12
        if i + 2 < n_points:
            corr[i, i + 2] = 0.05
            corr[i + 2, i] = 0.05

    sigma_diag = np.diag(sigma_values)
    covariance = sigma_diag @ corr @ sigma_diag

    os.makedirs(SYNTHETIC_DATA, exist_ok=True)
    csv_df = pd.DataFrame({"z": z_values, values.name: values.to_numpy(dtype=float)})
    write_csv_checked(csv_df, os.path.join(SYNTHETIC_DATA, csv_name))
    np.savetxt(os.path.join(SYNTHETIC_DATA, matrix_name), covariance, delimiter=",", fmt="%.10g")

    # Temporary compatibility aliases for older tests/scripts that still read data/inputs/structure_d.
    write_csv_checked(csv_df, os.path.join(DATA, csv_name))
    np.savetxt(os.path.join(DATA, matrix_name), covariance, delimiter=",", fmt="%.10g")


def main(seed=42, generate_covariance=False):
    os.makedirs(DATA, exist_ok=True)
    rng = np.random.default_rng(seed)

    z_hz = np.array([0.1, 0.2, 0.4, 0.6, 0.8, 1.0, 1.5, 2.0])
    hz_true = 70.0 * np.sqrt(0.3 * (1 + z_hz) ** 3 + 0.7)
    sig_hz = 3.0 + 2.0 * rng.random(len(z_hz))
    Hz_obs = hz_true + rng.normal(0, sig_hz)
    hz_df = pd.DataFrame({"z": z_hz, "Hz": Hz_obs, "sigma": sig_hz})
    write_csv_checked(hz_df, os.path.join(DATA, "Hz.csv"))

    z_fs = np.array([0.1, 0.3, 0.5, 0.8, 1.0, 1.5, 2.0])
    omz = (0.3 * (1 + z_fs) ** 3) / (0.3 * (1 + z_fs) ** 3 + 0.7)
    fs8_true = (omz ** 0.55) * 0.8
    sig_fs = 0.03 + 0.03 * rng.random(len(z_fs))
    fs8_obs = fs8_true + rng.normal(0, sig_fs)
    fs_df = pd.DataFrame({"z": z_fs, "fs8": fs8_obs, "sigma": sig_fs})
    write_csv_checked(fs_df, os.path.join(DATA, "fsigma8.csv"))

    if generate_covariance:
        _write_covariance_products(
            z_hz,
            hz_df["Hz"],
            hz_df["sigma"],
            csv_name="Hz_cov.csv",
            matrix_name="Hz_cov_matrix.csv",
        )
        _write_covariance_products(
            z_fs,
            fs_df["fs8"],
            fs_df["sigma"],
            csv_name="fsigma8_cov.csv",
            matrix_name="fsigma8_cov_matrix.csv",
        )

    metadata = {
        "seed": int(seed),
        "generated_at_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "generated_covariance": bool(generate_covariance),
        "datasets": {
            "Hz.csv": {
                "z_range": [float(np.min(z_hz)), float(np.max(z_hz))],
                "sigma_range": [float(np.min(sig_hz)), float(np.max(sig_hz))],
                "rows": int(len(z_hz)),
            },
            "fsigma8.csv": {
                "z_range": [float(np.min(z_fs)), float(np.max(z_fs))],
                "sigma_range": [float(np.min(sig_fs)), float(np.max(sig_fs))],
                "rows": int(len(z_fs)),
            },
        },
        "covariance_generated": bool(generate_covariance),
    }

    os.makedirs(SYNTHETIC_DATA, exist_ok=True)
    contract_path = os.path.join(SYNTHETIC_DATA, "mock_data_contract.json")
    with open(contract_path, "w", encoding="utf-8") as fp:
        json.dump(metadata, fp, ensure_ascii=False, indent=2)

    legacy_contract_path = os.path.join(DATA, "mock_data_contract.json")
    shutil.copy2(contract_path, legacy_contract_path)

    outputs = [
        "data/inputs/structure_d/Hz.csv",
        "data/inputs/structure_d/fsigma8.csv",
        CONTRACT_RELATIVE_PATH,
        LEGACY_CONTRACT_RELATIVE_PATH,
    ]
    if generate_covariance:
        outputs.extend(
            [
                "data/synthetic/structure_d/Hz_cov.csv",
                "data/synthetic/structure_d/Hz_cov_matrix.csv",
                "data/synthetic/structure_d/fsigma8_cov.csv",
                "data/synthetic/structure_d/fsigma8_cov_matrix.csv",
            ]
        )
    print("Example data written: " + ", ".join(outputs))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate synthetic Structure-D example datasets.")
    parser.add_argument("--seed", type=int, default=42, help="RNG seed for reproducible mock generation.")
    parser.set_defaults(generate_covariance=True)
    parser.add_argument(
        "--with-covariance",
        dest="generate_covariance",
        action="store_true",
        help="Generate synthetic covariance matrices and CSVs compatible with error_model='covariance' (default).",
    )
    parser.add_argument(
        "--without-covariance",
        dest="generate_covariance",
        action="store_false",
        help="Disable covariance artifact generation.",
    )
    args = parser.parse_args()
    main(seed=args.seed, generate_covariance=args.generate_covariance)
