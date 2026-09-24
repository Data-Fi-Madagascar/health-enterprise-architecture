---
domain: 00_metamodel
title: Schéma du référentiel
id: SCHEMA-REFERENTIEL
type: meta
niveau: "0"
status: draft
version: "1.0"
owner: DEPSI
envelope: 04_architecture-repository/00_metamodel/schema.md
tags: ["referentiel", "schema", "gouvernance"]
---

# Schéma du référentiel

Ce document définit le modèle d’objets du référentiel. Il est la source de vérité pour la structure, le nommage et le frontmatter de tout objet.

## Principe

- **Un objet = un fichier** dans un répertoire de couche TOGAF sous `04_architecture-repository/`.
- Chaque objet est un bloc de contenu **auto-portant** : il n’a pas besoin du reste du document d’origine pour être compris.
- Les documents historiques ne conservent que la **prose narrative**, les catalogues et les matrices ; ils **référencent** les objets par lien.
- Le frontmatter est la seule source des **métadonnées de gouvernance** (statut, propriétaire, version, relations).

## Types d’objets et répertoires

| Type | Statut | Répertoire | Préfixe d’id | Sources |
|------|--------|------------|--------------|---------|
| `architecture-partition` | actif | `04_architecture-repository/01_partitions/<famille>/` | `part-` | partitions TOGAF |
| `repository-view` | non indexé | `04_architecture-repository/01_partitions/index.md` et `04_architecture-repository/08_views/togaf/` | `view-` | vues dérivées TOGAF |
| `stakeholder` | actif | `04_architecture-repository/02_architecture-elements/motivation/stakeholders/` | `pp-` | parties prenantes CAESN |
| `business-value` | actif | `04_architecture-repository/02_architecture-elements/motivation/values/` | `val-` | valeurs CAESN |
| `principe` | actif | `04_architecture-repository/02_architecture-elements/motivation/principles/` | `p-`, `p-int-`, `pa-`, `pd-` | principes CAESN et CNISN |
| `flux-valeur` | actif | `04_architecture-repository/02_architecture-elements/strategy/value-streams/` | `vs-` | flux de valeur CAESN |
| `capabilite` | actif | `04_architecture-repository/02_architecture-elements/strategy/capabilities/` | `cap-` | capacités CAESN |
| `etape-valeur` | actif | `04_architecture-repository/02_architecture-elements/strategy/value-stages/` | `ev-` | étapes de valeur CAESN |
| `acteur` | actif | `04_architecture-repository/02_architecture-elements/business/actors/` | `act-` | acteurs métier CAESN |
| `role` | actif | `04_architecture-repository/02_architecture-elements/business/roles/` | `rol-` | rôles métier CAESN |
| `business-location` | actif | `04_architecture-repository/02_architecture-elements/business/locations/` | `loc-` | localisations métier |
| `processus-metier` | actif | `04_architecture-repository/02_architecture-elements/business/processes/` | `prc-` | processus métier CAESN |
| `objet-metier` | actif | `04_architecture-repository/02_architecture-elements/business/business-objects/` | `bo-` | objets métier CAESN |
| `service` | actif legacy conservé | `04_architecture-repository/02_architecture-elements/business/business-services/` pour `SRV-01` ; `04_architecture-repository/05_building-blocks/abb/legacy-services/` pour `SRV-02..06` | `srv-` | services transverses |
| `objet-de-donnees` | actif | `04_architecture-repository/02_architecture-elements/data/data-objects/` | `p-`, `s-`, `d-`, `f-`, `r-`, `e-`, `t-` | objets de données ARTSN |
| `reference-data` | actif | `04_architecture-repository/02_architecture-elements/data/reference-data/` | `ref-` | données de référence |
| `terminology` | actif | `04_architecture-repository/02_architecture-elements/data/terminologies/` | `term-` | terminologies |
| `exigence` | actif | `04_architecture-repository/03_requirements/` | `enf-`, `ex-` | exigences ARTSN |
| `architecture-pattern` | actif | `04_architecture-repository/04_patterns/<famille>/` | `pat-` | patrons et règles ARTSN |
| `architecture-building-block` | actif | `04_architecture-repository/05_building-blocks/abb/` | `abb-` | building blocks d'architecture |
| `solution-building-block` | actif | `04_architecture-repository/05_building-blocks/sbb/` | `sbb-` | building blocks de solution |
| `architecture-contract` | actif | `04_architecture-repository/06_governance/architecture-contracts/` | `contract-` | contrats d'architecture |
| `compliance-rule` | actif | `04_architecture-repository/06_governance/compliance/` | `cmp-rule-` | règles de conformité |
| `evidence` | actif | `04_architecture-repository/06_governance/evidence/` | `evd-` | preuves de conformité |
| `work-package` | actif | `04_architecture-repository/07_migration/work-packages/` | `wp-` | paquets de travail |
| `plateau` | actif | `04_architecture-repository/07_migration/plateaux/` | `pl-` | états cibles de l'architecture |
| `gap` | actif | `04_architecture-repository/07_migration/gaps/` | `gap-` | écarts entre plateaux |
| `fondation` | legacy conservé | `04_architecture-repository/04_patterns/foundations/` | `f-` | fondations ARTSN existantes |
| `chapitre` | legacy conservé | `04_architecture-repository/04_patterns/artsn-rules/` | `art-` | règles ARTSN existantes |
| `composant-applicatif` | legacy conservé | `04_architecture-repository/05_building-blocks/abb/legacy-components/` | `cmp-` | composants applicatifs CMP-01..25 |
| `composant-infrastructure` | legacy conservé | `04_architecture-repository/05_building-blocks/abb/legacy-components/` | `cmp-` | composants d'infrastructure CMP-26..31 |
| `composant-securite` | legacy conservé | `04_architecture-repository/05_building-blocks/abb/legacy-components/` | `cmp-` | composants de sécurité CMP-32..38 |
| `profil` | legacy conservé | `04_architecture-repository/05_building-blocks/sbb/legacy-profiles/` | `pt-` | profils PTISN existants |
| `registre-gouvernance` | legacy conservé | `04_architecture-repository/06_governance/registers/` | `cmp-` | registres de gouvernance CMP-39..46 |
| `partie-prenante` | legacy conservé | `04_architecture-repository/02_architecture-elements/motivation/stakeholders/` | `pp-` | ancien nom de type pour `stakeholder` |
| `valeur` | legacy conservé | `04_architecture-repository/02_architecture-elements/motivation/values/` | `val-` | ancien nom de type pour `business-value` |
| `lieu` | legacy conservé | `04_architecture-repository/02_architecture-elements/business/locations/` | `loc-` | ancien nom de type pour `business-location` |
| `capacite` | supprimé des objets actifs | aucune fiche active | n/a | ancien type d'interopérabilité interdit par `scripts/validate_ref.py` |
| `meta` | non indexé | `04_architecture-repository/00_metamodel/` | `schema` | métamodèle et documentation technique |

