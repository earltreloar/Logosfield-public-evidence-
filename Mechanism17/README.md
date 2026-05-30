# Mechanism 17 — H0 Reconciliation (V2 Canonical)
# TDCOSMO + JWST Cepheids
# Last updated: May 29, 2026

## Prediction

  H0 ~= 70.0 +/- 1.5 km/s/Mpc (V2 late-time Phi acceleration)

## Data

TDCOSMO-2025 + JWST Cepheid ladder. Prereg: OSF 2025-11-07.

## V2 Physical Mechanism

In V2, the Logosfield scalar Phi contributes subdominant stress-energy
to the Friedmann equation:

  H^2 = (8 pi G / 3)(rho_m + rho_Phi)
  rho_Phi = 1/2 Phi_dot^2 + V(Phi)

Case B potential V = 1/2 H_0^2 Phi^2 gives w_Phi(z=0) = -0.80.

This modifies the late-time expansion rate, shifting the inferred H0
upward relative to the Planck CMB anchor without introducing new
degrees of freedom beyond the frozen {alpha, beta, gamma} structure.

Important: w_Phi is an internal property of a sub-dominant field
(Omega_Phi ~ 10^-9). It is NOT directly observable as a dark energy
equation of state. DESI w_DE constraints do not apply directly.

## V2 Parameters (frozen)

  alpha = 1, beta ~= 2pi (working assumption), gamma = 0.005

## Status

Under review. Not part of the current locked two-test public challenge
path (CDDR + Mechanism 16). The H0 reconciliation is directionally
consistent with V2 but has not been formally derived to publication
standard. Remains open for development.

## Reproduce

  python Mechanism17/test.py
  make mech17

