"""
Mechanism 16 — null test (V2 Canonical)
Verifies the signature ratio is not produced by random eta fluctuations.
"""
import numpy as np
import random
from predict import predict_sigma8, signature_ratio, SIGMA8_REF

def run_null(n=1000, seed=42):
    random.seed(seed)
    np.random.seed(seed)

    ratios = []
    diffs = []

    for _ in range(n):
        # Null: random eta drawn from noise around 1.0 (no Logosfield signal)
        eta_null = random.gauss(1.0, 0.02)
        s8_null = predict_sigma8(eta=eta_null, mode="conservative")
        diff = s8_null - SIGMA8_REF
        diffs.append(diff)

        # Null signature ratio (should be near 0 for conservative k=0)
        r = signature_ratio(eta_null, s8_null)
        if r is not None:
            ratios.append(r)

    print(f"Null sigma_8 diff mean = {np.mean(diffs):.5f} +/- {np.std(diffs):.5f}")
    print(f"Null signature ratio mean = {np.mean(ratios):.4f} +/- {np.std(ratios):.4f}")
    print(f"(V2 prediction: ratio in 0.13-0.25 from real signal)")

if __name__ == "__main__":
    print("=== Mechanism 16 Null Test ===")
    run_null()

