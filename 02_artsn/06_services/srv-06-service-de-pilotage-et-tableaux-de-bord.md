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

Service de catégorie *applicatif*, il [sert l'autorité district, région et Ministère](../../referentiel/parties-prenantes/pp-07.md), [réalise la capacité « Pilotage et performance »](../../referentiel/capabilites/cap-03.md), [accède à l'objet de données de pilotage](../../referentiel/objets-de-donnees/do-04.md) et [met en œuvre le chapitre ART-3 (pilotage)](../../referentiel/chapitres/art-3.md). Il s'appuie sur le [composant de pilotage](../../referentiel/composants/cmp-12.md).

## Catégorie

applicatif.

## Exposition

Sert la partie prenante [PP-07](../../referentiel/parties-prenantes/pp-07.md) et crée de la valeur pour son bénéficiaire.

## Réalisation

Réalisé par les capacités [CAP-03](../../referentiel/capabilites/cap-03.md) et mis en œuvre via les chapitres [ART-3](../../referentiel/chapitres/art-3.md).

<!-- END:GENERATED -->
