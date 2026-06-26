# RLL Parameter Policy Checklist

Use before any run that reports chi2, AIC, AICc or BIC.

## Parameter policy

- [ ] H0 declared as free, fixed, or prior.
- [ ] Omega_m declared as free, fixed, or derived.
- [ ] Omega_b h2 declared if r_d is derived.
- [ ] Omega_c h2 declared if physical densities are used.
- [ ] Omega_k declared flat or released for every compared model.
- [ ] r_d policy is identical for LCDM, wCDM, CPL and RLL.
- [ ] w is counted in k for wCDM if fitted.
- [ ] w0 and wa are counted in k for CPL if fitted.
- [ ] Sigma_mnu and N_eff have one shared policy across all models if used.
- [ ] sigma8 and S8 are declared only for growth/lensing/RSD runs.
- [ ] M_abs is counted in k if fitted as an SN nuisance.
- [ ] Os0, zt and wt are marked as RLL authorial and counted in k.

## Covariance policy

- [ ] DESI BAO covariance policy declared.
- [ ] Pantheon+ raw files and covariance hash recorded before SN claim.
- [ ] CMB compressed covariance declared; diagonal/proxy marked partial.
- [ ] Growth marked proxy unless benchmarked by CLASS or CAMB.

## Claim policy

- [ ] Same data vector used for LCDM, wCDM, CPL and RLL.
- [ ] Same covariance policy used for all models in one table.
- [ ] Delta AICc and Delta BIC are reported relative to CPL.
- [ ] TOKEN_VAZIO is used for missing evidence instead of inference.
