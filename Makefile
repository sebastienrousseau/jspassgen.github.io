SSG ?= $(shell command -v ssg 2>/dev/null || echo /Users/seb/Code/Public/Rust/static-site-generator/target/release/ssg)

.PHONY: all build clean check

all: build

build:
	$(SSG) build -f ssg.toml
	@mkdir -p docs/images docs/assets docs/.well-known
	@cp -f CNAME docs/CNAME 2>/dev/null || true
	@cp -f .nojekyll docs/.nojekyll 2>/dev/null || true
	@cp -rf images/* docs/images/ 2>/dev/null || true
	@cp -f assets/logo.svg docs/assets/logo.svg 2>/dev/null || true
	@cp -f favicon.svg docs/favicon.svg 2>/dev/null || true
	@cp -f llms.txt docs/llms.txt 2>/dev/null || true
	@cp -f llms-full.txt docs/llms-full.txt 2>/dev/null || true
	@cp -f openapi.json docs/openapi.json 2>/dev/null || true
	@cp -f .well-known/agents.json docs/.well-known/agents.json 2>/dev/null || true
	@cp -f .well-known/security.txt docs/.well-known/security.txt 2>/dev/null || true
	@cp -f robots.txt docs/robots.txt 2>/dev/null || true
	@sed -i '' 's/"theme_color": null/"theme_color": "#2455e8"/g' docs/manifest.json docs/*/manifest.json 2>/dev/null || true
	@python3 scripts/clean_sitemaps.py

check:
	$(SSG) check -f ssg.toml

clean:
	rm -rf docs/*.html docs/sitemap.xml docs/manifest.json
