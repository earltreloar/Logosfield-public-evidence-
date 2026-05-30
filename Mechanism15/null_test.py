"""
Mechanism 15 — null test (V2 Canonical)
Verifies the Ly-alpha boost is not produced by random z fluctuations.
"""
import numpy as np
import random
from predict import predict_lya_escape

def run_null(n=1000, seed=42):
    random.seed(seed)
    np.random.seed(seed)

    # Null: random redshifts across a broad range (no specific z=13 signal)
    null_f = [predict_lya_escape(z=random.uniform(6, 15), gamma=0.005) for _ in range(n)]

    # Signal: at z=13 with frozen gamma
    signal_f = predict_lya_escape(z=13.0, gamma=0.005)

    print(f"Null f_Lya mean = {np.mean(null_f):.4f} +/- {np.std(null_f):.4f}")
    print(f"Signal f_Lya at z=13: {signal_f:.4f}")
    snr = (signal_f - np.mean(null_f)) / np.std(null_f)
    print(f"Null SNR = {snr:.3f}")

if __name__ == "__main__":
    print("=== Mechanism 15 Null Test ===")
    run_null()

