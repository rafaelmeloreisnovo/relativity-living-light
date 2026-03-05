"""Referência explícita de saídas textuais deste módulo/pipeline."""

TEXTUAL_OUTPUTS = [
    'data/inputs/structure_d/Hz.csv',
    'data/inputs/structure_d/fsigma8.csv',
    'data/inputs/structure_d/Hz_cov.csv',
    'data/inputs/structure_d/Hz_cov_matrix.csv',
    'data/inputs/structure_d/fsigma8_cov.csv',
    'data/inputs/structure_d/fsigma8_cov_matrix.csv',
    'data/inputs/structure_d/mock_data_contract.json',
]

import argparse
import json
import os
from datetime import datetime, timezone

import numpy as np
import pandas as pd

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
DATA = os.path.join(BASE_DIR, "data", "inputs", "structure_d")


def write_csv_checked(df, output_path):
    try:
        df.to_csv(output_path, index=False)
    except OSError as exc:
        raise OSError(f"Falha ao escrever arquivo CSV: {output_path}") from exc

    if (not os.path.exists(output_path)) or os.path.getsize(output_path) <= 0:
        raise RuntimeError(
            f"Arquivo CSV inválido após escrita (ausente ou vazio): {output_path}"
        )


def write_matrix_checked(matrix, output_path):
    np.savetxt(output_path, matrix, delimiter=",")
    if (not os.path.exists(output_path)) or os.path.getsize(output_path) <= 0:
        raise RuntimeError(
            f"Arquivo de matriz inválido após escrita (ausente ou vazio): {output_path}"
        )


def _correlated_covariance(sigmas, corr=0.2):
    sigmas = np.asarray(sigmas, dtype=float)
    n = sigmas.size
    corr_m = np.full((n, n), corr, dtype=float)
    np.fill_diagonal(corr_m, 1.0)
    cov = np.outer(sigmas, sigmas) * corr_m
    return cov


def main(seed=42, generate_covariance=True):
    os.makedirs(DATA, exist_ok=True)
    rng = np.random.default_rng(seed)

    z_hz = np.array([0.1, 0.2, 0.4, 0.6, 0.8, 1.0, 1.5, 2.0])
    hz_true = 70.0 * np.sqrt(0.3 * (1 + z_hz) ** 3 + 0.7)
    sig_hz = 3.0 + 2.0 * rng.random(len(z_hz))
    hz_obs = hz_true + rng.normal(0, sig_hz)

    write_csv_checked(
        pd.DataFrame({"z": z_hz, "Hz": hz_obs, "sigma": sig_hz}),
        os.path.join(DATA, "Hz.csv"),
    )

    z_fs = np.array([0.1, 0.3, 0.5, 0.8, 1.0, 1.5, 2.0])
    omz = (0.3 * (1 + z_fs) ** 3) / (0.3 * (1 + z_fs) ** 3 + 0.7)
    fs8_true = (omz ** 0.55) * 0.8
    sig_fs = 0.03 + 0.03 * rng.random(len(z_fs))
    fs8_obs = fs8_true + rng.normal(0, sig_fs)

    write_csv_checked(
        pd.DataFrame({"z": z_fs, "fs8": fs8_obs, "sigma": sig_fs}),
        os.path.join(DATA, "fsigma8.csv"),
    )

    if generate_covariance:
        write_csv_checked(
            pd.DataFrame({"z": z_hz, "Hz": hz_obs}),
            os.path.join(DATA, "Hz_cov.csv"),
        )
        write_csv_checked(
            pd.DataFrame({"z": z_fs, "fs8": fs8_obs}),
            os.path.join(DATA, "fsigma8_cov.csv"),
        )
        write_matrix_checked(
            _correlated_covariance(sig_hz, corr=0.15),
            os.path.join(DATA, "Hz_cov_matrix.csv"),
        )
        write_matrix_checked(
            _correlated_covariance(sig_fs, corr=0.10),
            os.path.join(DATA, "fsigma8_cov_matrix.csv"),
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
    }
    contract_path = os.path.join(DATA, "mock_data_contract.json")
    with open(contract_path, "w", encoding="utf-8") as fp:
        json.dump(metadata, fp, ensure_ascii=False, indent=2)

    print(
        "Example data written: Hz.csv, fsigma8.csv, mock_data_contract.json"
        + (", Hz_cov.csv, Hz_cov_matrix.csv, fsigma8_cov.csv, fsigma8_cov_matrix.csv" if generate_covariance else "")
    )


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
    parser.add_argument(
        "--without-covariance",
        action="store_true",
        help="Disable covariance generation even if --with-covariance is present.",
    )
    args = parser.parse_args()
    generate_covariance = bool(args.with_covariance or not args.without_covariance)
    main(seed=args.seed, generate_covariance=generate_covariance)
