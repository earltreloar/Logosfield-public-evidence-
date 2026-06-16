"""
Mechanism 16 — sigma_8 response
STATUS: SUSPENDED (V3) — see THEORY.md Section 10 and Cosmology.md

The V2 predictions below depended on a linear EFT completion
(Z(Phi) = 1 + c_g*Phi/M_Pl, Y(Phi) = 1 + c_y*Phi/M_Pl) that has been
removed after an audit found an eight-order-of-magnitude conflict with
precision measurements. The replacement, conformally-protected coupling
form is quadratic in Phi/M_Pl and reduces to exactly 1 at Phi=0. Since
V(Phi)'s classical minimum is at Phi=0, and the cosmological reference
value Phi_ref is not yet derived (Gap 8, open), there is currently no
V3-consistent prediction for sigma_8 to compute.

Calling any of the V2 prediction functions below will raise
NotImplementedError. They are retained, renamed with a _v2_legacy
suffix, for historical/reference purposes only — do not use them as
a current prediction of the framework.

A V3-consistent rederivation, once Gap 8 is resolved, should replace
this file's active entry points.
"""

import numpy as np

SUSPENDED_NOTICE = (
    "Mechanism 16 sigma_8 prediction is SUSPENDED (V3). "
    "It depended on a linear EFT completion (c_g, c_y) removed for "
    "conflicting with precision measurements by ~8 orders of magnitude. "
    "See THEORY.md Section 10 and Cosmology.md. Gap 8 (Phi_ref) must be "
    "resolved before a V3-consistent prediction can be computed."
)

# Current default parameters (V3, Pair 1) — see THEORY.md Section 4
ALPHA = 1.0
BETA = 2 * np.pi
GAMMA = 0.003122

# Reference value, retained for context (not used by any active function)
SIGMA8_REF = 0.8121   # DESI+CMB


def _suspended(*args, **kwargs):
    raise NotImplementedError(SUSPENDED_NOTICE)


# Active entry points — all suspended pending Gap 8
eta_prediction = _suspended
sigma8_channel1_phi_stress = _suspended
sigma8_channel2_geff = _suspended
sigma8_v2_combined = _suspended
sigma8_from_eta = _suspended
predict_sigma8 = _suspended
signature_ratio = _suspended


# ---------------------------------------------------------------------
# V2 LEGACY — historical reference only. NOT a current prediction.
# Renamed with _v2_legacy suffix so they cannot be imported under their
# original names and mistaken for active V3 functions.
# ---------------------------------------------------------------------

A_G_V2_LEGACY = 0.5             # exact analytical, V2
A_Y_FY_V2_LEGACY = 0.2384       # numerical, z=0.5, V2
G_EFF_RATIO_V2_LEGACY = 0.98


def eta_prediction_v2_legacy(epsilon_g, epsilon_y, z=0.5):
    """V2 (superseded): eta(z=0.5)-1 = -0.0569*epsilon_g + 0.2384*epsilon_y."""
    return 1.0 + (-0.0569 * epsilon_g + A_Y_FY_V2_LEGACY * epsilon_y)


def sigma8_channel1_phi_stress_v2_legacy():
    """V2 (superseded): Phi stress-energy channel, -1.13% suppression."""
    return SIGMA8_REF * (1 - 0.0113)


def sigma8_channel2_geff_v2_legacy(g_eff_ratio=G_EFF_RATIO_V2_LEGACY):
    """V2 (superseded): Y(Phi) G_eff channel, -6.82% at G_eff/G=0.98."""
    return SIGMA8_REF * (1 - 0.0682 * (1 - g_eff_ratio) / 0.02)


def sigma8_v2_combined_legacy(epsilon_y=-0.021):
    """V2 (superseded): combined dual-channel prediction."""
    suppression = -0.0569 + 10 * epsilon_y
    suppression = max(-0.08, min(-0.01, suppression))
    return SIGMA8_REF * (1 + suppression)


if __name__ == "__main__":
    print("=== Mechanism 16 — sigma_8 response ===")
    print()
    print("STATUS: SUSPENDED (V3)")
    print(SUSPENDED_NOTICE)
    print()
    print("Historical V2 values (NOT a current prediction; for reference only):")
    s8_1 = sigma8_channel1_phi_stress_v2_legacy()
    s8_2 = sigma8_channel2_geff_v2_legacy()
    s8_v2 = sigma8_v2_combined_legacy()
    print(f"  V2 channel1 (Phi stress): {s8_1:.4f}  ({100*(s8_1/SIGMA8_REF-1):.2f}%)")
    print(f"  V2 channel2 (G_eff):      {s8_2:.4f}  ({100*(s8_2/SIGMA8_REF-1):.2f}%)")
    print(f"  V2 combined:              {s8_v2:.4f}  ({100*(s8_v2/SIGMA8_REF-1):.2f}%)")
    print()
    print("These V2 numbers should not be cited as a current framework prediction.")
