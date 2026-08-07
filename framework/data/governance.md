---
title: Gouvernance, qualité et protection des données
id: data-governance
domain: data
version: "0.1.0"
status: draft
last_reviewed: 2026-07-03
owner: Cellule du Système d'Information Sanitaire
tags: [données, gouvernance, qualité, protection]
---

# Gouvernance, qualité et protection des données

## Gouvernance des données

La gouvernance garantit que les données sont fiables, protégées, accessibles aux autorisés et utilisées pour produire de la valeur. Elle définit les responsabilités, règles et mécanismes. Elle est reliée à la gouvernance globale du cadre : le Comité National statue sur les règles structurantes d'architecture des données, tandis que les responsables métier et de capabilités veillent à leur application.

## Qualité des données

La qualité est une condition de l'utilité des données. Dimensions retenues :

| Dimension | Signification |
|-----------|----------------|
| Complétude | Les données attendues sont effectivement renseignées |
| Exactitude | Les données reflètent correctement la réalité observée |
| Cohérence | Les données sont compatibles entre systèmes, périodes, régions, programmes |
| Promptitude | Les données sont disponibles dans les délais nécessaires |
| Unicité | Les doublons sont évités ou maîtrisés |
| Traçabilité | L'origine, les modifications et les transformations sont retraçables |
| Utilisabilité | Les données sont compréhensibles et exploitables |

Chaque système intègre des mécanismes de contrôle : contrôles à la saisie, validation métier, détection des doublons, règles de cohérence, tableaux de qualité, retour aux producteurs, revues périodiques, correction documentée.

## Accès, partage et échange

L'accès obéit au principe du **besoin légitime d'accès** dans le cadre d'une finalité définie. Les échanges doivent utiliser les référentiels nationaux, passer par des mécanismes homologués, être documentés dans des contrats d'interface, sécurisés et journalisés, et respecter la confidentialité. Les échanges informels ou bilatéraux sont progressivement remplacés par des échanges gouvernés.

## Protection des données personnelles de santé

Exigences retenues :

| Exigence | Description |
|----------|-------------|
| Finalité définie | Toute collecte/utilisation liée à une finalité explicite |
| Minimisation | Seules les données nécessaires sont collectées |
| Contrôle des accès | Accès selon rôles, responsabilités et besoins réels |
| Traçabilité | Accès, modifications, échanges et extractions journalisés |
| Confidentialité | Données nominatives protégées contre les accès non autorisés |
| Consentement / base légale | Modalités adaptées au contexte sanitaire et au cadre juridique |
| Anonymisation / pseudonymisation | Pour l'analyse, la recherche ou la publication |
| Gestion des incidents | Détection, documentation, traitement et remontée selon une procédure |

Risques particuliers au contexte : hébergement hors du territoire sans garanties, multiplicité des identifiants programmatiques, consentement numérique difficile en zone rurale, risque de réidentification en faible population, accès excessifs aux données sensibles. Pour chacun, des mesures sont définies (politique de souveraineté, référentiel national des bénéficiaires, modèles de consentement adaptés, seuils d'agrégation, rôles d'accès et revues des habilitations).

## Règles minimales pour toute initiative

Toute initiative produisant, collectant, échangeant ou exploitant des données de santé doit :

1. identifier les domaines de données concernés ;
2. démontrer le lien avec un flux de valeur et une capacité ;
3. utiliser les référentiels nationaux applicables ;
4. définir le propriétaire métier ;
5. documenter les données collectées et leurs définitions ;
6. préciser les règles de qualité ;
7. définir les droits d'accès et profils utilisateurs ;
8. prévoir la protection des données personnelles ;
9. décrire les échanges avec les autres systèmes ;
10. garantir la portabilité et la restitution des données ;
11. prévoir l'intégration avec l'entrepôt national si usage analytique requis ;
12. relier les tableaux de bord à un processus réel de décision ;
13. définir les indicateurs de mesure de la valeur produite.

Une initiative qui ne respecte pas ces règles n'est pas conforme au cadre.

## Liens

- [Entrepôt national de données](../data/index.md)
- [Couche décisionnelle](../application/layers.md)
- [Référentiels nationaux](./referentials.md)
- [Principes de l'architecture des données](./principles.md)