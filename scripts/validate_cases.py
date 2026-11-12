#!/usr/bin/env python3
"""Validate contributed JSONL benchmark cases. This validates data shape, not detector performance."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schemas" / "attack-case.schema.json"
CASE_ROOT = ROOT / "data" / "cases"


def main() -> int:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: unable to read case schema: {exc}", file=sys.stderr)
        return 2

    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    files = sorted(CASE_ROOT.rglob("*.jsonl")) if CASE_ROOT.exists() else []
    if not files:
        print("INFO: no JSONL case files yet; schema loaded successfully. No benchmark performance is implied.")
        return 0

    errors: list[str] = []
    records = 0
    for path in files:
        for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if not raw.strip() or raw.lstrip().startswith("#"):
                continue
            records += 1
            try:
                record = json.loads(raw)
            except json.JSONDecodeError as exc:
                errors.append(f"{path.relative_to(ROOT)}:{line_no}: invalid JSON: {exc}")
                continue
            for error in validator.iter_errors(record):
                location = ".".join(str(part) for part in error.absolute_path) or "<root>"
                errors.append(f"{path.relative_to(ROOT)}:{line_no}:{location}: {error.message}")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        print(f"FAILED: {len(errors)} validation error(s) across {records} record(s).", file=sys.stderr)
        return 1

    print(f"PASS: {records} benchmark case record(s) validated across {len(files)} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
