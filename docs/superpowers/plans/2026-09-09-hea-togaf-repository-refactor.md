# HEA TOGAF Repository Refactor Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Refactor the HEA architecture repository so the structured source of truth is explicitly aligned with TOGAF 10, while removing `CAP-INT-*` as an active object type and preserving traceability through replacement objects.

**Architecture:** Keep `00_caesn/`, `01_cnisn/`, `02_artsn/` and `03_ptisn/` at repository root as the HEA Architecture Landscape and Solutions Landscape. Rename `referentiel/` to `04_architecture-repository/`, then reorganize the structured objects by TOGAF repository section: metamodel, partitions, architecture elements, requirements, patterns, building blocks, governance, migration, views and baselines. Treat `CAP-INT-*` as composite CNISN migration bundles that are decomposed into `PART-*`, `REQ-*`, `PAT-*`, `ABB-*`, governance objects and architecture elements.

**Tech Stack:** Markdown with YAML frontmatter, Python 3 standard-library scripts, generated wrapper blocks, YAML indexes, JSON/OpenAPI/FHIR generators, git.

**Spec:** `docs/superpowers/specs/2026-09-09-hea-togaf-repository-refactor-design.md`

## Global Constraints

- Work on a non-main branch. Current branch should remain `codex/apply-audit-recommendations` unless the user asks for a different branch.
- Do not include unrelated existing changes. `.gitignore` currently has a pre-existing modification and must remain excluded unless the user explicitly asks to include it.
- Keep `00_caesn/`, `01_cnisn/`, `02_artsn/` and `03_ptisn/` at repository root.
- Rename `referentiel/` to `04_architecture-repository/` in one physical pass.
- After the rename, no active source file, wrapper marker, script constant or active Markdown link may point to `referentiel/`.
- `CAP-*` remains the only canonical capability family. `CAP-INT-*` is allowed only in `legacy_id` fields and migration correspondence files.
- Active status vocabulary remains `draft`, `active`, `stable`, `candidate`, `deprecated`.
- Declination IDs remain uppercase in content and frontmatter, with lowercase filenames where the current convention requires it.
- Do not edit generated wrapper content manually. Edit source objects or wrapper markers, then run `python3 scripts/build_wrappers.py`.
- Regenerate wrappers after changing architecture source objects.
- Regenerate `04_architecture-repository/_index.yaml` with `python3 scripts/build_ref_index.py`; never edit it manually.
- Exclude `graphify-out/` and `.obsidian/` from commits.
- Required checks before final handoff: `python3 scripts/validate_ref.py`, `python3 scripts/build_ref_index.py --check`, `python3 scripts/build_wrappers.py --check`, and `make check` if available and not blocked by missing local dependencies.

---

## Execution Decisions Locked By This Plan

This plan resolves the two open decisions from the design document:

| Decision | Chosen execution |
|----------|------------------|
| `CMP-*`, `SRV-*`, `PT-*` migration scope | First pass creates the ABB/SBB structure and only creates new `ABB-*` objects derived from `CAP-INT-*`. Existing `CMP-*`, `SRV-*` and `PT-*` are moved into their TOGAF-aligned folders but keep their IDs until a second, focused identifier migration. |
| `CAP-INT-*` correspondence format | Create both `04_architecture-repository/00_metamodel/cap-int-migration.yaml` and `04_architecture-repository/08_views/togaf/cap-int-migration.md`. |

This plan also closes one structural gap found before execution: existing `parties-prenantes`, `principes`, `valeurs` and `lieux` must receive explicit target locations. They are not left as residual folders.

## Target Placement Map

| Current source | Target source |
|----------------|---------------|
| `referentiel/_schema.md` | `04_architecture-repository/00_metamodel/schema.md` |
| `referentiel/_index.yaml` | `04_architecture-repository/_index.yaml` |
| `referentiel/flux-valeur/` | `04_architecture-repository/02_architecture-elements/strategy/value-streams/` |
| `referentiel/etapes-valeur/` | `04_architecture-repository/02_architecture-elements/strategy/value-stages/` |
| `referentiel/capabilites/` | `04_architecture-repository/02_architecture-elements/strategy/capabilities/` |
| `referentiel/valeurs/` | `04_architecture-repository/02_architecture-elements/motivation/values/` |
| `referentiel/principes/` | `04_architecture-repository/02_architecture-elements/motivation/principles/` |
| `referentiel/parties-prenantes/` | `04_architecture-repository/02_architecture-elements/motivation/stakeholders/` |
| `referentiel/acteurs/` | `04_architecture-repository/02_architecture-elements/business/actors/` |
| `referentiel/roles/` | `04_architecture-repository/02_architecture-elements/business/roles/` |
| `referentiel/processus/` | `04_architecture-repository/02_architecture-elements/business/processes/` |
| `referentiel/lieux/` | `04_architecture-repository/02_architecture-elements/business/locations/` |
| `referentiel/objets-metier/` | `04_architecture-repository/02_architecture-elements/business/business-objects/` |
| `referentiel/objets-de-donnees/` | `04_architecture-repository/02_architecture-elements/data/data-objects/` |
| `referentiel/exigences/` | `04_architecture-repository/03_requirements/` |
| `referentiel/fondations/` | `04_architecture-repository/04_patterns/foundations/` |
| `referentiel/chapitres/` | `04_architecture-repository/04_patterns/artsn-rules/` |
| `referentiel/composants/` with `type: composant-applicatif`, `composant-infrastructure` or `composant-securite` | `04_architecture-repository/05_building-blocks/abb/legacy-components/` |
| `referentiel/services/` with `categorie: applicatif` or `technologique` | `04_architecture-repository/05_building-blocks/abb/legacy-services/` |
| `referentiel/services/` with `categorie: business` | `04_architecture-repository/02_architecture-elements/business/business-services/` |
| `referentiel/profils/` | `04_architecture-repository/05_building-blocks/sbb/legacy-profiles/` |
| `referentiel/composants/` with `type: registre-gouvernance` | `04_architecture-repository/06_governance/registers/` |
| `referentiel/work-packages/` | `04_architecture-repository/07_migration/work-packages/` |
| `referentiel/plateaux/` | `04_architecture-repository/07_migration/plateaux/` |
| `referentiel/gaps/` | `04_architecture-repository/07_migration/gaps/` |
| `referentiel/capacites/cap-int-*.md` | No target folder. These files are decomposed and then removed. |

