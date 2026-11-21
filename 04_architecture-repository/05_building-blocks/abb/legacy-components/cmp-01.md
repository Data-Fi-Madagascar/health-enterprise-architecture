---
domain: legacy-components
id: CMP-01
type: composant-applicatif
categorie: applicatif
niveau: "1"
title: Tableaux de bord & Portails nationaux (performance, CSU, ressources, veille)
status: active
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/05_cartographie/composants.md
maps_to: ["ABB-EXPOSITION-DONNEES-ANALYTIQUES", "ABB-RECONCILIATION-DONNEES"]
implements: ["ART-6"]
applies_to: ["PRC-04", "PRC-10", "PRC-11", "PRC-12"]
accesses: ["DO-25", "DO-26", "DO-27"]
related: ["ENF-5", "CAP-13", "CAP-16", "VS-04"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-01", "couche-6"]
---
# Tableaux de bord & Portails nationaux

**Contenu normatif.** Ce composant agrège les projections analytiques (Couche 5) et expose des tableaux de bord unifiés pour le pilotage national : performance sanitaire, suivi CSU, gestion des ressources et veille environnementale. L'accès y est cloisonné par profil (décideurs, SIS, partenaires). Il interopère avec l'entrepôt Lakehouse ([CMP-03: Entrepôt Lakehouse & Projections analytiques (pipeline ETL, Lakehouse, projections)](cmp-03.md)) et le moteur analytique ([CMP-04: Moteur analytique & IA (IA prédictive, routeur alertes, Grand Livre)](cmp-04.md)).

**Discipline de mise en œuvre.** Il constitue la seule source de vérité décisionnelle pour l'État ; tout indicateur officiel y transite. Il garantit l'unicité des métriques et la traçabilité des calculs.

**Configuration des tableaux de bord.** Le tableau de bord national est une vue consolidée et synthétique d'indicateurs de performance, affichée aux décideurs à des fins de pilotage. Il agrège des données provenant de plusieurs sources (formations sanitaires, programmes, districts) et les présente sous forme graphique avec des seuils d'alerte. Cette configuration est un artefact de restitution propre au composant et non un objet de données : la source de vérité des indicateurs reste le référentiel [DO-25 : Indicateur sanitaire](../../../02_architecture-elements/data/data-objects/do-25.md). Chaque tableau est décrit par les attributs suivants : indicateurs affichés (identifiant, libellé, unité), périmètre géographique (échelon de restitution), période (fenêtre d'agrégation et périodicité), fréquence de mise à jour (recalcul et publication), seuils d'alerte (valeurs et couleur de dépassement), niveau d'accès requis (profil cloisonné décideurs, SIS, partenaires) et destinataires (instances recevant la vue). L'objet de données DO-28 (Tableau de bord) est à ce titre retiré du catalogue par l'ADR-0014 : sa charge utile est hébergée par ce composant, sa source de vérité restant DO-25.

- **Rattachement** : [ART-6](../../../04_patterns/artsn-rules/art-6.md) (projections analytiques), [ABB-EXPOSITION-DONNEES-ANALYTIQUES: Accès et exposition des données analytiques](../abb-exposition-donnees-analytiques.md), [ABB-RECONCILIATION-DONNEES: Qualité et réconciliation](../abb-reconciliation-donnees.md).
- **Processus soutenus** : [PRC-10: Planification et allocation des ressources](../../../02_architecture-elements/business/processes/prc-10.md) (planification), [PRC-11: Suivi et pilotage de la performance](../../../02_architecture-elements/business/processes/prc-11.md) (pilotage performance), [PRC-12: Redevabilité et amélioration continue](../../../02_architecture-elements/business/processes/prc-12.md) (redevabilité).
- **Données portées** : [DO-25 : Indicateur sanitaire](../../../02_architecture-elements/data/data-objects/do-25.md), [DO-26 : Zone sanitaire](../../../02_architecture-elements/data/data-objects/do-26.md), [DO-27 : Tâche et action de suivi](../../../02_architecture-elements/data/data-objects/do-27.md)
- **Statut : Stable.**
