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
| `accesses` | non | Accès à un objet de données ou à une terminologie, dans ses deux emplois : le processus qui manipule la donnée et le composant, le service ou le bloc qui la détient. ArchiMate Access |
| `accessed_by` | non | Inverse de `accesses` (coté objet de données ou terminologie). Sur un objet de données, la liste mêle les deux emplois : le processus y figure pour la manipulation, le composant pour la détention |
| `constrained_by` | non | Objet de données dont les valeurs sont codées par une terminologie : Association sémantique (extension HEA) |
| `constrains` | non | Inverse de `constrained_by` (coté terminologie) |
| `realizes` | non | Service / paquet de travail / plateau réalise une capacité, composant ou service — ArchiMate Realization |
| `realized_by` | non | Inverse de `realizes` (coté capacité / composant / service) |
| `contributes_to` | non | Paquet de travail contribue à un plateau |
| `precedes` | non | Plateau précède un autre plateau (ordre temporel) |
| `between` | non | Écart (gap) entre deux plateaux |
| `gap_state` | obligatoire pour `gap` | État opérationnel : `identified`, `planned`, `in-remediation`, `closed` ou `accepted-risk`. Distinct du cycle documentaire `status` |
| `target_plateau` | obligatoire pour `gap` | Relation vers exactement un objet de type `plateau`, également présent dans `between` |
| `addressed_by` | obligatoire pour `gap` | Relation vers un ou plusieurs objets de type `work-package` responsables de la remédiation |
| `evidenced_by` | obligatoire pour `gap` | Relation vers un ou plusieurs objets de type `evidence` spécifiant les preuves de fermeture |
| `closure_criteria` | obligatoire pour `gap` | Liste non vide de critères courts et vérifiables. Cette propriété n'est pas une relation |
| `tier` | obligatoire pour `objet-de-donnees` | Classement de criticité de la donnée : `A` (référentiel et pilotage), `B` (transactionnel et opérationnel), `C` (appui analytique). Cette propriété n'est pas une relation |
| `system_of_record` | obligatoire pour `objet-de-donnees` | Système(s) qui détiennent la version faisant foi de l'objet. Cible un composant applicatif ou un bloc d'architecture. Cette propriété n'est pas une relation |
| `absorbs` | non | Identifiants d'objets de données retirés par fusion dans cet objet. Cette propriété n'est pas une relation : elle est confrontée à `00_metamodel/do-migration.yaml` par `scripts/validate_ref.py` |
| `theme` | obligatoire pour `objet-de-donnees` | Thème de données auquel l'objet appartient. La valeur appartient au vocabulaire contrôlé de `00_metamodel/themes.yaml`, qui porte pour chaque thème son libellé, sa description et les flux de valeur qu'il dessert. Cette propriété n'est pas une relation : elle n'apparaît ni comme arête du graphe ni comme cible de relation. Elle est confrontée à `00_metamodel/object-migration.yaml` par `scripts/validate_ref.py` |
| `fhir_resources` | obligatoire pour `objet-de-donnees` | Liste des ressources FHIR R4 par lesquelles l'objet s'échange. Cette déclaration est la source unique de vérité de la projection FHIR : le compilateur produit une StructureDefinition par ressource déclarée et n'en dérive aucune. Contrôlée par `scripts/compilers/compile_fhir.py` |
| `categorie` | non | Sous-couche ArchiMate de l'objet : `applicatif`, `infrastructure`, `securite`, `principe`, `regulation`, `acteur`, `work-package`, `data-object` |
| `governs` | non | Liens typés : element de gouvernance qui encadre/valide un composant (sens gouvernance -> composant) |
| `partition_kind` | conditionnel | Catégorie d'une `architecture-partition` : `value-stream`, `transverse`, `sectorielle` ou `externe` |
| `togaf_repository_section` | conditionnel | Section TOGAF qui gouverne l'objet : `architecture-landscape`, `standards-information-base`, `reference-library`, `governance-log` ou `requirements-repository` |
| `togaf_adm_phase` | conditionnel | Phase ADM principale qui produit ou gouverne l'objet : `B`, `C`, `D`, `G` ou `Requirements Management` |
| `architecture_level` | conditionnel | Niveau d'architecture : `enterprise-transversal`, `segment` ou `extended-enterprise` |
| `architecture_domain` | conditionnel | Domaine principal : `motivation`, `business`, `data`, `application`, `technology` ou `governance` |
| `architecture_scope` | conditionnel | Portée gouvernée : `value-stream`, `transverse`, `interoperability`, `one-health` ou `cross-border-exchange` |
| `architecture_state` | conditionnel | État temporel de l'architecture. La valeur actuellement contrôlée est `target` |
| `partitions` | non | Relation vers une ou plusieurs cibles de type `architecture-partition`. Toute autre cible est invalide |
| `building_block_role` | conditionnel | Rôle TOGAF du bloc. Les blocs d'architecture portent la valeur `ABB` |
| `building_block_domain` | conditionnel | Domaine de réalisation du bloc : `data`, `application` ou `technology` |
| `legacy_id` | non | Identifiant ou liste d'identifiants historiques conservés uniquement pour la traçabilité de migration |
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
- Le champ `partitions` rattache un objet à son périmètre de gouvernance TOGAF. Le validateur résout chaque identifiant et impose le type cible `architecture-partition`.

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
| Processus métier (PRC) | `accesses` | Objet de données (DO) | Business Process *access* Data Object | le processus manipule la donnée : il la produit, la met à jour ou la consomme |
| Composant / Service / Bloc (CMP, SRV, ABB) | `accesses` | Objet de données / Terminologie | Application Component *access* Data Object | le composant détient la donnée, la produit, l'expose ou la met à jour |
| Objet de données / Terminologie | `accessed_by` | Processus / Composant / Service | inverse de `accesses` | navigabilité (coté objet) |
| Objet de données (DO) | `maps_to` | Capacité CAESN (CAP) | Association (extension HEA) | l'objet de données est au service de la capacité déclarée |
| Objet de données (DO) | `constrained_by` | Terminologie (TERM) | Association sémantique (extension HEA) | les valeurs portées par l'objet sont codées par la terminologie |
| Terminologie (TERM) | `constrains` | Objet de données (DO) | inverse de `constrained_by` | navigabilité (coté terminologie) |
| Service (SRV) | `realizes` / `implements` | Capabilité CAESN / objet CNISN/TOGAF / chapitre ART | Service *realization* Capability/Requirement | le service met en œuvre l'objet ou la capabilité |
| Capacité / Composant / Service | `realized_by` | Service / Paquet de travail / Plateau | inverse de `realizes` | navigabilité (coté capacité) |
| Paquet de travail (WP) | `realizes` | Capacité / Composant / Service | Work Package *realization* | le lot réalise la capacité / le composant |
| Paquet de travail (WP) | `contributes_to` | Plateau (PL) | Association | le lot contribue à l'état cible |
| Plateau (PL) | `precedes` | Plateau (PL) | Ordre temporel | séquence de la roadmap |
| Plateau (PL) | `realizes` | Capabilité CAESN / objet CNISN/TOGAF | Plateau *realization* Capability | l'état cible couvre l'objet ou la capabilité |
| Écart (GAP) | `between` | Plateau, Plateau | Association | écart de couverture entre deux états |
| Écart (GAP) | `target_plateau` | Plateau (PL) | Association | état cible unique de la remédiation, inclus dans `between` |
| Écart (GAP) | `addressed_by` | Paquet de travail (WP) | Association | paquet responsable de la fermeture de l'écart |
| Écart (GAP) | `evidenced_by` | Preuve (EVID) | Association | spécification des pièces attendues pour démontrer la fermeture |

