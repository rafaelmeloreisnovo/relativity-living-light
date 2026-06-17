#!/usr/bin/env python3
"""
rll_dark_lensing_node.py

Minimal validator for the RLL dark-lensing node.

Purpose:
  Convert a gravitational-lensing observational record into a simple
  RLL coherence score while preserving claim boundaries.

Usage:
  cat > dark_lensing_cases.csv << 'EOF'
  case,mass_msun,mass_sigma,lensing_score,darkness_score,model_risk,degeneracy_risk,noise_risk
  B1938_666_dark_object,1000000,0.25,0.95,0.90,0.20,0.30,0.10
  EOF

  python3 scripts/rll_dark_lensing_node.py dark_lensing_cases.csv
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path


EPS = 1e-12


@dataclass(frozen=True)
class DarkLensingCase:
    case: str
    mass_msun: float
    mass_sigma: float
    lensing_score: float
    darkness_score: float
    model_risk: float
    degeneracy_risk: float
    noise_risk: float

    @staticmethod
    def clamp01(x: float) -> float:
        if x < 0.0:
            return 0.0
        if x > 1.0:
            return 1.0
        return x

    @classmethod
    def from_row(cls, row: dict[str, str]) -> "DarkLensingCase":
        return cls(
            case=(row.get("case") or "unnamed_case").strip(),
            mass_msun=float(row.get("mass_msun", "0") or 0),
            mass_sigma=cls.clamp01(float(row.get("mass_sigma", "1") or 1)),
            lensing_score=cls.clamp01(float(row.get("lensing_score", "0") or 0)),
            darkness_score=cls.clamp01(float(row.get("darkness_score", "0") or 0)),
            model_risk=cls.clamp01(float(row.get("model_risk", "1") or 1)),
            degeneracy_risk=cls.clamp01(float(row.get("degeneracy_risk", "1") or 1)),
            noise_risk=cls.clamp01(float(row.get("noise_risk", "1") or 1)),
        )

    def coherence(self) -> float:
        # P_mass penalizes relative uncertainty: sigma=0 => 1; sigma=1 => 0.
        p_mass = self.clamp01(1.0 - self.mass_sigma)
        numerator = self.lensing_score * p_mass * self.darkness_score
        denominator = self.model_risk + self.degeneracy_risk + self.noise_risk + EPS
        return self.clamp01(numerator / denominator)

    def classify(self) -> str:
        c = self.coherence()
        if c >= 0.85:
            return "strong_candidate"
        if c >= 0.60:
            return "moderate_candidate"
        if c >= 0.35:
            return "weak_candidate"
        return "insufficient"

    def note(self) -> str:
        label = self.classify()
        if label == "strong_candidate":
            return "compatible_with_hidden_mass_not_direct_particle_detection"
        if label == "moderate_candidate":
            return "useful_case_requires_model_and_degeneracy_audit"
        if label == "weak_candidate":
            return "keep_as_context_not_validation_grade"
        return "insufficient_for_rll_case_promotion"


def read_cases(path: Path) -> list[DarkLensingCase]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return [DarkLensingCase.from_row(row) for row in reader]


def print_table(cases: list[DarkLensingCase]) -> None:
    print("case,mass_msun,coherence,class,note")
    for item in cases:
        print(
            f"{item.case},"
            f"{item.mass_msun:.6g},"
            f"{item.coherence():.6f},"
            f"{item.classify()},"
            f"{item.note()}"
        )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compute a minimal RLL coherence score for dark-lensing cases."
    )
    parser.add_argument("csv_path", type=Path, help="Input CSV with dark-lensing fields.")
    args = parser.parse_args()

    cases = read_cases(args.csv_path)
    if not cases:
        raise SystemExit("no cases found in CSV")

    print_table(cases)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
