---
domain: processus
id: PRC-13
type: processus-metier
niveau: "1"
title: Échange et coordination transfrontaliers
status: active
owner: DEPSI
version: "0.0.1"
envelope: 00_caesn/01_value-streams/vs-02-risk-protection.md
maps_to: []
implements: []
applies_to: ["CAP-INT-13", "CAP-15", "CAP-17"]
related: ["VS-02", "BO-07"]
tags: ["caesn", "niveau-1", "processus-metier", "PRC-13"]
uses: ["CMP-02", "CMP-06", "CMP-15"]
performed_by: ["ROL-05"]
---
# Échange et coordination transfrontaliers

## Objectif

Garantir, dans le respect de la souveraineté et des accords de confiance, les échanges de données et de services de santé au-delà des frontières : résumé international du patient (IPS), sections normalisées, confiance internationale, résolution d'identité pour patients transfrontaliers et coordination épidémique régionale.

Ce processus opérationnalise l'objet métier [BO-07 : Interopérabilité transfrontalière](../objets-metier/bo-07.md) et s'appuie sur la capacité [CAP-INT-13 : Interopérabilité transfrontalière](../../referentiel/capacites/cap-int-13.md), le chapitre [ART-7 : Sécurité, contrôle d'accès et résidence de la donnée](../../referentiel/chapitres/art-7.md) et le profil [PT-14 : Interopérabilité transfrontalière](../../03_ptisn/03_profils/pt-14-interopabilite-transfrontaliere.md).

## Étapes clés

- Établissement et maintien des accords de confiance mutuelle (GDHCN, conventions bilatérales).
- Production et consommation de résumés internationaux du patient (IPS) conformes FHIR.
- Résolution d'identité des patients étrangers et gestion des identifiants temporaires.
- Vérification du consentement et de la base légale pour chaque flux sortant.
- Journalisation et audit de tous les flux transfrontaliers.
