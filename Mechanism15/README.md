# Mechanism 15 — Ly-alpha Escape at z=13
# JWST JADES-GS-z13-1-LA

## Status

Provisional. Preregistered. Not part of the current locked public challenge path (see `THEORY.md` / `CHALLENGE.md`). The mechanism's stated physical explanation has been partially superseded — see note below — and should currently be read as exploratory rather than an active prediction.

## Parameter update (V3)

Default `gamma` updated from `0.005` (V2 working value) to `0.003122` (V3 Pair 1 — see `THEORY.md` Section 4).

## Important correction — mechanism description superseded

The original (V2) physical mechanism for this prediction invoked `Z(Phi) = 1 + c_g*Phi/M_Pl`, the linear gauge-sector EFT coupling. **That coupling has been removed** (see `THEORY.md` Section 6, `EFT couplings`) after an audit found an eight-order-of-magnitude conflict with precision measurements. It has been replaced by a derived, conformally-protected form, `f(Phi/M_Pl) = 1 + O(gamma)*(Phi/M_Pl)^2`, which is quadratic rather than linear in `Phi/M_Pl` and has no free coefficient `c_g`.

This mechanism's prediction has **not yet been rederived** using the corrected coupling form. The number below (`f_esc ~ 0.70`) is retained from the original V2 derivation for historical reference, with only the `gamma` default updated; the underlying physical argument that motivated it (linear `Z(Phi)` dressing reducing recombination opacity) no longer matches the framework's derived coupling structure. This should be treated as **provisional and likely requiring rederivation**, not as a currently validated V3 prediction.

## Prediction (as previously stated, gamma updated, mechanism not rederived)

```
f_Lya ~= 0.70 +/- 0.03   (gamma = 0.003122; underlying Z(Phi) argument superseded — see above)
```

## Data

JADES spectrum (Nature, 2025). Prereg: OSF timestamp 2025-11-07.

## What would be needed to restore this mechanism to active status

A rederivation of the high-z photon escape argument using the corrected, conformally-protected coupling form (`f(Phi/M_Pl) = 1 + O(gamma)*(Phi/M_Pl)^2`) in place of the removed linear `Z(Phi)`. Note also that EM memory coupling is `gamma_EM = 0` exactly (conformal invariance, Force Coupling Table) — any high-z photon effect would need to enter through a different channel than direct EM memory coupling, consistent with how the original mechanism framed it (via the scalar dressing, not direct coupling).

## Reproduce

```
python Mechanism15/test.py
make mech15
```
