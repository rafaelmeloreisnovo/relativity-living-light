"""Ferramentas de inferência para o pipeline ``structure_d``.

Este módulo define espaços de parâmetros por modelo e funções explícitas para
cálculo de log-verossimilhança conjunta, log-prior, log-posterior,
amostragem MCMC (``emcee``) e evidência Bayesiana via nested sampling
(``dynesty``).
"""

from __future__ import annotations

import os
import time

import numpy as np

from .models import (
    model_LCDM_Hz,
    model_LCDM_fs8,
    model_RLL_like_Hz,
    model_RLL_like_fs8,
)


MODEL_PARAMETER_PRIORS = {
    "lcdm": {
        "H0": {"prior": "uniform", "min": 50.0, "max": 90.0},
        "Om": {"prior": "uniform", "min": 0.1, "max": 0.5},
        "Ol": {"prior": "uniform", "min": 0.5, "max": 0.9},
        "sigma8": {"prior": "uniform", "min": 0.5, "max": 1.1},
        "gamma": {"prior": "uniform", "min": 0.3, "max": 0.8},
    },
    "rll_like_agn": {
        "H0": {"prior": "uniform", "min": 50.0, "max": 90.0},
        "Om": {"prior": "uniform", "min": 0.1, "max": 0.5},
        "Ol": {"prior": "uniform", "min": 0.5, "max": 0.9},
        "sigma8": {"prior": "uniform", "min": 0.5, "max": 1.1},
        "gamma": {"prior": "uniform", "min": 0.3, "max": 0.8},
        "alpha": {"prior": "uniform", "min": 0.0, "max": 0.25},
        "z_peak": {"prior": "uniform", "min": 0.2, "max": 4.0},
        "width": {"prior": "uniform", "min": 0.1, "max": 3.0},
        "beta": {"prior": "uniform", "min": -0.5, "max": 0.5},
    },
}


def _get_model_prior_spec(model_name):
    if model_name not in MODEL_PARAMETER_PRIORS:
        raise ValueError(f"Unknown model_name: {model_name}")
    return MODEL_PARAMETER_PRIORS[model_name]


def _theta_to_params(theta, model_name):
    spec = _get_model_prior_spec(model_name)
    theta = np.asarray(theta, dtype=float)
    param_names = list(spec)
    if theta.shape[-1] != len(param_names):
        raise ValueError(
            f"theta length {theta.shape[-1]} incompatible with model '{model_name}' "
            f"({len(param_names)} parameters)."
        )
    return {name: float(theta[i]) for i, name in enumerate(param_names)}


def _validated_sigma_array(sigma):
    sigma_arr = np.asarray(sigma, dtype=float)
    if np.any(~np.isfinite(sigma_arr)) or np.any(sigma_arr <= 0.0):
        raise ValueError("sigma must contain only finite, strictly positive values")
    return sigma_arr


def _chi2(obs, mod, sigma):
    sigma = _validated_sigma_array(sigma)
    resid = (np.asarray(obs, dtype=float) - np.asarray(mod, dtype=float)) / sigma
    return float(np.sum(resid * resid))


def _column(data, key):
    if hasattr(data, "__getitem__"):
        values = data[key]
        if hasattr(values, "to_numpy"):
            values = values.to_numpy()
        return np.asarray(values, dtype=float)
    raise TypeError(f"Unsupported data container for key '{key}'")


def log_likelihood_joint(theta, model_name, data_hz, data_fs8):
    """Calcula log-verossimilhança conjunta de H(z) e fσ8.

    Signature:
        log_likelihood_joint(theta, model_name, data_hz, data_fs8)

    Parameter order:
        1) theta: array-like no mesmo ordenamento de ``MODEL_PARAMETER_PRIORS[model_name]``
        2) model_name: ``"lcdm"`` ou ``"rll_like_agn"``
        3) data_hz: estrutura com colunas/chaves ``z``, ``Hz`` e ``sigma``
        4) data_fs8: estrutura com colunas/chaves ``z``, ``fs8`` e ``sigma``

    Returns:
        float: ``-0.5 * (chi2_hz + chi2_fs8)``.
    """
    params = _theta_to_params(theta, model_name)

    if model_name == "lcdm":
        hz_model = model_LCDM_Hz(_column(data_hz, "z"), params)
        fs_model = model_LCDM_fs8(_column(data_fs8, "z"), params)
    elif model_name == "rll_like_agn":
        hz_model = model_RLL_like_Hz(_column(data_hz, "z"), params)
        fs_model = model_RLL_like_fs8(_column(data_fs8, "z"), params)
    else:
        raise ValueError(f"Unknown model_name: {model_name}")

    chi2_hz = _chi2(_column(data_hz, "Hz"), hz_model, _column(data_hz, "sigma"))
    chi2_fs = _chi2(_column(data_fs8, "fs8"), fs_model, _column(data_fs8, "sigma"))
    return float(-0.5 * (chi2_hz + chi2_fs))


