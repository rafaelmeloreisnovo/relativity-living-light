"""
RLL vs ΛCDM — Validação Dados Observacionais Reais
∆RafaelVerboΩ | Instituto Rafael | 2026
DOI: 10.5281/zenodo.17188137

Datasets:
  [A] H(z) Cosmic Chronometers — Moresco+ 2022  (33 pts)
  [B] BAO — BOSS DR12 + DESI 2024               (10 pts)
  [C] CMB shift params — Planck 2018 VI         (2  pts)
  Total: 45 observáveis

Parâmetros livres:
  ΛCDM : {H0, Om, OL, Ob_h2}         k=4
  RLL  : {H0, Om, OL, Os0, zt, wt, Ob_h2}  k=7
"""

import numpy as np
from scipy.optimize import minimize, differential_evolution
from scipy.integrate import quad
import warnings; warnings.filterwarnings('ignore')

c_kms = 299792.458
z_CMB = 1089.92

# ══ [A] H(z) Cosmic Chronometers + BAO Lyman-alpha ══
Hz_data = np.array([
    [0.070,  69.0, 19.6],[0.090,  69.0, 12.0],[0.120,  68.6, 26.2],
    [0.170,  83.0,  8.0],[0.179,  75.0,  4.0],[0.199,  75.0,  5.0],
    [0.200,  72.9, 29.6],[0.270,  77.0, 14.0],[0.280,  88.8, 36.6],
    [0.352,  83.0, 14.0],[0.380,  83.0, 13.5],[0.400,  95.0, 17.0],
    [0.440,  82.6,  7.8],[0.480,  97.0, 62.0],[0.510,  90.4,  1.9],
    [0.570,  96.8,  3.4],[0.593, 104.0, 13.0],[0.600,  87.9,  6.1],
    [0.610,  97.3,  2.1],[0.680,  92.0,  8.0],[0.730,  97.3,  7.0],
    [0.781, 105.0, 12.0],[0.875, 125.0, 17.0],[0.880,  90.0, 40.0],
    [0.900, 117.0, 23.0],[1.037, 154.0, 20.0],[1.300, 168.0, 17.0],
    [1.363, 160.0, 33.6],[1.430, 177.0, 18.0],[1.530, 140.0, 14.0],
    [1.750, 202.0, 40.0],[1.965, 186.5, 50.4],[2.340, 222.0,  7.0],
])
z_Hz = Hz_data[:,0]; H_obs = Hz_data[:,1]; sH = Hz_data[:,2]

# ══ [B] BAO DV/rs ══
BAO_data = np.array([
    [0.106, 2.976, 0.133],[0.150, 4.466, 0.168],[0.320, 8.467, 0.167],
    [0.570,13.773, 0.134],[0.510,13.36,  0.210],[0.706,16.85,  0.320],
    [0.930,21.71,  0.280],[1.317,27.79,  0.690],[1.491,30.21,  0.790],
    [2.330,36.31,  1.300],
])
z_BAO = BAO_data[:,0]; DV_obs = BAO_data[:,1]; sDV = BAO_data[:,2]

# ══ [C] CMB Planck 2018 ══
R_obs=1.7502;  R_sig=0.0046
la_obs=301.471; la_sig=0.090
N_obs = len(z_Hz) + len(z_BAO) + 2

# ═══════════════════════════════════════════
# FÍSICA
# ═══════════════════════════════════════════
def f_log(z, zt, wt):
    return 1.0/(1.0 + np.exp(np.clip((z-zt)/wt,-500,500)))

def E2_LCDM(z, Om, OL):
    Or = 9e-5
    return Om*(1+z)**3 + Or*(1+z)**4 + OL

def E2_RLL(z, Om, OL, Os0, zt, wt):
    Or = 9e-5
    f  = f_log(z, zt, wt)
    sup = Os0*(f + (1-f)*(1+z)**3)
    return Om*(1+z)**3 + Or*(1+z)**4 + OL + sup

def Hz_LCDM(z, H0, Om, OL):
    return H0*np.sqrt(np.maximum(E2_LCDM(z,Om,OL),1e-12))

