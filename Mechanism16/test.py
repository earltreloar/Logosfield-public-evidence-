"""
Mechanism 16 — test (V2 Canonical)
Runs all prediction modes and verifies signature ratio.
"""
from predict import predict_sigma8, eta_prediction, signature_ratio, SIGMA8_REF

def test_conservative():
    pred = predict_sigma8(eta=1.0, mode="conservative")
    assert abs(pred - SIGMA8_REF) < 1e-6, "Conservative mode should return SIGMA8_REF when eta=1"
    print(f"Conservative (k=0): sigma_8 = {pred:.4f}  PASS")

def test_v2_channels():
    s8_c1 = predict_sigma8(mode="channel1")
    s8_c2 = predict_sigma8(mode="channel2")
    s8_v2 = predict_sigma8(mode="v2_combined")
    print(f"Channel 1 (Phi stress):  sigma_8 = {s8_c1:.4f}  ({100*(s8_c1/SIGMA8_REF-1):.2f}%)")
    print(f"Channel 2 (G_eff):       sigma_8 = {s8_c2:.4f}  ({100*(s8_c2/SIGMA8_REF-1):.2f}%)")
    print(f"V2 combined:             sigma_8 = {s8_v2:.4f}  ({100*(s8_v2/SIGMA8_REF-1):.2f}%)")
    assert s8_v2 < SIGMA8_REF, "V2 combined should suppress sigma_8"
    print("V2 suppression direction: PASS")

def test_signature_ratio():
    eta = eta_prediction(epsilon_g=0.15, epsilon_y=-0.021)
    s8 = predict_sigma8(mode="v2_combined")
    ratio = signature_ratio(eta, s8)
    print(f"Signature ratio: {ratio:.3f}  (expected 0.13-0.25)")
    assert 0.10 <= ratio <= 0.30, f"Ratio {ratio:.3f} outside expected range"
    print("Signature ratio: PASS")

if __name__ == "__main__":
    print("=== Mechanism 16 V2 Tests ===")
    test_conservative()
    test_v2_channels()
    test_signature_ratio()
    print("All tests passed.")

