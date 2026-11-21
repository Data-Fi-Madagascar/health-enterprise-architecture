---
domain: terminologies
id: TERM-CIM-11
type: terminology
niveau: "3"
title: "TERM-CIM-11 : Classification internationale des maladies"
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
related: ["TERM-CODIFICATION-COMMUNE", "CMP-10", "STD-0006"]
constrains: ["DO-05"]
tags: ["artsn", "terminology", "term-cim-11"]
accessed_by: ["CMP-10"]
---
# TERM-CIM-11 : Classification internationale des maladies

## Finalité

Fournir la classification internationale des maladies, afin que les motifs de consultation et les diagnostics soient codés selon une nomenclature unique et intercomparable.

## Contenu et portée

- Chapitres, extensions et codes CIM-11 utilisés pour le codage des diagnostics et des motifs d'hospitalisation.
- Tableaux de correspondance avec la CIM-10 pour la continuité des séries historiques.
- Support des agrégations de la couche analytique (épidémiologie, programmes de santé).

## Objets de données contraints

- DO-05 : Consultation

## Rattachement

- **Composants porteurs** : , [CMP-10](../../../05_building-blocks/abb/legacy-components/cmp-10.md)
- **Service de codification** : [SRV-03 : Service de terminologie et codification communes](../../../05_building-blocks/abb/legacy-services/srv-03.md)
- **Terminologie chapeau** : [TERM-CODIFICATION-COMMUNE : Terminologie et codification communes](term-codification-commune.md)
- **Norme de référence** : [STD-0006](../../../../01_cnisn/05_standards/std-0006-terminologie.md)

