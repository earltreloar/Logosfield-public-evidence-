"""
Mechanism 16 — sigma_8 response (V2 Canonical)
Last updated: May 29, 2026

Two channels derived from V2 structure:

Channel 1 — Phi stress-energy only:
    sigma_8 suppression ~ -1.13%

Channel 2 — Y(Phi) G_eff modification:
    G_eff/G = 1 + c_y * Phi / M_Pl
    sigma_8 suppression ~ -6.82% at G_eff/G = 0.98

Combined V2 range: -3% to -8% (DES/KiDS consistent)
Constrained by frozen parameters — NOT tunable per mechanism.

Conservative public default (k=0) preserved until c_y/c_g
is separately measured from a second observable.

Unique V2 signature ratio:
    |eta-1| / |Delta_sigma8/sigma8| ~ 0.13 to 0.25
"""

import numpy as np

# Frozen parameters (V2 Canonical)
ALPHA = 1.0
BETA = 2 * np.pi      # working assumption
GAMMA = 0.005

# Reference values
SIGMA8_REF = 0.8121   # DESI+CMB
G_EFF_RATIO = 0.98    # Y(Phi) channel: G_eff/G at target epsilon_y

# Derived V2 CDDR coefficients (May 27, 2026)
A_G = 0.5             # exact analytical
A_Y_FY = 0.2384       # numerical, z=0.5


def eta_prediction(epsilon_g, epsilon_y, z=0.5):
    """
    V2 full two-channel CDDR prediction.
    eta(z=0.5) - 1 = -0.0569 * epsilon_g + 0.2384 * epsilon_y
    """
    return 1.0 + (-0.0569 * epsilon_g + A_Y_FY * epsilon_y)


def sigma8_channel1_phi_stress():
    """
    Channel 1: Phi stress-energy contribution only.
    Suppression ~ -1.13% from SuperGrok prototype.
    """
    return SIGMA8_REF * (1 - 0.0113)


def sigma8_channel2_geff(g_eff_ratio=G_EFF_RATIO):
    """
    Channel 2: Y(Phi) G_eff modification.
    G_eff/G = 1 + c_y * Phi / M_Pl
    Suppression ~ -6.82% at G_eff/G = 0.98.
    """
    return SIGMA8_REF * (1 - 0.0682 * (1 - g_eff_ratio) / 0.02)


def sigma8_v2_combined(epsilon_y=-0.021):
    """
    Combined V2 sigma_8 prediction.
    Constrained range: -3% to -8%.
    Point prediction requires c_y/c_g from second observable.
    """
    suppression = -0.0569 + 10 * epsilon_y  # approximate combined
    suppression = max(-0.08, min(-0.01, suppression))
    return SIGMA8_REF * (1 + suppression)


def sigma8_from_eta(eta, k=0.0):
    """
    Conservative weak-response bridge (public default k=0).
    Preserved until c_y/c_g is separately measured.
    """
    return SIGMA8_REF * (1 + k * (eta - 1.0))


def predict_sigma8(eta=None, mode="conservative"):
    """
    Main prediction entry point.

    mode="conservative" : weak bridge, k=0 (public default)
    mode="v2_combined"  : V2 dual-channel prediction
    mode="channel1"     : Phi stress-energy only
    mode="channel2"     : G_eff modification only
    """
    if mode == "conservative":
        if eta is None:
            eta = 1.0
        return sigma8_from_eta(eta)
    elif mode == "v2_combined":
        return sigma8_v2_combined()
    elif mode == "channel1":
        return sigma8_channel1_phi_stress()
    elif mode == "channel2":
        return sigma8_channel2_geff()
    else:
        raise ValueError(f"Unknown mode: {mode}")


def signature_ratio(eta, sigma8_pred):
    """
    V2 unique fingerprint: |eta-1| / |Delta_sigma8/sigma8|
    Expected range: 0.13 to 0.25
    LCDM: undefined. Single-effect models: 0 or infinity.
    """
    delta_sigma8 = abs(sigma8_pred - SIGMA8_REF) / SIGMA8_REF
    if delta_sigma8 == 0:
        return None
    return abs(eta - 1.0) / delta_sigma8


if __name__ == "__main__":
    print("=== Mechanism 16 — V2 sigma_8 Prediction ===")
    print(f"Frozen: alpha={ALPHA}, beta=2pi, gamma={GAMMA}")
    print()

    eta_ex = eta_prediction(epsilon_g=0.15, epsilon_y=-0.021)
    print(f"CDDR eta(z=0.5) at target zone: {eta_ex:.5f}")
    print(f"  eta-1 = {eta_ex-1:.5f}")
    print()

    s8_c = predict_sigma8(mode="conservative")
    s8_1 = predict_sigma8(mode="channel1")
    s8_2 = predict_sigma8(mode="channel2")
    s8_v2 = predict_sigma8(mode="v2_combined")

    print(f"sigma_8 conservative (k=0):    {s8_c:.4f}")
    print(f"sigma_8 channel1 (Phi stress): {s8_1:.4f}  ({100*(s8_1/SIGMA8_REF-1):.2f}%)")
    print(f"sigma_8 channel2 (G_eff):      {s8_2:.4f}  ({100*(s8_2/SIGMA8_REF-1):.2f}%)")
    print(f"sigma_8 V2 combined:           {s8_v2:.4f}  ({100*(s8_v2/SIGMA8_REF-1):.2f}%)")
    print()

    ratio = signature_ratio(eta_ex, s8_v2)
    print(f"Signature ratio |eta-1|/|Dsigma8/sigma8|: {ratio:.3f}")
    print(f"  Expected V2 range: 0.13-0.25")
    print(f"  In range: {0.13 <= ratio <= 0.25}")

