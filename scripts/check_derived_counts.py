#!/usr/bin/env python3
"""Cross-check machine-readable research status against derived result files."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
STATUS = ROOT / "results" / "derived" / "research-status.yaml"
STRICT_FILES = {
    "standard_compute": ROOT / "results" / "derived" / "standard-compute-strict.yaml",
    "database_node": ROOT / "results" / "derived" / "database-node-strict.yaml",
    "managed_kubernetes": ROOT / "results" / "derived" / "managed-kubernetes-strict.yaml",
}
QUEUE = ROOT / "results" / "benchmark" / "queue.yaml"


def load(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)
    escaped = message.replace("%", "%25").replace("\r", "%0D").replace("\n", "%0A")
    print(f"::error title=Derived count mismatch::{escaped}")


def main() -> int:
    errors: list[str] = []
    status = load(STATUS)
    counts = status.get("counts", {}) if isinstance(status, dict) else {}
    declared_strict = counts.get("strict_clear_passes", {}) if isinstance(counts, dict) else {}

    actual: dict[str, int] = {}
    for key, path in STRICT_FILES.items():
        data = load(path)
        clear_pass = data.get("clear_pass", []) if isinstance(data, dict) else []
        if clear_pass is None:
            clear_pass = []
        if not isinstance(clear_pass, list):
            fail(f"{path.relative_to(ROOT)} clear_pass must be a list", errors)
            continue
        actual[key] = len(clear_pass)
        if declared_strict.get(key) != len(clear_pass):
            fail(
                f"research-status strict_clear_passes.{key}={declared_strict.get(key)!r} "
                f"but {path.relative_to(ROOT)} contains {len(clear_pass)} clear pass(es)",
                errors,
            )

    queue = load(QUEUE)
    ready = queue.get("ready", []) if isinstance(queue, dict) else []
    if ready is None:
        ready = []
    if not isinstance(ready, list):
        fail(f"{QUEUE.relative_to(ROOT)} ready must be a list", errors)
    else:
        declared_ready = counts.get("validation_ready_resources") if isinstance(counts, dict) else None
        if declared_ready != len(ready):
            fail(
                f"research-status validation_ready_resources={declared_ready!r} "
                f"but {QUEUE.relative_to(ROOT)} contains {len(ready)} ready resource(s)",
                errors,
            )

    if errors:
        print(f"Derived count validation failed with {len(errors)} error(s).", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "Derived count validation passed: "
        f"standard={actual.get('standard_compute', 0)}, "
        f"database={actual.get('database_node', 0)}, "
        f"managed-kubernetes={actual.get('managed_kubernetes', 0)}, "
        f"ready={len(ready)}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