def Hz_RLL(z, H0, Om, OL, Os0, zt, wt):
    return H0*np.sqrt(np.maximum(E2_RLL(z,Om,OL,Os0,zt,wt),1e-12))

def DC(z_val, Hz_fn, *args):
    """Comóvel [Mpc]"""
    fn = lambda zz: c_kms/Hz_fn(zz,*args)
    v, _ = quad(fn, 0, z_val, limit=150, epsrel=1e-5)
    return v

def DV_fn(z, Hz_fn, *args):
    Dc = DC(z, Hz_fn, *args)
    Hz = Hz_fn(z, *args)
    return (z*c_kms/Hz*Dc**2)**(1./3.)

def rs_fn(H0, Ob_h2, Om):
    """Sound horizon Mpc — Percival 2010 calibrado Planck"""
    return 147.78*(Om*(H0/100)**2/0.1432)**(-0.255)*(Ob_h2/0.02236)**(-0.134)

def CMB_R(Hz_fn, H0, Om, *args):
    Dc = DC(z_CMB, Hz_fn, H0, *args[:2+len(args)-1] if args else (H0,Om))
    # Simplify: pass H0,Om via Hz_fn
    return np.sqrt(Om)*H0/c_kms*Dc

def CMB_la_fn(Hz_fn, H0, Om, Ob_h2, *extra):
    Dc = DC(z_CMB, Hz_fn, H0, *((Om,)+extra))
    rs = rs_fn(H0, Ob_h2, Om)
    return np.pi*Dc/rs

# ═══════════════════════════════════════════
# chi² POR DATASET
# ═══════════════════════════════════════════
def chi2_all_LCDM(H0, Om, OL, Ob_h2):
    # H(z)
    Hth = Hz_LCDM(z_Hz, H0, Om, OL)
    c2  = np.sum(((H_obs-Hth)/sH)**2)
    # BAO
    rs  = rs_fn(H0, Ob_h2, Om)
    DVth= np.array([DV_fn(z,Hz_LCDM,H0,Om,OL)/rs for z in z_BAO])
    c2 += np.sum(((DV_obs-DVth)/sDV)**2)
    # CMB
    Dc_cmb = DC(z_CMB, Hz_LCDM, H0, Om, OL)
    R_th   = np.sqrt(Om)*H0/c_kms*Dc_cmb
    la_th  = np.pi*Dc_cmb/rs_fn(H0,Ob_h2,Om)
    c2 += ((R_th-R_obs)/R_sig)**2 + ((la_th-la_obs)/la_sig)**2
    return c2

def chi2_all_RLL(H0, Om, OL, Os0, zt, wt, Ob_h2):
    # H(z)
    Hth = Hz_RLL(z_Hz, H0, Om, OL, Os0, zt, wt)
    c2  = np.sum(((H_obs-Hth)/sH)**2)
    # BAO
    rs  = rs_fn(H0, Ob_h2, Om)
    DVth= np.array([DV_fn(z,Hz_RLL,H0,Om,OL,Os0,zt,wt)/rs for z in z_BAO])
    c2 += np.sum(((DV_obs-DVth)/sDV)**2)
    # CMB
    Dc_cmb = DC(z_CMB, Hz_RLL, H0, Om, OL, Os0, zt, wt)
    R_th   = np.sqrt(Om)*H0/c_kms*Dc_cmb
    la_th  = np.pi*Dc_cmb/rs_fn(H0,Ob_h2,Om)
    c2 += ((R_th-R_obs)/R_sig)**2 + ((la_th-la_obs)/la_sig)**2
    return c2

def obj_LCDM(p):
    try:    return chi2_all_LCDM(*p)
    except: return 1e8

def obj_RLL(p):
    try:    return chi2_all_RLL(*p)
    except: return 1e8

# ═══════════════════════════════════════════
# MINIMIZAÇÃO
# ═══════════════════════════════════════════
print("="*62)
print("  RLL vs ΛCDM — Validação com 45 Observáveis Reais")
print("  ∆RafaelVerboΩ | Instituto Rafael | 2026")
print("="*62)
print(f"  H(z) CC={len(z_Hz)} | BAO={len(z_BAO)} | CMB=2  →  N_obs={N_obs}\n")

