# Task 7 Report - Remove active CAP-INT objects

## Résumé

Task 7 a supprimé les anciens objets actifs `CAP-INT-*` et remplacé leurs usages actifs par les objets TOGAF issus de Task 6. Les anciens identifiants sont conservés uniquement comme traçabilité historique dans les champs `legacy_id` et dans les deux fichiers de migration autorisés.

## Changements réalisés

- Suppression par `git rm` des 16 fichiers `04_architecture-repository/capacites/cap-int-01.md` à `04_architecture-repository/capacites/cap-int-16.md`.
- Remplacement des relations frontmatter `CAP-INT-*` par les cibles de la Primary Replacement Map, avec ajout des rattachements directs `CAP-*` pour les profils, plateaux et work packages quand ils servent la couverture.
- Remplacement des liens Markdown actifs vers les anciens fichiers `cap-int-*.md`, y compris le dernier lien cassé dans `quick-start-guides.md`.
- Correction des `legacy_id` des objets de remplacement afin de porter les anciens identifiants `CAP-INT-*`.
- Mise à jour de `scripts/validate_ref.py` pour interdire les objets actifs `CAP-INT-*`, le type actif `capacite` et les relations vers les anciens identifiants.
- Remplacement du contrôle obligatoire `PT -> CAP-INT -> CAP` par une traversée de graphe `profil`/`solution-building-block` vers au moins une capabilité `CAP-*`.
- Alignement des scripts d'audit sur la chaîne `PT/SBB -> ABB/PAT/REQ/PART -> CAP`.
- Mise à jour des wrappers, de l'index de référence, des artefacts OpenAPI et de l'artefact Mintlify.
- Nettoyage des vues racine et de l'ontologie active pour ne plus décrire `CAP-INT` comme modèle actif.

## Validations

Les commandes demandées ont été exécutées avec succès le 2026-09-11.

| Commande | Résultat |
|----------|----------|
| `python3 scripts/build_ref_index.py` | OK, `_index.yaml` régénéré |
| `python3 scripts/build_wrappers.py` | OK, 112 enveloppes écrites |
| `python3 scripts/validate_ref.py` | CONFORME, 369 objets indexés, 6093 liens vérifiés |
| `python3 scripts/build_ref_index.py --check` | OK, index à jour |
| `python3 scripts/build_wrappers.py --check` | OK, 112 enveloppes à jour |
| `git diff --check` | OK, aucune erreur d'espaces |
| `make check` | OK, liens, manifestes, RDF/SHACL, FHIR, JSON Schema, OpenAPI, ODA et Mintlify conformes |
| `.venv/bin/python scripts/audit/run_all.py` | OK, 4/4 audits réussis |

## Résultat validate_ref

`scripts/validate_ref.py` confirme les points suivants :

- Aucun ancien identifiant d'interopérabilité hors migration ou `legacy_id`.
- Aucun ancien objet d'interopérabilité actif.
- Aucune relation ne pointe vers un ancien identifiant d'interopérabilité.
- Tous les profils et SBB atteignent une capabilité CAESN.
- Les 18 capabilités CAESN sont atteintes par au moins un profil ou SBB.

## Occurrences CAP-INT restantes

Le scan officiel du brief :

```bash
rg -n "CAP-INT-[0-9]{2}" README.md AGENTS.md 00_caesn 01_cnisn 02_artsn 03_ptisn 04_architecture-repository scripts
```

ne retourne que des occurrences autorisées :

| Catégorie | Fichiers | Lignes |
|-----------|----------|--------|
| Migration machine-readable | `04_architecture-repository/00_metamodel/cap-int-migration.yaml` | 16 |
| Vue TOGAF de migration | `04_architecture-repository/08_views/togaf/cap-int-migration.md` | 16 |
| Traçabilité historique | champs `legacy_id` des objets de remplacement | 43 |

Aucun lien actif ne pointe encore vers `04_architecture-repository/capacites/cap-int-*.md`. Le dossier `04_architecture-repository/capacites/` n'existe plus dans l'arbre de travail.

## Hygiène Git

`.gitignore` reste une modification préexistante non incluse dans Task 7. Les dossiers `graphify-out/` et `.obsidian/` ne sont pas inclus dans les changements à committer.
