# Orbital Shape Angular Momentum v1 Report

Status: seed-level metric report  
Claim level: `claim_allowed=false`

> These calculations use reference seed parameters only. Raw ephemeris vectors, gravity/shape models, uncertainty, and baselines remain required.

---

## Results

| Record | Body | h specific km²/s | speed proxy km/s | spin proxy kg m²/s | Claim |
|---|---|---:|---:|---:|---:|
| `REAL_ORBIT_EARTH_HELIOCENTRIC_SHAPE_AM_V1` | Earth | 4.4551e+09 | 29.7805 | 5.85882e+33 | `false` |
| `REAL_ORBIT_MOON_GEOCENTRIC_SHAPE_AM_V1` | Moon | 393242 | 1.023 | 2.31828e+29 | `false` |
| `REAL_ORBIT_MARS_HELIOCENTRIC_SHAPE_AM_V1` | Mars | 5.47599e+09 | 24.0248 | 1.92124e+32 | `false` |
| `REAL_ORBIT_JUPITER_HELIOCENTRIC_SHAPE_AM_V1` | Jupiter | 1.01522e+10 | 13.041 | 4.50397e+38 | `false` |

---

## Formulas used

```text
h = sqrt(mu_central * a * (1 - e^2))
v ≈ h / a
omega = 2*pi / rotation_period
S ≈ Cbar * M * R^2 * omega
f = (Req - Rpole) / Req
```

---

## What this means

The orbital-shape-angular-momentum route now has first-pass computable seed metrics for Earth, Moon, Mars, and Jupiter.

This is not a raw ephemeris integration and is not a final deformation or gravity claim.

---

## Required next data

```text
raw JPL Horizons or SPICE state vectors
gravity harmonics with source/version
shape or reference ellipsoid model with source/version
rotation and pole orientation model
uncertainty or covariance model
Kepler/Newton/N-body/J2 baseline comparison
```

---

## Safe conclusion

```text
reference seed parameters + v1 formulas = first computable orbital route
reference seed parameters + v1 formulas ≠ final validation claim
```
