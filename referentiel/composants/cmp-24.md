---
domain: composants
id: CMP-24
type: composant-applicatif
categorie: applicatif
niveau: "1"
title: Surveillance de la sante animale (zoonoses)
status: active
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/05_cartographie/composants.md
implements: ["ENF-1", "F-1"]
maps_to: ["CAP-INT-14"]
applies_to: ["PRC-04", "PRC-05"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-24", "couche-2"]
related: ["VS-02", "VS-04"]
---
# CMP-24 : Surveillance de la sante animale (zoonoses)
**Contenu normatif.** Ce composant assure la surveillance sanitaire animale et la detection precoce des zoonoses dans une logique One Health. Il collecte les evenements chez les animaux (foyers, signaux cliniques, mouvements de cheptels), les croise avec la surveillance humaine (CMP-25, PRC-04) et declenche les alertes inter-sectorielles. Il s'appuie sur les referentiels de terminologie animal/humain et les registres des structures veterinaires.
**Discipline de mise en oeuvre.** L'interoperabilite avec la surveillance humaine est obligatoire : un meme evenement peut avoir une composante animale et humaine. Les signalements respectent les formats de messagerie d'alerte (ART-8) et sont horodates. Les donnees zoologiques et humaines sont cloisonnees par finalite et ne sont jointes qu'au sein des pipelines d'analyse autorises (CMP-03/CMP-04).
- **Rattachement** : [ENF-1: Resilience a l'instabilite reseau](../exigences/enf-1.md), [F-1: Resilience face a la realite geographique du pays](../fondations/f-1.md).
- **Processus soutenus** : [PRC-04: Veille, prevention et surveillance sanitaire](../processus/prc-04.md) (veille et prevention), [PRC-05: Alerte, investigation et riposte](../processus/prc-05.md) (alerte et riposte).
- **Statut : Brouillon.**
