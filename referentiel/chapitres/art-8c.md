---
id: art-8c
type: chapitre
niveau: "4"
title: ART-8c — Agrégation par lot
status: draft
owner: DEPSI
version: "0.0.1"
source: 02_artsn/03_chapitres/art-8c-agregation-par-lot.md
maps_to: ["cap-13", "cap-14"]
implements: []
applies_to: ["enf-1", "enf-2"]
related: ["art-8"]
tags: ['artsn', 'niveau-4', 'chapitre', 'art-8c']
---
# ART-8c — Agrégation par lot

**Contenu normatif.** L'architecture doit intégrer un moteur de traitement par lots capable de suspendre le flux transactionnel instantané pour regrouper les micro-agrégats individuels en un seul **agrégat consolidé de niveau supérieur** (pattern cible : *Netting*).

**Discipline existentielle.** Dès lors qu'une source échappe à la gouvernance directe de l'initiative (demandes massives de remboursements des pharmacies rurales, vagues de facturations d'hôpitaux) : elle seule permet de compiler les flux locaux et de générer une compensation globale unifiée sans saturer les réseaux d'échange centraux et sans rompre le pipeline.

- **Rattachement** : [CAP-13](../capabilites/cap-13.md), [CAP-14](../capabilites/cap-14.md).
- **Pattern cible** : Netting.
- **Déduit selon** : [ENF-1](../exigences/enf-1.md) (réseau instable) et [ENF-2](../exigences/enf-2.md) (anti-fraude).
- **Statut : Proposition ouverte.**
