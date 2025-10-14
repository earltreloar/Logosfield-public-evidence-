# Logosfield Replications (public)

This folder invites *independent* reruns of the public bundles (Mechanisms 1–3, 14; CDDR; SMBH).
It provides:
- **Blinded subsets** (rotations / masked views) to reduce confirmation bias
- **Hash manifest** (`hashes.json`) for integrity checks of each ZIP/CSV
- A **one-cell Colab** snippet to reproduce Mechanism 1 externally
- A **report template** to standardize replication summaries

---

## Quickstart (Mechanism 1 • Spins)

**Option A — Colab (one cell)**  
Open a fresh Colab notebook and run:

```python
# 1) Pull release assets (edit the tag/version if needed)
!mkdir -p /content/m1 && cd /content/m1
!wget -q -O Mechanism1_Spins_Repro_v1.1.zip \
  https://github.com/earltreloar/Logosfield-public-evidence-/releases/download/v1.0.0/Mechanism1_Spins_Repro_v1.1.zip
!wget -q -O mechanism1_all_surveys_alignment_vs_z_3.1.1.csv \
  https://github.com/earltreloar/Logosfield-public-evidence-/releases/download/v1.0.0/mechanism1_all_surveys_alignment_vs_z_3.1.1.csv

# 2) Verify file integrity (compare to replications/hashes.json)
import hashlib, json, pathlib, textwrap, os, sys
m = json.loads(open('/content/hashes.json').read()) if os.path.exists('/content/hashes.json') else None
def sha256(p): 
    h=hashlib.sha256(); 
    h.update(open(p,'rb').read()); 
    return h.hexdigest()
for p in ["Mechanism1_Spins_Repro_v1.1.zip","mechanism1_all_surveys_alignment_vs_z_3.1.1.csv"]:
    print(p, sha256(p))

# 3) Unzip and run the included notebook/script
!python - <<'PY'
import zipfile, os, glob, subprocess
z="Mechanism1_Spins_Repro_v1.1.zip"
with zipfile.ZipFile(z) as Z: Z.extractall("/content/m1_run")
os.chdir("/content/m1_run")
print("Contents:", glob.glob("*"))
# If a runner script is shipped:
if os.path.exists("run.py"):
    subprocess.check_call(["python","run.py"])
else:
    print("Open the .ipynb notebook here and run all cells.")
PY
