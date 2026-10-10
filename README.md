# jspassgen.github.io

Official website and interactive portal for **jspassgen** (https://jspassgen.com).

## Overview

jspassgen is an open-source, zero-dependency password and EFF Diceware passphrase generator with Shannon entropy scoring, post-quantum KDF resistance, and Juels-Rivest honeyword canary decoys.

This website is compiled using [Static Site Generator (Rust)](https://github.com/sebastienrousseau/static-site-generator).

## Compilation

Build the website locally:

```bash
/Users/seb/Code/Public/Rust/static-site-generator/target/release/ssg build -f ssg.toml
```

## Features

- **Interactive Generator**: 100% offline WebCrypto API implementation.
- **Deep Market Comparison**: Comprehensive technical benchmark against 1Password, Bitwarden, LastPass, Norton, Proton Pass, and Avast.
- **AI Agent Optimized**: Complete `llms.txt`, `llms-full.txt`, and `.well-known/agents.json` compliance.
- **Accessible & Fast**: Strict Content Security Policy, zero external tracker scripts, WCAG 2.2 AAA colour contrast.

## License

Dual licensed under Apache-2.0 and MIT.
Copyright © 2026 [Sebastien Rousseau](https://sebastienrousseau.com/).
