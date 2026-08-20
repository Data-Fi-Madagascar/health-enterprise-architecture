---
title: Annexe B : Glossaire des patterns cités
id: artsn-annexe-b-glossaire-patterns
domain: 02_artsn
version: "1.0.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, annexes, glossaire, patterns, niveau-3]
---

# Annexe B : Glossaire des patterns cités

## Pour qui lire ce document

**Niveau :** niveau 3 : Architecture de Référence Technique de la Santé Numérique.

La lecture de ce document est **ponctuelle** pour les décideurs institutionnels, **complémentaire** pour les directions métier et programmes ainsi que pour les partenaires techniques et financiers, et **prioritaire** pour l'équipe DEPSI et ses équipes techniques ainsi que pour les équipes SIS, données et suivi-évaluation. Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

Définitions des patterns techniques mobilisés par les chapitres de l'ARTSN.

## Event sourcing (historisation événementielle)

Pattern dans lequel l'état d'un système n'est jamais stocké directement : seule la **séquence complète des événements** qui l'ont produit est conservée, l'état étant une projection reconstructible de cette séquence. Mobilisé par ART-3 et F.1.

## CQRS (Command Query Responsibility Segregation)

Séparation du modèle utilisé pour écrire des données (commandes) et du modèle utilisé pour les lire (requêtes), permettant à chacun d'être optimisé et mis à l'échelle indépendamment. Mobilisé par ART-6.

## Idempotence

Propriété garantissant qu'une même opération, répétée plusieurs fois, produit exactement le même effet qu'une seule exécution : condition nécessaire pour absorber sans risque une livraison « au moins une fois ». Mobilisée par ART-1.

## Pattern médiateur

Composant qui absorbe l'hétérogénéité des systèmes sources et expose une interface canonique unique en aval, sans que les sources aient à se connaître entre elles ; popularisé par l'architecture OpenHIE (*Health Information Mediator*). Mobilisé par ART-2.

## Saga / process manager

Pattern d'orchestration d'un processus métier borné traversant plusieurs agrégats, sans les fusionner en un seul. Mobilisé par ART-8a.

## Chorégraphie

Style de coordination où chaque partie réagit de façon autonome à des événements partagés, sans composant central ayant autorité sur l'ensemble du processus. Mobilisé par ART-8d.

## SCD (Slowly Changing Dimension) type 2

Technique de modélisation de données consistant à conserver l'historique complet des versions successives d'une métadonnée, chacune associée à sa période de validité. Mobilisée par ART-4 et ART-4c.

## Golden record

Enregistrement pivot résultant d'un rapprochement probabiliste entre plusieurs représentations potentiellement divergentes d'une même entité (typiquement une identité individuelle). Mobilisé par ART-4a.

## Netting

Technique de compensation globale consistant à regrouper des micro-agrégats individuels en un seul agrégat consolidé de niveau supérieur. Mobilisée par ART-8c.

## Publication / Abonnement (Pub/Sub)

Modèle de messagerie décentralisée où les consommateurs s'abonnent de manière autonome à des files d'événements publics, sans autorité centrale. Mobilisé par ART-8d.

## Liens

Les liens utiles pour approfondir ce document sont les suivants : les chapitres et patterns de référence sont disponibles dans l'index des Chapitres et patterns de référence, et le dictionnaire de données fonctionnelles est consultable dans la section Dictionnaire de données fonctionnelles.

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **ART-3** : Historisation événementielle et profils de déploiement (`referentiel/chapitres/art-3.md`)
- **F.1** : F.1 : Résilience face à la réalité géographique du pays (`referentiel/fondations/f-1.md`)
- **ART-6** : Analytique et restitution (`referentiel/chapitres/art-6.md`)
- **ART-1** : Intégration et ingestion (`referentiel/chapitres/art-1.md`)
- **ART-2** : Médiation et normalisation (`referentiel/chapitres/art-2.md`)
- **ART-8a** : Orchestration de processus borné (`referentiel/chapitres/art-8a.md`)
- **ART-8d** : Chorégraphie inter-institutionnelle (`referentiel/chapitres/art-8d.md`)
- **ART-4** : Référentiels de métadonnées de gestion (`referentiel/chapitres/art-4.md`)
- **ART-4c** : Éligibilité et couverture (`referentiel/chapitres/art-4c.md`)
- **ART-4a** : Résolution d'identité (`referentiel/chapitres/art-4a.md`)
- **ART-8c** : Agrégation par lot (`referentiel/chapitres/art-8c.md`)
- **Chapitres et patterns de référence** : Chapitres et patterns de référence (`02_artsn/03_chapitres/index.md`)
- **Dictionnaire de données fonctionnelles** : Dictionnaire de données fonctionnelles (`02_artsn/05_dictionnaire/index.md`)
