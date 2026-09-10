---

domain: services
id: SRV-02
type: service
title: Service de dossier patient
status: draft
owner: Ministère de la Santé Publique
version: "0.1"
envelope: 02_artsn/06_services/srv-02-service-de-dossier-patient.md
categorie: applicatif
serves: ["PP-05"]
realizes: ["CAP-01"]
accesses: ["BO-01", "DO-01"]
implements: ["ART-2"]
related: ["PP-05", "CAP-01", "BO-01", "DO-01", "ART-2", "CMP-09"]
tags: ["artsn", "service", "srv-02", "patterns"]
---


# Service de dossier patient

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

Le service de dossier patient centralise et restitue l'historique clinique d'un bénéficiaire, garantissant sa continuité entre les structures. Il est le point de convergence des soins prodigués sur le terrain.

Service de catégorie *applicatif*, il [sert l'agent de santé](../../04_architecture-repository/02_architecture-elements/motivation/stakeholders/pp-05.md), [réalise la capacité « Offre de soins et continuité »](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-01.md), [accède à l'objet métier Patient](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-01.md) et à l'[objet de données du dossier](../../04_architecture-repository/02_architecture-elements/data/data-objects/do-01.md). Il [met en œuvre le chapitre ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md) et s'appuie sur le [composant de dossiers](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-09.md).

## Catégorie

applicatif.

## Exposition

Sert la partie prenante [PP-05](../../04_architecture-repository/02_architecture-elements/motivation/stakeholders/pp-05.md) et crée de la valeur pour son bénéficiaire.

## Réalisation

Réalisé par les capacités [CAP-01](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-01.md) et mis en œuvre via les chapitres [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md).

<!-- END:GENERATED -->
