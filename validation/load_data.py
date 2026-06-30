import glob
import numpy as np
import pandas as pd

def load_real_data():
    files = glob.glob("data/*.csv")

    if not files:
        print("⚠️ fallback simulado ativo")
        z = np.linspace(0.01, 1.5, 50)
        y = np.random.normal(70, 5, len(z))
        yerr = np.ones_like(z)
        return z, y, yerr

    df = pd.read_csv(files[0])

    z = df.iloc[:, 0].values
    y = df.iloc[:, 1].values if df.shape[1] > 1 else np.zeros_like(z)
    yerr = df.iloc[:, 2].values if df.shape[1] > 2 else np.ones_like(z)

    print(f"📦 DATA REAL: {files[0]} | N={len(z)}")

    return z, y, yerr
