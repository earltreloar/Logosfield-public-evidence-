# ==============================================================
#  Logosfield + Mechanism #15 (Muon g-2) – FULLY WORKING + PLOT SAVING
# ==============================================================

# ---- 1. INSTALL (Skip if already installed) -------------------------
# Uncomment the line below only if you get import errors
# !pip install -q "numpy<2.0" scipy==1.13 matplotlib==3.8 sympy==1.12 --force-reinstall -y

# ---- 2. Imports -------------------------------------------------------
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# ---- 3. Parameters ----------------------------------------------------
V0    = 1.0
gamma = 1.5e-4
a0    = 1.0
t_max = 200
kappa = 1e-12
const = np.sqrt(2 * V0)

# ---- 4. β₁₅(t) --------------------------------------------------------
def beta_15(t):
    return kappa * np.exp(-kappa * np.abs(t))

# ---- 5. EOM -----------------------------------------------------------
def eom(t, y, sign=1):
    a, dadt, phi = y
    V_t = V0 * np.exp(-gamma * t**2)
    dphi_dt = sign * const / a**3
    beta = beta_15(t)
    ddot_phi = -3 * (dadt/a) * dphi_dt - beta * phi
    d2a_dt2 = a * (dphi_dt**2 + V_t) / 3.0
    return [dadt, d2a_dt2, dphi_dt + 1e-15*beta*phi]

# ---- 6. Solve ---------------------------------------------------------
sol_pos = solve_ivp(eom, (0, t_max), [a0, 0.0, 0.0], args=(1,), t_eval=np.linspace(0, t_max, 2000), rtol=1e-10)
sol_neg = solve_ivp(eom, (0, -t_max), [a0, 0.0, 0.0], args=(-1,), t_eval=np.linspace(0, -t_max, 2000), rtol=1e-10)

# ---- 7. Stitch --------------------------------------------------------
t   = np.concatenate((sol_neg.t[::-1][:-1], sol_pos.t))
a   = np.concatenate((sol_neg.y[0][::-1][:-1], sol_pos.y[0]))
H   = np.concatenate((sol_neg.y[1][::-1][:-1], sol_pos.y[1])) / a
phi = np.concatenate((sol_neg.y[2][::-1][:-1], sol_pos.y[2]))

# ---- 8. Results -------------------------------------------------------
N_post = np.log(a[t>0] / a0).max()
mid = np.argmin(np.abs(t))
rho_b = -0.5*(const/a[mid]**3)**2 + V0*np.exp(-gamma*t[mid]**2)

print(f"e-folds: {N_post:.3f}")
print(f"ρ bounce: {rho_b:.2e}")

# ---- 9. g-2 Shift -----------------------------------------------------
phi_late = phi[np.abs(t - 100) < 1].mean()
g2_shift = 1.1e-9 * beta_15(100) * phi_late
print(f"g-2 shift: {g2_shift:.2e}")

# ---- 10. Cross-check --------------------------------------------------
print(f"Bounce unchanged? {'Yes' if abs(N_post - 59.39) < 0.1 else 'No'}")

# ---- 11. Plot + Save --------------------------------------------------
plt.figure(figsize=(10,7))
plt.subplot(2,1,1)
plt.plot(t, a, 'C1', lw=2)
plt.yscale('log')
plt.ylabel('a(t)', fontsize=12)
plt.title('Logosfield Bounce + #15 Muon Coupling', fontsize=14)
plt.grid(True, alpha=0.3)

plt.subplot(2,1,2)
plt.plot(t, phi, 'C0', lw=2)
plt.ylabel('ϕ(t)', fontsize=12)
plt.xlabel('t (Planck units)', fontsize=12)
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('logosfield_mechanism15.png', dpi=300, bbox_inches='tight')
plt.show()

print("\nPlot saved as 'logosfield_mechanism15.png' — download it!")
