# Mechanism 15 — Ly-alpha Escape at z=13 (V2 Canonical)
# JWST JADES-GS-z13-1-LA
# Last updated: May 29, 2026

## Prediction

  f_Lya ~= 0.70 +/- 0.03 (V2 memory-covariant scalar boost)

## Data

JADES spectrum (Nature, 2025). Prereg: OSF timestamp 2025-11-07.

## V2 Physical Mechanism

In V2, the Logosfield memory-covariant derivative D_mem,mu acts on
photon-sector matter fields. The Z(Phi) gauge-sector dressing modifies
photon propagation through the high-z IGM.

Z(Phi) = 1 + c_g * Phi / M_Pl

At z=13, Phi(z)/Phi(0) ~= 1.20 (extrapolating V2 Phi evolution table).
The enhanced Z(Phi) at high redshift reduces effective recombination opacity,
boosting Ly-alpha escape fraction above the naive reionization expectation.

Note: EM memory coupling = 0 exactly (conformal invariance). The boost
enters through Z(Phi) gauge dressing, not through direct memory coupling
to photons.

## V2 Parameters (frozen)

  alpha = 1, beta ~= 2pi (working assumption), gamma = 0.005
  c_g: constrained by CDDR (epsilon_g > 0.088 for Euclid threshold)

## Status

Provisional. Preregistered. Not part of the current locked two-test
public challenge path (CDDR + Mechanism 16). Remains scientifically
relevant as a V2 consistency check at high redshift.

## Reproduce

  python Mechanism15/test.py
  make mech15

