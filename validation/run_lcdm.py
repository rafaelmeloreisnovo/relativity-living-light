import json
import numpy as np
from validation.load_data import load_real_data

def lcdm(z):
    return 70 * np.sqrt(0.3 * (1 + z)**3 + 0.7)

if __name__ == "__main__":
    z, y, yerr = load_real_data()
    pred = lcdm(z)

    result = {
        "model": "LCDM",
        "values": pred.tolist()
    }

    with open("validation_outputs/lcdm.json", "w") as f:
        json.dump(result, f)
