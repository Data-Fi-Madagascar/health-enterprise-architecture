---
title: PT-03 — Profil technique national
id: ptisn-pt-03-catalogue-services-registre-contrats
domain: 03_ptisn
version: "0.4"
status: draft
last_reviewed: 2026-07-31
owner: Équipes techniques des initiatives
tags: ["ptisn", "niveau-4", "profils", "pt-03"]
---

# PT-03 — Profil technique national


## 1. Capacité CNISN

**CAP-INT-03 — Échange et médiation inter-systèmes**

## 2. Chapitres ART applicables

- F.3 — versionnement ;
- F.4 — rattachement aux capacités ;
- ART-1 — interfaces ;
- ART-2 — contrats canoniques.

## 3. Services nationaux

Deux services distincts sont requis.

### Catalogue national des services

Répertorie :

- les services exposés ;
- les propriétaires ;
- les consommateurs autorisés ;
- les environnements ;
- les niveaux de service ;
- les points d’accès ;
- les politiques de sécurité.

### Registre national des contrats

Répertorie :

- les schémas ;
- les profils ;
- les API ;
- les événements ;
- les versions ;
- les extensions ;
- les règles de compatibilité ;
- les dépréciations.

## 4. Formats recommandés

| Type de contrat      | Format recommandé                      |
|----------------------|----------------------------------------|
| API REST générale    | OpenAPI                                |
| Ressource de santé   | Profil HL7 FHIR                        |
| Guide national FHIR  | Implementation Guide publié            |
| Événement non-FHIR   | JSON Schema                            |
| Interface asynchrone | AsyncAPI ou contrat équivalent         |
| Terminologie         | CodeSystem, ValueSet, ConceptMap       |
| Exemples et tests    | Ressources et jeux de tests versionnés |

## 5. Produit

Aucun produit national n’est encore retenu.

**Statut : à instruire.**

## 6. Preuves de conformité

- contrat publié ;
- version explicite ;
- propriétaire ;
- test de validation ;
- politique de compatibilité ;
- calendrier de dépréciation.

------------------------------------------------------------------------
