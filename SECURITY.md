# Security policy

## Reporting a vulnerability

Please do not open a public issue for a security problem.

Report it privately through **Security → Report a vulnerability** on this repository. This sends the report only to the maintainers.

Include:

- the affected version (for example `0.1.1`) and platform (Windows, macOS, Linux, Android, or browser extension);
- the steps to reproduce, and what you expected to happen;
- the impact you think it has.

We will acknowledge the report and keep you updated while we investigate.

## Scope

This repository hosts release downloads and package manifests (Homebrew, Scoop, winget, and `latest.json`). Problems in these files, in the release process, or in the checksums and signatures are in scope. The application's source code is maintained privately; report issues in the application here as well, and we will route them.

## Verifying downloads

Each release publishes a `SHA256SUMS` file. Check your download against it before installing.
