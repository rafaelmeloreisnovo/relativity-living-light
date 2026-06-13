#!/usr/bin/env python3
"""Calculate Structure-D/RLL scientific-operational inspection rates.

The inspection rate is a diagnostic governance metric. It summarizes how much of
the current RLL validation stack is documented, executable, controlled, and still
exposed to risk. It does not authorize scientific claims.
"""

from __future__ import annotations

import argparse
import csv
import json
import time
from pathlib import Path
from typing import Any

BASE_DIR = Path(__file__).resolve().parents[2]
DEFAULT_INPUT = BASE_DIR / "data" / "inputs" / "structure_d_inspection" / "inspection_items.json"
DEFAULT_OUTPUT_DIR = BASE_DIR / "results" / "structure_d" / "inspection"

EVIDENCE_WEIGHT = 0.40
OPERATION_WEIGHT = 0.35
RISK_CONTROL_WEIGHT = 0.25


class InspectionError(ValueError):
    """Raised when an inspection ledger is malformed."""


def clamp01(value: float) -> float:
    return max(0.0, min(1.0, float(value)))


def item_score_percent(item: dict[str, Any]) -> float:
    """Weighted item inspection score in percent.

    Formula:
        100 * (0.40*evidence + 0.35*operation + 0.25*risk_control)
    """

    evidence = clamp01(float(item.get("evidence", 0.0)))
    operation = clamp01(float(item.get("operation", 0.0)))
    risk_control = clamp01(float(item.get("risk_control", 0.0)))
    return 100.0 * (EVIDENCE_WEIGHT * evidence + OPERATION_WEIGHT * operation + RISK_CONTROL_WEIGHT * risk_control)


def validate_item(item: dict[str, Any]) -> None:
    required = ["id", "category", "label", "weight", "evidence", "operation", "risk_control", "risk_severity", "status"]
    missing = [key for key in required if key not in item]
    if missing:
        raise InspectionError(f"inspection item missing required fields: {missing}")
    if float(item["weight"]) <= 0.0:
        raise InspectionError(f"inspection item {item['id']} must have positive weight")
    for key in ["evidence", "operation", "risk_control", "risk_severity"]:
        value = float(item[key])
        if not 0.0 <= value <= 1.0:
            raise InspectionError(f"inspection item {item['id']} has {key} outside [0, 1]: {value}")


