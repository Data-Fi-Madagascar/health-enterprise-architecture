---
title: Profil technique national
id: ptisn-PT-12
domain: 03_ptisn
version: "1.0.0"
status: draft
last_reviewed: 2026-07-31
owner: Équipes techniques des initiatives
tags: ["ptisn", "niveau-4", "profils", "PT-12"]
---

# Profil technique national

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

## 1. Capacité CNISN

[CAP-INT-10: Provenance, audit et traçabilité](../../referentiel/capacites/cap-int-10.md)

## 2. Chapitres ART applicables

- F.1 ;
- F.5 ;
- F.6 ;
- [ART-3: Historisation événementielle et profils de déploiement](../../referentiel/chapitres/art-3.md) ;
- [ART-7: Sécurité, contrôle d'accès et résidence de la donnée](../../referentiel/chapitres/art-7.md).

## 3. Services distincts

Le PTISN distingue quatre services.

### Journal des événements métier

Conserve les changements fonctionnels.

### Service de provenance

Explique :

- l’origine ;
- l’acteur ;
- la transformation ;
- les ressources sources ;
- les ressources produites.

### Service d’audit de sécurité

Conserve :

- consultations ;
- exports ;
- authentifications ;
- décisions d’autorisation ;
- opérations administratives ;
- modifications sensibles.

### Observabilité technique

Conserve :

- logs ;
- métriques ;
- traces ;
- erreurs ;
- performances.

## 4. Standards recommandés

| Besoin                    | Standard                                        |
|---------------------------|-------------------------------------------------|
| Audit de sécurité santé   | HL7 FHIR AuditEvent lorsque FHIR est applicable |
| Provenance des ressources | HL7 FHIR Provenance                             |
| Audit IHE                 | ATNA et profils d’audit associés                |
| Corrélation technique     | Identifiant de corrélation propagé              |
| Logs et métriques         | Standards ouverts d’observabilité à définir     |

FHIR `AuditEvent` permet de représenter des activités ayant une portée d’audit, tandis que `Provenance` décrit le « qui, quoi et quand » associé à la création ou à la transformation de ressources. Ces usages ne doivent pas être confondus avec les événements métier.

## 5. Règles

Les quatre catégories peuvent être corrélées mais peuvent utiliser :

- des formats différents ;
- des stockages différents ;
- des durées différentes ;
- des droits différents ;
- des politiques différentes.

Un journal technique ne doit pas être utilisé comme seul mécanisme de preuve métier.

------------------------------------------------------------------------

*Rattachement : CMP-17, CAP-INT-10, F-1, F-5, F-6, ART-3, ART-7 · fiche PT-12*

<!-- END:GENERATED -->
