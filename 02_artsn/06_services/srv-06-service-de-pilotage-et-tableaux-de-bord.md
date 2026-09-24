---

domain: services
id: SRV-06
type: service
title: Service de pilotage et tableaux de bord
status: draft
owner: Ministère de la Santé Publique
version: "0.1"
envelope: 02_artsn/06_services/srv-06-service-de-pilotage-et-tableaux-de-bord.md
categorie: applicatif
serves: ["PP-07"]
realizes: ["CAP-03"]
accesses: ["DO-04"]
implements: ["ART-3"]
related: ["PP-07", "CAP-03", "DO-04", "ART-3", "CMP-12"]
tags: ["artsn", "service", "srv-06", "patterns"]
---


# Service de pilotage et tableaux de bord

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

Le service de pilotage et tableaux de bord consolide les données du système en indicateurs de performance, tableaux de bord et alertes décisionnels. Il transforme la donnée brute en intelligence pour le pilotage.

Service de catégorie *applicatif*, il [sert l'autorité district, région et Ministère](../../04_architecture-repository/02_architecture-elements/motivation/stakeholders/pp-07.md), [réalise le bloc d'accès et d'exposition des données analytiques](../../04_architecture-repository/05_building-blocks/abb/abb-exposition-donnees-analytiques.md), accède aux indicateurs et tableaux de bord, et met en œuvre les chapitres [ART-3](../../04_architecture-repository/04_patterns/artsn-rules/art-3.md) et [ART-6](../../04_architecture-repository/04_patterns/artsn-rules/art-6.md). Il s'appuie sur l'[entrepôt analytique](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-03.md) et le [moteur analytique](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-04.md).

## Catégorie

applicatif.

## Exposition

Sert la partie prenante [PP-07](../../04_architecture-repository/02_architecture-elements/motivation/stakeholders/pp-07.md) et crée de la valeur pour son bénéficiaire.

## Réalisation

Réalisé par [ABB-EXPOSITION-DONNEES-ANALYTIQUES](../../04_architecture-repository/05_building-blocks/abb/abb-exposition-donnees-analytiques.md) et mis en œuvre via les chapitres [ART-3](../../04_architecture-repository/04_patterns/artsn-rules/art-3.md) et [ART-6](../../04_architecture-repository/04_patterns/artsn-rules/art-6.md).

<!-- END:GENERATED -->
