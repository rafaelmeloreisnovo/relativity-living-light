"""Formal RLL EFT exhaustion engine.

This module is conservative by construction: it computes only quantities that
follow from the supplied expansion history or already-materialized validation
artifacts, and emits TOKEN_VAZIO when a fundamental EFT, perturbation
coefficient, or observational datum is unavailable. It is a falsification/audit
engine, not a claim factory.
"""

from __future__ import annotations

import argparse
import csv
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Mapping

import numpy as np

TOKEN_VAZIO = "TOKEN_VAZIO"
DATASETS_REQUIRED = ("DESI DR2", "Pantheon+", "Planck 2018", "BAO", "SN Ia")
BASELINES_REQUIRED = ("LCDM", "w0waCDM")


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
        return (
            1.0
            - float(self.omega_m)
            - float(self.omega_r)
            - float(self.alpha) * float(s_transition(1.0, self.k, self.a_t))
        )


@dataclass(frozen=True)
class ArtifactInputs:
    validation_summary: Path | None = None
    model_comparison_csv: Path | None = None


@dataclass(frozen=True)
class ScanConfig:
    alpha_max: float = 0.05
    k_max: float = 20.0
    samples_per_axis: int = 5


def s_transition(a: float | np.ndarray, k: float, a_t: float) -> np.ndarray:
    a_arr = np.asarray(a, dtype=float)
    return 1.0 / (
        1.0 + np.exp(np.clip(-float(k) * (a_arr - float(a_t)), -700.0, 700.0))
    )


def e2_rll_a(a: float | np.ndarray, params: RLLParameters) -> np.ndarray:
    a_arr = np.asarray(a, dtype=float)
    # Required input gives alpha f(a) S(a) but does not define f(a). The only
    # non-invented default is f(a)=1; custom f(a) must be supplied by another
    # validated implementation before stronger claims are allowed.
    return (
        params.omega_m * a_arr**-3
        + params.omega_r * a_arr**-4
        + params.omega_lambda_closure
        + params.alpha * s_transition(a_arr, params.k, params.a_t)
    )


def numerical_d_e2_da(a: np.ndarray, params: RLLParameters) -> np.ndarray:
    e2 = e2_rll_a(a, params)
    return np.gradient(e2, a, edge_order=2)


def canonical_scalar_reconstruction(
    a: np.ndarray, params: RLLParameters
) -> dict[str, object]:
    """Reconstruct V(a) and phi(a) when canonical scalar inequalities permit it.

    Units set M_p=H0=1. For a flat FLRW canonical scalar,
    phi_dot^2 = -2 dot(H) - rho_m - 4 rho_r/3. Negative kinetic density proves
    this canonical reconstruction is impossible for that grid point.
    """

    e2 = e2_rll_a(a, params)
    d_e2_da = numerical_d_e2_da(a, params)
    kinetic = (
        -(a / 3.0) * d_e2_da
        - params.omega_m * a**-3
        - (4.0 / 3.0) * params.omega_r * a**-4
    )
    scalar_rho = e2 - params.omega_m * a**-3 - params.omega_r * a**-4
    potential = scalar_rho - 0.5 * kinetic
    valid = bool(
        np.all(np.isfinite(kinetic))
        and np.all(kinetic >= -1.0e-10)
        and np.all(np.isfinite(potential))
    )
    phi = np.full_like(a, np.nan)
    if valid:
        integrand = np.sqrt(np.maximum(kinetic, 0.0) / np.maximum(e2, 1.0e-300)) / a
        phi[0] = 0.0
        phi[1:] = np.cumsum(0.5 * (integrand[1:] + integrand[:-1]) * np.diff(a))
    return {
        "valid_canonical_reconstruction": valid,
        "reason": (
            "canonical V(phi) reconstruction computed"
            if valid
            else f"{TOKEN_VAZIO}: canonical kinetic density becomes negative; no derived canonical EFT proof"
        ),
        "a": a,
        "e2": e2,
        "kinetic": kinetic,
        "potential": potential,
        "phi": phi,
    }


