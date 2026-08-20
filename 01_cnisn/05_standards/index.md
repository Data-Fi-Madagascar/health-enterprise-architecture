---

title: Normes et standards d'architecture
id: standards
domain: 05_standards
version: "1.0.0"
status: approved
last_reviewed: 2026-08-18
owner: Comité National d'Architecture Santé Numérique
tags: ["standards", "normes", "homologation"]
---

# Normes et standards d'architecture

## Pour qui lire ce document

**Niveau :** niveau 2 : Cadre National d'Interopérabilité de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ● |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

Ce domaine regroupe les normes, qui sont des exigences obligatoires, et les standards, qui sont des guides recommandés, applicables aux solutions numériques du secteur santé. Il fait partie du CNISN de deuxième niveau et fixe les règles de gouvernance des normes.

## Distinction normes / standards

Une norme constitue une exigence obligatoire, condition d'homologation et de déploiement. Un standard constitue une bonne pratique recommandée pour la cohérence technique. Une norme est adoptée lorsqu'elle est indispensable à l'interopérabilité, à la sécurité des données, à la cohérence des référentiels ou à la soutenabilité des solutions. Toute norme doit être compatible avec les principes du cadre et les référentiels nationaux.

## Établissement d'une norme

L'établissement d'une norme suit un processus en six étapes. Il commence par l'identification du besoin de standard en matière d'interopérabilité, de sécurité ou de cohérence, suivi d'une proposition documentée référencée aux principes du cadre. L'arbitrage est ensuite réalisé par le Comité National d'Architecture Santé Numérique, puis la décision est enregistrée sous forme d'ADR. La norme est publiée et communiquée aux intégrateurs et partenaires, avant de faire l'objet de revues périodiques et de révisions.

Toute mise en œuvre d'une norme fait l'objet d'une homologation préalable ou d'une dérogation validée par l'instance nationale compétente. La conformité s'applique à toute solution déployée dans le secteur santé, qu'elle soit financée par le budget national ou par un partenaire.

## Template de norme

Un modèle de norme est proposé : STD-0000 : modèle.

## Registre des normes

| Code | Titre | Type | Statut |
|------|-------|------|--------|
| STD-0000 | Modèle de norme | modèle | : |
| **STD-0001** | Norme d'interopérabilité : HL7 FHIR R4 | Norme obligatoire | Approuvé |
| **STD-0002** | Norme de sécurité : Chiffrement et contrôle d'accès | Norme obligatoire | Approuvé |
| **STD-0003** | Norme d'échange interinstitutionnel : X-Road | Norme obligatoire | Approuvé |
| **STD-0004** | Norme de données agrégées : mADX | Norme obligatoire | Approuvé |
| **STD-0005** | Norme d'identité patient : PIXm/PDQm | Norme obligatoire | Approuvé |
| **STD-0006** | Norme terminologique : CIM-10 + LOINC | Norme obligatoire | Approuvé |
| **STD-0007** | Standard terminologique : SNOMED CT | Standard recommandé | Draft |
| **NORM-007** | Règlement Sanitaire International (RSI 2005) | Norme internationale obligatoire | Actif |
| **NORM-008** | Tripartite Plus OMS–WOAH–FAO–PNUE | Cadre normatif international | Actif |

## Liens

- Introduction du CNISN
- Principes du CNISN
- Capacités du CNISN
- Gouvernance du CNISN
- Décisions

## Références

- **matrice de lecture** : Matrice de lecture du CNISN (niveau 2) (`01_cnisn/reading-matrix.md`)
- **STD-0000 : modèle** : <Titre de la norme> (`01_cnisn/05_standards/std-0000-template.md`)
- **Modèle de norme** : <Titre de la norme> (`01_cnisn/05_standards/std-0000-template.md`)
- **Norme d'interopérabilité : HL7 FHIR R4** : Norme d'interopérabilité : HL7 FHIR R4 (`01_cnisn/05_standards/std-0001-interopabilite-fhir.md`)
- **Norme de sécurité : Chiffrement et contrôle d'accès** : Norme de sécurité : Chiffrement et contrôle d'accès (`01_cnisn/05_standards/std-0002-securite-chiffrement.md`)
- **Norme d'échange interinstitutionnel : X-Road** : Norme d'échange interinstitutionnel : X-Road (`01_cnisn/05_standards/std-0003-x-road.md`)
- **Norme de données agrégées : mADX** : Norme de données agrégées : mADX (`01_cnisn/05_standards/std-0004-madx.md`)
- **Norme d'identité patient : PIXm/PDQm** : Norme d'identité patient : PIXm/PDQm (`01_cnisn/05_standards/std-0005-identite-pixm.md`)
- **Norme terminologique : CIM-10 + LOINC** : Norme terminologique : CIM-10 + LOINC (`01_cnisn/05_standards/std-0006-terminologie.md`)
- **Standard terminologique : SNOMED CT** : Standard recommandé (`01_cnisn/05_standards/std-0007-snomed-ct.md`)
- **Règlement Sanitaire International (RSI 2005)** : Règlement Sanitaire International (RSI 2005) (`01_cnisn/05_standards/norm-007-rsi.md`)
- **Tripartite Plus OMS–WOAH–FAO–PNUE** : Tripartite Plus OMS–WOAH–FAO–PNUE (`01_cnisn/05_standards/norm-008-tripartite.md`)
- **Introduction du CNISN** : Préambule du CNISN (`01_cnisn/00_introduction/index.md`)
- **Principes du CNISN** : Partie I : Principes nationaux d'interopérabilité de santé (`01_cnisn/01_principes/index.md`)
- **Capacités du CNISN** : Partie II : Capacités nationales requises (`01_cnisn/02_capacites/index.md`)
- **Gouvernance du CNISN** : Partie III : Gouvernance (`01_cnisn/03_gouvernance/index.md`)
- **Décisions** : Décisions d'architecture (ADR) (`01_cnisn/06_decisions/index.md`)

## Documents de la section

- [std-0001: STD-0001 : Norme d'interopérabilité : HL7 FHIR R4](std-0001-interopabilite-fhir.md)
- [std-0003: STD-0003 : Norme d'échange interinstitutionnel : X-Road](std-0003-x-road.md)
- [norm-007: NORM-007 : Règlement Sanitaire International (RSI 2005)](norm-007-rsi.md)
- [std-0007: STD-0007 : Standard terminologique : SNOMED CT](std-0007-snomed-ct.md)
- [std-0005: STD-0005 : Norme d'identité patient : PIXm/PDQm](std-0005-identite-pixm.md)
- [std-0004: STD-0004 : Norme de données agrégées : mADX](std-0004-madx.md)
- [std-0006: STD-0006 : Norme terminologique : CIM-10 + LOINC](std-0006-terminologie.md)
- [norm-008: NORM-008 : Tripartite Plus OMS–WOAH–FAO–PNUE](norm-008-tripartite.md)
- [std-0000: STD-0000 : <Titre de la norme>](std-0000-template.md)
- [std-0002: STD-0002 : Norme de sécurité : Chiffrement et contrôle d'accès](std-0002-securite-chiffrement.md)

<!-- liens-section-auto -->
