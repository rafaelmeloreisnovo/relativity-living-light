# Structure D — Equations

Status: promoted from historical intake  
Claim: `claim_allowed=false`

## 1. Expansion model

The working background form is:

```math
H^2(z)=H_0^2\left[\Omega_m(1+z)^3+\Omega_r(1+z)^4+\Omega_\Lambda+\Omega_f(z)\right]
```

where `Omega_f(z)` is an effective phenomenological component. It may represent simplified astrophysical feedback, early-time effective terms, topological proxies, neutrino-like terms or other explicitly registered components.

## 2. Growth proxy

For linear growth, a practical approximation is:

```math
f(z) \equiv \frac{d\ln D}{d\ln a} \approx \Omega_m(z)^\gamma
```

and the observable route is:

```math
f\sigma_8(z) = f(z)\,\sigma_8(z)
```

## 3. Model comparison

```math
\chi^2 = \sum_i \left(\frac{x_i^{obs}-x_i^{mod}}{\sigma_i}\right)^2
```

```math
AIC = \chi^2 + 2k
```

```math
BIC = \chi^2 + k\ln N
```

## 4. Claim boundary

```text
[OK] These equations define an executable comparison route.
[OK] Optional components are phenomenological until tied to data and baseline.
[BLOQUEADO] No component proves new physics by being present in the equation.
[BLOQUEADO] RLL superiority requires lower metric after parameter penalty and same data/baseline.
```

## 5. Operational locations

```text
data/pipelines/structure_d/cosmo.py
data/pipelines/structure_d/growth.py
data/pipelines/structure_d/models.py
data/pipelines/structure_d/likelihood.py
results/structure_d/model_comparison.csv
```

## Safe conclusion

The equations are valid as a modeling scaffold. They are not evidence without the run artifacts, data provenance, uncertainty model and adversarial baseline.
