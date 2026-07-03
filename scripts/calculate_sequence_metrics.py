#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

BOUNDARY = "This tool calculates descriptive FASTA metrics only; it does not validate RLL or promote scientific claims."
CANON = {"A", "C", "G", "T"}


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_id(text: str) -> str:
    value = re.sub(r"[^A-Za-z0-9_.-]+", "_", text.strip()).strip("._-")
    if not value:
        raise ValueError("empty dataset id")
    return value[:100]


def parse_fasta(text: str) -> list[dict[str, str]]:
    records = []
    header = None
    chunks = []
    def flush() -> None:
        nonlocal header, chunks
        if header is None:
            return
        seq = re.sub(r"\s+", "", "".join(chunks)).upper().replace("U", "T")
        if not seq:
            raise ValueError("empty sequence")
        records.append({"id": header.split()[0], "sequence": seq})
        header = None
        chunks = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            flush()
            header = line[1:].strip()
        else:
            if header is None:
                raise ValueError("sequence before FASTA header")
            chunks.append(line)
    flush()
    if not records:
        raise ValueError("no FASTA records found")
    return records


def counts(seq: str) -> dict[str, int]:
    out = {"A": 0, "C": 0, "G": 0, "T": 0, "N": 0, "OTHER": 0}
    for ch in seq:
        out[ch if ch in out else "OTHER"] += 1
    return out


def gc(c: dict[str, int]) -> float | None:
    denom = c["A"] + c["C"] + c["G"] + c["T"]
    return None if denom == 0 else (c["G"] + c["C"]) / denom


def rows_and_summary(records: list[dict[str, str]]) -> tuple[list[dict[str, object]], dict[str, object]]:
    rows = []
    lengths = []
    agg = {"A": 0, "C": 0, "G": 0, "T": 0, "N": 0, "OTHER": 0}
    for rec in records:
        c = counts(rec["sequence"])
        for key in agg:
            agg[key] += c[key]
        length = len(rec["sequence"])
        lengths.append(length)
        rows.append({"record_id": rec["id"], "length": length, "gc_fraction": gc(c), **c})
    return rows, {"sequence_count": len(records), "total_bases": sum(lengths), "length_min": min(lengths), "length_max": max(lengths), "length_mean": sum(lengths) / len(lengths), "aggregate_counts": agg, "aggregate_gc_fraction": gc(agg)}


def pairwise(records: list[dict[str, str]]) -> tuple[list[dict[str, object]], dict[str, object]]:
    rows = []
    vals = []
    for i, a in enumerate(records):
        for b in records[i + 1:]:
            if len(a["sequence"]) != len(b["sequence"]):
                rows.append({"left_id": a["id"], "right_id": b["id"], "status": "SKIPPED_UNEQUAL_LENGTH"})
                continue
            comp = 0
            mis = 0
            for x, y in zip(a["sequence"], b["sequence"], strict=True):
                if x in CANON and y in CANON:
                    comp += 1
                    if x != y:
                        mis += 1
            pd = None if comp == 0 else mis / comp
            if pd is not None:
                vals.append(pd)
            rows.append({"left_id": a["id"], "right_id": b["id"], "status": "CALCULATED", "comparable_sites": comp, "mismatches": mis, "p_distance": pd})
    return rows, {"pairs_emitted": len(rows), "mean_p_distance": sum(vals) / len(vals) if vals else None}


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    import io
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    buf = io.StringIO()
    writer = csv.DictWriter(buf, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)
    path.write_text(buf.getvalue(), encoding="utf-8")


def run(input_path: Path, dataset_id: str, output_dir: Path) -> dict[str, object]:
    did = safe_id(dataset_id)
    data = input_path.read_bytes()
    records = parse_fasta(data.decode("utf-8"))
    rec_rows, rec_summary = rows_and_summary(records)
    pair_rows, pair_summary = pairwise(records)
    output_dir.mkdir(parents=True, exist_ok=True)
    raw = output_dir / f"{did}.raw.fasta"
    rec = output_dir / f"{did}.records.csv"
    par = output_dir / f"{did}.pairwise.csv"
    met = output_dir / f"{did}.metrics.json"
    man = output_dir / f"{did}.MANIFEST.json"
    raw.write_bytes(data)
    write_csv(rec, rec_rows)
    write_csv(par, pair_rows)
    metrics = {"schema": "rll.sequence_metrics.v1", "record_summary": rec_summary, "pairwise_summary": pair_summary, "claim_boundary": BOUNDARY}
    met.write_text(json.dumps(metrics, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    manifest = {"schema": "rll.sequence_metrics_manifest.v1", "status": "CALCULATED_CLAIM_BOUNDED", "generated_utc": datetime.now(timezone.utc).isoformat(), "dataset_id": did, "source_path": str(input_path), "source_sha256": digest(data), "artifacts": {"raw_fasta": str(raw), "records_csv": str(rec), "pairwise_csv": str(par), "metrics_json": str(met)}, "claim_boundary": BOUNDARY}
    man.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--dataset-id", required=True)
    parser.add_argument("--output-dir", type=Path, default=Path("data/real/evolutionary"))
    args = parser.parse_args()
    print(json.dumps(run(args.input, args.dataset_id, args.output_dir), indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
