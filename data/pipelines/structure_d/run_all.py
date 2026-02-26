import os
from .likelihood import chi2, aic, bic, load_csv, evaluate_model
from .models import model_LCDM_Hz, model_RLL_like_Hz, model_LCDM_fs8, model_RLL_like_fs8
from .systematics import build_systematics_config

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
DATA = os.path.join(BASE_DIR, "data", "inputs", "structure_d")
RESULTS = os.path.join(BASE_DIR, "results", "structure_d")


def _h0_seed_from_prior(h0_prior):
    distribution = h0_prior.get("distribution")
    if distribution == "gaussian":
        return float(h0_prior["mean"])
    if distribution == "uniform":
        return 0.5 * (float(h0_prior["min"]) + float(h0_prior["max"]))
    raise ValueError(f"Unsupported H0 prior distribution: {distribution}")


def main(h0_scenario="Planck_like"):
    os.makedirs(RESULTS, exist_ok=True)
    rows = []

    experiments = ("Hz", "fsigma8")
    systematics_config = build_systematics_config(experiments, h0_scenario=h0_scenario)
    h0_seed = _h0_seed_from_prior(systematics_config["h0"]["prior"])

    hz = load_csv(os.path.join(DATA, "Hz.csv"), ["z", "Hz", "sigma"])
    fs8 = load_csv(os.path.join(DATA, "fsigma8.csv"), ["z", "fs8", "sigma"])

    lcdm = dict(H0=h0_seed, Om=0.3, Ol=0.7, sigma8=0.8, gamma=0.55)
    rll = dict(H0=h0_seed, Om=0.3, Ol=0.7, sigma8=0.8, gamma=0.55, alpha=0.06, z_peak=2.0, width=1.2, beta=0.00)

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

    traceability = systematics_config["traceability"]
    base_row = dict(
        h0_scenario=traceability["h0_scenario"],
        h0_prior_reference=traceability["h0_prior_reference"],
        systematics_Hz=",".join(systematics_config["by_experiment"]["Hz"]["active_systematics"]),
        systematics_fsigma8=",".join(systematics_config["by_experiment"]["fsigma8"]["active_systematics"]),
    )

    rows.append(dict(model="LCDM", chi2=chi2_lcdm, AIC=aic(chi2_lcdm, k_lcdm), BIC=bic(chi2_lcdm, k_lcdm, N), N=N, k=k_lcdm,
                     fit_params=",".join(fit_params_lcdm), fixed_params=",".join(fixed_params_lcdm), **base_row))
    rows.append(dict(model="RLL_like+AGN", chi2=chi2_rll, AIC=aic(chi2_rll, k_rll), BIC=bic(chi2_rll, k_rll, N), N=N, k=k_rll,
                     fit_params=",".join(fit_params_rll), fixed_params=",".join(fixed_params_rll), **base_row))

    out = os.path.join(RESULTS, "model_comparison.csv")
    df = evaluate_model(rows, out)
    print(df.to_string(index=False))
    print(f"\nWrote: {out}")


if __name__ == "__main__":
    main()
