---
domain: referentiel
title: Schéma du référentiel
id: SCHEMA-REFERENTIEL
type: meta
niveau: "0"
status: draft
version: "1.0"
owner: DEPSI
envelope: referentiel/_schema.md
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
| `capabilite` | `referentiel/capabilites/` | `cap-` | CAESN (CAP-01…18) |
| `principe` | `referentiel/principes/` | `p-` (CNISN `p-int-`, CAESN `pa-`/`pd-`) | CAESN (PA, PD), CNISN (P-INT) |
| `etape-valeur` | `referentiel/etapes-valeur/` | `ev-` | CAESN (EV-01…28) |
| `processus-metier` | `referentiel/processus/` | `prc-` | CAESN (PRC-01…13) |
| `composant-applicatif` | `referentiel/composants/` | `cmp-` | CAESN : composants applicatifs (couches 2 a 6), CMP-01…25 |
| `composant-infrastructure` | `referentiel/composants/` | `cmp-` | socle technologique (couche 1) : CMP-26…31 |
| `composant-securite` | `referentiel/composants/` | `cmp-` | axe securite/confiance : CMP-32…38 |
| `registre-gouvernance` | `referentiel/composants/` | `cmp-` | axe gouvernance : CMP-39…46 |
| `partie-prenante` | `referentiel/parties-prenantes/` | `pp-` | CAESN (PP-01…10) |
| `capacite` | `referentiel/capacites/` | `cap-int-` | CNISN (CAP-INT-01…16) |
| `fondation` | `referentiel/fondations/` | `f-` | ARTSN (F.1…6) |
| `exigence` | `referentiel/exigences/` | `enf-`, `ex-` | ARTSN (ENF-1…5, exigences) |
| `chapitre` | `referentiel/chapitres/` | `art-` | ARTSN (ART-0…12) |
| `profil` | `referentiel/profils/` | `pt-` | PTISN (PT-01…19) |
| `service` | `referentiel/services/` | `srv-` | services transverses (business / applicatif / technologique) |
| `acteur` | `referentiel/acteurs/` | `act-` | acteurs métier (organisations, personnes) — CAESN |
| `role` | `referentiel/roles/` | `rol-` | rôles métier (responsabilités) — CAESN |
| `lieu` | `referentiel/lieux/` | `loc-` | localisation géographique — CAESN |
| `work-package` | `referentiel/work-packages/` | `wp-` | paquets de travail (lots ARTSN) |
| `plateau` | `referentiel/plateaux/` | `pl-` | états cibles de l'architecture (roadmap) |
| `gap` | `referentiel/gaps/` | `gap-` | écarts entre plateaux |
| `meta` | `referentiel/` (racine) | `_schema`, `_index` | — |

## Conventions de nommage

- **Dossier** : nom court en kebab-case, singulier (`principes`, pas `principes/domaine`).
- **Fichier** : `<id>-slugified.md`, id minuscule en kebab-case.
- Normalisation des identifiants pendant la migration : `P-INT-01` → fichier `p-int-01.md` ; `CAP-INT-02` → `cap-int-02.md` ; `ART-4A` → `art-4a.md` ; `F.5` → `f-5.md` ; `PT-01` → `pt-01.md`.
- Le **code source** (`P-INT-01`) reste le titre H1 et le label canonique ; le nom de fichier est sa forme slugifiée.

## Frontmatter canonique