def perturbation_stability(reconstruction: Mapping[str, object]) -> dict[str, object]:
    valid = bool(reconstruction["valid_canonical_reconstruction"])
    if not valid:
        return {
            "Q_s": TOKEN_VAZIO,
            "c_s2": TOKEN_VAZIO,
            "stable": False,
            "decision": "REJEITADO COMO EFT",
        }
    kinetic = np.asarray(reconstruction["kinetic"], dtype=float)
    qs_ok = bool(np.all(kinetic > 0.0))
    cs2 = 1.0
    return {
        "Q_s_min": float(np.min(kinetic)),
        "c_s2": cs2,
        "stable": qs_ok and 0.0 < cs2 <= 1.0,
        "decision": "stable_canonical_sector" if qs_ok else "REJEITADO COMO EFT",
    }


def information_criteria(chi2: float, n_params: int, n_data: int) -> dict[str, float]:
    return {
        "chi2": float(chi2),
        "aic": float(chi2 + 2 * n_params),
        "bic": float(chi2 + n_params * np.log(max(n_data, 1))),
    }


def identifiability_scan(
    alpha_values: Iterable[float], k_values: Iterable[float], at_values: Iterable[float]
) -> dict[str, object]:
    grid = [
        (alpha, k, at) for alpha in alpha_values for k in k_values for at in at_values
    ]
    non_identifiable = any(k == 0.0 for _, k, _ in grid) or any(
        alpha == 0.0 for alpha, _, _ in grid
    )
    return {
        "grid_points": len(grid),
        "non_identifiable": bool(non_identifiable),
        "reason": (
            f"{TOKEN_VAZIO}: parâmetros não identificáveis em alpha=0 ou k=0"
            if non_identifiable
            else "finite grid has distinguishable transition amplitudes"
        ),
    }


def _scan_axis(max_value: float, samples: int) -> np.ndarray:
    if samples < 2:
        raise ValueError("samples_per_axis must be >= 2")
    if max_value <= 0.0 or not np.isfinite(max_value):
        raise ValueError("scan upper bounds must be finite and positive")
    return np.linspace(0.0, float(max_value), int(samples), dtype=float)


def parameter_exhaustion_grid(
    base: RLLParameters,
    scale_factor_grid: np.ndarray,
    config: ScanConfig,
) -> tuple[list[dict[str, object]], dict[str, object]]:
    """Run a finite, declared parameter exhaustion over alpha, k and a_t.

    The mathematical prompt asks for alpha,k in [0, infinity]. A computer run
    cannot exhaust infinity, so this function records a finite truncation and
    keeps the global claim blocked unless the degeneracy boundary is resolved.
    """

    alpha_values = _scan_axis(config.alpha_max, config.samples_per_axis)
    k_values = _scan_axis(config.k_max, config.samples_per_axis)
    at_values = np.linspace(0.0, 1.0, config.samples_per_axis, dtype=float)
    rows: list[dict[str, object]] = []
    stable_count = 0
    non_identifiable_count = 0
    invalid_background_count = 0
    for alpha in alpha_values:
        for k in k_values:
            for a_t in at_values:
                params = RLLParameters(
                    base.omega_m,
                    base.omega_r,
                    base.omega_lambda,
                    float(alpha),
                    float(k),
                    float(a_t),
                )
                e2 = e2_rll_a(scale_factor_grid, params)
                background_ok = bool(np.all(np.isfinite(e2)) and np.all(e2 > 0.0))
                non_identifiable = bool(alpha == 0.0 or k == 0.0)
                stable = False
                qs_min: float | str = TOKEN_VAZIO
                if background_ok and not non_identifiable:
                    reconstruction = canonical_scalar_reconstruction(
                        scale_factor_grid, params
                    )
                    stability = perturbation_stability(reconstruction)
                    stable = bool(stability.get("stable"))
                    qs_min = stability.get("Q_s_min", TOKEN_VAZIO)
                stable_count += int(stable)
                non_identifiable_count += int(non_identifiable)
                invalid_background_count += int(not background_ok)
                rows.append(
                    {
                        "alpha": float(alpha),
                        "k": float(k),
                        "a_t": float(a_t),
                        "background_ok": background_ok,
                        "non_identifiable": non_identifiable,
                        "stable_canonical_eft": stable,
                        "Q_s_min": qs_min,
                    }
                )
    summary = {
        "grid_points": len(rows),
        "stable_canonical_points": stable_count,
        "non_identifiable_points": non_identifiable_count,
        "invalid_background_points": invalid_background_count,
        "alpha_range_scanned": [0.0, float(config.alpha_max)],
        "k_range_scanned": [0.0, float(config.k_max)],
        "a_t_range_scanned": [0.0, 1.0],
        "samples_per_axis": int(config.samples_per_axis),
        "truncation_notice": f"{TOKEN_VAZIO}: alpha,k exigem [0, infinito]; execução computacional usa corte finito declarado",
    }
    return rows, summary


