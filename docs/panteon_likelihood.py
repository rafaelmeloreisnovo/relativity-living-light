"""
panteon_likelihood.py
Relativity Living Light — Pipeline observacional Pantheon+

Fluxo:
1) Validar arquivos Pantheon+ em data/pantheon/
2) Ajustar RLL e ΛCDM por minimização de χ²
3) Exportar artefatos canônicos em data/results/
4) (Opcional) salvar figura comparativa em figs/paper/
"""

import json
import os
import hashlib
import subprocess
from datetime import datetime, timezone

import numpy as np
from scipy.integrate import quad
from scipy.optimize import differential_evolution, minimize


C_KMS = 299792.458
H0 = 70.0
SCRIPT_VERSION = 'v1.2.0'


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def hash_file_sha256(path, chunk_size=1024 * 1024):
    digest = hashlib.sha256()
    with open(path, 'rb') as f:
        while True:
            block = f.read(chunk_size)
            if not block:
                break
            digest.update(block)
    return digest.hexdigest()


def get_git_commit():
    try:
        return subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
    except Exception:
        return None


def _resolve_column_name(dtype_names, accepted_names, label):
    normalized = {name.lower(): name for name in dtype_names}
    for candidate in accepted_names:
        if candidate.lower() in normalized:
            return normalized[candidate.lower()]
    raise ValueError(
        f"Coluna obrigatória não encontrada para '{label}'. "
        f"Aceitas: {accepted_names}. Colunas disponíveis: {list(dtype_names)}"
    )


def E2_RLL(z, Om0, OL, Os0, zt, wt):
    f = 1.0 / (1.0 + np.exp((z - zt) / wt))
    return (
        Om0 * (1.0 + z) ** 3
        + OL
        + Os0 * (f + (1.0 - f) * (1.0 + z) ** 3)
    )


def E2_LCDM(z, Om0):
    OL = 1.0 - Om0
    return Om0 * (1.0 + z) ** 3 + OL


def comoving_distance(z, e2_func, *params):
    integrand = lambda zp: 1.0 / np.sqrt(e2_func(zp, *params))
    dc, _ = quad(integrand, 0.0, z, limit=200)
    return (C_KMS / H0) * dc


def mu_from_e2(z_vals, e2_func, *params, M_abs=-19.3):
    z_vals = np.asarray(z_vals)
    d_l = np.array([(1.0 + z) * comoving_distance(z, e2_func, *params) for z in z_vals])
    mu = 5.0 * np.log10(d_l * 1.0e6 / 10.0)
    return mu + M_abs


PANTHEON_COVARIANCE_FILENAME = 'Pantheon+SH0ES_STAT+SYS.cov'


def _load_pantheon_plus_covariance(cov_file, n_obs):
    values = np.fromfile(cov_file, dtype=float, sep=' ')
    expected_elements = int(n_obs) * int(n_obs)

    if values.size == expected_elements + 1:
        header_n = int(values[0])
        if not np.isclose(values[0], header_n):
            raise ValueError(
                f"Cabeçalho inválido em {os.path.basename(cov_file)}: "
                f"primeiro valor deve ser dimensão inteira, recebido {values[0]}."
            )
        if header_n != n_obs:
            raise ValueError(
                f"{os.path.basename(cov_file)} incompatível: cabeçalho declara {header_n} observações, "
                f"mas lcparam tem {n_obs}."
            )
        values = values[1:]
    elif values.size != expected_elements:
        raise ValueError(
            f"{os.path.basename(cov_file)} incompatível: esperado {expected_elements} elementos "
            f"(ou {expected_elements + 1} com cabeçalho Pantheon+), recebido {values.size}."
        )

    if not np.all(np.isfinite(values)):
        raise ValueError(f"{os.path.basename(cov_file)} contém NaN/inf.")

    return values.reshape(n_obs, n_obs)


