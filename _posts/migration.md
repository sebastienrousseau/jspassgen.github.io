---
name: "jspassgen"
short_name: "jspassgen"
title: "Migrating from the jspassgen package to @sebastienrousseau/jspassgen | jspassgen"
description: "jspassgen moved to the scoped npm name @sebastienrousseau/jspassgen in version 0.0.20. How to switch the command, the dependency and the imports."
keywords: "jspassgen migration, @sebastienrousseau/jspassgen, jspassgen deprecated, npm package rename"
author: "Sebastien Rousseau"
date: "2026-10-26"
news_publication_date: "2026-10-26"
layout: "page"
language: "en-GB"
schema: "page"
changefreq: "monthly"
eyebrow: "Migration"
headline: "Moving to @sebastienrousseau/jspassgen"
lead: "Version 0.0.20 changed the package name and added an exports map. The commands did not change."
nav_migration: "true"
---
## What changed?

From version 0.0.20, jspassgen is published on npm as `@sebastienrousseau/jspassgen`. The unscoped
`jspassgen` package stops at 0.0.19 and is marked deprecated, with the
message "Moved to @sebastienrousseau/jspassgen. Install that instead."

## How do I update the command?

```bash
npm uninstall -g jspassgen
npm install -g @sebastienrousseau/jspassgen
```

The `jspassgen` and `password-generator` commands and their options are the
same.

## How do I update a project?

```bash
npm uninstall jspassgen
npm install @sebastienrousseau/jspassgen
```

Then change the import paths:

| Before | After |
| :--- | :--- |
| `import PasswordGenerator from 'jspassgen'` | `import PasswordGenerator from '@sebastienrousseau/jspassgen'` |
| `'jspassgen/core'` or `'@jspassgen/core'` | `'@sebastienrousseau/jspassgen/core'` |

## What else changed in 0.0.20?

The package now has an `exports` map. Its public entry points are the root,
`core`, `adapters/node` and `workers`; the
[reference](/documentation/#package-entry-points) lists them. Imports of
other files deep inside the package no longer resolve, so move any such
import to one of those entry points.
