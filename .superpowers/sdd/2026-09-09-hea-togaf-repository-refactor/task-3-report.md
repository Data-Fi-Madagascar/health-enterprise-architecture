# Task 3 Report: Rename Architecture Repository Root

## Statut

Task 3 a renommé physiquement la racine active `referentiel/` en `04_architecture-repository/` sans placement TOGAF interne. Les anciens sous-dossiers sont conservés sous la nouvelle racine pour laisser le Task 4 gérer le reclassement.

Commit attendu: `refactor: rename architecture repository root`.
Hash final: `433306e8f47e304154c1aaf4a4442915b0dcd3eb`.

## Chemins déplacés

- `referentiel/` -> `04_architecture-repository/` via `git mv`.
- Les 338 objets indexés restent dans les sous-dossiers temporaires existants: `acteurs/`, `capabilites/`, `capacites/`, `chapitres/`, `composants/`, `etapes-valeur/`, `exigences/`, `flux-valeur/`, `fondations/`, `gaps/`, `lieux/`, `objets-de-donnees/`, `objets-metier/`, `parties-prenantes/`, `plateaux/`, `principes/`, `processus/`, `profils/`, `roles/`, `services/`, `valeurs/`, `work-packages/`.

## Chemins modifiés

- `scripts/`: constantes `ARCH_REPOSITORY_DIR` basculées vers `04_architecture-repository`; messages de génération et métadonnées de source mis à jour.
- `README.md`, `quick-start-guides.md`, `Makefile`, `ontologie/hea.ttl`: chemins actifs ou messages d'outillage mis à jour.
- `AGENTS.md`: vérifié, aucune modification requise dans le commit Task 3.
- `00_caesn/`, `01_cnisn/`, `02_artsn/`, `03_ptisn/`: liens Markdown actifs et marqueurs `BEGIN:GENERATED source=` repointés vers `04_architecture-repository/`.
- `03_ptisn/schemas/openapi/`: métadonnées générées `x-hea-source` et `x-hea-file` repointées.
- `mintlify-site/`: artefact dérivé suivi régénéré pour satisfaire `make check`.

## Vérifications

- `python3 scripts/build_ref_index.py`: `[OK] 04_architecture-repository/_index.yaml généré.`
- `python3 scripts/build_wrappers.py`: `101 enveloppes écrites`.
- `python3 scripts/validate_ref.py`: `Résumé : CONFORME`, 338 objets indexés, 5885 liens relatifs vérifiés, 0 lien relatif cassé; 4 avertissements multi-niveaux CAP-INT préexistants conservés car la logique CAP-INT n'est pas modifiée dans Task 3.
- `python3 scripts/build_ref_index.py --check`: `[OK] 04_architecture-repository/_index.yaml à jour.`
- `python3 scripts/build_wrappers.py --check`: `OK : 101 enveloppes à jour`.
- `git diff --check`: OK, aucune sortie.
- `rg -n "referentiel/" README.md AGENTS.md 00_caesn 01_cnisn 02_artsn 03_ptisn scripts 04_architecture-repository`: aucune correspondance active, exit code 1 attendu.
- `make check`: OK. Inclut index, wrappers, liens, manifestes, `validate_ref.py`, RDF/SHACL, FHIR, sync Graphify en mode check, JSON Schema, OpenAPI, ODA, gouvernance et Mintlify.

## Restes `referentiel/`

Aucun reste `referentiel/` dans le périmètre actif Task 3 ni dans `Makefile`, `quick-start-guides.md`, `mintlify-site/` ou `ontologie/`.

Restes conservés hors périmètre actif: documents historiques et plans sous `docs/`, plus `coherence-report.md`. Ces occurrences décrivent l'historique de refactor ou les états antérieurs et ne sont pas des liens actifs validés par Task 3.

## Exclusions confirmées

- `.gitignore` est une modification préexistante et ne doit pas être stagée ni commitée.
- `graphify-out/` n'est pas inclus.
- `.obsidian/` n'est pas inclus.

## Fix round 1

- P2 corrigé: le hash final du commit Task 3 est renseigné explicitement.
- P3 corrigé: `AGENTS.md` est retiré de la liste des fichiers modifiés et mentionné comme vérifié sans modification requise.

DONE
