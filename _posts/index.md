---
name: "jspassgen"
short_name: "jspassgen"
title: "jspassgen: password and passphrase generator for Node.js"
description: "jspassgen generates passwords and passphrases from the platform's cryptographic random source, as a command-line tool and a Node.js library, with eight generation types and an entropy estimate for each result."
keywords: "jspassgen, password generator, passphrase generator, diceware, EFF word list, honeywords, Node.js, npm, CLI"
author: "Sebastien Rousseau"
date: "2026-10-26"
news_publication_date: "2026-10-26"
layout: "index"
language: "en-GB"
schema: "page"
changefreq: "weekly"
eyebrow: "Open-source password generator"
headline: "Strong passwords and passphrases from your terminal or your code"
lead: "jspassgen draws every character and word from Node.js crypto, offers eight kinds of secret from random strings to EFF word passphrases, and tells you how much entropy each one has."
---
## What is jspassgen?

jspassgen is a free, open-source password and passphrase generator for
Node.js. It runs as a command-line tool, installed as both `jspassgen` and
`password-generator`, and as an ES module you can import. It produces eight
kinds of secret, from chunks of random characters to passphrases of words
from the EFF word list, draws its randomness from Node.js `crypto`, and
reports an entropy estimate in bits for each result. It is dual-licensed
under Apache-2.0 or MIT.

## Which package do I install?

`@sebastienrousseau/jspassgen`. Since version 0.0.20 jspassgen is published under that scoped
name; the unscoped `jspassgen` package stops at 0.0.19 and is deprecated.
The commands are unchanged. The [migration guide](/migration/) covers the
switch.

```bash
npx @sebastienrousseau/jspassgen -p quick
```

## What does it not do?

jspassgen generates secrets; it does not store, hash, synchronise or send
them. Keep what it generates in a password manager, and hash passwords on
the server with a key-derivation function. The [security page](/security/)
sets out what it does and does not protect against.

## Can I use it in a browser?

The jspassgen repository also publishes a web version at
[sebastienrousseau.com/jspassgen](https://sebastienrousseau.com/jspassgen/).
In code, the generators live in a core package that takes its random source
as a parameter, and the repository ships a Web Crypto adapter for it; see
the [API reference](/documentation/#the-core-package).

## Who makes it?

jspassgen is written by [Sebastien Rousseau](https://sebastienrousseau.com/).
The source, the issue tracker and every release are on
[GitHub](https://github.com/sebastienrousseau/jspassgen); the package is on [npm](https://www.npmjs.com/package/@sebastienrousseau/jspassgen). Read more on the
[about page](/about/).