## `CAP-INT-*` Primary Replacement Map

This map is used when a relation can only point to one replacement target. When the source text carries several meanings, add secondary links to the supporting objects listed in Task 6.

| Legacy ID | Primary replacement |
|-----------|---------------------|
| `CAP-INT-01` | `ABB-IDENTITE-BENEFICIAIRE` |
| `CAP-INT-02` | `ABB-REGISTRE-PROFESSIONNELS` |
| `CAP-INT-03` | `ABB-ECHANGE-MEDIATION` |
| `CAP-INT-04` | `ABB-REFERENTIEL-STRUCTURES-SERVICES` |
| `CAP-INT-05` | `ABB-SERVICE-TERMINOLOGIE` |
| `CAP-INT-06` | `ABB-CATALOGUE-CONTRATS` |
| `CAP-INT-07` | `ABB-EXPOSITION-DONNEES-ANALYTIQUES` |
| `CAP-INT-08` | `ABB-CONFIANCE-AUTORISATION` |
| `CAP-INT-09` | `ABB-GESTION-CONSENTEMENT` |
| `CAP-INT-10` | `ABB-AUDIT-PROVENANCE` |
| `CAP-INT-11` | `ABB-RECONCILIATION-DONNEES` |
| `CAP-INT-12` | `COMP-HOMOLOGATION-INTEROPERABILITE` |
| `CAP-INT-13` | `PART-ECHANGE-TRANSFRONTALIER` |
| `CAP-INT-14` | `PART-ONE-HEALTH` |
| `CAP-INT-15` | `ABB-ECHANGE-LOGISTIQUE-LMIS` |
| `CAP-INT-16` | `RD-DONNEES-ENVIRONNEMENTALES-CLIMAT` |

## Task 1: Baseline And Safety Snapshot

**Files:**
- Create: `docs/refactor-baseline/2026-09-09-hea-togaf-refactor-baseline.md`
- Read only: `docs/superpowers/specs/2026-09-09-hea-togaf-repository-refactor-design.md`
- Read only: `AGENTS.md`

**Interfaces:**
- Consumes: current repository state.
- Produces: a committed baseline with validation output, object count, wrapper count and old path inventory.

- [ ] **Step 1: Confirm branch and dirty state**

Run:

```bash
git branch --show-current
git status --short
```

Expected:

```text
codex/apply-audit-recommendations
 M .gitignore
 M docs/superpowers/specs/2026-09-09-hea-togaf-repository-refactor-design.md
```

If additional user-owned changes are present, record them in the baseline and do not include them in refactor commits unless they are directly required.

- [ ] **Step 2: Capture current object and wrapper state**

Run:

```bash
python3 scripts/validate_ref.py
python3 scripts/build_ref_index.py --check
python3 scripts/build_wrappers.py --check
rg -n "referentiel/|CAP-INT-[0-9]{2}" README.md AGENTS.md 00_caesn 01_cnisn 02_artsn 03_ptisn scripts
```

Expected:

```text
validate_ref.py reports Résumé : CONFORME
build_ref_index.py reports index à jour
build_wrappers.py reports OK
rg reports active references that will be migrated by later tasks
```

- [ ] **Step 3: Create the baseline document**

Create `docs/refactor-baseline/2026-09-09-hea-togaf-refactor-baseline.md` with this structure:

```markdown
# Baseline du refactor TOGAF HEA

## Contexte

Ce document capture l'état du dépôt avant le refactor `referentiel/` vers `04_architecture-repository/` et avant la suppression active des `CAP-INT-*`.

## Etat git

Coller la sortie de `git branch --show-current` et `git status --short`.

## Validation initiale

Coller la synthèse de `python3 scripts/validate_ref.py`, `python3 scripts/build_ref_index.py --check` et `python3 scripts/build_wrappers.py --check`.

## Inventaire des références actives

Coller la synthèse comptée des références `referentiel/` et `CAP-INT-*` dans `README.md`, `AGENTS.md`, `00_caesn/`, `01_cnisn/`, `02_artsn/`, `03_ptisn/` et `scripts/`.
```

- [ ] **Step 4: Commit baseline only**

Run:

```bash
git add docs/refactor-baseline/2026-09-09-hea-togaf-refactor-baseline.md
git commit -m "docs: capture HEA TOGAF refactor baseline"
```

## Task 2: Parameterize The Architecture Repository Root

**Files:**
- Modify: `scripts/build_ref_index.py`
- Modify: `scripts/build_wrappers.py`
- Modify: `scripts/validate_ref.py`
- Modify: `scripts/compile_rdf.py`
- Modify: `scripts/compilers/compile_jsonschema.py`
- Modify: `scripts/compilers/compile_fhir.py`
- Modify: `scripts/compilers/compile_oda.py`
- Modify: `scripts/compilers/compile_openapi.py`
- Modify: `scripts/audit/audit_conformite.py`
- Modify: `scripts/audit/audit_chaine.py`
- Modify: `scripts/audit/audit_couverture.py`
- Modify: `scripts/audit/fix_anomalies.py`
- Modify: `scripts/audit/fix_vs_links.py`

**Interfaces:**
- Consumes: current `referentiel/` root.
- Produces: scripts that use a single repository-root constant and can be switched to `04_architecture-repository/` in Task 3.

- [ ] **Step 1: Introduce a shared constant in each touched script**

Use this naming consistently:

```python
ARCH_REPOSITORY_DIR = "referentiel"
ARCH_REPOSITORY_ROOT = os.path.join(REPO_ROOT, ARCH_REPOSITORY_DIR)
```

For `pathlib` scripts, use:

```python
ARCH_REPOSITORY_DIR = "referentiel"
ARCH_REPOSITORY_ROOT = REPO_ROOT / ARCH_REPOSITORY_DIR
```

