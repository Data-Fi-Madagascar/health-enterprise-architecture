---
domain: chapitres

id: ART-5
type: chapitre
niveau: "3"
title: Cohérence et qualité des données
status: stable
maturity_condition: "Stable pour principe ; Proposition ouverte pour branches d'escalade. Condition : instruction détaillée de chaque branche par domaine"
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_patterns/art-5-coherence-qualite-donnees.md
maps_to: ["CAP-13"]
implements: []
applies_to: ["ENF-5"]
related: []
tags: ["artsn", "niveau-3", "chapitre", "ART-5"]
---
# Cohérence et qualité des données

**Contenu normatif.** Tout flux ingéré doit être audité en continu face aux dimensions de qualité des données. En cas de détection d’anomalie, le système doit router l’événement vers l’une des **branches d’escalade humaine** définies réglementairement. Les circuits cibles sont : sécurité clinique, alerte épidémiologique, fraude financière, risque intersectoriel.

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (données corrompues du terrain, anomalies massives de facturation), cette discipline seule permet d’aiguiller le problème vers la bonne cellule humaine de décision stratégique sans rompre le pipeline.

- **Rattachement** : [CAP-13: Système d'information sanitaire, données et recherche](../capabilites/cap-13.md) (gestion des données sanitaires).
- **Référentiel cible** : DAMA/DMBOK.
- **Circuits cibles** : sécurité clinique, alerte épidémiologique, fraude financière, risque intersectoriel.
- **Déduit selon** : [ENF-5: Coordination des processus complexes décentralisés et asynchrones](../exigences/enf-5.md) (coordination des processus).
- **Statut : Stable.** (pour les métriques) / **Statut : Proposition ouverte.** (pour la gouvernance des 4 branches).
