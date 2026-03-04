import csv
from pathlib import Path

WT_MIN = 0.1
WT_MAX = 1.0


def _is_number(value: str) -> bool:
    try:
        float(value)
        return True
    except (TypeError, ValueError):
        return False


def _collect_wt_violations(csv_path: Path):
    violations = []
    with csv_path.open(newline="", encoding="utf-8") as fp:
        reader = csv.DictReader(fp)
        if not reader.fieldnames or "wt" not in reader.fieldnames:
            return violations
        for row in reader:
            raw = (row.get("wt") or "").strip()
            if raw in {"", "-"}:
                continue
            if not _is_number(raw):
                violations.append((raw, "not-numeric"))
                continue
            wt = float(raw)
            if not (WT_MIN <= wt <= WT_MAX):
                violations.append((wt, f"out-of-range [{WT_MIN}, {WT_MAX}]"))
    return violations


def test_wt_convention_in_result_outputs():
    csv_targets = [
        Path("results/RLL_chi2_results.csv"),
        Path("results/structure_d/model_comparison_real.csv"),
    ]

    missing = [str(path) for path in csv_targets if not path.exists()]
    assert not missing, f"missing expected outputs: {missing}"

    violations = {}
    for path in csv_targets:
        bad = _collect_wt_violations(path)
        if bad:
            violations[str(path)] = bad

    assert not violations, f"wt convention violations found: {violations}"
