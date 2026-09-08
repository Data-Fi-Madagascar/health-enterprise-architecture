# Build DOCX consolidés + release GitHub
# Prérequis : pandoc
#   brew install pandoc  # Linux: sudo apt install pandoc
#
# Usage:
#   make venv               # crée l'environnement virtuel + requirements.txt
#   make docx               # 5 DOCX dans dist/ (version 0.0.1 par défaut)
#   make docx VERSION=1.2.3 # avec version précise
#   make pdf                # 5 PDF dans dist/ (optionnel, nécessite LaTeX)
#   make wrappers           # régénère les 101 enveloppes du référentiel
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

.PHONY: pdf docx public wrappers ref-index check clean release note validate rdf sync jsonschema fhir openapi nomenclatures oda mintlify venv

pdf:
	@echo "==> Génération des 5 PDF (version $(VERSION), moteur $(ENGINE))"
	$(PY) scripts/build_pdf.py --version $(VERSION) --engine $(ENGINE) --font "$(FONT)"

docx:
	@echo "==> Génération des 5 DOCX (version $(VERSION))"
	$(PY) scripts/build_docx.py --version $(VERSION)

public:
	@echo "==> Génération des 3 DOCX publics + HEA-public (version $(VERSION))"
	$(PY) scripts/build_docx_public.py --version $(VERSION)

# Transclusion des objets du référentiel dans les enveloppes publiées
wrappers:
	@echo "==> Régénération des enveloppes (transclusion des objets)"
	$(PY) scripts/build_wrappers.py

ref-index:
	@echo "==> Régénération de referentiel/_index.yaml"
	$(PY) scripts/build_ref_index.py

# Garde-fou : enveloppes à jour (A1/A4) + 0 lien relatif cassé (A2) + graphe de
# relations sans îlot ni cible non résolue (validate_ref.py) + artefacts validés.
# Lecture seule : ne régénère pas, pour détecter toute édition d'un bloc généré.
check:
	$(PY) scripts/build_ref_index.py --check
	$(PY) scripts/build_wrappers.py --check
	$(PY) scripts/check_links.py
	$(PY) scripts/check_manifests.py
	$(PY) scripts/validate_ref.py
	@tmp=$$(mktemp -d); \
		set -e; \
		trap 'rm -rf "$$tmp"' EXIT; \
		$(PY) scripts/compile_rdf.py --validate --output "$$tmp/hea.ttl"; \
		$(PY) scripts/compilers/compile_fhir.py --validate --output "$$tmp/fhir"; \
		$(PY) scripts/sync_rdf_graphify.py --check --rdf "$$tmp/hea.ttl"
	$(PY) scripts/compilers/compile_jsonschema.py --check
	$(PY) scripts/compilers/compile_openapi.py --check
	$(PY) scripts/compilers/compile_oda.py --check
	$(PY) scripts/compilers/compile_oda.py --check-governance
	$(PY) scripts/build_mintlify.py --check

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

# Compilation JSON Schema : source unique des payloads des objets de données (DO → 03_ptisn/schemas/payloads/)
jsonschema:
	@echo "==> Compilation JSON Schema (DO → payloads dans 03_ptisn/schemas/payloads/)"
	$(PY) scripts/compilers/compile_jsonschema.py --validate

# Compilation FHIR R4 : génère CodeSystem, ValueSet et StructureDefinition
fhir:
	@echo "==> Compilation FHIR R4 (DO → StructureDefinition, CodeSystem, ValueSet)"
	$(PY) scripts/compilers/compile_fhir.py --validate

# Compilation OpenAPI 3.0 : génère les spécifications API pour les profils
openapi:
	@echo "==> Compilation OpenAPI 3.0 (PT → OpenAPI specs)"
	$(PY) scripts/compilers/compile_openapi.py --validate

mintlify:
	@echo "==> Génération du site Mintlify"
	$(PY) scripts/build_mintlify.py

# Compilation ODA complète : nomenclatures (payload + CodeSystem FHIR) puis sync Graphify.
# Les payloads des objets de données sont produits par la dépendance `jsonschema`.
nomenclatures:
	@echo "==> Compilation des nomenclatures ODA"
	$(PY) scripts/compilers/compile_oda.py --validate

oda: rdf jsonschema fhir openapi nomenclatures sync
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
