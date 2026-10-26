---
name: "jspassgen"
short_name: "jspassgen"
title: "Contributing to jspassgen | jspassgen"
description: "How to report a bug, suggest a feature or send a change to jspassgen: setting up the repository, running the tests and linters, and opening a pull request."
keywords: "contribute to jspassgen, jspassgen development, jspassgen tests"
author: "Sebastien Rousseau"
date: "2026-10-26"
news_publication_date: "2026-10-26"
layout: "page"
language: "en-GB"
schema: "page"
changefreq: "monthly"
eyebrow: "Contributing"
headline: "Contributing to jspassgen"
lead: "Bug reports, documentation fixes and code are all welcome."
---
## How do I report a bug or ask for a feature?

[Open an issue](https://github.com/sebastienrousseau/jspassgen/issues/new/choose) with the steps to reproduce, what
you expected and what happened, and your Node.js version and operating
system. Report security problems by email instead, as the
[security page](/security/#how-do-i-report-a-vulnerability) explains.

## How do I set up the repository?

```bash
git clone https://github.com/sebastienrousseau/jspassgen.git
cd jspassgen
npm install
```

## How do I check a change?

```bash
npm test             # tests with coverage
npm run lint         # ESLint
npm run verify:core  # the core package imports nothing from outside
```

## How do I send a change?

Fork the repository, make your change on a branch, run the checks above and
open a pull request against the `master` branch. Keep the core package free
of dependencies: it must run anywhere the ports are provided.

## What about this website?

The site's source is in
[jspassgen.github.io](https://github.com/sebastienrousseau/jspassgen.github.io).
Corrections are welcome as issues or pull requests there.
