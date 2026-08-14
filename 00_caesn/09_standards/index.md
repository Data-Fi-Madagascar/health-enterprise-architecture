---
title: Normes et standards d'architecture
id: standards
domain: 09_standards
version: "1.0.0"
status: approved
last_reviewed: 2026-08-13
owner: Comité National d'Architecture Santé Numérique
tags: [standards, normes, homologation]
---

# Normes et standards d'architecture

## Pour qui lire ce document

**Niveau :** niveau 1 — Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ● |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../reading-matrix.md).

Ce domaine regroupe les **normes** (exigences obligatoires) et les **standards** (guides recommandés) applicables aux solutions numériques du secteur santé. Le catalogue détaillé est défini dans l'[Architecture de Référence Technique de la Santé Numérique](../../02_artsn/index.md) (ARTSN), document de niveau 3 distinct. La présente section fixe les règles de gouvernance des normes.

## Distinction normes / standards

| Type | Caractère | Usage |
|------|-----------|-------|
| Norme | Obligatoire | Condition d'homologation et de déploiement |
| Standard | Recommandé | Bonnes pratiques et cohérence technique |

Une norme est adoptée lorsqu'elle est indispensable à l'interopérabilité, à la sécurité des données, à la cohérence des référentiels ou à la soutenabilité des solutions. Toute norme doit être compatible avec les principes du cadre et les référentiels nationaux.

## Établissement d'une norme

1. Identification du besoin de standard interopérabilité, sécurité ou cohérence ;
2. Proposition documentée, référencée aux principes du cadre ;
3. Arbitrage par le Comité National d'Architecture Santé Numérique ;
4. Enregistrement sous forme d'ADR ([`../08_decisions/index.md`](../08_decisions/index.md)) ;
5. Publication et communication aux intégrateurs et partenaires ;
6. Revue périodique et révision.

Toute mise en œuvre d'une norme fait l'objet d'une homologation préalable ou d'une dérogation validée par l'instance nationale compétente. La conformité s'applique à toute solution déployée dans le secteur santé, qu'elle soit financée par le budget national ou par un partenaire.

## Template de norme

Un modèle de norme est proposé : [STD-0000 — modèle](./std-0000-template.md).

## Registre des normes

| Code | Titre | Type | Statut |
|------|-------|------|--------|
| STD-0000 | [Modèle de norme](./std-0000-template.md) | modèle | — |
| **STD-0001** | [Norme d'interopérabilité — HL7 FHIR R4](./std-0001-interopabilite-fhir.md) | Norme obligatoire | Approuvé |
| **STD-0002** | [Norme de sécurité — Chiffrement et contrôle d'accès](./std-0002-securite-chiffrement.md) | Norme obligatoire | Approuvé |
| **STD-0003** | [Norme d'échange interinstitutionnel — X-Road](./std-0003-x-road.md) | Norme obligatoire | Approuvé |
| **STD-0004** | [Norme de données agrégées — mADX](./std-0004-madx.md) | Norme obligatoire | Approuvé |
| **STD-0005** | [Norme d'identité patient — PIXm/PDQm](./std-0005-identite-pixm.md) | Norme obligatoire | Approuvé |
| **STD-0006** | [Norme terminologique — CIM-10 + LOINC](./std-0006-terminologie.md) | Norme obligatoire | Approuvé |
| **NORM-007** | [Règlement Sanitaire International (RSI 2005)](./norm-007-rsi.md) | Norme internationale obligatoire | Actif |
| **NORM-008** | [Tripartite Plus OMS–WOAH–FAO–PNUE](./norm-008-tripartite.md) | Cadre normatif international | Actif |

## Liens

- [Homologation](../05_application/lifecycle.md)
- [Principes d'architecture](../02_principles/index.md)
- [Décisions](../08_decisions/index.md)
- [Gouvernance](../07_governance/index.md)