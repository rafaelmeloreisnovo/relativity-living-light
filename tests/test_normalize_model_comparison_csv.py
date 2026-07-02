from __future__ import annotations

import csv
from pathlib import Path

from tools.normalize_model_comparison_csv import normalize_model_comparison_csv


def _read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def test_normalize_model_comparison_adds_eft_alias_columns(tmp_path: Path) -> None:
    path = tmp_path / "model_comparison.csv"
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=["model", "chi2", "n_real_points", "k_params", "AIC", "BIC", "data_status"],
        )
        writer.writeheader()
        writer.writerow({"model": "LCDM", "chi2": "10.0", "n_real_points": "4", "k_params": "2", "AIC": "14.0", "BIC": "15.0", "data_status": "real_non_synthetic"})
        writer.writerow({"model": "RLL", "chi2": "9.0", "n_real_points": "4", "k_params": "5", "AIC": "19.0", "BIC": "22.0", "data_status": "real_non_synthetic"})

    summary = normalize_model_comparison_csv(path)
    rows = _read_rows(path)

    assert summary["added_columns"] == ["aic", "bic", "chi2_total"]
    assert rows[0]["AIC"] == "14.0"
    assert rows[0]["aic"] == "14.0"
    assert rows[0]["BIC"] == "15.0"
    assert rows[0]["bic"] == "15.0"
    assert rows[0]["chi2"] == "10.0"
    assert rows[0]["chi2_total"] == "10.0"
    assert rows[1]["aic"] == "19.0"
    assert rows[1]["bic"] == "22.0"


def test_normalize_model_comparison_preserves_existing_lowercase_values(tmp_path: Path) -> None:
    path = tmp_path / "model_comparison.csv"
    with path.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["model", "AIC", "aic", "BIC", "bic", "chi2", "chi2_total"])
        writer.writeheader()
        writer.writerow({"model": "RLL", "AIC": "19.0", "aic": "18.5", "BIC": "22.0", "bic": "21.5", "chi2": "9.0", "chi2_total": "8.5"})

    normalize_model_comparison_csv(path)
    row = _read_rows(path)[0]

    assert row["aic"] == "18.5"
    assert row["bic"] == "21.5"
    assert row["chi2_total"] == "8.5"
