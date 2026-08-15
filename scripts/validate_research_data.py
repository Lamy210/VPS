#!/usr/bin/env python3
"""Validate research YAML structure and cross-file consistency.

This intentionally validates repository invariants rather than provider truth.
Provider facts are verified through the research workflow and official sources;
this script prevents bookkeeping and schema drift from corrupting that work.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
VERIFIED = ROOT / "results" / "verified"
DERIVED = ROOT / "results" / "derived"
BENCHMARK = ROOT / "results" / "benchmark" / "queue.yaml"
STATUS = DERIVED / "research-status.yaml"


class UniqueKeyLoader(yaml.SafeLoader):
    """SafeLoader that rejects duplicate YAML mapping keys."""


def _construct_mapping(loader: UniqueKeyLoader, node: yaml.MappingNode, deep: bool = False) -> dict[Any, Any]:
    mapping: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                f"found duplicate key: {key!r}",
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_mapping,
)


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.load(handle, Loader=UniqueKeyLoader)


def normalize_name(value: str) -> str:
    """Normalize display-name differences without asserting corporate identity."""
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def validate_batch(path: Path, errors: list[str]) -> list[str]:
    try:
        data = load_yaml(path)
    except Exception as exc:  # noqa: BLE001 - report parser context cleanly
        errors.append(f"{path.relative_to(ROOT)}: YAML parse error: {exc}")
        return []

    require(isinstance(data, dict), f"{path.relative_to(ROOT)}: top level must be a mapping", errors)
    if not isinstance(data, dict):
        return []

    require(data.get("schema_version") == 1, f"{path.relative_to(ROOT)}: schema_version must be 1", errors)
    require(bool(data.get("verified_at")), f"{path.relative_to(ROOT)}: verified_at is required", errors)
    require(bool(data.get("source_policy")), f"{path.relative_to(ROOT)}: source_policy is required", errors)

    providers = data.get("providers")
    require(isinstance(providers, list), f"{path.relative_to(ROOT)}: providers must be a list", errors)
    if not isinstance(providers, list):
        return []

    names: list[str] = []
    for index, provider in enumerate(providers):
        prefix = f"{path.relative_to(ROOT)}: providers[{index}]"
        require(isinstance(provider, dict), f"{prefix} must be a mapping", errors)
        if not isinstance(provider, dict):
            continue

        name = provider.get("canonical_name")
        require(isinstance(name, str) and bool(name.strip()), f"{prefix}.canonical_name is required", errors)
        if isinstance(name, str) and name.strip():
            names.append(name.strip())

        confidence = provider.get("confidence")
        if confidence is not None:
            require(confidence in {"A+", "A", "B", "C", "D"}, f"{prefix}.confidence has invalid value {confidence!r}", errors)

        sources = provider.get("sources")
        if sources is not None:
            require(isinstance(sources, list), f"{prefix}.sources must be a list", errors)
            if isinstance(sources, list):
                for source_index, source in enumerate(sources):
                    require(
                        isinstance(source, str) and source.startswith("https://"),
                        f"{prefix}.sources[{source_index}] must be an https URL",
                        errors,
                    )

    return names


def collect_batch_providers(errors: list[str]) -> tuple[dict[str, tuple[str, Path]], list[Path]]:
    batch_paths = sorted(VERIFIED.glob("batch-*.yaml"))
    require(bool(batch_paths), "No results/verified/batch-*.yaml files found", errors)

    providers: dict[str, tuple[str, Path]] = {}
    for path in batch_paths:
        for display_name in validate_batch(path, errors):
            key = normalize_name(display_name)
            if key in providers:
                previous_name, previous_path = providers[key]
                errors.append(
                    "Normalized canonical provider duplicate: "
                    f"{display_name!r} in {path.relative_to(ROOT)} conflicts with "
                    f"{previous_name!r} in {previous_path.relative_to(ROOT)}"
                )
            else:
                providers[key] = (display_name, path)
    return providers, batch_paths


def validate_followups(provider_keys: set[str], errors: list[str]) -> list[Path]:
    paths = sorted(VERIFIED.glob("followup-*.yaml"))
    for path in paths:
        try:
            data = load_yaml(path)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{path.relative_to(ROOT)}: YAML parse error: {exc}")
            continue

        require(isinstance(data, dict), f"{path.relative_to(ROOT)}: top level must be a mapping", errors)
        if not isinstance(data, dict):
            continue
        require(data.get("schema_version") == 1, f"{path.relative_to(ROOT)}: schema_version must be 1", errors)
        providers = data.get("providers")
        require(isinstance(providers, list), f"{path.relative_to(ROOT)}: providers must be a list", errors)
        if not isinstance(providers, list):
            continue
        for index, provider in enumerate(providers):
            if not isinstance(provider, dict):
                errors.append(f"{path.relative_to(ROOT)}: providers[{index}] must be a mapping")
                continue
            name = provider.get("canonical_name")
            if not isinstance(name, str) or not name.strip():
                errors.append(f"{path.relative_to(ROOT)}: providers[{index}].canonical_name is required")
                continue
            require(
                normalize_name(name) in provider_keys,
                f"{path.relative_to(ROOT)}: follow-up references unknown provider {name!r}",
                errors,
            )
    return paths


def validate_derived_references(provider_keys: set[str], errors: list[str]) -> None:
    for path in sorted(DERIVED.glob("*-strict.yaml")):
        try:
            data = load_yaml(path)
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{path.relative_to(ROOT)}: YAML parse error: {exc}")
            continue
        if not isinstance(data, dict):
            errors.append(f"{path.relative_to(ROOT)}: top level must be a mapping")
            continue
        for section in ("clear_pass", "blocked_by_unknown", "clear_fail_examples"):
            entries = data.get(section, [])
            if entries is None:
                entries = []
            require(isinstance(entries, list), f"{path.relative_to(ROOT)}: {section} must be a list", errors)
            if not isinstance(entries, list):
                continue
            for index, entry in enumerate(entries):
                if not isinstance(entry, dict):
                    errors.append(f"{path.relative_to(ROOT)}: {section}[{index}] must be a mapping")
                    continue
                name = entry.get("provider")
                if isinstance(name, str):
                    require(
                        normalize_name(name) in provider_keys,
                        f"{path.relative_to(ROOT)}: {section}[{index}] references unknown provider {name!r}",
                        errors,
                    )


def validate_benchmark_references(provider_keys: set[str], errors: list[str]) -> None:
    if not BENCHMARK.exists():
        return
    try:
        data = load_yaml(BENCHMARK)
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{BENCHMARK.relative_to(ROOT)}: YAML parse error: {exc}")
        return
    if not isinstance(data, dict):
        errors.append(f"{BENCHMARK.relative_to(ROOT)}: top level must be a mapping")
        return
    for section in ("ready", "blocked"):
        entries = data.get(section, [])
        require(isinstance(entries, list), f"{BENCHMARK.relative_to(ROOT)}: {section} must be a list", errors)
        if not isinstance(entries, list):
            continue
        for index, entry in enumerate(entries):
            if not isinstance(entry, dict):
                errors.append(f"{BENCHMARK.relative_to(ROOT)}: {section}[{index}] must be a mapping")
                continue
            name = entry.get("provider")
            require(isinstance(name, str), f"{BENCHMARK.relative_to(ROOT)}: {section}[{index}].provider is required", errors)
            if isinstance(name, str):
                require(
                    normalize_name(name) in provider_keys,
                    f"{BENCHMARK.relative_to(ROOT)}: {section}[{index}] references unknown provider {name!r}",
                    errors,
                )


def validate_status(provider_count: int, batch_count: int, followup_count: int, errors: list[str]) -> None:
    if not STATUS.exists():
        errors.append(f"Missing {STATUS.relative_to(ROOT)}")
        return
    try:
        data = load_yaml(STATUS)
    except Exception as exc:  # noqa: BLE001
        errors.append(f"{STATUS.relative_to(ROOT)}: YAML parse error: {exc}")
        return
    if not isinstance(data, dict):
        errors.append(f"{STATUS.relative_to(ROOT)}: top level must be a mapping")
        return
    counts = data.get("counts")
    require(isinstance(counts, dict), f"{STATUS.relative_to(ROOT)}: counts must be a mapping", errors)
    if not isinstance(counts, dict):
        return
    require(counts.get("verification_batches") == batch_count, f"research-status verification_batches must equal {batch_count}", errors)
    require(counts.get("unique_verified_providers") == provider_count, f"research-status unique_verified_providers must equal {provider_count}", errors)
    require(counts.get("targeted_followup_files") == followup_count, f"research-status targeted_followup_files must equal {followup_count}", errors)


def main() -> int:
    errors: list[str] = []
    providers, batch_paths = collect_batch_providers(errors)
    provider_keys = set(providers)
    followup_paths = validate_followups(provider_keys, errors)
    validate_derived_references(provider_keys, errors)
    validate_benchmark_references(provider_keys, errors)
    validate_status(len(providers), len(batch_paths), len(followup_paths), errors)

    if errors:
        print(f"Research data validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        "Research data validation passed: "
        f"{len(batch_paths)} batches, {len(providers)} unique providers, "
        f"{len(followup_paths)} follow-up files."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
