# DoRaptim downloads

Official downloads of DoRaptim, a download manager for your browser by Tenkuryu Code. The project website is [doraptim.com](https://doraptim.com). This repository only hosts the releases; the source code is private.

> DoRaptim is under active development. Do not rely on it for downloads that must not fail.

## Download

<!-- latest-downloads:start -->
**Latest version: 0.1.1-beta.6** ([release notes](https://github.com/TenkuryuCode/doraptim-releases/releases/tag/v0.1.1-beta.6))

The extension is installed from the [Chrome Web Store](https://chromewebstore.google.com/detail/opmbiaopegjjcijloalolfilhcpcbogk) (ID `opmbiaopegjjcijloalolfilhcpcbogk`), or for Firefox from [addons.mozilla.org](https://addons.mozilla.org/firefox/addon/doraptim/).

| Download | File |
|---|---|
| Windows (64-bit) installer | [doraptim-0.1.1-beta.6-windows-x86_64-setup.exe](https://github.com/TenkuryuCode/doraptim-releases/releases/download/v0.1.1-beta.6/doraptim-0.1.1-beta.6-windows-x86_64-setup.exe) |
| macOS installer, Apple Silicon (M1 or later) | [doraptim-0.1.1-beta.6-macos-arm64.pkg](https://github.com/TenkuryuCode/doraptim-releases/releases/download/v0.1.1-beta.6/doraptim-0.1.1-beta.6-macos-arm64.pkg) |
| macOS installer, Intel | [doraptim-0.1.1-beta.6-macos-x86_64.pkg](https://github.com/TenkuryuCode/doraptim-releases/releases/download/v0.1.1-beta.6/doraptim-0.1.1-beta.6-macos-x86_64.pkg) |

Check the files with [SHA256SUMS](https://github.com/TenkuryuCode/doraptim-releases/releases/download/v0.1.1-beta.6/SHA256SUMS). Every release, including older ones, is on the [Releases](https://github.com/TenkuryuCode/doraptim-releases/releases) page.
<!-- latest-downloads:end -->

## System requirements

DoRaptim runs on these systems. Older versions are not supported.

| System | Minimum | Processor | What you get |
|---|---|---|---|
| macOS | macOS 11 (Big Sur) or later | Apple Silicon (arm64) or 64-bit Intel (x86-64) | An installer with the engine and the desktop window |
| Windows | Windows 10 or later | 64-bit Intel or AMD (x86-64) | An installer with the engine and the desktop window |
| Linux | glibc 2.35 or later (Ubuntu 22.04 or newer) | 64-bit Intel or AMD (x86-64) | The engine as a `.tar.gz` archive, with no installer and no desktop window |

## Install

DoRaptim has two parts: the **engine**, a small program on your computer that does the downloading, and the **browser extension** for Chrome or Firefox, which hands browser downloads to it. Install the engine in one of the two ways below, then the extension.

### Option 1: download the installer

1. Download the installer for your computer from [Releases](../../releases):
   - **Windows (64-bit):** `doraptim-<version>-windows-x86_64-setup.exe`
   - **macOS, Apple Silicon (M1 or later):** `doraptim-<version>-macos-arm64.pkg`
   - **macOS, Intel:** `doraptim-<version>-macos-x86_64.pkg`
2. Open it and follow the steps. It installs the engine for your user account and connects it to the browsers you have.

Nothing else is needed: no Homebrew, no developer tools.

**On macOS** the app is installed in your own `~/Applications` folder (`~/Applications/DoRaptim.app`, with the engine inside). The installer asks for your administrator password **once**, on this first install; later updates need no password. To use the `doraptim` command in Terminal, add `~/.local/bin` to your `PATH` (the installer links the command there), for example by adding `export PATH="$HOME/.local/bin:$PATH"` to `~/.zshrc`.

**Coming from a beta?** Install 0.1.1 once by hand over the beta, as above. From then on the engine updates itself.

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
- **Do not mix the Homebrew install with the macOS installer (`.pkg`) on the same Mac.** You would get two separate `doraptim` commands, and each `doraptim setup` rewrites the browser registration so that it points at only one of them. Pick one. If you switch, uninstall the other first.

### On Windows, Scoop works too

```powershell
scoop bucket add doraptim https://github.com/TenkuryuCode/doraptim-releases
scoop install doraptim
```

Scoop connects the engine to your browsers by itself. **winget** (`winget install TenkuryuCode.DoRaptim`) will follow once Microsoft has accepted the package.

### For developers

The `.tar.gz` archives and `doraptim-<version>-x86_64-pc-windows-msvc.zip` contain only the engine program. Put it anywhere, then run `doraptim setup`.

### Install the browser extension

**Chrome** (and Edge, Brave, Opera, Vivaldi): install the extension from the [Chrome Web Store](https://chromewebstore.google.com/detail/opmbiaopegjjcijloalolfilhcpcbogk). Its ID is `opmbiaopegjjcijloalolfilhcpcbogk`. The installer connects the engine only to that ID.

**Firefox** (140 or later): install the add-on from [addons.mozilla.org](https://addons.mozilla.org/firefox/addon/doraptim/). The installer connects the engine to Firefox too, when Firefox is installed.

Do not load an unpacked ZIP from an older GitHub release: that build has a different ID, and the engine will not talk to it.

Chrome and Firefox update the extension by themselves. Keep the engine on the same version. Some managed (work or school) browsers only allow extensions on an allow list: ask the administrator to allow `opmbiaopegjjcijloalolfilhcpcbogk`.

### The builds are not code-signed yet

- **Windows** shows "Windows protected your PC". Choose *More info*, then *Run anyway*.
- **macOS** says the package cannot be checked. Open *System Settings*, *Privacy & Security*, and choose *Open Anyway*.

Only do this for files downloaded from this repository's Releases page.

## Use

- **Downloads from the browser** go to DoRaptim by itself once the extension is installed. A preview window lets you rename the file, choose where it goes, and start it; it then shows the progress.
- **The popup** (the DoRaptim icon in the browser's toolbar) lists the current downloads, adds a download from a link, and opens the **Downloads** page with every download, their details, and the settings.
- **Videos:** a **Download with DoRaptim** button appears on videos on popular video and social sites (such as TikTok, Instagram, Facebook, X, Bilibili, and Twitch) from install. **Find videos automatically** in the settings chooses where: **Off**, **Video sites** (the default), or **All sites**, which asks the browser first. On any page, **Find videos** in the popup lists what it has. Right-clicking a video or link also offers **Download with DoRaptim**. The button's menu lists the qualities to choose from. Supported: video and audio files, HLS streams (with a choice of quality, also encrypted with AES-128, and a separate audio track when the stream names one), DASH (`.mpd`) streams from 0.1.0-alpha.5, players that stream video and audio separately (joined into one MP4), and subtitle files, which are saved next to the video. Streams are saved as MP4, which plays in QuickTime and every other player.
- **Not supported:** live streams, files on services that encrypt them end to end (such as MEGA), and services that protect their videos against copying (DRM) or do not allow downloading them, such as YouTube and Netflix. Download only what you have the right to download.

## Update

**Installer (`.pkg` or `setup.exe`):** the engine checks for a new version once a day and, unless you turn it off in the settings, installs it by itself. This is on by default. When the Terms of Use or Privacy Policy change, it waits until you have read and accepted the new version in the DoRaptim window or the extension. On macOS an update needs no administrator password, because the app is in your own `~/Applications` folder. You can also check by hand with `doraptim update`, or in the desktop window under **Engine**. Updates are read from `latest.json` on this repository's `main` branch (checked with `latest.json.sig` when the engine was built with a public key).

**Homebrew and Scoop** update through their own tools and never update themselves: `brew update && brew upgrade doraptim`, or `scoop update doraptim`.

Chrome and Firefox update the extension from their stores by themselves.

## Uninstall

**Windows:** open *Settings*, *Apps*, *Installed apps*, choose **DoRaptim**, and *Uninstall*.

**macOS (installer):** open Terminal and run `doraptim uninstall` (if the command is not found, run `~/.local/bin/doraptim uninstall` or `~/Applications/DoRaptim.app/Contents/MacOS/doraptim uninstall`). It stops the engine, removes it from your browsers, asks whether to keep or delete the download queue, and removes `~/Applications/DoRaptim.app` and the `~/.local/bin/doraptim` command without a password. It asks for your administrator password only to clear what the installer keeps outside your home folder (the documents in `/usr/local/share/doc/doraptim` and the installer receipt, and the files of an older release). Your downloaded files are not touched. Add `--keep-data` to keep the queue, or `--remove-data` to delete it, without being asked.

**Homebrew:** run `doraptim uninstall --yes`, then `brew uninstall doraptim`.

**Scoop:** run `scoop uninstall doraptim`.

Then remove the extension: open `chrome://extensions` (in Firefox, `about:addons`) and choose **Remove** on DoRaptim.

## Check a download

Each release has a `SHA256SUMS` file. In the folder with your download:

```sh
sha256sum --check --ignore-missing SHA256SUMS          # Linux, or Windows with Git Bash
shasum -a 256 --check --ignore-missing SHA256SUMS      # macOS
```

## Privacy

The DoRaptim engine, browser extension, desktop app, and installers have no account, telemetry, analytics, or cloud service. The public website at doraptim.com uses Google Analytics 4 to measure aggregate website usage. See [PRIVACY.md](PRIVACY.md) ([Bahasa Indonesia](PRIVACY.id.md); also at [doraptim.com/en/privacy](https://doraptim.com/en/privacy/) and [doraptim.com/id/privacy](https://doraptim.com/id/privacy/)).

## Security

Report a vulnerability privately with this repository's *Security* tab, *Report a vulnerability*. Do not open a public issue.

## Terms

By installing or using DoRaptim you accept the [terms of use](TERMS-OF-USE.md) ([Bahasa Indonesia](TERMS-OF-USE.id.md); also at [doraptim.com/en/terms](https://doraptim.com/en/terms/) and [doraptim.com/id/terms](https://doraptim.com/id/terms/); the Indonesian version prevails if the two differ). In short: DoRaptim is free for personal use and internal use in your organization; you may not sell or redistribute the builds, and it comes without warranty.

Copyright (c) 2026 Tenkuryu Code. All rights reserved. The DoRaptim name and logo belong to Tenkuryu Code.
