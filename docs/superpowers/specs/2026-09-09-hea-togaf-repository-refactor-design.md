---
domain: specs
title: Design du refactor du HEA Architecture Repository aligné TOGAF
id: hea-togaf-repository-refactor-design
version: "0.2"
status: draft
last_reviewed: 2026-09-09
owner: DEPSI
tags: ["hea", "togaf", "architecture-repository", "refactor"]
---

# Design du refactor du HEA Architecture Repository aligné TOGAF

## 1. Contexte

Le dépôt HEA documente l'architecture d'entreprise de la santé numérique de Madagascar selon une structure à quatre niveaux : CAESN, CNISN, ARTSN et PTISN. Cette structure est cohérente pour les lecteurs institutionnels et techniques, mais l'alignement avec le vocabulaire TOGAF doit être rendu plus explicite pour soutenir la gouvernance, la traçabilité et une éventuelle valorisation comme cas d'usage auprès de The Open Group.

Le refactor proposé est équilibré : il conserve les dossiers documentaires publiés à la racine, tout en transformant le référentiel structuré en un véritable Architecture Repository explicite. Cette approche évite une réorganisation trop brutale du landscape documentaire, tout en donnant aux concepts TOGAF une place vérifiable dans le métamodèle.

## 2. Décisions de conception

### 2.1 Le dépôt complet représente le HEA Architecture Repository

Le dépôt Git complet est considéré comme le HEA Architecture Repository. Il contient à la fois les documents publiés, les objets structurés, les règles de gouvernance, les vues générées et les preuves de conformité.

Les dossiers `00_caesn/`, `01_cnisn/`, `02_artsn/` et `03_ptisn/` restent à la racine. Ils constituent le landscape documentaire HEA et ne sont pas déplacés sous un dossier TOGAF générique.

### 2.2 Les dossiers 00 à 03 forment le Landscape HEA

La lecture TOGAF cible est la suivante :

| Dossier | Rôle TOGAF |
|---------|------------|
| `00_caesn/` | Architecture Landscape - Enterprise Architecture |
| `01_cnisn/` | Architecture Landscape - Transversal Interoperability Architecture |
| `02_artsn/` | Architecture Landscape - Segment, Capability and Reference Architecture |
| `03_ptisn/` | Solutions Landscape - Implementation Profiles and Solution Building Blocks |

Cette décision clarifie que le CNISN n'est pas seulement une bibliothèque de standards. Il constitue une architecture transverse d'interopérabilité qui contraint les partitions d'architecture, les building blocks et les solutions.

### 2.3 Le dossier `referentiel/` devient `04_architecture-repository/`

Le dossier `referentiel/` ne doit pas être renommé en `artifacts/`, car il contient plus que des artifacts au sens TOGAF. Il contient des capacités, exigences, patterns, building blocks, plateaux, gaps, work packages, relations et objets de gouvernance.

Le nom cible est donc :

```text
04_architecture-repository/
```

Les artifacts deviennent une sous-vue du repository, et non le nom du repository complet.

Le renommage physique est réalisé en une seule passe. Il n'y a pas de période de coexistence entre `referentiel/` et `04_architecture-repository/`, afin d'éviter deux sources de vérité concurrentes.

### 2.4 Les nouveaux identifiants ABB/SBB deviennent les identifiants principaux

Les objets transformés en building blocks adoptent les nouveaux identifiants `ABB-*` ou `SBB-*` comme identifiants principaux. Les anciens identifiants `CMP-*`, `SRV-*` et `PT-*` peuvent être conservés temporairement dans un champ `legacy_id`, mais ils ne restent pas l'identité canonique de l'objet.

Cette décision rend la séparation TOGAF immédiatement lisible. Elle impose en contrepartie une migration stricte des liens et des index pour éviter toute rupture de traçabilité.

## 3. Structure cible

La structure cible du repository structuré est la suivante :

