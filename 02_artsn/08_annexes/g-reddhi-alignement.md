---
title: "Annexe G : Alignement REDDHI / DPI-H et l'HEA"
id: reddhi-alignement
domain: 08_annexes
version: "1.0.0"
status: draft
last_reviewed: 2026-08-26
owner: DEPSI
tags: ["artsn", "annexes", "reddhi", "dpi-h", "alignement", "oms"]
---

# Annexe G : Alignement REDDHI / DPI-H et l'HEA

Le cadre **REDDHI** (*Resilient Essential Digital and Data Health Infrastructure*) est la formulation OMS/ITU (Global Initiative on Digital Health — GIDH) de l'infrastructure numérique de santé comme **bien commun essentiel, résilient et sous possession nationale**. Il prolonge le DPI-H ([fondements CAESN](../../00_caesn/00_overview/foundations.md)) en ajoutant l'exigence de résilience et de souveraineté pays.

Cette annexe répond à la question : *comment l'HEA (CAESN / CNISN / ARTSN) répond-elle aux principes et composantes REDDHI ?* Elle complète l'annexe F (normes CNISN consommées par les lots) en remontant à la source internationale.

## 1. Principes REDDHI → traduction HEA

| Principe REDDHI | Signification | Traduction dans l'HEA | Référence |
|-----------------|---------------|-----------------------|-----------|
| **Resilient** (résiliente) | Disponibilité, reprise, sécurité | Hébergement souverain, chiffrement, journalisation, garanties transactionnelles | [ART-7](../../referentiel/chapitres/art-7.md), [ART-9](../../referentiel/chapitres/art-9.md), [STD-0002](../../01_cnisn/05_standards/std-0002-securite-chiffrement.md), [ADR-0008](../../01_cnisn/06_decisions/adr-0008-atna.md) |
| **Essential** (essentielle) | Composantes minimales partagées = bien commun | 9 composantes DPI-H positionnées comme biens communs, déployées par les lots L1–L7 | [Feuille de route](../07_lots/index.md) |
| **Digital & Data** (données) | Données comme actif souverain | Résidence de la donnée, architecture de l'information sanitaire | [ART-7](../../referentiel/chapitres/art-7.md) (résidence), [Architecture des données CAESN](../../00_caesn/04_data/index.md) |
| **Health Infrastructure** (infrastructure partagée) | Infrastructure d'État réutilisable | Cadre national d'interopérabilité mutualisé | [CNISN](../../01_cnisn/index.md), DPI-F (identité, paiements, échange) |
| **Country-owned** (possession nationale) | Gouvernance nationale, souveraineté | CNASN, homologation, principe de souveraineté | [Gouvernance CAESN](../../00_caesn/07_governance/index.md), [PA-05](../../00_caesn/02_principles/index.md) |

## 2. Composantes REDDHI / DPI-H → chapitres ART et normes CNISN

Les 9 composantes DPI-H se traduisent directement en chapitres ART de référence et en normes/ADR du CNISN :

