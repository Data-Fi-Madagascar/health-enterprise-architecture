---
domain: legacy-services
id: SRV-04
type: service
title: Service d'échange inter-systèmes
status: draft
owner: Ministère de la Santé Publique
version: "0.1"
envelope: 02_artsn/06_services/srv-04-service-d-change-inter-syst-mes.md
categorie: technologique
serves: ["PP-10"]
realizes: ["ABB-CONFIANCE-AUTORISATION"]
accesses: ["DO-03"]
implements: ["ART-9"]
related: ["PP-10", "ABB-CONFIANCE-AUTORISATION", "DO-03", "ART-9", "CMP-11"]
tags: ["artsn", "service", "srv-04", "patterns"]
---
# Service d'échange inter-systèmes

Le service d'échange inter-systèmes assure le transport et la médiation des messages entre applications, au sein du système comme avec les partenaires externes (X-Road, GDHCN). Il est le garant de l'interopérabilité technique.

Service de catégorie *technologique*, il [sert l'équipe technique DEPSI / SIS](../../../02_architecture-elements/motivation/stakeholders/pp-10.md), [réalise la capacité « Interopérabilité et échanges »](../abb-confiance-autorisation.md), [accède à l'objet de données d'échange](../../../02_architecture-elements/data/data-objects/do-03.md) et [met en œuvre le chapitre ART-9 (échange)](../../../04_patterns/artsn-rules/art-9.md). Il s'appuie sur le [composant de médiation / transport](../legacy-components/cmp-11.md).

## Catégorie

technologique.

## Exposition

Sert la partie prenante [PP-10](../../../02_architecture-elements/motivation/stakeholders/pp-10.md) et crée de la valeur pour son bénéficiaire.

## Réalisation

Réalisé par les capacités [ABB-CONFIANCE-AUTORISATION](../abb-confiance-autorisation.md) et mis en œuvre via les chapitres [ART-9](../../../04_patterns/artsn-rules/art-9.md).
