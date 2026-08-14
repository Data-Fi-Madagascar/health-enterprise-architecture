---
title: Annexe B — Glossaire des patterns cités
id: artsn-annexe-b-glossaire-patterns
domain: 02_artsn
version: "0.0.1"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, annexes, glossaire, patterns, niveau-3]
---

# Annexe B — Glossaire des patterns cités

## Pour qui lire ce document

**Niveau :** niveau 3 — Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ○ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../reading-matrix.md).

Définitions des patterns techniques mobilisés par les chapitres de l'ARTSN.

## Event sourcing (historisation événementielle)

Pattern dans lequel l'état d'un système n'est jamais stocké directement : seule la **séquence complète des événements** qui l'ont produit est conservée, l'état étant une projection reconstructible de cette séquence. Mobilisé par [ART-3](../../referentiel/chapitres/art-3.md) et [F.1](../../referentiel/fondations/f-1.md).

## CQRS (Command Query Responsibility Segregation)

Séparation du modèle utilisé pour écrire des données (commandes) et du modèle utilisé pour les lire (requêtes), permettant à chacun d'être optimisé et mis à l'échelle indépendamment. Mobilisé par [ART-6](../../referentiel/chapitres/art-6.md).

## Idempotence

Propriété garantissant qu'une même opération, répétée plusieurs fois, produit exactement le même effet qu'une seule exécution — condition nécessaire pour absorber sans risque une livraison « au moins une fois ». Mobilisée par [ART-1](../../referentiel/chapitres/art-1.md).

## Pattern médiateur

Composant qui absorbe l'hétérogénéité des systèmes sources et expose une interface canonique unique en aval, sans que les sources aient à se connaître entre elles ; popularisé par l'architecture OpenHIE (*Health Information Mediator*). Mobilisé par [ART-2](../../referentiel/chapitres/art-2.md).

## Saga / process manager

Pattern d'orchestration d'un processus métier borné traversant plusieurs agrégats, sans les fusionner en un seul. Mobilisé par [ART-8a](../../referentiel/chapitres/art-8a.md).

## Chorégraphie

Style de coordination où chaque partie réagit de façon autonome à des événements partagés, sans composant central ayant autorité sur l'ensemble du processus. Mobilisé par [ART-8d](../../referentiel/chapitres/art-8d.md).

## SCD (Slowly Changing Dimension) type 2

Technique de modélisation de données consistant à conserver l'historique complet des versions successives d'une métadonnée, chacune associée à sa période de validité. Mobilisée par [ART-4](../../referentiel/chapitres/art-4.md) et [ART-4c](../../referentiel/chapitres/art-4c.md).

## Golden record

Enregistrement pivot résultant d'un rapprochement probabiliste entre plusieurs représentations potentiellement divergentes d'une même entité (typiquement une identité individuelle). Mobilisé par [ART-4a](../../referentiel/chapitres/art-4a.md).

## Netting

Technique de compensation globale consistant à regrouper des micro-agrégats individuels en un seul agrégat consolidé de niveau supérieur. Mobilisée par [ART-8c](../../referentiel/chapitres/art-8c.md).

## Publication / Abonnement (Pub/Sub)

Modèle de messagerie décentralisée où les consommateurs s'abonnent de manière autonome à des files d'événements publics, sans autorité centrale. Mobilisé par [ART-8d](../../referentiel/chapitres/art-8d.md).

## Liens

- [Chapitres et patterns de référence](../03_chapitres/index.md)
- [Dictionnaire de données fonctionnelles](../05_dictionnaire/index.md)
