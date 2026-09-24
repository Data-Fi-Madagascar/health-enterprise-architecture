---

domain: services
id: SRV-01
type: service
title: Service d'identité du bénéficiaire
status: draft
owner: Ministère de la Santé Publique
version: "0.1"
envelope: 02_artsn/06_services/srv-01-service-d-identit-du-b-n-ficiaire.md
categorie: business
serves: ["PP-01"]
realizes: ["CAP-17"]
accesses: ["BO-01"]
implements: ["ART-2"]
related: ["PP-01", "CAP-17", "BO-01", "ART-2", "CMP-08"]
tags: ["artsn", "service", "srv-01", "patterns"]
---


# Service d'identité du bénéficiaire

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

Le service d'identité du bénéficiaire permet de résoudre et d'authentifier l'identité d'une personne de façon unique et fiable à travers tout le système. C'est le socle de la confiance : sans identité résolue, aucune donnée ne peut être attribuée à la bonne personne.

Service de catégorie *business*, il [sert le patient et usager](../../04_architecture-repository/02_architecture-elements/motivation/stakeholders/pp-01.md), [réalise la capacité « Engagement patient et identité numérique »](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-17.md) et [accède à l'objet métier Patient](../../04_architecture-repository/02_architecture-elements/business/business-objects/bo-01.md). Il [met en œuvre le chapitre ART-2 (identité)](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md) et s'appuie sur le [composant d'identité](../../04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-08.md).

## Catégorie

business.

## Exposition

Sert la partie prenante [PP-01](../../04_architecture-repository/02_architecture-elements/motivation/stakeholders/pp-01.md) et crée de la valeur pour son bénéficiaire.

## Réalisation

Réalisé par les capacités [CAP-17](../../04_architecture-repository/02_architecture-elements/strategy/capabilities/cap-17.md) et mis en œuvre via les chapitres [ART-2](../../04_architecture-repository/04_patterns/artsn-rules/art-2.md).

<!-- END:GENERATED -->
