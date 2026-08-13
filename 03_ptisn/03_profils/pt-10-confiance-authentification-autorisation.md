---
title: PT-10 — Profil technique national
id: ptisn-pt-10-confiance-authentification-autorisation
domain: 03_ptisn
version: "0.4"
status: draft
last_reviewed: 2026-07-31
owner: Équipes techniques des initiatives
tags: ["ptisn", "niveau-4", "profils", "pt-10"]
---

# PT-10 — Profil technique national

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py — ne pas éditer à la main -->

## 1. Capacité CNISN

**CAP-INT-08 — Confiance, sécurité et autorisation**

## 2. Chapitres ART applicables

- ART-0 ;
- ART-4b ;
- ART-7 ;
- ART-9 lorsque applicable.

## 3. Services nationaux

- fournisseur d’identité sectoriel ou fédéré ;
- authentification des utilisateurs ;
- identité des systèmes ;
- service d’autorisation ;
- gestion des politiques ;
- gestion des comptes techniques ;
- fédération avec les identités pangouvernementales ;
- gestion des certificats et secrets.

## 4. Profils recommandés

| Besoin | Profil ou standard |
|----|----|
| Autorisation des API REST/FHIR | OAuth 2.0 / OpenID Connect selon le contexte |
| Profil IHE d’autorisation REST | IHE IUA |
| Authentification des nœuds et audit | IHE ATNA lorsque applicable |
| Confiance interinstitutionnelle | Mécanismes de la plateforme nationale d’échange |
| Authentification renforcée | Profil national à définir |
| Autorisation par attributs | Politique ABAC nationale à définir |

IHE IUA fournit un cadre d’autorisation fondé sur des jetons pour les services HTTP REST, notamment FHIR. ATNA porte des exigences relatives à l’authentification des nœuds et à l’audit des événements de sécurité.

## 5. Principe de séparation

Authentification
    Qui est l’utilisateur ou le système ?
                 │
                 ▼
    Contexte professionnel
    Quelle est sa fonction et son affectation ?
                 │
                 ▼
    Base d’autorisation
    Pourquoi l’accès est-il permis ?
                 │
                 ▼
    Décision d’autorisation
    Quelles actions sont autorisées ?

## 6. Exigences minimales

- moindre privilège ;
- authentification adaptée au risque ;
- séparation des comptes utilisateurs et techniques ;
- révocation ;
- rotation des secrets ;
- contrôle territorial ;
- contrôle programmatique ;
- journalisation ;
- durée limitée des jetons ;
- vérification du contexte professionnel ;
- décision explicite.

------------------------------------------------------------------------

*Rattachement : [CMP-15](../../referentiel/composants/cmp-15.md), [CAP-INT-08](../../referentiel/capacites/cap-int-08.md), [ART-0](../../referentiel/chapitres/art-0.md), [ART-4B](../../referentiel/chapitres/art-4b.md), [ART-7](../../referentiel/chapitres/art-7.md), [ART-9](../../referentiel/chapitres/art-9.md) · [fiche](../../referentiel/profils/pt-10.md)*

<!-- END:GENERATED -->
