---
name: "jspassgen"
short_name: "jspassgen"
title: "Changelog: recent jspassgen releases | jspassgen"
description: "What changed in recent jspassgen releases, from the jspassgen repository's CHANGELOG: the web word-list fix, the conformance kit, the move to @sebastienrousseau/jspassgen and the exports map."
keywords: "jspassgen changelog, jspassgen release notes, jspassgen 0.0.21"
author: "Sebastien Rousseau"
date: "2026-10-26"
news_publication_date: "2026-10-26"
layout: "page"
language: "en-GB"
schema: "page"
changefreq: "monthly"
eyebrow: "Changelog"
headline: "Recent releases"
lead: "A summary of the jspassgen CHANGELOG. The full file, with every release, is in the repository."
---
## 0.0.21, 18 November 2026

- **Web word list:** the web version and the Web Worker built the core
  without a dictionary, so `memorable` passwords came from a 48-word
  placeholder list while their strength was reported for the 7,776-word
  EFF list, and `diceware` failed. Both now load the EFF list, and the core
  reports word-based entropy from the size of the list it is given
  ([GHSA-8q9w-f94p-vxg8](https://github.com/sebastienrousseau/jspassgen/security/advisories/GHSA-8q9w-f94p-vxg8)).
  The command line and the Node.js service were not affected.
- **Conformance kit:** `conformance/` holds the vectors every port of
  jspassgen must reproduce, generated from the core; the test suite fails
  if it drifts.
- **Release workflow:** the workflow starts when a release is published
  rather than created. 0.0.20's release was first created as a draft,
  which starts no workflow, so 0.0.20 was not published to GitHub Packages.
- **Dependencies:** commander ^15.1.0; npm overrides force `minimatch`
  ^11.0.1 and `glob` ^14.0.2, and the lockfile moves `serialize-javascript`
  to 7.1.4, clearing their Dependabot alerts.

## 0.0.20, 23 October 2026

- **New package name:** published as `@sebastienrousseau/jspassgen`. The unscoped `jspassgen`
  package stops at 0.0.19 and is deprecated. See the
  [migration guide](/migration/).
- **Exports map:** the root, `core`, `adapters/node` and `workers` are the
  public entry points; deep imports of other files no longer resolve.
- **Release workflow:** from 0.0.21, npm releases are staged through trusted
  publishing with provenance and approved by a maintainer. 0.0.20 was
  published by hand, without provenance.
- **Security:** `markdown-it` is constrained to `^14.3.3` so a version with a
  published advisory cannot resolve.

## 0.0.18 and 0.0.19, 10 October 2026

- Release workflow fixes for publishing to npm and GitHub Packages.

## 0.0.12, 9 October 2026

- `--allowed-chars` and `--forbidden-chars` for the `custom` type, and
  `--reveal` for honeyword sets.
- The core package and the TypeScript declarations are included in the
  published package.
- Faster random sampling in the Node.js adapter, drawing random bytes in
  batches with rejection sampling.

The [full CHANGELOG](https://github.com/sebastienrousseau/jspassgen/blob/main/CHANGELOG.md) covers every release
back to 0.0.1 in April 2022.
