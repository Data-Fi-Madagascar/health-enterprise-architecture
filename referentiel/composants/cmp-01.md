---
id: CMP-01
type: composant-applicatif
niveau: "1"
title: Tableaux de bord & Portails nationaux (performance, CSU, ressources, veille)
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_cartographie-cible/index.md
maps_to: ["CAP-INT-07", "CAP-INT-11"]
implements: ["ART-6"]
applies_to: ["PRC-10", "PRC-11", "PRC-12"]
related: ["ENF-5", "CAP-13", "CAP-16", "VS-04"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-01", "couche-6"]
---
# Tableaux de bord & Portails nationaux

**Contenu normatif.** Ce composant agrège les projections analytiques (Couche 5) et expose des tableaux de bord unifiés pour le pilotage national : performance sanitaire, suivi CSU, gestion des ressources et veille environnementale. L'accès y est cloisonné par profil (décideurs, SIS, partenaires). Il interopère avec l'entrepôt Lakehouse ([CMP-03: Entrepôt Lakehouse & Projections analytiques (pipeline ETL, Lakehouse, projections)](cmp-03.md)) et le moteur analytique ([CMP-04: Moteur analytique & IA (IA prédictive, routeur alertes, Grand Livre)](cmp-04.md)).

**Discipline de mise en œuvre.** Il constitue la seule source de vérité décisionnelle pour l'État ; tout indicateur officiel y transite. Il garantit l'unicité des métriques et la traçabilité des calculs.

- **Rattachement** : [ART-6](../chapitres/art-6.md) (projections analytiques), [CAP-INT-07: Accès et exposition des données analytiques](../capacites/cap-int-07.md), [CAP-INT-11: Qualité et réconciliation](../capacites/cap-int-11.md).
- **Processus soutenus** : [PRC-10: Planification et allocation des ressources](../processus/prc-10.md) (planification), [PRC-11: Suivi et pilotage de la performance](../processus/prc-11.md) (pilotage performance), [PRC-12: Redevabilité et amélioration continue](../processus/prc-12.md) (redevabilité).
- **Statut : Stable.**
