---
title: "Partie IV : Matrice d'alignement"
id: ptisn-matrice-alignement
domain: 04_matrice-alignement
version: "1.0.0"
status: draft
last_reviewed: 2026-07-31
owner: Équipes techniques des initiatives
tags: ["ptisn", "niveau-4", "interopérabilité", "alignement"]
---

# Partie IV : Matrice d'alignement

La matrice d'alignement établit la correspondance systématique entre les profils techniques d'implémentation par initiative (PTISN), les capacités du Cadre National d'Interopérabilité de la Santé Numérique (CNISN), les chapitres de l'Architecture de Référence Technique (ART) et les composants de l'architecture OpenHIE. Les alignements présentés ci-après ont été corrigés et vérifiés au cours de la migration documentaire (voir `coherence-report.md`) : chaque profil pointe désormais vers la capacité CNISN et le chapitre ART auxquels il se rattache effectivement.

## 1. Alignement avec les capacités CNISN

Le tableau suivant établit, pour chaque capacité d'interopérabilité définie par le CNISN, les profils PTISN qui y contribuent. Cette correspondance permet de s'assurer que l'ensemble des capacités nationales sont couvertes par au moins un profil technique, tout en identifiant les éventuels écarts de couverture.

| Capacité CNISN | Profils PTISN (mapping) |
|---|--|
| CAP-INT-01 | PT-04 |
| CAP-INT-02 | PT-05 |
| CAP-INT-03 | PT-01, PT-02, PT-08, PT-16 |
| CAP-INT-04 | PT-06 |
| CAP-INT-05 | PT-07 |
| CAP-INT-06 | PT-03 |
| CAP-INT-07 | PT-08, PT-09 |
| CAP-INT-08 | PT-10 |
| CAP-INT-09 | PT-11 |
| CAP-INT-10 | PT-12 |
| CAP-INT-11 | PT-13 |
| CAP-INT-12 | : |
| CAP-INT-13 | PT-14 |
| CAP-INT-14 | PT-15 |

On constate que la capacité CAP-INT-12 ne fait l'objet d'aucun profil technique pour le moment. Cette situation traduit soit une capacité dont l'implémentation n'est pas encore requise par les initiatives en cours, soit un domaine nécessitant le développement d'un nouveau profil.

## 2. Alignement avec l'ART

Le tableau ci-dessous associe chaque chapitre de l'Architecture de Référence Technique aux profils PTISN qui en mobilisent les patterns architecturaux. Cette lecture croisée permet de vérifier que chaque chapitre ART est effectivement couvert par au moins un profil, et d'identifier les profils qui mobilisent plusieurs chapitres simultanément.

| Chapitre ART | Profils PTISN principaux |
|---|---|
| ART-0 | PT-01, PT-10, PT-11, PT-14, PT-15 |
| ART-1 | PT-01, PT-02, PT-03, PT-08, PT-14 |
| ART-2 | PT-02, PT-03, PT-07, PT-08 |
| ART-3 | PT-09, PT-12 |
| ART-4 | PT-04, PT-05, PT-06, PT-07, PT-13, PT-15 |
| ART-4A | PT-04, PT-05 |
| ART-4B | PT-04, PT-10, PT-11 |
| ART-4D | PT-15 |
| ART-5 | PT-02, PT-06, PT-07, PT-08, PT-09, PT-13 |
| ART-6 | PT-06, PT-08, PT-09, PT-13 |
| ART-7 | PT-01, PT-02, PT-04, PT-05, PT-09, PT-10, PT-11, PT-12, PT-14, PT-16 |
| ART-8 | PT-02, PT-16 |
| ART-8A | PT-16 |
| ART-8B | PT-15 |
| ART-9 | PT-10 |
| ART-10 | Profil futur |
| ART-11 | PT-01, PT-11, PT-15 |

Le chapitre ART-10 n'est associé à aucun profil existant ; il fait l'objet d'un profil en cours de définition. Les chapitres ART-5 et ART-7 concentrent le plus grand nombre de profils, ce qui confirme leur rôle transversal dans la couche de médiation et la sécurité des données.

## 3. Alignement avec les composants OpenHIE

Le PTISN utilise OpenHIE comme architecture de référence et non comme obligation de produit. OpenHIE documente des composants de partage d'information de santé, notamment les registres, la couche d'interopérabilité et les services terminologiques. Le tableau ci-dessous établit la correspondance entre les services nationaux attendus et les composants OpenHIE auxquels ils se rapportent.

| Service national                   | Composant OpenHIE correspondant        |
|------------------------------------|----------------------------------------|
| Résolution d'identité bénéficiaire | Client Registry                        |
| Registre des professionnels        | Health Worker Registry                 |
| Référentiel des établissements     | Facility Registry                      |
| Terminologie                       | Terminology Service                    |
| Médiation sectorielle              | Interoperability Layer                 |
| Orchestration de processus         | Process Manager / Saga                 |
| Données agrégées                   | Health Metrics and Indicator Reporting |
| Données longitudinales futures     | Shared Health Record, si applicable    |
| Logistique future                  | Product Management and Supply Chain    |
| Échange transfrontalier            | Cross-border HIE (GDHCN)              |
| Surveillance One Health            | Multi-sector event broker              |

Cette correspondance ne signifie pas que tous les composants doivent être déployés simultanément. Le calendrier de mise en œuvre de chaque composant dépend du niveau de maturité de l'initiative correspondante et des prérequis infrastructurels. Les composants qualifiés de « futurs » relèvent de phases ultérieures du programme et ne constituent pas des prérequis pour les initiatives actuellement en cours de conception.

