---
title: "Annexe F : Index des normes et ADR CNISN consommées par les lots ARTSN"
id: normes-cnisn-lots
domain: 08_annexes
version: "1.0.0"
status: draft
last_reviewed: 2026-08-22
owner: DEPSI
tags: ["artsn", "annexes", "cnisn", "alignement", "lots"]
---

# Annexe F : Index des normes et ADR CNISN consommées par les lots ARTSN

Cet index inverse la section 9 de la Feuille de route de déploiement (lots). Il répond à la question : *quelle norme ou décision CNISN est mobilisée par quel lot de travail ARTSN ?* Chaque lot opérationnalise un sous-ensemble de la trajectoire CNISN ; cet index garantit la traçabilité arrière (norme → initiatives).

## Index norme / ADR → lots

| Référentiel CNISN | Intitulé | Lots ARTSN consommateurs |
|-------------------|----------|---------------------------|
| [STD-0001](../../01_cnisn/05_standards/std-0001-interopabilite-fhir.md) | HL7 FHIR R4 (interopérabilité) | [L2 — Applications terrain](../07_lots/index.md), [L4 — Analytique & pilotage](../07_lots/index.md) |
| [STD-0002](../../01_cnisn/05_standards/std-0002-securite-chiffrement.md) | Chiffrement et sécurité | [L1 — Infrastructure & sécurité](../07_lots/index.md) |
| [STD-0003](../../01_cnisn/05_standards/std-0003-x-road.md) | X-Road (plateforme d'échange) | [L3 — Médiation & registres](../07_lots/index.md) |
| [STD-0004](../../01_cnisn/05_standards/std-0004-madx.md) | mADX (analytique DHIS2) | [L3 — Médiation & registres](../07_lots/index.md) |
| [STD-0005](../../01_cnisn/05_standards/std-0005-identite-pixm.md) | PIXm / PDQm (identité) | [L3 — Médiation & registres](../07_lots/index.md) |
| [STD-0006](../../01_cnisn/05_standards/std-0006-terminologie.md) | Terminologie et codification | [L2 — Applications terrain](../07_lots/index.md) |
| [STD-0007](../../01_cnisn/05_standards/std-0007-snomed-ct.md) | SNOMED CT (licence) | [L1 — Infrastructure & sécurité](../07_lots/index.md) |
| [ADR-0001](../../01_cnisn/06_decisions/adr-0001-x-road.md) | Adoption de X-Road | [L3 — Médiation & registres](../07_lots/index.md), [L7 — Coordination One Health](../07_lots/index.md) |
| [ADR-0003](../../01_cnisn/06_decisions/adr-0003-fhir.md) | FHIR R4 comme standard | [L2 — Applications terrain](../07_lots/index.md), [L4 — Analytique & pilotage](../07_lots/index.md) |
| [ADR-0004](../../01_cnisn/06_decisions/adr-0004-identite.md) | Résolution d'identité | [L3 — Médiation & registres](../07_lots/index.md) |
| [ADR-0005](../../01_cnisn/06_decisions/adr-0005-consentement.md) | Gestion du consentement | [L5 — Extension & pérennisation](../07_lots/index.md) |
| [ADR-0006](../../01_cnisn/06_decisions/adr-0006-inp.md) | Registre INP | [L3 — Médiation & registres](../07_lots/index.md) |
| [ADR-0007](../../01_cnisn/06_decisions/adr-0007-gdhcn.md) | GDHCN (échange transfrontalier) | [L6 — Interopérabilité transfrontalière](../07_lots/index.md), [L7 — Coordination One Health](../07_lots/index.md) |
| [ADR-0008](../../01_cnisn/06_decisions/adr-0008-atna.md) | Audit ATNA | [L1 — Infrastructure & sécurité](../07_lots/index.md), [L4 — Analytique & pilotage](../07_lots/index.md) |
| [ADR-0010](../../01_cnisn/06_decisions/adr-0010-cadre-legal.md) | Cadre légal contraignant | [L1 — Infrastructure & sécurité](../07_lots/index.md) |

## Notes

- **GDHCN** (réseau mondial d'échange de certificats de vaccination) est référencé dans la lot L6 via l'ADR-0007 ; il ne dispose pas d'une norme `STD-*` distincte.
- Les lots L5 et L7 n'introduisent pas de nouvelle norme : ils renforcent des décisions existantes (consentement ADR-0005 pour L5 ; X-Road ADR-0001 et GDHCN ADR-0007 pour L7).
- La correspondance lot → normes reste disponible dans la [section 9 de la feuille de route](../07_lots/index.md#9-trajectoire-cnisn-et-alignement-des-lots).

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **Feuille de route ARTSN** : Feuille de route de déploiement (`../07_lots/index.md`)
- **CNISN** : Cadre National d'Interopérabilité (`../../01_cnisn/index.md`)
