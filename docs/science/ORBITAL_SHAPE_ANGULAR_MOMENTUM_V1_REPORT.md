# Orbital Shape Angular Momentum v1 Report

Status: seed-level metric report
Claim level: `claim_allowed=false`

> These calculations use reference seed parameters only. Raw ephemeris vectors, gravity/shape models, uncertainty, and baselines remain required.

| Record | Body | h specific km²/s | speed proxy km/s | spin proxy kg m²/s | Claim |
|---|---|---:|---:|---:|---:|
| `REAL_ORBIT_EARTH_HELIOCENTRIC_SHAPE_AM_V1` | Earth | 4.4551e+09 | 29.7805 | 5.85882e+33 | `false` |
| `REAL_ORBIT_MOON_GEOCENTRIC_SHAPE_AM_V1` | Moon | 393242 | 1.023 | 2.31828e+29 | `false` |
| `REAL_ORBIT_MARS_HELIOCENTRIC_SHAPE_AM_V1` | Mars | 5.47599e+09 | 24.0239 | 1.92124e+32 | `false` |
| `REAL_ORBIT_JUPITER_HELIOCENTRIC_SHAPE_AM_V1` | Jupiter | 1.01522e+10 | 13.041 | 4.50397e+38 | `false` |

## Safe conclusion

The orbital-shape-angular-momentum route now has first-pass computable seed metrics. It still does not validate a new gravity, deformation, or RLL claim.