- [ ] **Step 2: Replace direct root literals**

Replace root constructions like:

```python
os.path.join(REPO_ROOT, "referentiel", "**", "*.md")
REPO_ROOT / "referentiel"
```

with:

```python
os.path.join(ARCH_REPOSITORY_ROOT, "**", "*.md")
ARCH_REPOSITORY_ROOT
```

Keep generated metadata strings as `referentiel/...` in this task. Those are migrated after the physical rename.

- [ ] **Step 3: Keep current behavior green**

Run:

```bash
python3 scripts/validate_ref.py
python3 scripts/build_ref_index.py --check
python3 scripts/build_wrappers.py --check
```

Expected:

```text
All three commands pass with the current `referentiel/` layout.
```

- [ ] **Step 4: Commit script root parameterization**

Run:

```bash
git add scripts/build_ref_index.py scripts/build_wrappers.py scripts/validate_ref.py scripts/compile_rdf.py scripts/compilers/compile_jsonschema.py scripts/compilers/compile_fhir.py scripts/compilers/compile_oda.py scripts/compilers/compile_openapi.py scripts/audit/audit_conformite.py scripts/audit/audit_chaine.py scripts/audit/audit_couverture.py scripts/audit/fix_anomalies.py scripts/audit/fix_vs_links.py
git commit -m "refactor: parameterize architecture repository root"
```

## Task 3: Rename `referentiel/` To `04_architecture-repository/`

**Files:**
- Move: `referentiel/` to `04_architecture-repository/`
- Modify: scripts from Task 2
- Modify: `README.md`
- Modify: `AGENTS.md`
- Modify: all active Markdown links and `BEGIN:GENERATED source=` markers under `00_caesn/`, `01_cnisn/`, `02_artsn/`, `03_ptisn/`
- Modify: generated schema metadata under `03_ptisn/schemas/`

**Interfaces:**
- Consumes: parameterized scripts from Task 2.
- Produces: a single active source root named `04_architecture-repository/`.

- [ ] **Step 1: Rename the source root with git**

Run:

```bash
git mv referentiel 04_architecture-repository
```

- [ ] **Step 2: Switch script constants**

Change every script-level constant from:

```python
ARCH_REPOSITORY_DIR = "referentiel"
```

to:

```python
ARCH_REPOSITORY_DIR = "04_architecture-repository"
```

For user-facing messages in scripts, replace `referentiel` with `04_architecture-repository`.

- [ ] **Step 3: Update active Markdown paths**

Replace active paths in `README.md`, `AGENTS.md`, `00_caesn/`, `01_cnisn/`, `02_artsn/`, `03_ptisn/`:

```text
referentiel/
```

with:

```text
04_architecture-repository/
```

Update relative links by path resolution, not by blind prefix replacement. Examples:

```text
../../referentiel/capabilites/cap-14.md
../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-14.md
```

```text
../referentiel/profils/pt-04.md
../04_architecture-repository/05_building-blocks/sbb/legacy-profiles/pt-04.md
```

- [ ] **Step 4: Update generated marker paths**

Change marker sources such as:

```markdown
<!-- BEGIN:GENERATED source=referentiel/principes/pa-*.md -->
```

to the final paths after Task 4 placement. If Task 4 has not yet moved the subfolder, use the temporary path under `04_architecture-repository/` and update it again in Task 4.

- [ ] **Step 5: Validate the simple rename**

Run:

```bash
python3 scripts/validate_ref.py
python3 scripts/build_ref_index.py
python3 scripts/build_wrappers.py
python3 scripts/build_ref_index.py --check
python3 scripts/build_wrappers.py --check
rg -n "referentiel/" README.md AGENTS.md 00_caesn 01_cnisn 02_artsn 03_ptisn scripts 04_architecture-repository
```

Expected:

```text
Validation passes.
Generated index and wrappers are up to date.
The `rg` command has no active reference to `referentiel/` outside historical docs under `docs/`.
```

- [ ] **Step 6: Commit physical rename**

Run:

```bash
git add README.md AGENTS.md 00_caesn 01_cnisn 02_artsn 03_ptisn scripts 03_ptisn/schemas 04_architecture-repository
git commit -m "refactor: rename architecture repository root"
```

## Task 4: Move Existing Objects Into TOGAF-Aligned Folders

**Files:**
- Move: all folders listed in Target Placement Map except `cap-int-*.md`
- Modify: `04_architecture-repository/00_metamodel/schema.md`
- Modify: `04_architecture-repository/_index.yaml` through generator
- Modify: generated wrapper markers under `00_caesn/`, `01_cnisn/`, `02_artsn/`, `03_ptisn/`
- Modify: Markdown links and frontmatter `envelope` fields in moved source files
- Modify: `scripts/build_ref_index.py`
- Modify: `scripts/build_wrappers.py`
- Modify: `scripts/validate_ref.py`

**Interfaces:**
- Consumes: `04_architecture-repository/` from Task 3.
- Produces: target TOGAF folders with all existing non-`CAP-INT` objects placed.

- [ ] **Step 1: Create target directories**

Run:

```bash
mkdir -p 04_architecture-repository/00_metamodel 04_architecture-repository/01_partitions/value-streams 04_architecture-repository/01_partitions/transverses 04_architecture-repository/01_partitions/sectorielles 04_architecture-repository/01_partitions/externes 04_architecture-repository/02_architecture-elements/motivation/stakeholders 04_architecture-repository/02_architecture-elements/motivation/principles 04_architecture-repository/02_architecture-elements/motivation/values 04_architecture-repository/02_architecture-elements/strategy/capabilities 04_architecture-repository/02_architecture-elements/strategy/value-streams 04_architecture-repository/02_architecture-elements/strategy/value-stages 04_architecture-repository/02_architecture-elements/business/actors 04_architecture-repository/02_architecture-elements/business/roles 04_architecture-repository/02_architecture-elements/business/functions 04_architecture-repository/02_architecture-elements/business/processes 04_architecture-repository/02_architecture-elements/business/locations 04_architecture-repository/02_architecture-elements/business/business-objects 04_architecture-repository/02_architecture-elements/business/business-services 04_architecture-repository/02_architecture-elements/data/data-objects 04_architecture-repository/02_architecture-elements/data/reference-data 04_architecture-repository/02_architecture-elements/data/terminologies 04_architecture-repository/03_requirements 04_architecture-repository/04_patterns/foundations 04_architecture-repository/04_patterns/artsn-rules 04_architecture-repository/05_building-blocks/abb/legacy-components 04_architecture-repository/05_building-blocks/abb/legacy-services 04_architecture-repository/05_building-blocks/sbb/legacy-profiles 04_architecture-repository/06_governance/registers 04_architecture-repository/06_governance/architecture-contracts 04_architecture-repository/06_governance/derogations 04_architecture-repository/06_governance/decisions 04_architecture-repository/06_governance/compliance 04_architecture-repository/06_governance/evidence 04_architecture-repository/07_migration/work-packages 04_architecture-repository/07_migration/plateaux 04_architecture-repository/07_migration/gaps 04_architecture-repository/08_views/togaf 04_architecture-repository/09_baselines
```

