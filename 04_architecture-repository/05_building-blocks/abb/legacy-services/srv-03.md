---
domain: legacy-services
id: SRV-03
type: service
title: Service de référentiels
status: draft
owner: Ministère de la Santé Publique
version: "0.1"
envelope: 02_artsn/06_services/srv-03-service-de-r-f-rentiels.md
categorie: applicatif
serves: ["PP-06"]
realizes: ["ABB-SERVICE-TERMINOLOGIE"]
accesses: ["TERM-CODIFICATION-COMMUNE", "DO-11", "DO-23", "DO-25"]
implements: ["ART-4"]
related: ["PP-06", "ABB-SERVICE-TERMINOLOGIE", "TERM-CODIFICATION-COMMUNE", "DO-11", "DO-23", "DO-25", "ART-4", "CMP-10"]
tags: ["artsn", "service", "srv-03", "patterns"]
---
# Service de référentiels

Le service de référentiels gère les listes et terminologies partagées — produits, organisations, CIM-11, SNOMED CT, LOINC — sur lesquelles s'appuie toute la donnée de santé. Il assure l'interprétabilité et la comparabilité des échanges.

Service de catégorie *applicatif*, il [sert la formation sanitaire](../../../02_architecture-elements/motivation/stakeholders/pp-06.md), [réalise le service de terminologie et codification communes](../abb-service-terminologie.md), accède aux terminologies ainsi qu'aux référentiels de produits, structures et indicateurs, et [met en œuvre le chapitre ART-4 (référentiels)](../../../04_patterns/artsn-rules/art-4.md). Il s'appuie sur le [registre des terminologies](../legacy-components/cmp-10.md).

## Catégorie

applicatif.

## Exposition

Sert la partie prenante [PP-06](../../../02_architecture-elements/motivation/stakeholders/pp-06.md) et crée de la valeur pour son bénéficiaire.

## Réalisation

Réalisé par [ABB-SERVICE-TERMINOLOGIE](../abb-service-terminologie.md) et mis en œuvre via le chapitre [ART-4](../../../04_patterns/artsn-rules/art-4.md).
