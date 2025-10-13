#!/usr/bin/env python3
import os, json, hashlib, yaml, sys, time, platform, subprocess
from pathlib import Path

PREREG = os.environ.get("PREREG", sys.argv[sys.argv.index("--prereg")+1] if "--prereg" in sys.argv else None)
if not PREREG or not Path(PREREG).exists():
    print("ERROR: Provide --prereg /path/to/prereg.yaml or set PREREG env var, and ensure the file exists.")
    sys.exit(2)

Path("logs").mkdir(exist_ok=True)
meta = {
    "python": platform.python_version(),
    "platform": platform.platform(),
    "pip_freeze": subprocess.check_output([sys.executable, "-m", "pip", "freeze"]).decode().splitlines()
}
with open("logs/execution.json", "w") as f: json.dump(meta, f, indent=2)

with open(PREREG, "rb") as f:
    prereg_bytes = f.read()
    prereg_sha = hashlib.sha256(prereg_bytes).hexdigest()
    prereg = yaml.safe_load(prereg_bytes.decode("utf-8"))

Path("meta").mkdir(exist_ok=True)
with open("meta/prereg.yaml", "wb") as f: f.write(prereg_bytes)

# Hash inputs if present locally
inputs = {}
for k,v in (prereg.get("inputs", {}) or {}).items():
    p = (v or "").split("#")[0]
    if p and Path(p).exists():
        inputs[k] = {"path": p, "sha256": hashlib.sha256(Path(p).read_bytes()).hexdigest()}
with open("meta/inputs.json", "w") as f: json.dump(inputs, f, indent=2)

# Stub: Emit a minimal results bundle to prove execution wiring.
Path("results").mkdir(exist_ok=True)
with open("results/placeholder_results.json", "w") as f:
    json.dump({"status": "ok", "mechanism_or_module": prereg.get("mechanism", prereg.get("module", "unknown")),
               "run_date": prereg.get("run_date"), "note": "Replace this stub with your real analysis runner."}, f, indent=2)

print("Runner completed (stub). See results/placeholder_results.json and meta/*.")
