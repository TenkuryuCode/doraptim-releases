# DoRaptim downloads

Official downloads of DoRaptim, a download manager for your browser by Tenkuryu Code. This repository only hosts the releases; the source code is private.

> **Pre-alpha.** DoRaptim is early software. Do not rely on it for downloads that must not fail.

## Download

<!-- latest-downloads:start -->
**Latest version: 0.1.0-alpha.2** ([release notes](https://github.com/TenkuryuCode/doraptim-releases/releases/tag/v0.1.0-alpha.2))

| Download | File |
|---|---|
| Chrome extension | [doraptim-extension-0.1.0-alpha.2-chrome.zip](https://github.com/TenkuryuCode/doraptim-releases/releases/download/v0.1.0-alpha.2/doraptim-extension-0.1.0-alpha.2-chrome.zip) |
| Windows (64-bit) installer | [doraptim-0.1.0-alpha.2-windows-x86_64-setup.exe](https://github.com/TenkuryuCode/doraptim-releases/releases/download/v0.1.0-alpha.2/doraptim-0.1.0-alpha.2-windows-x86_64-setup.exe) |
| macOS installer, Apple Silicon (M1 or later) | [doraptim-0.1.0-alpha.2-macos-arm64.pkg](https://github.com/TenkuryuCode/doraptim-releases/releases/download/v0.1.0-alpha.2/doraptim-0.1.0-alpha.2-macos-arm64.pkg) |
| macOS installer, Intel | [doraptim-0.1.0-alpha.2-macos-x86_64.pkg](https://github.com/TenkuryuCode/doraptim-releases/releases/download/v0.1.0-alpha.2/doraptim-0.1.0-alpha.2-macos-x86_64.pkg) |

Check the files with [SHA256SUMS](https://github.com/TenkuryuCode/doraptim-releases/releases/download/v0.1.0-alpha.2/SHA256SUMS). Every release, including older ones, is on the [Releases](https://github.com/TenkuryuCode/doraptim-releases/releases) page.
<!-- latest-downloads:end -->

## Install

DoRaptim has two parts: the **engine**, a small program on your computer that does the downloading, and the **Chrome extension**, which hands browser downloads to it. Install the engine in one of the two ways below, then the extension.

### Option 1: download the installer

1. Download the installer for your computer from [Releases](../../releases):
   - **Windows (64-bit):** `doraptim-<version>-windows-x86_64-setup.exe`
   - **macOS, Apple Silicon (M1 or later):** `doraptim-<version>-macos-arm64.pkg`
   - **macOS, Intel:** `doraptim-<version>-macos-x86_64.pkg`
2. Open it and follow the steps. It installs the engine for your user account and connects it to the browsers you have.

Nothing else is needed: no Homebrew, no developer tools.

### Option 2: install with Homebrew (macOS, or Linux on x86-64)

```sh
brew tap tenkuryucode/doraptim https://github.com/TenkuryuCode/doraptim-releases
brew trust tenkuryucode/doraptim
brew install doraptim
doraptim setup
```

- The `brew tap` and `brew trust` lines are needed once. Newer Homebrew versions only install from a tap you have trusted.
- `doraptim setup` connects the engine to your browsers. Run it again if you install another browser later.
- Homebrew needs up-to-date **Command Line Tools**. If it stops with *"Your Command Line Tools are too outdated"* (common right after a macOS upgrade), update them in *System Settings*, *General*, *Software Update*, or run `sudo rm -rf /Library/Developer/CommandLineTools` and then `sudo xcode-select --install`. Then run `brew install doraptim` again. Or use option 1, which does not need them.
- To update later: `brew update && brew upgrade doraptim`.

### On Windows, Scoop works too

```powershell
scoop bucket add doraptim https://github.com/TenkuryuCode/doraptim-releases
scoop install doraptim
```

Scoop connects the engine to your browsers by itself. **winget** (`winget install TenkuryuCode.DoRaptim`) will follow once Microsoft has accepted the package.

### For developers

The `.tar.gz` archives and `doraptim-<version>-x86_64-pc-windows-msvc.zip` contain only the engine program. Put it anywhere, then run `doraptim setup`.

### Install the Chrome extension (developer preview)

The extension is not in the Chrome Web Store yet. Until it is, each release includes it as `doraptim-extension-<version>-chrome.zip`, and you load it into Chrome yourself:

1. Download `doraptim-extension-<version>-chrome.zip` (the link under [Download](#download), or the same release as the installer).
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

## Use

- **Downloads from the browser** go to DoRaptim by itself once the extension is installed. A preview window lets you rename the file, choose where it goes, and start it; it then shows the progress.
- **The popup** (the DoRaptim icon in Chrome's toolbar) lists the current downloads, adds a download from a link, and opens the **Downloads** page with every download, their details, and the settings.
- **Videos:** choose **Find videos on this page** in the popup, or turn on **Find videos automatically** in the settings to get a **Download with DoRaptim** button on videos. Right-clicking a video or link also offers **Download with DoRaptim**. The button's menu lists the qualities to choose from. Supported: video and audio files, HLS streams (with a choice of quality, also encrypted with AES-128), players that stream video and audio separately (joined into one MP4), and subtitle files, which are saved next to the video. Streams are saved as MP4, which plays in QuickTime and every other player.
- **Not supported:** live streams, DASH streams for now, files on services that encrypt them end to end (such as MEGA), and services that protect their videos against copying (DRM) or do not allow downloading them, such as YouTube and Netflix. Download only what you have the right to download.

## Update

To see whether a newer version is out, run `doraptim update` in a terminal (Command Prompt on Windows), or watch this repository's Releases. To update, install the new installer or package over the old one: it stops the running engine and replaces it. With Homebrew run `brew upgrade doraptim`, with Scoop `scoop update doraptim`. Then load the new extension ZIP from the same release (unzip it into the same folder and choose reload on the extension's card).

## Uninstall

**Windows:** open *Settings*, *Apps*, *Installed apps*, choose **DoRaptim**, and *Uninstall*.

**macOS:** open Terminal and run:

```sh
doraptim uninstall
```

It stops the engine, removes it from your browsers, and deletes its download queue, then shows the three `sudo` commands that remove the program itself. Your downloaded files are not touched. Add `--keep-data` to keep the queue.

**Homebrew:** run `doraptim uninstall --yes`, then `brew uninstall doraptim`.

**Scoop:** run `scoop uninstall doraptim`.

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
