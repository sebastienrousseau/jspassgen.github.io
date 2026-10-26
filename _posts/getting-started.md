---
name: "jspassgen"
short_name: "jspassgen"
title: "Getting started with jspassgen: install and generate a first password | jspassgen"
description: "Install jspassgen with npm or run it with npx, generate a password and a passphrase, use presets and bulk output, and call it from Node.js code."
keywords: "jspassgen getting started, npx jspassgen, npm install jspassgen, password generator node"
author: "Sebastien Rousseau"
date: "2026-10-26"
news_publication_date: "2026-10-26"
layout: "page"
language: "en-GB"
schema: "page"
changefreq: "monthly"
eyebrow: "Getting started"
headline: "Your first password with jspassgen"
lead: "From nothing installed to a password, a passphrase and a script that generates them."
nav_docs: "true"
---
## What do I need?

Node.js 22 or newer, the version the package declares in `engines`. CI tests
jspassgen on Node.js 22 and 24.

## How do I run it without installing?

```bash
npx @sebastienrousseau/jspassgen -p quick
```

npx downloads the package and runs it once. Run it again with
`-p memorable` for a passphrase of four words.

## How do I install the command?

```bash
npm install -g @sebastienrousseau/jspassgen
jspassgen -p secure
```

The package installs two commands, `jspassgen` and `password-generator`,
which are the same program.

## How do I choose the details myself?

Give the type, the length of each chunk, the number of chunks and the
separator:

```bash
jspassgen -t strong -l 16 -i 3 -s -
jspassgen -t memorable -i 5 -s .
```

Add `-c` to copy the result to the clipboard, or `-a` for an audit report
alongside it. The [reference](/documentation/#command-line-options) lists
every flag.

## How do I generate many at once?

```bash
jspassgen -p quick -n 5 -f json
```

`-f` accepts `text`, `json`, `csv` and `yaml`.

## How do I call it from code?

Install the package in your project:

```bash
npm install @sebastienrousseau/jspassgen
```

Then import the default export. It is an ES module, so use `import` in a
`.mjs` file or a package with `"type": "module"`:

```javascript
import PasswordGenerator from '@sebastienrousseau/jspassgen';

const password = await PasswordGenerator({
  type: 'strong',
  length: 20,
  iteration: 2,
  separator: '-',
});

console.log(password);
```

The [API reference](/documentation/#library-api) shows the core service,
which also returns the entropy.
