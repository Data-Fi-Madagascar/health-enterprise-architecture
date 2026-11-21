---
domain: terminologies
id: TERM-DCI
type: terminology
niveau: "3"
title: "TERM-DCI : Dénomination commune internationale"
status: candidate
owner: DEPSI
version: "0.1"
envelope: 02_artsn/03_objets-de-donnees/index.md
togaf_repository_section: standards-information-base
togaf_adm_phase: C
architecture_level: enterprise-transversal
architecture_domain: data
architecture_scope: semantics
architecture_state: target
maps_to: ["CAP-13", "CAP-14"]
implements: ["ART-2", "ART-4"]
related: ["TERM-SNOMED-CT", "TERM-RXNORM", "TERM-CODIFICATION-COMMUNE", "CMP-10"]
constrains: ["DO-06", "DO-10", "DO-11", "DO-12"]
tags: ["artsn", "terminology", "term-dci"]
accessed_by: ["CMP-09", "CMP-10"]
---
# TERM-DCI : Dénomination commune internationale

## Finalité

Fournir la dénomination commune internationale des substances actives, afin que la traçabilité du médicament depuis le répertoire jusqu'au bénéficiaire ne dépende d'aucun nom commercial local.

## Contenu et portée

- Dénomination commune internationale des substances actives, par lفرة OMS.
- Usage obligatoire dans les objets de données produits et dispensés : le lot et la dispensation identifient le produit par sa DCI.
- Relation de correspondance avec SNOMED CT et RxNorm.

## Objets de données contraints

- DO-06 : Prescription
- DO-10 : Dispensation
- DO-11 : Produit de santé
- DO-12 : Lot

## Rattachement

- **Composants porteurs** : [CMP-10](../../../05_building-blocks/abb/legacy-components/cmp-10.md)
- **Service de codification** : [SRV-03 : Service de terminologie et codification communes](../../../05_building-blocks/abb/legacy-services/srv-03.md)
- **Terminologie chapeau** : [TERM-CODIFICATION-COMMUNE : Terminologie et codification communes](term-codification-commune.md)

