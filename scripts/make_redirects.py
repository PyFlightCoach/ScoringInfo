#!/usr/bin/env python3
"""Generate the redirect pages for the retired ScoringInfo site.

ScoringInfo has been replaced by FCScoreDocs. Each old path gets a small
static page under site/ that redirects to the new location, so old links keep
working on GitHub Pages. Output is deterministic, so rerunning the script only
changes files whose mapping has changed.

Run from anywhere: python3 scripts/make_redirects.py
"""

from __future__ import annotations

import html
from pathlib import Path

NEW_BASE = "https://pyflightcoach.github.io/FCScoreDocs/"

# Old site path (no leading or trailing slash; "" is the root) -> new path under NEW_BASE.
REDIRECTS: dict[str, str] = {
    "": "process/",
    "elements": "process/segmentation/",
    "sequences": "process/sequence_definition/",
    "intra": "process/intra/",
    "inter": "process/inter/",
    "visibility": "process/visibility/",
    "positioning": "process/box/",
    "competition": "instructions/competitions/",
    "competition/cheat_sheet": "instructions/competitions/cheat_sheet/",
    "competition/example_1": "instructions/competitions/example_1/",
    "competition/example_2": "instructions/competitions/example_2/",
    "competition/example_3": "instructions/competitions/example_3/",
}

SITE = Path(__file__).resolve().parent.parent / "site"

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="0; url={target}">
<link rel="canonical" href="{target}">
<title>Moved to FCScore Documentation</title>
</head>
<body>
<p>This page has moved to <a href="{target}">{target}</a>.</p>
</body>
</html>
"""


def render(target: str) -> str:
    return PAGE.format(target=html.escape(target, quote=True))


def main() -> None:
    for old, new in REDIRECTS.items():
        target = NEW_BASE + new
        out = SITE / old / "index.html" if old else SITE / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(target), encoding="utf-8")
        print(f"wrote {out.relative_to(SITE.parent)} -> {target}")

    not_found = SITE / "404.html"
    not_found.write_text(render(NEW_BASE), encoding="utf-8")
    print(f"wrote {not_found.relative_to(SITE.parent)} -> {NEW_BASE}")


if __name__ == "__main__":
    main()
