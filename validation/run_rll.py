import numpy as np
import emcee
import json

# -----------------------------
# EQUAÇÃO-MÃE DO MODELO
# R(t) = ΛCDM(t) + β * I(t)
# -----------------------------

def lcdm_model(z, H0, Omega_m):
    # modelo simplificado (placeholder físico)
    return H0 * np.sqrt(Omega_m * (1 + z)**3 + (1 - Omega_m))

def informational_term(z):
    # 𝓘(t) — DEFINIÇÃO OPERACIONAL (ESCOLHER UMA FORMA FIXA)
    return np.log(1 + z)

def rll_model(z, H0, Omega_m, beta):
    return lcdm_model(z, H0, Omega_m) + beta * informational_term(z)


# -----------------------------
# LIKELIHOOD
# -----------------------------

def log_likelihood(theta, z, y, yerr):
    H0, Omega_m, beta = theta
    model = rll_model(z, H0, Omega_m, beta)
    sigma2 = yerr**2
    return -0.5 * np.sum((y - model)**2 / sigma2)


# -----------------------------
# PRIORS
# -----------------------------

def log_prior(theta):
    H0, Omega_m, beta = theta
    if 50 < H0 < 90 and 0.1 < Omega_m < 0.5 and -5 < beta < 5:
        return 0.0
    return -np.inf


# -----------------------------
# POSTERIOR
# -----------------------------

def log_probability(theta, z, y, yerr):
    lp = log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_likelihood(theta, z, y, yerr)


# -----------------------------
# EXECUÇÃO MCMC
# -----------------------------

def run_mcmc(z, y, yerr):

    initial = np.array([70, 0.3, 0.1])
    ndim = 3
    nwalkers = 32

    pos = initial + 1e-4 * np.random.randn(nwalkers, ndim)

    sampler = emcee.EnsembleSampler(
        nwalkers,
        ndim,
        log_probability,
        args=(z, y, yerr)
    )

    sampler.run_mcmc(pos, 2000, progress=True)

    samples = sampler.get_chain(discard=500, flat=True)

    return samples


# -----------------------------
# OUTPUT
# -----------------------------

def save_results(samples):
    result = {
        "H0_mean": float(np.mean(samples[:, 0])),
        "Omega_m_mean": float(np.mean(samples[:, 1])),
        "beta_mean": float(np.mean(samples[:, 2]))
    }

    with open("validation_outputs/rll.json", "w") as f:
        json.dump(result, f, indent=2)


# -----------------------------
# MAIN
# -----------------------------

if __name__ == "__main__":

    # placeholder dataset (substituir por DESI/Pantheon+)
    z = np.linspace(0.01, 1.5, 50)
    y = np.random.normal(70, 5, size=len(z))
    yerr = np.ones_like(y)

    samples = run_mcmc(z, y, yerr)
    save_results(samples)
