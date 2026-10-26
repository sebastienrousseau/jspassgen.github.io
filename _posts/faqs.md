---
name: "jspassgen"
short_name: "jspassgen"
title: "Frequently asked questions about jspassgen | jspassgen"
description: "Answers about jspassgen: what it is, the package name, Node.js versions, how random the passwords are, entropy, quantum resistance, honeywords, the browser and the licence."
keywords: "jspassgen faq, is jspassgen secure, jspassgen node version, jspassgen quantum resistant"
author: "Sebastien Rousseau"
date: "2026-10-26"
news_publication_date: "2026-10-26"
layout: "page"
language: "en-GB"
schema: "page"
changefreq: "monthly"
eyebrow: "FAQ"
headline: "Frequently asked questions"
lead: "Short answers first; each links to the page with the detail where there is one."
nav_faqs: "true"
---
## What is jspassgen?

A free, open-source password and passphrase generator for Node.js, used from
the command line or imported as a library. See the [features](/features/).

## Which npm package is it?

`@sebastienrousseau/jspassgen`, since version 0.0.20. The unscoped `jspassgen` package is
deprecated at 0.0.19; see the [migration guide](/migration/).

## Which Node.js versions does it support?

Node.js 22 or newer. CI tests on Node.js 22 and 24.

## How random are the passwords?

Every character and word comes from Node.js `crypto`, with rejection
sampling so no character is favoured. See the [security page](/security/).

## How much entropy do I need?

That depends on what the password protects and how it is stored. jspassgen
prints the entropy of each result, so you can compare: four EFF words are
about 52 bits, and the `quick` preset, four chunks of 14 characters, is
336 bits.

## Is the quantum-resistant type a different algorithm?

No. It uses the same random source and alphabet as `strong`, sized to carry
at least 256 bits; the `quantum` preset gives 258 bits. See
[password types](/features/#eight-password-types).

## What is a honeyword?

A decoy password stored next to the real one, so that a login with the
decoy reveals a stolen password database. jspassgen generates the set; see
[honeywords](/features/#honeywords).

## Can I use it in a browser?

Yes. A web version is published from the repository at
[sebastienrousseau.com/jspassgen](https://sebastienrousseau.com/jspassgen/),
and the core package runs with the repository's Web Crypto adapter.

## Is jspassgen a password manager?

No. It does not store or sync anything. Use it to create passwords, and a
password manager to keep them.

## What licence is it under?

Apache-2.0 or MIT, at your option. See the [terms](/terms/).