# ΛCDM
print("▶ ΛCDM [k=4] minimizando...")
bounds_L = [(60,80),(0.10,0.60),(0.50,0.90),(0.018,0.026)]
res_L = differential_evolution(obj_LCDM, bounds_L, seed=42, maxiter=300, tol=1e-6, workers=1)
bL = res_L.x; c2_L = res_L.fun; k_L = 4
print(f"   H0={bL[0]:.2f}  Om={bL[1]:.4f}  OL={bL[2]:.4f}  Ob_h2={bL[3]:.5f}")
print(f"   χ²={c2_L:.2f}  dof={N_obs-k_L}  χ²/dof={c2_L/(N_obs-k_L):.2f}\n")

# RLL
print("▶ RLL  [k=7] minimizando...")
bounds_R = [(60,80),(0.10,0.55),(0.40,0.90),(0.00,0.25),(0.10,3.0),(0.05,2.0),(0.018,0.026)]
res_R = differential_evolution(obj_RLL, bounds_R, seed=42, maxiter=500, tol=1e-6, workers=1)
bR = res_R.x; c2_R = res_R.fun; k_R = 7
print(f"   H0={bR[0]:.2f}  Om={bR[1]:.4f}  OL={bR[2]:.4f}")
print(f"   Os0={bR[3]:.4f}  zt={bR[4]:.3f}  wt={bR[5]:.3f}  Ob_h2={bR[6]:.5f}")
print(f"   χ²={c2_R:.2f}  dof={N_obs-k_R}  χ²/dof={c2_R/(N_obs-k_R):.2f}\n")

# ═══ CRITÉRIOS ═══
AIC_L = c2_L + 2*k_L; AIC_R = c2_R + 2*k_R
BIC_L = c2_L + k_L*np.log(N_obs); BIC_R = c2_R + k_R*np.log(N_obs)
dchi2=c2_R-c2_L; dAIC=AIC_R-AIC_L; dBIC=BIC_R-BIC_L

print("─"*62)
print("  CRITÉRIOS (RLL − ΛCDM)")
print("─"*62)
print(f"  Δχ²  = {dchi2:+.2f}")
print(f"  ΔAIC = {dAIC:+.2f}   (< -10: forte evidência RLL | > +2: ΛCDM preferido)")
print(f"  ΔBIC = {dBIC:+.2f}   (mais conservador, penaliza +parâmetros)\n")

if   dAIC < -10: verdict="FORTE evidência para RLL ✅✅"
elif dAIC <  -2: verdict="Evidência moderada para RLL ✅"
elif dAIC <   2: verdict="Indistinguíveis — RLL compatível 🔄"
elif dAIC <  10: verdict="ΛCDM preferido moderadamente ⚠️"
else:            verdict="FORTE evidência ΛCDM — RLL penalizado ❌"
print(f"  → {verdict}\n")

# Tensão H0
print("─"*62)
print("  TENSÃO H₀")
print("─"*62)
print(f"  Planck 2018 : {67.4} | SH0ES 2022 : {73.04} km/s/Mpc")
print(f"  ΛCDM fit    : {bL[0]:.2f} | RLL fit : {bR[0]:.2f} km/s/Mpc")
sigma_comb = 1.73  # erro combinado Planck+SH0ES
t_L = abs(bL[0]-67.4)/sigma_comb; t_R = abs(bR[0]-67.4)/sigma_comb
print(f"  Tensão vs Planck → ΛCDM: {t_L:.1f}σ | RLL: {t_R:.1f}σ")
if bR[0] > bL[0]: print("  RLL tende H0 mais alto → tensão H0 parcialmente aliviada")
print()

# ═══ PLOTS ═══
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

fig = plt.figure(figsize=(15,11))
fig.suptitle('RLL vs ΛCDM — Validação: H(z) + BAO + CMB (Planck 2018)\n'
             '∆RafaelVerboΩ | Instituto Rafael | DOI: 10.5281/zenodo.17188137',
             fontsize=12, fontweight='bold', y=0.98)
gs = gridspec.GridSpec(2,3, hspace=0.42, wspace=0.35)