def load_pantheon(data_dir='data/pantheon', require_covariance=True):
    lc_file = os.path.join(data_dir, 'lcparam_full_long_zhel.txt')
    cov_file = os.path.join(data_dir, PANTHEON_COVARIANCE_FILENAME)
    sanity_checks = []
    input_meta = {
        'lc_file': lc_file,
        'cov_file': cov_file,
        'sys_file': cov_file,
        'has_systematics': False,
        'covariance_used': False,
        'require_covariance': bool(require_covariance),
        'sanity_checks': sanity_checks,
    }

    try:
        if not os.path.exists(lc_file):
            raise FileNotFoundError(
                f"Arquivo não encontrado: {lc_file}\n"
                "Baixe Pantheon+ em: https://github.com/PantheonPlusSH0ES/DataRelease"
            )

        data = np.genfromtxt(lc_file, names=True, dtype=None, encoding=None)
        if data.ndim == 0:
            data = np.array([data], dtype=data.dtype)

        z_col = _resolve_column_name(data.dtype.names, ['zhel', 'zcmb'], 'redshift')
        mu_col = _resolve_column_name(data.dtype.names, ['mb', 'mu', 'm_b_corr'], 'modulo_distancia')
        err_col = _resolve_column_name(data.dtype.names, ['dmb', 'dmu', 'mb_err'], 'erro_modulo')
        sanity_checks.append({
            'name': 'required_columns_resolution',
            'passed': True,
            'details': {
                'resolved_columns': {
                    'redshift': z_col,
                    'modulo_distancia': mu_col,
                    'erro_modulo': err_col,
                }
            },
        })

        z_hel = np.asarray(data[z_col], dtype=float)
        mu_obs = np.asarray(data[mu_col], dtype=float)
        mu_err = np.asarray(data[err_col], dtype=float)
        n_obs = len(z_hel)

        finite_ok = bool(
            np.all(np.isfinite(z_hel))
            and np.all(np.isfinite(mu_obs))
            and np.all(np.isfinite(mu_err))
        )
        sanity_checks.append({
            'name': 'finite_values_validation',
            'passed': finite_ok,
            'details': {
                'n_obs': int(n_obs),
                'finite': finite_ok,
            },
        })
        if not finite_ok:
            raise ValueError('Dados contêm NaN/inf em redshift, módulo de distância ou erro.')

        mu_err_positive = bool(np.all(mu_err > 0))
        sanity_checks.append({
            'name': 'mu_err_positive_validation',
            'passed': mu_err_positive,
            'details': {
                'n_obs': int(n_obs),
                'min_mu_err': float(np.min(mu_err)) if n_obs else None,
            },
        })
        if not mu_err_positive:
            raise ValueError('Todos os erros de módulo de distância devem ser positivos.')

        c_stat = np.diag(mu_err ** 2)

        has_covariance = os.path.exists(cov_file)
        input_meta['has_systematics'] = has_covariance
        if has_covariance:
            c_total = _load_pantheon_plus_covariance(cov_file, n_obs)
            input_meta['covariance_used'] = PANTHEON_COVARIANCE_FILENAME
            sanity_checks.append({
                'name': 'pantheon_plus_covariance_dimensional_compatibility',
                'passed': True,
                'details': {
                    'covariance_file': PANTHEON_COVARIANCE_FILENAME,
                    'has_covariance': True,
                    'n_obs': int(n_obs),
                    'expected_elements': int(n_obs * n_obs),
                    'received_elements': int(n_obs * n_obs),
                },
            })
        elif require_covariance:
            sanity_checks.append({
                'name': 'pantheon_plus_covariance_presence',
                'passed': False,
                'details': {
                    'covariance_file': PANTHEON_COVARIANCE_FILENAME,
                    'has_covariance': False,
                    'fallback': 'disabled',
                },
            })
            raise FileNotFoundError(
                f"Arquivo de covariância obrigatório não encontrado: {cov_file}. "
                "O fluxo --with-covariance não usa fallback diagonal silencioso."
            )
        else:
            print('⚠️ Matriz Pantheon+ STAT+SYS ausente; usando fallback explícito de covariância estatística diagonal.')
            sanity_checks.append({
                'name': 'pantheon_plus_covariance_presence',
                'passed': True,
                'details': {
                    'covariance_file': PANTHEON_COVARIANCE_FILENAME,
                    'has_covariance': False,
                    'fallback': 'statistical_diagonal',
                    'n_obs': int(n_obs),
                },
            })
            c_total = c_stat

        c_inv = np.linalg.inv(c_total)
        sanity_checks.append({
            'name': 'covariance_inversion',
            'passed': True,
            'details': {
                'n_obs': int(n_obs),
                'has_systematics': has_covariance,
            },
        })

        return z_hel, mu_obs, c_inv, input_meta
    except Exception as exc:
        if not sanity_checks:
            sanity_checks.append({
                'name': 'required_columns_resolution',
                'passed': False,
                'details': {
                    'resolved_columns': None,
                    'error': str(exc),
                },
            })
        elif sanity_checks[-1]['passed']:
            sanity_checks.append({
                'name': sanity_checks[-1]['name'],
                'passed': False,
                'details': {
                    'error': str(exc),
                },
            })

        input_meta['load_error'] = {
            'last_check': sanity_checks[-1]['name'] if sanity_checks else None,
            'message': str(exc),
        }
        setattr(exc, 'input_meta', input_meta)
        raise