### Gouvernance opérationnelle des gaps

Le champ général `status` décrit la maturité documentaire de la fiche. Le champ
`gap_state` décrit séparément l'avancement de la remédiation. Un gap conforme
porte exactement un plateau cible, au moins un paquet de travail responsable,
au moins une preuve attendue et une liste non vide de critères de fermeture.

```yaml
gap_state: planned
target_plateau: [PL-02]
addressed_by: [WP-02]
evidenced_by: [EVID-GAP-01-QUALIFICATION-OFFLINE]
closure_criteria: ["Qualification terrain acceptée", "Synchronisation sans perte démontrée"]
```

Règle d'intégrité : un flux de valeur ne doit laisser aucune capacité orpheline ; chaque processus liste ses capacités réalisées de façon **granulaire** (pas par copie du flux parent) ; `uses` (PRC -> CMP applicatif) et `applies_to` (CMP applicatif -> PRC) sont les deux sens d'une même relation *service* et doivent rester cohérents. De même, `accesses` et `accessed_by` décrivent un seul et même accès, mais cet accès porte deux énoncés distincts : le processus qui manipule la donnée et le composant qui la détient. Ces deux énoncés ne se déduisent pas l'un de l'autre et ne se substituent pas l'un à l'autre. De la même manière, `constrained_by` (objet de données -> terminologie) et `constrains` (terminologie -> objet de données) une seule et même contrainte de codage. Le socle transverse (infrastructure CMP-26..31, securite CMP-32..38) n'est **pas** lié directement aux processus : il est atteint via `uses` depuis les composants applicatifs. La gouvernance (CMP-39..46) n'utilise pas `uses` ; elle encadre les composants via `governs`.

