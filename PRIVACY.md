# Privacy

Last updated: 2026-10-31

DoRaptim runs on the user's own computer. The project has no account service, telemetry, analytics, advertising, or hosted download proxy, and it sends nothing to Tenkuryu Code.

This page covers the engine, the browser extension, and the installers.

## What the extension handles

When the browser starts a supported download (HTTP or HTTPS, not from a private window, not started by another extension, and by default at least 1 MiB or of unknown size), the extension passes these to the engine through Chrome native messaging, a local connection to a program on the same computer:

- the download URL and its redirect result;
- the suggested filename;
- the referrer and the browser's user-agent text.

The extension does not read or send cookies, passwords, browsing history, or page contents, and it requests no host permissions. Its settings (whether takeover is on, and the minimum file size) are kept in Chrome's extension storage on the device.

## What the engine keeps

The engine may process and store, in a SQLite journal on the device:

- source URLs and redirect results;
- optional referrer and user-agent metadata supplied by a client;
- response metadata such as filename, size, content type, ETag, and Last-Modified;
- queue state, progress, retry state, destination category, and errors;
- optional expected and computed SHA-256 values.

The journal can contain sensitive URLs, because some sites put tokens in them. Protect it with normal operating-system account permissions and do not share it. Referrers and user agents are used for the download and are not written to the journal. The daemon also keeps a private local file with a random access token, replaced at every start.

## Network activity

The engine connects only to the sources the user or a local client asked for, including the redirects those sources require. It does not contact any server of its own and does not check for updates by itself.

## Local interfaces

The daemon binds to the loopback address, requires the bearer token, and checks request host and origin information. Native messaging uses local process pipes. The installers register the native-messaging host for the current user and for the exact extension IDs they were built with.

## Logs

Logs must not contain passwords, authorization values, cookies, secrets, or complete credential-bearing URLs.

## User control

Users can turn the extension's takeover off, choose the download directory, remove queue records, and delete downloaded files. Uninstalling the extension and running `doraptim host uninstall` remove the browser integration. Deleting the journal after the daemon has stopped clears the stored history.

## Contact

Questions about privacy: open an issue in this repository. Security problems: use the *Security* tab, *Report a vulnerability*, instead of a public issue.
