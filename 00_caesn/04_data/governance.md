---

title: Gouvernance, qualité et protection des données
id: data-governance
domain: 04_data
version: "1.0.0"
status: draft
last_reviewed: 2026-07-03
owner: Cellule du Système d'Information Sanitaire
tags: ["données", "gouvernance", "qualité", "protection"]
---

# Gouvernance, qualité et protection des données

## Pour qui lire ce document

**Niveau :** niveau 1 : Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ○ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

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

Le cadre de protection des données personnelles de santé s'appuie sur la **Loi n°2014-038** sur la protection des données à caractère personnel (promulguée le 9 janvier 2015, décret d'application 2023-1541) et sur la **Convention de Malabo** (ratifiée par la loi 2024-004). La loi institue la Commission Malagasy de l'Informatique et des Libertés (CMIL) comme autorité indépendante chargée de veiller au respect des principes de protection.

Exigences retenues, alignées sur les principes de la loi 2014-038 :

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

- Entrepôt national de données
- Couche décisionnelle
- Référentiels nationaux
- Principes de l'architecture des données

## Références

- **matrice de lecture** : Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
- **Entrepôt national de données** : Architecture des données et de l'information sanitaire (`00_caesn/04_data/index.md`)
- **Couche décisionnelle** : Paysage applicatif cible (`00_caesn/05_application/layers.md`)
- **Référentiels nationaux** : Référentiels nationaux (`00_caesn/04_data/referentials.md`)
- **Principes de l'architecture des données** : Principes de l'architecture des données (`00_caesn/04_data/principles.md`)
