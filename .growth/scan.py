#!/usr/bin/env python3
"""
BrainWire Growth Scanner — Automated health & gap detection
Scans: unimplemented modalities, missing safety protocols, untested stimulation
       parameters, documentation gaps
Output: JSON report to stdout + growth_bus.jsonl
"""

import json
import os
import re
import sys
import time
from pathlib import Path
from datetime import datetime, timezone

BW_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = BW_ROOT / "docs"
ENGINE_DIR = BW_ROOT / "brainwire" / "engine"
HARDWARE_DIR = BW_ROOT / "brainwire" / "hardware"
PROFILES_DIR = BW_ROOT / "brainwire" / "profiles"
TESTS_DIR = BW_ROOT / "tests"
GROWTH_STATE = BW_ROOT / ".growth" / "growth_state.json"
GROWTH_BUS = Path.home() / "Dev" / "nexus6" / "shared" / "growth_bus.jsonl"

# 12 stimulation modalities expected in BrainWire
EXPECTED_MODALITIES = [
    "tDCS", "tACS", "tRNS", "TMS", "tFUS",
    "PBM", "tVNS", "CES", "binaural",
    "neurofeedback", "pharmacological", "thermal",
]

# Safety-critical files/patterns
SAFETY_PATTERNS = [
    "safety", "protocol", "limit", "threshold",
    "contraindication", "emergency", "abort",
]


def scan_modalities():
    """Check which modalities are implemented vs documented."""
    result = {
        "expected": len(EXPECTED_MODALITIES),
        "implemented": [],
        "documented_only": [],
        "missing": [],
    }

    # Search source code for modality references
    code_content = ""
    for py_file in BW_ROOT.joinpath("brainwire").rglob("*.py"):
        try:
            code_content += py_file.read_text(errors="replace") + "\n"
        except OSError:
            pass

    # Search docs for modality references
    doc_content = ""
    if DOCS_DIR.exists():
        for md_file in DOCS_DIR.rglob("*.md"):
            try:
                doc_content += md_file.read_text(errors="replace") + "\n"
            except OSError:
                pass

    for mod in EXPECTED_MODALITIES:
        in_code = mod.lower() in code_content.lower()
        in_docs = mod.lower() in doc_content.lower()

        if in_code:
            result["implemented"].append(mod)
        elif in_docs:
            result["documented_only"].append(mod)
        else:
            result["missing"].append(mod)

    return result


def scan_safety():
    """Check safety protocol coverage."""
    result = {
        "safety_files": [],
        "has_emergency_stop": False,
        "has_current_limits": False,
        "has_contraindications": False,
        "missing_protocols": [],
    }

    # Find safety-related files
    for f in BW_ROOT.rglob("*safety*"):
        if f.is_file():
            result["safety_files"].append(str(f.relative_to(BW_ROOT)))

    # Check hardware safety module
    safety_py = HARDWARE_DIR / "safety.py"
    if safety_py.exists():
        content = safety_py.read_text(errors="replace")
        result["has_emergency_stop"] = "emergency" in content.lower() or "abort" in content.lower() or "stop" in content.lower()
        result["has_current_limits"] = "limit" in content.lower() or "max_current" in content.lower() or "threshold" in content.lower()
        result["has_contraindications"] = "contraindic" in content.lower()

    # Check for protocol files
    required_protocols = [
        "experiment-protocol",
        "safety",
        "emergency",
    ]
    existing_docs = set()
    if DOCS_DIR.exists():
        existing_docs = {f.stem.lower() for f in DOCS_DIR.glob("*.md")}

    for proto in required_protocols:
        if not any(proto in d for d in existing_docs):
            result["missing_protocols"].append(proto)

    return result


def scan_parameters():
    """Check stimulation parameter coverage and testing."""
    result = {
        "parameter_files": 0,
        "tested_configs": 0,
        "untested_params": [],
        "profiles_count": 0,
    }

    # Count hardware config files
    if HARDWARE_DIR.exists():
        configs_py = HARDWARE_DIR / "configs.py"
        if configs_py.exists():
            result["parameter_files"] += 1
            content = configs_py.read_text(errors="replace")
            # Count class/dict definitions as parameter sets
            result["tested_configs"] = len(re.findall(r"class\s+\w+|=\s*\{", content))

    # Count profiles
    if PROFILES_DIR.exists():
        result["profiles_count"] = sum(
            1 for f in PROFILES_DIR.rglob("*") if f.is_file() and f.suffix in (".py", ".json", ".toml")
        )

    # Check test coverage
    if TESTS_DIR.exists():
        test_files = list(TESTS_DIR.rglob("test_*.py"))
        tested_modules = set()
        for tf in test_files:
            tested_modules.add(tf.stem.replace("test_", ""))

        # Check which brainwire modules lack tests
        bw_dir = BW_ROOT / "brainwire"
        if bw_dir.exists():
            for py in bw_dir.rglob("*.py"):
                if py.name.startswith("_"):
                    continue
                mod_name = py.stem
                if mod_name not in tested_modules and mod_name != "__init__":
                    result["untested_params"].append(mod_name)

    return result