def log_prior(theta, model_name):
    """Calcula log-prior para ``theta`` com suporte mínimo a prior uniforme.

    Signature:
        log_prior(theta, model_name)

    Parameter order:
        1) theta: array-like no ordenamento de ``MODEL_PARAMETER_PRIORS[model_name]``
        2) model_name: ``"lcdm"`` ou ``"rll_like_agn"``

    Returns:
        float: ``0.0`` dentro do suporte uniforme e ``-np.inf`` fora do suporte.
    """
    spec = _get_model_prior_spec(model_name)
    theta = np.asarray(theta, dtype=float)

    if theta.shape[-1] != len(spec):
        return -np.inf

    for idx, (name, prior_cfg) in enumerate(spec.items()):
        if prior_cfg.get("prior") != "uniform":
            raise ValueError(f"Unsupported prior type for '{name}': {prior_cfg.get('prior')}")
        vmin = float(prior_cfg["min"])
        vmax = float(prior_cfg["max"])
        value = float(theta[idx])
        if not (vmin <= value <= vmax):
            return -np.inf

    return 0.0


def log_posterior(theta, model_name, data_hz, data_fs8):
    """Calcula log-posterior como soma de log-prior e log-likelihood conjunta.

    Signature:
        log_posterior(theta, model_name, data_hz, data_fs8)

    Parameter order:
        1) theta
        2) model_name
        3) data_hz
        4) data_fs8

    Returns:
        float: ``log_prior(theta, model_name) + log_likelihood_joint(...)``.
    """
    lp = log_prior(theta, model_name)
    if not np.isfinite(lp):
        return -np.inf
    return float(lp + log_likelihood_joint(theta, model_name, data_hz, data_fs8))


