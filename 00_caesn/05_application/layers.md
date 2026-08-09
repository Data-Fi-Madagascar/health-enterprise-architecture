---
title: Paysage applicatif cible (six couches)
id: application-target-layers
domain: 05_application
version: "0.1.0"
status: draft
last_reviewed: 2026-07-03
owner: Direction des Systèmes d'Information
tags: [applications, couches, paysage, cible]
---

# Paysage applicatif cible

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

Le paysage applicatif national est organisé en six couches complémentaires :

```
Utilisateurs et points de service
        ↓
Applications métier
        ↓
Plateformes et services partagés
        ↓
Couche nationale d'échange
        ↓
Données, analyse et pilotage
        ↓
Infrastructure, sécurité et exploitation
```

## 1. Utilisateurs et points de service

Lieux et acteurs qui utilisent les services : patients et ménages, agents de santé communautaire, formations sanitaires, districts, régions, directions centrales, programmes, partenaires autorisés, décideurs. Les applications sont conçues à partir des besoins réels de ces utilisateurs.

## 2. Applications métier

Applications directement liées aux processus de santé : soins et parcours patient, santé communautaire, surveillance épidémiologique, vaccination et prévention, protection financière, logistique, ressources humaines, qualité des soins, planification et coordination. Voir [domaines applicatifs](./application-domains.md).

## 3. Plateformes et services partagés

Composants nationaux réutilisables : référentiels (FOSA, géographie, agents, produits, indicateurs), registre des bénéficiaires, services d'identité, d'authentification, d'accès, de notification, de consentement, catalogue des API, registre des initiatives. Voir [services partagés](./shared-services.md).

## 4. Couche nationale d'échange

Assure la médiation entre systèmes, la transformation des formats, le routage, la journalisation, l'application des règles de sécurité, la gestion des contrats d'interface et l'intégration avec DPI-H, OpenHIE et GovStack.

## 5. Données, analyse et pilotage

Composants d'usage décisionnel : entrepôt national, tableaux de bord, outils d'analyse, rapports nationaux, suivi des indicateurs et des bénéfices, revues de performance. Voir [entrepôt](../04_data/governance.md).

## 6. Infrastructure, sécurité et exploitation

Soutien de l'ensemble : hébergement souverain, connectivité différenciée, sauvegarde, cybersécurité, supervision, support, incidents, maintenance, documentation. Les choix relèvent de l'Architecture de Référence Technique ; le cadre fixe les exigences.

## Liens

- [Architecture applicative](./index.md)
- [Référentiels](../04_data/referentials.md)
- [Services partagés](./shared-services.md)