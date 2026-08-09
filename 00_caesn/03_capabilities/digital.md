---
title: Capabilités numériques transversales et composantes DPI-H
id: capabilities-digital
domain: 03_capabilities
version: "0.1.0"
status: draft
last_reviewed: 2026-07-03
owner: Responsable des capabilités numériques
tags: [capabilités, numérique, snsd]
---

# Capabilités numériques transversales et composants DPI-H

## Pour qui lire ce document

**Niveau :** niveau 1 — Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../10_annexes/reading-matrix.md).

Les capabilités numériques transversales traduisent les axes de la Stratégie Nationale de Santé Digitale (SNSD) et les exigences des référentiels DPI-H, OpenHIE et GovStack. Elles ne constituent pas des finalités autonomes, mais un socle numérique au service des flux de valeur santé.

## Capabilités numériques issues de la SNSD

| Code | Capabilité numérique | Ce qu'elle recouvre |
|------|----------------------|---------------------|
| DIG-01 | Gouvernance digitale, normes et coordination | Cadres juridiques, normes, standards, mécanismes de coordination nationale, régulation du numérique santé et homologation des initiatives. |
| DIG-02 | Architecture, urbanisation et solutions numériques | Architecture cible du système d'information, urbanisation, digitalisation des services prioritaires, interopérabilité et promotion de l'usage. |
| DIG-03 | Ressources, infrastructures et compétences numériques | Connectivité, équipements, compétences numériques des agents, support technique, hébergement, exploitation et mise aux normes. |
| DIG-04 | Financement durable et alignement des investissements | Modèle de financement du portefeuille, mobilisation des partenaires, coût total de possession et soutenabilité des plateformes. |

## Composants DPI-H couverts

| Composante DPI-H | Couverture dans le cadre | Critères de sélection |
|------------------|--------------------------|-----------------------|
| Identité Patient / numérique | Référentiel national des bénéficiaires lié à l'identité nationale ; identifiant unique des agents | Standard ouvert, lien possible avec le registre civil national, utilisable au point de service, déployable dans les districts |
| Échange de données | Couche nationale de médiation et d'échange conforme à OpenHIE | Standards ouverts, maintenabilité locale, compatibilité avec l'existant, fonctionnement en mode dégradé |
| Registre des formations sanitaires | Référentiel national de toutes les structures de santé | Couverture exhaustive, mise à jour décentralisée, identifiant unique par structure |
| Terminologie et codification | Référentiel national des indicateurs, des produits, terminologies et classifications | Harmonisation nationale, stabilité des définitions, alignement progressif sur les référentiels internationaux |
| Analyse et visualisation | Entrepôt national de données, tableaux de bord multi-niveaux, mécanismes analyse et redevabilité | Alimentation multi-sources, accès adapté à chaque niveau, données traçables et utilisables |
| Confiance et sécurité | Cadre de cybersécurité, gouvernance des données personnelles de santé, accès, traçabilité, consentement | Conformité au cadre juridique national, mise en œuvre réaliste, compétences locales disponibles |

Le présent cadre définit le rôle, la justification et les exigences auxquelles ces composantes doivent répondre. Les choix d'implémentation technique relèvent de l'Architecture de Référence Technique.

## Liens

- [Capabilités](./index.md)
- [Runway](./runway.md)
- [Données](../04_data/index.md)