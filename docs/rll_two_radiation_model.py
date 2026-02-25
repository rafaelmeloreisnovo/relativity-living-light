"""
rll_two_radiation_model.py

Implementação mínima e reproduzível do modelo de dois níveis de radiação:
1) Radiação cosmológica homogênea: Ωr em H(z).
2) Radiação ativa astrofísica (AGN/quasares): modulação em crescimento fσ8.

Uso:
    python docs/rll_two_radiation_model.py
"""

from __future__ import annotations

from dataclasses import dataclass
from math import exp, sqrt
from pathlib import Path
import csv


REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_HZ = REPO_ROOT / "data" / "real" / "Hz_data_real.csv"
OUT_CSV = REPO_ROOT / "results" / "two_radiation_model_preview.csv"


@dataclass(frozen=True)
class BackgroundParams:
    H0: float = 67.4
    omega_m: float = 0.315
    omega_r: float = 9.0e-5
    omega_lambda: float = 0.685
    omega_k: float = 0.0


@dataclass(frozen=True)
class FeedbackParams:
    amplitude: float = 0.18
    z_peak: float = 2.2
    z_cut: float = 5.5
    alpha: float = 2.0
    beta: float = 2.6
    suppression: float = 0.22


# Pivô simples de crescimento usado como baseline analítico para preview rápido.
def fs8_baseline(z: float, sigma8_0: float = 0.811, gamma: float = 0.55) -> float:
    omz = 0.315 * (1.0 + z) ** 3 / (
        0.315 * (1.0 + z) ** 3 + 0.685 + 9.0e-5 * (1.0 + z) ** 4
    )
    growth_rate = omz ** gamma
    growth_amp = 1.0 / (1.0 + z)
    return growth_rate * sigma8_0 * growth_amp


def e2_background(z: float, p: BackgroundParams) -> float:
    return (
        p.omega_m * (1.0 + z) ** 3
        + p.omega_r * (1.0 + z) ** 4
        + p.omega_lambda
        + p.omega_k * (1.0 + z) ** 2
    )


def h_of_z(z: float, p: BackgroundParams) -> float:
    return p.H0 * sqrt(e2_background(z, p))


def feedback_window(z: float, f: FeedbackParams) -> float:
    x = (1.0 + z) / (1.0 + f.z_peak)
    xc = (1.0 + z) / (1.0 + f.z_cut)
    return f.amplitude * (x ** f.alpha) * exp(-(xc ** f.beta))


def fs8_with_feedback(z: float, f: FeedbackParams) -> float:
    base = fs8_baseline(z)
    window = feedback_window(z, f)
    factor = 1.0 - f.suppression * window
    return base * factor


def read_hz_points(path: Path) -> list[tuple[float, float]]:
    rows: list[tuple[float, float]] = []
    with path.open("r", encoding="utf-8") as f:
        rd = csv.DictReader(f)
        for row in rd:
            z = float(row["z"])
            hz = float(row["H_obs"])
            rows.append((z, hz))
    return rows


def build_preview_table() -> list[dict[str, float]]:
    bg = BackgroundParams()
    fb = FeedbackParams()
    hz_points = read_hz_points(DATA_HZ)

    table: list[dict[str, float]] = []
    for z, hz_obs in hz_points:
        hz_model = h_of_z(z, bg)
        fs8_std = fs8_baseline(z)
        fs8_fb = fs8_with_feedback(z, fb)
        table.append(
            {
                "z": round(z, 6),
                "H_obs": round(hz_obs, 6),
                "H_model": round(hz_model, 6),
                "delta_H": round(hz_model - hz_obs, 6),
                "fs8_baseline": round(fs8_std, 6),
                "fs8_feedback": round(fs8_fb, 6),
                "delta_fs8_pct": round(100.0 * (fs8_fb - fs8_std) / fs8_std, 6),
            }
        )
    return table


def write_preview_csv(rows: list[dict[str, float]], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "z",
        "H_obs",
        "H_model",
        "delta_H",
        "fs8_baseline",
        "fs8_feedback",
        "delta_fs8_pct",
    ]
    with out_path.open("w", encoding="utf-8", newline="") as f:
        wr = csv.DictWriter(f, fieldnames=fields)
        wr.writeheader()
        wr.writerows(rows)


def main() -> None:
    rows = build_preview_table()
    write_preview_csv(rows, OUT_CSV)

    print("Modelo de duas radiações executado.")
    print(f"Amostras processadas: {len(rows)}")
    print(f"Saída: {OUT_CSV.relative_to(REPO_ROOT)}")
    if rows:
        print("Primeira linha:")
        print(rows[0])


if __name__ == "__main__":
    main()