## Conventions de nommage

- **Dossier** : nom court en kebab-case, singulier (`principes`, pas `principes/domaine`).
- **Fichier** : `<id>-slugified.md`, id minuscule en kebab-case.
- Normalisation des identifiants pendant la migration : `P-INT-01` → fichier `p-int-01.md` ; `ABB-REGISTRE-PROFESSIONNELS` → `abb-registre-professionnels.md` ; `ART-4A` → `art-4a.md` ; `F.5` → `f-5.md` ; `PT-01` → `pt-01.md`. Les anciens identifiants d'interopérabilité ne sont conservés que dans `legacy_id` et dans la table de migration.
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
maps_to: ["ABB-IDENTITE-BENEFICIAIRE"]   # correspondance vers autre référentiel (id)
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
| `status` | oui | `draft`, `active`, `stable`, `candidate` ou `deprecated` |
| `owner` | oui | Responsable / entité de gouvernance |
| `version` | non | Version héritée du document source |
| `envelope` | conditionnel | Chemin du document d’origine ou du document enveloppe publié. Obligatoire pour les objets transclus dans les documents publiés ; absent pour les partitions TOGAF autonomes et les vues dérivées non indexées |
| `family` | non | Famille de réponse documentaire, conservée uniquement lorsque le générateur en a besoin |
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

