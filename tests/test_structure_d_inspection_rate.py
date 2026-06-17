from __future__ import annotations

import json
from pathlib import Path

import pytest

from scripts.analysis import structure_d_inspection_rate as inspect


def test_item_score_formula_uses_weighted_evidence_operation_and_control() -> None:
    item = {
        "evidence": 1.0,
        "operation": 0.5,
        "risk_control": 0.0,
    }

    score = inspect.item_score_percent(item)

    assert score == pytest.approx(100.0 * (0.40 * 1.0 + 0.35 * 0.5 + 0.25 * 0.0))


def test_weighted_inspection_rate_respects_item_weights() -> None:
    rows = [
        {"weight": 1.0, "item_score_percent": 100.0, "evidence": 1.0, "operation": 1.0, "risk_control": 1.0, "risk_severity": 1.0, "residual_risk": 0.0},
        {"weight": 3.0, "item_score_percent": 0.0, "evidence": 0.0, "operation": 0.0, "risk_control": 0.0, "risk_severity": 1.0, "residual_risk": 1.0},
    ]

    assert inspect.inspection_rate_percent(rows) == pytest.approx(25.0)


def test_risk_exposure_drops_when_item_is_fully_inspected() -> None:
    rows = [
        {"weight": 1.0, "item_score_percent": 100.0, "risk_severity": 1.0, "residual_risk": 0.0},
        {"weight": 1.0, "item_score_percent": 0.0, "risk_severity": 1.0, "residual_risk": 1.0},
    ]

    assert inspect.risk_exposure_percent(rows) == pytest.approx(50.0)


def test_category_summary_groups_items() -> None:
    items = [
        {
            "id": "a",
            "category": "cat1",
            "label": "A",
            "weight": 1,
            "evidence": 1.0,
            "operation": 1.0,
            "risk_control": 1.0,
            "risk_severity": 1.0,
            "status": "done",
        },
        {
            "id": "b",
            "category": "cat2",
            "label": "B",
            "weight": 1,
            "evidence": 0.0,
            "operation": 0.0,
            "risk_control": 0.0,
            "risk_severity": 1.0,
            "status": "gap",
        },
    ]
    rows = inspect.build_rows(items)
    summary = inspect.category_summary(rows)

    by_category = {row["category"]: row for row in summary}
    assert by_category["cat1"]["inspection_rate_percent"] == pytest.approx(100.0)
    assert by_category["cat2"]["inspection_rate_percent"] == pytest.approx(0.0)


def test_load_ledger_rejects_invalid_scores(tmp_path: Path) -> None:
    ledger = {
        "schema": "rll.structure_d_inspection_items.v1",
        "items": [
            {
                "id": "bad",
                "category": "test",
                "label": "Bad",
                "weight": 1,
                "evidence": 1.5,
                "operation": 0.0,
                "risk_control": 0.0,
                "risk_severity": 1.0,
                "status": "bad",
            }
        ],
    }
    path = tmp_path / "ledger.json"
    path.write_text(json.dumps(ledger), encoding="utf-8")

    with pytest.raises(inspect.InspectionError):
        inspect.load_ledger(path)


def test_run_writes_manifest_and_csvs(tmp_path: Path) -> None:
    ledger = {
        "schema": "rll.structure_d_inspection_items.v1",
        "items": [
            {
                "id": "ok",
                "category": "test",
                "label": "OK",
                "weight": 2,
                "evidence": 1.0,
                "operation": 0.5,
                "risk_control": 1.0,
                "risk_severity": 0.5,
                "status": "partial",
            }
        ],
    }
    ledger_path = tmp_path / "ledger.json"
    output_dir = tmp_path / "out"
    ledger_path.write_text(json.dumps(ledger), encoding="utf-8")

    result = inspect.run(ledger_path, output_dir)

    assert Path(result["items_csv"]).exists()
    assert Path(result["categories_csv"]).exists()
    assert Path(result["manifest_json"]).exists()
    assert result["manifest"]["claim_allowed"] is False
    assert result["manifest"]["global"]["items"] == 1
