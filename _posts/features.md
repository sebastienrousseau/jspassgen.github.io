---
name: "jspassgen"
short_name: "jspassgen"
title: "Features: password types, presets, entropy estimates and honeywords | jspassgen"
description: "What jspassgen does: eight password types, six presets, an entropy estimate for every result, honeyword decoy sets, bulk output as JSON, CSV or YAML, and a dependency-free core."
keywords: "jspassgen features, password types, EFF diceware, honeywords, entropy, presets, json csv yaml"
author: "Sebastien Rousseau"
date: "2026-10-26"
news_publication_date: "2026-10-26"
layout: "page"
language: "en-GB"
schema: "page"
changefreq: "monthly"
eyebrow: "Features"
headline: "What jspassgen does, and where it stops"
lead: "Each section says what the feature is, how to use it and what it does not cover."
nav_features: "true"
---
## Eight password types

**Choose the type with `-t`.** Every type draws from the same random source;
they differ in what they draw.

| Type | What you get | Example |
| :--- | :--- | :--- |
| `strong` | Chunks of random characters from a 64-character alphabet: `A-Z`, `a-z`, `0-9`, `+` and `/` | `-t strong -l 16 -i 3 -s -` |
| `base64` | The same 64-character alphabet, for tokens and API secrets | `-t base64 -l 32 -i 1 -s -` |
| `memorable` | Words from the EFF large word list | `-t memorable -i 4 -s -` |
| `diceware` | Words from the same EFF list, six by default in its preset | `-p diceware` |
| `quantum-resistant` | Characters from the 64-character alphabet, with a warning below 256 bits | `-p quantum` |
| `pronounceable` | Consonant-vowel-vowel-consonant syllables | `-p pronounceable` |
| `custom` | Characters from named sets or literal characters you choose | `-t custom --allowed-chars "UPPERCASE,DIGITS" -l 16 -i 1 -s -` |
| `honeyword` | A set of passwords with one real one and the rest decoys | `-t honeyword -l 12 -i 4 -s -` |

`-l` sets the length of each chunk, `-i` the number of chunks, words or
syllables, and `-s` the separator between them. The named sets for
`--allowed-chars` are `UPPERCASE`, `LOWERCASE`, `DIGITS`, `SPECIAL`,
`HEX_UPPERCASE` and `HEX_LOWERCASE`; `--forbidden-chars` removes characters,
for example look-alikes such as `0O1I`.

The quantum-resistant type is named for its size, not for a different
algorithm: it uses the same alphabet as `strong`, and warns when the result
would carry fewer than 256 bits. Its preset uses 43 characters, which is
258 bits.

## Presets

**A preset sets the type, length, count and separator in one flag.**

| Preset | Type | Shape |
| :--- | :--- | :--- |
| `-p quick` | `strong` | Four chunks of 14 characters, joined by `-` |
| `-p secure` | `strong` | Four chunks of 16 characters, no separator |
| `-p memorable` | `memorable` | Four words, joined by `-` |
| `-p diceware` | `diceware` | Six words, joined by `-` |
| `-p quantum` | `quantum-resistant` | One chunk of 43 characters |
| `-p pronounceable` | `pronounceable` | Three syllables, joined by `-` |

Add `--learn` to a preset to print the explicit flags it stands for, so you
can adjust them.

## An entropy estimate for every result

**jspassgen prints the entropy of each password in bits, with a strength
rating.** The figure is computed from the generator's parameters: the
number of bits per choice (log2 of the alphabet or word-list size) times the
number of choices. A character from the 64-character alphabet is 6 bits, and
a word from the 7,776-word EFF list is about 12.9 bits, so four words are
about 52 bits.

This measures how the password was made, not how it looks: it assumes an
attacker knows the type and settings, and it is only as good as the random
source behind it.

## Honeywords

**`-t honeyword` generates a set of look-alike passwords, one of them
real.** `-i` sets the size of the set, at least two; `--reveal` marks which
one is real:

```text
honeyword decoy set
total: 4 (1 real, 3 decoys)

 1. 95K9gt7AaOuT [DECOY]
 2. HVCSHe7GCsi7 [REAL]
 3. fRlbyKsy8Hmf [DECOY]
 4. wNX655fozqia [DECOY]
```

Honeywords are the technique Ari Juels and Ronald L. Rivest described in
2013: a server stores the decoys alongside the real password, and a login
with a decoy shows that the password database has been stolen. jspassgen
generates the set; detecting the login is up to the system that stores it.

## Bulk output in JSON, CSV and YAML

**`-n` generates several passwords at once and `-f` picks the format:**
`text`, `json`, `csv` or `yaml`. Each record carries the password, its
type, length, count, separator and strength:

```bash
jspassgen -p quick -n 10 -f csv
```

## Cryptographic random source

**Every character and word comes from Node.js `crypto`.** The Node.js
adapter uses `crypto.randomBytes` and `crypto.randomInt`. When the alphabet
size does not divide 256, it discards bytes above the largest multiple of
the alphabet size, a technique called rejection sampling, so that no
character is more likely than another. The browser adapter uses the Web
Crypto API, `crypto.getRandomValues`.

## A dependency-free core

**The generators live in `packages/core`, which has no dependencies.** It
receives its random source, word list, clock, logger and storage as
parameters ("ports"), so the same generator code runs behind the
command-line tool and in the browser. A CI job checks that the core
imports no Node.js built-in module and no outside package. The published package itself depends on
`chalk`, `clipboardy` and `commander` for the command line.

## Clipboard copy

**`-c` copies the password to the clipboard** instead of only printing
it, using `clipboardy`. If no clipboard is available, jspassgen prints a
warning and still prints the password.

## Interactive mode

**`--interactive` walks you through the choices** in the terminal and
generates the password at the end. Run with no flags in a terminal, it
offers the same guided setup.
