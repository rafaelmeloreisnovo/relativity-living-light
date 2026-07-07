"""
[COD]/[HIP] Comparacao direta: LCDM vs w0waCDM(CPL) vs RLL-original vs RLL-OpcaoA
contra dado REAL Pantheon+SH0ES (1624 SNe apos exclusao de 77 calibradores Cepheid)

Retroalimentacao: converte o resultado sintetico anterior (wa_eff=+0.32, ganho 48.6x)
de [HIP] para [COD] ou refuta, usando dado observacional real pela primeira vez.
"""
import numpy as np
from load_pantheon import load_pantheon
from models import chi2, fit_model

d = load_pantheon()
z, mu, mu_err = d["z"], d["mu"], d["mu_err"]
n = len(z)

print(f"F_ok: N={n} SNe reais (Pantheon+SH0ES, calibradores excluidos)")
print(f"z range: [{z.min():.4f}, {z.max():.4f}]\n")

results = {}

print("=== Fit 1/4: LCDM (H0, Om) ===")
r_lcdm = fit_model(z, mu, mu_err, "lcdm", x0=[70.0, 0.3])
chi2_lcdm = r_lcdm.fun
k_lcdm = 2
print(f"  H0={r_lcdm.x[0]:.3f}  Om={r_lcdm.x[1]:.4f}  chi2={chi2_lcdm:.2f}  chi2/dof={chi2_lcdm/(n-k_lcdm):.4f}")
results["lcdm"] = (r_lcdm.x, chi2_lcdm, k_lcdm)

print("\n=== Fit 2/4: w0waCDM / CPL (H0, Om, w0, wa) — adversario correto ===")
r_cpl = fit_model(z, mu, mu_err, "cpl", x0=[70.0, 0.3, -1.0, 0.0])
chi2_cpl = r_cpl.fun
k_cpl = 4
print(f"  H0={r_cpl.x[0]:.3f}  Om={r_cpl.x[1]:.4f}  w0={r_cpl.x[2]:.4f}  wa={r_cpl.x[3]:.4f}  chi2={chi2_cpl:.2f}  chi2/dof={chi2_cpl/(n-k_cpl):.4f}")
results["cpl"] = (r_cpl.x, chi2_cpl, k_cpl)

print("\n=== Fit 3/4: RLL original (transicao f(z), sharpness fixo=5.0, z_t fixo=0.5) ===")
r_rll_orig = fit_model(z, mu, mu_err, "rll_original", x0=[70.0, 0.3, -1.0, 0.0], z_t=0.5, sharpness=5.0)
chi2_rll_orig = r_rll_orig.fun
k_rll = 4
print(f"  H0={r_rll_orig.x[0]:.3f}  Om={r_rll_orig.x[1]:.4f}  w0={r_rll_orig.x[2]:.4f}  wa={r_rll_orig.x[3]:.4f}  chi2={chi2_rll_orig.fun if hasattr(chi2_rll_orig,'fun') else chi2_rll_orig:.2f}")
print(f"  chi2={chi2_rll_orig:.2f}  chi2/dof={chi2_rll_orig/(n-k_rll):.4f}")
results["rll_original"] = (r_rll_orig.x, chi2_rll_orig, k_rll)

print("\n=== Fit 4/4: RLL Opcao A (g(z)=1-f(z), transicao invertida) ===")
r_rll_A = fit_model(z, mu, mu_err, "rll_optionA", x0=[70.0, 0.3, -1.0, 0.0], z_t=0.5, sharpness=5.0)
chi2_rll_A = r_rll_A.fun
print(f"  H0={r_rll_A.x[0]:.3f}  Om={r_rll_A.x[1]:.4f}  w0={r_rll_A.x[2]:.4f}  wa={r_rll_A.x[3]:.4f}")
print(f"  chi2={chi2_rll_A:.2f}  chi2/dof={chi2_rll_A/(n-k_rll):.4f}")
results["rll_optionA"] = (r_rll_A.x, chi2_rll_A, k_rll)

print("\n" + "="*70)
print("RETROALIMENTACAO FINAL — comparacao contra dado REAL")
print("="*70)
print(f"{'Modelo':<16} {'chi2':>10} {'k':>3} {'chi2/dof':>10} {'AIC':>10}")
for name, (params, c2, k) in results.items():
    aic = c2 + 2*k
    print(f"{name:<16} {c2:>10.2f} {k:>3} {c2/(n-k):>10.4f} {aic:>10.2f}")

print("\nF_gap fechado: wa_eff sintetico anterior era +0.32 (oposto ao DESI wa=-0.62).")
print(f"F_ok real: RLL original entrega wa={results['rll_original'][0][3]:.4f} contra dado Pantheon+ real.")
print(f"F_ok real: RLL Opcao A entrega wa={results['rll_optionA'][0][3]:.4f} contra dado Pantheon+ real.")

razao = results["rll_original"][1] / results["rll_optionA"][1] if results["rll_optionA"][1] > 0 else float("nan")
print(f"\nRazao chi2(original)/chi2(OpcaoA) = {razao:.3f}")
print("(compare com o fator 48.6x calculado no cenario sintetico anterior — este e o valor REAL)")

with open("/home/claude/rll_pantheon/RESULTADO_REAL.txt", "w") as f:
    f.write("RESULTADO REAL — RLL vs Pantheon+SH0ES (dado observacional, nao sintetico)\n")
    f.write(f"N SNe usadas (cosmo, sem calibradores): {n}\n\n")
    for name, (params, c2, k) in results.items():
        f.write(f"{name}: params={list(np.round(params,4))} chi2={c2:.3f} chi2/dof={c2/(n-k):.4f} AIC={c2+2*k:.3f}\n")
    f.write(f"\nRazao chi2(RLL_original)/chi2(RLL_OpcaoA) = {razao:.4f}\n")
    f.write("Classificacao epistemologica: [COD] — calculo direto contra dado real Pantheon+SH0ES.\n")
    f.write("Gap G0 (Pantheon+ ausente) fechado nesta sessao.\n")

print("\nArquivo salvo: RESULTADO_REAL.txt")