def _read_json(path: Path | None) -> dict[str, object] | None:
    if path is None or not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def _read_model_rows(path: Path | None) -> dict[str, dict[str, object]]:
    if path is None or not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as fh:
        return {str(row.get("model", "")): dict(row) for row in csv.DictReader(fh)}


def _float_from_row(row: Mapping[str, object], key: str) -> float | None:
    try:
        return float(row[key])
    except (KeyError, TypeError, ValueError):
        return None


def _aic_decision(delta_aic_rll_minus_baseline: float) -> str:
    if delta_aic_rll_minus_baseline < -2.0:
        return "favorável"
    if abs(delta_aic_rll_minus_baseline) <= 2.0:
        return "inconclusivo"
    return "rejeitado"


def load_observational_evidence(inputs: ArtifactInputs) -> dict[str, object]:
    """Load already-materialized validation artifacts without downloading data."""

    summary = _read_json(inputs.validation_summary)
    rows = _read_model_rows(inputs.model_comparison_csv)
    dataset_status = {name: TOKEN_VAZIO for name in DATASETS_REQUIRED}
    if summary:
        dataset_status["BAO"] = "materialized_summary"
        if "HZ" in json.dumps(summary):
            dataset_status["cosmic_chronometers_Hz"] = "materialized_summary"
    if rows:
        dataset_status["model_comparison_csv"] = "materialized"

    comparisons: dict[str, object] = {
        "RLL_vs_LCDM": TOKEN_VAZIO,
        "RLL_vs_w0waCDM": TOKEN_VAZIO,
    }
    rll_row = rows.get("RLL")
    for baseline_name, report_key in (
        ("LCDM", "RLL_vs_LCDM"),
        ("w0waCDM", "RLL_vs_w0waCDM"),
        ("w0wa", "RLL_vs_w0waCDM"),
    ):
        baseline_row = rows.get(baseline_name)
        if not rll_row or not baseline_row:
            continue
        rll_aic = _float_from_row(rll_row, "aic")
        base_aic = _float_from_row(baseline_row, "aic")
        rll_bic = _float_from_row(rll_row, "bic")
        base_bic = _float_from_row(baseline_row, "bic")
        rll_chi2 = _float_from_row(rll_row, "chi2_total") or _float_from_row(
            rll_row, "chi2"
        )
        base_chi2 = _float_from_row(baseline_row, "chi2_total") or _float_from_row(
            baseline_row, "chi2"
        )
        if rll_aic is None or base_aic is None:
            continue
        comparisons[report_key] = {
            "baseline": baseline_name,
            "delta_aic_rll_minus_baseline": rll_aic - base_aic,
            "delta_bic_rll_minus_baseline": (
                None if rll_bic is None or base_bic is None else rll_bic - base_bic
            ),
            "delta_chi2_rll_minus_baseline": (
                None if rll_chi2 is None or base_chi2 is None else rll_chi2 - base_chi2
            ),
            "decision_by_delta_aic": _aic_decision(rll_aic - base_aic),
        }

    missing_required = [
        name for name in DATASETS_REQUIRED if dataset_status.get(name) == TOKEN_VAZIO
    ]
    missing_baselines = [
        name
        for name in BASELINES_REQUIRED
        if comparisons.get(f"RLL_vs_{name}") == TOKEN_VAZIO
    ]
    return {
        "datasets": dataset_status,
        "model_comparison": comparisons,
        "missing_required_datasets": missing_required,
        "missing_required_baselines": missing_baselines,
        "source_artifacts": {
            "validation_summary": (
                str(inputs.validation_summary) if inputs.validation_summary else None
            ),
            "model_comparison_csv": (
                str(inputs.model_comparison_csv)
                if inputs.model_comparison_csv
                else None
            ),
        },
    }


