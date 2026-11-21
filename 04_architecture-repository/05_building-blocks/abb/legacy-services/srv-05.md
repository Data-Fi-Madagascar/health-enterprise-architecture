---
domain: legacy-services
id: SRV-05
type: service
title: Service logistique (LMIS)
status: draft
owner: Ministère de la Santé Publique
version: "0.1"
envelope: 02_artsn/06_services/srv-05-service-logistique-lmis.md
categorie: applicatif
serves: ["PP-06"]
realizes: ["ABB-ECHANGE-LOGISTIQUE-LMIS"]
accesses: ["DO-11", "DO-12", "DO-13"]
implements: ["ART-10"]
related: ["PP-06", "ABB-ECHANGE-LOGISTIQUE-LMIS", "ABB-AUDIT-PROVENANCE", "DO-11", "DO-12", "DO-13", "ART-10", "CMP-23"]
tags: ["artsn", "service", "srv-05", "patterns"]
---
# Service logistique (LMIS)

Le service logistique (LMIS) assure la continuité de la chaîne d'approvisionnement — médicaments, vaccins, intrants, équipements — par la traçabilité de chaque mouvement de stock. Il réconcilie les entrées, sorties et soldes en mode dégradé comme en ligne.

Service de catégorie *applicatif*, il [sert la formation sanitaire](../../../02_architecture-elements/motivation/stakeholders/pp-06.md), [réalise le bloc d'échange logistique LMIS](../abb-echange-logistique-lmis.md), accède aux produits, lots et stocks, et [met en œuvre le chapitre ART-10 (logistique)](../../../04_patterns/artsn-rules/art-10.md). Il s'appuie sur le [composant de chaîne logistique](../legacy-components/cmp-23.md). L'audit et la provenance restent une exigence transverse, sans constituer la responsabilité principale du service.

## Catégorie

applicatif.

## Exposition

Sert la partie prenante [PP-06](../../../02_architecture-elements/motivation/stakeholders/pp-06.md) et crée de la valeur pour son bénéficiaire.

## Réalisation

Réalisé par [ABB-ECHANGE-LOGISTIQUE-LMIS](../abb-echange-logistique-lmis.md) et mis en œuvre via le chapitre [ART-10](../../../04_patterns/artsn-rules/art-10.md).
