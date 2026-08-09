---
title: Référentiels nationaux
id: data-referentials
domain: 04_data
version: "0.0.1"
status: draft
last_reviewed: 2026-07-03
owner: Cellule du Système d'Information Sanitaire
tags: [données, référentiels, normes]
---

# Référentiels nationaux

## Pour qui lire ce document

**Niveau :** niveau 1 — Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ○ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../reading-matrix.md).

Les référentiels nationaux sont les socles communs qui permettent à tous les systèmes d'information de parler le même langage : identifier les mêmes structures, personnes, produits, zones géographiques, indicateurs et bénéficiaires.

Ils constituent des **biens communs nationaux**. Ils ne doivent pas être fragmentés, dupliqués ou remplacés par des référentiels propriétaires de programmes, de projets ou de partenaires.

| Référentiel | Rôle dans le système | Composante DPI-H | Capabilités soutenues |
|-------------|----------------------|------------------|-----------------------|
| Référentiel des formations sanitaires | Identifier de manière unique toutes les structures de santé (publics, privés, confessionnels, communautaires) | Registre des formations sanitaires | CAP-01, 05, 10, 13, 14 |
| Référentiel géographique sanitaire | Harmoniser régions, districts, communes, fokontany, bassins de couverture | Registre / géographie sanitaire | CAP-05, 08, 13, 14 |
| Référentiel des indicateurs sanitaires | Garantir une définition unique, stable et partagée des indicateurs | Terminologie et codification | CAP-03, 05, 08, 13 |
| Référentiel des agents de santé | Identifier les agents, rôles, affectations, qualifications, formations | Identité numérique / registre des professionnels | CAP-09, 13, 14, 15 |
| Référentiel des produits de santé | Harmoniser la désignation, la codification et le suivi des médicaments, vaccins, intrants | Terminologie et codification | CAP-10, 13, 14 |
| Référentiel des bénéficiaires / patients | Soutenir la continuité, la protection financière, le suivi des droits | Identité numérique | CAP-01, 02, 07, 13, 14, 15 |
| Référentiel des partenaires et initiatives | Identifier les projets, partenaires, financements, zones, bénéfices | Portefeuille d'initiatives | CAP-08, 13, 16 |

## Exigences de qualité

Chaque référentiel national doit disposer de :

- un propriétaire institutionnel ;
- un mécanisme de mise à jour ;
- un identifiant unique ;
- une règle de qualité ;
- un processus de validation ;
- un mécanisme d'accès par les systèmes autorisés ;
- un historique des modifications ;
- un plan de soutenabilité.

## Liens

- [Domaines de données](./domains.md)
- [Composants DPI-H](../03_capabilities/digital.md)
- [Architecture applicative](../05_application/index.md)