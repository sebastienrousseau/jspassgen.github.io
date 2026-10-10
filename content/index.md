---
name: "jspassgen"
short_name: "jspassgen"
title: "jspassgen | Quantum-Resistant Password and Passphrase Generator"
description: "Zero-dependency, quantum-resistant password and EFF Diceware passphrase generator with Shannon entropy scoring, honeyword decoys, and client-side WebCrypto security."
keywords: "password generator, diceware, passphrase, quantum-resistant, argon2id, honeywords, shannon entropy, nist sp 800-63b, webcrypto, zero-dependency, jspassgen"
author: "Sebastien Rousseau"
date: "2026-10-10"
layout: "index"
language: "en-GB"
schema: "SoftwareApplication"
changefreq: "daily"
copyright_year: "2026"
theme_style: "style-dark"
theme_colour: "#10b981"
---

## Cryptographic Security Overview

jspassgen is an open-source, zero-dependency password and passphrase generator designed for the post-quantum era.

### Core Guarantees

* **100% Client-Side Execution**: Cryptographic operations occur strictly within the browser using W3C WebCrypto `crypto.getRandomValues()` or the Node.js `crypto` module.
* **Information-Theoretic Rigour**: Real-time Shannon Entropy computation measures genuine randomness and unpredictability rather than simplistic rule validation.
* **Active Defense with Honeywords**: Generates Juels-Rivest decoy passwords for breach detection and proactive canary alerting.
* **Dual Open-Source Licensing**: Licensed under Apache-2.0 and MIT for unencumbered commercial and private integration.
