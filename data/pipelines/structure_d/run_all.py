import os
from .likelihood import chi2, aic, bic, load_csv, evaluate_model
from .models import model_LCDM_Hz, model_RLL_like_Hz, model_LCDM_fs8, model_RLL_like_fs8

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
DATA = os.path.join(BASE_DIR, "data", "inputs", "structure_d")
RESULTS = os.path.join(BASE_DIR, "results", "structure_d")

def main():
    os.makedirs(RESULTS, exist_ok=True)
    rows = []

    hz = load_csv(os.path.join(DATA, "Hz.csv"), ["z", "Hz", "sigma"])
    fs8 = load_csv(os.path.join(DATA, "fsigma8.csv"), ["z", "fs8", "sigma"])

    lcdm = dict(H0=70.0, Om=0.3, Ol=0.7, sigma8=0.8, gamma=0.55)
    rll = dict(H0=70.0, Om=0.3, Ol=0.7, sigma8=0.8, gamma=0.55, alpha=0.06, z_peak=2.0, width=1.2, beta=0.00)

    # Fonte única para contagem de parâmetros livres usada em AIC/BIC.
    fit_params_lcdm = ["H0", "Om", "sigma8", "gamma"]
    fit_params_rll = fit_params_lcdm + ["alpha", "z_peak", "width"]
    fixed_params_lcdm = sorted(set(lcdm) - set(fit_params_lcdm))
    fixed_params_rll = sorted(set(rll) - set(fit_params_rll))

    z_hz = hz["z"].to_numpy()
    chi2_lcdm_hz = chi2(hz["Hz"].to_numpy(), model_LCDM_Hz(z_hz, lcdm), hz["sigma"].to_numpy())
    chi2_rll_hz = chi2(hz["Hz"].to_numpy(), model_RLL_like_Hz(z_hz, rll), hz["sigma"].to_numpy())

    z_fs = fs8["z"].to_numpy()
    chi2_lcdm_fs = chi2(fs8["fs8"].to_numpy(), model_LCDM_fs8(z_fs, lcdm), fs8["sigma"].to_numpy())
    chi2_rll_fs = chi2(fs8["fs8"].to_numpy(), model_RLL_like_fs8(z_fs, rll), fs8["sigma"].to_numpy())

    chi2_lcdm = chi2_lcdm_hz + chi2_lcdm_fs
    chi2_rll = chi2_rll_hz + chi2_rll_fs
    N = len(hz) + len(fs8)

    # Convenção: k conta apenas parâmetros efetivamente calibráveis (livres).
    # Parâmetros fixos em cada modelo são documentados abaixo e não entram em k.
    k_lcdm = len(fit_params_lcdm)
    k_rll = len(fit_params_rll)

    rows.append(dict(model="LCDM", chi2=chi2_lcdm, AIC=aic(chi2_lcdm, k_lcdm), BIC=bic(chi2_lcdm, k_lcdm, N), N=N, k=k_lcdm,
                     fit_params=",".join(fit_params_lcdm), fixed_params=",".join(fixed_params_lcdm)))
    rows.append(dict(model="RLL_like+AGN", chi2=chi2_rll, AIC=aic(chi2_rll, k_rll), BIC=bic(chi2_rll, k_rll, N), N=N, k=k_rll,
                     fit_params=",".join(fit_params_rll), fixed_params=",".join(fixed_params_rll)))

    out = os.path.join(RESULTS, "model_comparison.csv")
    df = evaluate_model(rows, out)
    print(df.to_string(index=False))
    print(f"\nWrote: {out}")

if __name__ == "__main__":
    main()
