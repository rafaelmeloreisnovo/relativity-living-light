import os
import pandas as pd
from .likelihood import chi2_blocks, covariance_usage_summary, aic, bic, load_csv, evaluate_model
from .models import model_LCDM_Hz, model_RLL_like_Hz, model_LCDM_fs8, model_RLL_like_fs8
from .sensitivity import sensitivity_table_by_redshift

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
DATA = os.path.join(BASE_DIR, "data", "inputs", "structure_d")
RESULTS = os.path.join(BASE_DIR, "results", "structure_d")


def _base_blocks():
    hz = load_csv(os.path.join(DATA, "Hz.csv"), ["z", "Hz", "sigma"])
    fs8 = load_csv(os.path.join(DATA, "fsigma8.csv"), ["z", "fs8", "sigma"])
    return hz, fs8


def main():
    os.makedirs(RESULTS, exist_ok=True)
    rows = []

    hz, fs8 = _base_blocks()

    lcdm = dict(H0=70.0, Om=0.3, Ol=0.7, sigma8=0.8, gamma=0.55)
    rll = dict(H0=70.0, Om=0.3, Ol=0.7, sigma8=0.8, gamma=0.55, alpha=0.06, z_peak=2.0, width=1.2, beta=0.00)

    fit_params_lcdm = ["H0", "Om", "sigma8", "gamma"]
    fit_params_rll = fit_params_lcdm + ["alpha", "z_peak", "width"]
    fixed_params_lcdm = sorted(set(lcdm) - set(fit_params_lcdm))
    fixed_params_rll = sorted(set(rll) - set(fit_params_rll))

    z_hz = hz["z"].to_numpy()
    z_fs = fs8["z"].to_numpy()

    blocks_lcdm_active = [
        {"name": "fσ8", "obs": fs8["fs8"].to_numpy(), "mod": model_LCDM_fs8(z_fs, lcdm), "sigma": fs8["sigma"].to_numpy()},
        {"name": "Hz", "obs": hz["Hz"].to_numpy(), "mod": model_LCDM_Hz(z_hz, lcdm), "sigma": hz["sigma"].to_numpy()},
    ]

    blocks_rll_active = [
        {"name": "fσ8", "obs": fs8["fs8"].to_numpy(), "mod": model_RLL_like_fs8(z_fs, rll), "sigma": fs8["sigma"].to_numpy()},
        {"name": "Hz", "obs": hz["Hz"].to_numpy(), "mod": model_RLL_like_Hz(z_hz, rll), "sigma": hz["sigma"].to_numpy()},
    ]

    chi2_lcdm, _ = chi2_blocks(blocks_lcdm_active, diagonal_fallback=True)
    chi2_rll, _ = chi2_blocks(blocks_rll_active, diagonal_fallback=True)

    N = len(hz) + len(fs8)
    k_lcdm = len(fit_params_lcdm)
    k_rll = len(fit_params_rll)

    rows.append(dict(model="LCDM", chi2=chi2_lcdm, AIC=aic(chi2_lcdm, k_lcdm), BIC=bic(chi2_lcdm, k_lcdm, N), N=N, k=k_lcdm,
                     fit_params=",".join(fit_params_lcdm), fixed_params=",".join(fixed_params_lcdm)))
    rows.append(dict(model="RLL_like+AGN", chi2=chi2_rll, AIC=aic(chi2_rll, k_rll), BIC=bic(chi2_rll, k_rll, N), N=N, k=k_rll,
                     fit_params=",".join(fit_params_rll), fixed_params=",".join(fixed_params_rll)))

    out = os.path.join(RESULTS, "model_comparison.csv")
    df = evaluate_model(rows, out)

    cov_rows = []
    expected_blocks = ["SNe", "BAO", "fσ8", "lenses", "Hz"]
    for model_name, active_blocks in (("LCDM", blocks_lcdm_active), ("RLL_like+AGN", blocks_rll_active)):
        summary_df = covariance_usage_summary(active_blocks, diagonal_fallback=True)
        missing = [
            {"block": b, "covariance_mode": "not_used", "has_full_covariance": False, "has_diagonal_sigma": False}
            for b in expected_blocks if b not in set(summary_df["block"].tolist())
        ]
        if missing:
            summary_df = pd.concat([summary_df, pd.DataFrame(missing)], ignore_index=True)
        summary_df.insert(0, "model", model_name)
        cov_rows.append(summary_df)
    cov_out = os.path.join(RESULTS, "covariance_usage.csv")
    evaluate_model([r for d in cov_rows for r in d.to_dict(orient="records")], cov_out)

    sens_out = os.path.join(RESULTS, "rll_sensitivity_derivatives.csv")
    sensitivity_table_by_redshift().to_csv(sens_out, index=False)

    print(df.to_string(index=False))
    print(f"\nWrote: {out}")
    print(f"Wrote: {cov_out}")
    print(f"Wrote: {sens_out}")


if __name__ == "__main__":
    main()
