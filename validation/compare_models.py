import json
import numpy as np
from validation.load_data import load_real_data

if __name__ == "__main__":

    z, y, yerr = load_real_data()

    with open("validation_outputs/lcdm.json") as f:
        lcdm = json.load(f)

    with open("validation_outputs/rll.json") as f:
        rll = json.load(f)

    lcdm_vals = np.array(lcdm["values"])
    rll_vals = np.array(rll["values"])

    # χ² simplificado com dados reais
    chi2_lcdm = np.sum((lcdm_vals - y)**2 / (yerr + 1e-8))
    chi2_rll  = np.sum((rll_vals - y)**2 / (yerr + 1e-8))

    result = {
        "chi2_lcdm": float(chi2_lcdm),
        "chi2_rll": float(chi2_rll),
        "delta": float(chi2_lcdm - chi2_rll)
    }

    with open("validation_outputs/comparison.json", "w") as f:
        json.dump(result, f)

    print(result)