## 4. Alignement avec les lots de déploiement (ARTSN)

Cette section ferme la boucle de traçabilité en reliant chaque lot de la feuille de route ARTSN à ses profils PTISN, aux chapitres ART et aux normes/ADR CNISN qu'il opérationnalise. Elle complète les sections 1–3 (PTISN ↔ CNISN ↔ ART) et la [trajectoire CNISN des lots](../../02_artsn/07_lots/index.md#9-trajectoire-cnisn-et-alignement-des-lots).

| Lot | Profils PTISN concernés | Chapitres ART mobilisés | Normes / ADR CNISN |
|-----|--------------------------|--------------------------|---------------------|
| L1 — Infrastructure & sécurité | PT-04 (via CAP-INT-01) | ART-4, ART-4A, ART-4B, ART-7 | STD-0002, STD-0007, ADR-0008, ADR-0010 |
| L2 — Applications terrain | PT-01, PT-02 (applications & échange) | ART-0, ART-1, ART-2, ART-7, ART-11 | STD-0001, STD-0006, ADR-0003 |
| L3 — Médiation & registres | PT-01, PT-02, PT-03, PT-04, PT-05, PT-06, PT-07, PT-08, PT-16 | ART-1, ART-2, ART-4, ART-4A, ART-4B, ART-4C, ART-5, ART-6, ART-7, ART-8, ART-8C, ART-8D | STD-0003, STD-0005, STD-0004, ADR-0001, ADR-0004, ADR-0006 |
| L4 — Analytique & pilotage | PT-06, PT-08, PT-09, PT-13 (via ART-6) | ART-3, ART-5, ART-6, ART-7 | STD-0001, ADR-0008, ADR-0003 |
| L5 — Extension & pérennisation | PT-10, PT-14, PT-15 (explicites WP-05) | ART-0, ART-4B, ART-7, ART-9, ART-11 | ADR-0005 |
| L6 — Interopérabilité transfrontalière | PT-10, PT-14 (explicites WP-06) | ART-0, ART-1, ART-7, ART-9 | GDHCN, ADR-0007 |
| L7 — Coordination One Health | PT-15 (explicite WP-07) | ART-0, ART-4D, ART-8B, ART-11 | ADR-0001, ADR-0007 |

> **Méthode** : L5/L6/L7 sont dérivés directement des profils listés dans les paquets de travail `wp-05`/`wp-06`/`wp-07` ; L1–L4 sont dérivés par jointure entre le champ `Réalise` des work-packages (capacités CNISN `CAP-INT-*` et chapitres `ART-*`) et les sections 1–2 de cette matrice. Les montants et périmètres précis par lot sont à confirmer en cadrage BRV (voir [méthode TCO](../../00_caesn/06_portfolio/financement-tco.md)).

## Références

- [CAP-INT-01](../../referentiel/capacites/cap-int-01.md)
- [PT-04](../../referentiel/profils/pt-04.md)
- [CAP-INT-02](../../referentiel/capacites/cap-int-02.md)
- [PT-05](../../referentiel/profils/pt-05.md)
- [CAP-INT-03](../../referentiel/capacites/cap-int-03.md)
- [PT-01](../../referentiel/profils/pt-01.md)
- [PT-02](../../referentiel/profils/pt-02.md)
- [PT-08](../../referentiel/profils/pt-08.md)
- [CAP-INT-04](../../referentiel/capacites/cap-int-04.md)
- [PT-06](../../referentiel/profils/pt-06.md)
- [CAP-INT-05](../../referentiel/capacites/cap-int-05.md)
- [PT-07](../../referentiel/profils/pt-07.md)
- [CAP-INT-06](../../referentiel/capacites/cap-int-06.md)
- [PT-03](../../referentiel/profils/pt-03.md)
- [CAP-INT-07](../../referentiel/capacites/cap-int-07.md)
- [PT-09](../../referentiel/profils/pt-09.md)
- [CAP-INT-08](../../referentiel/capacites/cap-int-08.md)
- [PT-10](../../referentiel/profils/pt-10.md)
- [CAP-INT-09](../../referentiel/capacites/cap-int-09.md)
- [PT-11](../../referentiel/profils/pt-11.md)
- [CAP-INT-10](../../referentiel/capacites/cap-int-10.md)
- [PT-12](../../referentiel/profils/pt-12.md)
- [CAP-INT-11](../../referentiel/capacites/cap-int-11.md)
- [PT-13](../../referentiel/profils/pt-13.md)
- [CAP-INT-12](../../referentiel/capacites/cap-int-12.md)
- [ART-0](../../referentiel/chapitres/art-0.md)
- [ART-1](../../referentiel/chapitres/art-1.md)
- [ART-2](../../referentiel/chapitres/art-2.md)
- [ART-3](../../referentiel/chapitres/art-3.md)
- [ART-4](../../referentiel/chapitres/art-4.md)
- [ART-4A](../../referentiel/chapitres/art-4a.md)
- [ART-4B](../../referentiel/chapitres/art-4b.md)
- [ART-5](../../referentiel/chapitres/art-5.md)
- [ART-6](../../referentiel/chapitres/art-6.md)
- [ART-7](../../referentiel/chapitres/art-7.md)
- [ART-8](../../referentiel/chapitres/art-8.md)
- [ART-9](../../referentiel/chapitres/art-9.md)
- [ART-10](../../referentiel/chapitres/art-10.md)
- [ART-11](../../referentiel/chapitres/art-11.md)