```text
04_architecture-repository/
  _index.yaml

  00_metamodel/
    schema.md
    togaf-mapping.md
    archimate-mapping.md

  01_partitions/
    index.md
    value-streams/
      part-vs-01.md
      part-vs-02.md
      part-vs-03.md
      part-vs-04.md
    transverses/
      part-transverse-interoperabilite.md
      part-transverse-identite.md
      part-transverse-securite-confiance.md
      part-transverse-donnees-referentielles.md
      part-transverse-analytics-pilotage.md
    sectorielles/
      part-one-health.md
    externes/
      part-echange-transfrontalier.md

  02_architecture-elements/
    strategy/
      capabilities/
      value-streams/
      value-stages/
    business/
      actors/
      roles/
      functions/
      processes/
      business-objects/
      business-services/
    data/
      data-objects/
      reference-data/
      terminologies/

  03_requirements/
    req-*.md
    enf-*.md

  04_patterns/
    pat-*.md

  05_building-blocks/
    index.md
    abb/
      abb-*.md
    sbb/
      sbb-*.md

  06_governance/
    architecture-contracts/
      ac-*.md
    derogations/
      der-*.md
    decisions/
    compliance/
    evidence/

  07_migration/
    work-packages/
    plateaux/
    gaps/

  08_views/
    togaf/
      architecture-landscape.md
      standards-information-base.md
      reference-library.md
      governance-log.md
      requirements-repository.md
      solutions-landscape.md
      adm-traceability.md

  09_baselines/
    baseline-*.md
    target-*.md
    transition-*.md
```

## 4. Métamodèle cible

Le métamodèle HEA reste natif au domaine santé numérique, mais il porte une classification TOGAF explicite. Les champs existants sont conservés autant que possible pour limiter le risque de rupture.

### 4.1 Champs TOGAF à ajouter

```yaml
togaf_repository_section: architecture-landscape
togaf_adm_phase: B
architecture_level: segment
architecture_domain: data
architecture_scope: interoperability
architecture_state: target
partitions: ["PART-VS-01"]
building_block_role: ABB
building_block_domain: application
legacy_id: CMP-06
```

### 4.2 Vocabulaires contrôlés

| Champ | Valeurs proposées |
|-------|-------------------|
| `togaf_repository_section` | `architecture-landscape`, `standards-information-base`, `reference-library`, `governance-log`, `requirements-repository`, `solutions-landscape` |
| `togaf_adm_phase` | `Preliminary`, `A`, `B`, `C`, `D`, `E`, `F`, `G`, `H`, `Requirements Management` |
| `architecture_level` | `enterprise`, `enterprise-transversal`, `segment`, `capability`, `solution`, `implementation` |
| `architecture_domain` | `business`, `data`, `application`, `technology`, `security`, `governance` |
| `architecture_state` | `baseline`, `target`, `transition`, `retired` |
| `partition_kind` | `value-stream`, `transverse`, `sectorielle`, `externe` |
| `building_block_role` | `ABB`, `SBB` |
| `building_block_domain` | `business`, `data`, `application`, `technology`, `security`, `governance` |
| `legacy_id` | ancien identifiant conservé pour traçabilité uniquement |

### 4.3 Clarification `source` et `envelope`

Le champ `envelope` doit devenir la provenance documentaire active de l'objet, car il est déjà utilisé dans les objets existants. Le champ `source` peut être conservé comme alias historique ou rendu optionnel.

Cette clarification doit être intégrée dans `00_metamodel/schema.md` afin de supprimer l'ambiguïté actuelle entre le schéma documenté et les frontmatters réellement présents.

## 5. Partitions d'architecture

Les partitions sont des découpages d'architecture du landscape HEA. Elles ne doivent pas dupliquer les objets. Elles les agrègent par périmètre, valeur, transversalité ou échange externe.

### 5.1 Familles de partitions

| Famille | Rôle |
|---------|------|
| Value streams | Découpage par production de valeur métier |
| Transverses | Capacités communes imposées à plusieurs partitions |
| Sectorielles | Périmètres multi-domaines, notamment One Health |
| Externes | Echanges régionaux, internationaux ou transfrontaliers |

### 5.2 Partitions initiales

| Partition | Type | Rôle |
|-----------|------|------|
| `PART-VS-01` | `value-stream` | Partition du premier flux de valeur national |
| `PART-VS-02` | `value-stream` | Partition du deuxième flux de valeur national |
| `PART-VS-03` | `value-stream` | Partition du troisième flux de valeur national |
| `PART-VS-04` | `value-stream` | Partition du quatrième flux de valeur national |
| `PART-TRANSVERSE-INTEROPERABILITE` | `transverse` | Règles et capacités communes d'interopérabilité |
| `PART-TRANSVERSE-IDENTITE` | `transverse` | Identification, annuaires, autorités et référentiels |
| `PART-TRANSVERSE-SECURITE-CONFIANCE` | `transverse` | IAM, traçabilité, sécurité, consentement et confiance |
| `PART-TRANSVERSE-DONNEES-REFERENTIELLES` | `transverse` | Nomenclatures, terminologies et données de référence |
| `PART-TRANSVERSE-ANALYTICS-PILOTAGE` | `transverse` | Analytics, pilotage, supervision et indicateurs |
| `PART-ONE-HEALTH` | `sectorielle` | Articulation santé humaine, animale et environnementale |
| `PART-ECHANGE-TRANSFRONTALIER` | `externe` | Echanges internationaux et interopérabilité transfrontalière |

