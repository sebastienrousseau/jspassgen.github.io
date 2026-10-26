<!-- SPDX-License-Identifier: Apache-2.0 OR MIT -->

# AGENTS.md: jspassgen.github.io

This repository is the source of <https://jspassgen.com>, the website for
[jspassgen](https://github.com/sebastienrousseau/jspassgen), built with
Static Site Generator (ssg) and the Prism theme. Its value is accuracy:
every statement about jspassgen must come from the jspassgen repository or
the npm registry.

## Rules

- Content lives in `_posts/`, layouts in `_layouts/`. `docs/` is build
  output: never edit or commit it.
- Facts about jspassgen come from its source, README, CHANGELOG and
  SECURITY.md (default branch `master`), or from the npm registry. Leave
  out anything you cannot check.
- Colours are tokens in `_layouts/styles.css`; `scripts/contrast.py`
  holds text to 7:1 and UI to 3:1 in light and dark mode.
- No em dashes. Copyright lines naming Sebastien Rousseau link the name
  to <https://sebastienrousseau.com/>.

## The one command

```bash
make build
```

It runs the contrast check, `ssg build`, heading anchors, post-build checks
(canonical URLs, sitemap, fragments, SRI, ssg's quality gate at 10/10),
the social images and `ssg audit`. CI runs the same target.

## Leave alone

`LICENSE-*`, `LICENSES/` and the theme files that `LICENSES/README.md`
lists as Prism's.
