---
title: Règles d'urbanisation applicative
id: application-urbanisation
domain: 05_application
version: "0.0.1"
status: draft
last_reviewed: 2026-07-03
owner: Direction des Systèmes d'Information
tags: [applications, urbanisation]
---

# Règles d'urbanisation applicative

## Pour qui lire ce document

**Niveau :** niveau 1 — Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ○ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../reading-matrix.md).

L'urbanisation vise à organiser le paysage applicatif pour éviter les doublons, clarifier les responsabilités et faciliter l'évolution du système.

1. **Une application ne doit pas devenir propriétaire d'un référentiel national.** Elle peut contribuer à l'alimenter ou le consommer, mais le référentiel reste un bien commun gouverné nationalement.
2. **Une application ne doit pas collecter une donnée déjà disponible.** Elle réutilise les données existantes via les mécanismes d'échange homologués.
3. **Une application métier reste centrée sur son processus opérationnel.** Elle n'absorbe pas indéfiniment des fonctions de reporting, de référentiel, d'identité ou d'intégration relevant de services partagés.
4. **Une application analytique ne remplace pas un système opérationnel.** Un entrepôt de données ne devient pas le lieu principal de correction des activités.
5. **Les applications exposent des interfaces documentées.** Les échanges sont décrits dans des contrats d'interface validés dans l'Architecture de Référence Technique.
6. **Les doublons applicatifs sont identifiés et rationalisés.** Une trajectoire de consolidation, coexistence, interopérabilité ou retrait est définie.
7. **Les applications pilotes ont une trajectoire claire.** Elles précisent si elles seront généralisées, intégrées, remplacées ou arrêtées.
8. **Les applications sont conçues pour évoluer.** Les choix évitent la dépendance excessive à un fournisseur, un bailleur ou une architecture fermée.

## Liens

- [Principes de l'architecture applicative](./principles.md)
- [Rationalisation](./rationalization.md)
- [Services partagés](./shared-services.md)