## Chaîne à quatre couches

Le référentiel n'est pas une collection d'objets juxtaposés : il articule quatre couches de sens, chacune portée par un type d'objet distinct, et il relie ces couches par deux ponts qui rendent la chaîne vérifiable de bout en bout. Cette structure répond à une question simple que tout lecteur d'architecture doit pouvoir poser à n'importe quel objet : à quoi cette donnée sert, qui la produit, comment elle est codée.

| Couche | Question à laquelle elle répond | Type d'objet | Plage d'identifiants | Relation porteuse |
|---------|-------------------------------|--------------|----------------------|-------------------|
| 1. Business | Que le système de santé doit-il garantir au citoyen ? | `capabilite` | CAP-01 à CAP-18 | `applies_to` porté par le processus (PRC vers CAP) |
| 2. Application | Par quel moyen numérique la capacité est-elle tenue ? | `composant-applicatif` | CMP-01 à CMP-25 | `uses` porté par le processus (PRC vers CMP), `applies_to` porté par le composant (CMP vers PRC) |
| 3. Données | Sur quelles données la capacité opère-t-elle ? | `objet-de-donnees` | 23 objets canoniques (plage DO-01 à DO-32, neuf identifiants retirés par fusion) | `accesses` porté par le composant (CMP vers DO) et par le processus (PRC vers DO), `accessed_by` porté par l'objet (DO vers PRC et CMP), `maps_to` porté par l'objet (DO vers CAP) |
| 4. Sémantique | Selon quel référentiel de codes les données sont-elles interprétées ? | `terminology` | TERM-CODIFICATION-COMMUNE et les six terminologies de codes publics (TERM-SNOMED-CT, TERM-RXNORM, TERM-ATC, TERM-DCI, TERM-CIM-11, TERM-LOINC) | `constrained_by` porté par l'objet (DO vers TERM), `constrains` porté par la terminologie (TERM vers DO) |

### Les deux emplois de l'accès aux données

La relation `accesses` relie un acteur à un objet de données, mais elle porte deux énoncés de nature différente. Le premier est déclaratif : le processus métier qui manipule la donnée, c'est-à-dire celle qu'il produit, met à jour ou consomme. Le second est technique : le composant, le service ou le bloc d'architecture qui détient la donnée, la produit, l'expose ou la met à jour. Le premier répond à la question « à quelle activité la donnée est-elle adossée », le second à la question « où la donnée est-elle logée et qui la tient ».

Les deux énoncés sont nécessaires et aucun ne se déduit de l'autre. L'état mesuré du corpus le montre. Sur les vingt-trois objets de données, quarante-neuf arêtes relient un processus à un objet et soixante-quinze relient un composant, un service ou un bloc. Les quarante-neuf arêtes de processus se déduisent désormais de la chaîne `PRC` vers `CMP` vers `DO` : chaque processus qui manipule une donnée mobilise au moins un composant qui la porte. À l'inverse, vingt des soixante-quinze arêtes de la couche technique ne sont pas restituables par la chaîne. Leurs dix porteurs sont le composant applicatif de référentiel CMP-05, cinq services d'interface (SRV-02 à SRV-06), les deux blocs d'architecture ABB-ELIGIBILITE-COUVERTURE et ABB-REFERENTIEL-STRUCTURES-SERVICES, et les deux autorités de certification CMP-35 et CMP-36 : aucun processus déclaré ne les mobilise. Aucun objet de données ne peut donc être ramené à l'une de ses deux extrémités, et les deux familles d'acteurs ne sont pas interchangeables.

