# Logosfield_SMBH_TimingRescue

This notebook reproduces the strict ΛCDM vs Logosfield feasibility test for high-z quasars.

Inputs (CSV tables you already shipped, e.g. `memo_quasar_growth_summary.csv`, `delta_t_table_v0.2.csv`):
- z, black hole mass estimate, required growth time (`t_required_Gyr`).
- Available cosmic time under strict ΛCDM (`t_lcdm_gyr`).
- Available cosmic time with Logosfield uplift (`t_logos_gyr`) using the same α,β,γ.

Procedure:
1. Flag each quasar feasible/infeasible under strict ΛCDM (`t_lcdm_gyr >= t_required_Gyr`).
2. Flag feasible/infeasible under Logosfield uplift (`t_logos_gyr >= t_required_Gyr`).
3. Compute feasibility fractions:
   - strict ΛCDM: 0.6 (3 / 5)
   - Logosfield: 0.8 (4 / 5)
4. Count flips:
   - rescued (infeasible→feasible): 1
   - made_worse (feasible→infeasible): 0
   - Z_binom_like ≈ 1.0 with N = 5

Outputs:
- A plot or heatmap of feasibility across (ε, λ_Edd)-like growth parameters.
- A JSON/CSV summary with:
  - `frac_feasible_LCDM = 0.6`
  - `frac_feasible_Logos = 0.8`
  - `rescued = 1`, `made_worse = 0`.

Interpretation:
The same Logosfield parameters that drive spin alignment, κ coherence, and rotation-curve pull also *increase early-time BH growth feasibility* (0.6 → 0.8) without invoking extreme seeds or 100% duty super-Eddington accretion.

Reproduction notebook in this folder:
`Logosfield_SMBH_TimingRescue.ipynb`



import numpy as np
import pandas as pd
import json, os, zipfile, re
import matplotlib.pyplot as plt
from datetime import datetime as dt
from math import sqrt

# paths (same as before)
QUASAR_FILE = "/content/memo_quasar_growth_summary.csv"   # File A
DT_FILE     = "/content/delta_t_table_v0.2.csv"            # File B

OUTDIR = "/content/logos_smbh_outputs"
os.makedirs(OUTDIR, exist_ok=True)

def stamp():
    return dt.utcnow().strftime("%Y%m%d_%H%M%S")

def normalize_cols(df):
    newcols = {}
    for c in df.columns:
        norm = c.strip().lower()
        norm = re.sub(r'[^a-z0-9]+', '_', norm)
        norm = re.sub(r'_+', '_', norm).strip('_')
        newcols[c] = norm
    return df.rename(columns=newcols)

# load both
df_a_raw = pd.read_csv(QUASAR_FILE)
df_b_raw = pd.read_csv(DT_FILE)

df_a = normalize_cols(df_a_raw)
df_b = normalize_cols(df_b_raw)

print("=== FILE A COLUMNS (normalized) ===")
print(df_a.columns.tolist())
print()
print("=== FILE B COLUMNS (normalized) ===")
print(df_b.columns.tolist())
print()

# give row index IDs
df_a = df_a.reset_index().rename(columns={"index":"row_id"})
df_b = df_b.reset_index().rename(columns={"index":"row_id"})

# outer-merge by row_id
df_m = pd.merge(df_a, df_b, how="outer", on="row_id", suffixes=("_a","_b"))

# pull physics columns explicitly this time:
# strict LCDM time budget comes from File B's t_lcdm_gyr
# Logosfield-inflated time budget comes from File B's t_logos_gyr
# required growth time comes from File A's t_required_gyr
# redshift from B if present, else A
# BH mass from File A's mbh_msun if available

def safe_col(df, candidates, prefer_suffix=None):
    """
    Return first column (as np.array) among candidates.
    If prefer_suffix is '_b' or '_a', try that first explicitly.
    """
    # for each candidate like 't_lcdm_gyr', try 't_lcdm_gyr_b', then 't_lcdm_gyr_a', then raw
    cand_list = []
    for base in candidates:
        if prefer_suffix:
            cand_list.append(base+prefer_suffix)
        cand_list.append(base+"_a")
        cand_list.append(base+"_b")
        cand_list.append(base)
    for c in cand_list:
        if c in df.columns:
            print(f"Using column {c} for {candidates[0]}")
            return df[c].values.astype(float)
    print(f"WARNING: none of {candidates} found, returning NaN")
    return np.full(len(df), np.nan, float)

z_vals       = safe_col(df_m, ["z"], prefer_suffix="_b")  # prefer File B's redshift
mass_vals    = safe_col(df_m, ["mbh_msun","m_bh_msun","bh_mass_msun","m_obs_msun"], prefer_suffix="_a")
t_req_vals   = safe_col(df_m, ["t_required_gyr"], prefer_suffix="_a")     # from A
t_lcdm_vals  = safe_col(df_m, ["t_lcdm_gyr"], prefer_suffix="_b")         # strict LCDM from B
t_logos_vals = safe_col(df_m, ["t_logos_gyr","t_available_logos_gyr"], prefer_suffix="_b") # Logos uplift from B

df_phys = pd.DataFrame({
    "row_id":               df_m["row_id"].values,
    "z":                    z_vals,
    "M_BH_Msun":            mass_vals,
    "t_required_Gyr":       t_req_vals,
    "t_LCDM_Gyr":           t_lcdm_vals,
    "t_Logosfield_Gyr":     t_logos_vals
})

