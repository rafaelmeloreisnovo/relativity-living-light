"""Formal RLL EFT exhaustion engine.

This module is intentionally conservative: it computes only quantities that
follow from the supplied expansion history and emits TOKEN_VAZIO when a
fundamental EFT, perturbation coefficient, or observational datum is not
available in the repository.  It is a falsification/audit engine, not a claim
factory.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

import numpy as np

TOKEN_VAZIO = "TOKEN_VAZIO"


@dataclass(frozen=True)
class RLLParameters:
    omega_m: float = 0.315
    omega_r: float = 9.0e-5
    omega_lambda: float | None = None
    alpha: float = 0.0
    k: float = 10.0
    a_t: float = 0.5

    @property
    def omega_lambda_closure(self) -> float:
        if self.omega_lambda is not None:
            return float(self.omega_lambda)
        return 1.0 - float(self.omega_m) - float(self.omega_r) - float(self.alpha) * float(s_transition(1.0, self.k, self.a_t))


def s_transition(a: float | np.ndarray, k: float, a_t: float) -> np.ndarray:
    a_arr = np.asarray(a, dtype=float)
    return 1.0 / (1.0 + np.exp(np.clip(-float(k) * (a_arr - float(a_t)), -700.0, 700.0)))


def e2_rll_a(a: float | np.ndarray, params: RLLParameters) -> np.ndarray:
    a_arr = np.asarray(a, dtype=float)
    # Required input gives alpha f(a) S(a) but does not define f(a).  The only
    # non-invented default is f(a)=1; custom f(a) must be supplied by another
    # validated implementation before stronger claims are allowed.
    return (
        params.omega_m * a_arr ** -3
        + params.omega_r * a_arr ** -4
        + params.omega_lambda_closure
        + params.alpha * s_transition(a_arr, params.k, params.a_t)
    )


def numerical_d_e2_da(a: np.ndarray, params: RLLParameters) -> np.ndarray:
    e2 = e2_rll_a(a, params)
    return np.gradient(e2, a, edge_order=2)


def canonical_scalar_reconstruction(a: np.ndarray, params: RLLParameters) -> dict[str, object]:
    """Reconstruct V(a) and phi(a) when canonical scalar inequalities permit it.

    Units set M_p=H0=1.  For a flat FLRW canonical scalar,
    phi_dot^2 = -2 dot(H) - rho_m - 4 rho_r/3.  Negative kinetic density proves
    this canonical reconstruction is impossible for that grid point.
    """

    e2 = e2_rll_a(a, params)
    d_e2_da = numerical_d_e2_da(a, params)
    kinetic = -(a / 3.0) * d_e2_da - params.omega_m * a ** -3 - (4.0 / 3.0) * params.omega_r * a ** -4
    scalar_rho = e2 - params.omega_m * a ** -3 - params.omega_r * a ** -4
    potential = scalar_rho - 0.5 * kinetic
    valid = bool(np.all(np.isfinite(kinetic)) and np.all(kinetic >= -1.0e-10) and np.all(np.isfinite(potential)))
    phi = np.full_like(a, np.nan)
    if valid:
        integrand = np.sqrt(np.maximum(kinetic, 0.0) / np.maximum(e2, 1.0e-300)) / a
        phi[0] = 0.0
        phi[1:] = np.cumsum(0.5 * (integrand[1:] + integrand[:-1]) * np.diff(a))
    return {
        "valid_canonical_reconstruction": valid,
        "reason": "canonical V(phi) reconstruction computed" if valid else f"{TOKEN_VAZIO}: canonical kinetic density becomes negative; no derived canonical EFT proof",
        "a": a,
        "e2": e2,
        "kinetic": kinetic,
        "potential": potential,
        "phi": phi,
    }


def perturbation_stability(reconstruction: dict[str, object]) -> dict[str, object]:
    valid = bool(reconstruction["valid_canonical_reconstruction"])
    if not valid:
        return {"Q_s": TOKEN_VAZIO, "c_s2": TOKEN_VAZIO, "stable": False, "decision": "REJEITADO COMO EFT"}
    kinetic = np.asarray(reconstruction["kinetic"], dtype=float)
    qs_ok = bool(np.all(kinetic > 0.0))
    cs2 = 1.0
    return {"Q_s_min": float(np.min(kinetic)), "c_s2": cs2, "stable": qs_ok and 0.0 < cs2 <= 1.0, "decision": "stable_canonical_sector" if qs_ok else "REJEITADO COMO EFT"}


def information_criteria(chi2: float, n_params: int, n_data: int) -> dict[str, float]:
    return {"chi2": float(chi2), "aic": float(chi2 + 2 * n_params), "bic": float(chi2 + n_params * np.log(max(n_data, 1)))}


def identifiability_scan(alpha_values: Iterable[float], k_values: Iterable[float], at_values: Iterable[float]) -> dict[str, object]:
    grid = [(a, k, at) for a in alpha_values for k in k_values for at in at_values]
    non_identifiable = any(k == 0.0 for _, k, _ in grid) or any(a == 0.0 for a, _, _ in grid)
    return {
        "grid_points": len(grid),
        "non_identifiable": bool(non_identifiable),
        "reason": f"{TOKEN_VAZIO}: parâmetros não identificáveis em alpha=0 ou k=0" if non_identifiable else "finite grid has distinguishable transition amplitudes",
    }


def run_exhaustion(params: RLLParameters, out_dir: Path, n_grid: int = 256) -> dict[str, object]:
    out_dir.mkdir(parents=True, exist_ok=True)
    a = np.linspace(1.0e-3, 1.0, n_grid)
    reconstruction = canonical_scalar_reconstruction(a, params)
    stability = perturbation_stability(reconstruction)
    ident = identifiability_scan([0.0, params.alpha], [0.0, params.k], [0.0, params.a_t, 1.0])

    csv_path = out_dir / "eft_reconstruction.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=["a", "E2", "kinetic", "potential", "phi"])
        writer.writeheader()
        for row in zip(reconstruction["a"], reconstruction["e2"], reconstruction["kinetic"], reconstruction["potential"], reconstruction["phi"]):
            writer.writerow({"a": row[0], "E2": row[1], "kinetic": row[2], "potential": row[3], "phi": row[4]})

    observational = {
        "DESI DR2": TOKEN_VAZIO,
        "Pantheon+": TOKEN_VAZIO,
        "Planck 2018": TOKEN_VAZIO,
        "BAO": TOKEN_VAZIO,
        "SN Ia": TOKEN_VAZIO,
        "reason": f"{TOKEN_VAZIO}: this command does not fabricate or download missing likelihood data; use existing real-data pipelines when materialized",
    }
    decision = "REJEITADO COMO EFT" if not stability["stable"] else "INCONCLUSIVO (TOKEN_VAZIO)"
    report = {
        "parameters": asdict(params),
        "background": {"equation": "E^2(a)=Omega_m a^-3+Omega_r a^-4+Omega_Lambda+alpha S(a)", "omega_total_a1": float(e2_rll_a(1.0, params))},
        "eft_reconstruction": {"valid": reconstruction["valid_canonical_reconstruction"], "reason": reconstruction["reason"]},
        "stability_eft": stability,
        "observational_validation": observational,
        "model_comparison": {"RLL_vs_LCDM": TOKEN_VAZIO, "RLL_vs_w0waCDM": TOKEN_VAZIO},
        "parameter_exhaustion": ident,
        "final_decision": decision,
        "artifacts": {"reconstruction_csv": str(csv_path)},
    }
    report_path = out_dir / "eft_exhaustion_report.json"
    report_path.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run conservative RLL EFT exhaustion/falsification engine")
    parser.add_argument("--out-dir", type=Path, default=Path("validacao_real/results/eft_exhaustion"))
    parser.add_argument("--omega-m", type=float, default=0.315)
    parser.add_argument("--omega-r", type=float, default=9.0e-5)
    parser.add_argument("--omega-lambda", type=float, default=None)
    parser.add_argument("--alpha", type=float, default=0.0)
    parser.add_argument("--k", type=float, default=10.0)
    parser.add_argument("--a-t", type=float, default=0.5)
    parser.add_argument("--grid", type=int, default=256)
    args = parser.parse_args(argv)
    report = run_exhaustion(RLLParameters(args.omega_m, args.omega_r, args.omega_lambda, args.alpha, args.k, args.a_t), args.out_dir, args.grid)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
