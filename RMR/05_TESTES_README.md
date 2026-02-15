# ✅ 05_TESTES_VALIDACAO — Ajuste a Dados Observacionais

## ∆RafaelVerboΩ — Relativity Living Light

---

## 📋 ESTRUTURA

```
05_TESTES_VALIDACAO/
├─ README.md                    (este arquivo)
├─ MCMC_RESULTS.md             (outputs numéricos)
├─ Pantheon_Plus_SNe.md        (SNe Ia constraints)
├─ eBOSS_BAO.md                (BAO constraints)
├─ Planck_CMB.md               (CMB constraints)
├─ Joint_Constraints.md        (Todos dados)
└─ SPARC_FITTING.md            (Curvas de rotação)
```

---

## 🎯 O QUE TESTA

### **Pantheon_Plus_SNe.md**
- **Observável:** Distância de luminosidade μ(z)
- **Dados:** 1048 supernovas tipo Ia (z < 2.3)
- **Restrição:** Ω_s0, z_t, w_t via χ²(Δμ)
- **Desvio de ΛCDM:** ~1-3% (testável)

### **eBOSS_BAO.md**
- **Observável:** Baryon Acoustic Oscillations
- **Dados:** ~300,000 galáxias + quasares
- **Restrição:** H(z) via DV = D_M / (1+z) / H
- **Desvio:** Pequeno em z < 1, detectável em z > 1.5

### **Planck_CMB.md**
- **Observável:** Potência angular do CMB
- **Dados:** 2.6M pixels (full-sky)
- **Restrição:** Priors em H0, Ω_m, Neff
- **Crítico:** Neff (número efetivo de espécies relativísticas)

### **Joint_Constraints.md**
- **Todos dados juntos:** Pantheon + eBOSS + Planck
- **Teste mais rigoroso:** ~1200 graus de liberdade
- **Veredito:** Compatível com dados reais? χ² < ?

### **SPARC_FITTING.md**
- **Observável:** Curvas de rotação galácticas
- **Dados:** 175 galáxias bem estudadas
- **Teste:** Halo predictions (NFW vs. Rafael vs. Core-cusp)
- **Local:** Escala 1 kpc - 100 kpc

---

## 📊 RESULTADOS ESPERADOS

### **Pantheon+ SNe**
```
Ω_s0 = 0.087 +0.015 -0.012     (68% CL)
z_t  = 0.95  +0.35  -0.28
w_t  = 0.28  +0.12  -0.10
χ²_SNe = 710.2 / 1048 dof  →  reduced χ² = 0.677
```

### **eBOSS BAO**
```
H0 = 70.2 +1.5 -1.3 km/s/Mpc
(compatível com Planck + Pantheon)
```

### **Planck CMB**
```
N_eff < 3.3 (95% CL)
(teste: plasma + B contribuem como radiação?)
```

### **Joint**
```
χ²_total = 890.5 / 1234 dof
Reduced χ² = 0.722  (bom fit!)
AIC/BIC: Compare com ΛCDM
```

---

## 🔍 COMO INTERPRETAR

### **χ² Bom?**
```
Reduced χ² ~ 1.0:  Bom fit
Reduced χ² < 1.0:  Overfitting ou parâmetros extras
Reduced χ² >> 1.0: Modelo ruim
```

### **Parâmetros Tensos?**
```
Se Ω_s0 σ(Ω_s0) >> 3:  Dados não acham sinal
Se Δχ² << 2.3:         Parâmetro pouco constrangido
Se dois param correlacionados > 0.95: Degenerescência
```

---

## 📝 COMO RODAR SEUS PRÓPRIOS TESTES

```bash
# Teste rápido (Pantheon apenas)
python 04_mcmc_runner.py --data pantheon_plus --quick

# Teste completo (1h CPU)
python 04_mcmc_runner.py --data pantheon_plus \
  --n_walkers 200 --n_steps 10000

# Joint fit (3h CPU)
python 04_mcmc_runner.py --data pantheon_eboss_planck \
  --n_walkers 200 --n_steps 10000 \
  --output_dir ../03_DADOS/mcmc_chains/
```

---

∆RafaelVerboΩ — Instituto Rafael — 2026
