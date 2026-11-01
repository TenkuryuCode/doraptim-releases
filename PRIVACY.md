# Privacy

Last updated: 2026-11-01

DoRaptim runs on the user's own computer. The project has no account service, telemetry, analytics, advertising, or hosted download proxy, and it sends nothing to Tenkuryu Code.

This page covers the engine, the browser extension, and the installers.

## What the extension handles

When the browser starts a supported download (HTTP or HTTPS, not from a private window, not started by another extension, and by default at least 1 MiB or of unknown size), the extension passes these to the engine through Chrome native messaging, a local connection to a program on the same computer:

- the download URL and its redirect result;
- the suggested filename;
- the referrer and the browser's user-agent text.

The extension does not read or send cookies, passwords, browsing history, or page contents, and it asks for no host permissions when it is installed. Its settings (whether takeover is on, the minimum file size, whether to name files after the page, notifications, and whether to find videos automatically) are kept in Chrome's extension storage on the device.

Naming files after the page is off by default. When the user turns it on, Chrome asks for the `tabs` permission, which lets the extension read the titles and addresses of open tabs. The extension uses it only when a captured download has a meaningless name, to read the title of the page the download came from, and only to suggest a name in the preview window. The title is kept in the browser's memory until the preview closes; only the name the user confirms reaches the engine. Turning the setting off gives the permission back.

Finding videos works in two ways. **Find videos on this page** in the popup looks at the page the user is on, only when they click it, including embedded players' frames the extension may read. **Find videos automatically**, off by default, does the same on every page, also on pages already open when it is turned on, so that a download button can appear on videos; turning it on asks Chrome for access to all sites, and turning it off gives it back. Either way the extension reads, inside the page, the addresses of its video and audio, links to media files, subtitle files and their labels and languages, and the addresses of the files the page's player has loaded (for a player that fetches video and audio separately, the address of each whole file is worked out from them). Nothing leaves the browser until the user picks a video: then its address (or the addresses of its video and audio files), its subtitles' addresses, labels, and languages, the address of the page or frame that played it as the referrer, the page's title (as a suggested name), and the video's length and quality (shown in the preview) go to the engine or stay in the browser's memory, as for any other download. **Download with DoRaptim** in the right-click menu hands over the link or media the user clicked in the same way.

## What the engine keeps

The engine may process and store, in a SQLite journal on the device:

- source URLs and redirect results;
- optional referrer and user-agent metadata supplied by a client;
- response metadata such as filename, size, content type, ETag, and Last-Modified;
- queue state, progress, retry state, destination category, and errors;
- optional expected and computed SHA-256 values;
- for a stream or a video with separate audio, the addresses of the qualities it offers, of its audio file, and of the subtitles offered with it, with their labels and languages;
- the download folder and category subfolder names the user chose, a folder chosen for a single download, and the number of parallel downloads and speed limit the user set.

The journal can contain sensitive URLs, because some sites put tokens in them. Protect it with normal operating-system account permissions and do not share it. Referrers and user agents are used for the download and are not written to the journal. The daemon also keeps a private local file with a random access token, replaced at every start.

## Network activity

The engine connects only to the sources the user or a local client asked for, including the redirects those sources require and, for a video the user chose, its stream pieces, its separate audio file, and the subtitles the user kept ticked. It does not contact any server of its own and does not check for updates by itself. Only when the user runs `doraptim update` does it ask GitHub (`api.github.com`) for the list of published releases; that request carries the program's version in its User-Agent and nothing else about the user or their downloads.

## Local interfaces

The daemon binds to the loopback address, requires the bearer token, and checks request host and origin information. Native messaging uses local process pipes. The installers register the native-messaging host for the current user and for the exact extension IDs they were built with.

## Logs

Logs must not contain passwords, authorization values, cookies, secrets, or complete credential-bearing URLs.

## User control

Users can turn the extension's takeover off, choose the download directory, remove queue records, and delete downloaded files. Uninstalling the extension and running `doraptim host uninstall` remove the browser integration. Deleting the journal after the daemon has stopped clears the stored history.

## Contact

Questions about privacy: open an issue in this repository. Security problems: use the *Security* tab, *Report a vulnerability*, instead of a public issue.
