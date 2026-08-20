---
title: PT-01 : Profil technique national
id: ptisn-PT-01-echange-interinstitutionnel
domain: 03_ptisn
version: "1.0.0"
status: draft
last_reviewed: 2026-07-31
owner: Équipes techniques des initiatives
tags: ["ptisn", "niveau-4", "profils", "PT-01"]
---

# PT-01 : Profil technique national

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

## 1. Capacité CNISN

[CAP-INT-03: Échange et médiation inter-systèmes](../../referentiel/capacites/cap-int-03.md)

## 2. Chapitres ART applicables

- [ART-0: accords de partage](../../referentiel/chapitres/art-0.md)partage ;
- [ART-1: intégration et ingestion](../../referentiel/chapitres/art-1.md)gestion ;
- [ART-7: sécurité et résidence](../../referentiel/chapitres/art-7.md)sidence ;
- [ART-11: coordination intersectorielle.](../../referentiel/chapitres/art-11.md)orielle.

## 3. Service national

**Service national d’échange interinstitutionnel**

Ce service permet les échanges entre le secteur santé et :

- l’état civil ;
- le registre de la population ;
- la protection sociale ;
- les finances publiques ;
- l’éducation ;
- les collectivités territoriales ;
- les autres autorités publiques ;
- les partenaires autorisés.

## 4. Implémentation nationale

| Élément | Décision |
|----|----|
| Plateforme | X-Road |
| Portée | Interinstitutionnelle |
| Point de raccordement santé | Serveur de sécurité sectoriel ou dispositif équivalent prévu par le CNI |
| Autorité de gouvernance | Instance nationale compétente, en coordination avec l’UGD |
| Statut | Retenu par le cadre national d’interopérabilité |
| Usage interne au secteur santé | Non obligatoire par défaut |

X-Road permet l’échange sécurisé entre organisations membres au moyen de serveurs de sécurité et d’une infrastructure de confiance commune. Il ne constitue pas, à lui seul, un service de normalisation sémantique de santé.

## 5. Contrats requis

Toute initiative utilisant ce service doit fournir :

- un accord de partage ;
- un fournisseur de service identifié ;
- un consommateur identifié ;
- une description de service ;
- un contrat de données ;
- une politique d’accès ;
- une politique de résidence ;
- une preuve de conformité au CNI ;
- une procédure de gestion des incidents.

## 6. Limites

Le service national d’échange ne remplace pas :

- la résolution d’identité patient ;
- le registre des professionnels ;
- le consentement ;
- la terminologie ;
- l’autorisation fonctionnelle ;
- la transformation sémantique ;
- l’orchestration métier.

------------------------------------------------------------------------

*Rattachement : CMP-06, CAP-INT-03, ART-0, ART-1, ART-7, ART-11 · fiche PT-01*

<!-- END:GENERATED -->