```yaml
---
id: P-INT-01              # id normalisé, unique, kebab-case
type: principe            # type de l'objet (cf. tableau)
niveau: "2"               # niveau de référence : 1 (CAESN), 2 (CNISN), 3 (ARTSN), 4 (PTISN)
title: P-INT-01 — Autorité désignée
status: active            # draft | active | stable | candidate | deprecated
owner: DEPSI              # entité responsable
version: "0.5"            # version héritée de la source
envelope: 01_cnisn/01_principes/index.md   # chemin de provenance pré-refactor
maps_to: ["CAP-INT-01"]   # correspondance vers autre référentiel (id)
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
| `represents` | non | Acteur représente / réalise une partie prenante (PP) — ArchiMate Realization/Association |
| `represented_by` | non | Inverse de `represents` (coté partie prenante) |
| `assigned_to` | non | Rôle assigné à un acteur — ArchiMate Assignment |
| `has_role` | non | Inverse de `assigned_to` (coté acteur) |
| `performs` | non | Rôle / acteur réalise un processus métier (PRC) — ArchiMate Assignment |
| `performed_by` | non | Inverse de `performs` (coté processus) |
| `located_at` | non | Acteur / composant / service / capacité localisé géographiquement (Location) — ArchiMate Association |
| `serves` | non | Service rendu à une partie prenante / un acteur — ArchiMate Serving |
| `accesses` | non | Service / composant / processus accède à un objet métier / donnée — ArchiMate Access |
| `accessed_by` | non | Inverse de `accesses` (coté objet métier / donnée) |
| `realizes` | non | Service / paquet de travail / plateau réalise une capacité, composant ou service — ArchiMate Realization |
| `realized_by` | non | Inverse de `realizes` (coté capacité / composant / service) |
| `contributes_to` | non | Paquet de travail contribue à un plateau |
| `precedes` | non | Plateau précède un autre plateau (ordre temporel) |
| `between` | non | Écart (gap) entre deux plateaux |
| `categorie` | non | Sous-couche ArchiMate de l'objet : `applicatif`, `infrastructure`, `securite`, `principe`, `regulation`, `acteur`, `work-package`, `data-object` |
| `governs` | non | Liens typés : element de gouvernance qui encadre/valide un composant (sens gouvernance -> composant) |
| `tags` | non | Mots-clés pour l’indexation |

### Statuts

| Statut | Signification |
|--------|---------------|
| `draft` | Non validé, en rédaction |
| `active` | Validé et en vigueur |
| `stable` | Mature, largement adopté, changements rares |
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

- [CAP-INT-01 — Résolution d'identité du bénéficiaire](capacites/cap-int-01.md)
```

- Le **contenu textuel** des objets n’est **pas reformulé** : il est copié tel quel depuis la source (seule la structure de titres peut être normalisée).
- Les relations transversales peuvent être portées par le frontmatter (`maps_to`, `implements`, `applies_to`, `related`) et/ou par une section `## Liens` en fin d’objet.
- La **prose narrative** (paragraphes « pour qui lire », légendes, introductions) **reste dans le document source** et n’est pas dupliquée dans les objets.
- Le champ `family` classe chaque capacité CNISN dans l’une des cinq familles de réponse alignées sur l’ARTSN (couches 3 à 5 et axes de la cartographie cible). Il est porté par le frontmatter des `cap-int-*.md` et sert d’en-tête de section dans `01_cnisn/02_capacites.md` (voir [annexe B](../01_cnisn/08_annexes/b-articulation-art-sn.md)).

## Relations d'architecture (alignement ArchiMate)

Le référentiel suit le modèle de relations d'ArchiMate : la **capacité** est le pivot stable, le **flux de valeur** la justifie (à quoi elle sert), le **processus métier** l'opérationnalise (comment), et le **composant applicatif** la rend numériquement possible. Chaque relation est portée par le champ frontmatter adéquat et sa **direction** (objet source -> objet cible) encode le type ArchiMate.

