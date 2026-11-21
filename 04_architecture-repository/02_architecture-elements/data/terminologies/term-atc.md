---
domain: terminologies
id: TERM-ATC
type: terminology
niveau: "3"
title: "TERM-ATC : Classification pharmacologique ATC de l'OMS"
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
related: ["TERM-DCI", "TERM-CODIFICATION-COMMUNE", "CMP-10"]
constrains: ["DO-06", "DO-10", "DO-11"]
tags: ["artsn", "terminology", "term-atc"]
accessed_by: ["CMP-10"]
---
# TERM-ATC : Classification pharmacologique ATC de l'OMS

## Finalité

Fournir la classification pharmacologique de l'OMS, afin de comparer les consommations et les expenditures de médicaments entre formations sanitaires et entre périodes.

## Contenu et portée

- Classification hiérarchique à sept niveaux : groupe pharmacologique, classe thérapeutique, sous-classe, groupe chimique, sous-groupe chimique, principe actif, substance.
- Codification des produits de santé pour l'analyse épidémiologique.
- Base de référence pour les indicateurs de couverture médicamenteuse.

## Objets de données contraints

- DO-06 : Prescription
- DO-10 : Dispensation
- DO-11 : Produit de santé

## Rattachement

- **Composants porteurs** : [CMP-10](../../../05_building-blocks/abb/legacy-components/cmp-10.md)
- **Service de codification** : [SRV-03 : Service de terminologie et codification communes](../../../05_building-blocks/abb/legacy-services/srv-03.md)
- **Terminologie chapeau** : [TERM-CODIFICATION-COMMUNE : Terminologie et codification communes](term-codification-commune.md)

