---
title: Logistique & chaîne d'approvisionnement (LMIS)
id: ptisn-PT-17
domain: 03_profils
version: "1.0.0"
status: candidate
last_reviewed: 2026-08-24
owner: DEPSI
tags: ["ptisn", "niveau-4", "profils", "PT-17"]
related: ["CAP-INT-10", "ART-10", "CMP-23"]
---

# Logistique & chaîne d'approvisionnement (LMIS)

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

## 1. Objet et périmètre

Le **profil PT-17 — Logistique & chaîne d’approvisionnement (LMIS)** définit le registre logistique et la traçabilité des stocks (médicaments, vaccins, intrants, équipements). Il assure la continuité de la chaîne d’approvisionnement par une traçabilité de bout en bout et un échange interopérable entre LMIS et partenaires.

Périmètre : mouvements de stock (livraison, dispensation, transfert, destruction), catalogue produit partagé, alertes de rupture/péremption. Norme de référence : [STD-0009: échange des données logistiques (LMIS)](../../01_cnisn/05_standards/std-0009-echange-donnees-logistiques-lmis.md).

## 2. Capacité CNISN

- [CAP-INT-10: Provenance, audit et traçabilité](../../referentiel/capacites/cap-int-10.md)
- [CAP-INT-15: Échange et traçabilité de la chaîne d'approvisionnement sanitaire](../../referentiel/capacites/cap-int-15.md)

## 3. Chapitres ART applicables

- [ART-10: Logistique](../../referentiel/chapitres/art-10.md) — traçabilité de bout en bout des mouvements de stock ;
- [ART-9: Garanties transactionnelles fortes](../../referentiel/chapitres/art-9.md) — intégrité et non-répudiation des échanges de mouvements ;
- [ART-7: Résidence, contrôle d'accès et sécurité de la donnée](../../referentiel/chapitres/art-7.md) — hébergement souverain et contrôle d'accès aux données logistiques ;
- [STD-0009: échange des données logistiques (LMIS)](../../01_cnisn/05_standards/std-0009-echange-donnees-logistiques-lmis.md).

## 4. Acteurs (Actors)

- **LMIS (central / district / région / point de service)** — tient le registre logistique, évidence les mouvements et remonte les niveaux de stock.
- **Partenaire logistique** — système externe consommant/produisant des flux logistiques interopérables.
- **Annuaire de sites (mCSD)** — fournit les lieux des mouvements (référence PT-06).

*Référence — capacité CNISN mise en œuvre : [CAP-INT-10](../../referentiel/capacites/cap-int-10.md).
## 5. Transactions

| Transaction | Acteurs | R/O | Standard |
|----|----|----|----|
| T1 — Remontée de niveaux de stock | LMIS → Référentiel | R | FHIR `InventoryReport` (R4) |
| T2 — Mouvement de stock | LMIS → LMIS/Partenaire | R | FHIR `SupplyDelivery` / `SupplyRequest` (R4) |
| T3 — Alerte rupture / péremption | LMIS → Niveaux pertinents | R | Événement d’alerte |
| T4 — Échange interopérable | LMIS ↔ Partenaire | R | X-Road (STD-0003, ADR-0001) — STD-0009 |

R = requis ; O = optionnel (à définir si le dépôt ne précise pas).

*Référence — capacité CNISN mise en œuvre : [CAP-INT-10](../../referentiel/capacites/cap-int-10.md).
## 6. Content Modules

- **FHIR `Medication` / `MedicationKnowledge`** : catalogue produit (codification GS1 GTIN).
- **FHIR `InventoryReport`** : niveaux de stock par établissement.
- **FHIR `SupplyDelivery` / `SupplyRequest`** : mouvements (réception, transfert, dispensation, destruction), liés au lot et au lieu.
- **Alerte** : rupture et péremption diffusées aux niveaux pertinents.

## 7. Options

- **O1 — Interfaces** : HL7 FHIR et/ou DHIS2 selon le système opérationnel.
- **O2 — Transport** : X-Road (STD-0003, ADR-0001) pour l’échange interopérable.
- **O3 — Unité logistique** : codification SSCC en complément du GTIN article.

## 8. Service national

**Registre logistique et traçabilité des stocks (LMIS)**

Ce service assure la continuité de la chaîne d'approvisionnement : chaque mouvement (livraison, dispensation, transfert, destruction) est un événement immuable, horodaté, adossé aux référentiels de produits, et réconcilié selon les règles comptables de conservation de quantité (Entrées − Sorties = Solde).

Il expose en outre un **profil d'échange logistique interopérable** entre LMIS (central, district, région, point de service) et partenaires, conformément à la norme [STD-0009](../../01_cnisn/05_standards/std-0009-echange-donnees-logistiques-lmis.md), véhiculé par X-Road (STD-0003, ADR-0001).

### Catalogue produit partagé

- codification GS1 (GTIN article, SSCC unité logistique) ;
- désignation, unité, seuils de sécurité par type d'intrant et de structure.

### Stock et mouvements

- remontée des niveaux de stock par établissement (`InventoryReport`) ;
- événementisation de chaque mouvement (réception, transfert, dispensation, destruction) comme événement immuable, lié au lot et au lieu ;
- réconciliation à somme nulle (Entrées − Sorties = Solde).

### Alertes

- alerte de rupture et de péremption diffusée aux niveaux pertinents.

## 9. Formats et standards recommandés

| Type d'échange | Format recommandé |
|----------------|-------------------|
| Produit | GS1 GTIN + FHIR `Medication` / `MedicationKnowledge` |
| Stock | FHIR `InventoryReport` (R4) |
| Mouvement | FHIR `SupplyDelivery` / `SupplyRequest` (R4) |
| Transport | X-Road (STD-0003, ADR-0001) |
| Lieux | mCSD (annuaire de sites) |
| Terminologie | CIM-11 + LOINC (STD-0006) |

*Référence — normes et standards CNISN : [01_cnisn/05_standards](../../01_cnisn/05_standards/index.md).
## 10. Exigences

Une solution LMIS doit au minimum supporter :

- modélisation des établissements et dépôts de stock ;
- gestion des lots, péremptions et seuils ;
- traçabilité des transferts inter-établissements ;
- interfaces HL7 FHIR et/ou DHIS2 ;
- journalisation et audit des mouvements ;
- reprise et réconciliation en cas de défaillance réseau ;
- intégration avec le composant [CMP-23: Chaîne logistique (LMIS)](../../referentiel/composants/cmp-23.md).

## 11. Déclaration de conformité (Integration Statement)

- ressources FHIR profilées publiées (STD-0009) ;
- flux véhiculé par X-Road ;
- chaque mouvement est un événement immuable, réconcilié (E−S=Solde) ;
- alertes de rupture exposées.

## 12. Articulation avec les autres profils

Le profil opérationnalise le chapitre [ART-10: Logistique](../../referentiel/chapitres/art-10.md) et les capacités CNISN [CAP-INT-10: Provenance, audit et traçabilité](../../referentiel/capacites/cap-int-10.md) et [CAP-INT-15: Échange et traçabilité de la chaîne d'approvisionnement](../../referentiel/capacites/cap-int-15.md), en s'appuyant sur le composant [CMP-23: Chaîne logistique (LMIS)](../../referentiel/composants/cmp-23.md) et conformément à l'exigence [ENF-2: Intégrité des flux et traçabilité des valeurs](../../referentiel/exigences/enf-2.md). L'échange interopérable respecte la norme [STD-0009](../../01_cnisn/05_standards/std-0009-echange-donnees-logistiques-lmis.md).

## 13. Limites et dépendances

Le profil dépend des référentiels de produits (PT-05/PT-06), de la terminologie (PT-07) et du médiateur (PT-02) pour l’acheminement X-Road. Il ne définit pas le référentiel produit lui-même (codification GS1 à gouverner nationalement).

<!-- END:GENERATED -->

## Références au cadre

- **ARTSN — lots consommateurs** : [L2 — Applications terrain](../../02_artsn/07_lots/index.md), [L3 — Médiation & registres](../../02_artsn/07_lots/index.md), [L4 — Analytique & pilotage](../../02_artsn/07_lots/index.md)
