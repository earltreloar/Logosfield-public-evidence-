import numpy as np

def predict_lya_escape(z=13.0, gamma=0.005):
    """
    Logosfield scalar boost to Ly-α escape fraction.
    γ ≈ 0.005 reduces recombination → higher visibility at high z.
    """
    # Base escape + scalar enhancement
    f_esc = 0.70 + 0.03 * np.tanh(gamma * (z - 10))
    return f_esc
