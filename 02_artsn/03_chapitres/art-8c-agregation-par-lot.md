---
title: ART-8c — Agrégation par lot
id: art-8c-agregation-par-lot
domain: 02_artsn
version: "0.1.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, chapitres, art-8c, batch, netting, niveau-3]
---

# ART-8c — Agrégation par lot

**Contenu normatif.** L'architecture doit intégrer un moteur de traitement par lots capable de suspendre le flux transactionnel instantané pour regrouper les micro-agrégats individuels en un seul **agrégat consolidé de niveau supérieur** (pattern cible : *Netting*).

**Discipline existentielle.** Dès lors qu'une source échappe à la gouvernance directe de l'initiative (demandes massives de remboursements des pharmacies rurales, vagues de facturations d'hôpitaux) : elle seule permet de compiler les flux locaux et de générer une compensation globale unifiée sans saturer les réseaux d'échange centraux et sans rompre le pipeline.

- **Rattachement** : [CAP-13](../../00_caesn/03_capabilities/index.md), [CAP-14](../../00_caesn/03_capabilities/index.md).
- **Pattern cible** : Netting.
- **Déduit selon** : [ENF-1](../02_exigences-contextuelles.md#enf-1--résilience-à-l-instabilité-réseau) (réseau instable) et [ENF-2](../02_exigences-contextuelles.md#enf-2--intégrité-des-flux-et-traçabilité-des-valeurs) (anti-fraude).
- **Statut : Proposition ouverte.**

## Liens

- [Index des chapitres](./index.md)
- [ART-8 — Orchestration de processus borné](./art-8-orchestration-processus-borne.md)
- [Couche 3 — Échange, transport et ingestion](../04_cartographie-cible.md)
