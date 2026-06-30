import json
import numpy as np
import os
from validation.load_data import load_real_data

if __name__ == "__main__":

    os.makedirs("validation_outputs", exist_ok=True)

    z, y, yerr = load_real_data()

    lcdm = json.load(open("validation_outputs/lcdm.json"))
    rll  = json.load(open("validation_outputs/rll.json"))

    lcdm_vals = np.array(lcdm["values"])
    rll_vals  = np.array(rll["values"])

    chi_lcdm = np.sum((lcdm_vals - y)**2 / (yerr + 1e-8))
    chi_rll  = np.sum((rll_vals - y)**2 / (yerr + 1e-8))

    result = {
        "chi2_lcdm": float(chi_lcdm),
        "chi2_rll": float(chi_rll),
        "delta": float(chi_lcdm - chi_rll)
    }

    with open("validation_outputs/comparison.json", "w") as f:
        json.dump(result, f)

    print("RESULT:", result)
