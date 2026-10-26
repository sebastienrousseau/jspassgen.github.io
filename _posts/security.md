---
name: "jspassgen"
short_name: "jspassgen"
title: "Security: random source, scope and vulnerability reporting | jspassgen"
description: "How jspassgen draws randomness, what it does and does not protect against, how to store what it generates, and how to report a vulnerability."
keywords: "jspassgen security, csprng, crypto.randomBytes, rejection sampling, report vulnerability"
author: "Sebastien Rousseau"
date: "2026-10-26"
news_publication_date: "2026-10-26"
layout: "page"
language: "en-GB"
schema: "page"
changefreq: "monthly"
eyebrow: "Security"
headline: "What jspassgen protects, and what it leaves to you"
lead: "A password generator has one job: make secrets an attacker cannot guess. This page says how jspassgen does it and where its job ends."
nav_security: "true"
---
## Where does the randomness come from?

From the operating system, through Node.js `crypto`: `crypto.randomBytes`
and `crypto.randomInt` in the Node.js adapter, and `crypto.getRandomValues`
from the Web Crypto API in the browser adapter. Characters are picked with
rejection sampling, so each character in the alphabet is equally likely.

## How strong is a generated password?

As strong as its entropy, which jspassgen prints with every result: about
6 bits per character from the 64-character alphabet and about 12.9 bits per
word from the EFF list. The figure assumes the attacker knows how the
password was generated; it does not depend on keeping the settings secret.
The [features page](/features/#an-entropy-estimate-for-every-result) explains
the calculation.

## What does jspassgen not do?

- **It does not store passwords.** Keep them in a password manager.
- **It does not hash passwords.** A server that stores passwords should hash
  them with a key-derivation function such as Argon2id, scrypt or bcrypt;
  jspassgen does neither.
- **It does not send anything over the network.** Generation is local.
- **It does not detect breaches.** A honeyword set is only useful if the
  system that stores it alerts on a decoy login.

## What about the clipboard?

`-c` writes the password to the system clipboard, where other programs on
the machine can read it until it is overwritten. Clear it yourself when you
have pasted the password.

## How do I report a vulnerability?

Email **hello@jspassgen.com**, the address in jspassgen's
[security policy](https://github.com/sebastienrousseau/jspassgen/security/policy), with a description, steps to
reproduce and the impact. Do not open a public issue for a vulnerability.
Machine-readable contact details are in
[/.well-known/security.txt](/.well-known/security.txt).
