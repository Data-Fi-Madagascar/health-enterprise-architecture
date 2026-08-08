---
title: Normes et standards d'architecture
id: standards
domain: 09_standards
version: "0.1.0"
status: draft
last_reviewed: 2026-07-03
owner: Comité National d'Architecture Santé Numérique
tags: [standards, normes, homologation]
---

# Normes et standards d'architecture

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

## Liens

- [Homologation](../05_application/lifecycle.md)
- [Principes d'architecture](../02_principles/index.md)
- [Décisions](../08_decisions/index.md)
- [Gouvernance](../07_governance/index.md)