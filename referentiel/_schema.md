---
title: Schéma du référentiel
id: schema-referentiel
type: meta
status: draft
version: "1.0"
owner: DEPSI
tags: ["referentiel", "schema", "gouvernance"]
---

# Schéma du référentiel

Ce document définit le modèle d’objets du référentiel. Il est la source de vérité pour la structure, le nommage et le frontmatter de tout objet.

## Principe

- **Un objet = un fichier** dans `referentiel/<type>/<id>.md`.
- Chaque objet est un bloc de contenu **auto-portant** : il n’a pas besoin du reste du document d’origine pour être compris.
- Les documents historiques ne conservent que la **prose narrative**, les catalogues et les matrices ; ils **référencent** les objets par lien.
- Le frontmatter est la seule source des **métadonnées de gouvernance** (statut, propriétaire, version, relations).

## Types d’objets et répertoires

| Type | Répertoire | Préfixe d’id | Sources (niveaux) |
|------|------------|--------------|-------------------|
| `flux-valeur` | `referentiel/flux-valeur/` | `vs-` | CAESN (VS-01…04) |
| `capabilite` | `referentiel/capabilites/` | `cap-` | CAESN (CAP-01…16) |
| `principe` | `referentiel/principes/` | `p-` (CNISN `p-int-`, CAESN `pa-`/`pd-`) | CAESN (PA, PD), CNISN (P-INT) |
| `capacite` | `referentiel/capacites/` | `cap-int-` | CNISN (CAP-INT-01…12) |
| `fondation` | `referentiel/fondations/` | `f-` | ART-SN (F.1…6) |
| `exigence` | `referentiel/exigences/` | `enf-`, `ex-` | ART-SN (ENF-1…5, exigences) |
| `chapitre` | `referentiel/chapitres/` | `art-` | ART-SN (ART-0…11) |
| `profil` | `referentiel/profils/` | `pt-` | PTISN (PT-01…13) |
| `service` | `referentiel/services/` | — | éléments de services transverses |
| `meta` | `referentiel/` (racine) | `_schema`, `_index` | — |

## Conventions de nommage

- **Dossier** : nom court en kebab-case, singulier (`principes`, pas `principes/domaine`).
- **Fichier** : `<id>-slugified.md`, id minuscule en kebab-case.
- Normalisation des identifiants pendant la migration : `P-INT-01` → fichier `p-int-01.md` ; `CAP-INT-02` → `cap-int-02.md` ; `ART-4a` → `art-4a.md` ; `F.5` → `f-5.md` ; `PT-01` → `pt-01.md`.
- Le **code source** (`P-INT-01`) reste le titre H1 et le label canonique ; le nom de fichier est sa forme slugifiée.

## Frontmatter canonique

```yaml
---
id: p-int-01              # id normalisé, unique, kebab-case
type: principe            # type de l'objet (cf. tableau)
niveau: "2"               # niveau de référence : 1 (CAESN), 2 (CNISN), 3 (ART-SN), 4 (PTISN)
title: P-INT-01 — Autorité désignée
status: active            # draft | active | deprecated | candidate
owner: DEPSI              # entité responsable
version: "0.5"            # version héritée de la source
source: 01_cnisn/01_principes.md   # chemin de provenance pré-refactor
maps_to: ["cap-int-01"]   # correspondance vers autre référentiel (id)
implements: []          # chapitre/objet mis en œuvre
applies_to: []          # objets auxquels il s'applique
related: []             # autres objets liés
tags: ["cnisn", "autorite", "donnees-de-reference"]
---
```

### Champs

| Champ | Obligatoire | Description |
|-------|-------------|-------------|
| `id` | oui | Identifiant normalisé unique dans le référentiel |
| `type` | oui | Type d’objet (tableau ci-dessus) |
| `niveau` | oui | Niveau de référence source |
| `title` | oui | Titre canonique de l’objet |
| `status` | oui | `draft`, `active`, `deprecated` ou `candidate` |
| `owner` | oui | Responsable / entité de gouvernance |
| `version` | non | Version héritée du document source |
| `source` | oui | Chemin du document d’origine pré-refactor |
| `family` | non | Famille de réponse (type `capacite` uniquement) : `referentiels`, `echange`, `analytique`, `confiance`, `qualite-conformite` |
| `maps_to` | non | Liens typés : correspondance vers un autre objet du référentiel (ids) |
| `implements` | non | Liens typés : chapitres / objets mis en œuvre |
| `applies_to` | non | Liens typés : objets auxquels il s’applique |
| `related` | non | Liens typés : autres objets liés |
| `tags` | non | Mots-clés pour l’indexation |

### Statuts

| Statut | Signification |
|--------|---------------|
| `draft` | Non validé, en rédaction |
| `active` | Validé et en vigueur |
| `deprecated` | Remplacé, conservé pour historique |
| `candidate` | Proposé, en attente d’arbitrage (ex. ART-10/11, F.5/6) |

## Structure du corps d’un objet

Le corps suit le gabarit `H1 (titre) → H2 (finalité / contenu) → H3 (sous-sections)`.

```markdown
# P-INT-01 — Autorité désignée

## Enoncé

(texte du principe, inchangé par rapport à la source)

## Domaines concernés

(liste, si présente dans la source)

## Liens

- [CAP-INT-01 — Résolution d'identité du bénéficiaire](../capacites/cap-int-01.md)
```

- Le **contenu textuel** des objets n’est **pas reformulé** : il est copié tel quel depuis la source (seule la structure de titres peut être normalisée).
- Les relations transversales peuvent être portées par le frontmatter (`maps_to`, `implements`, `applies_to`, `related`) et/ou par une section `## Liens` en fin d’objet.
- La **prose narrative** (paragraphes « pour qui lire », légendes, introductions) **reste dans le document source** et n’est pas dupliquée dans les objets.
- Le champ `family` classe chaque capacité CNISN dans l’une des cinq familles de réponse alignées sur l’ART-SN (couches 3 à 5 et axes de la cartographie cible). Il est porté par le frontmatter des `cap-int-*.md` et sert d’en-tête de section dans `01_cnisn/02_capacites.md` (voir [annexe B](../01_cnisn/08_annexes/b-articulation-art-sn.md)).

## Registre des objets

Le registre central de tous les objets est `referentiel/_index.yaml` : id, type, niveau, chemin, statut. Il est la source de vérité pour la vérification des comptes et la détection de perte pendant la migration.
