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
  #!/usr/bin/env python3
import os, json, hashlib, sys, time, platform, subprocess
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: Missing pyyaml. Try: pip install pyyaml")
    sys.exit(2)

def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

def find_latest_prereg(mech: str) -> Path:
    root = Path("prereg") / str(mech)
    if not root.exists():
        raise FileNotFoundError(f"prereg folder not found for mechanism {mech}: {root}")
    candidates = sorted(root.rglob("prereg.yaml"))
    if not candidates:
        raise FileNotFoundError(f"No prereg.yaml found under {root}")
    return candidates[-1]

def run_cmd(cmd, cwd=None):
    print("RUN:", " ".join(cmd))
    subprocess.check_call(cmd, cwd=cwd)

def main():
    # Args
    prereg_path = None
    mech = None
    if "--prereg" in sys.argv:
        prereg_path = sys.argv[sys.argv.index("--prereg") + 1]
    if "--mechanism" in sys.argv:
        mech = sys.argv[sys.argv.index("--mechanism") + 1]

    if prereg_path is None and mech is None:
        print("ERROR: Provide --prereg /path/to/prereg.yaml OR --mechanism N")
        sys.exit(2)

    if prereg_path is None:
        prereg_file = find_latest_prereg(mech)
    else:
        prereg_file = Path(prereg_path)

    if not prereg_file.exists():
        print(f"ERROR: prereg file not found: {prereg_file}")
        sys.exit(2)

    Path("logs").mkdir(exist_ok=True)
    Path("meta").mkdir(exist_ok=True)
    Path("results").mkdir(exist_ok=True)

    # Environment meta
    meta = {
        "timestamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "python": platform.python_version(),
        "platform": platform.platform(),
    }
    try:
        meta["pip_freeze"] = subprocess.check_output([sys.executable, "-m", "pip", "freeze"]).decode().splitlines()
    except Exception:
        meta["pip_freeze"] = ["<pip_freeze_failed>"]

    (Path("meta") / "execution.json").write_text(json.dumps(meta, indent=2))

    # Hash prereg
    prereg_bytes = prereg_file.read_bytes()
    prereg_sha = hashlib.sha256(prereg_bytes).hexdigest()
    (Path("meta") / "prereg.sha256").write_text(prereg_sha + "\n")
    (Path("meta") / "prereg.yaml").write_bytes(prereg_bytes)

    prereg = yaml.safe_load(prereg_bytes.decode("utf-8"))
    mech_id = str(prereg.get("mechanism", mech if mech is not None else "unknown"))

    # Hash inputs if present locally
    inputs = {}
    for k, v in (prereg.get("inputs", {}) or {}).items():
        p = (v or "").split("#")[0]
        if p and Path(p).exists():
            inputs[k] = {"path": p, "sha256": sha256_file(Path(p))}
    (Path("meta") / "inputs.json").write_text(json.dumps(inputs, indent=2))

    # Dispatch policy:
    # Prefer a per-mechanism script if it exists, else fail with clear guidance.
    mech_script_candidates = [
        Path(f"Mechanism{mech_id}") / "run.py",
        Path(f"Mechanism{mech_id}") / "test.py",
        Path(f"Mechanism{mech_id}") / "runner.py",
    ]

    for candidate in mech_script_candidates:
        if candidate.exists():
            run_cmd([sys.executable, str(candidate), "--prereg", str(prereg_file)])
            print("OK: completed via", candidate)
            return

    # As fallback, allow Makefile targets if you define them
    # e.g., make mech14 PREREG=...
    make_target = f"mech{mech_id}"
    try:
        run_cmd(["make", make_target, f"PREREG={prereg_file}"])
        print("OK: completed via make target", make_target)
        return
    except Exception:
        pass

    raise RuntimeError(
        f"No runnable entrypoint found for Mechanism{mech_id}. "
        f"Add Mechanism{mech_id}/run.py (preferred) or define make target {make_target}."
    )

if __name__ == "__main__":
    main()
