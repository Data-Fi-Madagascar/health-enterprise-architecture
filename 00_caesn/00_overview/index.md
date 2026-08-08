---
title: Cadre d'Architecture d'Entreprise de la Santé Numérique
id: CAESN
domain: 00_overview
version: "0.1.0"
status: draft
last_reviewed: 2026-07-03
owner: Ministère de la Santé Publique
tags: [cadre, gouvernance, santé-numérique, madagascar]
---

# Cadre d'Architecture d'Entreprise de la Santé Numérique (CAESN)

## Objet

Le présent cadre fixe les principes, les méthodes et les mécanismes de gouvernance qui doivent guider la planification, le financement, le déploiement et le suivi de toute initiative numérique dans le secteur santé à Madagascar.

Son objet est triple :

1. **Définir la valeur** que le système de santé doit produire pour la population et la traduire en flux opérationnels mesurables.
2. **Identifier les capabilités** que le système de santé doit développer pour produire cette valeur, évaluer leur maturité actuelle et définir les cibles.
3. **Établir les règles de gouvernance** pour s'assurer que les investissements numériques contribuent aux priorités nationales, produisent des bénéfices mesurables et s'inscrivent dans une logique de soutenabilité.

## Portée

Le cadre couvre l'ensemble des initiatives numériques du secteur santé à Madagascar, portées par le Ministère de la Santé Publique, ses directions techniques, les régions et districts sanitaires, ou les partenaires techniques et financiers.

Il s'applique aux systèmes d'information sanitaire, plateformes de données, applications de gestion, outils de terrain, infrastructures technologiques partagées et référentiels nationaux.

Il ne couvre pas les équipements biomédicaux ni les infrastructures physiques des formations sanitaires, sauf dans leur interface avec les systèmes d'information.

## Ce que ce cadre n'est pas

- **Un plan de projet** : il ne décrit pas les étapes de mise en œuvre d'une solution particulière.
- **Un catalogue de logiciels** : il ne recommande pas de produits ou d'éditeurs. Les choix d'implémentation relèvent de l'Architecture de Référence Technique.
- **Un document réservé aux informaticiens** : il s'adresse d'abord aux décideurs, responsables de programmes et partenaires.

## Hiérarchie documentaire

| Niveau | Document | Destinataires |
|--------|----------|---------------|
| 1 | Cadre d'Architecture d'Entreprise (ce document) : valeur, capabilités, principes, gouvernance | Décideurs, directions métiers, partenaires |
| 2 | Cadre National d'Interopérabilité : standards d'échange, référentiels, profils | DEPSI, architectes, intégrateurs |
| 3 | Architecture de Référence Technique : standards, solutions retenues, règles d'homologation | DEPSI, architectes, intégrateurs |
| 4 | Profils techniques d'implémentation (par initiative) : configurations, API, contrats d'interfaces | Développeurs, fournisseurs, équipes techniques |

## Structure du référentiel

Ce dépôt implémente le cadre comme **architecture as code** : chaque concept est documenté dans un fichier Markdown structuré (YAML frontmatter + contenu), versionné et référençable.

| Domaine | Contenu |
|---------|---------|
| [Fondements](./foundations.md) | Ancrage stratégique et normatif (PDSS, SNSD, PSRSIS, OMS DPI-H, OpenHIE, GovStack) |
| [Modèle de valeur](./value-model.md) | Bénéficiaires, dimensions de valeur |
| [Flux de valeur](../01_value-streams/) | Les 4 flux de valeur nationaux (VS-01 à VS-04) |
| [Principes](../02_principles/) | Principes d'architecture transversaux (PA) et principes de domaine (PD) |
| [Capabilités](../03_capabilities/) | Catalogue CAP-01 à CAP-16, maturité, architecture runway |
| [Données](../04_data/) | Principes DA, domaines de données, référentiels, gouvernance |
| [Application](../05_application/) | Principes AA, paysage applicatif cible, services partagés |
| [Portefeuille](../06_portfolio/) | Registre des initiatives, fiche initiative, priorisation |
| [Gouvernance](../07_governance/) | Comité National, Bureau de Réalisation de la Valeur, responsabilités |
| [Décisions](../08_decisions/) | Architecture Decision Records (ADR) |
| [Normes](../09_standards/) | Standards et règles d'homologation |
| [Annexes](../10_annexes/) | Matrice de lecture, glossaire |
