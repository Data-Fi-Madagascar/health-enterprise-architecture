---
title: "Annexe G : Matrice des types d'interopérabilité"
id: cnisn-annexe-g
domain: 08_annexes
version: "1.0.0"
status: draft
last_reviewed: 2026-08-18
owner: DEPSI
tags: ["cnisn", "niveau-2", "annexes", "interopérabilité"]
---

# Annexe G : Matrice des types d'interopérabilité

Cette annexe rend explicite la couverture des quatre types d'interopérabilité par les composants du CNISN (capacités, principes, standards, gouvernance).

## 1. Définitions

| Type | Définition |
|------|------------|
| **Technique** | Capacité des systèmes à échanger des données au niveau des protocoles, formats et mécanismes de communication. |
| **Sémantique** | Capacité des systèmes à échanger et comprendre la signification des données, via des vocabulaires, terminologies et codifications communs. |
| **Organisationnelle** | Capacité des organisations à travailler ensemble via des accords de gouvernance, des processus métier partagés et des structures de responsabilité. |
| **Juridique** | Capacité des systèmes et organisations à respecter les bases légales, les obligations de consentement, les contraintes de résidence des données et les cadres réglementaires applicables. |

## 2. Matrice capacités → types

| Capacité | Technique | Sémantique | Organisationnelle | Juridique |
|----------|:---------:|:----------:|:-----------------:|:---------:|
| ABB-IDENTITE-BENEFICIAIRE : Résolution d'identité du bénéficiaire | | | ● | |
| ABB-REGISTRE-PROFESSIONNELS : Registre des professionnels de santé | | | ● | |
| ABB-ECHANGE-MEDIATION : Échange et médiation inter-systèmes | ● | | ● | |
| ABB-REFERENTIEL-STRUCTURES-SERVICES : Référentiel des structures et services | | ● | | |
| ABB-SERVICE-TERMINOLOGIE : Terminologie et codification communes | | ● | | |
| ABB-CATALOGUE-CONTRATS : Catalogue des services et registre des contrats | ● | | ● | |
| ABB-EXPOSITION-DONNEES-ANALYTIQUES : Accès et exposition des données analytiques | ● | | | |
| ABB-CONFIANCE-AUTORISATION : Confiance, sécurité et autorisation | ● | | ● | |
| ABB-GESTION-CONSENTEMENT : Consentement et bases d'autorisation | | | ● | ● |
| ABB-AUDIT-PROVENANCE : Provenance, audit et traçabilité | | | ● | ● |
| ABB-RECONCILIATION-DONNEES : Qualité et réconciliation | | ● | | |
| COMP-HOMOLOGATION-INTEROPERABILITE : Conformité et tests d'interopérabilité | ● | | ● | |
| PART-ECHANGE-TRANSFRONTALIER : Interopérabilité transfrontalière | ● | | ● | ● |
| PART-ONE-HEALTH : Échanges intersectoriels One Health | | | ● | ● |

**Lecture :** ● = couverture directe principale. Les capacités peuvent contribuer à plusieurs types simultanément.

## 3. Matrice principes → types

| Principe | Technique | Sémantique | Organisationnelle | Juridique |
|----------|:---------:|:----------:|:-----------------:|:---------:|
| P-INT-01 : Autorité désignée | | ● | ● | |
| P-INT-02 : Résolution contre l'autorité | | ● | | |
| P-INT-03 : Copies locales non autoritatives | ● | | | |
| P-INT-04 : Historisation des références | | ● | | |
| P-INT-05 : Contrat explicite | ● | | ● | |
| P-INT-06 : Versionnement et compatibilité | ● | | | |
| P-INT-07 : Responsabilité de la donnée | | | ● | |
| P-INT-08 : Publication au catalogue des services | ● | | ● | |
| P-INT-09 : Publication des contrats | ● | | | |
| P-INT-10 : Accord préalable | | | ● | ● |
| P-INT-11 : Arbitrage des conflits d'autorité | | | ● | |
| P-INT-12 : Dérogation explicite | | | ● | ● |
| P-INT-13 : Dérogation d'urgence | | | ● | ● |
| P-INT-14 : Base d'autorisation explicite | | | | ● |
| P-INT-15 : Limitation à la finalité | | | | ● |
| P-INT-16 : Résidence et non-réplication | | | | ● |
| P-INT-17 : Minimisation | | | | ● |
| P-INT-18 : Traçabilité différenciée | | | | ● |
| P-INT-19 : Neutralité technologique | ● | | | |
| P-INT-20 : Portabilité et réversibilité | ● | | | |
| P-INT-21 : Progressivité | ● | | | |
| P-INT-22 : Fonctionnement en connectivité contrainte | ● | | | |
| P-INT-23 : Conformité fondée sur des preuves | | | ● | |
| P-INT-24 : Applicabilité déclarée | | | ● | |
| P-INT-25 : Réévaluation continue | | | ● | |

