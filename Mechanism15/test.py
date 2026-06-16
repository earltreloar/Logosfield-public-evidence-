"""
Mechanism 15 — test
Ly-alpha escape fraction at z=13 (JWST JADES-GS-z13-1-LA)

Status: provisional, exploratory — see README.md for the note on the
superseded Z(Phi) mechanism description. Default gamma updated to V3
Pair 1 (0.003122); test_frozen_gamma below checks both the new default
and the historical V2 value for reference.
"""
from predict import predict_lya_escape

GAMMA_V3 = 0.003122
GAMMA_V2_LEGACY = 0.005


def test_lya_prediction():
    pred = predict_lya_escape(z=13.0)
    target = 0.70
    uncertainty = 0.03
    diff = abs(pred - target)
    print(f"Predicted f_Lya at z=13 (gamma={GAMMA_V3}): {pred:.4f}")
    print(f"Target: {target} +/- {uncertainty}")
    print(f"Difference from target: {diff:.4f}")
    in_range = diff <= uncertainty
    print(f"Within uncertainty: {'PASS' if in_range else 'FAIL'}")
    return pred


def test_redshift_scaling():
    for z in [6, 10, 13, 15]:
        f = predict_lya_escape(z=z)
        print(f"  z={z:2d}: f_Lya = {f:.4f}")
    print("Redshift scaling: complete")


def test_frozen_gamma():
    f_v3 = predict_lya_escape(z=13.0, gamma=GAMMA_V3)
    f_v2_legacy = predict_lya_escape(z=13.0, gamma=GAMMA_V2_LEGACY)
    f_zero = predict_lya_escape(z=13.0, gamma=0.0)
    print(f"gamma={GAMMA_V3} (V3 default): f_Lya = {f_v3:.4f}")
    print(f"gamma={GAMMA_V2_LEGACY} (V2 legacy):  f_Lya = {f_v2_legacy:.4f}")
    print(f"gamma=0.000 (no coupling): f_Lya = {f_zero:.4f}")
    assert f_v3 >= f_zero, "Memory coupling should boost escape fraction"
    print("Gamma boost direction: PASS")


if __name__ == "__main__":
    print("=== Mechanism 15 Tests — Ly-alpha escape z=13 (V3 parameters) ===")
    test_lya_prediction()
    print()
    test_redshift_scaling()
    print()
    test_frozen_gamma()
