---
domain: sbb
id: CMP-04
type: composant-applicatif
categorie: applicatif
niveau: "1"
title: Moteur analytique & IA (IA prédictive, routeur alertes, Grand Livre)
status: active
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/05_cartographie/composants.md
maps_to: ["ABB-EXPOSITION-DONNEES-ANALYTIQUES", "ABB-AUDIT-PROVENANCE"]
implements: ["ART-5", "ART-9"]
applies_to: ["PRC-05", "PRC-09"]
accesses: ["DO-16", "DO-17", "DO-18", "DO-19", "DO-20"]
related: ["ENF-2", "ENF-5", "CAP-13", "CAP-15", "VS-02", "VS-04"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-04", "couche-5"]
---
# Moteur analytique & IA

**Contenu normatif.** Ce composant exécute les modèles prédictifs (IA), le routeur d'escalade et d'alertes ([ART-5: Cohérence et qualité des données](../../patterns/artsn-rules/art-5.md)) et la réconciliation analytique du Grand Livre ([ART-9: Garanties transactionnelles fortes](../../patterns/artsn-rules/art-9.md)). Il consomme l'entrepôt Lakehouse ([CMP-03: Entrepôt Lakehouse & Projections analytiques (pipeline ETL, Lakehouse, projections)](cmp-03.md)) et alimente le centre de commande ([CMP-02: Centre de commande & Crises intersectorielles (alertes, crises, veille)](cmp-02.md)) ainsi que la facturation ([CMP-10: Registre des terminologies](cmp-10.md)).

**Discipline de mise en œuvre.** Il sépare l'inférence analytique du stockage et garantit la traçabilité des modèles (versionnage, données d'entraînement) ainsi que l'audit des décisions automatisées ([ENF-2: Intégrité des flux et traçabilité des valeurs](../../../02_requirements/enf-2.md), [ENF-5: Coordination des processus complexes décentralisés et asynchrones](../../../02_requirements/enf-5.md)).

- **Rattachement** : [ART-5](../../patterns/artsn-rules/art-5.md) (alertes), [ART-9](../../patterns/artsn-rules/art-9.md) (Grand Livre), [ABB-EXPOSITION-DONNEES-ANALYTIQUES: Accès et exposition des données analytiques](../abb/abb-exposition-donnees-analytiques.md), [ABB-AUDIT-PROVENANCE: Provenance, audit et traçabilité](../abb/abb-audit-provenance.md).
- **Processus soutenus** : [PRC-09: Remboursement et régulation des mécanismes](../../../03_business-architecture/business/processes/prc-09.md) (remboursement), [PRC-05: Alerte, investigation et riposte](../../../03_business-architecture/business/processes/prc-05.md) (alerte/riposte).
- **Données portées** : [DO-16 : Facturation et demande de remboursement](../../../04_data-architecture/data-objects/do-16.md), [DO-17 : Demande et preuve de vérification d'éligibilité](../../../04_data-architecture/data-objects/do-17.md), [DO-18 : Signal, notification et alerte sanitaires](../../../04_data-architecture/data-objects/do-18.md), [DO-19 : Foyer épidémique](../../../04_data-architecture/data-objects/do-19.md), [DO-20 : Investigation épidémiologique](../../../04_data-architecture/data-objects/do-20.md)
- **Statut : Stable.**
