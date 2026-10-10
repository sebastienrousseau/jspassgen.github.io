---
name: "jspassgen"
title: "About jspassgen | Security Architecture and Principles"
description: "Learn about the cryptographic principles, hexagonal architecture, and design philosophy behind jspassgen."
author: "Sebastien Rousseau"
date: "2026-10-10"
layout: "page"
language: "en-GB"
theme_color: "#10b981"
theme_colour: "#10b981"
---

# About jspassgen

jspassgen was created to solve a persistent vulnerability in modern authentication workflows: the reliance on proprietary, cloud-hosted, and telemetry-heavy password generators.

## Design Principles

1. **Zero External Dependencies**: The core generator library contains zero third-party packages, preventing software supply chain compromises.
2. **Local Trust Boundary**: Passwords never touch a network socket. All entropy is derived from hardware noise via operating system CSPRNG interfaces.
3. **NIST SP 800-63B Compliance**: Full adherence to modern digital identity guidelines, discouraging arbitrary composition rules in favour of length and entropy.
4. **Post-Quantum Preparedness**: Hardened key derivation primitives designed to resist future quantum acceleration.

## Author & Maintainer

Created and maintained by [Sebastien Rousseau](https://sebastienrousseau.com/). Dual licensed under Apache-2.0 and MIT.