## 6. Eléments d'architecture

Le dossier `02_architecture-elements/` regroupe les éléments qui décrivent l'entreprise, le métier et l'information sans les confondre avec les exigences, les patterns ou les building blocks.

### 6.1 Structure

```text
02_architecture-elements/
  strategy/
    capabilities/
    value-streams/
    value-stages/

  business/
    actors/
    roles/
    functions/
    processes/
    business-objects/
    business-services/

  data/
    data-objects/
    reference-data/
    terminologies/
```

### 6.2 Placement des concepts métier

| Concept | Dossier cible | Rôle |
|---------|---------------|------|
| Capability | `strategy/capabilities/` | Ce que le système de santé doit être capable de faire |
| Value stream | `strategy/value-streams/` | Flux de production de valeur métier |
| Value stage | `strategy/value-stages/` | Etape dans un flux de valeur |
| Actor | `business/actors/` | Organisation, entité ou personne qui intervient dans l'architecture |
| Role | `business/roles/` | Responsabilité portée par un acteur |
| Function | `business/functions/` | Groupe stable de comportements métier |
| Process | `business/processes/` | Enchaînement opérationnel qui réalise une capacité |
| Business object | `business/business-objects/` | Objet métier manipulé par les processus |
| Business service | `business/business-services/` | Service métier rendu à un acteur ou une partie prenante |
| Data object | `data/data-objects/` | Objet de données logique ou sémantique |
| Reference data | `data/reference-data/` | Données de référence et nomenclatures |
| Terminology | `data/terminologies/` | Terminologies, codifications et vocabulaires contrôlés |

### 6.3 Distinction entre fonction, processus, acteur et rôle

La fonction métier représente une responsabilité stable de l'entreprise, indépendante d'un déroulement précis. Le processus représente l'enchaînement opérationnel d'activités, avec un début, une fin et des dépendances. L'acteur est l'entité qui participe à l'exécution, tandis que le rôle décrit la responsabilité assumée par cet acteur.

La relation cible est :

```text
Value Stream
  -> Partition
  -> Capability
  -> Business Function
  -> Business Process
  -> Role
  -> Actor
  -> Business Object / Data Object
```

Cette séparation évite de faire porter aux building blocks des éléments purement métier. Les ABB et SBB doivent rester des blocs d'architecture et de solution, pas des acteurs, rôles ou processus.

## 7. CNISN dans le Landscape

Le CNISN occupe une position transverse. Il n'est pas seulement un niveau documentaire entre CAESN et ARTSN. Il définit les contraintes d'interopérabilité nationales qui s'appliquent aux partitions, aux ABB, aux SBB et aux preuves de conformité.

La relation cible est :

```text
CAESN
  -> définit la stratégie, la valeur, les capacités et la gouvernance

CNISN
  -> impose les principes, standards, capacités et règles d'interopérabilité

ARTSN
  -> traduit CAESN et CNISN en partitions, patterns, ABB et services de référence

PTISN
  -> instancie les SBB, profils techniques, API, schemas et preuves
```

Le CNISN doit donc être classé principalement avec :

```yaml
togaf_repository_section:
  - architecture-landscape
  - standards-information-base
  - governance-log
architecture_level: enterprise-transversal
architecture_scope: interoperability
```

## 8. Exigences, patterns et chapitres ART

Le refactor doit séparer trois notions actuellement proches :

| Notion | Rôle cible |
|--------|------------|
| `REQ-*` | Exigence d'architecture traçable, issue d'un besoin métier, réglementaire ou technique |
| `ENF-*` | Exigence non fonctionnelle ou contrainte contextuelle |
| `PAT-*` | Pattern d'architecture réutilisable |
| `ART-*` | Chapitre normatif ou règle de référence ARTSN |

Cette séparation réduit la surcharge actuelle des chapitres ART, qui peuvent être lus à la fois comme chapitres, exigences et patterns. Les ART doivent rester la référence normative publiée, tandis que les patterns et exigences deviennent des objets spécialisés et traçables.

## 9. Building blocks

