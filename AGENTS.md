# AGENTS.md : jspassgen.github.io

Guidelines for AI agents and human contributors working on `jspassgen.github.io` (https://jspassgen.com).

## Core Invariants
- This repository is the official static website for jspassgen.
- Built strictly using Static Site Generator (Rust) at `/Users/seb/Code/Public/Rust/static-site-generator/target/release/ssg`.
- Output directory is `docs/` for GitHub Pages.
- CNAME is `jspassgen.com`.
- No em dashes in documentation or descriptions.
- All copyright lines naming Sebastien Rousseau link to `https://sebastienrousseau.com/`.

## Build & Validation
- Compile site: `/Users/seb/Code/Public/Rust/static-site-generator/target/release/ssg build -f ssg.toml`
- Validate output: verify `docs/index.html` exists and conforms to WCAG 2.2 AAA.
