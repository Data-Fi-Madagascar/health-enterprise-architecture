---
domain: specs
title: Design du refactor du HEA Architecture Repository aligné TOGAF
id: hea-togaf-repository-refactor-design
version: "0.1"
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

  02_requirements/
    req-*.md
    enf-*.md

  03_patterns/
    pat-*.md

  04_building-blocks/
    index.md
    abb/
      abb-*.md
    sbb/
      sbb-*.md

  05_governance/
    architecture-contracts/
      ac-*.md
    derogations/
      der-*.md
    decisions/
    compliance/
    evidence/

  06_migration/
    work-packages/
    plateaux/
    gaps/

  07_views/
    togaf/
      architecture-landscape.md
      standards-information-base.md
      reference-library.md
      governance-log.md
      requirements-repository.md
      solutions-landscape.md
      adm-traceability.md

  08_baselines/
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

## 6. CNISN dans le Landscape

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

## 7. Exigences, patterns et chapitres ART

Le refactor doit séparer trois notions actuellement proches :

| Notion | Rôle cible |
|--------|------------|
| `REQ-*` | Exigence d'architecture traçable, issue d'un besoin métier, réglementaire ou technique |
| `ENF-*` | Exigence non fonctionnelle ou contrainte contextuelle |
| `PAT-*` | Pattern d'architecture réutilisable |
| `ART-*` | Chapitre normatif ou règle de référence ARTSN |

Cette séparation réduit la surcharge actuelle des chapitres ART, qui peuvent être lus à la fois comme chapitres, exigences et patterns. Les ART doivent rester la référence normative publiée, tandis que les patterns et exigences deviennent des objets spécialisés et traçables.

## 8. Building blocks

Les building blocks deviennent un espace explicite du repository. Ils sont organisés en deux familles :

```text
04_building-blocks/
  abb/
  sbb/
```

### 8.1 Architecture Building Blocks

Les ABB décrivent les blocs d'architecture attendus, neutres technologiquement. Ils répondent à des capacités, exigences, patterns et règles ARTSN.

Les sources candidates sont principalement :

| Source actuelle | Traitement cible |
|-----------------|------------------|
| `composants/cmp-*` | Transformation progressive en `ABB-*` |
| `services/srv-*` | Classification ABB si le service reste abstrait et réutilisable |
| certains patterns ARTSN | Liaison vers ABB, sans fusion systématique |

### 8.2 Solution Building Blocks

Les SBB décrivent les réalisations concrètes, vérifiables ou instanciables. Ils réalisent des ABB et sont liés aux profils PTISN, schemas, API ou artefacts techniques.

Les sources candidates sont principalement :

| Source actuelle | Traitement cible |
|-----------------|------------------|
| `profils/pt-*` | Transformation progressive en `SBB-*` ou lien SBB vers profil PTISN |
| OpenAPI | Spécification technique associée à un SBB |
| FHIR profiles | Spécification technique associée à un SBB |
| JSON Schema | Preuve ou contrat technique associé à un SBB |

### 8.3 Relation minimale

La relation minimale attendue est :

```text
CAP / CAP-INT
  -> REQ / ENF
  -> PAT / ART
  -> ABB
  -> SBB
```

Aucun SBB ne doit exister sans ABB réalisé. Aucun ABB ne doit exister sans capacité ou exigence justifiante.

## 9. Gouvernance

Le dossier `05_governance/` consolide les objets nécessaires au contrôle de l'architecture :

| Sous-dossier | Rôle |
|--------------|------|
| `architecture-contracts/` | Contrats d'architecture entre architecture et mise en oeuvre |
| `derogations/` | Ecarts approuvés, datés et justifiés |
| `decisions/` | Vue structurée des ADR |
| `compliance/` | Règles et statuts de conformité |
| `evidence/` | Preuves d'homologation, tests, validations SHACL, FHIR, OpenAPI |

Cette zone doit permettre de soutenir les phases G et H de l'ADM : gouvernance de l'implémentation et gestion du changement.

## 10. Migration et baselines

Le dossier `06_migration/` regroupe les objets liés aux phases E et F de l'ADM :