z_p = np.linspace(0.01, 2.5, 600)

# ─ H(z)
ax1 = fig.add_subplot(gs[0,:2])
ax1.errorbar(z_Hz, H_obs, yerr=sH, fmt='o', color='#666', ms=4, alpha=0.75,
             label='CC + BAO Lyman-α (real)', capsize=2, elinewidth=0.8)
ax1.plot(z_p, Hz_LCDM(z_p,*bL[:3]), 'royalblue', lw=2.2,
         label=f'ΛCDM  H0={bL[0]:.1f} Om={bL[1]:.3f}')
ax1.plot(z_p, Hz_RLL(z_p,*bR[:6]), 'crimson', lw=2.2, ls='--',
         label=f'RLL   H0={bR[0]:.1f} Os0={bR[3]:.3f} zt={bR[4]:.2f}')
ax1.set_xlabel('Redshift z'); ax1.set_ylabel('H(z) [km/s/Mpc]')
ax1.set_title('H(z) — Cosmic Chronometers (33 pts) + BAO Lyman-α')
ax1.legend(fontsize=8.5); ax1.grid(alpha=0.25)

# ─ Resíduos H(z)
ax2 = fig.add_subplot(gs[0,2])
rL = (H_obs - Hz_LCDM(z_Hz,*bL[:3]))/sH
rR = (H_obs - Hz_RLL( z_Hz,*bR[:6]))/sH
ax2.scatter(z_Hz, rL, c='royalblue', s=22, alpha=0.7, label='ΛCDM')
ax2.scatter(z_Hz, rR, c='crimson',   s=22, alpha=0.7, marker='^', label='RLL')
ax2.axhline(0,  c='k', lw=0.9, ls='--')
ax2.axhline(+1, c='gray', lw=0.5, ls=':'); ax2.axhline(-1, c='gray', lw=0.5, ls=':')
ax2.axhline(+2, c='gray', lw=0.4, ls=':'); ax2.axhline(-2, c='gray', lw=0.4, ls=':')
ax2.set_xlabel('z'); ax2.set_ylabel('(H_obs − H_th) / σ')
ax2.set_title('Resíduos Normalizados H(z)'); ax2.legend(fontsize=8); ax2.grid(alpha=0.25)

# ─ BAO DV/rs
ax3 = fig.add_subplot(gs[1,:2])
rs_L = rs_fn(bL[0],bL[3],bL[1])
rs_R = rs_fn(bR[0],bR[6],bR[1])
z_b2 = np.linspace(0.05,2.5,200)
DVL = np.array([DV_fn(z,Hz_LCDM,bL[0],bL[1],bL[2])/rs_L for z in z_b2])
DVR = np.array([DV_fn(z,Hz_RLL, bR[0],bR[1],bR[2],bR[3],bR[4],bR[5])/rs_R for z in z_b2])
ax3.errorbar(z_BAO, DV_obs, yerr=sDV, fmt='s', color='darkorange', ms=6, alpha=0.85,
             label='BAO BOSS DR12 + DESI 2024', capsize=3, elinewidth=1.0)
ax3.plot(z_b2, DVL, 'royalblue', lw=2.2, label='ΛCDM')
ax3.plot(z_b2, DVR, 'crimson',   lw=2.2, ls='--', label='RLL')
ax3.set_xlabel('Redshift z'); ax3.set_ylabel('DV(z) / rs')
ax3.set_title('BAO — DV(z)/rs  [BOSS DR12 + DESI 2024]')
ax3.legend(fontsize=8.5); ax3.grid(alpha=0.25)

