---
domain: business-services
id: SRV-06
type: service
title: Service de pilotage et tableaux de bord
status: draft
owner: Ministère de la Santé Publique
version: "0.1"
envelope: 02_artsn/06_services/srv-06-service-de-pilotage-et-tableaux-de-bord.md
categorie: applicatif
serves: ["PP-07"]
realizes: ["ABB-EXPOSITION-DONNEES-ANALYTIQUES"]
accesses: ["DO-25"]
implements: ["ART-3", "ART-6"]
related: ["PP-07", "ABB-EXPOSITION-DONNEES-ANALYTIQUES", "CAP-03", "DO-25", "ART-3", "ART-6", "CMP-03", "CMP-04"]
tags: ["artsn", "service", "srv-06", "patterns"]
---
# Service de pilotage et tableaux de bord

Le service de pilotage et tableaux de bord consolide les données du système en indicateurs de performance, tableaux de bord et alertes décisionnels. Il transforme la donnée brute en intelligence pour le pilotage.

Service de catégorie *applicatif*, il [sert l'autorité district, région et Ministère](../../motivation/stakeholders/pp-07.md), [réalise le bloc d'accès et d'exposition des données analytiques](../../../05_reference-library/building-blocks/abb/abb-exposition-donnees-analytiques.md), accède aux indicateurs et tableaux de bord, et met en œuvre les chapitres [ART-3](../../../05_reference-library/patterns/artsn-rules/art-3.md) et [ART-6](../../../05_reference-library/patterns/artsn-rules/art-6.md). Il s'appuie sur l'[entrepôt analytique](../../../05_reference-library/building-blocks/sbb/cmp-03.md) et le [moteur analytique](../../../05_reference-library/building-blocks/sbb/cmp-04.md).

## Catégorie

applicatif.

## Exposition

Sert la partie prenante [PP-07](../../motivation/stakeholders/pp-07.md) et crée de la valeur pour son bénéficiaire.

## Réalisation

Réalisé par [ABB-EXPOSITION-DONNEES-ANALYTIQUES](../../../05_reference-library/building-blocks/abb/abb-exposition-donnees-analytiques.md) et mis en œuvre via les chapitres [ART-3](../../../05_reference-library/patterns/artsn-rules/art-3.md) et [ART-6](../../../05_reference-library/patterns/artsn-rules/art-6.md).