Cette distinction explique la forme du champ `accessed_by` porté par un objet de données, qui mêle les deux familles d'acteurs et que le lecteur doit savoir lire en deux temps. Elle n'autorise pas pour autant à les confondre. Le validateur refuse un processus qui manipule un objet sans mobiliser de composant qui le porte, et il refuse un système de référence qui n'accède pas à l'objet dont il est censé détenir la version faisant foi.

### La projection FHIR des objets de données

La couche données ne se contente pas de nommer ses objets : elle désigne, pour chacun d'eux, la ressource par laquelle il s'échange. Cette désignation est portée par la déclaration `fhir_resources` du frontmatter de l'objet de données, et elle est la source unique de vérité de la projection FHIR. Le compilateur `scripts/compilers/compile_fhir.py` ne dérive le type d'aucune ressource d'une table de correspondance interne, ni du libellé de type rédigé dans le corps du document : il lit la déclaration, et produit une StructureDefinition par ressource déclarée, de type et d'identifiant conformes à cette déclaration. Un objet qui porte un bloc `fhir:` décrivant ses contraintes de cardinalité, de typage, de liaison terminologique et de découpage en tranches d'identifiants voit ce bloc devenir le différentiel du profil produit, appliqué à la ressource qu'il déclare comme base.

Cette règle prolonge le principe qui préside à l'ensemble de la chaîne : la déclaration portée par la source fait foi, et le compilateur la projette sans la contredire. Elle ne vaut cependant que si la ressource déclarée est échangeable dans la version visée. Le compilateur embarque le vocabulaire des cent quarante-neuf ressources du paquet FHIR R4 ainsi que le niveau de maturité FMM que HL7 publie pour chacune d'elles dans l'index des ressources. Une ressource déclarée doit exister dans ce paquet et porter un niveau de maturité d'au moins un : le niveau zéro signifie que la ressource est publiée dans la version mais que le groupe de travail responsable ne la considère pas prête pour l'implémentation, ce qui la rend impropre à fonder une projection normative nationale. Les ressources normatives de l'index R4, qui ne portent pas de niveau numérique, sont admises.

Le répertoire de sortie appartient en outre au compilateur. À chaque compilation, celui-ci supprime les fichiers qu'il a produits et qui ne correspondent plus à une déclaration du corpus. Le répertoire contient donc, à tout instant, exactement la projection effective du corpus, ni plus ni moins : la question de savoir si un artefact est encore valide ne se pose plus, puisqu'il est présent, il l'est par construction.

L'état mesuré du corpus est le suivant : les vingt-trois objets de données déclarent trente-six ressources FHIR, toutes existantes dans le paquet R4 et toutes portresses d'un niveau de maturité d'au moins un. La projection produite compte trente-huit artefacts, soit trente-six StructureDefinition, une CodeSystem de codification commune et une ValueSet des types d'objets de données. Le compilateur échoue si une ressource déclarée ne produit pas exactement un artefact conforme, et si un artefact produit ne correspond à aucune déclaration.

### Les deux ponts et leur portée réelle

Les couches 1 et 2 sont historiquement portées par des relations déjà peuplées : un processus métier déclare les capacités qu'il réalise, et les composants applicatifs qu'il mobilise. Le référentiel s'arrêtait toutefois au milieu de la chaîne. Le pont vers les données n'existait qu'au niveau du processus : douze processus sur treize déclaraient les objets de données qu'ils manipulent, mais aucun des trente-huit composants ne déclarait l'objet de données qu'il porte. Le pont sémantique, lui, n'existait pas : une terminologie était atteinte par un service, mais aucun objet de données n'était jamais déclaré comme contraint par une terminologie. Trois conséquences en découlaient, toutes vérifiables dans le corpus avant correction.

- Un composant applicatif ne pouvait pas être caractérisé par les données qu'il détient, alors que cette caractérisation est la seule qui distingue un registre de terminologies d'un entrepôt analytique.
- Un objet de données ne pouvait pas dire sous quelles codifications ses valeurs doivent être interprétées, ce qui rendait impossible de garantir qu'une prescription échangée entre deux institutions désigne le même médicament.
- La traçabilité entre la capacité stratégique et le code utilisé sur le terrain s'arrêtait à la frontière du composant.

