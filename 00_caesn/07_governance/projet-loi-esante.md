---
title: "Avant-projet de loi e-santé (cadre législatif opposable)"
id: projet-loi-esante
domain: 07_governance
version: "1.1.0"
status: draft
last_reviewed: 2026-08-26
owner: Ministère de la Santé Publique
tags: ["gouvernance", "légal", "e-santé", "conformité", "opposabilité"]
---

# Avant-projet de loi e-santé (cadre législatif opposable)

## Pour qui lire ce document

**Niveau :** niveau 1 : Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ◐ |
| SIS / données / suivi-évaluation | ○ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

## Objet

Ce document est l'**avant-projet** de loi e-santé recommandé par [ADR-0010](../../01_cnisn/06_decisions/adr-0010-cadre-legal.md). Il transforme le HEA de cadre *consultatif* en cadre *opposable* : il confère au CNASN un mandat légal et rend la conformité aux standards obligatoire. Il structure le système de santé numérique malgache autour de infrastructures partagées souveraines, interopérables et finançables.

> **Nature du document.** Il s'agit d'un **avant-projet** (squelette légistique) destiné à alimenter la rédaction gouvernementale et l'arbitrage interinstitutionnel. Les libellés d'articles sont indicatifs et devront être conformes à la technique législative en vigueur.

## Périmètre et champ d'application

**Périmètre fonctionnel.** La loi couvre l'ensemble des composants du système de santé numérique : infrastructures partagées (identité, échange, dossier, terminologie, analytique), applicatifs métier, données de santé et services rendus aux usagers et acteurs.

**Champ d'application (assujettis).** Sont soumis à la loi :

1. Les **acteurs publics** de la santé (État, régions, districts, formations sanitaires) et leurs systèmes d'information.
2. Les **prestataires privés** (établissements, mutuelles, assureurs) lorsqu'ils sont interconnectés aux infrastructures nationales ou traitent des données de santé relevant de l'intérêt général.
3. Les **plateformes et services numériques** de santé (télémédecine, registres, applications usagers) déployés sur le territoire.
4. Les **partenaires techniques et financiers** lorsque leurs initiatives utilisent les infrastructures partagées ou sont cofinancées par l'État.

**Hors champ (sauf accord).** Les dispositifs à usage strictement personnel, les recherches hors données opérationnelles, et les systèmes relevant d'autres ministères (coordonnés via One Health — [lot L7](../../02_artsn/07_lots/index.md)).

## Structure de la loi — titres et articles clés

### Titre I — Dispositions générales

- **Art. 1 — Objet et définitions** : définit le « système de santé numérique », la « donnée de santé », les « infrastructures partagées » et le « HEA » comme cadre de référence.
- **Art. 2 — Champ d'application** : reprend les assujettis ci-dessus.
- **Art. 3 — Principes** : souveraineté, interopérabilité, confidentialité, équité d'accès, opposabilité du HEA, et alignement [Convention de Malabo](fondement-legal.md).

### Titre II — Gouvernance et CNASN

- **Art. 4 — Institution du CNASN** : crée le Comité National d'Architecture Santé Numérique, rattaché au Ministère de la Santé Publique, avec personnalité et pouvoir d'homologation.
- **Art. 5 — Attributions** : architecture de référence, homologation des systèmes, publication des normes, conformité et sanction.
- **Art. 6 — Instances** : DEPSI (secrétariat technique), instances sectorielles dont la [plateforme nationale de coordination PHC](instances-sectorielles.md).
- **Art. 7 — Opposabilité** : les ADR, référentiels et critères de conformité publiés par le CNASN sont opposables aux assujettis.

### Titre III — Interopérabilité et normes

- **Art. 8 — Conformité obligatoire** : respect des normes [CNISN](../../01_cnisn/05_standards/index.md) (FHIR R4, X-Road, PIXm/PDQm, terminologies).
- **Art. 9 — Couche d'échange nationale** : X-Road comme infrastructure partagée obligatoire de routage et transformation.
- **Art. 10 — Référentiels maîtres** : registres nationaux du patient, des formations sanitaires et des professionnels de santé comme sources authentiques.

### Titre IV — Données, consentement et résidence

