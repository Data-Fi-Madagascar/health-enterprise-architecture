---
domain: code-systems
id: TERM-LOINC
type: terminology
niveau: "3"
title: "TERM-LOINC : Terminologie des observations de laboratoire"
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
related: ["TERM-CIM-11", "TERM-CODIFICATION-COMMUNE", "CMP-10", "STD-0006"]
constrains: ["DO-20", "DO-32"]
tags: ["artsn", "terminology", "term-loinc"]
accessed_by: ["CMP-10"]
---
# TERM-LOINC : Terminologie des observations de laboratoire

## Finalité

Fournir le referentiel international des observations de laboratoire, afin que les resultats d'analyse d'une enquete ou d'une investigation soient compares et agregeables sans reinterpretation.

## Contenu et portée

- Identification des observations de laboratoire : code, denomination, methode, specimen, systeme, unite et valeurs de reference.
- Codification des resultats d'analyse portes par les objets de donnees d'enquete et d'investigation.
- Base de reference pour les indicateurs de laboratoire du tableau de bord national.

## Objets de données contraints

- DO-20 : Investigation

## Rattachement

- **Composants porteurs** : , [CMP-10](../../building-blocks/sbb/cmp-10.md)
- **Service de codification** : [SRV-03 : Service de terminologie et codification communes](../../../03_business-architecture/business/business-services/srv-03.md)
- **Terminologie chapeau** : [TERM-CODIFICATION-COMMUNE : Terminologie et codification communes](term-codification-commune.md)
- **Norme de référence** : [STD-0006](../../../../01_cnisn/05_standards/std-0006-terminologie.md)

