#!/usr/bin/env python3
"""Copy FCScoreDocs help markdown into site/help for deployed FCScore clients.

Why this exists: deployed FCScore clients fetch
https://pyflightcoach.github.io/ScoringInfo/help/<name>.md, so these files must
keep being served at that exact path even though the documentation now lives in
FCScoreDocs. This script copies docs/help/*.md from an FCScoreDocs checkout into
site/help and rewrites the links that old clients cannot resolve:

  /fcsdocsbase -> https://pyflightcoach.github.io/FCScoreDocs
  /fcscorebase -> /fcscore

Old clients only replaced the first occurrence of each placeholder, so every
occurrence is replaced here. Both deployed old clients are served at /fcscore.

Files already in site/help with no source in FCScoreDocs are never deleted;
they are reported as warnings because deployed clients may still fetch them.

Usage:
  python3 scripts/sync_help.py [--docs ../FCScoreDocs]
  python3 scripts/sync_help.py --check   # exit 1 if site/help is out of date
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPLACEMENTS = (
    ("/fcsdocsbase", "https://pyflightcoach.github.io/FCScoreDocs"),
    ("/fcscorebase", "/fcscore"),
)

REPO = Path(__file__).resolve().parent.parent
SITE_HELP = REPO / "site" / "help"


def transform(text: str) -> str:
    for old, new in REPLACEMENTS:
        text = text.replace(old, new)
    return text


def desired_outputs(docs_help: Path) -> dict[str, str]:
    """Map output file name -> transformed content for every source help file."""
    return {
        src.name: transform(src.read_text(encoding="utf-8"))
        for src in sorted(docs_help.glob("*.md"))
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument(
        "--docs",
        type=Path,
        default=REPO.parent / "FCScoreDocs",
        help="FCScoreDocs checkout (default: ../FCScoreDocs)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="do not write; exit 1 if site/help differs from the sync output",
    )
    args = parser.parse_args(argv)

    docs_help = args.docs / "docs" / "help"
    if not docs_help.is_dir():
        print(f"error: {docs_help} not found; pass --docs <FCScoreDocs checkout>", file=sys.stderr)
        return 2

    outputs = desired_outputs(docs_help)
    if not outputs:
        print(f"error: no *.md files in {docs_help}", file=sys.stderr)
        return 2

    existing = {p.name: p for p in SITE_HELP.glob("*.md")} if SITE_HELP.is_dir() else {}
    stale = sorted(set(existing) - set(outputs))
    for name in stale:
        print(f"warning: site/help/{name} has no source in FCScoreDocs; kept (deployed clients may fetch it)")

    changed = []
    for name, content in outputs.items():
        target = SITE_HELP / name
        current = target.read_text(encoding="utf-8") if target.exists() else None
        if current != content:
            changed.append(name)

    if args.check:
        if changed:
            for name in changed:
                print(f"out of date: site/help/{name}")
            return 1
        print(f"site/help is up to date with {docs_help} ({len(outputs)} files)")
        return 0

    SITE_HELP.mkdir(parents=True, exist_ok=True)
    for name in changed:
        (SITE_HELP / name).write_text(outputs[name], encoding="utf-8", newline="\n")
        print(f"wrote site/help/{name}")
    print(f"synced {len(outputs)} files, {len(changed)} changed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