- **Art. 11 — Résidence de la donnée** : hébergement souverain sur le territoire national, chiffrement de bout en bout ([ART-7](../../referentiel/chapitres/art-7.md), [STD-0002](../../01_cnisn/05_standards/std-0002-securite-chiffrement.md)).
- **Art. 12 — Consentement et droits** : consentement éclairé, accès et rectification des données du patient ([ADR-0005](../../01_cnisn/06_decisions/adr-0005-consentement.md)).
- **Art. 13 — Sécurité et traçabilité** : journalisation, authentification, garanties transactionnelles ([ART-9](../../referentiel/chapitres/art-9.md), [ADR-0008](../../01_cnisn/06_decisions/adr-0008-atna.md)).
- **Art. 14 — Échanges transfrontaliers** : encadrement des échanges internationaux (GDHCN) dans le respect de la résidence.

### Titre V — Financement et budgetisation

- **Art. 15 — Enveloppe e-santé** : inscription d'une enveloppe pluriannuelle, calculée selon la méthode du coût total de possession (TCO) par lot ([méthode TCO](../06_portfolio/financement-tco.md) ; [ADR-0010](../../01_cnisn/06_decisions/adr-0010-cadre-legal.md)).
- **Art. 16 — Coordination des financements** : les programmes verticaux sont coordonnés via le portefeuille pour éviter la fragmentation.

### Titre VI — Contrôles, sanctions et pénalités

- **Art. 17 — Conformité et certification** : audit de conformité, certification des profils techniques (PTISN), homologation préalable à la mise en service.
- **Art. 18 — Sanctions** : exclusion des infrastructures partagées, retrait ou conditionnalité des financements publics en cas de non-conformité.

### Titre VII — Dispositions transitoires

- **Art. 19 — Mise en conformité** : délai de mise en conformité des systèmes existants (cadrage [ADR-0010](../../01_cnisn/06_decisions/adr-0010-cadre-legal.md)).
- **Art. 20 — Entrée en vigueur** : date d'application et habilitation à statuer par décret.

## Articulations avec le CNASN et l'ARTSN

La loi n'est pas un document isolé : elle ancre juridiquement la chaîne CAESN → CNISN → ARTSN.

| Maillon | Rôle rendu opposable par la loi | Référence HEA |
|---------|----------------------------------|---------------|
| **CAESN** (stratégie) | Principes, gouvernance, fondement légal | [Fondement légal](fondement-legal.md), [Gouvernance](index.md) |
| **CNASN** (autorité) | Mandat d'architecture et d'homologation (Art. 4–7) | [ADR-0010](../../01_cnisn/06_decisions/adr-0010-cadre-legal.md) |
| **CNISN** (normes) | Conformité obligatoire aux standards (Art. 8–10) | [Normes](../../01_cnisn/05_standards/index.md), ADR-0001/0004/0006 |
| **ARTSN** (référence technique) | Déploiement par lots, finançable (Art. 15) | [Feuille de route](../../02_artsn/07_lots/index.md), [TCO](../06_portfolio/financement-tco.md) |
| **PTISN** (mise en œuvre) | Certification des profils (Art. 17) | Profils techniques (`../../03_ptisn/`) |

Ainsi, la loi transforme le HEA d'un *référentiel conseillé* en un *socle juridique exécutoire* : chaque chapitre ART, chaque norme CNISN et chaque lot ARTSN devient un objet de conformité vérifiable.

## Modèle de référence

Inspiré du *Kenya Digital Health Act* (2023) et aligné sur la [Convention de Malabo](fondement-legal.md) et la [Loi 2014-038](fondement-legal.md) sur la santé de base. La structure par titres reprend les domaines faibles identifiés par l'évaluation [ADHMAT](../../02_artsn/08_annexes/h-benchmark-adhmat.md) (législation, infrastructure, workforce).

## Statut

**Proposé** (évolutif vers `candidate` puis `active` à l'adoption). En attendant la promulgation, le CNASN exerce son mandat par accord interinstitutionnel et conditionnalité des financements (voir [ADR-0010](../../01_cnisn/06_decisions/adr-0010-cadre-legal.md)).

## Références

- **matrice de lecture** : Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
- **ADR-0010** : Cadre légal et mandat d'opposabilité du CNASN (`../../01_cnisn/06_decisions/adr-0010-cadre-legal.md`)
- **Fondement légal** : Fondement légal et cadre législatif (`fondement-legal.md`)
- **Gouvernance** : Gouvernance du cadre d'architecture (`index.md`)
- **Instances sectorielles** : Plateforme nationale de coordination PHC (`instances-sectorielles.md`)
- **TCO** : Méthode TCO et enveloppe de financement (`../06_portfolio/financement-tco.md`)
- **ADHMAT** : Benchmark de maturité (annexe H) (`../../02_artsn/08_annexes/h-benchmark-adhmat.md`)