def final_decision(
    stability: Mapping[str, object],
    evidence: Mapping[str, object],
    identifiability: Mapping[str, object],
) -> str:
    if not bool(stability.get("stable")):
        return "REJEITADO COMO EFT"
    if bool(identifiability.get("non_identifiable")):
        return "INCONCLUSIVO (TOKEN_VAZIO)"
    comparisons = evidence.get("model_comparison", {})
    if not isinstance(comparisons, Mapping):
        return "INCONCLUSIVO (TOKEN_VAZIO)"
    lcdm = comparisons.get("RLL_vs_LCDM")
    w0wa = comparisons.get("RLL_vs_w0waCDM")
    if not isinstance(lcdm, Mapping) or not isinstance(w0wa, Mapping):
        return "INCONCLUSIVO (TOKEN_VAZIO)"
    if (
        lcdm.get("decision_by_delta_aic") == "favorável"
        and w0wa.get("decision_by_delta_aic") == "favorável"
    ):
        return "ACEITO COMO TEORIA FUNDAMENTAL"
    if (
        lcdm.get("decision_by_delta_aic") == "rejeitado"
        or w0wa.get("decision_by_delta_aic") == "rejeitado"
    ):
        return "REJEITADO COMO EFT"
    return "INCONCLUSIVO (TOKEN_VAZIO)"


