"""
Mechanism 15 — test (V2 Canonical)
Ly-alpha escape fraction at z=13 (JWST JADES-GS-z13-1-LA)
"""
from predict import predict_lya_escape

def test_lya_prediction():
    pred = predict_lya_escape(z=13.0)
    target = 0.70
    uncertainty = 0.03
    diff = abs(pred - target)
    print(f"Predicted f_Lya at z=13: {pred:.4f}")
    print(f"Target: {target} +/- {uncertainty}")
    print(f"Difference from target: {diff:.4f}")
    in_range = diff <= uncertainty
    print(f"Within uncertainty: {PASS if in_range else FAIL}")
    return pred

def test_redshift_scaling():
    for z in [6, 10, 13, 15]:
        f = predict_lya_escape(z=z)
        print(f"  z={z:2d}: f_Lya = {f:.4f}")
    print("Redshift scaling: complete")

def test_frozen_gamma():
    f_default = predict_lya_escape(z=13.0, gamma=0.005)
    f_zero = predict_lya_escape(z=13.0, gamma=0.0)
    print(f"gamma=0.005: f_Lya = {f_default:.4f}")
    print(f"gamma=0.000: f_Lya = {f_zero:.4f}")
    assert f_default >= f_zero, "Memory coupling should boost escape fraction"
    print("Gamma boost direction: PASS")

if __name__ == "__main__":
    print("=== Mechanism 15 V2 Tests — Ly-alpha escape z=13 ===")
    test_lya_prediction()
    print()
    test_redshift_scaling()
    print()
    test_frozen_gamma()

