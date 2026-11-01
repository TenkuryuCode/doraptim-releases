#!/usr/bin/env python3
"""Point the README's download links at one release.

Usage: latest-links.py VERSION [README]

Rewrites the block between `<!-- latest-downloads:start -->` and `<!-- latest-downloads:end -->`
with direct links to that release's files. GitHub's `releases/latest` skips pre-releases and the
file names carry the version, so the links name the release itself. Run by the package
manifests workflow when a release is published.
"""

import re
import sys

REPOSITORY = "https://github.com/TenkuryuCode/doraptim-releases"
START = "<!-- latest-downloads:start -->"
END = "<!-- latest-downloads:end -->"


def block(version: str) -> str:
    base = f"{REPOSITORY}/releases/download/v{version}"
    rows = [
        ("Chrome extension", f"doraptim-extension-{version}-chrome.zip"),
        ("Windows (64-bit) installer", f"doraptim-{version}-windows-x86_64-setup.exe"),
        ("macOS installer, Apple Silicon (M1 or later)", f"doraptim-{version}-macos-arm64.pkg"),
        ("macOS installer, Intel", f"doraptim-{version}-macos-x86_64.pkg"),
    ]
    lines = [
        START,
        f"**Latest version: {version}** ([release notes]({REPOSITORY}/releases/tag/v{version}))",
        "",
        "| Download | File |",
        "|---|---|",
    ]
    lines += [f"| {label} | [{name}]({base}/{name}) |" for label, name in rows]
    lines += [
        "",
        f"Check the files with [SHA256SUMS]({base}/SHA256SUMS). Every release, including older ones, is on the [Releases]({REPOSITORY}/releases) page.",
        END,
    ]
    return "\n".join(lines)


def main() -> int:
    if len(sys.argv) not in (2, 3):
        print(__doc__.strip().splitlines()[2], file=sys.stderr)
        return 2
    version = sys.argv[1].removeprefix("v")
    if not re.fullmatch(r"\d+\.\d+\.\d+(-[0-9A-Za-z.]+)?", version):
        print(f"not a version: {version}", file=sys.stderr)
        return 2
    path = sys.argv[2] if len(sys.argv) == 3 else "README.md"
    with open(path, encoding="utf-8") as f:
        text = f.read()
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
    if not pattern.search(text):
        print(f"{path} has no {START} ... {END} block", file=sys.stderr)
        return 1
    updated = pattern.sub(lambda _: block(version), text, count=1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(updated)
    return 0


if __name__ == "__main__":
    sys.exit(main())