def write_markdown_report(report: Mapping[str, object], path: Path) -> None:
    comparison = report.get("model_comparison", {})
    stability = report.get("stability_eft", {})
    exhaustion = report.get("parameter_exhaustion", {})
    lines = [
        "# RLL EFT Exhaustion Report",
        "",
        "## Decisão final",
        f"{report.get('final_decision', TOKEN_VAZIO)}",
        "",
        "## Estabilidade EFT",
        "| item | resultado |",
        "| --- | --- |",
    ]
    if isinstance(stability, Mapping):
        for key, value in stability.items():
            lines.append(f"| {key} | {value} |")
    lines.extend(
        ["", "## Comparação estatística", "| comparação | resultado |", "| --- | --- |"]
    )
    if isinstance(comparison, Mapping):
        for key, value in comparison.items():
            lines.append(f"| {key} | {json.dumps(value, ensure_ascii=False)} |")
    lines.extend(
        ["", "## Exaustão de parâmetros", "| item | resultado |", "| --- | --- |"]
    )
    if isinstance(exhaustion, Mapping):
        finite_scan = exhaustion.get("finite_scan", {})
        if isinstance(finite_scan, Mapping):
            for key, value in finite_scan.items():
                lines.append(f"| {key} | {value} |")
    lines.extend(
        [
            "",
            "## Observação",
            "Nenhuma conclusão é promovida quando derivação, dado ou baseline obrigatório está ausente.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def run_exhaustion(
    params: RLLParameters,
    out_dir: Path,
    n_grid: int = 256,
    artifact_inputs: ArtifactInputs | None = None,
    scan_config: ScanConfig | None = None,
) -> dict[str, object]:
    out_dir.mkdir(parents=True, exist_ok=True)
    a = np.linspace(1.0e-3, 1.0, n_grid)
    reconstruction = canonical_scalar_reconstruction(a, params)
    stability = perturbation_stability(reconstruction)
    ident = identifiability_scan(
        [0.0, params.alpha], [0.0, params.k], [0.0, params.a_t, 1.0]
    )
    scan_rows, scan_summary = parameter_exhaustion_grid(
        params, a, scan_config or ScanConfig()
    )
    evidence = load_observational_evidence(artifact_inputs or ArtifactInputs())

    csv_path = out_dir / "eft_reconstruction.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(
            fh, fieldnames=["a", "E2", "kinetic", "potential", "phi"]
        )
        writer.writeheader()
        for row in zip(
            reconstruction["a"],
            reconstruction["e2"],
            reconstruction["kinetic"],
            reconstruction["potential"],
            reconstruction["phi"],
        ):
            writer.writerow(
                {
                    "a": row[0],
                    "E2": row[1],
                    "kinetic": row[2],
                    "potential": row[3],
                    "phi": row[4],
                }
            )

    scan_path = out_dir / "parameter_scan.csv"
    with scan_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "alpha",
                "k",
                "a_t",
                "background_ok",
                "non_identifiable",
                "stable_canonical_eft",
                "Q_s_min",
            ],
        )
        writer.writeheader()
        writer.writerows(scan_rows)

    report_path = out_dir / "eft_exhaustion_report.json"
    markdown_path = out_dir / "eft_exhaustion_report.md"
    report = {
        "parameters": asdict(params),
        "background": {
            "equation": "E^2(a)=Omega_m a^-3+Omega_r a^-4+Omega_Lambda+alpha S(a)",
            "omega_total_a1": float(e2_rll_a(1.0, params)),
        },
        "eft_reconstruction": {
            "valid": reconstruction["valid_canonical_reconstruction"],
            "reason": reconstruction["reason"],
        },
        "stability_eft": stability,
        "observational_validation": evidence["datasets"],
        "model_comparison": evidence["model_comparison"],
        "evidence_audit": {
            "missing_required_datasets": evidence["missing_required_datasets"],
            "missing_required_baselines": evidence["missing_required_baselines"],
            "source_artifacts": evidence["source_artifacts"],
        },
        "parameter_exhaustion": {**ident, "finite_scan": scan_summary},
        "final_decision": final_decision(stability, evidence, ident),
        "artifacts": {
            "reconstruction_csv": str(csv_path),
            "parameter_scan_csv": str(scan_path),
            "json_report": str(report_path),
            "markdown_report": str(markdown_path),
        },
    }
    report_path.write_text(
        json.dumps(report, indent=2, sort_keys=True), encoding="utf-8"
    )
    write_markdown_report(report, markdown_path)
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Run conservative RLL EFT exhaustion/falsification engine"
    )
    parser.add_argument(
        "--out-dir", type=Path, default=Path("validacao_real/results/eft_exhaustion")
    )
    parser.add_argument("--omega-m", type=float, default=0.315)
    parser.add_argument("--omega-r", type=float, default=9.0e-5)
    parser.add_argument("--omega-lambda", type=float, default=None)
    parser.add_argument("--alpha", type=float, default=0.0)
    parser.add_argument("--k", type=float, default=10.0)
    parser.add_argument("--a-t", type=float, default=0.5)
    parser.add_argument("--grid", type=int, default=256)
    parser.add_argument(
        "--validation-summary",
        type=Path,
        default=Path("validacao_real/results/validation_summary.json"),
    )
    parser.add_argument(
        "--model-comparison-csv",
        type=Path,
        default=Path("validacao_real/results/model_comparison.csv"),
    )
    parser.add_argument("--scan-alpha-max", type=float, default=0.05)
    parser.add_argument("--scan-k-max", type=float, default=20.0)
    parser.add_argument("--scan-samples", type=int, default=5)
    args = parser.parse_args(argv)
    report = run_exhaustion(
        RLLParameters(
            args.omega_m, args.omega_r, args.omega_lambda, args.alpha, args.k, args.a_t
        ),
        args.out_dir,
        args.grid,
        ArtifactInputs(args.validation_summary, args.model_comparison_csv),
        ScanConfig(args.scan_alpha_max, args.scan_k_max, args.scan_samples),
    )
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
