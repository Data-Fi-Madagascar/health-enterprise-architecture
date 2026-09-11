---

domain: services
id: SRV-03
type: service
title: Service de référentiels
status: draft
owner: Ministère de la Santé Publique
version: "0.1"
envelope: 02_artsn/06_services/srv-03-service-de-r-f-rentiels.md
categorie: applicatif
serves: ["PP-06"]
realizes: ["ABB-ECHANGE-MEDIATION"]
accesses: ["DO-02"]
implements: ["ART-4"]
related: ["PP-06", "ABB-ECHANGE-MEDIATION", "DO-02", "ART-4", "CMP-10"]
tags: ["artsn", "service", "srv-03", "patterns"]
---


# Service de référentiels

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

Le service de référentiels gère les listes et terminologies partagées — produits, organisations, CIM-11, SNOMED CT, LOINC — sur lesquelles s'appuie toute la donnée de santé. Il assure l'interprétabilité et la comparabilité des échanges.

Service de catégorie *applicatif*, il [sert la formation sanitaire](../../04_architecture-repository/02_architecture-elements/motivation/stakeholders/pp-06.md), [réalise la capacité « Référentiels et terminologies »](../../04_architecture-repository/05_building-blocks/abb/abb-echange-mediation.md), [accède à l'objet de données de référentiel](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-02.md) et [met en œuvre le chapitre ART-4 (référentiels)](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md). Il s'appuie sur le [composant de référentiels](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-10.md).

## Catégorie

applicatif.

## Exposition

Sert la partie prenante [PP-06](../../04_architecture-repository/02_architecture-elements/motivation/stakeholders/pp-06.md) et crée de la valeur pour son bénéficiaire.

## Réalisation

Réalisé par les capacités [ABB-ECHANGE-MEDIATION](../../04_architecture-repository/05_building-blocks/abb/abb-echange-mediation.md) et mis en œuvre via les chapitres [ART-4](../../04_architecture-repository/04_patterns/artsn-rules/art-4.md).

<!-- END:GENERATED -->
