---
domain: legacy-components
id: CMP-09
type: composant-applicatif
categorie: applicatif
niveau: "1"
title: Référentiel des métadonnées d'exploitation (ART-4)
status: active
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/05_cartographie/composants.md
maps_to: ["ABB-GESTION-CONSENTEMENT"]
implements: ["ART-4"]
applies_to: ["PRC-07", "PRC-08"]
accesses: ["TERM-SNOMED-CT", "TERM-RXNORM", "TERM-ATC", "TERM-DCI", "TERM-CIM-11", "TERM-LOINC", "TERM-CODIFICATION-COMMUNE"]
related: ["ENF-4", "CAP-09", "VS-03"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-09", "couche-4"]
realized_by: ["WP-02"]
---
# Référentiel des métadonnées d'exploitation ([ART-4: Référentiels de métadonnées de gestion](../../../04_patterns/artsn-rules/art-4.md))

**Contenu normatif.** Ce composant définit et gère les métadonnées d'exploitation : nomenclatures, codifications et standards de données. Il assure l'interopérabilité sémantique entre les systèmes et garantit l'utilisation cohérente des terminologies et classifications.

**Discipline de mise en œuvre.** Il est l'autorité sémantique de la plateforme. Toute définition de donnée clinique ou administrative passe par ce référentiel, ce qui garantit l'unicité des définitions à l'échelle nationale.

- **Rattachement** : [ART-4](../../../04_patterns/artsn-rules/art-4.md) (référentiel des métadonnées), [ABB-GESTION-CONSENTEMENT: Gestion des consentements et bases d’autorisation](../abb-gestion-consentement.md).
- **Processus soutenus** : [PRC-07: Identification et droits des bénéficiaires](../../../02_architecture-elements/business/processes/prc-07.md) (production données), [PRC-08: Financement et exemption au point de service](../../../02_architecture-elements/business/processes/prc-08.md) (qualité).
- **Données portées** : [TERM-SNOMED-CT : Terminologie clinique SNOMED CT](../../../02_architecture-elements/data/terminologies/term-snomed-ct.md), [TERM-RXNORM : Terminologie des médicaments RxNorm](../../../02_architecture-elements/data/terminologies/term-rxnorm.md), [TERM-ATC : Classification pharmacologique ATC de l'OMS](../../../02_architecture-elements/data/terminologies/term-atc.md), [TERM-DCI : Dénomination commune internationale](../../../02_architecture-elements/data/terminologies/term-dci.md), [TERM-CIM-11 : Classification internationale des maladies](../../../02_architecture-elements/data/terminologies/term-cim-11.md), [TERM-CODIFICATION-COMMUNE : Terminologie et codification communes](../../../02_architecture-elements/data/terminologies/term-codification-commune.md)
- **Statut : Stable.**
