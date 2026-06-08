from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "real" / "rll_real_sources_manifest_2026.yml"
CSV_OUT = ROOT / "data" / "real" / "cosmology_observational_seed_2026.csv"
PROVENANCE_OUT = ROOT / "data" / "real" / "cosmology_observational_seed_2026.provenance.json"
REPORT_OUT = ROOT / "docs" / "real_data" / "RLL_REAL_DATA_INGESTION_REPORT_2026.md"

CLAIM_BOUNDARY = "No superiority claim unless real-data metrics pass predefined thresholds."
PUBLICATION_BOUNDARY = "RLL is a candidate effective dynamic-transition cosmology under real-data evaluation."

FIELDS = [
    "source_id",
    "domain",
    "probe",
    "z",
    "observable",
    "value",
    "err_minus",
    "err_plus",
    "units",
    "year",
    "reference",
    "claim_status",
    "notes",
]

# Curated deterministic projection from data/real/rll_real_sources_manifest_2026.yml.
# This is intentionally explicit: no fake-fill, no web download, no statistical inference.
ROWS = [
    {
        "source_id": "cc_borghi_2021_lega_c",
        "domain": "cosmology_expansion_Hz",
        "probe": "cosmic_chronometers",
        "z": "0.75",
        "observable": "H(z)",
        "value": "98.8",
        "err_minus": "33.6",
        "err_plus": "33.6",
        "units": "km/s/Mpc",
        "year": "2021",
        "reference": "arXiv:2110.04304",
        "claim_status": "observed_seed",
        "notes": "LEGA-C cosmic chronometer point from published abstract; seed only, not a complete compilation.",
    },
    {
        "source_id": "cc_jiao_2022_lega_c_full_spectrum",
        "domain": "cosmology_expansion_Hz",
        "probe": "cosmic_chronometers",
        "z": "0.80",
        "observable": "H(z)",
        "value": "113.1",
        "err_minus": "19.188",
        "err_plus": "32.773",
        "units": "km/s/Mpc",
        "year": "2022",
        "reference": "arXiv:2205.05701",
        "claim_status": "observed_seed",
        "notes": "LEGA-C full-spectrum fitting point; asymmetric systematic uncertainty preserved in quadrature.",
    },
    {
        "source_id": "cc_tomasetti_2025_clusters",
        "domain": "cosmology_expansion_Hz",
        "probe": "cosmic_chronometers_clusters",
        "z": "0.542",
        "observable": "H(z)",
        "value": "66.0",
        "err_minus": "31.780",
        "err_plus": "82.037",
        "units": "km/s/Mpc",
        "year": "2025",
        "reference": "arXiv:2512.02109",
        "claim_status": "observed_seed",
        "notes": "Galaxy-cluster cosmic chronometer seed; low-weight independent control because uncertainty is broad.",
    },
    {
        "source_id": "desi_dr2_bao_2025",
        "domain": "cosmology_BAO",
        "probe": "BAO",
        "z": "",
        "observable": "BAO source summary",
        "value": "14e6",
        "err_minus": "",
        "err_plus": "",
        "units": "objects",
        "year": "2025",
        "reference": "arXiv:2503.14738",
        "claim_status": "source_summary",
        "notes": "DESI DR2 BAO source uses more than 14 million galaxies and quasars; full BAO table and covariance required before chi2.",
    },
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_csv(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(ROWS)


def validate_manifest_presence(manifest: Path) -> None:
    if not manifest.exists():
        raise FileNotFoundError(f"missing manifest: {manifest}")
    text = manifest.read_text(encoding="utf-8")
    missing = [row["source_id"] for row in ROWS if row["source_id"] not in text]
    if missing:
        raise ValueError(f"manifest is missing source ids required by ingestor: {missing}")


def write_provenance(manifest: Path, csv_path: Path, out: Path) -> None:
    payload = {
        "schema": "rll.real_data_provenance.v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "claim_boundary": CLAIM_BOUNDARY,
        "publication_boundary": PUBLICATION_BOUNDARY,
        "inputs": {
            str(manifest.relative_to(ROOT)): {
                "sha256": sha256_file(manifest),
                "bytes": manifest.stat().st_size,
            }
        },
        "outputs": {
            str(csv_path.relative_to(ROOT)): {
                "sha256": sha256_file(csv_path),
                "bytes": csv_path.stat().st_size,
                "rows": len(ROWS),
            }
        },
        "row_counts_by_claim_status": {
            "observed_seed": 3,
            "source_summary": 1,
        },
    }
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_report(out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# RLL Real Data Ingestion Report — 2026",
        "",
        "## Coerência × Amor × Prova",
        "Este relatório materializa a primeira camada de dados reais auditáveis do RLL sem converter hipótese em conclusão.",
        "",
        f"- Manifesto: `{MANIFEST.relative_to(ROOT)}`",
        f"- CSV normalizado: `{CSV_OUT.relative_to(ROOT)}`",
        f"- Proveniência: `{PROVENANCE_OUT.relative_to(ROOT)}`",
        f"- Claim boundary: `{CLAIM_BOUNDARY}`",
        "",
        "## Saídas atuais",
        "- Linhas totais no CSV: 4",
        "- Pontos observacionais H(z): 3",
        "- Fontes-resumo aguardando tabela/covariância: 1",
        "",
        "## Pontos observacionais materializados",
        "",
        "| source_id | z | observável | valor | erro - | erro + | unidade | referência |",
        "|---|---:|---|---:|---:|---:|---|---|",
    ]
    for row in ROWS:
        if row["claim_status"] == "observed_seed":
            lines.append(
                f"| {row['source_id']} | {row['z']} | {row['observable']} | {row['value']} | {row['err_minus']} | {row['err_plus']} | {row['units']} | {row['reference']} |"
            )
    lines += [
        "",
        "## Lacunas preservadas como dado",
        "- DESI DR2 BAO foi registrado como fonte real, mas ainda exige tabela oficial de distâncias BAO e covariância antes de qualquer chi2.",
        "- Pantheon+SH0ES foi registrado como entrada esperada do runner real, mas arquivos grandes oficiais devem ser materializados localmente em `data/pantheon/`.",
        "- Planck 2018 foi preservado como referência/prior, não como dado bruto ingerido.",
        "",
        "## Próximo passo executável",
        "```bash",
        "python scripts/ingest_real_cosmology_sources.py --check",
        "python scripts/run_real_pantheon_validation.py",
        "```",
        "",
    ]
    out.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate RLL real cosmology seed CSV, provenance and report.")
    parser.add_argument("--check", action="store_true", help="fail when generated CSV differs from committed CSV")
    args = parser.parse_args()

    validate_manifest_presence(MANIFEST)
    old_csv = CSV_OUT.read_text(encoding="utf-8") if CSV_OUT.exists() else None
    write_csv(CSV_OUT)
    write_provenance(MANIFEST, CSV_OUT, PROVENANCE_OUT)
    write_report(REPORT_OUT)

    if args.check and old_csv is not None and CSV_OUT.read_text(encoding="utf-8") != old_csv:
        print("[rll-real-ingest] generated CSV differs from committed CSV", file=sys.stderr)
        raise SystemExit(1)

    print(f"[rll-real-ingest] wrote {CSV_OUT.relative_to(ROOT)}")
    print(f"[rll-real-ingest] wrote {PROVENANCE_OUT.relative_to(ROOT)}")
    print(f"[rll-real-ingest] wrote {REPORT_OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
