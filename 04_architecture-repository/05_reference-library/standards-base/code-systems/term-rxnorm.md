---
domain: code-systems
id: TERM-RXNORM
type: terminology
niveau: "3"
title: "TERM-RXNORM : Terminologie des médicaments RxNorm"
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
related: ["TERM-SNOMED-CT", "TERM-CODIFICATION-COMMUNE", "CMP-10", "STD-0007"]
constrains: ["DO-06", "DO-10", "DO-11"]
tags: ["artsn", "terminology", "term-rxnorm"]
accessed_by: ["CMP-10"]
---
# TERM-RXNORM : Terminologie des médicaments RxNorm

## Finalité

Fournir le référentiel international des médicaments normalisé, afin que le même produit pharmaceutique soit identifié sans ambiguïté dans les échanges entre systèmes.

## Contenu et portée

- Normalisation des dénominations de médicaments et des marques, avec relations de synonymie et de regroupement.
- Relation avec SNOMED CT pour les concepts médicamenteux.
- Utilisation comme source de correspondance pour les produits dispensés.

## Objets de données contraints

- DO-06 : Prescription
- DO-10 : Dispensation
- DO-11 : Produit de santé

## Rattachement

- **Composants porteurs** : [CMP-10](../../building-blocks/sbb/cmp-10.md)
- **Service de codification** : [SRV-03 : Service de terminologie et codification communes](../../../03_business-architecture/business/business-services/srv-03.md)
- **Terminologie chapeau** : [TERM-CODIFICATION-COMMUNE : Terminologie et codification communes](term-codification-commune.md)
- **Norme de référence** : [STD-0007](../../../../01_cnisn/05_standards/std-0007-snomed-ct.md)