Le présent méta-modèle comble ces deux ponts : `accesses` devient une relation de premier rang pour les composants applicatifs, et `constrained_by` est introduit pour lier un objet de données à la terminologie qui en régit le codage.

### Exemple travaillé

La chaîne de référence est celle de la prescription de chimiothérapie. Le corpus ne comporte pas de capacité d'oncologie dédiée : la capacité de prise en charge du patient cancéreux se rattache à CAP-10 (Gestion des médicaments, vaccins, intrants et chaîne d'approvisionnement) et à CAP-01 (Offre de soins et continuité des services). La chaîne projetée dans le référentiel est la suivante.

| Couche | Objet du corpus | Identifiant |
|--------|-----------------|-------------|
| Business | Gestion des médicaments, vaccins, intrants et chaîne d'approvisionnement | CAP-10 |
| Business | Offre de soins et continuité des services | CAP-01 |
| Application (processus) | Prestation des soins cliniques | PRC-02 |
| Application (composant) | Dossiers et statistiques de santé (hôpitaux), système d'information hospitalier de base | CMP-19 |
| Données | Prescription, ressource FHIR MedicationRequest | DO-06 |
| Données (attribution de portée) | Capacités servies par cet objet : médicaments et chaîne d'approvisionnement, offre de soins et continuité | CAP-10, CAP-01 |
| Sémantique | Terminologie clinique SNOMED CT, codes de médicaments | TERM-SNOMED-CT |
| Sémantique | Terminologie RxNorm des médicaments, source de correspondance internationale | TERM-RXNORM |
| Sémantique | Classification ATC de l'OMS | TERM-ATC |

Cette projection illustre la fonction de chaque pont. Le pont applicatif relie la capacité à un actif numérique identifiable et versionnable. Le pont données relie cet actif à un objet de données dont la ressource d'échange est fixée (FHIR MedicationRequest pour DO-06), ce qui rend la matérialité de l'échange discutable avec un tiers. Le pont sémantique fixe enfin les référentiels de codes admis pour les valeurs de l'objet, ce qui conditionne la comparabilité des données entre institutions et la validité des indicateurs calculés au-dessus. L'attribution de portée referme la boucle en descendant : l'objet de données déclare les capacités qu'il sert, et le validateur confronte cette déclaration aux processus qui le manipulent pour s'assurer qu'au moins l'un d'eux réalise la capacité annoncée.

### Règles d'intégrité de la chaîne

