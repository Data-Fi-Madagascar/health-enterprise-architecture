---
domain: terminologies
id: TERM-SNOMED-CT
type: terminology
niveau: "3"
title: "TERM-SNOMED-CT : Terminologie clinique SNOMED CT"
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
related: ["TERM-CODIFICATION-COMMUNE", "TERM-RXNORM", "CMP-09", "CMP-10", "STD-0007"]
constrains: ["DO-06", "DO-10", "DO-11"]
tags: ["artsn", "terminology", "term-snomed-ct"]
accessed_by: ["CMP-09", "CMP-10"]
---
# TERM-SNOMED-CT : Terminologie clinique SNOMED CT

## Finalité

Fournir la codification clinique internationale des concepts de santé, afin que les observations cliniques partagées entre institutions soient interprétables de façon identique.

## Contenu et portée

- Concepts cliniques : findings, symptoms, diagnoses, procedures, medicinal products, body structures.
- Hiérarchieontologique et attributs de contexte (finding site, severity, laterality).
- Versionnage, extensions nationales et traduction clinically significant.

## Objets de données contraints

- DO-06 : Prescription
- DO-10 : Dispensation
- DO-11 : Produit de santé

## Rattachement

- **Composants porteurs** : [CMP-09](../../../05_building-blocks/abb/legacy-components/cmp-09.md), [CMP-10](../../../05_building-blocks/abb/legacy-components/cmp-10.md)
- **Service de codification** : [SRV-03 : Service de terminologie et codification communes](../../../05_building-blocks/abb/legacy-services/srv-03.md)
- **Terminologie chapeau** : [TERM-CODIFICATION-COMMUNE : Terminologie et codification communes](term-codification-commune.md)
- **Norme de référence** : [STD-0007](../../../../01_cnisn/05_standards/std-0007-snomed-ct.md)

