---
name: "jspassgen"
short_name: "jspassgen"
title: "CLI and API reference | jspassgen"
description: "Reference for jspassgen: every command-line option and preset, the default export, the core service, the package entry points and the Node.js and Web Crypto adapters."
keywords: "jspassgen reference, jspassgen cli options, jspassgen api, createService, NodeCryptoRandom"
author: "Sebastien Rousseau"
date: "2026-10-26"
news_publication_date: "2026-10-26"
layout: "page"
language: "en-GB"
schema: "page"
changefreq: "monthly"
eyebrow: "Reference"
headline: "Command-line options and library API"
lead: "Everything the 0.0.20 package exposes, checked against its source."
nav_docs: "true"
---
## Command-line options

```text
jspassgen [options]
```

| Option | What it does |
| :--- | :--- |
| `-p, --preset <name>` | Use a preset: `quick`, `secure`, `memorable`, `quantum`, `diceware` or `pronounceable` |
| `-t, --type <type>` | Password type: `strong`, `base64`, `memorable`, `quantum-resistant`, `diceware`, `honeyword`, `pronounceable` or `custom` |
| `-l, --length <n>` | Length of each chunk |
| `-i, --iteration <n>` | Number of chunks, words or syllables |
| `-s, --separator <char>` | Separator between chunks |
| `-c, --clipboard` | Copy the result to the clipboard |
| `-a, --audit` | Print a security audit report with the result |
| `--learn` | Print the explicit flags a preset stands for |
| `-n, --count <n>` | Number of passwords to generate |
| `-f, --format <format>` | Output format for bulk generation: `text`, `json`, `csv` or `yaml` |
| `--allowed-chars <chars>` | Named sets or literal characters for `custom` |
| `--forbidden-chars <chars>` | Characters to leave out of `custom` |
| `--reveal` | Mark the real password in `honeyword` output |
| `--interactive` | Start the guided setup |
| `-h, --help` | Print the usage |

Without a preset, give `-t`, `-i` and `-s`; `-l` defaults to 16. The
[features page](/features/#presets) lists what each preset sets.

## Library API

The default export generates one password from a configuration object and
returns it as a string:

```javascript
import PasswordGenerator from '@sebastienrousseau/jspassgen';

const password = await PasswordGenerator({
  type: 'strong',
  length: 20,
  iteration: 2,
  separator: '-',
});
```

## The core package

`createService` builds a generator around a random source you supply.
`generate` returns an object with the password and, when asked, its entropy
and a security level:

```javascript
import { createService } from '@sebastienrousseau/jspassgen/core';
import { NodeCryptoRandom } from '@sebastienrousseau/jspassgen/adapters/node';

const service = createService({}, { randomGenerator: new NodeCryptoRandom() });

const result = await service.generate({
  type: 'quantum-resistant',
  length: 43,
  includeEntropy: true,
});

console.log(result.password);
console.log(`Entropy: ${result.entropy} bits (${result.securityLevel})`);
```

This prints a 43-character password and `Entropy: 258 bits (EXCELLENT)`.

## Package entry points

The package's `exports` map makes these paths public; other files inside
the package cannot be imported.

| Import path | What it holds |
| :--- | :--- |
| `@sebastienrousseau/jspassgen` | The default export above, with TypeScript declarations |
| `@sebastienrousseau/jspassgen/core` | The platform-independent core: `createService`, generators, ports |
| `@sebastienrousseau/jspassgen/adapters/node` | Node.js adapters, including `NodeCryptoRandom` |
| `@sebastienrousseau/jspassgen/workers` | A pool of Web Workers for generating in parallel |

The browser adapter, which uses `crypto.getRandomValues`, is in the
repository under `src/adapters/web/`.