# ─ Tabela sumário
ax4 = fig.add_subplot(gs[1,2])
ax4.axis('off')
txt = (
    "Parâmetros ótimos\n"
    "─────────────────────\n"
    f"ΛCDM   H0 = {bL[0]:.2f}\n"
    f"       Om = {bL[1]:.4f}\n"
    f"       OL = {bL[2]:.4f}\n\n"
    f"RLL    H0 = {bR[0]:.2f}\n"
    f"       Om = {bR[1]:.4f}\n"
    f"       OL = {bR[2]:.4f}\n"
    f"      Os0 = {bR[3]:.4f}\n"
    f"       zt = {bR[4]:.3f}\n"
    f"       wt = {bR[5]:.3f}\n\n"
    "─────────────────────\n"
    f"χ²  ΛCDM  = {c2_L:.1f}\n"
    f"χ²  RLL   = {c2_R:.1f}\n"
    f"Δχ²       = {dchi2:+.1f}\n\n"
    f"ΔAIC = {dAIC:+.1f}\n"
    f"ΔBIC = {dBIC:+.1f}\n\n"
    f"→ {verdict.split(' ')[0]}\n"
    f"  {' '.join(verdict.split(' ')[1:])}"
)
ax4.text(0.03,0.97, txt, transform=ax4.transAxes, fontsize=8.5,
         va='top', fontfamily='monospace',
         bbox=dict(boxstyle='round,pad=0.5', fc='#fffde7', alpha=0.95))
ax4.set_title('Sumário Estatístico', fontsize=10)

plt.savefig('/mnt/user-data/outputs/RLL_validacao_real.png', dpi=150, bbox_inches='tight')
print("  ✅ PNG  → RLL_validacao_real.png")

# ═══ CSV ═══
import csv, os; os.makedirs('/mnt/user-data/outputs', exist_ok=True)
with open('/mnt/user-data/outputs/RLL_chi2_results.csv','w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['Model','H0','Om','OL','Os0','zt','wt','Ob_h2','chi2','AIC','BIC','N_obs','k','chi2_dof','verdict'])
    w.writerow(['LCDM',round(bL[0],3),round(bL[1],4),round(bL[2],4),
                '-','-','-',round(bL[3],5),
                round(c2_L,3),round(AIC_L,3),round(BIC_L,3),N_obs,k_L,round(c2_L/(N_obs-k_L),3),'-'])
    w.writerow(['RLL',round(bR[0],3),round(bR[1],4),round(bR[2],4),
                round(bR[3],4),round(bR[4],3),round(bR[5],3),round(bR[6],5),
                round(c2_R,3),round(AIC_R,3),round(BIC_R,3),N_obs,k_R,round(c2_R/(N_obs-k_R),3),verdict])
    w.writerow(['DELTA_RLL_minus_LCDM','-','-','-','-','-','-','-',
                round(dchi2,3),round(dAIC,3),round(dBIC,3),N_obs,k_R-k_L,'-',verdict])
print("  ✅ CSV  → RLL_chi2_results.csv")

# ═══ H(z) data CSV ═══
with open('/mnt/user-data/outputs/Hz_data_real.csv','w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['z','H_obs','sigma_H','source'])
    sources = ['CC']*17 + ['BOSS_DR12']*3 + ['CC']*9 + ['BOSS_Lya']
    for i,(z,H,s) in enumerate(Hz_data):
        src = 'CC+BAO_BOSS' if z in [0.380,0.510,0.570,0.610] else ('BAO_Lya' if z==2.340 else 'CC_Moresco2022')
        w.writerow([z,H,s,src])
print("  ✅ CSV  → Hz_data_real.csv")

with open('/mnt/user-data/outputs/BAO_data_real.csv','w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['z_eff','DV_over_rs','sigma','survey'])
    surveys=['6dFGS','SDSS_MGS','BOSS_DR12_LOWZ','BOSS_DR12_CMASS','DESI2024_BGS','DESI2024_LRG1','DESI2024_LRG2','DESI2024_ELG','DESI2024_QSO','BOSS_Lya']
    for i,(z,dv,s) in enumerate(BAO_data):
        w.writerow([z,dv,s,surveys[i]])
print("  ✅ CSV  → BAO_data_real.csv\n")

print("="*62)
print(f"  Ciclo ψ→χ→ρ→Δ→Σ→Ω completo | N=45 obs")
print(f"  Os0_best = {bR[3]:.4f} | zt={bR[4]:.3f} | wt={bR[5]:.3f}")
if bR[3] < 0.005:
    print("  → Os0 ≈ 0: RLL degenerado em ΛCDM neste dataset")
else:
    print(f"  → Superposição ativa Ω_s0={bR[3]:.4f} — componente não-nula")
print("="*62)
