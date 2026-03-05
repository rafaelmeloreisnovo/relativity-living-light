#!/usr/bin/env python3
"""Gera relatório de lacunas de execução (auditável) para o pipeline RLL."""

from __future__ import annotations

import csv
import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
STRUCTURE_D = RESULTS / "structure_d"
OUT_DIR = RESULTS / "audit"


@dataclass
class ModelRow:
    model: str
    chi2: float
    aic: float
    bic: float
    k: int
    n_obs: int



def read_model_comparison(path: Path) -> Dict[str, ModelRow]:
    rows: Dict[str, ModelRow] = {}
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            model = row["Model"].strip()
            if model not in {"LCDM", "RLL"}:
                continue
            rows[model] = ModelRow(
                model=model,
                chi2=float(row["chi2"]),
                aic=float(row["AIC"]),
                bic=float(row["BIC"]),
                k=int(float(row["k"])),
                n_obs=int(float(row["N_obs"])),
            )
    return rows


def read_covariance_modes(path: Path) -> List[dict]:
    with path.open("r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def classify_delta(delta: float, metric: str) -> str:
    if metric == "chi2":
        return "RLL melhora marginal" if delta < 0 else "RLL pior que ΛCDM"
    if delta >= 10:
        return "evidência forte contra RLL"
    if delta >= 6:
        return "evidência moderada contra RLL"
    if delta >= 2:
        return "evidência fraca contra RLL"
    return "inconclusivo"


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    model_csv = RESULTS / "RLL_chi2_results.csv"
    cov_csv = STRUCTURE_D / "covariance_usage.csv"

    if not model_csv.exists():
        raise FileNotFoundError(f"Arquivo ausente: {model_csv}")
    if not cov_csv.exists():
        raise FileNotFoundError(f"Arquivo ausente: {cov_csv}")

    models = read_model_comparison(model_csv)
    if "LCDM" not in models or "RLL" not in models:
        raise ValueError("RLL_chi2_results.csv precisa conter linhas para LCDM e RLL")

    lcdm = models["LCDM"]
    rll = models["RLL"]

    delta = {
        "chi2": round(rll.chi2 - lcdm.chi2, 6),
        "AIC": round(rll.aic - lcdm.aic, 6),
        "BIC": round(rll.bic - lcdm.bic, 6),
    }

    cov_rows = read_covariance_modes(cov_csv)
    diagonal_only = [
        r for r in cov_rows if r.get("covariance_mode", "").strip().lower() == "diagonal"
    ]

    payload = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "inputs": {
            "model_comparison": str(model_csv.relative_to(ROOT)),
            "covariance_usage": str(cov_csv.relative_to(ROOT)),
        },
        "models": {
            "LCDM": lcdm.__dict__,
            "RLL": rll.__dict__,
        },
        "delta_rll_minus_lcdm": {
            **delta,
            "chi2_assessment": classify_delta(delta["chi2"], "chi2"),
            "AIC_assessment": classify_delta(delta["AIC"], "AIC"),
            "BIC_assessment": classify_delta(delta["BIC"], "BIC"),
        },
        "covariance": {
            "rows": len(cov_rows),
            "all_diagonal": len(diagonal_only) == len(cov_rows),
            "diagonal_rows": [r.get("dataset_id", "") for r in diagonal_only],
        },
        "gates": {
            "pantheon_plus_integrated": False,
            "lnB_available": (STRUCTURE_D / "bayes_evidence_bic_proxy.csv").exists(),
            "full_covariance_usage": len(diagonal_only) != len(cov_rows),
        },
    }

    json_path = OUT_DIR / "rll_audit_gap_report.json"
    md_path = OUT_DIR / "rll_audit_gap_report.md"

    with json_path.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    lines = [
        "# RLL — Audit Gap Report",
        "",
        f"Gerado em: `{payload['generated_at_utc']}`",
        "",
        "## Comparação ΛCDM vs RLL (dados atuais)",
        "",
        "| Métrica | Δ (RLL−ΛCDM) | Leitura |",
        "|---|---:|---|",
        f"| χ² | {delta['chi2']:.6f} | {payload['delta_rll_minus_lcdm']['chi2_assessment']} |",
        f"| AIC | {delta['AIC']:.6f} | {payload['delta_rll_minus_lcdm']['AIC_assessment']} |",
        f"| BIC | {delta['BIC']:.6f} | {payload['delta_rll_minus_lcdm']['BIC_assessment']} |",
        "",
        "## Estado de covariância",
        "",
        f"- Linhas analisadas: **{payload['covariance']['rows']}**",
        f"- Uso apenas diagonal: **{payload['covariance']['all_diagonal']}**",
        f"- Datasets em modo diagonal: `{', '.join(payload['covariance']['diagonal_rows'])}`",
        "",
        "## Gates de publicação (automáticos)",
        "",
        f"- Pantheon+ integrado: **{payload['gates']['pantheon_plus_integrated']}**",
        f"- ln B disponível: **{payload['gates']['lnB_available']}**",
        f"- Covariância completa em uso: **{payload['gates']['full_covariance_usage']}**",
    ]

    with md_path.open("w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print(f"OK: {json_path.relative_to(ROOT)}")
    print(f"OK: {md_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
