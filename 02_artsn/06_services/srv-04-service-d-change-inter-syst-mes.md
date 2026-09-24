---

domain: services
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

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

Le service d'échange inter-systèmes assure le transport et la médiation des messages entre applications, au sein du système comme avec les partenaires externes (X-Road, GDHCN). Il est le garant de l'interopérabilité technique.

Service de catégorie *technologique*, il [sert l'équipe technique DEPSI / SIS](../../04_architecture-repository/02_architecture-elements/motivation/stakeholders/pp-10.md), [réalise le bloc d'échange et médiation inter-systèmes](../../04_architecture-repository/05_building-blocks/abb/abb-echange-mediation.md), transporte les charges utiles métier et met en œuvre les chapitres [ART-1](../../04_architecture-repository/04_patterns/artsn-rules/art-1.md), [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md) et [ART-7](../../04_architecture-repository/04_patterns/artsn-rules/art-7.md). Il s'appuie sur le [composant d'intégration et médiation](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-06.md).

## Catégorie

technologique.

## Exposition

Sert la partie prenante [PP-10](../../04_architecture-repository/02_architecture-elements/motivation/stakeholders/pp-10.md) et crée de la valeur pour son bénéficiaire.

## Réalisation

Réalisé par [ABB-ECHANGE-MEDIATION](../../04_architecture-repository/05_building-blocks/abb/abb-echange-mediation.md) et mis en œuvre via les chapitres [ART-1](../../04_architecture-repository/04_patterns/artsn-rules/art-1.md), [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md) et [ART-7](../../04_architecture-repository/04_patterns/artsn-rules/art-7.md).

<!-- END:GENERATED -->
