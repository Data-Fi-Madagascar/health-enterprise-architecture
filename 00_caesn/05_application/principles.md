---
title: Principes de l'architecture applicative
id: application-principles
domain: 05_application
version: "0.1.0"
status: draft
last_reviewed: 2026-07-03
owner: Direction des Systèmes d'Information
tags: [applications, urbanisation, principes]
---

# Principes de l'architecture applicative

## Pour qui lire ce document

**Niveau :** niveau 1 — Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ○ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../10_annexes/reading-matrix.md).

Les principes suivants s'appliquent à toute application ou plateforme numérique du secteur santé.

| Code | Principe | Signification | Implications |
|------|----------|---------------|--------------|
| AA-01 | Les applications sont dérivées des flux de valeur et des capabilités | Une application n'a de légitimité que si elle soutient une capabilité nécessaire à un flux | Toute application indique le flux, la capabilité, les données et les indicateurs qu'elle soutient |
| AA-02 | Les applications ne doivent pas dupliquer les référentiels nationaux | Les référentiels sont des biens communs, non des composants internes | Une application consomme les référentiels nationaux plutôt que créer ses propres listes (FOSA, agents, produits, indicateurs, bénéficiaires) |
| AA-03 | Les applications doivent être interopérables par conception | L'interopérabilité ne doit pas être ajoutée après déploiement | Toute application expose/consomme des interfaces documentées, sécurisées, conformes à l'Architecture de Référence Technique |
| AA-04 | Les applications opérationnelles et analytiques doivent être séparées | Un outil de prestation ne doit pas devenir un outil de reporting, et un entrepôt ne doit pas remplacer un système opérationnel | Les systèmes opérationnels soutiennent l'action ; les entrepôts et tableaux de bord soutiennent l'analyse |
| AA-05 | Les applications doivent fonctionner dans les conditions réelles du terrain | Le contexte impose des usages à connectivité limitée | Les applications destinées au terrain prévoient le mode hors ligne ou dégradé |
| AA-06 | Les plateformes partagées doivent être réutilisées avant de créer de nouveaux composants | Le système doit éviter la multiplication des solutions parallèles | Avant un nouveau composant, vérifier l'existence d'un service partagé national |
| AA-07 | Les applications doivent être soutenables | Une dépendance durable à un partenaire unique fragilise le système national | Toute application modèle de maintenance, support, transfert de compétences, coût total de possession et réversibilité |
| AA-08 | Les applications doivent être homologuées avant extension | Une application pilote ne doit pas être généralisée sans validation | L'extension est conditionnée à l'alignement sur cadre, standards, sécurité, valeur |
| AA-09 | Les applications obsolètes ou redondantes doivent être rationalisées | Le portefeuille doit évoluer, pas s'accumuler | Les doublons, systèmes non utilisés ou non conformes sont consolidés, remplacés ou retirés |

## Liens

- [Architecture applicative](./index.md)
- [Règles d'urbanisation](./urbanisation.md)
- [Rationalisation](./rationalization.md)