def run_mcmc_emcee(
    model_name,
    data_hz,
    data_fs8,
    nwalkers=32,
    nsteps=2000,
    burnin=None,
    thin=1,
    initial_theta=None,
    random_seed=42,
    progress=False,
):
    """Executa MCMC com ``emcee`` e retorna saída padronizada.

    Signature:
        run_mcmc_emcee(model_name, data_hz, data_fs8, nwalkers=32, nsteps=2000,
                       burnin=None, thin=1, initial_theta=None, random_seed=42,
                       progress=False)

    Parameter order:
        1) model_name
        2) data_hz
        3) data_fs8
        4+) hiperparâmetros do sampler

    Returns:
        dict com:
        - ``model_name``: str
        - ``param_names``: list[str]
        - ``chain_flat``: ndarray [nsamples, ndim]
        - ``log_prob_flat``: ndarray [nsamples]
        - ``acceptance_fraction_mean``: float
        - ``autocorr_time``: ndarray | None
        - ``burnin``: int
        - ``thin``: int
        - ``sampler``: objeto sampler ``emcee.EnsembleSampler``
    """
    try:
        import emcee
    except ImportError as exc:
        raise ImportError("run_mcmc_emcee requires 'emcee' installed") from exc

    prior_spec = _get_model_prior_spec(model_name)
    param_names = list(prior_spec)
    ndim = len(param_names)

    rng = np.random.default_rng(random_seed)

    if initial_theta is None:
        initial_theta = np.array(
            [0.5 * (cfg["min"] + cfg["max"]) for cfg in prior_spec.values()],
            dtype=float,
        )
    else:
        initial_theta = np.asarray(initial_theta, dtype=float)

    if initial_theta.shape[-1] != ndim:
        raise ValueError(f"initial_theta must have length {ndim}")

    span = np.array([cfg["max"] - cfg["min"] for cfg in prior_spec.values()], dtype=float)
    p0 = initial_theta + 1e-3 * span * rng.normal(size=(nwalkers, ndim))

    sampler = emcee.EnsembleSampler(
        nwalkers,
        ndim,
        log_posterior,
        args=(model_name, data_hz, data_fs8),
    )
    sampler.run_mcmc(p0, nsteps, progress=progress)

    if burnin is None:
        burnin = max(0, nsteps // 4)

    chain_flat = sampler.get_chain(discard=burnin, thin=thin, flat=True)
    log_prob_flat = sampler.get_log_prob(discard=burnin, thin=thin, flat=True)
    acceptance_fraction_mean = float(np.mean(sampler.acceptance_fraction))

    autocorr_time = None
    try:
        autocorr_time = sampler.get_autocorr_time(tol=0)
    except Exception:
        autocorr_time = None

    return {
        "model_name": model_name,
        "param_names": param_names,
        "chain_flat": chain_flat,
        "log_prob_flat": log_prob_flat,
        "acceptance_fraction_mean": acceptance_fraction_mean,
        "autocorr_time": autocorr_time,
        "burnin": int(burnin),
        "thin": int(thin),
        "sampler": sampler,
    }


def run_nested_dynesty(
    model_name,
    data_hz,
    data_fs8,
    nlive=400,
    bound="multi",
    sample="rwalk",
    random_seed=42,
):
    """Executa nested sampling com ``dynesty`` e retorna evidência Bayesiana.

    Signature:
        run_nested_dynesty(model_name, data_hz, data_fs8, nlive=400,
                           bound="multi", sample="rwalk", random_seed=42)

    Parameter order:
        1) model_name
        2) data_hz
        3) data_fs8
        4+) hiperparâmetros do nested sampler

    Returns:
        dict com:
        - ``model_name``: str
        - ``param_names``: list[str]
        - ``logZ``: float
        - ``logZ_err``: float
        - ``results``: objeto ``dynesty.results.Results``
    """
    try:
        from dynesty import DynamicNestedSampler
    except ImportError as exc:
        raise ImportError("run_nested_dynesty requires 'dynesty' installed") from exc

    prior_spec = _get_model_prior_spec(model_name)
    param_names = list(prior_spec)
    ndim = len(param_names)

    def prior_transform(u):
        u = np.asarray(u, dtype=float)
        theta = np.empty(ndim, dtype=float)
        for i, cfg in enumerate(prior_spec.values()):
            if cfg.get("prior") != "uniform":
                raise ValueError(f"Unsupported prior type: {cfg.get('prior')}")
            vmin = float(cfg["min"])
            vmax = float(cfg["max"])
            theta[i] = vmin + u[i] * (vmax - vmin)
        return theta

    def loglike(theta):
        return log_likelihood_joint(theta, model_name, data_hz, data_fs8)

    sampler = DynamicNestedSampler(
        loglike,
        prior_transform,
        ndim,
        bound=bound,
        sample=sample,
        rstate=np.random.default_rng(random_seed),
    )
    sampler.run_nested(nlive_init=nlive, print_progress=False)

    results = sampler.results
    logz = float(results.logz[-1])
    logz_err = float(results.logzerr[-1])

    return {
        "model_name": model_name,
        "param_names": param_names,
        "logZ": logz,
        "logZ_err": logz_err,
        "results": results,
    }


def _standardize_input_data(hz, fs8):
    hz_data = {
        "z": _column(hz, "z"),
        "Hz": _column(hz, "Hz"),
        "sigma": _column(hz, "sigma"),
    }
    fs8_data = {
        "z": _column(fs8, "z"),
        "fs8": _column(fs8, "fs8"),
        "sigma": _column(fs8, "sigma"),
    }
    return hz_data, fs8_data


def _build_bayes_summary(model_name, nested_result, *, seed, nwalkers, nsteps, nlive, output_dir, elapsed_seconds):
    os.makedirs(output_dir, exist_ok=True)
    run_timestamp_utc = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    row = {
        "model": model_name,
        "logZ": float(nested_result["logZ"]),
        "logZ_err": float(nested_result["logZ_err"]),
        "seed": int(seed),
        "nwalkers": int(nwalkers),
        "nsteps": int(nsteps),
        "nlive": int(nlive),
        "output_dir": output_dir,
        "run_timestamp_utc": run_timestamp_utc,
        "elapsed_seconds": float(elapsed_seconds),
    }
    return {
        "model": model_name,
        "logZ": float(nested_result["logZ"]),
        "logZ_err": float(nested_result["logZ_err"]),
        "metadata": {
            "seed": int(seed),
            "nwalkers": int(nwalkers),
            "nsteps": int(nsteps),
            "nlive": int(nlive),
            "output_dir": output_dir,
            "run_timestamp_utc": run_timestamp_utc,
            "elapsed_seconds": float(elapsed_seconds),
        },
        "row": row,
    }


def run_lcdm_bayes(hz, fs8, seed=42, nwalkers=32, nsteps=2000, nlive=400, output_dir="results/structure_d"):
    hz_data, fs8_data = _standardize_input_data(hz, fs8)
    t0 = time.perf_counter()
    nested_result = run_nested_dynesty(
        "lcdm",
        hz_data,
        fs8_data,
        nlive=nlive,
        random_seed=seed,
    )
    elapsed = time.perf_counter() - t0
    return _build_bayes_summary(
        "lcdm",
        nested_result,
        seed=seed,
        nwalkers=nwalkers,
        nsteps=nsteps,
        nlive=nlive,
        output_dir=output_dir,
        elapsed_seconds=elapsed,
    )


def run_rll_like_agn_bayes(hz, fs8, seed=42, nwalkers=32, nsteps=2000, nlive=400, output_dir="results/structure_d"):
    hz_data, fs8_data = _standardize_input_data(hz, fs8)
    t0 = time.perf_counter()
    nested_result = run_nested_dynesty(
        "rll_like_agn",
        hz_data,
        fs8_data,
        nlive=nlive,
        random_seed=seed,
    )
    elapsed = time.perf_counter() - t0
    return _build_bayes_summary(
        "rll_like_agn",
        nested_result,
        seed=seed,
        nwalkers=nwalkers,
        nsteps=nsteps,
        nlive=nlive,
        output_dir=output_dir,
        elapsed_seconds=elapsed,
    )
