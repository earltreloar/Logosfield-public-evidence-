# Mechanism 16 — sigma_8 Response
# STATUS: SUSPENDED (V3)

## Status

**SUSPENDED.** This mechanism's prediction depended on a linear EFT completion (`Z(Phi) = 1 + c_g*Phi/M_Pl`, `Y(Phi) = 1 + c_y*Phi/M_Pl`) that has been removed after an audit found an eight-order-of-magnitude conflict with precision measurements (see repository `00_THEORY.md` Section 6 and `04_EFT_couplings.md`).

The replacement, conformally-protected coupling form is quadratic in `Phi/M_Pl` and reduces to exactly 1 at `Phi=0`. The scalar potential `V(Phi)` has since been derived and its classical minimum is at `Phi=0`. Producing a non-trivial sigma_8 response requires a cosmological reference value `Phi_ref != 0` that is not currently derivable (Gap 8, open — see `00_THEORY.md` Section 9). **There is therefore currently no V3-consistent prediction to test.**

`predict.py`'s active entry points now raise `NotImplementedError` rather than returning a number, so that running this mechanism cannot be mistaken for a current, validated prediction. `test.py` and `null_test.py` verify this suspension is correctly enforced.

---

## Historical V2 mechanism (superseded — for reference only)

The V2 sigma_8 suppression was claimed via two channels:

**Channel 1 — Phi stress-energy:**
```
H^2 = (8*pi*G/3)(rho_m + rho_Phi)
rho_Phi = 1/2*Phi_dot^2 + V(Phi)
Result: -1.13% sigma_8 suppression
```

**Channel 2 — Y(Phi) G_eff modification (removed coupling):**
```
G_eff/G ~= 1 + c_y*Phi/M_Pl
Result: -6.82% at G_eff/G = 0.98
```

These numbers are retained in `predict.py` as `_v2_legacy`-suffixed functions for historical record. They should not be cited as a current prediction of the framework.

---

## What would be needed to un-suspend this mechanism

1. Resolution of Gap 8 — an independently-derived, non-zero cosmological `Phi_ref`.
2. A rederivation of the sigma_8 response using the quadratic conformal-protection coupling form (`h(Phi/M_Pl) = 1 + O(gamma)*(Phi/M_Pl)^2`), not the removed linear form.
3. Re-evaluation of whether the resulting suppression remains in a range distinguishable from LCDM and from other modified-gravity models, repeating the joint CDDR/sigma_8 signature-ratio analysis under the new formula.

Until all three are complete, this mechanism remains suspended.