def chi2_rll(theta, z_hel, mu_obs, c_inv):
    om0, os0, zt, wt, m_abs = theta
    ol = 1.0 - om0 - os0

    if om0 <= 0 or os0 < 0 or ol < 0 or wt <= 0 or not (0.05 <= zt <= 3.0):
        return 1.0e30

    try:
        mu_th = mu_from_e2(z_hel, E2_RLL, om0, ol, os0, zt, wt, M_abs=m_abs)
    except Exception:
        return 1.0e30

    delta = mu_obs - mu_th
    return float(delta @ c_inv @ delta)


def chi2_lcdm(theta, z_hel, mu_obs, c_inv):
    om0, m_abs = theta
    if om0 <= 0 or om0 >= 1:
        return 1.0e30

    try:
        mu_th = mu_from_e2(z_hel, E2_LCDM, om0, M_abs=m_abs)
    except Exception:
        return 1.0e30

    delta = mu_obs - mu_th
    return float(delta @ c_inv @ delta)


def _finite_difference_gradient_norm(objective, x, bounds, args):
    x = np.asarray(x, dtype=float)
    grad = np.zeros_like(x)
    for i, value in enumerate(x):
        lo, hi = bounds[i]
        step = max(1.0e-6, abs(value) * 1.0e-6)
        x_hi = x.copy()
        x_lo = x.copy()
        x_hi[i] = min(hi, value + step)
        x_lo[i] = max(lo, value - step)
        denom = x_hi[i] - x_lo[i]
        if denom <= 0:
            continue
        grad[i] = (objective(x_hi, *args) - objective(x_lo, *args)) / denom
    return float(np.linalg.norm(grad, ord=2))


def _run_global_then_local_optimizer(objective, initial, bounds, args, label):
    initial = np.asarray(initial, dtype=float)
    initial_chi2 = float(objective(initial, *args))

    global_res = differential_evolution(
        objective,
        bounds=bounds,
        args=args,
        seed=1729,
        polish=False,
        updating='immediate',
        workers=1,
        tol=1.0e-6,
        maxiter=80,
        popsize=10,
    )

    candidates = [initial, np.asarray(global_res.x, dtype=float)]
    local_results = [
        minimize(
            objective,
            candidate,
            args=args,
            method='L-BFGS-B',
            bounds=bounds,
            options={'maxiter': 1000, 'ftol': 1.0e-10},
        )
        for candidate in candidates
    ]
    res = min(local_results, key=lambda item: float(item.fun))

    movement = float(np.linalg.norm(np.asarray(res.x, dtype=float) - initial, ord=2))
    gradient_norm = _finite_difference_gradient_norm(objective, res.x, bounds, args)
    initial_gradient_norm = _finite_difference_gradient_norm(objective, initial, bounds, args)
    nit = int(getattr(res, 'nit', 0) or 0)
    nfev = int(getattr(res, 'nfev', 0) or 0) + int(getattr(global_res, 'nfev', 0) or 0)
    final_chi2 = float(res.fun)
    message = f"global: {getattr(global_res, 'message', '')}; local: {getattr(res, 'message', '')}"

    diagnostics = {
        'optimizer': 'scipy.differential_evolution_plus_L-BFGS-B_polish',
        'initial_chi2': initial_chi2,
        'final_chi2': final_chi2,
        'nit': nit + int(getattr(global_res, 'nit', 0) or 0),
        'nfev': nfev,
        'parameter_movement_l2': movement,
        'initial_gradient_norm': initial_gradient_norm,
        'final_gradient_norm': gradient_norm,
        'success': bool(getattr(res, 'success', False)),
        'message': message,
    }

    stopped_at_initial = movement <= 1.0e-8 and diagnostics['nit'] <= 1
    large_evidence = (initial_chi2 > 1.0e6) or (initial_gradient_norm > 1.0e5)
    if stopped_at_initial and large_evidence:
        raise RuntimeError(
            f'{label} optimizer guard failed: stopped at initial point despite large chi2/gradient evidence. '
            f'diagnostics={diagnostics}'
        )
    if not np.isfinite(final_chi2):
        raise RuntimeError(f'{label} optimizer returned non-finite chi2. diagnostics={diagnostics}')
    if not bool(getattr(res, 'success', False)) and final_chi2 >= initial_chi2:
        raise RuntimeError(f'{label} optimizer failed without improvement. diagnostics={diagnostics}')

    return res, diagnostics


def info_criteria(chi2, k, n):
    aic = chi2 + 2 * k
    bic = chi2 + k * np.log(n)
    return aic, bic


