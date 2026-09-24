---
domain: 2026-09-09-hea-togaf-repository-refactor
id: task-5-report
type: implementation-report
title: "Task 5 report - TOGAF partitions and repository views"
status: active
owner: DEPSI
version: "0.1"
---
# Task 5 report - TOGAF partitions and repository views

## Synthèse

Task 5 est implémentée sur la branche `codex/apply-audit-recommendations`, à partir de la base `80b5a2b914423967819fa76bf7644de2121b4307`. La tâche ajoute les partitions TOGAF attendues et les vues de repository demandées, puis raccorde ces vues au cycle de génération des enveloppes.

## Fichiers créés

Partitions d'architecture :

- `04_architecture-repository/01_partitions/value-streams/part-vs-01.md`
- `04_architecture-repository/01_partitions/value-streams/part-vs-02.md`
- `04_architecture-repository/01_partitions/value-streams/part-vs-03.md`
- `04_architecture-repository/01_partitions/value-streams/part-vs-04.md`
- `04_architecture-repository/01_partitions/transverses/part-transverse-interoperabilite.md`
- `04_architecture-repository/01_partitions/transverses/part-transverse-identite.md`
- `04_architecture-repository/01_partitions/transverses/part-transverse-securite-confiance.md`
- `04_architecture-repository/01_partitions/transverses/part-transverse-donnees-referentielles.md`
- `04_architecture-repository/01_partitions/transverses/part-transverse-analytics-pilotage.md`
- `04_architecture-repository/01_partitions/sectorielles/part-one-health.md`
- `04_architecture-repository/01_partitions/externes/part-echange-transfrontalier.md`

Vues et index générés :

- `04_architecture-repository/01_partitions/index.md`
- `04_architecture-repository/08_views/togaf/architecture-landscape.md`
- `04_architecture-repository/08_views/togaf/standards-information-base.md`
- `04_architecture-repository/08_views/togaf/reference-library.md`
- `04_architecture-repository/08_views/togaf/governance-log.md`
- `04_architecture-repository/08_views/togaf/requirements-repository.md`
- `04_architecture-repository/08_views/togaf/solutions-landscape.md`
- `04_architecture-repository/08_views/togaf/adm-traceability.md`

## Décisions d'implémentation

Les partitions sont des objets `architecture-partition` et sont donc indexées dans `04_architecture-repository/_index.yaml`. Le total généré est désormais de 349 objets, dont 11 partitions TOGAF.

Les vues TOGAF et l'index des partitions sont des enveloppes dérivées. Elles portent un frontmatter documentaire, mais ne sont pas traitées comme objets du graphe, afin d'éviter des nœuds artificiels et des îlots non métier. Les scripts `build_ref_index.py`, `validate_ref.py` et `compile_rdf.py` les excluent donc de l'inventaire objet et du RDF.

`build_wrappers.py` a été étendu pour traiter ces enveloppes dérivées comme cibles explicites et pour permettre aux tables `mode=table` de lire les frontmatters Markdown hors `04_architecture-repository`, notamment `01_cnisn/05_standards/*.md` et `01_cnisn/06_decisions/*.md`. Les normes et ADR CNISN restent dans le CNISN ; elles ne sont pas reclassées comme objets du repository.

Le marqueur de `solutions-landscape.md` conserve la source `03_ptisn/schemas/**/*.json` demandée. Les JSON restent des contrats techniques générés, validés par les compilateurs dédiés dans `make check`, et ne sont pas convertis en lignes d'objets de repository.

Le schéma du référentiel documente désormais `repository-view` comme type non indexé et précise que `envelope` est conditionnel : obligatoire pour les objets transclus, absent pour les partitions TOGAF autonomes et les vues dérivées.

## Génération

Commandes exécutées :

- `python3 scripts/build_ref_index.py` : OK, index régénéré.
- `python3 scripts/build_wrappers.py` : OK, 109 enveloppes écrites.

## Validations

Commandes exécutées :

- `python3 -m py_compile scripts/build_wrappers.py scripts/build_ref_index.py scripts/validate_ref.py scripts/compile_rdf.py` : OK.
- `python3 scripts/validate_ref.py` : CONFORME, 349 objets indexés, 5917 liens relatifs vérifiés, aucun lien cassé, aucun îlot.
- `python3 scripts/build_ref_index.py --check` : OK.
- `python3 scripts/build_wrappers.py --check` : OK, 109 enveloppes à jour.
- `make check` : OK.

`make check` a également vérifié les manifestes, `check_links.py` avec 0 lien cassé sur 6116 liens, la compilation RDF avec 349 objets, la validation SHACL conforme, 33 ressources FHIR, 31 schémas JSON Schema, 19 spécifications OpenAPI, 1 nomenclature ODA et l'artefact Mintlify.

## Avertissements non bloquants

`validate_ref.py` signale 4 avertissements préexistants sur des profils PTISN qui mappent directement vers des capabilités CAESN : PT-14 vers CAP-15 et CAP-17, PT-15 vers CAP-05 et CAP-18. La commande reste conforme et ces avertissements ne sont pas introduits par Task 5.

## Exclusions de commit

`.gitignore` conserve sa modification préexistante et n'est pas inclus dans le commit Task 5. `graphify-out/`, `04_architecture-repository/graphify-out/` et `.obsidian/` restent exclus.
