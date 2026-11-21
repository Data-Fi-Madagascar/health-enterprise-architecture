---
domain: legacy-components
id: CMP-10
type: composant-applicatif
categorie: applicatif
niveau: "1"
title: Registre des terminologies
status: active
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/05_cartographie/composants.md
maps_to: ["ABB-SERVICE-TERMINOLOGIE"]
implements: ["ART-4"]
applies_to: ["PRC-07", "PRC-08"]
accesses: ["TERM-SNOMED-CT", "TERM-RXNORM", "TERM-ATC", "TERM-DCI", "TERM-CIM-11", "TERM-LOINC", "TERM-CODIFICATION-COMMUNE"]
related: ["ENF-4", "CAP-13", "CAP-14", "VS-03"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-10", "couche-4"]
realized_by: ["WP-02", "WP-03"]
---
# Registre des terminologies

**Contenu normatif.** Ce composant tient le registre national des terminologies et des référentiels de codification de la plateforme (CIM-11, SNOMED CT, LOINC, ATC, DCI, codification commune). Il assure le mapping sémantique entre les systèmes et fournit les services de traduction et de validation des codages. Il est l'autorité sémantique de la plateforme : toute définition de donnée clinique ou administrative passe par ce registre, ce qui garantit l'unicité des définitions à l'échelle nationale.

**Discipline de mise en œuvre.** Il sert de pont sémantique entre les systèmes hétérogènes. Il garantit que les données codées dans un système sont interprétables et exploitables par un autre.

- **Rattachement** : [ART-4](../../../04_patterns/artsn-rules/art-4.md) (référentiel des métadonnées), [ABB-SERVICE-TERMINOLOGIE: Service de terminologie et codification communes](../abb-service-terminologie.md).
- **Processus soutenus** : [PRC-07: Identification et droits des bénéficiaires](../../../02_architecture-elements/business/processes/prc-07.md) (production données), [PRC-08: Financement et exemption au point de service](../../../02_architecture-elements/business/processes/prc-08.md) (qualité).
- **Données portées** : [TERM-SNOMED-CT : Terminologie clinique SNOMED CT](../../../02_architecture-elements/data/terminologies/term-snomed-ct.md), [TERM-RXNORM : Terminologie des médicaments RxNorm](../../../02_architecture-elements/data/terminologies/term-rxnorm.md), [TERM-ATC : Classification pharmacologique ATC de l'OMS](../../../02_architecture-elements/data/terminologies/term-atc.md), [TERM-DCI : Dénomination commune internationale](../../../02_architecture-elements/data/terminologies/term-dci.md), [TERM-CIM-11 : Classification internationale des maladies](../../../02_architecture-elements/data/terminologies/term-cim-11.md), [TERM-LOINC : Terminologie des observations de laboratoire](../../../02_architecture-elements/data/terminologies/term-loinc.md), [TERM-CODIFICATION-COMMUNE : Terminologie et codification communes](../../../02_architecture-elements/data/terminologies/term-codification-commune.md)
- **Statut : Stable.**

## Fusion

Ce composant est le résultat de la fusion du composant suivant, retiré du catalogue :

- `CMP-09` (Référentiel des métadonnées d'exploitation)

CMP-09 partageait la même signature relationnelle que CMP-10 : il implémentait ART-4, s'appliquait aux mêmes processus et accédait aux mêmes terminologies. La fusion est tracée dans `04_architecture-repository/00_metamodel/object-migration.yaml` et décidée par l'ADR-0017.
