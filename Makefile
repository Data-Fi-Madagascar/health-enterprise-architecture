# Build PDF consolidés + release GitHub
# Prérequis : pandoc + un moteur LaTeX (xelatex ou tectonic) + DejaVu Sans.
#   brew install pandoc tectonic font-dejavu  # Linux: sudo apt install pandoc texlive-xetex fonts-dejavu-core
#
# Usage:
#   make pdf                # 5 PDF dans dist/ (version 0.0.1 par défaut)
#   make pdf VERSION=1.2.3  # avec version précise
#   make clean            # supprime dist/

SHELL := /bin/bash
VERSION ?= 0.0.1
ENGINE ?= $(shell command -v tectonic >/dev/null && echo tectonic || echo xelatex)
FONT  ?= DejaVu Sans
PY    := python3
DATE  := $(shell date +%F)

export TAG_VERSION=$(VERSION)

.PHONY: pdf clean release note

pdf:
	@echo "==> Génération des 5 PDF (version $(VERSION), moteur $(ENGINE))"
	$(PY) scripts/build_pdf.py --version $(VERSION) --engine $(ENGINE) --font "$(FONT)"

clean:
	rm -rf dist

# Affiche les notes de release prêtes à coller
note:
	@git log --oneline $(shell git describe --abbrev=0 --tags 2>/dev/null || echo HEAD~1)..HEAD -- . ':(exclude)dist' | sed 's/^/  * /'

release: pdf
	@echo "==> Release GitHub v$(VERSION)"
	gh release create v$(VERSION) \
		dist/*-v$(VERSION).pdf \
		--title "v$(VERSION) — Santé numérique de Madagascar" \
		--notes "Documentation as code consolidée (CAESN / CNISN / ARTSN / PTISN)."