- [ABB-IDENTITE-BENEFICIAIRE — Résolution d'identité du bénéficiaire](../05_building-blocks/abb/abb-identite-beneficiaire.md)
```

- Le **contenu textuel** des objets n’est **pas reformulé** : il est copié tel quel depuis la source (seule la structure de titres peut être normalisée).
- Les relations transversales peuvent être portées par le frontmatter (`maps_to`, `implements`, `applies_to`, `related`) et/ou par une section `## Liens` en fin d’objet.
- La **prose narrative** (paragraphes « pour qui lire », légendes, introductions) **reste dans le document source** et n’est pas dupliquée dans les objets.
- Le champ `legacy_id` porte la traçabilité des anciens bundles d'interopérabilité. Il ne constitue jamais une cible de relation active : les relations exploitables pointent vers les objets TOGAF de remplacement ou vers les capabilités CAESN `CAP-*`.

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
| Composant (CMP) | `maps_to` | Objet d'interopérabilité CNISN/TOGAF ou capabilité CAESN | Alignment | aligne le composant sur l'objet de référence ou la capabilité cible |
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
| Service (SRV) | `realizes` / `implements` | Capabilité CAESN / objet CNISN/TOGAF / chapitre ART | Service *realization* Capability/Requirement | le service met en œuvre l'objet ou la capabilité |
| Capacité / Composant / Service | `realized_by` | Service / Paquet de travail / Plateau | inverse de `realizes` | navigabilité (coté capacité) |
| Paquet de travail (WP) | `realizes` | Capacité / Composant / Service | Work Package *realization* | le lot réalise la capacité / le composant |
| Paquet de travail (WP) | `contributes_to` | Plateau (PL) | Association | le lot contribue à l'état cible |
| Plateau (PL) | `precedes` | Plateau (PL) | Ordre temporel | séquence de la roadmap |
| Plateau (PL) | `realizes` | Capabilité CAESN / objet CNISN/TOGAF | Plateau *realization* Capability | l'état cible couvre l'objet ou la capabilité |
| Écart (GAP) | `between` | Plateau, Plateau | Association | écart de couverture entre deux états |

Règle d'intégrité : un flux de valeur ne doit laisser aucune capacité orpheline ; chaque processus liste ses capacités réalisées de façon **granulaire** (pas par copie du flux parent) ; `uses` (PRC -> CMP applicatif) et `applies_to` (CMP applicatif -> PRC) sont les deux sens d'une même relation *service* et doivent rester cohérents. Le socle transverse (infrastructure CMP-26..31, securite CMP-32..38) n'est **pas** lié directement aux processus : il est atteint via `uses` depuis les composants applicatifs. La gouvernance (CMP-39..46) n'utilise pas `uses` ; elle encadre les composants via `governs`.

## Registre des objets

Le registre central de tous les objets est `04_architecture-repository/_index.yaml` : id, type, niveau, chemin, statut. Il est la source de vérité pour la vérification des comptes et la détection de perte pendant la migration.

## Couverture des concepts ArchiMate

Matrice de présence des concepts ArchiMate dans le référentiel après le placement TOGAF. Statut : `✓` couvert, `(plan)` à créer, `N/A` hors périmètre.

| Couche ArchiMate | Concept | Type HEA | Statut |
|---|---|---|---|
| Motivation | Driver / Assessment | `principe` / `exigence` | couverture indirecte |
| Motivation | Goal / Objective | `capabilite` (CAP) | ✓ |
| Motivation | Requirement | `exigence`, legacy `chapitre` (ART), futur `architecture-contract` / `compliance-rule` | ✓ |
| Motivation | Principle | `principe` (PA/PD) | ✓ |
| Motivation | Stakeholder | `stakeholder`, legacy `partie-prenante` (PP) | ✓ |
| Motivation | Value | `business-value`, legacy `valeur` | ✓ |
| Strategy | Capability | `capabilite` (CAP) | ✓ |
| Strategy | Resource / Course of Action | N/A | hors périmètre |
| Business | Value Stream | `flux-de-valeur` (VS) | ✓ |
| Business | Process | `processus-metier` (PRC) | ✓ |
| Business | Actor | `acteur` (ACT) | ✓ |
| Business | Role | `role` (ROL) | ✓ |
| Business | Collaboration | N/A | hors périmètre |
| Business | Location | `business-location`, legacy `lieu` (LOC) | ✓ |
| Business | Object | `objet-metier` (BO) / `objet-de-donnees` (DO) | ✓ |
| Business | Function / Event / Product / Contract | N/A | hors périmètre |
| Business | Business Service | `service` dans `business-services` | ✓ |
| Application | Component | futur `architecture-building-block`, legacy `composant-applicatif` (CMP) | ✓ |
| Application | Service / Function / Interface | `service` (`categorie: applicatif`) | ✓ |
| Technology | Component / Service / Node | futur `architecture-building-block`, legacy `composant-infrastructure` / `service` technologique | ✓ |
| Physical | Device / Equipment / Material / Facility | N/A | hors périmètre |
| Implementation & Migration | Work Package | `work-package` (WP) | ✓ |
| Implementation & Migration | Plateau | `plateau` (PL) | ✓ |
| Implementation & Migration | Gap | `gap` (GAP) | ✓ |
| Implementation & Migration | Deliverable | N/A | hors périmètre |

Sémantique des relations ArchiMate : les 13 types natifs sont projetés sur un sous-ensemble réduit de champs typés bidirectionnels. Les relations restantes (Composition/Aggregation/Specialization/Junction) ne sont pas modélisées explicitement ; la composition est implicite dans l'arborescence des dossiers et la hiérarchie `capabilite` / `capacite` legacy.

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