| Type | Rôle |
|------|------|
| `work-packages/` | Lots de mise en oeuvre |
| `plateaux/` | Etats intermédiaires ou cibles |
| `gaps/` | Ecarts entre baseline, transition et cible |

Le dossier `08_baselines/` conserve les architectures approuvées :

| Type | Rôle |
|------|------|
| `baseline-*` | Etat de référence existant |
| `target-*` | Etat cible approuvé |
| `transition-*` | Etat de transition approuvé |

Cette séparation évite de confondre la trajectoire de migration avec les versions approuvées du landscape.

## 11. Vues TOGAF

Les vues TOGAF sont placées dans :

```text
07_views/togaf/
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

## 12. Règles de traçabilité

La chaîne cible de traçabilité est :

```text
VS
  -> PART
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
| Un ABB doit référencer au moins une capacité ou une exigence | Garantir la justification architecture |
| Un SBB doit réaliser au moins un ABB | Garantir la séparation architecture solution |
| Une dérogation doit référencer une décision ou un contrat | Garantir la gouvernance |
| Un work package doit contribuer à un plateau ou répondre à un gap | Garantir la trajectoire |
| Une evidence doit référencer un contrat, SBB ou critère de conformité | Garantir la vérifiabilité |

## 13. Stratégie de migration

La migration doit être progressive et contrôlée :

1. Capturer l'état de validation actuel.
2. Renommer `referentiel/` vers `04_architecture-repository/`.
3. Mettre à jour les scripts, liens Markdown, chemins de génération et index.
4. Déplacer `_schema.md` vers `00_metamodel/schema.md`.
5. Ajouter les champs TOGAF au schéma et aux objets prioritaires.
6. Créer les partitions initiales.
7. Séparer progressivement exigences, patterns, ABB et SBB.
8. Créer les vues TOGAF.
9. Ajouter les règles de validation.
10. Exécuter la validation complète du dépôt.

Le refactor ne doit pas changer la signification métier des objets pendant la première passe. Il doit d'abord rendre explicite la structure TOGAF, puis permettre des enrichissements de contenu ultérieurs.

## 14. Hors périmètre du premier refactor

Les éléments suivants ne doivent pas être inclus dans la première passe :

| Elément | Raison |
|---------|--------|
| Réécriture complète des contenus CAESN, CNISN, ARTSN, PTISN | Risque de dérive éditoriale |
| Suppression massive d'identifiants existants | Risque de rupture des liens et de l'historique |
| Fusion complète CMP/SRV/PT vers ABB/SBB en une seule étape | Trop risqué sans revue objet par objet |
| Refonte complète de l'ontologie OWL | A traiter après stabilisation du métamodèle Markdown |
| Publication Open Group | A traiter après stabilisation et revue du repository |

## 15. Critères de succès

Le refactor est réussi si :

| Critère | Résultat attendu |
|---------|------------------|
| Structure | `04_architecture-repository/` remplace `referentiel/` sans perte d'objet |
| TOGAF | Les composants TOGAF sont visibles dans le schéma et les vues |
| CNISN | Son rôle d'architecture transverse d'interopérabilité est explicite |
| Partitions | Les partitions value stream, transverses, One Health et transfrontalière existent |
| ABB/SBB | La séparation est représentée dans l'arborescence et le frontmatter |
| Gouvernance | Contrats, dérogations, conformité et preuves ont un emplacement clair |
| Validation | `python3 scripts/validate_ref.py` reste conforme |
| Qualité | `make check` reste vert ou documente clairement les écarts non bloquants |

## 16. Questions à arbitrer avant implémentation

Deux décisions restent à confirmer avant le plan d'implémentation :

1. Le renommage physique `referentiel/` vers `04_architecture-repository/` doit-il être fait en une passe, ou faut-il une période de compatibilité avec un alias documentaire ?
2. Les objets `CMP-*`, `SRV-*` et `PT-*` doivent-ils garder leurs identifiants historiques en plus des nouveaux identifiants `ABB-*` et `SBB-*`, ou les nouveaux identifiants doivent-ils remplacer progressivement les anciens ?
