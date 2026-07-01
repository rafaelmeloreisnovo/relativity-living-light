from __future__ import annotations

from pathlib import Path


FETCHER = Path("scripts/fetch_public_astronomy_catalog_samples.py")
DOC = Path("docs/real_data/PUBLIC_ASTRONOMY_CATALOG_FETCHER.md")

BLOCKED_CLAIMS = [
    "RLL is validated",
    "dark matter is measured",
    "dark energy is confirmed",
    "CMB likelihood is reproduced",
    "validate cosmology",
]

REQUIRED_FETCHER_TERMS = [
    "data/real/astronomy",
    "data/provenance",
    "data/examples",
    "SYNTHETIC_TEMPLATE",
    "REAL_CATALOG_SAMPLE",
    "REAL_AGGREGATED_CATALOG",
    "not a cosmology likelihood",
    "not RLL validation",
]

REQUIRED_DOC_TERMS = [
    "not_cosmology_validation",
    "CLAIM_BLOCKED",
    "SYNTHETIC_TEMPLATE",
    "data/examples/cmb_power_spectrum_template.json",
    "must not be written under",
    "data/real/**",
]


def require_file(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8")


def main() -> int:
    fetcher = require_file(FETCHER)
    doc = require_file(DOC)

    for term in REQUIRED_FETCHER_TERMS:
        if term not in fetcher:
            raise ValueError(f"fetcher missing required boundary term: {term!r}")

    for term in REQUIRED_DOC_TERMS:
        if term not in doc:
            raise ValueError(f"documentation missing required boundary term: {term!r}")

    # Guard the highest-risk error: generated CMB template must never be saved under data/real.
    forbidden_patterns = [
        'out_dir / "cmb_power_spectrum_template.json"',
        '"data/real/cmb_power_spectrum_template.json"',
        '"data/real/cmb_power_spectrum.json"',
        '"data/real/astronomy/cmb_power_spectrum_template.json"',
    ]
    for pattern in forbidden_patterns:
        if pattern in fetcher:
            raise ValueError(f"generated CMB template appears to be written under data/real: {pattern}")

    # Block validation language unless it appears in blocked-claim context.
    for claim in BLOCKED_CLAIMS:
        if claim in fetcher and "BLOCKED_CLAIMS" not in fetcher:
            raise ValueError(f"claim appears outside explicit blocked-claim context: {claim}")

    print("OK: public astronomy catalog fetcher preserves real-data claim boundaries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
