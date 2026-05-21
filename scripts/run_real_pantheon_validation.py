from __future__ import annotations

import argparse
import json
import math
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_RESULTS = ROOT / "data" / "results"
MODEL_COMPARISON_JSON = DATA_RESULTS / "model_comparison.json"
PANTHEON_SUMMARY_JSON = DATA_RESULTS / "pantheon_fit_summary.json"

AIC_TENTATIVE_THRESHOLD = 2.0
AIC_STRONG_THRESHOLD = 10.0
BIC_TENTATIVE_THRESHOLD = 2.0
BIC_STRONG_THRESHOLD = 10.0
CHI2_IMPROVEMENT_MIN = 0.0
CLAIM_BOUNDARY = "No superiority claim unless real-data metrics pass predefined thresholds."
EXPECTED_SOURCE = "data/results/pantheon_fit_summary.json"


def _run(cmd: list[str], env: dict[str, str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, check=False, env=env)


def interpret_model_comparison(delta: dict) -> dict:
    delta_aic = delta.get("delta_aic_rll_minus_lcdm")
    delta_bic = delta.get("delta_bic_rll_minus_lcdm")
    delta_chi2 = delta.get("delta_chi2_rll_minus_lcdm")

    thresholds_used = {
        "aic_tentative": AIC_TENTATIVE_THRESHOLD,
        "aic_strong": AIC_STRONG_THRESHOLD,
        "bic_tentative": BIC_TENTATIVE_THRESHOLD,
        "bic_strong": BIC_STRONG_THRESHOLD,
        "chi2_improvement_min": CHI2_IMPROVEMENT_MIN,
    }

    def _is_valid_number(value: object) -> bool:
        return isinstance(value, (int, float)) and math.isfinite(value)

    if not _is_valid_number(delta_aic) or not _is_valid_number(delta_bic):
        return {
            "interpretation_label": "inconclusive",
            "interpretation_reason": "Missing or invalid delta_aic_rll_minus_lcdm and/or delta_bic_rll_minus_lcdm.",
            "thresholds_used": thresholds_used,
            "claim_boundary": CLAIM_BOUNDARY,
        }

    if delta_aic > 0 or delta_bic > 0:
        return {
            "interpretation_label": "lcdm_preferred",
            "interpretation_reason": "At least one information-criterion delta is positive (RLL worse than LCDM).",
            "thresholds_used": thresholds_used,
            "claim_boundary": CLAIM_BOUNDARY,
        }

    if (
        delta_aic <= -AIC_STRONG_THRESHOLD
        and delta_bic <= -BIC_STRONG_THRESHOLD
        and _is_valid_number(delta_chi2)
        and delta_chi2 < -CHI2_IMPROVEMENT_MIN
    ):
        return {
            "interpretation_label": "rll_preferred_strong",
            "interpretation_reason": "AIC/BIC exceed strong thresholds and chi2 improves beyond minimum guardrail.",
            "thresholds_used": thresholds_used,
            "claim_boundary": CLAIM_BOUNDARY,
        }

    if (
        delta_aic <= -AIC_TENTATIVE_THRESHOLD
        and delta_bic <= -BIC_TENTATIVE_THRESHOLD
        and _is_valid_number(delta_chi2)
        and delta_chi2 < 0
    ):
        return {
            "interpretation_label": "rll_preferred_tentative",
            "interpretation_reason": "AIC/BIC exceed tentative thresholds and chi2 improves.",
            "thresholds_used": thresholds_used,
            "claim_boundary": CLAIM_BOUNDARY,
        }

    return {
        "interpretation_label": "inconclusive",
        "interpretation_reason": "Deltas do not satisfy conservative preference thresholds.",
        "thresholds_used": thresholds_used,
        "claim_boundary": CLAIM_BOUNDARY,
    }


def validate_model_comparison_payload(payload: dict) -> list[str]:
    issues: list[str] = []
    if not payload.get("dataset"):
        issues.append("missing dataset")
    if payload.get("n_obs") is None:
        issues.append("missing n_obs")
    if not payload.get("source"):
        issues.append("missing source")
    elif payload.get("source") != EXPECTED_SOURCE:
        issues.append(f"source must be {EXPECTED_SOURCE}")
    if "covariance_used" not in payload:
        issues.append("missing covariance_used")

    models = payload.get("models")
    if not isinstance(models, dict):
        issues.append("missing models.rll or models.lcdm")
    else:
        rll = models.get("rll")
        lcdm = models.get("lcdm")
        if not isinstance(rll, dict) or not isinstance(lcdm, dict):
            issues.append("missing models.rll or models.lcdm")
        else:
            if rll.get("k_params") != 5:
                issues.append("wrong k_params for models.rll")
            if lcdm.get("k_params") != 2:
                issues.append("wrong k_params for models.lcdm")

    delta = payload.get("delta")
    if not isinstance(delta, dict):
        issues.append("missing delta")
        return issues

    if delta.get("claim_boundary") != CLAIM_BOUNDARY:
        issues.append("missing claim_boundary")
    if not delta.get("interpretation_label"):
        issues.append("missing interpretation_label")
    if not isinstance(delta.get("thresholds_used"), dict):
        issues.append("missing thresholds_used")

    for key in (
        "delta_chi2_rll_minus_lcdm",
        "delta_aic_rll_minus_lcdm",
        "delta_bic_rll_minus_lcdm",
    ):
        value = delta.get(key)
        if value is None:
            continue
        if not isinstance(value, (int, float)) or not math.isfinite(value):
            issues.append(f"invalid numerical delta: {key}")
    return issues


def _normalize_model_comparison(summary: dict) -> dict:
    source = EXPECTED_SOURCE
    rll = summary.get("rll", {})
    lcdm = summary.get("lcdm", {})

    def _metric(model_block: dict, *keys: str) -> float | None:
        for key in keys:
            if key in model_block:
                return model_block[key]
        return None

    rll_chi2 = _metric(rll, "chi2")
    lcdm_chi2 = _metric(lcdm, "chi2")
    rll_aic = _metric(rll, "aic", "AIC")
    lcdm_aic = _metric(lcdm, "aic", "AIC")
    rll_bic = _metric(rll, "bic", "BIC")
    lcdm_bic = _metric(lcdm, "bic", "BIC")

    delta = {
        "delta_chi2_rll_minus_lcdm": (rll_chi2 - lcdm_chi2) if (rll_chi2 is not None and lcdm_chi2 is not None) else None,
        "delta_aic_rll_minus_lcdm": (rll_aic - lcdm_aic) if (rll_aic is not None and lcdm_aic is not None) else None,
        "delta_bic_rll_minus_lcdm": (rll_bic - lcdm_bic) if (rll_bic is not None and lcdm_bic is not None) else None,
        "interpretation_guardrail": "Quantitative comparison only; do not infer model superiority from these deltas alone.",
    }
    delta.update(interpret_model_comparison(delta))

    return {
        "pipeline": summary.get("pipeline", "pantheon_oficial_prova_observacional"),
        "dataset": summary.get("dataset", "pantheon+"),
        "generated_at": summary.get("generated_at") or summary.get("timestamp_utc") or datetime.now(timezone.utc).isoformat(),
        "source": source,
        "source_summary": source,
        "n_obs": summary.get("n_obs"),
        "covariance_used": True,
        "models": {
            "rll": {
                "k_params": 5,
                "chi2": rll_chi2,
                "aic": rll_aic,
                "bic": rll_bic,
                "log_likelihood": _metric(rll, "log_likelihood"),
                "best_fit_params": rll.get("best_fit_params", rll.get("best_fit")),
            },
            "lcdm": {
                "k_params": 2,
                "chi2": lcdm_chi2,
                "aic": lcdm_aic,
                "bic": lcdm_bic,
                "log_likelihood": _metric(lcdm, "log_likelihood"),
                "best_fit_params": lcdm.get("best_fit_params", lcdm.get("best_fit")),
            },
        },
        "delta": delta,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Run minimal real Pantheon+ validation and emit auditable model_comparison.json")
    parser.add_argument("--skip-verify", action="store_true", help="Skip verify_pantheon_inputs step")
    parser.add_argument("--skip-preflight", action="store_true", help="Skip rll preflight-real step")
    args = parser.parse_args()

    env = os.environ.copy()
    env["PYTHONPATH"] = str(ROOT / "src")

    steps: list[tuple[str, list[str]]] = []
    if not args.skip_verify:
        steps.append(("verify", [sys.executable, "scripts/verify_pantheon_inputs.py", "--json"]))
    if not args.skip_preflight:
        steps.append(("preflight", [sys.executable, "-m", "rll.cli", "preflight-real", "--json"]))
    steps.append(("run_real", [sys.executable, "-m", "rll.cli", "run", "--data", "real", "--model", "both", "--with-covariance"]))

    for label, cmd in steps:
        completed = _run(cmd, env)
        if completed.returncode != 0:
            sys.stderr.write(f"[rll-real-validation] step={label} failed with code {completed.returncode}\n")
            sys.stderr.write(completed.stdout)
            sys.stderr.write(completed.stderr)
            raise SystemExit(completed.returncode)

    if not PANTHEON_SUMMARY_JSON.exists():
        raise FileNotFoundError(
            f"Expected summary not found: {PANTHEON_SUMMARY_JSON}. "
            "Real pipeline did not produce the required artifact."
        )

    summary = json.loads(PANTHEON_SUMMARY_JSON.read_text(encoding="utf-8"))
    normalized = _normalize_model_comparison(summary)
    DATA_RESULTS.mkdir(parents=True, exist_ok=True)
    MODEL_COMPARISON_JSON.write_text(json.dumps(normalized, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"[rll-real-validation] wrote {MODEL_COMPARISON_JSON}")


if __name__ == "__main__":
    main()