| Source | Champ | Cible | Relation ArchiMate | Sémantique |
|--------|-------|-------|--------------------|------------|
| Flux de valeur (VS) | `applies_to` | Capacité (CAP) | Capability *enables* / *serves* Value Stream | la capacité rend le flux possible |
| Flux de valeur (VS) | `applies_to` | Partie prenante (PP) | Value Stream *serves* Stakeholder | le flux crée de la valeur pour le partie prenante |
| Flux de valeur (VS) | `related` | Processus (PRC) | Value Stream *realized by* Business Process | lien direct flux -> processus |
| Capacité (CAP) | `related` | VS / PRC | inverse de enable / realize | navigabilité (coté capacité) |
| Processus (PRC) | `applies_to` | Capacité (CAP) | Business Process *realizes* Capability | le processus réalise la capacité |
| Processus (PRC) | `related` | Étape de valeur (EV) | Business Process *contributes to* Value | déclenchement dans une étape de flux |
| Processus (PRC) | `uses` | Composant (CMP) | Business Process *served by* Application Component | le processus utilise le composant |
| Composant (CMP) | `applies_to` | Processus (PRC) | Application Component *serves* Business Process | inverse de `uses` (coté composant applicatif uniquement) |
| Composant (CMP) | `implements` | Chapitre (ART) | Application Component *realizes* Requirement | met en oeuvre la norme |
| Composant (CMP) | `maps_to` | Capacité CNISN (CAP-INT) | Alignment | aligne la capacité ARTSN sur la capacité CNISN |
| Composant applicatif (CMP-01..25) | `uses` | Infrastructure (CMP-26..31) | Application Component *uses* Technology service | le composant applicatif utilise le socle infrastructural |
| Composant applicatif (CMP-01..25) | `uses` | Sécurité (CMP-32..38) | Application Component *uses* Security service | le composant applicatif consomme les services de securite |
| Sécurité (CMP-32..38) | `uses` | Infrastructure (CMP-26..31) | Security component *uses* Technology service | la securite utilise l'infrastructure |
| Gouvernance (CMP-39..46) | `governs` | Composant (CMP) | Governance element *governs* Component | l'organe/registre de gouvernance encadre le composant |
| Acteur (ACT) | `represents` | Partie prenante (PP) | Business Actor *realization* Stakeholder | l'acteur opérationnalise la partie prenante |
| Partie prenante (PP) | `represented_by` | Acteur (ACT) | inverse de `represents` | navigabilité (coté partie prenante) |
| Rôle (ROL) | `assigned_to` | Acteur (ACT) | Role *assignment* Actor | le rôle est assigné à l'acteur |
| Acteur (ACT) | `has_role` | Rôle (ROL) | inverse de `assigned_to` | navigabilité (coté acteur) |
| Rôle / Acteur (ROL/ACT) | `performs` | Processus (PRC) | Role/Actor *assignment* Business Process | le rôle ou l'acteur réalise le processus |
| Processus (PRC) | `performed_by` | Rôle / Acteur (ROL/ACT) | inverse de `performs` | navigabilité (coté processus) |
| Acteur / Composant / Service / Capacité | `located_at` | Lieu (LOC) | Association géographique | la ressource est localisée sur le territoire |
| Service (SRV) | `serves` | Partie prenante / Acteur | Service *serving* Stakeholder | le service crée de la valeur pour le bénéficiaire |
| Service / Composant / Processus | `accesses` | Objet métier / Objet de données | Application/Component *access* Data Object | le service consomme / produit l'objet |
| Objet métier / Objet de données | `accessed_by` | Service / Composant / Processus | inverse de `accesses` | navigabilité (coté objet) |
| Service (SRV) | `realizes` / `implements` | Capacité (CAP/CAP-INT) / Chapitre (ART) | Service *realization* Capability/Requirement | le service met en œuvre la capacité |
| Capacité / Composant / Service | `realized_by` | Service / Paquet de travail / Plateau | inverse de `realizes` | navigabilité (coté capacité) |
| Paquet de travail (WP) | `realizes` | Capacité / Composant / Service | Work Package *realization* | le lot réalise la capacité / le composant |
| Paquet de travail (WP) | `contributes_to` | Plateau (PL) | Association | le lot contribue à l'état cible |
| Plateau (PL) | `precedes` | Plateau (PL) | Ordre temporel | séquence de la roadmap |
| Plateau (PL) | `realizes` | Capacité (CAP/CAP-INT) | Plateau *realization* Capability | l'état cible couvre la capacité |
| Écart (GAP) | `between` | Plateau, Plateau | Association | écart de couverture entre deux états |

Règle d'intégrité : un flux de valeur ne doit laisser aucune capacité orpheline ; chaque processus liste ses capacités réalisées de façon **granulaire** (pas par copie du flux parent) ; `uses` (PRC -> CMP applicatif) et `applies_to` (CMP applicatif -> PRC) sont les deux sens d'une même relation *service* et doivent rester cohérents. Le socle transverse (infrastructure CMP-26..31, securite CMP-32..38) n'est **pas** lié directement aux processus : il est atteint via `uses` depuis les composants applicatifs. La gouvernance (CMP-39..46) n'utilise pas `uses` ; elle encadre les composants via `governs`.

