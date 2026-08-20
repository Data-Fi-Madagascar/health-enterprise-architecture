---
title: Capabilités critiques et architecture runway
id: capabilities-runway
domain: 03_capabilities
version: "1.0.0"
status: draft
last_reviewed: 2026-07-03
owner: Comité National d'Architecture Santé Numérique
tags: [capabilités, runway, critiques]
---

# Capabilités critiques et architecture runway

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

## Distinction

- Une capabilité est **critique** lorsque son delta de maturité est élevé et sa contribution importe dans un flux de valeur.
- Une capabilité relève de l'**architecture runway** lorsqu'elle constitue un socle transversal sans lequel plusieurs flux ou capabilités ne peuvent produire durablement leurs bénéfices.

Toutes les capabilités runway sont critiques, mais toutes les capabilités critiques ne sont pas nécessairement des capabilités runway.

## Capabilités critiques métier

| Capabilité | Criticité |
|------------|-----------|
| CAP-03 : Qualité, sécurité et amélioration continue | Critique pour VS-01 et VS-04 |
| CAP-07 : Protection financière et CSU | Prioritaire pour VS-03 |
| CAP-02 : Parcours patient, référence et contre-référence | Prioritaire pour la continuité des soins dans VS-01 |

## Capabilités d'architecture runway

Quatre capabilités constituent le socle commun dont le développement doit être engagé en priorité, car elles conditionnent la réussite de nombreuses initiatives.

### CAP-13 : Système d'information sanitaire, données et recherche

Produit, intègre, contrôle, analyse et utilise les données nécessaires à la décision, la recherche, la redevabilité et l'amélioration continue.

Son absence bloque : le pilotage de la performance, le suivi des bénéfices, l'analyse des inégalités d'accès et de qualité, la surveillance consolidée et la redevabilité.

### CAP-14 : Interopérabilité, référentiels nationaux et infrastructure numérique partagée

C'est la capabilité la plus structurante pour la cohérence du système d'information sanitaire : échange de données, référentiels nationaux, identité, terminologies, registres et mécanismes d'intégration.

Son absence bloque : CAP-01 (dossier patient en silo), CAP-05 (surveillance fragmentée), CAP-07 (droits non vérifiables), CAP-13 (entrepôt incomplet).

### CAP-15 : Cybersécurité, confidentialité et gouvernance des données personnelles

Conditionne la confiance des patients, agents, partenaires et institutions dans le système d'information sanitaire.

Son absence bloque : CAP-01 (partage du dossier exige une protection forte), CAP-07 (données de vulnérabilité sensibles), CAP-13 (règles d'accès claires), CAP-14 (échange sécurisé et auditable). Sans elle, l'interopérabilité devient un risque au lieu d'être un levier de valeur.

### CAP-16 : Gestion du portefeuille d'initiatives numériques

Gouverne les initiatives selon leur contribution réelle aux flux de valeur, et non selon la seule disponibilité de fonds.

Son absence bloque : la priorisation cohérente, l'identification des doublons, le suivi des bénéfices, la redevabilité des responsables, l'arbitrage entre initiatives, et l'arrêt ou la réorientation des initiatives non performantes.

## Liens

- Capabilités
- Maturité
- Gouvernance

## Références

- **matrice de lecture** : Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
- **Capabilités** : Capabilités du système de santé (`00_caesn/03_capabilities/index.md`)
- **Maturité** : Évaluation de la maturité des capabilités (`00_caesn/03_capabilities/maturity.md`)
- **Gouvernance** : Gouvernance du cadre d'architecture (`00_caesn/07_governance/index.md`)