| Règle | Portée | Contrôle |
|-------|--------|----------|
| Toute relation `accesses` (X vers Y) dispose de son inverse `accessed_by` (Y vers X) | Objets de données et terminologies | `scripts/validate_ref.py` |
| Toute arête `PRC` vers `DO` est adossée à un composant que le processus mobilise : ce composant déclare `accesses` vers l'objet | Objets de données et processus métiers | `scripts/validate_ref.py` |
| Tout `system_of_record` d'un objet de données déclare lui-même l'accès à cet objet (`accesses`), et figure parmi ses accesseurs | Objets de données | `scripts/validate_ref.py` |
| Toute relation `constrained_by` (DO vers TERM) dispose de son inverse `constrains` (TERM vers DO) | Objets de données et terminologies | `scripts/validate_ref.py` |
| `accesses` ne cible qu'un objet de données ou une terminologie | Composants, services, processus | `scripts/validate_ref.py` |
| `constrained_by` ne cible qu'une terminologie | Objets de données | `scripts/validate_ref.py` |
| `uses` (PRC vers CMP) et `applies_to` (CMP vers PRC) restent symétriques | Composants applicatifs | `scripts/validate_ref.py` |
| Tout objet de données est détenu par au moins un composant et manipulé par au moins un processus | Objets de données | `scripts/validate_ref.py` |
| Toute terminologie est portée par au moins un composant applicatif | Terminologies | `scripts/validate_ref.py` |
| Le `maps_to` d'un objet de données cible au moins une capacité CAESN, et uniquement des capacités | Objets de données | `scripts/validate_ref.py` |
| Toute capacité déclarée par le `maps_to` d'un objet de données est réalisée par au moins un processus qui manipule cet objet | Objets de données et processus métiers | `scripts/validate_ref.py` |
| Tout objet de données déclare un `tier` appartenant à `A`, `B` ou `C` | Objets de données | `scripts/validate_ref.py` |
| Tout objet de données déclare au moins un `system_of_record` ciblant un composant applicatif ou un bloc d'architecture | Objets de données | `scripts/validate_ref.py` |
| Tout identifiant listé dans `absorbs` est un objet de données retiré, et sa fusion est déclarée dans `00_metamodel/do-migration.yaml` | Objets de données | `scripts/validate_ref.py` |
| Aucun identifiant retiré par fusion ne subsiste comme objet actif ni comme cible de relation | Objets de données | `scripts/validate_ref.py` |
| Tout objet de données déclare exactement un `theme`, et ce thème figure dans le vocabulaire contrôlé de `00_metamodel/themes.yaml` | Objets de données | `scripts/validate_ref.py` |
| Chaque thème du vocabulaire contrôlé est porte par au moins un objet de données, et l'ensemble des objets d'un thème coïncide exactement avec la portée de l'objet retiré qui l'a créé | Objets de données et thèmes | `scripts/validate_ref.py` |
| Aucun identifiant retiré par décision d'architecture ne subsiste comme objet actif, comme cible de relation, ni comme mention en prose hors des documents de décision et des traces de migration | Objets retirés | `scripts/validate_ref.py` |
| Tout objet de données déclare au moins une ressource FHIR, et aucune ressource deux fois | Objets de données | `scripts/compilers/compile_fhir.py` |
| Toute ressource FHIR déclarée existe dans le paquet FHIR R4 et porte un niveau de maturité FMM d'au moins un | Objets de données | `scripts/compilers/compile_fhir.py` |
| Le bloc `fhir:` d'un objet de données déclare une base qui figure parmi les ressources déclarées | Objets de données | `scripts/compilers/compile_fhir.py` |
| Chaque ressource déclarée produit exactement une StructureDefinition, de type et d'identifiant conformes, et aucun artefact produit ne subsiste sans déclaration correspondante | Objets de données et artefacts FHIR | `scripts/compilers/compile_fhir.py` |

Ces règles sont strictes : le référentiel doit pouvoir être relu par un tiers sans reconstruire les relations à la main. L'état mesuré du corpus après correction est le suivant : sur les trente-huit composants, vingt-deux déclarent des objets de données portés, dont vingt composants applicatifs et les deux autorités de confiance CMP-35 et CMP-36 ; les treize processus déclarent tous leurs données ; les vingt-trois objets de données sont tous détenus et tous utilisés ; les sept terminologies sont toutes portées par un composant. Les vingt-trois objets de données déclarent en outre, via `maps_to`, les capacités CAESN qu'ils servent, et chacune de ces capacités est réalisée par au moins un processus qui manipule l'objet. L'attribution de portée n'est donc plus une mention portée à côté de la chaîne : elle en est le maillon, et le validateur refuse toute capacité déclarée dont aucun processus ne porterait la réalisation. Les quarante-neuf arêtes qui relient un processus à un objet de données sont toutes adossées à un composant que le processus mobilise, et chaque système de référence déclare lui-même l'accès à l'objet dont il détient la version faisant foi. Sur le plan de la projection FHIR, la porte de conformité ne trouve aucun cas : les vingt-trois objets déclarent trente-six ressources, toutes existantes dans le paquet R4 et toutes matures.

