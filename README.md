# DoRaptim downloads

Official downloads of DoRaptim, a download manager for your browser by Tenkuryu Code. This repository only hosts the releases; the source code is private.

> **Pre-alpha.** DoRaptim is early software. Do not rely on it for downloads that must not fail.

## Install

1. Download the installer for your computer from [Releases](../../releases):
   - **Windows (64-bit):** `doraptim-<version>-windows-x86_64-setup.exe`
   - **macOS, Apple Silicon (M1 or later):** `doraptim-<version>-macos-arm64.pkg`
   - **macOS, Intel:** `doraptim-<version>-macos-x86_64.pkg`
2. Run it. It installs the DoRaptim engine for your user account and connects it to the DoRaptim browser extension.
3. Install the DoRaptim extension for Chrome.

The `.tar.gz` and `.zip` archives contain only the engine program, for developers.

### The builds are not code-signed yet

- **Windows** shows "Windows protected your PC". Choose *More info*, then *Run anyway*.
- **macOS** says the package cannot be checked. Open *System Settings*, *Privacy & Security*, and choose *Open Anyway*.

Only do this for files downloaded from this repository's Releases page.

## Check a download

Each release has a `SHA256SUMS` file. In the folder with your download:

```sh
sha256sum --check --ignore-missing SHA256SUMS          # Linux, or Windows with Git Bash
shasum -a 256 --check --ignore-missing SHA256SUMS      # macOS
```

## Privacy

DoRaptim has no account, telemetry, analytics, or cloud service. See [PRIVACY.md](PRIVACY.md).

## Security

Report a vulnerability privately with this repository's *Security* tab, *Report a vulnerability*. Do not open a public issue.

## Terms

By installing or using DoRaptim you accept the [terms of use](TERMS-OF-USE.md) ([Bahasa Indonesia](TERMS-OF-USE.id.md); the Indonesian version prevails if the two differ). In short: DoRaptim is free for personal use and internal use in your organization; you may not sell or redistribute the builds, and it comes without warranty.

Copyright (c) 2026 Tenkuryu Code. All rights reserved. The DoRaptim name and logo belong to Tenkuryu Code.
