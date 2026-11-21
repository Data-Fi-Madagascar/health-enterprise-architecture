---
domain: principles
id: P-INT-07
type: principe
niveau: "2"
title: Responsabilité de la donnée
status: active
owner: DEPSI
version: "0.5"
envelope: 01_cnisn/01_principes/index.md
maps_to: ["CAP-13"]
implements: []
applies_to: []
related: ["ABB-ECHANGE-MEDIATION", "ABB-CATALOGUE-CONTRATS", "ABB-EXPOSITION-DONNEES-ANALYTIQUES", "ABB-AUDIT-PROVENANCE", "ABB-RECONCILIATION-DONNEES"]
tags: ["cnisn", "niveau-2", "principe"]
---

# Responsabilité de la donnée

Pour chaque donnée ou événement échangé, les responsabilités suivantes doivent être explicites :

- source autoritative de l’état courant ;
- propriétaire fonctionnel ;
- responsable technique ;
- producteur ;
- consommateur ;
- responsable de la qualité ;
- responsable de la correction ;
- responsable de la conservation.

Aucun composant ne doit être déclaré « source unique de vérité » sans préciser la responsabilité exacte concernée.

Il convient de distinguer :

- l’état opérationnel courant ;
- l’historique capturé ;
- la preuve de réception ;
- les métadonnées ;
- la projection analytique ;
- la restitution.
