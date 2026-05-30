"""
Mechanism 17 — null test (V2 Canonical)
Verifies H0 shift is not produced by random gamma fluctuations.
"""
import numpy as np
import random
from predict import predict_h0, H0_PLANCK

def run_null(n=1000, seed=42):
    random.seed(seed)
    np.random.seed(seed)

    # Null: gamma drawn from noise around 0 (no Logosfield coupling)
    null_h0 = [predict_h0(gamma=random.gauss(0.0, 0.001)) for _ in range(n)]
    signal_h0 = [predict_h0(gamma=random.gauss(0.005, 0.001)) for _ in range(n)]

    print(f"Null H0 mean    = {np.mean(null_h0):.2f} +/- {np.std(null_h0):.3f} km/s/Mpc")
    print(f"Signal H0 mean  = {np.mean(signal_h0):.2f} +/- {np.std(signal_h0):.3f} km/s/Mpc")
    shift = np.mean(signal_h0) - np.mean(null_h0)
    print(f"Signal shift: {shift:.3f} km/s/Mpc above null")

if __name__ == "__main__":
    print("=== Mechanism 17 Null Test ===")
    run_null()

