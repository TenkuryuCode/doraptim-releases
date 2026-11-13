# Privacy

Last updated: 2026-11-14

DoRaptim runs on the user's own computer. The engine, browser extension, desktop application, and installers do not send telemetry or analytics to Tenkuryu Code and have no account service or hosted download proxy. The public website may use Google Analytics to measure aggregate website usage.

This page covers the engine, the browser extension, and the installers.

## Public website

The public DoRaptim website loads Google Analytics 4 in production. Google Analytics may use cookies or similar browser storage and may collect page views, interactions, approximate geographic information, device and browser information, and referral information. This data is sent to Google and used to understand website usage. It is not used to identify or combine website visitors with downloads performed by the engine or browser extension. Do not enter credentials or sensitive download URLs on the website.

## What the extension handles

The extension takes over a download the browser starts when it uses HTTP or HTTPS, does not come from a private window or from another extension, and is at least 1 MiB or of unknown size; the minimum size can be changed in the settings. For such a download, the extension passes these to the engine through Chrome native messaging, a local connection to a program on the same computer:

- the download URL and its redirect result;
- the suggested filename;
- the referrer and the browser's user-agent text.

The extension does not read or send cookies, passwords, browsing history, or page contents, and it asks for no host permissions when it is installed. Its settings (whether takeover is on, the minimum file size, whether to name files after the page, notifications, and whether to find videos automatically) are kept in Chrome's extension storage on the device.

Naming files after the page is off by default. When the user turns it on, Chrome asks for the `tabs` permission, which lets the extension read the titles and addresses of open tabs. The extension uses it only when a captured download has a meaningless name, to read the title of the page the download came from, and only to suggest a name in the preview window. The title is kept in the browser's memory until the preview closes; only the name the user confirms reaches the engine. Turning the setting off gives the permission back.

Finding videos works in two ways. **Find videos on this page** in the popup looks at the page the user is on, only when they click it, including embedded players' frames the extension may read. **Find videos automatically**, off by default, does the same on every page, also on pages already open when it is turned on, so that a download button can appear on videos; turning it on asks Chrome for access to all sites, and turning it off gives it back. Either way the extension reads, inside the page, the addresses of its video and audio, links to media files, subtitle files and their labels and languages, and the addresses of the files the page's player has loaded (for a player that fetches video and audio separately, the address of each whole file is worked out from them). When the user opens the video button's menu for a stream or for a player that fetches video and audio separately, the addresses of its files go to the engine, which asks their server about each one (its size, and for a video file the first 256 KiB, to read the picture size) so the menu can list the qualities; nothing is kept. The button inside an embedded player's frame also asks the extension for the title of the page it is shown on, to show it in the menu. Otherwise nothing leaves the browser until the user picks a video: then its address (or the addresses of its video and audio files), its subtitles' addresses, labels, and languages, the address of the page or frame that played it as the referrer, the page's title (as a suggested name), and the video's length and quality (shown in the preview) go to the engine or stay in the browser's memory, as for any other download. **Download with DoRaptim** in the right-click menu hands over the link or media the user clicked in the same way.

## What the engine keeps

The engine may process and store, in a SQLite journal on the device:

- source URLs and redirect results;
- optional referrer and user-agent metadata supplied by a client;
- response metadata such as filename, size, content type, ETag, and Last-Modified;
- queue state, progress, retry state, destination category, and errors;
- optional expected and computed SHA-256 values;
- for a stream or a video with separate audio, the addresses of the qualities it offers, of its audio file, and of the subtitles offered with it, with their labels and languages;
- the download folder and category subfolder names the user chose, a folder chosen for a single download, and the number of parallel downloads and speed limit the user set;
- the download hours the user set (days and local times) and whether "Wi‑Fi or cable only" is on.

The journal can contain sensitive URLs, because some sites put tokens in them. Protect it with normal operating-system account permissions and do not share it. Referrers and user agents are used for the download and are not written to the journal. The daemon also keeps a private local file with a random access token, replaced at every start.

When a download finishes, the engine puts the operating system's own "from the internet" mark on the file, as browsers do: the `com.apple.quarantine` attribute on macOS and the `Zone.Identifier` stream on Windows. The mark holds the time and the name DoRaptim, or the internet zone; it never holds the address or the page the file came from.

## Network activity

The engine connects only to the sources the user or a local client asked for, including the redirects those sources require and, for a video the user chose, its stream pieces, its separate audio file, and the subtitles the user kept ticked. It does not contact any server of Tenkuryu Code for downloads. Checking for a newer engine reads a signed `latest.json` from the public `doraptim-releases` repository (`raw.githubusercontent.com`). That request carries the program's version in its User-Agent and nothing else about the user or their downloads. `doraptim update` does this when the user runs it. An optional setting, off by default, lets the engine do the same at most once a day; it can be turned off in Settings.

When "Wi‑Fi or cable only" is on, the engine asks the operating system what kind of connection the computer uses, about every 30 seconds: on macOS, the network port of the default route (for example Wi‑Fi, Ethernet, or an iPhone over USB); on Windows, whether Windows counts the connection as metered. This is a question to the computer itself: nothing is sent over the network for it, and the answer is kept only in the engine's memory, not in the journal. With the setting off, the engine does not ask.

When the user gives a page address instead of a file address, the extension opens that page in the user's own browser, and the page and its media come straight from that website to the device. Tenkuryu Code runs no intermediate server for this and never receives the address, the page, or the files. The address and the download's state are kept only in the local journal on the device. The journal is not encrypted: protect it with operating-system account permissions.

## Local interfaces

The daemon binds to the loopback address, requires the bearer token, and checks request host and origin information. Native messaging uses local process pipes. The installers register the native-messaging host for the current user and for the exact extension IDs they were built with.

## Logs

Logs must not contain passwords, authorization values, cookies, secrets, or complete credential-bearing URLs.

## User control

Users can turn the extension's takeover off, choose the download directory, remove queue records, and delete downloaded files. Uninstalling the extension and running `doraptim host uninstall` remove the browser integration. Deleting the journal after the daemon has stopped clears the stored history.

## Contact

Questions about privacy: open an issue in this repository. Security problems: use the *Security* tab, *Report a vulnerability*, instead of a public issue.