- [ ] **Step 2: Move files according to the placement map**

Use `git mv` for each source folder. Split `04_architecture-repository/composants/` by frontmatter `type`, and split `04_architecture-repository/services/` by `categorie`.

Exact service split:

```text
SRV-01 -> 02_architecture-elements/business/business-services/srv-01.md
SRV-02 -> 05_building-blocks/abb/legacy-services/srv-02.md
SRV-03 -> 05_building-blocks/abb/legacy-services/srv-03.md
SRV-04 -> 05_building-blocks/abb/legacy-services/srv-04.md
SRV-05 -> 05_building-blocks/abb/legacy-services/srv-05.md
SRV-06 -> 05_building-blocks/abb/legacy-services/srv-06.md
```

Exact governance component split:

```text
CMP-39 -> 06_governance/registers/cmp-39.md
CMP-40 -> 06_governance/registers/cmp-40.md
CMP-41 -> 06_governance/registers/cmp-41.md
CMP-42 -> 06_governance/registers/cmp-42.md
CMP-43 -> 06_governance/registers/cmp-43.md
CMP-44 -> 06_governance/registers/cmp-44.md
CMP-45 -> 06_governance/registers/cmp-45.md
CMP-46 -> 06_governance/registers/cmp-46.md
```

All other `CMP-*` files move to `05_building-blocks/abb/legacy-components/`.

- [ ] **Step 3: Update metamodel schema**

Move:

```bash
git mv 04_architecture-repository/_schema.md 04_architecture-repository/00_metamodel/schema.md
```

Edit `schema.md` so the type table reflects the target placement. Remove `capacite` as an active type and introduce these active target types:

```text
architecture-partition
architecture-building-block
solution-building-block
architecture-pattern
architecture-contract
compliance-rule
evidence
reference-data
terminology
stakeholder
business-location
business-value
```

Keep existing legacy type names during this first pass where IDs are not yet renamed: `composant-applicatif`, `composant-infrastructure`, `composant-securite`, `profil`, `service`, `registre-gouvernance`.

- [ ] **Step 4: Update scripts for new excluded metamodel files**

In `scripts/build_wrappers.py`, skip metamodel documentation files when loading source objects unless they are intended as graph objects. Exclude:

```text
04_architecture-repository/00_metamodel/schema.md
04_architecture-repository/00_metamodel/togaf-mapping.md
04_architecture-repository/00_metamodel/archimate-mapping.md
04_architecture-repository/00_metamodel/cap-int-migration.yaml
```

In `scripts/validate_ref.py`, skip the same metamodel documentation files for graph island detection.

In `scripts/build_ref_index.py`, include active object files and exclude metamodel documentation files. The generated `_index.yaml` must remain a compact inventory of architecture objects, not an index of explanatory documentation.

- [ ] **Step 5: Rewrite frontmatter `domain` and path relations**

For every moved Markdown source file:

```yaml
domain: <new immediate parent folder name including numeric prefix when applicable>
```

Update body links and frontmatter paths so every relative Markdown link resolves from the new location.

- [ ] **Step 6: Regenerate and validate**

Run:

```bash
python3 scripts/build_ref_index.py
python3 scripts/build_wrappers.py
python3 scripts/validate_ref.py
python3 scripts/build_ref_index.py --check
python3 scripts/build_wrappers.py --check
```

Expected:

```text
Index regenerated under 04_architecture-repository/_index.yaml.
Wrappers regenerated without empty generated blocks.
Validation reports CONFORME.
```

- [ ] **Step 7: Commit TOGAF placement**

Run:

```bash
git add 00_caesn 01_cnisn 02_artsn 03_ptisn scripts 04_architecture-repository
git commit -m "refactor: align architecture repository folders with TOGAF"
```

## Task 5: Create Partitions And TOGAF Views Skeleton

**Files:**
- Create: `04_architecture-repository/01_partitions/index.md`
- Create: `04_architecture-repository/01_partitions/value-streams/part-vs-01.md`
- Create: `04_architecture-repository/01_partitions/value-streams/part-vs-02.md`
- Create: `04_architecture-repository/01_partitions/value-streams/part-vs-03.md`
- Create: `04_architecture-repository/01_partitions/value-streams/part-vs-04.md`
- Create: `04_architecture-repository/01_partitions/transverses/part-transverse-interoperabilite.md`
- Create: `04_architecture-repository/01_partitions/transverses/part-transverse-identite.md`
- Create: `04_architecture-repository/01_partitions/transverses/part-transverse-securite-confiance.md`
- Create: `04_architecture-repository/01_partitions/transverses/part-transverse-donnees-referentielles.md`
- Create: `04_architecture-repository/01_partitions/transverses/part-transverse-analytics-pilotage.md`
- Create: `04_architecture-repository/01_partitions/sectorielles/part-one-health.md`
- Create: `04_architecture-repository/01_partitions/externes/part-echange-transfrontalier.md`
- Create: `04_architecture-repository/08_views/togaf/architecture-landscape.md`
- Create: `04_architecture-repository/08_views/togaf/standards-information-base.md`
- Create: `04_architecture-repository/08_views/togaf/reference-library.md`
- Create: `04_architecture-repository/08_views/togaf/governance-log.md`
- Create: `04_architecture-repository/08_views/togaf/requirements-repository.md`
- Create: `04_architecture-repository/08_views/togaf/solutions-landscape.md`
- Create: `04_architecture-repository/08_views/togaf/adm-traceability.md`

