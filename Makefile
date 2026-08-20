# Build DOCX consolidés + release GitHub
# Prérequis : pandoc
#   brew install pandoc  # Linux: sudo apt install pandoc
#
# Usage:
#   make docx               # 5 DOCX dans dist/ (version 0.0.1 par défaut)
#   make docx VERSION=1.2.3 # avec version précise
#   make pdf                # 5 PDF dans dist/ (optionnel, nécessite LaTeX)
#   make wrappers           # régénère les 51 enveloppes (transclusion des 150 objets)
#   make check              # idempotence des enveloppes + 0 lien relatif cassé
#   make clean              # supprime dist/
#
# Release :
#   git tag v0.0.2 && git push origin v0.0.2
#   → l'action GitHub génère les DOCX et crée la release

SHELL := /bin/bash
VERSION ?= 0.0.1
ENGINE ?= $(shell command -v tectonic >/dev/null && echo tectonic || echo xelatex)
FONT  ?= DejaVu Sans
PY    := python3
DATE  := $(shell date +%F)

export TAG_VERSION=$(VERSION)

.PHONY: pdf docx public wrappers check clean release note

pdf:
	@echo "==> Génération des 5 PDF (version $(VERSION), moteur $(ENGINE))"
	$(PY) scripts/build_pdf.py --version $(VERSION) --engine $(ENGINE) --font "$(FONT)"

docx:
	@echo "==> Génération des 5 DOCX (version $(VERSION))"
	$(PY) scripts/build_docx.py --version $(VERSION)

public:
	@echo "==> Génération des 3 DOCX publics + HEA-public (version $(VERSION))"
	$(PY) scripts/build_docx_public.py --version $(VERSION)

# Transclusion des 150 objets du référentiel dans les 51 enveloppes
wrappers:
	@echo "==> Régénération des enveloppes (transclusion des objets)"
	$(PY) scripts/build_wrappers.py

# Garde-fou : enveloppes à jour (A1/A4) + 0 lien relatif cassé (A2).
# Lecture seule : ne régénère pas, pour détecter toute édition d'un bloc généré.
check:
	$(PY) scripts/build_wrappers.py --check
	$(PY) scripts/check_links.py

clean:
	rm -rf dist

# Affiche les notes de release prêtes à coller
note:
	@git log --oneline $(shell git describe --abbrev=0 --tags 2>/dev/null || echo HEAD~1)..HEAD -- . ':(exclude)dist' | sed 's/^/  * /'

release: docx public
	@echo "==> Release GitHub v$(VERSION)"
	gh release create v$(VERSION) \
		dist/*-v$(VERSION).docx \
		dist/public/*-v$(VERSION).docx \
		--title "v$(VERSION) — Santé numérique de Madagascar" \
		--notes "Documentation as code consolidée (CAESN / CNISN / ARTSN / PTISN) + versions publiques pour décideurs/PTF."