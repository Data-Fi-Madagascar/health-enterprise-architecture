---
id: art-5
type: chapitre
niveau: "3"
title: ART-5 — Cohérence et qualité des données
status: draft
owner: DEPSI
version: "0.0.1"
source: 02_artsn/03_chapitres/art-5-coherence-qualite-donnees.md
maps_to: ["cap-13"]
implements: []
applies_to: ["enf-5"]
related: []
tags: ['artsn', 'niveau-3', 'chapitre', 'art-5']
---
# ART-5 — Cohérence et qualité des données

**Contenu normatif.** Tout flux ingéré doit être audité en continu face aux dimensions de qualité des données. En cas de détection d’anomalie, le système a l’obligation de router l’événement vers l’une des **branches d’escalade humaine** définies réglementairement. Les circuits cibles sont : sécurité clinique, alerte épidémiologique, fraude financière, risque intersectoriel.

**Discipline existentielle.** Dès lors qu’une source échappe à la gouvernance directe de l’initiative (données corrompues du terrain, anomalies massives de facturation) : elle seule permet d’aiguiller le problème vers la bonne cellule humaine de décision stratégique sans rompre le pipeline.

- **Rattachement** : [CAP-13](../capabilites/cap-13.md) (gestion des données sanitaires).
- **Référentiel cible** : DAMA/DMBOK.
- **Circuits cibles** : sécurité clinique, alerte épidémiologique, fraude financière, risque intersectoriel.
- **Déduit selon** : [ENF-5](../exigences/enf-5.md) (coordination des processus).
- **Statut : Stable** (pour les métriques) / **Proposition ouverte** (pour la gouvernance des 4 branches).
