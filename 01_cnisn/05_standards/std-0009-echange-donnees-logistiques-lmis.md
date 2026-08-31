---
title: "STD-0009 : Norme d'échange des données logistiques (LMIS)"
id: std-0009
domain: 05_standards
version: "1.0.0"
status: active
last_reviewed: 2026-08-27
owner: Comité National d'Architecture Santé Numérique
tags: ["standards", "interoperabilite", "logistique", "lmis", "supply-chain", "obligatoire"]
related: ["Lot L4", "PT-17"]
---

# STD-0009 : Norme d'échange des données logistiques (LMIS)

## Pour qui lire ce document

**Niveau :** niveau 2 : Cadre National d'Interopérabilité de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ● |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

- **Type** : norme (obligatoire)
- **Statut** : approuvé
- **ADR de référence** : ADR-0003
- **Date d'entrée en vigueur** : 2026-08-27

## Contexte

La continuité de la chaîne d'approvisionnement (médicaments, vaccins, intrants, équipements) conditionne l'exécution des soins. Les systèmes LMIS existants fragmentent les données (tableurs, portails propriétaires, formats variés), ce qui retarde les réapprovisionnements et masque les ruptures. L'OMS recommande une traçabilité de bout en bout des mouvements de stock, adossée à un catalogue produit et à une codification internationale (GS1).

## Énoncé

Toute solution numérique échangeant des données logistiques dans le secteur santé de Madagascar **doit** :

1. **Coder les produits selon GS1** (GTIN pour l'article, SSCC pour les unités logistiques, lots et dates de péremption) ;
2. **Utiliser HL7 FHIR R4** pour les ressources `Medication`, `MedicationKnowledge`, `SupplyDelivery`, `SupplyRequest` et `InventoryReport` (profilées selon l'ARTSN) ;
3. **Véhiculer les flux via l'échange interinstitutionnel X-Road** (STD-0003, ADR-0001) en mode asynchrone ;
4. **Événementiser chaque mouvement** (réception, transfert, dispensation, destruction) comme événement immuable, horodaté, lié au lot et au lieu, réconcilié à somme nulle (Entrées − Sorties = Solde) selon ART-10 ;
5. **Exposer les niveaux de stock et les alertes de rupture** selon un contrat de service partagé.

## Champ d'application

Cette norme s'applique à :

- Tous les systèmes LMIS (central, district, région, point de service) ;
- Tous les échanges catalogue produit / stock / mouvement avec le Ministère et les partenaires ;
- Tous les profils PTISN d'interopérabilité logistique ;
- Toutes les solutions soumises à homologation dans le domaine de la chaîne d'approvisionnement.

## Références au cadre

- **CNISN** : CAP-INT-15 (échange et traçabilité de la chaîne d'approvisionnement sanitaire)
- **ARTSN** : ART-10 (logistique, traçabilité de bout en bout), ART-7 (résidence & sécurité), ART-9 (garanties transactionnelles)
- **ARTSN — lots consommateurs** : [L4 — Analytique & pilotage](../../02_artsn/07_lots/index.md)
- **PTISN** : [PT-17: Logistique & chaîne d'approvisionnement (LMIS)](../../03_ptisn/03_profils/pt-17-logistique-lmis.md)
- **Standards internationaux** : HL7 FHIR R4, GS1 (GTIN/SSCC), OpenLMIS, mCSD (lieux)

## Contrôle et conformité

Lors de l'homologation, le Comité National vérifiera :

| Critère | Vérification |
|---------|--------------|
| Codification produit | Articles codés GTIN ; unités logistiques SSCC |
| Format d'échange | Ressources FHIR R4 (`Medication`, `SupplyDelivery`, `InventoryReport`) |
| Transport | Flux véhiculés par X-Road (STD-0003) |
| Traçabilité | Chaque mouvement est un événement immuable, lié au lot, réconcilié (E−S=Solde) |
| Alertes | Niveaux de stock et alertes de rupture exposés |

## Dérogations

Les dérogations sont possibles pour les LMIS legacy en phase de migration (batch CSV via médiation obligatoire). Toute dérogation doit être justifiée et approuvée par le Comité National.

## Références

- Normes et standards
- ADR-0001 : Échange interinstitutionnel X-Road
- ADR-0003 : Utilisation de HL7 FHIR
- ARTSN : ART-10 (Logistique), ART-7 (Résidence)
- CNISN : CAP-INT-15 (Chaîne d'approvisionnement sanitaire)

- **matrice de lecture** : Matrice de lecture du CNISN (niveau 2) (`01_cnisn/reading-matrix.md`)
