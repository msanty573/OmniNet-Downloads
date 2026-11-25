# Security policy

Thank you for helping keep MJSNet and its users safe.

## Supported versions

Only the **latest release** of MJSNet receives security fixes. **Help → Check for
Updates…** in the app installs it, as do `dnf` and `apt` for the Linux packages. The
newest downloads are always at <https://mjsapps.net/mjsnet/>.

| Version | Supported |
|---|---|
| Latest release | ✅ |
| Older releases | ❌ — please update |

## Reporting a vulnerability

**Please don't report security problems in a public issue, discussion or post.** Report
them privately in either of these ways:

- **GitHub:** open the **Security** tab of this repository and click
  **Report a vulnerability**. Only you and the maintainer can see the report.
- **Email:** <support@mjsapps.net>, with "Security" in the subject.

Please include:

- the MJSNet version and build — shown in **Help → About MJSNet** (for example
  *1.0.0, macOS · Apple silicon (arm64)*), or which download or page it affects;
- your operating system and version;
- what the problem is and the steps to reproduce it, and what an attacker could do with it.

## What happens next

- You'll get a reply **within 3 business days** confirming the report was received.
- We'll keep you updated while we investigate, and tell you whether the report is
  accepted or declined and why.
- Fixes are released as a new version, delivered through Check for Updates, `dnf` and
  `apt`. With your permission, we're glad to credit you in the release notes.
- Please give us a reasonable time to release a fix before sharing details publicly.

## Scope

- The MJSNet apps for macOS, Windows and Linux, and their installers and packages.
- The update information MJSNet downloads (`update-*.json`) and the signed `dnf` and
  `apt` repositories at <https://msanty573.github.io/OmniNet-Downloads/>.

## How MJSNet handles your data

MJSNet works on your computer. Scan results, device names and notes, and history are
stored locally (on a Mac in `~/Library/Application Support/MJSNet`) and are never sent
anywhere. Your router's admin password, if you give it, is kept in the system keychain.

MJSNet talks to the internet only for these, all over HTTPS:

- **Check for Updates** — MJSNet's update information and, when you choose to update,
  the new version from GitHub, checked against a SHA-256 checksum before use. The daily
  automatic check can be turned off in the **Help** menu.
- **Known-vulnerability lookups** — the names and version numbers of software found on
  your devices (for example "OpenSSH 9.9") are looked up in NIST's National
  Vulnerability Database, and CISA's list of exploited vulnerabilities is downloaded.
  No addresses or other details about your network are sent. Turn it off in Settings.
- **What the internet sees** (Tools) — only when you press its button, your home's
  public IP address is looked up in Shodan's InternetDB.

Scanning itself stays on your network: MJSNet only connects to devices the way any app
does and never tries to log in or break in.
