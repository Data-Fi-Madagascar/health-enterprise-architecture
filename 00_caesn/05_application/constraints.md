---
title: Contraintes d'exploitation différenciées
id: application-constraints
domain: 05_application
version: "1.0.0"
status: draft
last_reviewed: 2026-07-03
owner: Direction des Systèmes d'Information
tags: [applications, exploitation, terrain]
---

# Contraintes d'exploitation différenciées

## Pour qui lire ce document

**Niveau :** niveau 1 : Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ○ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

Madagascar présente plusieurs contextes d'exploitation numérique. Les applications doivent être conçues en fonction du contexte réel d'utilisation, non uniquement des conditions du niveau central.

| Contexte | Caractéristiques | Exigences applicatives |
|----------|------------------|------------------------|
| Connecté | Niveau central, régions et établissements mieux équipés | Applicatifs web, échanges fréquents, synchronisation régulière, tableaux de bord avancés |
| Intermittent | Districts, FOSA avec connectivité instable | Mode dégradé, synchronisation différée, tolérance aux coupures, files d'attente d'échanges |
| Faible connectivité / hors ligne | Zones rurales, communautés, connectivité limitée ou absente | Fonctionnement hors ligne, saisie locale, synchronisation ultérieure, interfaces simples, support mobile |
| Mode assisté | Utilisateurs à faible littératie numérique ou équipements limités | Parcours simplifiés, assistance par agent, impression ou QR code, langage adapté |

Toute application destinée au terrain (formations sanitaires, districts, communautés) doit au minimum satisfaire le contexte intermittent. Les applications critiques pour le soin, la surveillance ou la protection financière prévoient des mécanismes de continuité en cas d'indisponibilité réseau.

## Liens

- Architecture applicative
- Principes AA-05

## Références

- **matrice de lecture** : Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
- **Architecture applicative** : Architecture applicative et systèmes numériques (`00_caesn/05_application/index.md`)
- **Principes AA-05** : Principes de l'architecture applicative (`00_caesn/05_application/principles.md`)
