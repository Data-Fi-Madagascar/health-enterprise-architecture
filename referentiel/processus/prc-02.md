---
domain: processus
id: PRC-02
type: processus-metier
niveau: "1"
title: Prestation des soins cliniques
status: active
owner: Direction des soins
version: "0.0.1"
envelope: 00_caesn/01_value-streams/vs-01-access-care.md
maps_to: []
implements: []
applies_to: ["CAP-01", "CAP-03", "CAP-09", "CAP-10", "CAP-11", "CAP-13", "CAP-14", "CAP-15"]
related: ["VS-01-03", "VS-01-04", "VS-01-05", "VS-01", "BO-02", "BO-03"]
tags: ["caesn", "niveau-1", "processus-metier", "PRC-02"]
uses: ["CMP-19", "CMP-20", "CMP-21"]
performed_by: ["ROL-02"]
---
# Prestation des soins cliniques

## Objectif

Assurer le cœur clinique du parcours : consultation et diagnostic, traitement et prise en charge, référence et contre-référence vers le niveau de soins supérieur.

## Étapes couvertes

- [VS-01-03: Consultation et diagnostic](../etapes-valeur/vs-01-03.md)
- [VS-01-04: Traitement et prise en charge](../etapes-valeur/vs-01-04.md)
- [VS-01-05: Référence et contre-référence](../etapes-valeur/vs-01-05.md)

## Acteurs

Clinicien, dossier patient, pharmacie, laboratoire, formation sanitaire référente, formation cible, système de transport

## Indicateurs

Taux de consultations avec diagnostic documenté, taux de disponibilité des médicaments traceurs, taux de référence complétée avec retour d'information
