import json
import os
import sys
from pathlib import Path

import numpy as np

if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from validation.load_data import load_real_data


def lcdm(z):
    return 70 * np.sqrt(0.3 * (1 + z) ** 3 + 0.7)


if __name__ == "__main__":
    os.makedirs("validation_outputs", exist_ok=True)

    z, y, yerr = load_real_data()
    pred = lcdm(z)

    with open("validation_outputs/lcdm.json", "w", encoding="utf-8") as f:
        json.dump({"model": "LCDM", "values": pred.tolist()}, f)

    print("LCDM done")
