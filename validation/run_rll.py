import json
import numpy as np
import os
from validation.load_data import load_real_data

def rll(z):
    return 70 * np.sqrt(0.3 * (1 + z)**3 + 0.7) + 0.1*np.log(1 + z)

if __name__ == "__main__":
    os.makedirs("validation_outputs", exist_ok=True)

    z, y, yerr = load_real_data()
    pred = rll(z)

    with open("validation_outputs/rll.json", "w") as f:
        json.dump({"model": "RLL", "values": pred.tolist()}, f)

    print("✔ RLL done")
