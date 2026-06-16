import numpy as np

# Default gamma updated to V3 Pair 1 (see THEORY.md Section 4).
# Was 0.005 (V2 working value); now 0.003122 (baryogenesis line + Matsubara lead).

def predict_lya_escape(z=13.0, gamma=0.003122):
    """
    Logosfield scalar boost to Ly-alpha escape fraction.
    gamma ~ 0.003122 (V3 default) reduces recombination -> higher visibility at high z.
    """
    # Base escape + scalar enhancement
    f_esc = 0.70 + 0.03 * np.tanh(gamma * (z - 10))
    return f_esc
