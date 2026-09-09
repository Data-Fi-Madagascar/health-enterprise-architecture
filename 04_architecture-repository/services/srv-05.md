---
domain: services
id: SRV-05
type: service
title: Service logistique (LMIS)
status: draft
owner: Ministère de la Santé Publique
version: "0.1"
envelope: 02_artsn/06_services/srv-05-service-logistique-lmis.md
categorie: applicatif
serves: ["PP-06"]
realizes: ["CAP-INT-10"]
accesses: ["DO-03"]
implements: ["ART-10"]
related: ["PP-06", "CAP-INT-10", "DO-03", "ART-10", "CMP-23"]
tags: ["artsn", "service", "srv-05", "patterns"]
---
# Service logistique (LMIS)

Le service logistique (LMIS) assure la continuité de la chaîne d'approvisionnement — médicaments, vaccins, intrants, équipements — par la traçabilité de chaque mouvement de stock. Il réconcilie les entrées, sorties et soldes en mode dégradé comme en ligne.

Service de catégorie *applicatif*, il [sert la formation sanitaire](../parties-prenantes/pp-06.md), [réalise la capacité « Chaîne logistique et traçabilité »](../capacites/cap-int-10.md), [accède à l'objet de données logistique](../objets-de-donnees/do-03.md) et [met en œuvre le chapitre ART-10 (logistique)](../chapitres/art-10.md). Il s'appuie sur le [composant de chaîne logistique](../composants/cmp-23.md).

## Catégorie

applicatif.

## Exposition

Sert la partie prenante [PP-06](../parties-prenantes/pp-06.md) et crée de la valeur pour son bénéficiaire.

## Réalisation

Réalisé par les capacités [CAP-INT-10](../capacites/cap-int-10.md) et mis en œuvre via les chapitres [ART-10](../chapitres/art-10.md).
