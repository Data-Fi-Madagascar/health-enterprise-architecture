---
title: Cycle de vie des données
id: data-lifecycle
domain: data
version: "0.1.0"
status: draft
last_reviewed: 2026-07-03
owner: Cellule du Système d'Information Sanitaire
tags: [données, cycle-de-vie]
---

# Cycle de vie des données

Chaque donnée de santé doit être gouvernée tout au long de son cycle de vie.

| Étape | Description | Exigence d'architecture |
|-------|-------------|-------------------------|
| Création / collecte | La donnée est produite à la source : formation sanitaire, communauté, laboratoire, programme, chaîne logistique, système financier | Collecter uniquement les données nécessaires, avec définitions claires et référentiels communs |
| Validation | La donnée est contrôlée pour détecter erreurs, incohérences, doublons, valeurs manquantes | Intégrer contrôles automatiques et validations métier |
| Référencement | La donnée est reliée aux référentiels nationaux (FOSA, géographie, patient, agent, produit, indicateur) | Utiliser des identifiants nationaux stables |
| Transmission / échange | La donnée circule entre systèmes ou niveaux | Utiliser des mécanismes d'échange homologués et sécurisés |
| Stockage | La donnée est conservée dans un système, registre, entrepôt ou archive | Appliquer des règles de sécurité, disponibilité, sauvegarde, conservation |
| Analyse | La donnée est transformée en information utile | Garantir qualité, traçabilité et documentation des transformations |
| Utilisation | La donnée soutient une décision, une action, une allocation ou une amélioration | Relier tableaux de bord et rapports à des processus réels de décision |
| Archivage / suppression | La donnée est conservée, stockée, anonymisée, archivée ou supprimée | Définir des règles de conservation, d'anonymisation et de suppression |

## Liens

- [Principes de l'architecture des données](./principles.md)
- [Gouvernance des données](./governance.md)
- [Domaines de données](./domains.md)