## 4. Matrice standards → types

| Standard | Technique | Sémantique | Organisationnelle | Juridique |
|----------|:---------:|:----------:|:-----------------:|:---------:|
| STD-0001 : HL7 FHIR R4 | ● | ● | | |
| STD-0002 : Chiffrement et contrôle d'accès | ● | | | ● |
| STD-0003 : X-Road | ● | | ● | |
| STD-0004 : mADX | ● | ● | | |
| STD-0005 : PIXm/PDQm | ● | ● | | |
| STD-0006 : CIM-11 + LOINC | | ● | | |
| NORM-007 : RSI 2005 | | | | ● |
| NORM-008 : Tripartite Plus | | | ● | ● |

## 5. Gouvernance → types

| Composant | Technique | Sémantique | Organisationnelle | Juridique |
|-----------|:---------:|:----------:|:-----------------:|:---------:|
| CNASN (Comité National d'Ayatice et de Normalisation) | | | ● | ● |
| ADR-0002 : mADX | ● | ● | | |
| ADR-0003 : FHIR | ● | ● | | |
| ADR-0005 : Consentement | | | ● | ● |
| ADR-0006 : INP | | ● | ● | |
| ADR-0007 : GDHCN | | | ● | ● |
| ADR-0008 : ATNA | ● | | ● | ● |
| ADR-0009 : Terminologie | | ● | | |

## 6. Synthèse par type

### 6.1 Interopérabilité technique

**Capacités :** ABB-ECHANGE-MEDIATION, 06, 07, 08, 12, 13 (6 capacités)

**Principes :** P-INT-03, 05, 06, 08, 09, 19, 20, 21, 22 (9 principes)

**Standards :** STD-0001, 0002, 0003, 0004, 0005 (5 standards)

### 6.2 Interopérabilité sémantique

**Capacités :** ABB-REFERENTIEL-STRUCTURES-SERVICES, 05, 11 (3 capacités)

**Principes :** P-INT-01, 02, 04 (3 principes)

**Standards :** STD-0001, 0004, 0005, 0006 (4 standards)

### 6.3 Interopérabilité organisationnelle

**Capacités :** ABB-IDENTITE-BENEFICIAIRE, 02, 03, 06, 08, 09, 10, 12, 13, 14 (10 capacités)

**Principes :** P-INT-01, 05, 07, 08, 10, 11, 12, 13, 23, 24, 25 (11 principes)

**Standards :** STD-0003, NORM-008 (2 standards)

**Gouvernance :** CNASN, ADR-0005, 0006, 0007, 0008

### 6.4 Interopérabilité juridique

**Capacités :** ABB-GESTION-CONSENTEMENT, 10, 13, 14 (4 capacités)

**Principes :** P-INT-10, 12, 13, 14, 15, 16, 17, 18 (8 principes)

**Standards :** STD-0002, NORM-007, NORM-008 (3 standards)

**Gouvernance :** CNASN, ADR-0005, 0007, 0008

## 7. Observation

Les 16 capacités, 25 principes et 8 standards du CNISN couvrent **l'ensemble des quatre types d'interopérabilité** sans nécessiter de taxonomie explicite supplémentaire. La matrice ci-dessus rend cette couverture visible et vérifiable.

L'interopérabilité **organisationnelle** est la plus largement couverte (10 capacités, 11 principes), ce qui reflète la nature governance-first du CNISN. L'interopérabilité **technique** est couverte par 6 capacités et 9 principes, principalement via les standards FHIR, X-Road et mADX.
