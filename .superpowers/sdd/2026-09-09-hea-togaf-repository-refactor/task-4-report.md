# Task 4 Report: Align Architecture Repository Folders With TOGAF

## Statut

Task 4 a déplacé les objets existants non `CAP-INT` de `04_architecture-repository/` dans le layout TOGAF cible. Les 16 fichiers `04_architecture-repository/capacites/cap-int-*.md` sont restés en place pour les Tasks 6 et 7. Aucun nouvel objet ABB, PAT, REQ ou PART n'a été créé.

Commit attendu: `refactor: align architecture repository folders with TOGAF`.
Hash final: fourni dans la réponse finale, car ce rapport est inclus dans le commit Task 4.

## Base et branche

- Branche: `codex/apply-audit-recommendations`.
- Base vérifiée au démarrage: `7f4da53d5cce5a8172977e278cb6f14955b3241f`.
- Modification préexistante conservée hors commit: `.gitignore`.

## Chemins déplacés

Les déplacements ont été faits avec `git mv`.

- Métamodèle: `04_architecture-repository/_schema.md` -> `04_architecture-repository/00_metamodel/schema.md`.
- Motivation: parties prenantes, principes et valeurs -> `02_architecture-elements/motivation/`.
- Strategy: capacités CAESN, flux de valeur et étapes de valeur -> `02_architecture-elements/strategy/`.
- Business: acteurs, rôles, processus, lieux, objets métier et `SRV-01` -> `02_architecture-elements/business/`.
- Data: objets de données -> `02_architecture-elements/data/data-objects/`.
- Requirements: exigences ENF -> `03_requirements/`.
- Patterns: fondations et chapitres ARTSN -> `04_patterns/foundations/` et `04_patterns/artsn-rules/`.
- ABB legacy: `CMP-01..38` et `SRV-02..06` -> `05_building-blocks/abb/legacy-components/` et `legacy-services/`.
- SBB legacy: profils `PT-01..19` -> `05_building-blocks/sbb/legacy-profiles/`.
- Governance: `CMP-39..46` -> `06_governance/registers/`.
- Migration: work packages, plateaux et gaps -> `07_migration/`.

## Mise à jour des métadonnées

- Les `domain:` frontmatter des fichiers Markdown déplacés reflètent maintenant le dossier parent immédiat, préfixe numérique inclus quand il existe.
- Les chemins `envelope:` et les marqueurs `BEGIN:GENERATED source=` pointent vers les nouveaux emplacements.
- Les liens Markdown relatifs ont été recalculés depuis les nouveaux dossiers.
- `README.md` et `quick-start-guides.md` pointent vers les nouveaux chemins du dépôt d'architecture.
- Les métadonnées OpenAPI générées `x-hea-source` et `x-hea-file` pointent vers `05_building-blocks/sbb/legacy-profiles/`.

## Schéma et scripts

- `04_architecture-repository/00_metamodel/schema.md` introduit les types actifs TOGAF demandés: `architecture-partition`, `architecture-building-block`, `solution-building-block`, `architecture-pattern`, `architecture-contract`, `compliance-rule`, `evidence`, `reference-data`, `terminology`, `stakeholder`, `business-location`, `business-value`.
- `capacite` est classé `legacy non actif`; les types legacy demandés restent documentés: `composant-applicatif`, `composant-infrastructure`, `composant-securite`, `profil`, `service`, `registre-gouvernance`.
- `scripts/build_wrappers.py`, `scripts/validate_ref.py`, `scripts/build_ref_index.py` excluent les documents métamodèle non objets de l'indexation ou de la détection d'îlots.
- `scripts/compile_rdf.py` et les compilateurs JSON Schema, FHIR, OpenAPI et ODA utilisent les nouveaux chemins source.
- Les scripts d'audit `scripts/audit/fix_anomalies.py` et `scripts/audit/fix_vs_links.py` ont été alignés sur les nouveaux dossiers.

## Régénérations

- `python3 scripts/build_ref_index.py`: `[OK] 04_architecture-repository/_index.yaml généré.`
- `python3 scripts/build_wrappers.py`: `101 enveloppes écrites`.
- `python3 scripts/compilers/compile_openapi.py --validate`: 19 spécifications OpenAPI générées et valides.
- `python3 scripts/build_mintlify.py`: artefact Mintlify régénéré pour maintenir `make check` vert.

## Vérifications

- `python3 scripts/validate_ref.py`: `Résumé : CONFORME`, 338 objets indexés, 5885 liens relatifs vérifiés, 0 lien relatif cassé.
- `python3 scripts/build_ref_index.py --check`: `[OK] 04_architecture-repository/_index.yaml à jour.`
- `python3 scripts/build_wrappers.py --check`: `OK : 101 enveloppes à jour`.
- `make check`: OK. Inclut index, wrappers, liens, manifestes, `validate_ref.py`, RDF/SHACL, FHIR, sync Graphify en mode check, JSON Schema, OpenAPI, ODA, gouvernance et Mintlify.
- Recherche des anciens chemins internes actifs `04_architecture-repository/(profils|capabilites|composants|flux-valeur|processus|_schema.md|chapitres|fondations|objets-de-donnees|objets-metier|services|work-packages|plateaux|gaps)`: aucune correspondance dans `scripts`, `04_architecture-repository`, `00_caesn`, `01_cnisn`, `02_artsn`, `03_ptisn`, `README.md`, `quick-start-guides.md` et `mintlify-site`.

## Avertissements conservés

`validate_ref.py` signale 4 avertissements multi-niveaux préexistants sur `PT-14` et `PT-15`, qui mappent directement vers des capacités CAESN. Le résumé reste `CONFORME`; Task 4 ne modifie pas la logique CAP-INT.

## Exclusions confirmées

- `.gitignore` est resté non stagé et non commité.
- `graphify-out/` n'est pas inclus.
- `.obsidian/` n'est pas inclus.

DONE
