#!/usr/bin/env python3
"""Fetch a Mars heliocentric state-vector sample from NASA/JPL Horizons.

This script downloads a small VECTORS table for Mars relative to the Sun and
stores it as a local raw CSV with metadata. It is intended to run in GitHub
Actions, where outbound network access is available.
"""

from __future__ import annotations

import csv
import hashlib
import urllib.parse
import urllib.request
from pathlib import Path

RAW_CSV = Path("data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.csv")
META_YML = Path("data/raw/orbital_dynamics/ephemerides/jpl_horizons_mars_vectors_2006_sample.meta.yml")

PARAMS = {
    "format": "text",
    "COMMAND": "'499'",
    "OBJ_DATA": "NO",
    "MAKE_EPHEM": "YES",
    "EPHEM_TYPE": "VECTORS",
    "CENTER": "'500@10'",
    "START_TIME": "'2006-01-01'",
    "STOP_TIME": "'2006-01-02'",
    "STEP_SIZE": "'1 d'",
    "OUT_UNITS": "'KM-S'",
    "VEC_TABLE": "'2'",
    "CSV_FORMAT": "YES",
    "TIME_TYPE": "TDB",
}

URL = "https://ssd.jpl.nasa.gov/api/horizons.api?" + urllib.parse.urlencode(PARAMS, quote_via=urllib.parse.quote)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def numeric(value: str) -> float:
    return float(value.strip().replace("D", "E"))


def parse_vector_lines(text: str) -> list[dict[str, object]]:
    in_table = False
    rows: list[dict[str, object]] = []
    for raw in text.splitlines():
        line = raw.strip()
        if line == "$$SOE":
            in_table = True
            continue
        if line == "$$EOE":
            break
        if not in_table or not line:
            continue
        parts = [p.strip() for p in line.split(",")]
        # Expected CSV VEC_TABLE=2 shape:
        # JD, Calendar Date, X, Y, Z, VX, VY, VZ
        if len(parts) < 8:
            continue
        try:
            rows.append({
                "jd_tdb": numeric(parts[0]),
                "calendar_tdb": parts[1],
                "x_km": numeric(parts[2]),
                "y_km": numeric(parts[3]),
                "z_km": numeric(parts[4]),
                "vx_km_s": numeric(parts[5]),
                "vy_km_s": numeric(parts[6]),
                "vz_km_s": numeric(parts[7]),
            })
        except ValueError:
            continue
    return rows


def main() -> int:
    RAW_CSV.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(URL, timeout=60) as response:
        text = response.read().decode("utf-8", errors="replace")

    rows = parse_vector_lines(text)
    if not rows:
        raise RuntimeError("No vector rows parsed from Horizons response")

    with RAW_CSV.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["jd_tdb", "calendar_tdb", "x_km", "y_km", "z_km", "vx_km_s", "vy_km_s", "vz_km_s"],
            lineterminator="\n",
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    digest = sha256_file(RAW_CSV)
    size = RAW_CSV.stat().st_size
    META_YML.write_text(
        "schema_version: 0.1\n"
        "status: raw_file_present_hash_ready\n"
        "claim_allowed: false\n"
        "raw_id: RAW_JPL_HORIZONS_MARS_VECTORS_2006_SAMPLE\n"
        "route_id: orbital_shape_angular_momentum\n"
        "record_id: REAL_ORBIT_MARS_HELIOCENTRIC_SHAPE_AM_V1\n"
        "raw_role: heliocentric_cartesian_state_vector_sample\n"
        "source:\n"
        "  provider: NASA/JPL Horizons API\n"
        f"  source_url: {URL!r}\n"
        "  access_date_utc: generated_by_ci_runtime\n"
        "  source_version: Horizons API runtime response\n"
        "  license_or_terms: NASA/JPL public API output; verify downstream reuse terms before redistribution outside this repository\n"
        "local:\n"
        f"  path: {RAW_CSV.as_posix()}\n"
        f"  sha256: {digest}\n"
        f"  bytes: {size}\n"
        "  raw_data_local: true\n"
        "claim_boundary:\n"
        "  state_vector_sample_is_not_full_validation: true\n"
        "  baseline_required_for_metric_claim: true\n"
        "  uncertainty_required_for_metric_claim: true\n"
        "  claim_allowed: false\n"
        "safe_conclusion: Raw Horizons vector sample is locally present and checksummed against the canonical LF-normalized repository artifact, but claims remain blocked pending baseline and uncertainty model.\n",
        encoding="utf-8",
    )

    print(f"wrote {RAW_CSV}")
    print(f"wrote {META_YML}")
    print(f"sha256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
