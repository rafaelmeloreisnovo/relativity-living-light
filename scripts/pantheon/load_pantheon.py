"""
[COD] Loader Pantheon+SH0ES real data
Fonte: PantheonPlusSH0ES/DataRelease (GitHub oficial)
Colunas confirmadas por leitura direta do header:
  3=zHD, 11=MU_SH0ES, 12=MU_SH0ES_ERR_DIAG, 14=IS_CALIBRATOR
Regra padrão SH0ES: excluir IS_CALIBRATOR==1 do fit cosmológico
(esses pontos servem para ancorar H0 via Cepheids, não para o fit z-mu puro)
"""
import numpy as np

def load_pantheon(path="/home/claude/rll_pantheon/pantheon_data.dat"):
    with open(path) as f:
        header = f.readline().split()
    idx = {name: i for i, name in enumerate(header)}

    data = np.genfromtxt(path, skip_header=1, dtype=str)
    zHD = data[:, idx["zHD"]].astype(float)
    mu = data[:, idx["MU_SH0ES"]].astype(float)
    mu_err = data[:, idx["MU_SH0ES_ERR_DIAG"]].astype(float)
    is_calib = data[:, idx["IS_CALIBRATOR"]].astype(float)

    # F_ok: separar amostra cosmológica (não-calibradora) da amostra de ancoragem
    mask_cosmo = is_calib == 0
    return {
        "z_all": zHD, "mu_all": mu, "mu_err_all": mu_err, "is_calib": is_calib,
        "z": zHD[mask_cosmo], "mu": mu[mask_cosmo], "mu_err": mu_err[mask_cosmo],
        "n_total": len(zHD), "n_cosmo": mask_cosmo.sum(), "n_calib": (~mask_cosmo).sum()
    }

if __name__ == "__main__":
    d = load_pantheon()
    print(f"F_ok: total={d['n_total']} cosmo={d['n_cosmo']} calibradores_excluidos={d['n_calib']}")
    print(f"z range: [{d['z'].min():.5f}, {d['z'].max():.5f}]")
    print(f"mu range: [{d['mu'].min():.3f}, {d['mu'].max():.3f}]")