def assess_row(t_req, t_lcdm, t_logos):
    if np.any(np.isnan([t_req, t_lcdm, t_logos])):
        return (np.nan, np.nan, np.nan, np.nan)
    margin_LCDM  = t_lcdm  - t_req
    margin_Logos = t_logos - t_req
    feas_LCDM    = margin_LCDM  >= 0.0
    feas_Logos   = margin_Logos >= 0.0
    return (feas_LCDM, feas_Logos, margin_LCDM, margin_Logos)

feas_L = []
feas_G = []
mL_list = []
mG_list = []

for t_req, tL, tG in zip(df_phys["t_required_Gyr"], df_phys["t_LCDM_Gyr"], df_phys["t_Logosfield_Gyr"]):
    fL,fG,mL,mG = assess_row(t_req, tL, tG)
    feas_L.append(fL)
    feas_G.append(fG)
    mL_list.append(mL)
    mG_list.append(mG)

df_phys["feasible_LCDM"]     = feas_L
df_phys["feasible_Logos"]    = feas_G
df_phys["margin_LCDM_Gyr"]   = mL_list
df_phys["margin_Logos_Gyr"]  = mG_list

# significance: how often we flip "impossible → possible"
def paired_sig(df_eval):
    sub = df_eval.dropna(subset=["feasible_LCDM","feasible_Logos"])
    lcdm_ok  = sub["feasible_LCDM"].astype(bool).values
    logos_ok = sub["feasible_Logos"].astype(bool).values

    rescued = np.logical_and(~lcdm_ok, logos_ok)
    worse   = np.logical_and(lcdm_ok, ~logos_ok)

    n_rescued = int(rescued.sum())
    n_worse   = int(worse.sum())

    N_pairs = n_rescued + n_worse
    if N_pairs == 0:
        Z = 0.0
    else:
        Z = (n_rescued - n_worse)/max(np.sqrt(N_pairs),1e-9)

    return {
        "N_used":       int(sub.shape[0]),
        "rescued":      n_rescued,
        "made_worse":   n_worse,
        "flip_pairs":   N_pairs,
        "Z_binom_like": float(Z),
        "meaning": (
            "rescued = infeasible in strict LCDM (t_LCDM_Gyr < t_required_Gyr) "
            "but feasible with Logosfield time (t_Logosfield_Gyr >= t_required_Gyr). "
            "Z_binom_like ~ (rescued - worse)/sqrt(rescued + worse)."
        )
    }

siginfo = paired_sig(df_phys)

mask_valid = df_phys[["feasible_LCDM","feasible_Logos"]].dropna()
N_tot = mask_valid.shape[0]
N_LCDM_ok  = int((mask_valid["feasible_LCDM"]  == True).sum())
N_Logos_ok = int((mask_valid["feasible_Logos"] == True).sum())

frac_LCDM  = N_LCDM_ok  / max(N_tot,1)
frac_Logos = N_Logos_ok / max(N_tot,1)

summary = {
    "N_objects_used":     int(N_tot),
    "N_feasible_LCDM":    N_LCDM_ok,
    "N_feasible_Logos":   N_Logos_ok,
    "frac_feasible_LCDM": frac_LCDM,
    "frac_feasible_Logos":frac_Logos,
    "paired_flip_test":   siginfo,
    "interpretation": (
        "If Logosfield time (t_Logosfield_Gyr) consistently turns infeasible BHs into feasible "
        "ones while ΛCDM time (t_LCDM_Gyr) fails, that's direct evidence this SAME scalar "
        "field that explains spins/κ also solves the high-z SMBH timing tension."
    )
}

print("\n=== SMBH TIMING SUMMARY (STRICT ΛCDM VS LOGOSFIELD) ===")
print(json.dumps(summary, indent=2))

# simple bar plot
plt.figure(figsize=(4,4))
plt.bar([0,1],[frac_LCDM, frac_Logos],
        tick_label=["ΛCDM","Logosfield"],
        alpha=0.7, color=["#c0802e","#2e6cc0"])
plt.ylabel("Fraction feasible (t_available ≥ t_required)")
plt.title("High-z SMBH growth feasibility")
plt.ylim(0,1)
plt.grid(alpha=0.3, axis="y")
plot_path = os.path.join(OUTDIR, f"bh_feasibility_STRICT_{stamp()}.png")
plt.tight_layout()
plt.savefig(plot_path, dpi=140)
plt.close()

tbl_path  = os.path.join(OUTDIR, f"bh_eval_STRICT_{stamp()}.csv")
json_path = os.path.join(OUTDIR, f"bh_summary_STRICT_{stamp()}.json")
zip_path  = os.path.join(OUTDIR, f"bh_quasar_STRICT_{stamp()}.zip")

df_phys.to_csv(tbl_path, index=False)
with open(json_path,"w") as f:
    json.dump(summary, f, indent=2)

with zipfile.ZipFile(zip_path,"w",zipfile.ZIP_DEFLATED) as z:
    z.write(tbl_path,  os.path.basename(tbl_path))
    z.write(json_path, os.path.basename(json_path))
    z.write(plot_path, os.path.basename(plot_path))

print("\nSaved:")
print(" ", tbl_path)
print(" ", json_path)
print(" ", plot_path)
print(" ", zip_path)

