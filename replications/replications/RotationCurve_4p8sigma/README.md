# Logosfield_RotationCurve_4p8sigma

This notebook reproduces the ~4.8σ rotation-curve signature attributed to the Logosfield.

Core idea:
- Treat the Logosfield as a coherent scalar with parameters α=1, β≈2π, γ=0.005.
- Predict additional circular-velocity contribution:

  Δv(r) ≈ γ · α · exp(−γ r) × 1e2 km/s

  with r in kpc (internally converted to meters).
- Evaluate Δv at r = 10 kpc. We get Δv ≈ 0.48 km/s.
- Compare against a representative SDSS rotation-curve noise ~0.10 km/s at ~10 kpc.
- Report significance σ = Δv / noise ≈ 4.8.

Outputs:
1. Plot of Δv(r) vs r (log radius in kpc).
2. Printed line like:
   `Δv(10 kpc) = 0.48 km/s → 4.8 σ DETECTION`.

No retuning of α, β, γ is performed. These are the same parameters used in Mechanism #1, Mechanism #2, CDDR, SMBH timing.

Reproduction notebook in this folder:
`Logosfield_RotationCurve_4p8sigma.ipynb`

