#!/usr/bin/env python3
"""Initialize a fresh BRIDGE project overlay.

Standard-library only. Refuses to write into a non-empty destination.
Role defaults reproduce BRIDGE's reference casting but may be replaced explicitly.
"""
from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("destination", help="New or empty destination directory")
    parser.add_argument("--project-id", default="NEW-PROJECT")
    parser.add_argument("--owner", default="Karma")
    parser.add_argument("--architect", default="Hex")
    parser.add_argument("--primary-builder", default="Codex")
    parser.add_argument("--standin-builder", default="Claude Code")
    parser.add_argument("--verifier", default="Fable")
    args = parser.parse_args()

    source = Path(__file__).resolve().parents[1] / "project-template"
    dest = Path(args.destination).expanduser().resolve()

    if not source.is_dir():
        raise SystemExit(f"project template missing: {source}")

    if dest.exists() and any(dest.iterdir()):
        raise SystemExit(f"refusing non-empty destination: {dest}")
    dest.mkdir(parents=True, exist_ok=True)

    replacements = {
        "<PROJECT-ID>": args.project_id,
        "<OWNER>": args.owner,
        "<ARCHITECT>": args.architect,
        "<PRIMARY-BUILDER>": args.primary_builder,
        "<STANDIN-BUILDER>": args.standin_builder,
        "<VERIFIER>": args.verifier,
    }

    for path in source.rglob("*"):
        rel = path.relative_to(source)
        target = dest / rel
        if path.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            continue
        text = path.read_text(encoding="utf-8")
        for old, new in replacements.items():
            text = text.replace(old, new)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8", newline="\n")

    print(f"Initialized BRIDGE project overlay at: {dest}")
    print(f"Project ID: {args.project_id}")
    print(f"Owner: {args.owner}")
    print(f"Architect: {args.architect}")
    print(f"Primary Builder: {args.primary_builder}")
    print(f"Stand-in Builder: {args.standin_builder}")
    print(f"Verifier: {args.verifier}")
    print("Next: complete PROJECT_CHARTER.md, then perform the Architect comprehension handshake.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
