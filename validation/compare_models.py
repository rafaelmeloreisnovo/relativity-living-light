import json
import os
import sys
from pathlib import Path

import numpy as np

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from validation.load_data import load_real_data


if __name__ == "__main__":
    os.makedirs("validation_outputs", exist_ok=True)

    z, y, yerr = load_real_data()

    lcdm = json.load(open("validation_outputs/lcdm.json", encoding="utf-8"))
    rll = json.load(open("validation_outputs/rll.json", encoding="utf-8"))

    lcdm_vals = np.array(lcdm["values"], dtype=float)
    rll_vals = np.array(rll["values"], dtype=float)

    chi_lcdm = np.sum(((lcdm_vals - y) / (yerr + 1e-8)) ** 2)
    chi_rll = np.sum(((rll_vals - y) / (yerr + 1e-8)) ** 2)

    result = {
        "chi2_lcdm": float(chi_lcdm),
        "chi2_rll": float(chi_rll),
        "delta": float(chi_lcdm - chi_rll),
        "claim_boundary": "comparison metric only; no superiority claim without predefined real-data thresholds",
    }

    with open("validation_outputs/comparison.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print("RESULT:", result)