**Interfaces:**
- Consumes: moved strategy, business and data objects.
- Produces: explicit TOGAF partition objects and view envelopes.

- [ ] **Step 1: Create partition frontmatter**

Use this exact pattern for each partition file:

```yaml
---
domain: <immediate-parent-folder>
id: PART-VS-01
type: architecture-partition
niveau: "2"
title: Partition VS-01
status: draft
owner: DEPSI
version: "0.1"
partition_kind: value-stream
togaf_repository_section: architecture-landscape
togaf_adm_phase: B
architecture_level: segment
architecture_domain: business
architecture_scope: value-stream
architecture_state: target
applies_to: ["VS-01"]
related: []
tags: ["togaf", "partition", "value-stream"]
---
```

For transverse partitions, set `partition_kind` to `transverse`, `architecture_level` to `enterprise-transversal`, and `applies_to` to the four value-stream partitions:

```yaml
applies_to: ["PART-VS-01", "PART-VS-02", "PART-VS-03", "PART-VS-04"]
```

For `PART-ONE-HEALTH`, set:

```yaml
partition_kind: sectorielle
applies_to: ["CAP-18", "VS-02", "VS-04"]
```

For `PART-ECHANGE-TRANSFRONTALIER`, set:

```yaml
partition_kind: externe
applies_to: ["CAP-15", "CAP-18", "DO-29", "DO-30", "DO-31"]
```

- [ ] **Step 2: Create TOGAF view envelopes with generated markers**

Each view file must contain frontmatter, a short analytical introduction, and at least one generated table marker. Example for `requirements-repository.md`:

```markdown
<!-- BEGIN:GENERATED mode=table source=04_architecture-repository/03_requirements/*.md -->
<!-- END:GENERATED -->
```

Use these marker sources:

```text
architecture-landscape.md -> 04_architecture-repository/01_partitions/**/*.md,04_architecture-repository/02_architecture-elements/strategy/**/*.md
standards-information-base.md -> 01_cnisn/05_standards/*.md
reference-library.md -> 04_architecture-repository/04_patterns/**/*.md,04_architecture-repository/05_building-blocks/abb/**/*.md
governance-log.md -> 01_cnisn/06_decisions/*.md,04_architecture-repository/06_governance/**/*.md
requirements-repository.md -> 04_architecture-repository/03_requirements/*.md
solutions-landscape.md -> 04_architecture-repository/05_building-blocks/sbb/**/*.md,03_ptisn/schemas/**/*.json
adm-traceability.md -> 04_architecture-repository/**/*.md
```

If `build_wrappers.py` does not support `**` in generated source globs correctly, replace each recursive pattern with the concrete target directories used in this plan.

- [ ] **Step 3: Regenerate and validate**

Run:

```bash
python3 scripts/build_ref_index.py
python3 scripts/build_wrappers.py
python3 scripts/validate_ref.py
python3 scripts/build_ref_index.py --check
python3 scripts/build_wrappers.py --check
```

Expected:

```text
New partitions are indexed.
No partition is an unauthorized island.
Wrappers are current.
```

- [ ] **Step 4: Commit partitions and views**

Run:

```bash
git add 04_architecture-repository scripts
git commit -m "docs: add TOGAF partitions and repository views"
```

## Task 6: Decompose `CAP-INT-*` Into Target Objects

**Files:**
- Create: `04_architecture-repository/00_metamodel/cap-int-migration.yaml`
- Create: `04_architecture-repository/08_views/togaf/cap-int-migration.md`
- Create: `04_architecture-repository/05_building-blocks/abb/abb-identite-beneficiaire.md`
- Create: `04_architecture-repository/05_building-blocks/abb/abb-registre-professionnels.md`
- Create: `04_architecture-repository/05_building-blocks/abb/abb-echange-mediation.md`
- Create: `04_architecture-repository/05_building-blocks/abb/abb-referentiel-structures-services.md`
- Create: `04_architecture-repository/05_building-blocks/abb/abb-service-terminologie.md`
- Create: `04_architecture-repository/05_building-blocks/abb/abb-catalogue-contrats.md`
- Create: `04_architecture-repository/05_building-blocks/abb/abb-exposition-donnees-analytiques.md`
- Create: `04_architecture-repository/05_building-blocks/abb/abb-confiance-autorisation.md`
- Create: `04_architecture-repository/05_building-blocks/abb/abb-gestion-consentement.md`
- Create: `04_architecture-repository/05_building-blocks/abb/abb-audit-provenance.md`
- Create: `04_architecture-repository/05_building-blocks/abb/abb-reconciliation-donnees.md`
- Create: `04_architecture-repository/05_building-blocks/abb/abb-echange-logistique-lmis.md`
- Create: `04_architecture-repository/04_patterns/pat-echange-mediation.md`
- Create: `04_architecture-repository/04_patterns/pat-qualite-reconciliation.md`
- Create: `04_architecture-repository/04_patterns/pat-echange-international-ips.md`
- Create: `04_architecture-repository/02_architecture-elements/data/reference-data/rd-structures-services.md`
- Create: `04_architecture-repository/02_architecture-elements/data/reference-data/rd-donnees-environnementales-climat.md`
- Create: `04_architecture-repository/02_architecture-elements/data/terminologies/term-codification-commune.md`
- Create: `04_architecture-repository/06_governance/architecture-contracts/ac-catalogue-services.md`
- Create: `04_architecture-repository/06_governance/compliance/comp-homologation-interoperabilite.md`
- Create: `04_architecture-repository/06_governance/evidence/evid-tests-interoperabilite.md`
- Create: `04_architecture-repository/03_requirements/req-tf-01.md` through `req-tf-08.md`
- Create: `04_architecture-repository/03_requirements/req-oh-01.md` through `req-oh-07.md`
- Modify: `01_cnisn/02_capacites/index.md`