def load_ledger(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("schema") != "rll.structure_d_inspection_items.v1":
        raise InspectionError("unsupported inspection ledger schema")
    items = payload.get("items")
    if not isinstance(items, list) or not items:
        raise InspectionError("inspection ledger must contain a non-empty items list")
    for item in items:
        validate_item(item)
    return payload


def build_rows(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for item in items:
        score = item_score_percent(item)
        risk_severity = float(item["risk_severity"])
        residual_risk = risk_severity * (1.0 - score / 100.0)
        rows.append(
            {
                "id": item["id"],
                "category": item["category"],
                "label": item["label"],
                "weight": float(item["weight"]),
                "evidence": float(item["evidence"]),
                "operation": float(item["operation"]),
                "risk_control": float(item["risk_control"]),
                "risk_severity": risk_severity,
                "item_score_percent": score,
                "residual_risk": residual_risk,
                "status": item["status"],
                "evidence_path": item.get("evidence_path", ""),
                "knowledge_note": item.get("knowledge_note", ""),
            }
        )
    return rows


def weighted_average(rows: list[dict[str, Any]], value_key: str, weight_key: str = "weight") -> float:
    total_weight = sum(float(row[weight_key]) for row in rows)
    if total_weight <= 0.0:
        raise InspectionError("total weight must be positive")
    return sum(float(row[weight_key]) * float(row[value_key]) for row in rows) / total_weight


def inspection_rate_percent(rows: list[dict[str, Any]]) -> float:
    return weighted_average(rows, "item_score_percent")


def knowledge_rate_percent(rows: list[dict[str, Any]]) -> float:
    return 100.0 * weighted_average(rows, "evidence")


def operation_rate_percent(rows: list[dict[str, Any]]) -> float:
    return 100.0 * weighted_average(rows, "operation")


def risk_control_rate_percent(rows: list[dict[str, Any]]) -> float:
    return 100.0 * weighted_average(rows, "risk_control")


def risk_exposure_percent(rows: list[dict[str, Any]]) -> float:
    denominator = sum(float(row["weight"]) * float(row["risk_severity"]) for row in rows)
    if denominator <= 0.0:
        return 0.0
    numerator = sum(float(row["weight"]) * float(row["residual_risk"]) for row in rows)
    return 100.0 * numerator / denominator


def classify_rate(value: float) -> str:
    if value >= 85.0:
        return "operational_high_confidence"
    if value >= 70.0:
        return "operational_but_needs_hardening"
    if value >= 50.0:
        return "partial_inspection"
    if value >= 30.0:
        return "early_scaffold"
    return "critical_gap"


def category_summary(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    categories = sorted({str(row["category"]) for row in rows})
    out: list[dict[str, Any]] = []
    for category in categories:
        subset = [row for row in rows if row["category"] == category]
        out.append(
            {
                "category": category,
                "inspection_rate_percent": inspection_rate_percent(subset),
                "knowledge_rate_percent": knowledge_rate_percent(subset),
                "operation_rate_percent": operation_rate_percent(subset),
                "risk_control_rate_percent": risk_control_rate_percent(subset),
                "risk_exposure_percent": risk_exposure_percent(subset),
                "items": len(subset),
            }
        )
    return out


def build_manifest(ledger_path: Path, rows: list[dict[str, Any]], output_csv: Path, category_csv: Path) -> dict[str, Any]:
    inspection = inspection_rate_percent(rows)
    risk_exposure = risk_exposure_percent(rows)
    return {
        "schema": "rll.structure_d_inspection_rate.v1",
        "created_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "source_ledger": str(ledger_path.relative_to(BASE_DIR)),
        "output_csv": str(output_csv.relative_to(BASE_DIR)),
        "category_csv": str(category_csv.relative_to(BASE_DIR)),
        "formula": {
            "item_score_percent": "100 * (0.40*evidence + 0.35*operation + 0.25*risk_control)",
            "inspection_rate_percent": "sum(weight*item_score_percent)/sum(weight)",
            "risk_exposure_percent": "100 * sum(weight*risk_severity*(1-item_score_percent/100))/sum(weight*risk_severity)",
        },
        "global": {
            "inspection_rate_percent": inspection,
            "knowledge_rate_percent": knowledge_rate_percent(rows),
            "operation_rate_percent": operation_rate_percent(rows),
            "risk_control_rate_percent": risk_control_rate_percent(rows),
            "risk_exposure_percent": risk_exposure,
            "inspection_class": classify_rate(inspection),
            "risk_exposure_class": classify_rate(100.0 - risk_exposure),
            "items": len(rows),
        },
        "claim_allowed": False,
        "interpretation": "Inspection/governance metric only; not a cosmological model-comparison result.",
        "raw_datasets_modified": False,
        "canonical_results_modified": False,
    }


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys())
    with path.open("w", encoding="utf-8", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def run(ledger_path: Path, output_dir: Path) -> dict[str, Any]:
    ledger = load_ledger(ledger_path)
    rows = build_rows(ledger["items"])
    output_csv = output_dir / "structure_d_inspection_rate_items.csv"
    category_csv = output_dir / "structure_d_inspection_rate_categories.csv"
    manifest_json = output_dir / "structure_d_inspection_rate_manifest.json"
    write_csv(output_csv, rows)
    categories = category_summary(rows)
    write_csv(category_csv, categories)
    manifest = build_manifest(ledger_path, rows, output_csv, category_csv)
    write_json(manifest_json, manifest)
    return {"items_csv": str(output_csv), "categories_csv": str(category_csv), "manifest_json": str(manifest_json), "manifest": manifest}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Calculate RLL/Structure-D inspection readiness and residual risk.")
    parser.add_argument("--ledger", default=str(DEFAULT_INPUT), help="Inspection item ledger JSON.")
    parser.add_argument("--output-dir", default=str(DEFAULT_OUTPUT_DIR), help="Directory for inspection outputs.")
    return parser


def main(argv: list[str] | None = None) -> dict[str, Any]:
    args = build_parser().parse_args(argv)
    result = run(Path(args.ledger).resolve(), Path(args.output_dir).resolve())
    manifest = result["manifest"]
    print(f"inspection_rate_percent={manifest['global']['inspection_rate_percent']:.2f}")
    print(f"risk_exposure_percent={manifest['global']['risk_exposure_percent']:.2f}")
    print(f"inspection_class={manifest['global']['inspection_class']}")
    print(f"Wrote: {Path(result['items_csv']).relative_to(BASE_DIR)}")
    print(f"Wrote: {Path(result['categories_csv']).relative_to(BASE_DIR)}")
    print(f"Wrote: {Path(result['manifest_json']).relative_to(BASE_DIR)}")
    return result


if __name__ == "__main__":
    main()
