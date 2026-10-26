<!-- SPDX-License-Identifier: Apache-2.0 OR MIT -->

# Changelog

All notable changes to jspassgen.com are documented here.

## [0.0.2] - Unreleased

### Changed

- Rebuilt the site with Static Site Generator 0.0.69 and the Prism theme,
  coloured from the jspassgen logo, replacing the October 2026 site.
- Rewrote every page from the jspassgen repository at version 0.0.21:
  the site now describes the command-line tool and the Node.js library as
  they ship, under the `@sebastienrousseau/jspassgen` package name, and
  drops claims the source does not support (Argon2id key derivation, a
  zero-dependency package, command-line flags that do not exist).
- `make build` checks colour contrast (WCAG AAA), requires ssg's quality
  gate at 10/10, verifies every `#fragment` and SRI hash, renders one social
  image per page and runs `ssg audit`; the Pages workflow builds and deploys
  the result instead of uploading committed output.

### Removed

- The in-browser generator on the home page, `openapi.json` (an API
  description with no paths), the hand-written `llms.txt`,
  `llms-full.txt` and `.well-known/agents.json` (the build now generates
  `llms.txt`, `agents.txt` and `.well-known/ai-plugin.json`), and the
  unused background photographs.

## [0.0.1] - 2026-10-26 (merged, not tagged)

### Changed

- Deployed GitHub Pages with GitHub Actions instead of from a branch.