Les building blocks deviennent un espace explicite du repository. Ils sont organisés en deux familles :

```text
05_building-blocks/
  abb/
  sbb/
```

### 9.1 Architecture Building Blocks

Les ABB décrivent les blocs d'architecture attendus, neutres technologiquement. Ils répondent à des capacités, exigences, patterns et règles ARTSN.

Les sources candidates sont principalement :

| Source actuelle | Traitement cible |
|-----------------|------------------|
| `composants/cmp-*` | Remplacement par des objets `ABB-*` |
| `services/srv-*` | Remplacement par `ABB-*` si le service reste abstrait et réutilisable |
| certains patterns ARTSN | Liaison vers ABB, sans fusion systématique |

### 9.2 Solution Building Blocks

Les SBB décrivent les réalisations concrètes, vérifiables ou instanciables. Ils réalisent des ABB et sont liés aux profils PTISN, schemas, API ou artefacts techniques.

Les sources candidates sont principalement :

| Source actuelle | Traitement cible |
|-----------------|------------------|
| `profils/pt-*` | Remplacement par des objets `SBB-*` |
| OpenAPI | Spécification technique associée à un SBB |
| FHIR profiles | Spécification technique associée à un SBB |
| JSON Schema | Preuve ou contrat technique associé à un SBB |

Les identifiants historiques peuvent être portés par `legacy_id`, mais les liens actifs du repository pointent vers les nouveaux objets `SBB-*`.

### 9.3 Relation minimale

La relation minimale attendue est :

```text
CAP / CAP-INT
  -> REQ / ENF
  -> PAT / ART
  -> ABB
  -> SBB
```

Aucun SBB ne doit exister sans ABB réalisé. Aucun ABB ne doit exister sans capacité ou exigence justifiante.

## 10. Gouvernance

Le dossier `06_governance/` consolide les objets nécessaires au contrôle de l'architecture :

| Sous-dossier | Rôle |
|--------------|------|
| `architecture-contracts/` | Contrats d'architecture entre architecture et mise en oeuvre |
| `derogations/` | Ecarts approuvés, datés et justifiés |
| `decisions/` | Vue structurée des ADR |
| `compliance/` | Règles et statuts de conformité |
| `evidence/` | Preuves d'homologation, tests, validations SHACL, FHIR, OpenAPI |

Cette zone doit permettre de soutenir les phases G et H de l'ADM : gouvernance de l'implémentation et gestion du changement.

## 11. Migration et baselines

Le dossier `07_migration/` regroupe les objets liés aux phases E et F de l'ADM :

| Type | Rôle |
|------|------|
| `work-packages/` | Lots de mise en oeuvre |
| `plateaux/` | Etats intermédiaires ou cibles |
| `gaps/` | Ecarts entre baseline, transition et cible |

Le dossier `09_baselines/` conserve les architectures approuvées :

| Type | Rôle |
|------|------|
| `baseline-*` | Etat de référence existant |
| `target-*` | Etat cible approuvé |
| `transition-*` | Etat de transition approuvé |

Cette séparation évite de confondre la trajectoire de migration avec les versions approuvées du landscape.

## 12. Vues TOGAF

Les vues TOGAF sont placées dans :

```text
08_views/togaf/
```

Elles ne doivent pas dupliquer les objets. Elles réorganisent les objets du repository selon les composants TOGAF :

| Vue | Contenu |
|-----|---------|
| `architecture-landscape.md` | CAESN, CNISN, ARTSN, partitions, capacités et états d'architecture |
| `standards-information-base.md` | Standards CNISN, normes, profils et règles applicables |
| `reference-library.md` | Patterns, fondations, ABB réutilisables, références externes |
| `governance-log.md` | ADR, contrats, dérogations, conformité, evidence |
| `requirements-repository.md` | REQ, ENF, contraintes, liens vers capacités et patterns |
| `solutions-landscape.md` | SBB, profils PTISN, API, schemas, ressources FHIR |
| `adm-traceability.md` | Traçabilité par phase ADM |

## 13. Règles de traçabilité

La chaîne cible de traçabilité est :

```text
VS
  -> PART
  -> Architecture Element
  -> CAP / CAP-INT
  -> REQ / ENF
  -> PAT / ART
  -> ABB
  -> SBB
  -> WP
  -> PL / GAP
  -> Evidence
```

Les règles minimales à valider sont :

