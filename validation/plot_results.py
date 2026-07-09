import json
from pathlib import Path


OUTPUT_DIR = Path("validation_outputs")


if __name__ == "__main__":
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    lcdm_path = OUTPUT_DIR / "lcdm.json"
    rll_path = OUTPUT_DIR / "rll.json"
    comparison_path = OUTPUT_DIR / "comparison.json"

    missing = [str(path) for path in [lcdm_path, rll_path, comparison_path] if not path.exists()]
    if missing:
        raise FileNotFoundError("missing validation outputs: " + ", ".join(missing))

    lcdm = json.loads(lcdm_path.read_text(encoding="utf-8"))
    rll = json.loads(rll_path.read_text(encoding="utf-8"))
    comparison = json.loads(comparison_path.read_text(encoding="utf-8"))

    report = [
        "# RLL Validation Plot Placeholder",
        "",
        "This report is generated in CI as a lightweight plotting-stage artifact.",
        "It does not declare model superiority.",
        "",
        f"LCDM points: {len(lcdm.get('values', []))}",
        f"RLL points: {len(rll.get('values', []))}",
        f"chi2_lcdm: {comparison.get('chi2_lcdm')}",
        f"chi2_rll: {comparison.get('chi2_rll')}",
        "",
    ]
    out = OUTPUT_DIR / "plot_results_report.md"
    out.write_text("\n".join(report), encoding="utf-8")
    print(f"wrote {out}")
