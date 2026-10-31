# DoRaptim downloads

Official downloads of DoRaptim, a download manager for your browser by Tenkuryu Code. This repository only hosts the releases; the source code is private.

> **Pre-alpha.** DoRaptim is early software. Do not rely on it for downloads that must not fail.

## Install

1. Download the installer for your computer from [Releases](../../releases):
   - **Windows (64-bit):** `doraptim-<version>-windows-x86_64-setup.exe`
   - **macOS, Apple Silicon (M1 or later):** `doraptim-<version>-macos-arm64.pkg`
   - **macOS, Intel:** `doraptim-<version>-macos-x86_64.pkg`
2. Run it. It installs the DoRaptim engine for your user account and connects it to the DoRaptim browser extension.
3. Install the DoRaptim extension for Chrome, as described below.

The `.tar.gz` archives and the `doraptim-<version>-x86_64-pc-windows-msvc.zip` archive contain only the engine program, for developers.

### Install the Chrome extension (developer preview)

The extension is not in the Chrome Web Store yet. Until it is, each release includes it as `doraptim-extension-<version>-chrome.zip`, and you load it into Chrome yourself:

1. Download `doraptim-extension-<version>-chrome.zip` from the same release as the installer.
2. Unzip it into a folder you will keep, for example `Documents/DoRaptim extension`. Chrome loads the extension from that folder, so do not delete or move it.
3. Open `chrome://extensions` in Chrome.
4. Turn on **Developer mode** (top right).
5. Choose **Load unpacked** and select the unzipped folder (the one that contains `manifest.json`).
6. The extension's ID must be `omaocaakodbohegmpboammlafnagpnpd`. The installer connects the engine only to that ID.

Good to know:

- Chrome does not update this extension automatically. For a new release, unzip the new ZIP into the same folder (replacing the old files) and choose the reload button on the extension's card.
- Chrome may show a warning about developer-mode extensions when it starts. That is expected for a developer preview.
- Install it only from this repository's Releases page, and check the ID above.
- Some managed (work or school) browsers block developer-mode extensions.

### The builds are not code-signed yet

- **Windows** shows "Windows protected your PC". Choose *More info*, then *Run anyway*.
- **macOS** says the package cannot be checked. Open *System Settings*, *Privacy & Security*, and choose *Open Anyway*.

Only do this for files downloaded from this repository's Releases page.

## Update

To see whether a newer version is out, run `doraptim update` in a terminal (Command Prompt on Windows), or watch this repository's Releases. To update, install the new installer or package over the old one: it stops the running engine and replaces it. Then load the new extension ZIP from the same release (unzip it into the same folder and choose reload on the extension's card).

## Uninstall

**Windows:** open *Settings*, *Apps*, *Installed apps*, choose **DoRaptim**, and *Uninstall*.

**macOS:** open Terminal and run:

```sh
doraptim uninstall
```

It stops the engine, removes it from your browsers, and deletes its download queue, then shows the three `sudo` commands that remove the program itself. Your downloaded files are not touched. Add `--keep-data` to keep the queue.

Then remove the extension: open `chrome://extensions` and choose **Remove** on DoRaptim.

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