def fit_models(z_hel, mu_obs, c_inv):
    n_obs = len(z_hel)

    rll_init = np.array([0.30, 0.05, 1.0, 0.30, -19.3])
    rll_bounds = [(0.05, 0.8), (0.0, 0.3), (0.05, 3.0), (0.03, 1.5), (-20.5, -17.5)]
    res_rll, diagnostics_rll = _run_global_then_local_optimizer(
        chi2_rll,
        rll_init,
        rll_bounds,
        (z_hel, mu_obs, c_inv),
        'RLL',
    )

    lcdm_init = np.array([0.30, -19.3])
    lcdm_bounds = [(0.05, 0.8), (-20.5, -17.5)]
    res_lcdm, diagnostics_lcdm = _run_global_then_local_optimizer(
        chi2_lcdm,
        lcdm_init,
        lcdm_bounds,
        (z_hel, mu_obs, c_inv),
        'ΛCDM',
    )

    chi2_best_rll = float(res_rll.fun)
    chi2_best_lcdm = float(res_lcdm.fun)

    aic_rll, bic_rll = info_criteria(chi2_best_rll, k=5, n=n_obs)
    aic_lcdm, bic_lcdm = info_criteria(chi2_best_lcdm, k=2, n=n_obs)

    return {
        'n_obs': int(n_obs),
        'rll': {
            'best_fit': {
                'Om0': float(res_rll.x[0]),
                'Os0': float(res_rll.x[1]),
                'zt': float(res_rll.x[2]),
                'wt': float(res_rll.x[3]),
                'M_abs': float(res_rll.x[4]),
                'OL': float(1.0 - res_rll.x[0] - res_rll.x[1]),
            },
            'chi2': chi2_best_rll,
            'AIC': float(aic_rll),
            'BIC': float(bic_rll),
            'optimizer_diagnostics': diagnostics_rll,
        },
        'lcdm': {
            'best_fit': {
                'Om0': float(res_lcdm.x[0]),
                'M_abs': float(res_lcdm.x[1]),
                'OL': float(1.0 - res_lcdm.x[0]),
            },
            'chi2': chi2_best_lcdm,
            'AIC': float(aic_lcdm),
            'BIC': float(bic_lcdm),
            'optimizer_diagnostics': diagnostics_lcdm,
        },
    }