Une exception assumée existe pour les cinq composants de la couche de médiation (orchestrateur de parcours CMP-07, passerelle d'API CMP-15, registre de schémas CMP-16, courtier de messages CMP-17, compensateur de flux CMP-18) : ils transportent des objets de données sans être leur propriétaire, et ne déclarent donc pas d'`accesses` propre. Leur rattachement aux données est porté par les composants qui leur confient les flux. Le composant d'intégration CMP-06, qui assume la médiation de bout en bout, déclare en revanche les objets qu'il porte. Le socle transverse (infrastructure CMP-26 à CMP-31, sécurité CMP-32 à CMP-38) reste hors de la chaîne applicative par construction : il est atteint par `uses` depuis les composants qui l'exploitent et ne porte pas de données métier en propre.

Une seconde exception, nommée et strictement limitée, porte sur l'ancre de confiance DO-31. La PKI nationale CMP-35 et la passerelle de confiance mondiale CMP-36 en sont les autorités émettrices : ils émettent, publient et vérifient les certificats dont l'objet est fait. Ils déclarent donc l'accès à cet objet, contrairement au reste du socle de sécurité. Cette exception ne s'étend à aucune donnée métier et ne préfigure pas un rattachement général du socle transverse aux objets de données.

## Registre des objets

Le registre central de tous les objets est `04_architecture-repository/_index.yaml` : id, type, niveau, chemin, statut. Il est la source de vérité pour la vérification des comptes et la détection de perte pendant la migration.

## Traces de migration et vocabulaire contrôlé

Trois fichiers de `00_metamodel/` portent l'historique et les vocabulaires que le corpus ne peut plus exprimer par lui-même.

| Fichier | Portée | Contenu |
|---------|--------|---------|
| `do-migration.yaml` | fusions d'objets de données | Pour chaque objet de données retiré par fusion, l'identifiant d'origine, l'identifiant qui l'absorbe et la date de la décision. Confronté à la propriété `absorbs` des objets actifs |
| `object-migration.yaml` | retraits et fusions d'objets par décision d'architecture | Pour chaque objet retiré, sa disposition (`retired` ou `merged`), le thème ou le composant qui l'absorbe, et la liste des identifiants qui le remplacent. Ce fichier est la trace de référence des huit retraits du lot de réduction de redondance |
| `themes.yaml` | vocabulaire contrôlé des thèmes de données | Pour chaque thème, son slug, son libellé, sa description et les flux de valeur qu'il dessert. Ce vocabulaire est la seule source admise pour la propriété `theme` d'un objet de données |

La séparation des trois rôles est délibérée. Une trace de migration enregistre ce qui a disparu et vers quoi ; un vocabulaire contrôlé enregistre ce qui reste et comment il se nomme. Le validateur confronte les deux : la propriété `theme` de chaque objet doit appartenir au vocabulaire, chaque thème doit être порteur d'au moins un objet, et l'ensemble des objets d'un thème doit coïncider avec la portée de l'objet retiré qui l'a créé. Cette confrontation rend impossible l'ajout d'un objet dans un thème sans que la trace ne soit mise à jour, et impossible l'oubli d'un objet retiré sans que la propriété `theme` ne soit répartie.

Les flux de valeur portés par `themes.yaml` ne sont pas redondants avec le graphe. La dérivation d'un thème vers un flux de valeur à partir des objets qu'il contient est mesurée : six des sept thèmes s'écartent de la dérivation, seul le thème d'exploitation et de gestion coïncide. Cette information est donc déclarée, et non reconstruite.

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
| Business | Object | `objet-de-donnees` (DO), structuré par la propriété `theme` | ✓ |
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
| Serving (Composant↔Processus) | `applies_to` (CMP→PRC) / `uses` (PRC→CMP) | oui |
| Access (Service/Composant/Processus↔Data) | `accesses` / `accessed_by` | oui |
| Realization (Processus↔Capacité) | `applies_to` (PRC→CAP) | oui |
| Realization (Service↔Capability) | `realizes` / `realized_by` | oui |
| Realization (WorkPackage↔Capability) | `realizes` / `realized_by` | oui |
| Realization (Plateau↔Capability) | `realizes` / `realized_by` | oui |
| Triggering / Flow | `uses` (PRC→CMP) | oui |
| Association (gouvernance) | `governs` | oui |
| Association (roadmap) | `contributes_to` / `precedes` / `between` | oui |
| Association (sémantique, extension HEA) | `constrained_by` / `constrains` | oui |

Les champs ci-dessus s'ajoutent aux champs existants documentés plus haut (`related`, `uses`, `maps_to`, `applies_to`, `implements`, `governs`). La règle d'intégrité transverse reste : tout `uses` (PRC→CMP) doit avoir son `applies_to` inverse (CMP→PRC), tout `realizes` doit avoir son `realized_by` correspondant, tout `accesses` doit avoir son `accessed_by` correspondant et tout `constrained_by` doit avoir son `constrains` correspondant.
