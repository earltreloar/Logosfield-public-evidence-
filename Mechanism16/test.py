"""
Mechanism 16 — test (V3)
Mechanism 16's active sigma_8 prediction is SUSPENDED (see predict.py,
THEORY.md Section 10). These tests verify the suspension is correctly
enforced, rather than asserting any sigma_8 prediction value.
"""
from predict import (
    predict_sigma8,
    eta_prediction,
    signature_ratio,
    SUSPENDED_NOTICE,
    sigma8_v2_combined_legacy,
    SIGMA8_REF,
)


def test_active_functions_are_suspended():
    """Calling any active V3 entry point should raise NotImplementedError."""
    for fn, kwargs in [
        (predict_sigma8, {}),
        (eta_prediction, {"epsilon_g": 0.1, "epsilon_y": 0.1}),
    ]:
        try:
            fn(**kwargs)
            raise AssertionError(f"{fn.__name__} should have raised NotImplementedError")
        except NotImplementedError as e:
            assert "SUSPENDED" in str(e)
    print("Active functions correctly raise NotImplementedError: PASS")


def test_signature_ratio_suspended():
    try:
        signature_ratio(1.0, 0.8)
        raise AssertionError("signature_ratio should have raised NotImplementedError")
    except NotImplementedError:
        pass
    print("signature_ratio correctly suspended: PASS")


def test_v2_legacy_retrievable_for_reference():
    """V2 legacy functions remain callable for historical reference,
    under explicitly renamed identifiers — they are not a current prediction."""
    s8_v2 = sigma8_v2_combined_legacy()
    assert s8_v2 < SIGMA8_REF, "V2 legacy combined prediction should suppress sigma_8 (historical record only)"
    print(f"V2 legacy combined (reference only): sigma_8 = {s8_v2:.4f}  PASS")


if __name__ == "__main__":
    print("=== Mechanism 16 V3 Tests (suspension enforcement) ===")
    test_active_functions_are_suspended()
    test_signature_ratio_suspended()
    test_v2_legacy_retrievable_for_reference()
    print("All tests passed.")
    print()
    print(SUSPENDED_NOTICE)
