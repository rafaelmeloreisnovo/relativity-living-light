#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import zipfile
from pathlib import Path

PREFIX = {
    "cosmology_metrics": "COS",
    "integridade_e_criptografia": "INT",
    "geral": "GEN",
}
GATE = {
    "cosmology_metrics": "GATE_COSMOLOGY_DATA_LOADER_COVARIANCE_CI",
    "integridade_e_criptografia": "GATE_INTEGRITY_CRYPTO_REPRODUCIBILITY_CI",
    "geral": "GATE_SYMBOLIC_GENERAL_REVIEW",
}


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def formula_id(source: str, category: str, expression: str) -> str:
    payload = f"{source.strip()}\n{category.strip()}\n{expression.strip()}"
    return f"FORM-{PREFIX.get(category, 'FRM')}-{sha256_text(payload)[:12].upper()}"


def search_text(source: str, category: str, expression: str) -> str:
    text = f"{category} {source} {expression}".lower()
    return re.sub(r"\s+", " ", text).strip()[:220]


def script_candidate(category: str, expression: str) -> str:
    e = expression.lower()
    if category == "cosmology_metrics":
        if "chi" in e or "χ" in expression:
            return "scripts/check_desi_dr2_bao_covariance.py|rll_vs_lcdm.py"
        if "fsigma" in e or "fσ" in expression or "omega_m(z)" in e or "d\\ln d" in e:
            return "scripts/check_rll_growth.py"
        if "h^2" in e or "h_0" in e or "omega" in e:
            return "rll_vs_lcdm.py|scripts/check_rll_background.py"
    if category == "integridade_e_criptografia":
        return "scripts/validate_formulas_manifest.py"
    return "TOKEN_VAZIO"


def load_formulas(path: Path) -> list[dict[str, str]]:
    if path.suffix == ".zip":
        with zipfile.ZipFile(path) as zf:
            return json.loads(zf.read("formulas.json"))
    return json.loads(path.read_text(encoding="utf-8"))


def normalize(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    out = []
    for row in rows:
        source = row["source"]
        category = row["category"]
        expression = row["expression"]
        script = script_candidate(category, expression)
        out.append({
            "formula_id": formula_id(source, category, expression),
            "source": source,
            "category": category,
            "expression": expression,
            "expression_sha256": sha256_text(expression.strip()),
            "search_text": search_text(source, category, expression),
            "claim_gate": GATE.get(category, "GATE_TOKEN_VAZIO"),
            "script_tester": script,
            "result_status": "candidate_link_only" if script != "TOKEN_VAZIO" else "indexed_no_result_linked",
        })
    ids = [r["formula_id"] for r in out]
    if len(ids) != len(set(ids)):
        raise SystemExit("formula_id collision detected")
    return out


def write_outputs(rows: list[dict[str, str]], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    jsonl = out_dir / "formula_index.jsonl"
    csv_path = out_dir / "formula_claim_gate_index.csv"
    summary = out_dir / "formula_index_summary.json"
    jsonl.write_text("\n".join(json.dumps(r, ensure_ascii=False, separators=(",", ":")) for r in rows) + "\n", encoding="utf-8")
    fields = ["formula_id", "category", "source", "expression_sha256", "search_text", "claim_gate", "script_tester", "result_status"]
    with csv_path.open("w", newline="", encoding="utf-8") as fp:
        writer = csv.DictWriter(fp, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row[k] for k in fields})
    counts: dict[str, int] = {}
    for row in rows:
        counts[row["category"]] = counts.get(row["category"], 0) + 1
    summary.write_text(json.dumps({
        "schema": "rafaelia.formula_index_summary.v1",
        "total_formulas": len(rows),
        "unique_formula_ids": len({r["formula_id"] for r in rows}),
        "category_counts": counts,
        "outputs": [str(jsonl), str(csv_path)],
    }, indent=2, ensure_ascii=False), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to formulas.json or formulas artifact zip")
    parser.add_argument("--out-dir", default="results/formulas")
    args = parser.parse_args()
    rows = normalize(load_formulas(Path(args.input)))
    write_outputs(rows, Path(args.out_dir))
    print(f"materialized {len(rows)} formulas into {args.out_dir}")


if __name__ == "__main__":
    main()
