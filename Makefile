# Build DOCX consolidés + release GitHub
# Prérequis : pandoc
#   brew install pandoc  # Linux: sudo apt install pandoc
#
# Usage:
#   make venv               # crée l'environnement virtuel + requirements.txt
#   make docx               # 5 DOCX dans dist/ (version 0.0.1 par défaut)
#   make docx VERSION=1.2.3 # avec version précise
#   make pdf                # 5 PDF dans dist/ (optionnel, nécessite LaTeX)
#   make wrappers           # régénère les 51 enveloppes (transclusion des 150 objets)
#   make rdf                # compilation RDF/OWL + validation SHACL
#   make sync               # synchronisation bidirectionnelle RDF ↔ Graphify
#   make check              # idempotence des enveloppes + 0 lien relatif cassé + RDF/SHACL
#   make clean              # supprime dist/
#
# Release :
#   git tag v0.0.2 && git push origin v0.0.2
#   → l'action GitHub génère les DOCX et crée la release

SHELL := /bin/bash
VERSION ?= 0.0.1
ENGINE ?= $(shell command -v tectonic >/dev/null && echo tectonic || echo xelatex)
FONT  ?= DejaVu Sans
# RDF/SHACL et sync requièrent rdflib + pyshacl (voir requirements.txt).
# Par défaut on utilise l'interpréteur du .venv s'il existe, sinon python3 système.
PY    := $(shell [ -x .venv/bin/python ] && echo .venv/bin/python || echo python3)
DATE  := $(shell date +%F)

export TAG_VERSION=$(VERSION)

.PHONY: pdf docx public wrappers check clean release note validate rdf sync jsonschema fhir openapi oda venv

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

# Garde-fou : enveloppes à jour (A1/A4) + 0 lien relatif cassé (A2) + graphe de
# relations sans îlot ni cible non résolue (validate_ref.py) + RDF/SHACL validé.
# Lecture seule : ne régénère pas, pour détecter toute édition d'un bloc généré.
check:
	$(PY) scripts/build_wrappers.py --check
	$(PY) scripts/check_links.py
	$(PY) scripts/validate_ref.py
	$(PY) scripts/compile_rdf.py
	$(PY) scripts/compile_rdf.py --validate
	$(PY) scripts/compilers/compile_jsonschema.py --validate
	$(PY) scripts/compilers/compile_fhir.py --validate
	$(PY) scripts/compilers/compile_openapi.py --validate
	$(PY) scripts/sync_rdf_graphify.py --check

clean:
	rm -rf dist

# Compilation RDF : transforme le référentiel YAML/Markdown en graphe Turtle RDF/OWL
rdf:
	@echo "==> Compilation RDF (YAML → Turtle)"
	$(PY) scripts/compile_rdf.py
	@echo "==> Validation SHACL"
	$(PY) scripts/compile_rdf.py --validate

# Synchronisation bidirectionnelle RDF ↔ Graphify :
# enrichit graphify-out/graph.json avec les métadonnées RDF (rdf_type, rdf_status, ...)
# et dist/hea-enriched.ttl avec les communautés/centralité issues de Graphify.
# Génère aussi graphify-out/COHERENCE_REPORT.md
sync:
	@echo "==> Sync RDF ↔ Graphify"
	$(PY) scripts/sync_rdf_graphify.py

# Validation du graphe de relations du référentiel (îlots, cibles non résolues,
# liens relatifs cassés). Indépendant de build_wrappers --check (voir note ci-dessous).
validate:
	$(PY) scripts/validate_ref.py

# Compilation JSON Schema : transforme les objets de données en schémas JSON vDraft-07
jsonschema:
	@echo "==> Compilation JSON Schema (DO → JSON Schema vDraft-07)"
	$(PY) scripts/compilers/compile_jsonschema.py --validate

# Compilation FHIR R4 : génère CodeSystem, ValueSet et StructureDefinition
fhir:
	@echo "==> Compilation FHIR R4 (DO → StructureDefinition, CodeSystem, ValueSet)"
	$(PY) scripts/compilers/compile_fhir.py --validate

# Compilation OpenAPI 3.0 : génère les spécifications API pour les profils
openapi:
	@echo "==> Compilation OpenAPI 3.0 (PT → OpenAPI specs)"
	$(PY) scripts/compilers/compile_openapi.py --validate

# Compilation ODA complète : tous les compilateurs en séquence puis sync Graphify
oda: rdf jsonschema fhir openapi sync
	@echo "==> Compilation ODA complète terminée"

# Création de l'environnement virtuel local (réutilisé par make check / make rdf)
venv:
	@if [ ! -d .venv ]; then \
		echo "==> Création de .venv" ; \
		uv venv .venv --python python3 ; \
		.venv/bin/pip install -r requirements.txt -q ; \
	else \
		echo "==> .venv déjà présent" ; \
	fi

# NOTE : `build_wrappers.py --check` présente un décalage préexistant (générateur
# émet « — » dans les titres générés alors que les enveloppes committées utilisent
# « : »). Ce décalage est antérieur à la présente session et ne concerne pas les
# correctifs HEA. Pour le résorber : `make wrappers` régénère les ~57 enveloppes.

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