def export_results(results, input_meta=None, out_dir='data/results'):
    ensure_dir(out_dir)

    comp_rows = [
        {
            'modelo': 'RLL',
            'chi2': results['rll']['chi2'],
            'AIC': results['rll']['AIC'],
            'BIC': results['rll']['BIC'],
            'delta_AIC_vs_LCDM': results['rll']['AIC'] - results['lcdm']['AIC'],
            'delta_BIC_vs_LCDM': results['rll']['BIC'] - results['lcdm']['BIC'],
        },
        {
            'modelo': 'LCDM',
            'chi2': results['lcdm']['chi2'],
            'AIC': results['lcdm']['AIC'],
            'BIC': results['lcdm']['BIC'],
            'delta_AIC_vs_LCDM': 0.0,
            'delta_BIC_vs_LCDM': 0.0,
        },
    ]

    csv_path = os.path.join(out_dir, 'pantheon_comparativo_rll_vs_lcdm.csv')
    header = 'modelo,chi2,AIC,BIC,delta_AIC_vs_LCDM,delta_BIC_vs_LCDM'
    np.savetxt(
        csv_path,
        np.array([
            [row['chi2'], row['AIC'], row['BIC'], row['delta_AIC_vs_LCDM'], row['delta_BIC_vs_LCDM']]
            for row in comp_rows
        ]),
        delimiter=',',
        header=header,
        comments='',
        fmt='%.10f'
    )
    # acrescenta coluna textual 'modelo' reescrevendo em modo simples
    with open(csv_path, 'w', encoding='utf-8') as f:
        f.write(header + '\n')
        for row in comp_rows:
            f.write(
                f"{row['modelo']},{row['chi2']:.10f},{row['AIC']:.10f},{row['BIC']:.10f},"
                f"{row['delta_AIC_vs_LCDM']:.10f},{row['delta_BIC_vs_LCDM']:.10f}\n"
            )

    payload = {
        'pipeline': 'pantheon_oficial_prova_observacional',
        'timestamp_utc': datetime.now(timezone.utc).isoformat(),
        'n_obs': results['n_obs'],
        'covariance_used': (input_meta or {}).get('covariance_used', False),
        'rll': results['rll'],
        'lcdm': results['lcdm'],
        'comparativo': comp_rows,
    }
    json_path = os.path.join(out_dir, 'pantheon_fit_summary.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    return csv_path, json_path


def export_run_manifest(input_meta, out_dir='data/results'):
    ensure_dir(out_dir)

    lc_path = input_meta['lc_file']
    cov_path = input_meta['cov_file']
    lc_exists = os.path.exists(lc_path)
    cov_exists = os.path.exists(cov_path)

    manifest = {
        'timestamp_utc': datetime.now(timezone.utc).isoformat(),
        'script_path': os.path.abspath(__file__),
        'script_version': SCRIPT_VERSION,
        'git_commit': get_git_commit(),
        'inputs': {
            'lcparam_full_long_zhel.txt': {
                'path': lc_path,
                'exists': lc_exists,
                'sha256': hash_file_sha256(lc_path) if lc_exists else None,
            },
            PANTHEON_COVARIANCE_FILENAME: {
                'path': cov_path,
                'exists': cov_exists,
                'sha256': hash_file_sha256(cov_path) if cov_exists else None,
            },
        },
        'covariance_used': input_meta.get('covariance_used', False),
        'sanity_checks': input_meta.get('sanity_checks', []),
        'load_error': input_meta.get('load_error'),
    }

    manifest_path = os.path.join(out_dir, 'pantheon_run_manifest.json')
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    return manifest_path


def maybe_export_figure(z_hel, mu_obs, results, fig_dir='figs/paper'):
    try:
        import matplotlib.pyplot as plt
    except Exception:
        print('⚠️ matplotlib indisponível; figura não foi exportada.')
        return None

    ensure_dir(fig_dir)

    r = results['rll']['best_fit']
    l = results['lcdm']['best_fit']
    mu_rll = mu_from_e2(z_hel, E2_RLL, r['Om0'], r['OL'], r['Os0'], r['zt'], r['wt'], M_abs=r['M_abs'])
    mu_lcdm = mu_from_e2(z_hel, E2_LCDM, l['Om0'], M_abs=l['M_abs'])

    order = np.argsort(z_hel)
    plt.figure(figsize=(8, 5))
    plt.scatter(z_hel, mu_obs - mu_lcdm, s=8, alpha=0.35, label='dados - ΛCDM')
    plt.plot(z_hel[order], (mu_rll - mu_lcdm)[order], lw=2, label='RLL - ΛCDM (melhor ajuste)')
    plt.axhline(0.0, color='black', ls='--', lw=1)
    plt.xlabel('z')
    plt.ylabel('Δμ')
    plt.title('Pantheon+: comparativo RLL vs ΛCDM')
    plt.legend()
    plt.tight_layout()

    fig_path = os.path.join(fig_dir, 'pantheon_rll_vs_lcdm_delta_mu.png')
    plt.savefig(fig_path, dpi=200)
    plt.close()
    return fig_path


def main():
    print('Relativity Living Light — pipeline Pantheon+ (RLL vs ΛCDM)')
    z_hel, mu_obs, c_inv, input_meta = load_pantheon()
    print(f'Dados carregados: {len(z_hel)} supernovas')

    results = fit_models(z_hel, mu_obs, c_inv)
    csv_path, json_path = export_results(results, input_meta=input_meta)
    manifest_path = export_run_manifest(input_meta)
    fig_path = maybe_export_figure(z_hel, mu_obs, results)

    print('\n=== Resultado de ajuste ===')
    print(f"RLL  : χ²={results['rll']['chi2']:.4f} | AIC={results['rll']['AIC']:.4f} | BIC={results['rll']['BIC']:.4f}")
    print(f"ΛCDM : χ²={results['lcdm']['chi2']:.4f} | AIC={results['lcdm']['AIC']:.4f} | BIC={results['lcdm']['BIC']:.4f}")
    print(f"ΔAIC (RLL-ΛCDM)={results['rll']['AIC'] - results['lcdm']['AIC']:.4f}")
    print(f"ΔBIC (RLL-ΛCDM)={results['rll']['BIC'] - results['lcdm']['BIC']:.4f}")

    print('\nArquivos exportados:')
    print(f'- {csv_path}')
    print(f'- {json_path}')
    print(f'- {manifest_path}')
    if fig_path:
        print(f'- {fig_path}')


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        input_meta = getattr(exc, 'input_meta', None)
        if input_meta is not None:
            try:
                manifest_path = export_run_manifest(input_meta)
                print(f'Manifesto de erro exportado: {manifest_path}')
            except Exception as manifest_exc:
                print(f'Falha ao exportar manifesto de erro: {manifest_exc}')
        print(f'Erro no pipeline Pantheon+: {exc}')
        raise
