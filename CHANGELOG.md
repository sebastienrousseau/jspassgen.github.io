<!-- SPDX-License-Identifier: Apache-2.0 OR MIT -->

# Changelog

All notable changes to jspassgen.com are documented here.

## [0.0.25] - Unreleased

### Fixed

- The release notes' checksums list `SHA256SUMS` itself, so every
  asset attached to a release has its SHA-256 in the notes. The 0.0.23
  and 0.0.24 notes omitted it; the 0.0.24 notes were corrected.

## [0.0.24] - 2026-11-21

### Added

- Releases carry their SLSA build provenance. The release workflow
  attests every release file with `actions/attest-build-provenance`,
  signed through Sigstore and stored as a GitHub attestation, and
  attaches the bundle, listed in the release checksums, as
  `jspassgen.com-<version>.intoto.jsonl`. Check a download with
  `gh attestation verify <file> --repo sebastienrousseau/jspassgen.github.io`.
  This answers the OpenSSF Scorecard Signed-Releases check.

### Changed

- `VERSION` reads 0.0.24.
- The pages name 0.0.24 as the latest release (about page, structured
  data, the home page's npm line, the documentation lead), and the
  changelog page summarises it.
- The README names 0.0.24 as the suite's third lockstep release.

## [0.0.23] - 2026-11-20

### Changed

- The site's project name is `jspassgen.com`, as pain001's site is
  `pain001.com`: release tags are annotated `jspassgen.com v<version>`,
  releases are titled `jspassgen.com <version>` and the release archive
  is `jspassgen.com-<version>-site.tar.gz`. The release workflow defines
  the name once instead of taking it from the repository name, which
  stays `jspassgen.github.io`. The 0.0.22 tag and release were renamed
  the same way.
- The README and AGENTS.md name the project `jspassgen.com`; links to
  the GitHub repository keep its real name.
- `VERSION` reads 0.0.23.
- The pages name 0.0.23 as the latest release (about page, structured
  data, the home page's npm line, the documentation lead), and the
  changelog page summarises it.
- `.github/CODEOWNERS` names the maintainer as owner of every file, so
  the `main` ruleset can require a code-owner review.

## [0.0.22] - 2026-11-18

### Changed

- The site joins the jspassgen suite's lockstep release at the family's
  version, 0.0.22, as its first tagged release; `VERSION` reads 0.0.22.
- Rebuilt the site with Static Site Generator and the Prism theme,
  coloured from the jspassgen logo, replacing the October 2026 site.
- Builds with ssg 0.0.76, the latest release: CI installs it and checks
  the archive against its published SHA-256. ssg's SRI check still misreads
  an apostrophe in a `<head>` comment, so `base.html` keeps them out.
- `jspassgen` is presented as the command everywhere; `password-generator`
  is described as an older alias of the same command, which the package
  still installs.
- Facts moved to jspassgen 0.0.21, released 18 November 2026: the npm
  version, `softwareVersion`, the latest release on the about page, the
  reference page, a changelog entry for 0.0.21, and the home page cards and
  the honeyword example regenerated from the 0.0.21 command line.
- Facts moved to jspassgen 0.0.22, released 18 November 2026: the npm
  version, `softwareVersion`, the latest release on the about page, the
  reference page's lead and a changelog entry for 0.0.22. The home page
  cards stay the output of the 0.0.21 command line, as they say.
- The web version links to doc.jspassgen.com, where
  sebastienrousseau.com/jspassgen now redirects, and the changelog and
  contributing pages name jspassgen's default branch, `main`.
- Rewrote every page from the jspassgen repository at version 0.0.21:
  the site now describes the command-line tool and the Node.js library as
  they ship, under the `@sebastienrousseau/jspassgen` package name, and
  drops claims the source does not support (Argon2id key derivation, a
  zero-dependency package, command-line flags that do not exist).
- `make build` checks colour contrast (WCAG AAA), requires ssg's quality
  gate at 10/10, verifies every `#fragment` and SRI hash, renders one social
  image per page and runs `ssg audit`; the Pages workflow builds and deploys
  the result instead of uploading committed output.

### Added

- A release workflow: on a signed `v<version>` tag annotated
  `jspassgen.github.io v<version>` and matching `VERSION`, it builds the
  site and drafts the GitHub release with a tarball of `docs/` and its
  SHA-256.
- Dependabot updates for the pinned workflow actions.

### Removed

- The in-browser generator on the home page, `openapi.json` (an API
  description with no paths), the hand-written `llms.txt`,
  `llms-full.txt` and `.well-known/agents.json` (the build now generates
  `llms.txt`, `agents.txt` and `.well-known/ai-plugin.json`), and the
  unused background photographs.

## [0.0.1] - 2026-10-26 (merged, not tagged)

### Changed

- Deployed GitHub Pages with GitHub Actions instead of from a branch.
