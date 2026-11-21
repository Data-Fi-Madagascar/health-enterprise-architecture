---
domain: legacy-components
id: CMP-03
type: composant-applicatif
categorie: applicatif
niveau: "1"
title: Entrepôt Lakehouse & Projections analytiques (pipeline ETL, Lakehouse, projections)
status: active
owner: DEPSI
version: "0.0.1"
envelope: 02_artsn/05_cartographie/composants.md
maps_to: ["ABB-EXPOSITION-DONNEES-ANALYTIQUES", "ABB-RECONCILIATION-DONNEES"]
implements: ["ART-6", "ART-9"]
applies_to: ["PRC-09", "PRC-11"]
accesses: ["DO-16", "DO-17", "DO-25", "DO-28"]
related: ["ENF-5", "CAP-13", "CAP-16", "VS-04"]
tags: ["artsn", "niveau-1", "composant-applicatif", "CMP-03", "couche-5"]
---
# Entrepôt Lakehouse & Projections analytiques

**Contenu normatif.** Ce composant assure le stockage analytique central (Lakehouse) en recevant les flux ETL depuis la Couche 4. Il exécute les projections tabulaires, la réconciliation du Grand Livre ([ART-9: Garanties transactionnelles fortes](../../../04_patterns/artsn-rules/art-9.md)) et alimente les tableaux de bord ([CMP-01: Tableaux de bord & Portails nationaux (performance, CSU, ressources, veille)](cmp-01.md)). La séparation stricte CQRS ([ART-6: Analytique et restitution](../../../04_patterns/artsn-rules/art-6.md)) interdit tout traitement transactionnel.

**Discipline de mise en œuvre.** Il garantit l'intégrité analytique ([ENF-5: Coordination des processus complexes décentralisés et asynchrones](../../../03_requirements/enf-5.md)) et l'irréversibilité du masquage des identités. Toute analyse officielle passe par cet entrepôt.

- **Rattachement** : [ART-6](../../../04_patterns/artsn-rules/art-6.md) (CQRS), [ART-9](../../../04_patterns/artsn-rules/art-9.md) (Grand Livre), [ABB-EXPOSITION-DONNEES-ANALYTIQUES: Accès et exposition des données analytiques](../abb-exposition-donnees-analytiques.md), [ABB-RECONCILIATION-DONNEES: Qualité et réconciliation](../abb-reconciliation-donnees.md).
- **Processus soutenus** : [PRC-09: Remboursement et régulation des mécanismes](../../../02_architecture-elements/business/processes/prc-09.md) (remboursement), [PRC-11: Suivi et pilotage de la performance](../../../02_architecture-elements/business/processes/prc-11.md) (pilotage).
- **Données portées** : [DO-16 : Facturation](../../../02_architecture-elements/data/data-objects/do-16.md), [DO-17 : Vérification d'éligibilité](../../../02_architecture-elements/data/data-objects/do-17.md), [DO-25 : Indicateur sanitaire](../../../02_architecture-elements/data/data-objects/do-25.md), [DO-28 : Tableau de bord](../../../02_architecture-elements/data/data-objects/do-28.md)
- **Statut : Stable.**
