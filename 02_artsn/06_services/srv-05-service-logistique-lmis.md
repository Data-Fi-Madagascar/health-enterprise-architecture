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
realizes: ["ABB-AUDIT-PROVENANCE"]
accesses: ["DO-03"]
implements: ["ART-10"]
related: ["PP-06", "ABB-AUDIT-PROVENANCE", "DO-03", "ART-10", "CMP-23"]
tags: ["artsn", "service", "srv-05", "patterns"]
---


# Service logistique (LMIS)

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

Le service logistique (LMIS) assure la continuité de la chaîne d'approvisionnement — médicaments, vaccins, intrants, équipements — par la traçabilité de chaque mouvement de stock. Il réconcilie les entrées, sorties et soldes en mode dégradé comme en ligne.

Service de catégorie *applicatif*, il [sert la formation sanitaire](../../04_architecture-repository/02_architecture-elements/motivation/stakeholders/pp-06.md), [réalise le bloc d'échange logistique LMIS](../../04_architecture-repository/05_building-blocks/abb/abb-echange-logistique-lmis.md), accède aux produits, lots et stocks, et [met en œuvre le chapitre ART-10 (logistique)](../../04_architecture-repository/04_patterns/artsn-rules/art-10.md). Il s'appuie sur le [composant de chaîne logistique](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-23.md). L'audit et la provenance restent une exigence transverse, sans constituer la responsabilité principale du service.

## Catégorie

applicatif.

## Exposition

Sert la partie prenante [PP-06](../../04_architecture-repository/02_architecture-elements/motivation/stakeholders/pp-06.md) et crée de la valeur pour son bénéficiaire.

## Réalisation

Réalisé par [ABB-ECHANGE-LOGISTIQUE-LMIS](../../04_architecture-repository/05_building-blocks/abb/abb-echange-logistique-lmis.md) et mis en œuvre via le chapitre [ART-10](../../04_architecture-repository/04_patterns/artsn-rules/art-10.md).

<!-- END:GENERATED -->
