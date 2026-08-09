---
title: Capabilités du système de santé
id: capabilities
domain: 03_capabilities
version: "0.1.0"
status: draft
last_reviewed: 2026-07-03
owner: Responsables de capabilités
tags: [capabilités, catalogue]
---

# Capabilités du système de santé

## Pour qui lire ce document

**Niveau :** niveau 1 — Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../reading-matrix.md).

## Définition et rôle

Une **capabilité** désigne ce que le système de santé doit être durablement capable de faire pour produire la valeur attendue des bénéficiaires. Elle n'est pas une activité ponctuelle, un projet, une application ou un outil. Elle repose sur la combinaison de :

- responsabilités institutionnelles clairement définies ;
- processus métier documentés et appliqués ;
- ressources humaines compétentes ;
- données fiables et disponibles ;
- outils numériques adaptés ;
- mécanismes de gouvernance ;
- ressources financières et opérationnelles soutenables.

## Distinction flux de valeur / capabilité

- Un **flux de valeur** décrit le résultat attendu pour un bénéficiaire.
- Une **capabilité** décrit ce que le système doit savoir faire pour produire ce résultat.

Un même flux mobilise plusieurs capabilités, et une même capabilité peut contribuer à plusieurs flux. L'investissement se justifie par sa contribution au renforcement d'une capabilité nécessaire à l'exécution d'un ou de plusieurs flux.

L'évaluation d'une initiative doit répondre à :

1. quel flux de valeur l'initiative sert-elle ?
2. quelle étape du flux est ciblée ?
3. quel principe de domaine l'initiative permet-elle de respecter ?
4. quelle capabilité nationale renforce-t-elle ?
5. quel est le niveau de maturité actuel ?
6. quel niveau de maturité cible permet-elle d'atteindre ?
7. quelles données, référentiels ou composants sont nécessaires ?
8. quels indicateurs vérifient que la capabilité produit de la valeur ?
9. quels risques de fragmentation, dépendance, non-adoption ou non-soutenabilité sont à maîtriser ?

Une initiative qui ne renforce aucune capabilité identifiée ni contribution à un flux de valeur national n'est pas prête à être financée.

## Typologie

| Type | Rôle |
|------|------|
| [Capabilités métier](./business.md) | Capabilités directement orientées à la production de valeur pour les bénéficiaires. |
| [Capabilités habilitantes](./enabling.md) | Conditions de fonctionnement dont l'absence bloque l'exécution des flux de valeur. |
| [Capabilités numériques transversales](./digital.md) | Socle numérique issu de la SNSD et des référentiels DPI-H, OpenHIE, GovStack. |

## Lecture des capabilités par flux de valeur

| Flux de valeur | Capabilités principales | Capabilités habilitantes critiques |
|----------------|-------------------------|-----------------------------------|
| VS-01 Soins essentiels | CAP-01, 02, 03, 04 | CAP-09, 10, 11, 13, 14, 15 |
| VS-02 Prévention et surveillance | CAP-04, 05, 06 | CAP-09, 10, 11, 13, 14, 15 |
| VS-03 Protection financière | CAP-07 | CAP-08, 12, 13, 14, 15, 16 |
| VS-04 Pilotage du système | CAP-03, 08, 13, 16 | CAP-09, 12, 14, 15 |

## Maturité et priorisation

Chaque capabilité est évaluée sur une échelle de maturité (1 à 5). Le delta entre niveau actuel et niveau critique guide la priorisation et la mesure du renfort. Voir [Maturité](./maturity.md).

## Architecture runway

Quatre capabilités constituent le socle commun (architecture runway) dont l'absence bloque de nombreuses initiatives : **CAP-13, CAP-14, CAP-15, CAP-16**. Voir [Runway](./runway.md).

## Liens

- [Flux de valeur](../01_value-streams/index.md)
- [Portefeuille](../06_portfolio/index.md)
- [Données](../04_data/index.md)