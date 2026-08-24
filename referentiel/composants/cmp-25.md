---
domain: composants
id: CMP-25
type: composant-applicatif
categorie: applicatif
niveau: "1"
title: Enquetes & capteurs terrain
status: draft
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/05_cartographie/composants.md
implements: ["ENF-1", "F-1"]
applies_to: ["PRC-04", "PRC-05", "PRC-11"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-25", "couche-2"]
---
# CMP-25 : Enquetes & capteurs terrain
**Contenu normatif.** Ce composant gere les enquetes de terrain (enquetes sante, collectes ciblees) et les flux de capteurs environnementaux et de sante publique (meteo, qualite de l'air, eau, capteurs de surveillance). Il ingest les donnees, en verifie la provenance et l'horodatage, et les met a disposition de la veille (PRC-04) et du pilotage de la performance (PRC-11). Il alimente egalement les tableaux de bord (CMP-01).
**Discipline de mise en oeuvre.** La qualite et la provenance des donnees capteurs sont garanties (signature a la source, horodatage fiable). Les resultats sont reconcilies avant publication afin d'eviter les doubles comptes. Les protocoles d'enquete sont versionnes et tracables. Les flux exterieurs (partenaires, capteurs tiers) sont admis selon des accords references (CMP-39).
- **Rattachement** : [ENF-1: Resilience a l'instabilite reseau](../exigences/enf-1.md), [F-1: Resilience face a la realite geographique du pays](../fondations/f-1.md).
- **Processus soutenus** : [PRC-04: Veille, prevention et surveillance sanitaire](../processus/prc-04.md) (veille terrain), [PRC-05: Alerte, investigation et riposte](../processus/prc-05.md) (alerte), [PRC-11: Suivi et pilotage de la performance](../processus/prc-11.md) (pilotage de la performance).
- **Statut : Brouillon.**
