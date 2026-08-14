---
title: Décisions d'architecture (ADR)
id: decisions
domain: 08_decisions
version: "0.0.1"
status: draft
last_reviewed: 2026-07-03
owner: Bureau de Réalisation de la Valeur
tags: [décisions, adr]
---

# Décisions d'architecture (ADR)

## Pour qui lire ce document

**Niveau :** niveau 1 — Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../reading-matrix.md).

Les décisions d'architecture sont enregistrées sous forme d'Architecture Decision Records (ADR). Chaque ADR documente un choix structurant de façon concise, datée et traçable, afin de préserver la mémoire des choix et de leurs justifications.

Un ADR est produit lorsque le Comité National d'Architecture Santé Numérique statue sur un arbitrage, une homologation, un standard, une dérogation ou un choix technique structurant. Les ADR applicables au domaine applicatif sont mentionnés dans [`../application/index.md`](../05_application/index.md).

## Modèle

Chaque ADR suit le [modèle type](./adr-0000-template.md), avec un statut parmi `proposé`, `accepté`, `appliqué`, `remplacé`, `déprécié`.

## Registre des ADR

| ADR | Titre | Statut | Date |
|-----|-------|--------|------|
| ADR-0000 | [Template](./adr-0000-template.md) | modèle | — |
| ADR-0001 | [X-Road — Plateforme d'échange](./adr-0001-x-road.md) | appliqué | 2026-07-01 |
| ADR-0002 | [mADX — Données agrégées](./adr-0002-madx.md) | appliqué | 2026-07-01 |
| ADR-0003 | [HL7 FHIR — Standard d'interopérabilité](./adr-0003-fhir.md) | appliqué | 2026-07-01 |
| ADR-0004 | [PIXm/PDQm — Résolution d'identité](./adr-0004-identite.md) | appliqué | 2026-07-01 |
| ADR-0005 | [FHIR Consent — Consentement structuré](./adr-0005-consentement.md) | proposé | 2026-08-13 |
| ADR-0006 | [INP — Identité nationale patient](./adr-0006-inp.md) | proposé | 2026-08-13 |
| ADR-0007 | [GDHCN — Confiance transfrontalière](./adr-0007-gdhcn.md) | proposé | 2026-08-13 |
| ADR-0008 | [ATNA — Audit et traçabilité](./adr-0008-atna.md) | proposé | 2026-08-13 |
| ADR-0009 | [Terminologie — CIM-10 + LOINC](./adr-0009-terminologie.md) | proposé | 2026-08-13 |

## Outils de gestion des décisions

| Outil | Description |
|-------|-------------|
| [Registre des décisions](./registre-decisions.md) | Tableau centralisé de toutes les ADRs avec statut et impact |
| [Template de modification](./template-modification.md) | Structure standardisée pour proposer un changement architectural |

## Liens

- [Gouvernance](../07_governance/index.md)
- [Portefeuille](../06_portfolio/index.md)
- [Normes](../09_standards/index.md)