| Composante REDDHI / DPI-H | Fonction | Chapitre ART (HEA) | Norme / ADR CNISN |
|---------------------------|----------|--------------------|-------------------|
| Registre des bénéficiaires (Client Registry) | Identité unique du patient | [ART-4A](../../referentiel/chapitres/art-4a.md) (Résolution d'identité) | [STD-0005](../../01_cnisn/05_standards/std-0005-identite-pixm.md), [ADR-0004](../../01_cnisn/06_decisions/adr-0004-identite.md), [ADR-0006](../../01_cnisn/06_decisions/adr-0006-inp.md) |
| Registre des formations sanitaires (Facility Registry) | Identité des lieux de soins | [ART-4](../../referentiel/chapitres/art-4.md) (Référentiels) | [STD-0001](../../01_cnisn/05_standards/std-0001-interopabilite-fhir.md) |
| Registre des professionnels de santé (Health Worker Registry) | Identité des prestataires | [ART-4](../../referentiel/chapitres/art-4.md) (Référentiels) | [STD-0001](../../01_cnisn/05_standards/std-0001-interopabilite-fhir.md) |
| Couche d'échange (Interoperability Layer) | Routage et transformation des messages | [ART-2](../../referentiel/chapitres/art-2.md) (Médiation), [ART-3](../../referentiel/chapitres/art-3.md) (Historisation) | [STD-0003](../../01_cnisn/05_standards/std-0003-x-road.md), [ADR-0001](../../01_cnisn/06_decisions/adr-0001-x-road.md), [STD-0001](../../01_cnisn/05_standards/std-0001-interopabilite-fhir.md) |
| Service de terminologie | Codes et classifications communs | [ART-4](../../referentiel/chapitres/art-4.md) (Référentiels) | [STD-0006](../../01_cnisn/05_standards/std-0006-terminologie.md), [STD-0007](../../01_cnisn/05_standards/std-0007-snomed-ct.md) |
| Dossier partagé (Shared Health Record) | Repository longitudinal patient | [ART-1](../../referentiel/chapitres/art-1.md) (Intégration), [ART-3](../../referentiel/chapitres/art-3.md) (Historisation) | [STD-0001](../../01_cnisn/05_standards/std-0001-interopabilite-fhir.md), [STD-0005](../../01_cnisn/05_standards/std-0005-identite-pixm.md) |
| Système d'information sanitaire (HMIS) | Données agrégées et tableaux de bord | [ART-6](../../referentiel/chapitres/art-6.md) (Analytique) | [STD-0004](../../01_cnisn/05_standards/std-0004-madx.md), [ADR-0003](../../01_cnisn/06_decisions/adr-0003-fhir.md) |
| Gestion logistique (LMIS) | Visibilité sur les produits de santé | [ART-10](../../referentiel/chapitres/art-10.md) (Logistique) | [STD-0001](../../01_cnisn/05_standards/std-0001-interopabilite-fhir.md) |
| Cadre de confiance-sécurité | Authentification, autorisation, journalisation | [ART-7](../../referentiel/chapitres/art-7.md) (Sécurité), [ART-4B](../../referentiel/chapitres/art-4b.md) (Bases d'autorisation) | [STD-0002](../../01_cnisn/05_standards/std-0002-securite-chiffrement.md), [ADR-0008](../../01_cnisn/06_decisions/adr-0008-atna.md), [ADR-0005](../../01_cnisn/06_decisions/adr-0005-consentement.md) |

## 3. Articulation : comment l'HEA répond à REDDHI

L'HEA ne « copie » pas REDDHI ; elle l'opérationnalise à trois niveaux cohérents :

1. **Niveau stratégique (CAESN).** Les principes REDDHI (résilience, essence, possession nationale) sont repris par les principes d'architecture (notamment PA-05 souveraineté, PA-06 confiance) et par la gouvernance sous la tutelle du CNASN. La résidence de la donnée ([ART-7](../../referentiel/chapitres/art-7.md)) traduit l'exigence « données comme actif souverain ».

2. **Niveau d'interopérabilité (CNISN).** Les 9 composantes DPI-H sont couvertes par les normes et ADR du CNISN (colonne de droite du tableau §2). La couche d'échange s'appuie sur X-Road ([ADR-0001](../../01_cnisn/06_decisions/adr-0001-x-road.md)), l'identité sur PIXm/PDQm et l'INP ([ADR-0004](../../01_cnisn/06_decisions/adr-0004-identite.md), [ADR-0006](../../01_cnisn/06_decisions/adr-0006-inp.md)), la terminologie sur CIM-11+LOINC et SNOMED CT.

3. **Niveau technique (ARTSN).** Chaque composante REDDHI est réalisée par un ou plusieurs chapitres ART de référence, déployés via les lots L1–L7 ([feuille de route](../07_lots/index.md)). La couverture est totale : les 9 composantes DPI-H trouvent une réponse dans les 20 chapitres ART, sans chevauchement redondant.

> **Écart résiduel.** Les chapitres ART-4A, ART-4B, ART-6 et ART-10 sont encore au statut `draft`/`candidate` (voir [annexe A](a-table-de-maturite.md)) : la couverture REDDHI est définie normativement mais reste à confirmer par une initiative de déploiement. La résilience (principe *Resilient*) dépend de la confirmation d'ART-9 (garanties transactionnelles fortes).

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **Fondements CAESN** : Fondements stratégiques et normatifs (`../../00_caesn/00_overview/foundations.md`)
- **CNISN** : Cadre National d'Interopérabilité (`../../01_cnisn/index.md`)
- **Feuille de route ARTSN** : Feuille de route de déploiement (`../07_lots/index.md`)
- **Annexe F** : Index des normes/ADR CNISN consommées par les lots (`f-normes-cnisn-lots.md`)
- **DPI-H Reference Architecture** : OMS/ITU (`https://smart.who.int/ra/`)
- **GovStack Implementation Playbook** : Initiative mondiale (`https://specs.govstack.global/`)