**Interfaces:**
- Consumes: the 16 files in `04_architecture-repository/capacites/cap-int-*.md`.
- Produces: replacement objects with `legacy_id`, new IDs and active links to CAESN capabilities.

- [ ] **Step 1: Create the machine-readable migration file**

Create `04_architecture-repository/00_metamodel/cap-int-migration.yaml` with one entry per legacy ID. Each entry must include:

```yaml
- legacy_id: "CAP-INT-01"
  legacy_title: "Résolution d'identité du bénéficiaire"
  disposition: "decomposed"
  primary_replacement: "ABB-IDENTITE-BENEFICIAIRE"
  replacement_ids: ["ABB-IDENTITE-BENEFICIAIRE", "PART-TRANSVERSE-IDENTITE"]
  caesn_capabilities: ["CAP-01", "CAP-02", "CAP-04", "CAP-07", "CAP-14", "CAP-17"]
```

Use the full Primary Replacement Map and add secondary replacement IDs from the file list in this task.

- [ ] **Step 2: Create the human-readable migration view**

Create `04_architecture-repository/08_views/togaf/cap-int-migration.md` with:

```markdown
# Migration des CAP-INT

Ce document explicite la suppression des `CAP-INT-*` comme type actif. Les anciennes fiches CNISN sont conservées en traçabilité par `legacy_id` et remplacées par des partitions, exigences, patterns, ABB, objets de gouvernance et éléments de données.

| Ancien ID | Remplacement principal | Remplacements secondaires | Capacités CAESN |
|-----------|------------------------|---------------------------|-----------------|
```

Fill all 16 rows from the YAML file.

- [ ] **Step 3: Create ABB replacement files**

Every `ABB-*` file must use this frontmatter pattern:

```yaml
---
domain: abb
id: ABB-ECHANGE-MEDIATION
type: architecture-building-block
niveau: "2"
title: Échange et médiation inter-systèmes
status: candidate
owner: DEPSI
version: "0.1"
legacy_id: CAP-INT-03
building_block_role: ABB
building_block_domain: application
togaf_repository_section: reference-library
togaf_adm_phase: C
architecture_level: enterprise-transversal
architecture_domain: application
architecture_scope: interoperability
architecture_state: target
partitions: ["PART-TRANSVERSE-INTEROPERABILITE"]
maps_to: ["CAP-13", "CAP-14", "CAP-18"]
implements: ["ART-1", "ART-2", "F.3"]
related: ["PAT-ECHANGE-MEDIATION"]
tags: ["cnisn", "abb", "interoperabilite"]
---
```

Set each file's body to preserve the useful `Finalité`, `Services attendus` and `Principes associés` content from its legacy `CAP-INT-*` source. Do not preserve the claim that it is a capability.

- [ ] **Step 4: Create pattern files**

Create:

```text
PAT-ECHANGE-MEDIATION -> legacy_id: CAP-INT-03, maps_to: ["CAP-13", "CAP-14", "CAP-18"], related: ["ABB-ECHANGE-MEDIATION"]
PAT-QUALITE-RECONCILIATION -> legacy_id: CAP-INT-11, maps_to: ["CAP-13", "CAP-14"], related: ["ABB-RECONCILIATION-DONNEES"]
PAT-ECHANGE-INTERNATIONAL-IPS -> legacy_id: CAP-INT-13, maps_to: ["CAP-15", "CAP-18"], related: ["PART-ECHANGE-TRANSFRONTALIER", "DO-29", "DO-30", "DO-31"]
```

Use `type: architecture-pattern`, `togaf_repository_section: reference-library`, `togaf_adm_phase: C`, and `architecture_scope: interoperability`.

- [ ] **Step 5: Create reference data and terminology files**

Create:

```text
RD-STRUCTURES-SERVICES -> legacy_id: CAP-INT-04, maps_to: ["CAP-11", "CAP-13", "CAP-14"], related: ["ABB-REFERENTIEL-STRUCTURES-SERVICES", "DO-23"]
RD-DONNEES-ENVIRONNEMENTALES-CLIMAT -> legacy_id: CAP-INT-16, maps_to: ["CAP-04", "CAP-05", "CAP-18"], related: ["PART-ONE-HEALTH", "ENF-4", "ART-4D"]
TERM-CODIFICATION-COMMUNE -> legacy_id: CAP-INT-05, maps_to: ["CAP-13", "CAP-14"], related: ["ABB-SERVICE-TERMINOLOGIE", "STD-0007"]
```

Use `type: reference-data` for `RD-*` and `type: terminology` for `TERM-*`.

- [ ] **Step 6: Create governance and evidence files**

Create:

```text
AC-CATALOGUE-SERVICES -> legacy_id: CAP-INT-06, maps_to: ["CAP-12", "CAP-14", "CAP-16"], related: ["ABB-CATALOGUE-CONTRATS"]
COMP-HOMOLOGATION-INTEROPERABILITE -> legacy_id: CAP-INT-12, maps_to: ["CAP-14", "CAP-16"], related: ["EVID-TESTS-INTEROPERABILITE", "P-INT-23", "P-INT-24", "P-INT-25"]
EVID-TESTS-INTEROPERABILITE -> legacy_id: CAP-INT-12, maps_to: ["CAP-16"], related: ["COMP-HOMOLOGATION-INTEROPERABILITE"]
```

Use `type: architecture-contract`, `type: compliance-rule` and `type: evidence` respectively.

- [ ] **Step 7: Create transfrontier requirements**

Create eight files:

```text
REQ-TF-01 Tout flux transfrontalier doit être couvert par un accord explicite.
REQ-TF-02 Le consentement du patient doit être obtenu pour tout échange sortant sauf obligation légale.
REQ-TF-03 Seules les données minimisées nécessaires à la finalité peuvent être exportées.
REQ-TF-04 Tous les flux transfrontaliers doivent être journalisés et auditables.
REQ-TF-05 Le GDHCN doit être le référentiel de confiance pour les échanges internationaux.
REQ-TF-06 Les données souveraines ne quittent pas le territoire sauf dérogation.
REQ-TF-07 Les systèmes partenaires étrangers doivent démontrer leur conformité avant tout accès.
REQ-TF-08 Tout résumé patient échangé doit être conforme au profil HL7 FHIR IPS et contenir les sections minimales requises.
```

