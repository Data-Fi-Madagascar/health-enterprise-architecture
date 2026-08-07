---
title: Contraintes d'exploitation différenciées
id: application-constraints
domain: application
version: "0.1.0"
status: draft
last_reviewed: 2026-07-03
owner: Direction des Systèmes d'Information
tags: [applications, exploitation, terrain]
---

# Contraintes d'exploitation différenciées

Madagascar présente plusieurs contextes d'exploitation numérique. Les applications doivent être conçues en fonction du contexte réel d'utilisation, non uniquement des conditions du niveau central.

| Contexte | Caractéristiques | Exigences applicatives |
|----------|------------------|------------------------|
| Connecté | Niveau central, régions et établissements mieux équipés | Applicatifs web, échanges fréquents, synchronisation régulière, tableaux de bord avancés |
| Intermittent | Districts, FOSA avec connectivité instable | Mode dégradé, synchronisation différée, tolérance aux coupures, files d'attente d'échanges |
| Faible connectivité / hors ligne | Zones rurales, communautés, connectivité limitée ou absente | Fonctionnement hors ligne, saisie locale, synchronisation ultérieure, interfaces simples, support mobile |
| Mode assisté | Utilisateurs à faible littératie numérique ou équipements limités | Parcours simplifiés, assistance par agent, impression ou QR code, langage adapté |

Toute application destinée au terrain (formations sanitaires, districts, communautés) doit au minimum satisfaire le contexte intermittent. Les applications critiques pour le soin, la surveillance ou la protection financière prévoient des mécanismes de continuité en cas d'indisponibilité réseau.

## Liens

- [Architecture applicative](./index.md)
- [Principes AA-05](./principles.md)