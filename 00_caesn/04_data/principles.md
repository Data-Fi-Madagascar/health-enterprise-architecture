---
title: Principes de l'architecture des données
id: data-principles
domain: 04_data
version: "0.1.0"
status: draft
last_reviewed: 2026-07-03
owner: Cellule du Système d'Information Sanitaire
tags: [données, principes]
---

# Principes de l'architecture des données

## Pour qui lire ce document

**Niveau :** niveau 1 — Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ○ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../reading-matrix.md).

Les principes d'architecture transversaux s'appliquent à toutes les données du système d'information sanitaire. Ils se traduisent en règles spécifiques ci-dessous.

| Code | Principe | Signification | Implications |
|------|----------|---------------|--------------|
| DA-01 | Les données de santé sont un actif stratégique national | Les données produites par le système de santé doivent être gouvernées comme un bien public national | Leur gouvernance relève du Ministère de la Santé Publique ; aucun partenaire ne peut les contrôler exclusivement |
| DA-02 | Une donnée doit être collectée une seule fois et réutilisée plusieurs fois | La collecte répétée d'une même donnée crée de la charge, de l'incohérence et de la fragmentation | Toute nouvelle collecte vérifie l'existence de données déjà disponibles dans les systèmes ou référentiels nationaux |
| DA-03 | Les référentiels nationaux sont les sources de vérité | Les données clés doivent être rattachées à des référentiels communs | Les systèmes utilisent les référentiels nationaux (FOSA, géographie, indicateurs, agents, produits, bénéficiaires) au lieu de créer leurs propres listes locales |
| DA-04 | Les données opérationnelles et analytiques doivent être distinguées | Les systèmes de prestation ne doivent pas être confondus avec les systèmes de reporting | Les données circulent des systèmes opérationnels vers les systèmes analytiques selon des règles d'intégration, qualité et sécurité |
| DA-05 | La qualité des données est une responsabilité partagée | La qualité ne peut être imposée uniquement par le niveau central | Les systèmes intègrent des contrôles, des retours aux producteurs et des revues régulières |
| DA-06 | Les données doivent être utilisées pour des décisions réelles | Un tableau de bord n'a de valeur que s'il soutient un processus de décision effectif | Toute production de rapports ou visualisations est liée à une revue, un arbitrage, une allocation de ressources ou une action d'amélioration |
| DA-07 | Les données personnelles de santé doivent être protégées dès la conception | La confiance dans le système dépend de la protection des données sensibles | Confidentialité, gestion des accès, traçabilité, consentement et limitation des usages sont intégrés dès la conception |
| DA-08 | Les échanges de données doivent passer par des mécanismes gouvernés | Les échanges directs, informels ou propriétaires augmentent les risques de fragmentation et de fuite | Les échanges utilisent la couche nationale d'échange ou les mécanismes homologués par l'architecture de référence technique |

## Liens

- [Principes d'architecture](../02_principles/index.md)
- [Domaines de données](./domains.md)
- [Gouvernance des données](./governance.md)