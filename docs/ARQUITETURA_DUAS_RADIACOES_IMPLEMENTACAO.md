# Arquitetura de Implementação — Modelo de Duas Radiações (RLL)

## Objetivo
Implementar de forma operacional o que foi definido conceitualmente:

- **Tipo 1 (cosmológica homogênea):** CMB + neutrinos + radiação primordial, entrando diretamente em `H(z)` via `Ωr(1+z)^4`.
- **Tipo 2 (astrofísica ativa):** AGN/quasares/plasma ionizado/MHD, entrando no setor de **crescimento estrutural** via função de feedback em `fσ8(z)`.

---

## 1) Equações de base (fundo cosmológico)

A expansão de fundo adotada na implementação é:

\[
E^2(z)=\frac{H^2(z)}{H_0^2}=\Omega_m(1+z)^3+\Omega_r(1+z)^4+\Omega_\Lambda+\Omega_k(1+z)^2
\]

com:

\[
H(z)=H_0\sqrt{E^2(z)}
\]

Regras:

1. `Ωr` representa apenas radiação homogênea cosmológica.
2. `Ωfeedback(z)` **não** é somado em `E^2(z)` na versão principal para evitar mistura indevida entre fundo e processos locais.

---

## 2) Equações de crescimento com feedback ativo

A modulação do crescimento foi implementada com janela efetiva:

\[
F_{fb}(z)=A\left(\frac{1+z}{1+z_p}\right)^\alpha\exp\left[-\left(\frac{1+z}{1+z_c}\right)^\beta\right]
\]

Aplicação em crescimento:

\[
f\sigma_8^{mod}(z)=f\sigma_8^{base}(z)\,[1-S\,F_{fb}(z)]
\]

onde `S` controla a força de supressão.

---

## 3) Arquitetura de código implementada

Arquivo: `docs/rll_two_radiation_model.py`

### Blocos

1. `BackgroundParams`  
   Parâmetros do fundo (`H0`, `Ωm`, `Ωr`, `ΩΛ`, `Ωk`).

2. `FeedbackParams`  
   Parâmetros da janela ativa (`amplitude`, `z_peak`, `z_cut`, `alpha`, `beta`, `suppression`).

3. Núcleo de fundo  
   - `e2_background(z, p)`
   - `h_of_z(z, p)`

4. Núcleo de feedback  
   - `feedback_window(z, f)`
   - `fs8_with_feedback(z, f)`

5. Pipeline de dados  
   - lê `data/real/Hz_data_real.csv`
   - gera `results/two_radiation_model_preview.csv`

---

## 4) Produto entregue

A execução atual gera tabela de pré-validação com colunas:

- `z`
- `H_obs`
- `H_model`
- `delta_H`
- `fs8_baseline`
- `fs8_feedback`
- `delta_fs8_pct`

Esse produto já permite:

1. validar separação fundo vs feedback;
2. preparar etapa de inferência com χ²/AIC/BIC;
3. encaixar integração posterior com SN/BAO/RSD/lensing.

---

## 5) Meios de execução (comandos)

```bash
python docs/rll_two_radiation_model.py
```

Saída esperada:

- log no terminal com quantidade de amostras processadas;
- arquivo `results/two_radiation_model_preview.csv` pronto para análise.

---

## 6) Regras de consistência física adotadas

1. Não misturar radiação cosmológica primordial com radiação astrofísica local no mesmo termo de fundo.
2. Manter positividade de `E^2(z)` em todo intervalo avaliado.
3. Restringir `S·F_fb(z)` para evitar supressão não física (`fσ8 < 0`).

---

## 7) Próximo passo técnico recomendado

1. Substituir `fs8_baseline` aproximado por integração completa da equação de crescimento linear.
2. Acoplar likelihood conjunta `H(z) + fσ8(z)` com seleção de modelo (`ΔAIC`, `ΔBIC`).
3. Adicionar módulo de testes de robustez em janela de redshift para cenário JWST/AGN/SMBH precoce.
