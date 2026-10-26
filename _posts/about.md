---
name: "jspassgen"
title: "About jspassgen | Security Architecture and Principles"
description: "Cryptographic principles, hexagonal architecture, and verifiable entropy standards behind jspassgen."
author: "Sebastien Rousseau"
date: "2026-10-10"
lastmod: "2026-10-10"
news_publication_date: "2026-10-10T12:00:00+00:00"
layout: "page"
language: "en-GB"
theme_color: "#2455e8"
theme_colour: "#2455e8"
---

# About jspassgen

jspassgen was created to solve a persistent vulnerability in modern authentication workflows: the reliance on proprietary, cloud-hosted, and telemetry-heavy password generators.

## Cryptographic Foundation and Formal Specifications

jspassgen implements established peer-reviewed cryptographic standards and information-theoretic formulations:

1. **Information Entropy**: Credential strength is calculated using Claude Shannon's mathematical formulation of entropy:
   $$\mathcal{H}(X) = -\sum_{i=1}^{n} P(x_i) \log_2 P(x_i)$$
   Reference: Shannon, C. E. (1948), *"A Mathematical Theory of Communication"*, Bell System Technical Journal, [doi:10.1002/j.1538-7305.1948.tb01338.x](https://doi.org/10.1002/j.1538-7305.1948.tb01338.x).

2. **Digital Identity Standards**: Password generation strictly conforms to the [NIST SP 800-63B](https://csrc.nist.gov/pubs/sp/800/63/b/upd1/final) Digital Identity Guidelines. jspassgen rejects arbitrary composition rules (such as mandatory special character combinations) in favor of increased length and verified entropy density.

3. **Memory-Hard Key Derivation**: To neutralize parallel ASIC and GPU brute-force attacks, key derivation utilizes Argon2id as specified in [RFC 9106](https://www.rfc-editor.org/rfc/rfc9106.html) combined with HKDF key expansion as defined in [RFC 5869](https://www.rfc-editor.org/rfc/rfc5869.html).

4. **Breach Detection via Honeywords**: Decoy honeyword generation implements the honeyword canary framework established by Ari Juels and Ronald L. Rivest in *"Honeywords: Making password-cracking detectable"*, ACM SIGSAC Conference on Computer and Communications Security (CCS '13), [doi:10.1145/2508859.2516671](https://doi.org/10.1145/2508859.2516671).

5. **Passphrase Memorability**: Passphrase generation utilizes the curated 7,776-wordlist published by the [Electronic Frontier Foundation (EFF)](https://www.eff.org/dice), offering approximately 12.9 bits of entropy per selected word.

## Architecture Principles

- **Zero External Dependencies**: The core generator library contains zero third-party packages, eliminating software supply chain vectors.
- **Strict Local Isolation**: Secrets never traverse network sockets. All entropy is sourced directly from hardware CSPRNG interfaces (`window.crypto.getRandomValues` in browsers, `crypto.randomBytes` in Node.js).
- **Post-Quantum Bounds**: Symmetric entropy thresholds of 256 bits guarantee a minimum of 128 bits of security under Grover's quantum search algorithm.

## Author and Maintainer

Created and maintained by [Sebastien Rousseau](https://sebastienrousseau.com/), Security Engineer and Systems Architect.

- **GitHub**: [github.com/sebastienrousseau](https://github.com/sebastienrousseau)
- **LinkedIn**: [linkedin.com/in/sebastienrousseau](https://www.linkedin.com/in/sebastienrousseau/)
- **ORCID**: [0000-0002-0487-1478](https://orcid.org/0000-0002-0487-1478)
- **Wikidata**: [Q110298075](https://wikidata.org/wiki/Q110298075)

Dual licensed under [Apache-2.0](https://github.com/sebastienrousseau/jspassgen/blob/main/LICENSE-APACHE) and [MIT](https://github.com/sebastienrousseau/jspassgen/blob/main/LICENSE-MIT).