## Registre des objets

Le registre central de tous les objets est `referentiel/_index.yaml` : id, type, niveau, chemin, statut. Il est la source de vérité pour la vérification des comptes et la détection de perte pendant la migration.

## Couverture des concepts ArchiMate

Matrice de présence des concepts ArchiMate dans le référentiel (avant/après l'extension). Statut : `✓` couvert, `(plan)` à créer, `—` hors périmètre.

| Couche ArchiMate | Concept | Type HEA | Statut |
|---|---|---|---|
| Motivation | Driver / Assessment | — | hors périmètre (capturé par `contrainte`/`principe`) |
| Motivation | Goal / Objective | `capacite` (CAP) | ✓ |
| Motivation | Requirement | `chapitre` (ART) | ✓ |
| Motivation | Principle | `principe` (PA/PD) | ✓ |
| Motivation | Stakeholder | `partie-prenante` (PP) | ✓ |
| Motivation | Value | `flux-de-valeur` (VS) | ✓ |
| Strategy | Capability | `capacite` (CAP/CAP-INT) | ✓ |
| Strategy | Resource / Course of Action | — | hors périmètre |
| Business | Value Stream | `flux-de-valeur` (VS) | ✓ |
| Business | Process | `processus` (PRC) | ✓ |
| Business | Actor | `acteur` (ACT) | (plan) |
| Business | Role | `role` (ROL) | (plan) |
| Business | Collaboration | — | hors périmètre |
| Business | Location | `lieu` (LOC) | (plan) |
| Business | Object | `objet-metier` (BO) / `objet-de-donnees` (DO) | ✓ |
| Business | Function / Event / Product / Contract | — | hors périmètre |
| Business | Business Service | `service` (`categorie: business`) | (plan) |
| Application | Component | `composant` (CMP) | ✓ |
| Application | Service / Function / Interface | `service` (`categorie: applicatif`) | (plan) |
| Technology | Component / Service / Node | `composant` (CMP infra) / `service` (`categorie: technologique`) | (plan) |
| Physical | Device / Equipment / Material / Facility | — | hors périmètre |
| Implementation & Migration | Work Package | `work-package` (WP) | (plan) |
| Implementation & Migration | Plateau | `plateau` (PL) | (plan) |
| Implementation & Migration | Gap | `gap` (GAP) | (plan) |
| Implementation & Migration | Deliverable | — | hors périmètre |

Sémantique des relations ArchiMate : les 13 types natifs sont projetés sur un sous-ensemble réduit de champs typés bidirectionnels. Les relations restantes (Composition/Aggregation/Specialization/Junction) ne sont pas modélisées explicitement — la composition est implicite dans l'arborescence des dossiers et la hiérarchie `capacite`/`sous-capacite`.

| Relation ArchiMate | Champ HEA | Bidirectionnel |
|---|---|---|
| Realization (Actor↔Stakeholder) | `represents` / `represented_by` | oui |
| Assignment (Role↔Actor) | `assigned_to` / `has_role` | oui |
| Assignment (Role↔Process) | `performs` / `performed_by` | oui |
| Association (géo) | `located_at` | oui |
| Serving (Service↔Stakeholder) | `serves` | oui |
| Access (Service↔Data) | `accesses` / `accessed_by` | oui |
| Realization (Service↔Capability) | `realizes` / `realized_by` | oui |
| Realization (WorkPackage↔Capability) | `realizes` / `realized_by` | oui |
| Realization (Plateau↔Capability) | `realizes` / `realized_by` | oui |
| Triggering / Flow | `uses` (PRC→CMP) | oui |
| Association (gouvernance) | `governs` | oui |
| Association (roadmap) | `contributes_to` / `precedes` / `between` | oui |

Les champs ci-dessus s'ajoutent aux champs existants documentés plus haut (`related`, `uses`, `maps_to`, `applies_to`, `implements`, `governs`). La règle d'intégrité transverse reste : tout `uses` (PRC→CMP) doit avoir son `applies_to` inverse (CMP→PRC), et tout `realizes` doit avoir son `realized_by` correspondant.
