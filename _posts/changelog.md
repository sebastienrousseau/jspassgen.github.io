---
name: "jspassgen"
short_name: "jspassgen"
title: "Changelog: recent jspassgen releases | jspassgen"
description: "What changed in recent jspassgen releases, from the jspassgen repository's CHANGELOG: the move to @sebastienrousseau/jspassgen, the exports map and release workflow changes."
keywords: "jspassgen changelog, jspassgen release notes, jspassgen 0.0.20"
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
## 0.0.21 (in progress)

- The release workflow starts when a release is published rather than
  created. 0.0.20's release was first created as a draft, which starts no
  workflow, so 0.0.20 was not published to GitHub Packages.

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

The [full CHANGELOG](https://github.com/sebastienrousseau/jspassgen/blob/master/CHANGELOG.md) covers every release
back to 0.0.1 in April 2022.
