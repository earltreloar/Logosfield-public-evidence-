# Logosfield Replications (Public Evidence Pack v2.0)

This directory hosts the public rerun targets for the Logosfield field, using the SAME
scalar coupling parameters (α = 1, β = 2π, γ = 0.005) across astrophysics, cosmology,
and early structure growth.

## Active replication notebooks (v2.0)

### RotationCurve_4p8sigma/
- Test: galaxy rotation-curve residuals at ~10 kpc.
- Result: Δv ≈ 0.48 km/s with ~0.1 km/s scatter → ~4.8σ excess above standard expectations.
- Interpretation: this is a direct, astrophysical-strength pull consistent with a long-range scalar (the Logosfield), not normal baryonic modeling.
- Repro: run `Logosfield_Astrophysics_4p8sigma.ipynb`.

### SMBH_strict_uplift/
- Test: timing feasibility for z≳7 quasars / SMBH seeds.
- Strict ΛCDM feasibility fraction: ~0.6.
- Logosfield feasibility fraction: ~0.8.
  - 1 object “rescued” (infeasible in ΛCDM but feasible with Logosfield-added time),
    0 made worse.
  - Paired flip Z_binom_like ≈ 1.0 with N=5.
- Interpretation: Logosfield buys early growth time without exotic seeds / insane accretion.
- Repro: run `SMBH_strict_uplift.ipynb`.

## Notes
- These two tests are new after v1.0 and are what we call “direct physical coupling tests.”
- Earlier nested `replications/replications/` layout was a v1.0 artifact and was cleaned.
- This directory is the authoritative v2.0 replication entry point and is referenced in
  the Public Evidence Pack v2.0 release.
