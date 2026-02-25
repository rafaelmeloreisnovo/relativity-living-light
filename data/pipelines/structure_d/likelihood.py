import numpy as np
import pandas as pd

def chi2(obs, mod, sigma):
    r = (obs - mod) / sigma
    return float(np.sum(r*r))

def aic(chi2_val, k):
    return float(chi2_val + 2*k)

def bic(chi2_val, k, N):
    return float(chi2_val + k*np.log(N))

def load_csv(path, required_cols):
    df = pd.read_csv(path)
    missing = [c for c in required_cols if c not in df.columns]
    if missing:
        raise ValueError(f"CSV {path} missing columns: {missing}")
    return df

def evaluate_model(results_rows, out_csv):
    df = pd.DataFrame(results_rows)
    df.to_csv(out_csv, index=False)
    return df
