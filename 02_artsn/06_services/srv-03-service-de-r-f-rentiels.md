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
realizes: ["CAP-INT-03"]
accesses: ["DO-02"]
implements: ["ART-4"]
related: ["PP-06", "CAP-INT-03", "DO-02", "ART-4", "CMP-10"]
tags: ["artsn", "service", "srv-03", "patterns"]
---


# Service de référentiels

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

Le service de référentiels gère les listes et terminologies partagées — produits, organisations, CIM-10, SNOMED CT, LOINC — sur lesquelles s'appuie toute la donnée de santé. Il assure l'interprétabilité et la comparabilité des échanges.

Service de catégorie *applicatif*, il [sert la formation sanitaire](../../referentiel/parties-prenantes/pp-06.md), [réalise la capacité « Référentiels et terminologies »](../../referentiel/capacites/cap-int-03.md), [accède à l'objet de données de référentiel](../../referentiel/objets-de-donnees/do-02.md) et [met en œuvre le chapitre ART-4 (référentiels)](../../referentiel/chapitres/art-4.md). Il s'appuie sur le [composant de référentiels](../../referentiel/composants/cmp-10.md).

## Catégorie

applicatif.

## Exposition

Sert la partie prenante [PP-06](../../referentiel/parties-prenantes/pp-06.md) et crée de la valeur pour son bénéficiaire.

## Réalisation

Réalisé par les capacités [CAP-INT-03](../../referentiel/capacites/cap-int-03.md) et mis en œuvre via les chapitres [ART-4](../../referentiel/chapitres/art-4.md).

<!-- END:GENERATED -->
