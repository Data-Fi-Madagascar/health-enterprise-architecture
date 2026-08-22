---
domain: chapitres

id: ART-7
type: chapitre
niveau: "3"
title: Sécurité, contrôle d'accès et résidence de la donnée
status: stable
maturity_condition: "—"
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/04_patterns/art-7-securite-controle-acces.md
maps_to: ["CAP-15"]
implements: []
applies_to: ["ENF-1"]
related: []
tags: ["artsn", "niveau-3", "chapitre", "ART-7"]
---
# Sécurité, contrôle d’accès et résidence de la donnée

**Contenu normatif.** L’architecture impose un modèle de sécurité **strict par défaut**. Le contrôle d’accès doit combiner le rôle de l’agent et ses attributs contextuels ou territoriaux. Tout accès, lecture ou écriture doit être chiffré et journalisé de manière immuable. Les données de santé des citoyens ont l’obligation légale de **résider physiquement sur le territoire national** (copie maîtresse).

**Règle résidence ↔ échange.** La résidence obligatoire concerne la **donnée au repos** (copie maîtresse hébergée sur le territoire national, [STD-0002](../../01_cnisn/05_standards/std-0002-securite-chiffrement.md)). Elle ne fait pas obstacle aux **échanges transfrontaliers**, qui ne portent que des données **en transit**, chiffrées et horodatées, sans déplacement de la copie maîtresse : l’échange inter-institutionnel emprunte X-Road ([ADR-0001](../../01_cnisn/06_decisions/adr-0001-x-road.md)) et l’échange international emprunte la passerelle de confiance mondiale OMS GDHCN ([ADR-0007](../../01_cnisn/06_decisions/adr-0007-gdhcn.md)). La résidence et l’échange sont donc compatibles : seule la copie maîtresse est souveraine ; les flux sortants sont des vues chiffrées et révocables.

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (terminaux mobiles volés sur le terrain, tentatives d’intrusions extérieures, flux sortants vers partenaires étrangers), cette discipline seule permet de garantir l’inviolabilité du secret médical et la souveraineté numérique de l’État sans rompre le pipeline.

- **Rattachement** : [CAP-15: Cybersécurité, confidentialité et gouvernance des données personnelles](../capabilites/cap-15.md) (cybersécurité et gouvernance de la sécurité).
- **Modèles cibles** : Zero-Trust, RBAC, ABAC, chiffrement (AES-256), AuditEvent FHIR.
- **Normes CNISN** : [STD-0002: Sécurité et chiffrement](../../01_cnisn/05_standards/std-0002-securite-chiffrement.md), [ADR-0001: X-Road](../../01_cnisn/06_decisions/adr-0001-x-road.md), [ADR-0007: GDHCN](../../01_cnisn/06_decisions/adr-0007-gdhcn.md), [ADR-0008: Audit ATNA](../../01_cnisn/06_decisions/adr-0008-atna.md).
- **Déduit selon** : [ENF-1: Résilience à l'instabilité réseau](../exigences/enf-1.md) (sécurité locale).
- **Statut : Stable.**