Each file must use `type: exigence`, `legacy_id: CAP-INT-13`, `maps_to: ["CAP-15", "CAP-18"]`, `related: ["PART-ECHANGE-TRANSFRONTALIER"]`.

- [ ] **Step 8: Create One Health requirements**

Create seven files:

```text
REQ-OH-01 Tout échange intersectoriel doit être couvert par un accord explicite entre ministères.
REQ-OH-02 Les identités humaines ne doivent jamais être croisées avec les identités animales.
REQ-OH-03 Les données agrégées croisées doivent être irréversiblement désanonymisées.
REQ-OH-04 Chaque secteur conserve la souveraineté sur ses données source.
REQ-OH-05 Les dimensions d'agrégation communes doivent être normalisées.
REQ-OH-06 Tous les échanges intersectoriels doivent être journalisés et auditables.
REQ-OH-07 Le cadre Tripartite Plus doit être respecté pour les flux internationaux.
```

Each file must use `type: exigence`, `legacy_id: CAP-INT-14`, `maps_to: ["CAP-18"]`, `related: ["PART-ONE-HEALTH", "ENF-4"]`.

- [ ] **Step 9: Update the CNISN capacity chapter into an interoperability objects chapter**

Rename the narrative in `01_cnisn/02_capacites/index.md` from "capacités nationales requises" to "objets d'interopérabilité requis". Replace generated source markers that point to `cap-int-*.md` with generated markers pointing to the new replacement objects. The document may keep the folder name `02_capacites` for publication stability during this pass, but the prose must no longer assert that `CAP-INT-*` are active capabilities.

- [ ] **Step 10: Regenerate and validate**

Run:

```bash
python3 scripts/build_ref_index.py
python3 scripts/build_wrappers.py
python3 scripts/validate_ref.py
python3 scripts/build_ref_index.py --check
python3 scripts/build_wrappers.py --check
```

Expected:

```text
New replacement objects are indexed.
No new object is isolated.
CNISN wrappers render replacement objects instead of CAP-INT source files.
```

- [ ] **Step 11: Commit decomposed replacement objects**

Run:

```bash
git add 01_cnisn/02_capacites/index.md 04_architecture-repository scripts
git commit -m "refactor: decompose CNISN CAP-INT objects"
```

## Task 7: Replace Active `CAP-INT-*` References And Delete Legacy Files

**Files:**
- Delete: `04_architecture-repository/capacites/cap-int-01.md` through `cap-int-16.md`
- Modify: `README.md`
- Modify: `AGENTS.md`
- Modify: `00_caesn/`
- Modify: `01_cnisn/`
- Modify: `02_artsn/`
- Modify: `03_ptisn/`
- Modify: `04_architecture-repository/`
- Modify: `scripts/validate_ref.py`
- Modify: `scripts/audit/audit_chaine.py`
- Modify: `scripts/audit/audit_couverture.py`
- Modify: `scripts/audit/audit_conformite.py`

**Interfaces:**
- Consumes: replacement objects from Task 6.
- Produces: no active `CAP-INT-*` references except `legacy_id` and migration tables.

- [ ] **Step 1: Replace frontmatter relation IDs**

For each source object, replace `CAP-INT-*` relation IDs using the Primary Replacement Map. Add direct `CAP-*` relations when the object is a profile, plateau or work package and the relation exists for coverage purposes.

Examples:

```yaml
maps_to: ["CAP-INT-03", "CAP-INT-12"]
```

becomes:

```yaml
maps_to: ["ABB-ECHANGE-MEDIATION", "COMP-HOMOLOGATION-INTEROPERABILITE", "CAP-14", "CAP-16"]
```

```yaml
realizes: ["CAP-INT-08"]
```

becomes:

```yaml
realizes: ["ABB-CONFIANCE-AUTORISATION"]
maps_to: ["CAP-15"]
```

- [ ] **Step 2: Replace prose links**

For prose references, choose the semantic target:

```text
CAP-INT-03 exchange and mediation -> ABB-ECHANGE-MEDIATION or PAT-ECHANGE-MEDIATION
CAP-INT-12 conformity and tests -> COMP-HOMOLOGATION-INTEROPERABILITE or EVID-TESTS-INTEROPERABILITE
CAP-INT-13 transfrontier scope -> PART-ECHANGE-TRANSFRONTALIER
CAP-INT-14 One Health scope -> PART-ONE-HEALTH
CAP-INT-16 environmental and climate data -> RD-DONNEES-ENVIRONNEMENTALES-CLIMAT
```

Do not replace every prose occurrence with a CAESN `CAP-*`; only do that when the sentence is explicitly about enterprise capability alignment.

- [ ] **Step 3: Update validators to remove mandatory CAP-INT chain**

In `scripts/validate_ref.py`, replace the current `PT -> CAP-INT -> CAP` check with graph reachability from each `profil` or `solution-building-block` to at least one `capabilite`.

Use these relation keys for reachability:

```python
REACHABILITY_KEYS = [
    "maps_to", "realizes", "implements", "applies_to", "related",
    "contributes_to", "governs", "serves", "accesses"
]
```

The validator must now fail if:

```text
An active object has id starting with CAP-INT-
An active object has type capacite
A relation points to a deleted CAP-INT id
A profile/SBB cannot reach any CAP-* by graph traversal
```

The validator must allow `CAP-INT-*` only when:

```text
The field name is legacy_id
The file is 04_architecture-repository/00_metamodel/cap-int-migration.yaml
The file is 04_architecture-repository/08_views/togaf/cap-int-migration.md
```

- [ ] **Step 4: Update audit scripts**

Update audit names and text:

```text
Chaîne PT → CAP-INT → CAP
```

to:

```text
Chaîne PT/SBB → ABB/PAT/REQ/PART → CAP
```

