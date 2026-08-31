---
title: "Cas d'usage : Chaîne d'approvisionnement sanitaire (supply chain)"
id: ptisn-cas-usage-supply-chain
domain: 08_annexes
version: "1.0.0"
status: draft
last_reviewed: 2026-08-27
owner: DEPSI
tags: ["ptisn", "niveau-4", "cas-usage", "logistique", "lmis", "supply-chain", "VS-01", "VS-02"]
---

# Cas d'usage : Chaîne d'approvisionnement sanitaire (VS-01 / VS-02)

## Pour qui lire ce document

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| Partenaires techniques et financiers | ◐ |

## Objectif

Ce document montre comment les **profils et normes d'interopérabilité supply chain** composent pour garantir la disponibilité des médicaments, vaccins et intrants du centre d'achat jusqu'au point de service, et déclencher la riposte en cas de rupture. Il s'appuie sur `CAP-INT-15` (capacité CNISN), `ART-10` (traçabilité de bout en bout) et `STD-0009` (norme d'échange).

## Principe architectural

La supply chain est un **cas d'usage métier** qui consomme le profil d'échange LMIS (`PT-17`), le composant LMIS (`CMP-23`) et la norme `STD-0009`. Chaque mouvement est un événement immuable, codé GS1, réconcilié à somme nulle.

```
┌─────────────────────────────────────────────────────────────────────┐
│              CHAÎNE D'APPROVISIONNEMENT (VS-01 / VS-02)              │
│  Prévision → Réception → Stock → Dispensation → Alerte → Riposte   │
└──────┬──────────┬──────────┬──────────┬──────────┬─────────────────┘
       │          │          │          │          │
       ▼          ▼          ▼          ▼          ▼
┌─────────────────────────────────────────────────────────────────────┐
│                 PROFILS / NORMES TECHNIQUES                         │
│  PT-17   │  STD-0009 │  PT-09   │  PT-12   │  PT-13   │  ART-10   │
└─────────────────────────────────────────────────────────────────────┘
```

## Phase 1 : Prévision et réapprovisionnement

À partir des données d'activité clinique (`CMP-19`), le LMIS (`CMP-23`) calcule les besoins et les seuils de sécurité par structure. La centrale d'achat émet un `SupplyRequest` FHIR normalisé (STD-0009).

## Phase 2 : Réception et traçabilité par lot

À la réception, chaque mouvement est événementisé de façon immuable : article codé GTIN, lot, date de péremption, quantité. Le `SupplyDelivery` FHIR est transmis via X-Road (STD-0003). La réconciliation (Entrées − Sorties = Solde) est vérifiée.

## Phase 3 : Dispensation et stock au point de service

Le point de service dispense et met à jour son stock en temps réel ; l'`InventoryReport` FHIR remonte le niveau de stock. Cela alimente la disponibilité des intrants pour les soins (VS-01) et la qualité (O3).

## Phase 4 : Alerte de rupture et riposte

Lorsqu'un seuil de sécurité est franchi, le LMIS émet une alerte de rupture. En riposte épidémique (VS-02), les flux sont réorientés vers les zones touchées (PRC-05).

| Profil / Norme | Rôle |
|----------------|------|
| **PT-17** | Profil LMIS & chaîne d'approvisionnement (gestion métier + échange interopérable catalogue/stock/mouvement, STD-0009) |
| **STD-0009** | Norme d'échange des données logistiques (FHIR + GS1 + X-Road) |
| **PT-09** | Analytique et exposition des données de stock |
| **PT-12** | Audit et traçabilité des mouvements |
| **ART-10** | Discipline de traçabilité de bout en bout |
| **CAP-INT-15** | Capacité CNISN de la chaîne d'approvisionnement |

## Liens

- Norme : [STD-0009 : échange des données logistiques (LMIS)](../../01_cnisn/05_standards/std-0009-echange-donnees-logistiques-lmis.md)
- Profil : [PT-17 : Logistique & chaîne d'approvisionnement (LMIS)](../03_profils/pt-17-logistique-lmis.md)
- Capacité : [CAP-INT-15 : chaîne d'approvisionnement sanitaire](../../referentiel/capacites/cap-int-15.md)
- Chapitre : [ART-10 : Logistique](../../referentiel/chapitres/art-10.md)
- Composant : [CMP-23 : Chaîne logistique (LMIS)](../../referentiel/composants/cmp-23.md)