def scan_documentation():
    """Check documentation completeness."""
    result = {
        "total_docs": 0,
        "doc_files": [],
        "missing_topics": [],
        "stale_docs": [],
    }

    expected_topics = [
        "hardware-architecture",
        "experiment-protocol",
        "safety",
        "consciousness-states",
        "bci-bridge",
    ]

    if DOCS_DIR.exists():
        for f in DOCS_DIR.glob("*.md"):
            result["total_docs"] += 1
            result["doc_files"].append(f.name)

    existing_stems = {Path(d).stem.lower() for d in result["doc_files"]}
    for topic in expected_topics:
        if not any(topic in s for s in existing_stems):
            result["missing_topics"].append(topic)

    # Check for stale docs (>60 days)
    cutoff = time.time() - 60 * 86400
    if DOCS_DIR.exists():
        for f in DOCS_DIR.glob("*.md"):
            if f.stat().st_mtime < cutoff:
                result["stale_docs"].append(f.name)

    return result


def scan_cdo_violations():
    """Check CDO compliance."""
    result = {
        "json_without_meta": [],
    }

    for json_file in BW_ROOT.rglob("*.json"):
        if ".growth" in str(json_file) or "node_modules" in str(json_file):
            continue
        if json_file.name.startswith("."):
            continue
        try:
            data = json.loads(json_file.read_text(errors="replace"))
            if isinstance(data, dict) and "_meta" not in data and json_file.stat().st_size > 100:
                result["json_without_meta"].append(
                    str(json_file.relative_to(BW_ROOT))
                )
        except (json.JSONDecodeError, OSError):
            pass

    return result


def emit_bus(report):
    """Write summary to growth_bus.jsonl for cross-repo coordination."""
    entry = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "repo": "brainwire",
        "type": "growth_scan",
        "modalities_implemented": len(report["modalities"]["implemented"]),
        "modalities_missing": len(report["modalities"]["missing"]),
        "safety_files": len(report["safety"]["safety_files"]),
        "untested_modules": len(report["parameters"]["untested_params"]),
        "doc_count": report["documentation"]["total_docs"],
        "cdo_violations": len(report["cdo"]["json_without_meta"]),
    }
    try:
        GROWTH_BUS.parent.mkdir(parents=True, exist_ok=True)
        with open(GROWTH_BUS, "a") as f:
            f.write(json.dumps(entry) + "\n")
    except OSError as e:
        print(f"WARN: Could not write to growth_bus: {e}", file=sys.stderr)


def main():
    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "repo": "brainwire",
        "modalities": scan_modalities(),
        "safety": scan_safety(),
        "parameters": scan_parameters(),
        "documentation": scan_documentation(),
        "cdo": scan_cdo_violations(),
    }

    # Compute health score (0-100)
    mod = report["modalities"]
    mod_pct = len(mod["implemented"]) / max(1, mod["expected"]) * 100
    safety_score = 25 * (
        int(report["safety"]["has_emergency_stop"])
        + int(report["safety"]["has_current_limits"])
        + int(report["safety"]["has_contraindications"])
        + int(len(report["safety"]["missing_protocols"]) == 0)
    )
    doc_penalty = min(15, len(report["documentation"]["missing_topics"]) * 5)
    cdo_penalty = min(10, len(report["cdo"]["json_without_meta"]) * 2)
    health = max(0, min(100, int(mod_pct * 0.4 + safety_score * 0.4 - doc_penalty - cdo_penalty)))

    report["health_score"] = health
    report["summary"] = {
        "modality_coverage_pct": round(mod_pct, 1),
        "modalities_missing": mod["missing"],
        "safety_score": safety_score,
        "untested_module_count": len(report["parameters"]["untested_params"]),
        "missing_doc_topics": report["documentation"]["missing_topics"],
        "cdo_violation_count": len(report["cdo"]["json_without_meta"]),
    }

    emit_bus(report)

    # Update growth state
    try:
        state = json.loads(GROWTH_STATE.read_text()) if GROWTH_STATE.exists() else {}
    except (json.JSONDecodeError, OSError):
        state = {}
    state["last_scan"] = report["timestamp"]
    state["last_health"] = health
    state["scan_count"] = state.get("scan_count", 0) + 1
    GROWTH_STATE.parent.mkdir(parents=True, exist_ok=True)
    GROWTH_STATE.write_text(json.dumps(state, indent=2) + "\n")

    if "--quiet" in sys.argv:
        print(json.dumps(report["summary"], indent=2))
    else:
        print(json.dumps(report, indent=2))

    return 0 if health >= 50 else 1


if __name__ == "__main__":
    sys.exit(main())
