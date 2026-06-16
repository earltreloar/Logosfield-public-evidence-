"""
Mechanism 16 — null test (V3)
The original null test compared the V2 signature ratio against random
eta fluctuations. Since the V2 prediction is suspended (predict.py,
THEORY.md Section 10), there is currently no active signal to null-test
against. This file verifies that the suspension is correctly enforced
and is retained as a placeholder for a V3-consistent null test once
Gap 8 is resolved and a rederived prediction exists.
"""
from predict import predict_sigma8, signature_ratio, SUSPENDED_NOTICE


def run_null():
    print("Mechanism 16's active prediction is SUSPENDED — no null test to run.")
    print(SUSPENDED_NOTICE)
    try:
        predict_sigma8()
        raise AssertionError("predict_sigma8 should be suspended")
    except NotImplementedError:
        print("Confirmed: predict_sigma8 correctly raises NotImplementedError.")
    try:
        signature_ratio(1.0, 0.8)
        raise AssertionError("signature_ratio should be suspended")
    except NotImplementedError:
        print("Confirmed: signature_ratio correctly raises NotImplementedError.")


if __name__ == "__main__":
    print("=== Mechanism 16 Null Test (V3 — suspension check) ===")
    run_null()