Ensure the audit scripts use the same graph reachability logic as `validate_ref.py`.

- [ ] **Step 5: Delete legacy CAP-INT files**

Run:

```bash
git rm 04_architecture-repository/capacites/cap-int-01.md 04_architecture-repository/capacites/cap-int-02.md 04_architecture-repository/capacites/cap-int-03.md 04_architecture-repository/capacites/cap-int-04.md 04_architecture-repository/capacites/cap-int-05.md 04_architecture-repository/capacites/cap-int-06.md 04_architecture-repository/capacites/cap-int-07.md 04_architecture-repository/capacites/cap-int-08.md 04_architecture-repository/capacites/cap-int-09.md 04_architecture-repository/capacites/cap-int-10.md 04_architecture-repository/capacites/cap-int-11.md 04_architecture-repository/capacites/cap-int-12.md 04_architecture-repository/capacites/cap-int-13.md 04_architecture-repository/capacites/cap-int-14.md 04_architecture-repository/capacites/cap-int-15.md 04_architecture-repository/capacites/cap-int-16.md
```

Remove the empty `04_architecture-repository/capacites/` directory if git leaves it empty.

- [ ] **Step 6: Check that active references are gone**

Run:

```bash
rg -n "CAP-INT-[0-9]{2}" README.md AGENTS.md 00_caesn 01_cnisn 02_artsn 03_ptisn 04_architecture-repository scripts
```

Expected remaining matches only in:

```text
04_architecture-repository/00_metamodel/cap-int-migration.yaml
04_architecture-repository/08_views/togaf/cap-int-migration.md
legacy_id fields of replacement objects
```

- [ ] **Step 7: Regenerate and validate**

Run:

```bash
python3 scripts/build_ref_index.py
python3 scripts/build_wrappers.py
python3 scripts/validate_ref.py
python3 scripts/build_ref_index.py --check
python3 scripts/build_wrappers.py --check
```

Expected:

```text
No relation target is unresolved.
No Markdown link points to deleted cap-int files.
No active CAP-INT object remains.
Profile to CAP reachability passes.
```

- [ ] **Step 8: Commit CAP-INT removal**

Run:

```bash
git add README.md AGENTS.md 00_caesn 01_cnisn 02_artsn 03_ptisn 04_architecture-repository scripts
git commit -m "refactor: remove active CAP-INT objects"
```

## Task 8: Regenerate Derived Technical Artifacts

**Files:**
- Modify: `dist/` if tracked and generated by local commands
- Modify: `03_ptisn/schemas/openapi/*.json`
- Modify: generated FHIR or JSON Schema outputs produced by `scripts/compilers/`
- Modify: graphify output only if it is tracked and not under excluded `graphify-out/`

**Interfaces:**
- Consumes: final target paths and relation IDs.
- Produces: generated technical artifacts that no longer embed `referentiel/` or active `CAP-INT-*` references.

- [ ] **Step 1: Run available compilers**

Run the repository's known compilers:

```bash
python3 scripts/compile_rdf.py
python3 scripts/compilers/compile_openapi.py
python3 scripts/compilers/compile_jsonschema.py
python3 scripts/compilers/compile_fhir.py
python3 scripts/compilers/compile_oda.py
```

If a compiler fails because its input directory is intentionally absent, record the failure and decide whether the compiler is part of the current checked workflow. Do not suppress failures by deleting checks.

- [ ] **Step 2: Check generated metadata paths**

Run:

```bash
rg -n "referentiel/|CAP-INT-[0-9]{2}" 03_ptisn/schemas dist scripts
```

Expected:

```text
No generated schema source path points to referentiel/.
No generated active schema reference uses CAP-INT-*.
```

- [ ] **Step 3: Run full validation**

Run:

```bash
python3 scripts/validate_ref.py
python3 scripts/build_ref_index.py --check
python3 scripts/build_wrappers.py --check
make check
```

If `make check` does not exist, record:

```text
make check unavailable: no Makefile target in repository.
```

- [ ] **Step 4: Commit generated artifacts**

Run:

```bash
git add 03_ptisn/schemas dist scripts 04_architecture-repository
git commit -m "chore: regenerate architecture derived artifacts"
```

## Task 9: Final Review, Diff Hygiene And PR Preparation

**Files:**
- Read only: all changed files
- Modify: none unless final validation reveals a concrete defect

**Interfaces:**
- Consumes: all previous task commits.
- Produces: clean final branch ready for user review and PR.

- [ ] **Step 1: Inspect final diff**

Run:

```bash
git status --short
git log --oneline --decorate -8
git diff --stat origin/codex/apply-audit-recommendations
```

Expected:

```text
.gitignore remains unstaged unless explicitly requested.
Only TOGAF refactor files are changed.
Recent commits match the task sequence.
```

- [ ] **Step 2: Run final checks**

Run:

```bash
python3 scripts/validate_ref.py
python3 scripts/build_ref_index.py --check
python3 scripts/build_wrappers.py --check
rg -n "referentiel/" README.md AGENTS.md 00_caesn 01_cnisn 02_artsn 03_ptisn scripts 04_architecture-repository
rg -n "CAP-INT-[0-9]{2}" README.md AGENTS.md 00_caesn 01_cnisn 02_artsn 03_ptisn 04_architecture-repository scripts
```

Expected:

```text
Validation is CONFORME.
Index and wrappers are current.
No active referentiel/ path remains.
CAP-INT remains only in migration correspondence and legacy_id fields.
```

- [ ] **Step 3: Prepare final summary**

Prepare a concise summary with:

```text
Repository root renamed to 04_architecture-repository/
Architecture objects placed into TOGAF-aligned folders
Partitions and TOGAF views created
CAP-INT objects decomposed and deleted as active objects
Validators updated from PT -> CAP-INT -> CAP to graph reachability
Generated wrappers and indexes refreshed
Checks run and outcomes
```

- [ ] **Step 4: Push and create PR only after user confirms execution is complete**

Run:

```bash
git push
```

Then create or update the PR using the repository's existing GitHub workflow. The PR body must include the validation output and explicitly mention that `.gitignore` was not included unless the user requested it.
