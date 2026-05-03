#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, json, re
from dataclasses import dataclass, asdict
from pathlib import Path

BLOCK_RE = re.compile(r"\\begin\{align\*?\}(.*?)\\end\{align\*?\}", re.S)
INLINE_RE = re.compile(r"\$(.+?)\$", re.S)
DISPLAY_RE = re.compile(r"\\\[(.+?)\\\]", re.S)
EQ_RE = re.compile(r"^\s*(?:\d+\.\s*&\s*)?(.*?)\\\\\s*$")

@dataclass
class Formula:
    source: str
    category: str
    expression: str


def classify(expr: str) -> str:
    low = expr.lower()
    if any(k in low for k in ["crc", "hash", "merkle", "xor", "poly"]):
        return "integridade_e_criptografia"
    if any(k in low for k in ["sin", "cos", "omega", "f(", "hz", "fourier", "\\mathcal{f}"]):
        return "espectral_e_frequencial"
    if any(k in low for k in ["\\mathbb{t}^7", "toro", "spiral", "sqrt", "phi", "pi", "gcd"]):
        return "geometria_e_toro"
    if any(k in low for k in ["c_{t+1}", "h_{t+1}", "entrop", "coer", "atrator", "lim"]):
        return "dinamica_e_coerencia"
    return "geral"


def extract_from_text(text: str, source: str) -> list[Formula]:
    out: list[Formula] = []
    for block in BLOCK_RE.findall(text):
        for line in block.splitlines():
            m = EQ_RE.match(line)
            if m:
                expr = " ".join(m.group(1).split())
                if expr:
                    out.append(Formula(source, classify(expr), expr))
    for pat in (DISPLAY_RE, INLINE_RE):
        for expr in pat.findall(text):
            expr = " ".join(expr.split())
            if len(expr) > 5 and any(ch in expr for ch in "=\\^_"):
                out.append(Formula(source, classify(expr), expr))
    # de-dup preserving order
    seen = set()
    unique = []
    for f in out:
        key = (f.source, f.expression)
        if key not in seen:
            seen.add(key)
            unique.append(f)
    return unique


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--outdir", default="artifacts/formulas")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    outdir = root / args.outdir
    outdir.mkdir(parents=True, exist_ok=True)

    scopes = [root / "docs", root / "news/archive_legacy", root / "RMR", root / "newadd"]
    files = []
    for scope in scopes:
        if scope.exists():
            files.extend(scope.rglob("*.md"))

    all_formulas: list[Formula] = []
    for fp in sorted(files):
        txt = fp.read_text(encoding="utf-8", errors="ignore")
        all_formulas.extend(extract_from_text(txt, str(fp.relative_to(root))))

    (outdir / "formulas.json").write_text(json.dumps([asdict(f) for f in all_formulas], ensure_ascii=False, indent=2), encoding="utf-8")

    with (outdir / "formulas.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["source", "category", "expression"])
        for row in all_formulas:
            w.writerow([row.source, row.category, row.expression])

    by_cat: dict[str, int] = {}
    for f in all_formulas:
        by_cat[f.category] = by_cat.get(f.category, 0) + 1
    lines = ["# Catálogo Formal de Expressões Matemáticas", "", "## Estatísticas", ""]
    lines.append(f"- Total de expressões extraídas: **{len(all_formulas)}**")
    for k,v in sorted(by_cat.items()):
        lines.append(f"- {k}: **{v}**")
    lines += ["", "## Amostra (primeiras 120)", "", "| Fonte | Categoria | Expressão |", "|---|---|---|"]
    for f in all_formulas[:120]:
        lines.append(f"| `{f.source}` | {f.category} | `${f.expression}$ |")
    (outdir / "FORMAL_ACADEMIC_REPORT.md").write_text("\n".join(lines), encoding="utf-8")

if __name__ == "__main__":
    main()