| Règle | Finalité |
|-------|----------|
| Une partition doit avoir un périmètre explicite | Eviter les partitions décoratives |
| Une partition value stream doit référencer un `VS-*` | Garantir l'ancrage valeur |
| Une partition transverse doit référencer les partitions auxquelles elle s'applique | Garantir la transversalité réelle |
| Un processus doit réaliser une capacité ou une étape de valeur | Garantir la cohérence métier |
| Un acteur doit porter un rôle ou participer à un processus | Eviter les acteurs isolés |
| Un ABB doit référencer au moins une capacité ou une exigence | Garantir la justification architecture |
| Un SBB doit réaliser au moins un ABB | Garantir la séparation architecture solution |
| Une dérogation doit référencer une décision ou un contrat | Garantir la gouvernance |
| Un work package doit contribuer à un plateau ou répondre à un gap | Garantir la trajectoire |
| Une evidence doit référencer un contrat, SBB ou critère de conformité | Garantir la vérifiabilité |

## 14. Stratégie de migration

La migration doit être progressive et contrôlée :

1. Capturer l'état de validation actuel.
2. Renommer `referentiel/` vers `04_architecture-repository/`.
3. Mettre à jour les scripts, liens Markdown, chemins de génération et index.
4. Déplacer `_schema.md` vers `00_metamodel/schema.md`.
5. Créer `02_architecture-elements/` et y placer les concepts stratégie, métier et données.
6. Ajouter les champs TOGAF au schéma et aux objets prioritaires.
7. Créer les partitions initiales.
8. Séparer progressivement exigences, patterns, ABB et SBB.
9. Remplacer les identifiants principaux `CMP-*`, `SRV-*` et `PT-*` par `ABB-*` et `SBB-*` lorsque l'objet devient un building block.
10. Créer les vues TOGAF.
11. Ajouter les règles de validation.
12. Exécuter la validation complète du dépôt.

Le refactor ne doit pas changer la signification métier des objets pendant la première passe. Il doit d'abord rendre explicite la structure TOGAF, puis permettre des enrichissements de contenu ultérieurs.

## 15. Hors périmètre du premier refactor

Les éléments suivants ne doivent pas être inclus dans la première passe :

| Elément | Raison |
|---------|--------|
| Réécriture complète des contenus CAESN, CNISN, ARTSN, PTISN | Risque de dérive éditoriale |
| Suppression massive d'identifiants existants | Risque de rupture des liens et de l'historique |
| Refonte complète de l'ontologie OWL | A traiter après stabilisation du métamodèle Markdown |
| Publication Open Group | A traiter après stabilisation et revue du repository |

## 16. Critères de succès

Le refactor est réussi si :

| Critère | Résultat attendu |
|---------|------------------|
| Structure | `04_architecture-repository/` remplace `referentiel/` sans perte d'objet |
| TOGAF | Les composants TOGAF sont visibles dans le schéma et les vues |
| CNISN | Son rôle d'architecture transverse d'interopérabilité est explicite |
| Partitions | Les partitions value stream, transverses, One Health et transfrontalière existent |
| Eléments d'architecture | Les capacités, flux, fonctions, processus, acteurs, rôles et objets sont distincts des building blocks |
| ABB/SBB | La séparation est représentée dans l'arborescence, les identifiants et le frontmatter |
| Gouvernance | Contrats, dérogations, conformité et preuves ont un emplacement clair |
| Validation | `python3 scripts/validate_ref.py` reste conforme |
| Qualité | `make check` reste vert ou documente clairement les écarts non bloquants |

## 17. Arbitrages validés

Les décisions suivantes sont validées avant le plan d'implémentation :

1. Le renommage physique `referentiel/` vers `04_architecture-repository/` est fait en une passe.
2. Les nouveaux identifiants `ABB-*` et `SBB-*` remplacent les anciens identifiants principaux lorsque les objets sont transformés en building blocks.
3. Les anciens identifiants `CMP-*`, `SRV-*` et `PT-*` ne sont conservés que comme `legacy_id` temporaire pour la traçabilité.
4. Les fonctions, processus, acteurs et rôles sont placés dans `02_architecture-elements/business/`.

## 18. Questions restantes avant implémentation

Deux décisions mineures restent à préciser dans le plan d'implémentation :

1. Faut-il migrer tous les `CMP-*`, `SRV-*` et `PT-*` vers `ABB-*` ou `SBB-*` dès la première passe, ou seulement ceux qui ont une relation claire avec une capacité et une exigence ?
2. Faut-il créer des index de redirection documentaire pour les anciens identifiants, même si les liens actifs pointent vers les nouveaux objets ?
