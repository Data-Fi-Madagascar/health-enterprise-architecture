---
domain: 10_annexes
id: matrice-tracabilite-vs-cap-prc-cmp
title: Matrice de traçabilité (Flux de valeur, Capacités, Processus, Composants)
version: "1.0.0"
status: draft
owner: DEPSI
tags: ["caesn", "artsn", "tracabilite", "matrice"]
---

# Matrice de traçabilité : Flux de valeur → Capacités → Processus → Composants

Cette matrice dérive directement des champs de relation du référentiel (`applies_to`, `related`, `uses`). Elle matérialise l'articulation ArchiMate : le flux de valeur est **activé** par des capacités, le processus métier les **réalise**, et le composant applicatif les **rend possibles**.

## 1. Synthèse par flux de valeur

| Flux | Intitulé | Capacités activées | Processus métier |
|------|----------|---------------------|-------------------|
| [VS-01](../../referentiel/flux-valeur/vs-01.md) | Accéder à des services de santé essentiels, intégrés, équitables et de qualité | [CAP-01](../../referentiel/capabilites/cap-01.md), [CAP-02](../../referentiel/capabilites/cap-02.md), [CAP-03](../../referentiel/capabilites/cap-03.md), [CAP-04](../../referentiel/capabilites/cap-04.md), [CAP-09](../../referentiel/capabilites/cap-09.md), [CAP-10](../../referentiel/capabilites/cap-10.md), [CAP-11](../../referentiel/capabilites/cap-11.md), [CAP-13](../../referentiel/capabilites/cap-13.md), [CAP-14](../../referentiel/capabilites/cap-14.md), [CAP-15](../../referentiel/capabilites/cap-15.md), [CAP-17](../../referentiel/capabilites/cap-17.md) | [PRC-01](../../referentiel/processus/prc-01.md), [PRC-02](../../referentiel/processus/prc-02.md), [PRC-03](../../referentiel/processus/prc-03.md) |
| [VS-02](../../referentiel/flux-valeur/vs-02.md) | Prévenir, détecter et répondre aux risques sanitaires | [CAP-04](../../referentiel/capabilites/cap-04.md), [CAP-05](../../referentiel/capabilites/cap-05.md), [CAP-06](../../referentiel/capabilites/cap-06.md), [CAP-09](../../referentiel/capabilites/cap-09.md), [CAP-10](../../referentiel/capabilites/cap-10.md), [CAP-11](../../referentiel/capabilites/cap-11.md), [CAP-13](../../referentiel/capabilites/cap-13.md), [CAP-14](../../referentiel/capabilites/cap-14.md), [CAP-15](../../referentiel/capabilites/cap-15.md), [CAP-17](../../referentiel/capabilites/cap-17.md), [CAP-18](../../referentiel/capabilites/cap-18.md) | [PRC-04](../../referentiel/processus/prc-04.md), [PRC-05](../../referentiel/processus/prc-05.md), [PRC-06](../../referentiel/processus/prc-06.md) |
| [VS-03](../../referentiel/flux-valeur/vs-03.md) | Protéger financièrement la population face aux dépenses de santé | [CAP-07](../../referentiel/capabilites/cap-07.md), [CAP-08](../../referentiel/capabilites/cap-08.md), [CAP-12](../../referentiel/capabilites/cap-12.md), [CAP-13](../../referentiel/capabilites/cap-13.md), [CAP-14](../../referentiel/capabilites/cap-14.md), [CAP-15](../../referentiel/capabilites/cap-15.md), [CAP-16](../../referentiel/capabilites/cap-16.md) | [PRC-07](../../referentiel/processus/prc-07.md), [PRC-08](../../referentiel/processus/prc-08.md), [PRC-09](../../referentiel/processus/prc-09.md) |
| [VS-04](../../referentiel/flux-valeur/vs-04.md) | Piloter, coordonner et améliorer la performance du système de santé | [CAP-03](../../referentiel/capabilites/cap-03.md), [CAP-08](../../referentiel/capabilites/cap-08.md), [CAP-09](../../referentiel/capabilites/cap-09.md), [CAP-12](../../referentiel/capabilites/cap-12.md), [CAP-13](../../referentiel/capabilites/cap-13.md), [CAP-14](../../referentiel/capabilites/cap-14.md), [CAP-15](../../referentiel/capabilites/cap-15.md), [CAP-16](../../referentiel/capabilites/cap-16.md) | [PRC-10](../../referentiel/processus/prc-10.md), [PRC-11](../../referentiel/processus/prc-11.md), [PRC-12](../../referentiel/processus/prc-12.md) |

## 2. Chaîne Capacité → Processus → Composant

### [CAP-01](../../referentiel/capabilites/cap-01.md) : Offre de soins et continuité des services

- **Réalisée par** : [PRC-01](../../referentiel/processus/prc-01.md), [PRC-02](../../referentiel/processus/prc-02.md)
- **Servie par les composants** : _(aucun composant)_

### [CAP-02](../../referentiel/capabilites/cap-02.md) : Gestion du parcours patient, référence et contre-référence

- **Réalisée par** : [PRC-01](../../referentiel/processus/prc-01.md), [PRC-03](../../referentiel/processus/prc-03.md)
- **Servie par les composants** : _(aucun composant)_

### [CAP-03](../../referentiel/capabilites/cap-03.md) : Qualité, sécurité des soins et amélioration continue

- **Réalisée par** : [PRC-02](../../referentiel/processus/prc-02.md), [PRC-03](../../referentiel/processus/prc-03.md), [PRC-06](../../referentiel/processus/prc-06.md), [PRC-11](../../referentiel/processus/prc-11.md), [PRC-12](../../referentiel/processus/prc-12.md)
- **Servie par les composants** : [CMP-01](../../referentiel/composants/cmp-01.md), [CMP-02](../../referentiel/composants/cmp-02.md), [CMP-03](../../referentiel/composants/cmp-03.md), [CMP-07](../../referentiel/composants/cmp-07.md), [CMP-11](../../referentiel/composants/cmp-11.md), [CMP-14](../../referentiel/composants/cmp-14.md), [CMP-15](../../referentiel/composants/cmp-15.md), [CMP-17](../../referentiel/composants/cmp-17.md), [CMP-18](../../referentiel/composants/cmp-18.md)

### [CAP-04](../../referentiel/capabilites/cap-04.md) : Santé communautaire et engagement des communautés

- **Réalisée par** : [PRC-01](../../referentiel/processus/prc-01.md), [PRC-03](../../referentiel/processus/prc-03.md), [PRC-04](../../referentiel/processus/prc-04.md), [PRC-05](../../referentiel/processus/prc-05.md)
- **Servie par les composants** : [CMP-02](../../referentiel/composants/cmp-02.md), [CMP-04](../../referentiel/composants/cmp-04.md), [CMP-07](../../referentiel/composants/cmp-07.md), [CMP-08](../../referentiel/composants/cmp-08.md), [CMP-11](../../referentiel/composants/cmp-11.md), [CMP-13](../../referentiel/composants/cmp-13.md), [CMP-14](../../referentiel/composants/cmp-14.md), [CMP-15](../../referentiel/composants/cmp-15.md), [CMP-17](../../referentiel/composants/cmp-17.md), [CMP-18](../../referentiel/composants/cmp-18.md)

### [CAP-05](../../referentiel/capabilites/cap-05.md) : Surveillance épidémiologique, alerte, investigation et riposte

- **Réalisée par** : [PRC-04](../../referentiel/processus/prc-04.md), [PRC-05](../../referentiel/processus/prc-05.md)
- **Servie par les composants** : [CMP-02](../../referentiel/composants/cmp-02.md), [CMP-04](../../referentiel/composants/cmp-04.md), [CMP-07](../../referentiel/composants/cmp-07.md), [CMP-08](../../referentiel/composants/cmp-08.md), [CMP-11](../../referentiel/composants/cmp-11.md), [CMP-13](../../referentiel/composants/cmp-13.md), [CMP-14](../../referentiel/composants/cmp-14.md), [CMP-15](../../referentiel/composants/cmp-15.md), [CMP-17](../../referentiel/composants/cmp-17.md), [CMP-18](../../referentiel/composants/cmp-18.md)

### [CAP-06](../../referentiel/capabilites/cap-06.md) : Vaccination, prévention et promotion de la santé

- **Réalisée par** : [PRC-04](../../referentiel/processus/prc-04.md)
- **Servie par les composants** : [CMP-07](../../referentiel/composants/cmp-07.md), [CMP-08](../../referentiel/composants/cmp-08.md), [CMP-11](../../referentiel/composants/cmp-11.md), [CMP-13](../../referentiel/composants/cmp-13.md), [CMP-15](../../referentiel/composants/cmp-15.md), [CMP-17](../../referentiel/composants/cmp-17.md), [CMP-18](../../referentiel/composants/cmp-18.md)

### [CAP-07](../../referentiel/capabilites/cap-07.md) : Protection financière, couverture santé universelle

- **Réalisée par** : [PRC-07](../../referentiel/processus/prc-07.md), [PRC-08](../../referentiel/processus/prc-08.md), [PRC-09](../../referentiel/processus/prc-09.md)
- **Servie par les composants** : [CMP-03](../../referentiel/composants/cmp-03.md), [CMP-04](../../referentiel/composants/cmp-04.md), [CMP-09](../../referentiel/composants/cmp-09.md), [CMP-10](../../referentiel/composants/cmp-10.md), [CMP-12](../../referentiel/composants/cmp-12.md), [CMP-16](../../referentiel/composants/cmp-16.md)

### [CAP-08](../../referentiel/capabilites/cap-08.md) : Gouvernance institutionnelle, planification, coordination et redevabilité

- **Réalisée par** : [PRC-07](../../referentiel/processus/prc-07.md), [PRC-08](../../referentiel/processus/prc-08.md), [PRC-10](../../referentiel/processus/prc-10.md), [PRC-11](../../referentiel/processus/prc-11.md), [PRC-12](../../referentiel/processus/prc-12.md)
- **Servie par les composants** : [CMP-01](../../referentiel/composants/cmp-01.md), [CMP-02](../../referentiel/composants/cmp-02.md), [CMP-03](../../referentiel/composants/cmp-03.md), [CMP-09](../../referentiel/composants/cmp-09.md), [CMP-10](../../referentiel/composants/cmp-10.md), [CMP-12](../../referentiel/composants/cmp-12.md), [CMP-16](../../referentiel/composants/cmp-16.md)

### [CAP-09](../../referentiel/capabilites/cap-09.md) : Gestion des ressources humaines en santé

- **Réalisée par** : [PRC-02](../../referentiel/processus/prc-02.md), [PRC-10](../../referentiel/processus/prc-10.md)
- **Servie par les composants** : [CMP-01](../../referentiel/composants/cmp-01.md), [CMP-12](../../referentiel/composants/cmp-12.md)

### [CAP-10](../../referentiel/capabilites/cap-10.md) : Gestion des médicaments, vaccins, intrants et chaîne d'approvisionnement

- **Réalisée par** : [PRC-02](../../referentiel/processus/prc-02.md)
- **Servie par les composants** : _(aucun composant)_

### [CAP-11](../../referentiel/capabilites/cap-11.md) : Gestion des infrastructures, équipements et maintenance

- **Réalisée par** : [PRC-01](../../referentiel/processus/prc-01.md), [PRC-02](../../referentiel/processus/prc-02.md)
- **Servie par les composants** : _(aucun composant)_

### [CAP-12](../../referentiel/capabilites/cap-12.md) : Finances publiques, budget et allocation des ressources

- **Réalisée par** : [PRC-08](../../referentiel/processus/prc-08.md), [PRC-09](../../referentiel/processus/prc-09.md), [PRC-10](../../referentiel/processus/prc-10.md)
- **Servie par les composants** : [CMP-01](../../referentiel/composants/cmp-01.md), [CMP-03](../../referentiel/composants/cmp-03.md), [CMP-04](../../referentiel/composants/cmp-04.md), [CMP-09](../../referentiel/composants/cmp-09.md), [CMP-10](../../referentiel/composants/cmp-10.md), [CMP-12](../../referentiel/composants/cmp-12.md), [CMP-16](../../referentiel/composants/cmp-16.md)

### [CAP-13](../../referentiel/capabilites/cap-13.md) : Système d'information sanitaire, données et recherche

- **Réalisée par** : [PRC-01](../../referentiel/processus/prc-01.md), [PRC-02](../../referentiel/processus/prc-02.md), [PRC-03](../../referentiel/processus/prc-03.md), [PRC-04](../../referentiel/processus/prc-04.md), [PRC-05](../../referentiel/processus/prc-05.md), [PRC-06](../../referentiel/processus/prc-06.md), [PRC-07](../../referentiel/processus/prc-07.md), [PRC-08](../../referentiel/processus/prc-08.md), [PRC-09](../../referentiel/processus/prc-09.md), [PRC-10](../../referentiel/processus/prc-10.md), [PRC-11](../../referentiel/processus/prc-11.md), [PRC-12](../../referentiel/processus/prc-12.md)
- **Servie par les composants** : [CMP-01](../../referentiel/composants/cmp-01.md), [CMP-02](../../referentiel/composants/cmp-02.md), [CMP-03](../../referentiel/composants/cmp-03.md), [CMP-04](../../referentiel/composants/cmp-04.md), [CMP-07](../../referentiel/composants/cmp-07.md), [CMP-08](../../referentiel/composants/cmp-08.md), [CMP-09](../../referentiel/composants/cmp-09.md), [CMP-10](../../referentiel/composants/cmp-10.md), [CMP-11](../../referentiel/composants/cmp-11.md), [CMP-12](../../referentiel/composants/cmp-12.md), [CMP-13](../../referentiel/composants/cmp-13.md), [CMP-14](../../referentiel/composants/cmp-14.md), [CMP-15](../../referentiel/composants/cmp-15.md), [CMP-16](../../referentiel/composants/cmp-16.md), [CMP-17](../../referentiel/composants/cmp-17.md), [CMP-18](../../referentiel/composants/cmp-18.md)

### [CAP-14](../../referentiel/capabilites/cap-14.md) : Interopérabilité, référentiels nationaux et infrastructure numérique partagée

- **Réalisée par** : [PRC-01](../../referentiel/processus/prc-01.md), [PRC-02](../../referentiel/processus/prc-02.md), [PRC-03](../../referentiel/processus/prc-03.md), [PRC-04](../../referentiel/processus/prc-04.md), [PRC-05](../../referentiel/processus/prc-05.md), [PRC-06](../../referentiel/processus/prc-06.md), [PRC-07](../../referentiel/processus/prc-07.md), [PRC-09](../../referentiel/processus/prc-09.md), [PRC-11](../../referentiel/processus/prc-11.md), [PRC-12](../../referentiel/processus/prc-12.md)
- **Servie par les composants** : [CMP-01](../../referentiel/composants/cmp-01.md), [CMP-02](../../referentiel/composants/cmp-02.md), [CMP-03](../../referentiel/composants/cmp-03.md), [CMP-04](../../referentiel/composants/cmp-04.md), [CMP-07](../../referentiel/composants/cmp-07.md), [CMP-08](../../referentiel/composants/cmp-08.md), [CMP-09](../../referentiel/composants/cmp-09.md), [CMP-10](../../referentiel/composants/cmp-10.md), [CMP-11](../../referentiel/composants/cmp-11.md), [CMP-12](../../referentiel/composants/cmp-12.md), [CMP-13](../../referentiel/composants/cmp-13.md), [CMP-14](../../referentiel/composants/cmp-14.md), [CMP-15](../../referentiel/composants/cmp-15.md), [CMP-16](../../referentiel/composants/cmp-16.md), [CMP-17](../../referentiel/composants/cmp-17.md), [CMP-18](../../referentiel/composants/cmp-18.md)

### [CAP-15](../../referentiel/capabilites/cap-15.md) : Cybersécurité, confidentialité et gouvernance des données personnelles

- **Réalisée par** : [PRC-01](../../referentiel/processus/prc-01.md), [PRC-02](../../referentiel/processus/prc-02.md), [PRC-03](../../referentiel/processus/prc-03.md), [PRC-04](../../referentiel/processus/prc-04.md), [PRC-05](../../referentiel/processus/prc-05.md), [PRC-06](../../referentiel/processus/prc-06.md), [PRC-07](../../referentiel/processus/prc-07.md), [PRC-08](../../referentiel/processus/prc-08.md), [PRC-09](../../referentiel/processus/prc-09.md), [PRC-10](../../referentiel/processus/prc-10.md), [PRC-11](../../referentiel/processus/prc-11.md), [PRC-12](../../referentiel/processus/prc-12.md)
- **Servie par les composants** : [CMP-01](../../referentiel/composants/cmp-01.md), [CMP-02](../../referentiel/composants/cmp-02.md), [CMP-03](../../referentiel/composants/cmp-03.md), [CMP-04](../../referentiel/composants/cmp-04.md), [CMP-07](../../referentiel/composants/cmp-07.md), [CMP-08](../../referentiel/composants/cmp-08.md), [CMP-09](../../referentiel/composants/cmp-09.md), [CMP-10](../../referentiel/composants/cmp-10.md), [CMP-11](../../referentiel/composants/cmp-11.md), [CMP-12](../../referentiel/composants/cmp-12.md), [CMP-13](../../referentiel/composants/cmp-13.md), [CMP-14](../../referentiel/composants/cmp-14.md), [CMP-15](../../referentiel/composants/cmp-15.md), [CMP-16](../../referentiel/composants/cmp-16.md), [CMP-17](../../referentiel/composants/cmp-17.md), [CMP-18](../../referentiel/composants/cmp-18.md)

### [CAP-16](../../referentiel/capabilites/cap-16.md) : Gestion du portefeuille d'initiatives numériques

- **Réalisée par** : [PRC-08](../../referentiel/processus/prc-08.md), [PRC-10](../../referentiel/processus/prc-10.md), [PRC-11](../../referentiel/processus/prc-11.md), [PRC-12](../../referentiel/processus/prc-12.md)
- **Servie par les composants** : [CMP-01](../../referentiel/composants/cmp-01.md), [CMP-02](../../referentiel/composants/cmp-02.md), [CMP-03](../../referentiel/composants/cmp-03.md), [CMP-09](../../referentiel/composants/cmp-09.md), [CMP-10](../../referentiel/composants/cmp-10.md), [CMP-12](../../referentiel/composants/cmp-12.md), [CMP-16](../../referentiel/composants/cmp-16.md)

### [CAP-17](../../referentiel/capabilites/cap-17.md) : Engagement patient et identité numérique

- **Réalisée par** : [PRC-04](../../referentiel/processus/prc-04.md), [PRC-05](../../referentiel/processus/prc-05.md), [PRC-07](../../referentiel/processus/prc-07.md)
- **Servie par les composants** : [CMP-02](../../referentiel/composants/cmp-02.md), [CMP-04](../../referentiel/composants/cmp-04.md), [CMP-07](../../referentiel/composants/cmp-07.md), [CMP-08](../../referentiel/composants/cmp-08.md), [CMP-09](../../referentiel/composants/cmp-09.md), [CMP-10](../../referentiel/composants/cmp-10.md), [CMP-11](../../referentiel/composants/cmp-11.md), [CMP-13](../../referentiel/composants/cmp-13.md), [CMP-14](../../referentiel/composants/cmp-14.md), [CMP-15](../../referentiel/composants/cmp-15.md), [CMP-16](../../referentiel/composants/cmp-16.md), [CMP-17](../../referentiel/composants/cmp-17.md), [CMP-18](../../referentiel/composants/cmp-18.md)

### [CAP-18](../../referentiel/capabilites/cap-18.md) : Coordination intersectorielle (One Health)

- **Réalisée par** : [PRC-05](../../referentiel/processus/prc-05.md)
- **Servie par les composants** : [CMP-02](../../referentiel/composants/cmp-02.md), [CMP-04](../../referentiel/composants/cmp-04.md), [CMP-07](../../referentiel/composants/cmp-07.md), [CMP-08](../../referentiel/composants/cmp-08.md), [CMP-11](../../referentiel/composants/cmp-11.md), [CMP-13](../../referentiel/composants/cmp-13.md), [CMP-14](../../referentiel/composants/cmp-14.md), [CMP-15](../../referentiel/composants/cmp-15.md), [CMP-17](../../referentiel/composants/cmp-17.md), [CMP-18](../../referentiel/composants/cmp-18.md)

## 3. Détail par processus métier

| Processus | Capacités réalisées | Composants utilisés |
|----------|----------------------|---------------------|
| [PRC-01](../../referentiel/processus/prc-01.md) | [CAP-01](../../referentiel/capabilites/cap-01.md), [CAP-02](../../referentiel/capabilites/cap-02.md), [CAP-04](../../referentiel/capabilites/cap-04.md), [CAP-11](../../referentiel/capabilites/cap-11.md), [CAP-13](../../referentiel/capabilites/cap-13.md), [CAP-14](../../referentiel/capabilites/cap-14.md), [CAP-15](../../referentiel/capabilites/cap-15.md) | _(aucun)_ |
| [PRC-02](../../referentiel/processus/prc-02.md) | [CAP-01](../../referentiel/capabilites/cap-01.md), [CAP-03](../../referentiel/capabilites/cap-03.md), [CAP-09](../../referentiel/capabilites/cap-09.md), [CAP-10](../../referentiel/capabilites/cap-10.md), [CAP-11](../../referentiel/capabilites/cap-11.md), [CAP-13](../../referentiel/capabilites/cap-13.md), [CAP-14](../../referentiel/capabilites/cap-14.md), [CAP-15](../../referentiel/capabilites/cap-15.md) | _(aucun)_ |
| [PRC-03](../../referentiel/processus/prc-03.md) | [CAP-02](../../referentiel/capabilites/cap-02.md), [CAP-03](../../referentiel/capabilites/cap-03.md), [CAP-04](../../referentiel/capabilites/cap-04.md), [CAP-13](../../referentiel/capabilites/cap-13.md), [CAP-14](../../referentiel/capabilites/cap-14.md), [CAP-15](../../referentiel/capabilites/cap-15.md) | _(aucun)_ |
| [PRC-04](../../referentiel/processus/prc-04.md) | [CAP-04](../../referentiel/capabilites/cap-04.md), [CAP-05](../../referentiel/capabilites/cap-05.md), [CAP-06](../../referentiel/capabilites/cap-06.md), [CAP-13](../../referentiel/capabilites/cap-13.md), [CAP-14](../../referentiel/capabilites/cap-14.md), [CAP-15](../../referentiel/capabilites/cap-15.md), [CAP-17](../../referentiel/capabilites/cap-17.md) | [CMP-07](../../referentiel/composants/cmp-07.md), [CMP-08](../../referentiel/composants/cmp-08.md), [CMP-11](../../referentiel/composants/cmp-11.md), [CMP-13](../../referentiel/composants/cmp-13.md), [CMP-15](../../referentiel/composants/cmp-15.md), [CMP-17](../../referentiel/composants/cmp-17.md), [CMP-18](../../referentiel/composants/cmp-18.md) |
| [PRC-05](../../referentiel/processus/prc-05.md) | [CAP-04](../../referentiel/capabilites/cap-04.md), [CAP-05](../../referentiel/capabilites/cap-05.md), [CAP-13](../../referentiel/capabilites/cap-13.md), [CAP-14](../../referentiel/capabilites/cap-14.md), [CAP-15](../../referentiel/capabilites/cap-15.md), [CAP-17](../../referentiel/capabilites/cap-17.md), [CAP-18](../../referentiel/capabilites/cap-18.md) | [CMP-02](../../referentiel/composants/cmp-02.md), [CMP-04](../../referentiel/composants/cmp-04.md), [CMP-07](../../referentiel/composants/cmp-07.md), [CMP-08](../../referentiel/composants/cmp-08.md), [CMP-11](../../referentiel/composants/cmp-11.md), [CMP-13](../../referentiel/composants/cmp-13.md), [CMP-14](../../referentiel/composants/cmp-14.md), [CMP-15](../../referentiel/composants/cmp-15.md), [CMP-17](../../referentiel/composants/cmp-17.md), [CMP-18](../../referentiel/composants/cmp-18.md) |
| [PRC-06](../../referentiel/processus/prc-06.md) | [CAP-03](../../referentiel/capabilites/cap-03.md), [CAP-13](../../referentiel/capabilites/cap-13.md), [CAP-14](../../referentiel/capabilites/cap-14.md), [CAP-15](../../referentiel/capabilites/cap-15.md) | [CMP-07](../../referentiel/composants/cmp-07.md), [CMP-11](../../referentiel/composants/cmp-11.md), [CMP-14](../../referentiel/composants/cmp-14.md), [CMP-15](../../referentiel/composants/cmp-15.md), [CMP-17](../../referentiel/composants/cmp-17.md), [CMP-18](../../referentiel/composants/cmp-18.md) |
| [PRC-07](../../referentiel/processus/prc-07.md) | [CAP-07](../../referentiel/capabilites/cap-07.md), [CAP-08](../../referentiel/capabilites/cap-08.md), [CAP-13](../../referentiel/capabilites/cap-13.md), [CAP-14](../../referentiel/capabilites/cap-14.md), [CAP-15](../../referentiel/capabilites/cap-15.md), [CAP-17](../../referentiel/capabilites/cap-17.md) | [CMP-09](../../referentiel/composants/cmp-09.md), [CMP-10](../../referentiel/composants/cmp-10.md), [CMP-16](../../referentiel/composants/cmp-16.md) |
| [PRC-08](../../referentiel/processus/prc-08.md) | [CAP-07](../../referentiel/capabilites/cap-07.md), [CAP-08](../../referentiel/capabilites/cap-08.md), [CAP-12](../../referentiel/capabilites/cap-12.md), [CAP-13](../../referentiel/capabilites/cap-13.md), [CAP-15](../../referentiel/capabilites/cap-15.md), [CAP-16](../../referentiel/capabilites/cap-16.md) | [CMP-09](../../referentiel/composants/cmp-09.md), [CMP-10](../../referentiel/composants/cmp-10.md), [CMP-16](../../referentiel/composants/cmp-16.md) |
| [PRC-09](../../referentiel/processus/prc-09.md) | [CAP-07](../../referentiel/capabilites/cap-07.md), [CAP-12](../../referentiel/capabilites/cap-12.md), [CAP-13](../../referentiel/capabilites/cap-13.md), [CAP-14](../../referentiel/capabilites/cap-14.md), [CAP-15](../../referentiel/capabilites/cap-15.md) | [CMP-03](../../referentiel/composants/cmp-03.md), [CMP-04](../../referentiel/composants/cmp-04.md), [CMP-12](../../referentiel/composants/cmp-12.md) |
| [PRC-10](../../referentiel/processus/prc-10.md) | [CAP-08](../../referentiel/capabilites/cap-08.md), [CAP-09](../../referentiel/capabilites/cap-09.md), [CAP-12](../../referentiel/capabilites/cap-12.md), [CAP-13](../../referentiel/capabilites/cap-13.md), [CAP-15](../../referentiel/capabilites/cap-15.md), [CAP-16](../../referentiel/capabilites/cap-16.md) | [CMP-01](../../referentiel/composants/cmp-01.md), [CMP-12](../../referentiel/composants/cmp-12.md) |
| [PRC-11](../../referentiel/processus/prc-11.md) | [CAP-03](../../referentiel/capabilites/cap-03.md), [CAP-08](../../referentiel/capabilites/cap-08.md), [CAP-13](../../referentiel/capabilites/cap-13.md), [CAP-14](../../referentiel/capabilites/cap-14.md), [CAP-15](../../referentiel/capabilites/cap-15.md), [CAP-16](../../referentiel/capabilites/cap-16.md) | [CMP-01](../../referentiel/composants/cmp-01.md), [CMP-02](../../referentiel/composants/cmp-02.md), [CMP-03](../../referentiel/composants/cmp-03.md) |
| [PRC-12](../../referentiel/processus/prc-12.md) | [CAP-03](../../referentiel/capabilites/cap-03.md), [CAP-08](../../referentiel/capabilites/cap-08.md), [CAP-13](../../referentiel/capabilites/cap-13.md), [CAP-14](../../referentiel/capabilites/cap-14.md), [CAP-15](../../referentiel/capabilites/cap-15.md), [CAP-16](../../referentiel/capabilites/cap-16.md) | [CMP-01](../../referentiel/composants/cmp-01.md) |

## 4. Notes

- Les capacités transverses [CAP-17](../../referentiel/capabilites/cap-17.md) (Engagement patient & identité numérique) et [CAP-18](../../referentiel/capabilites/cap-18.md) (Coordination intersectorielle, One Health) sont rattachées aux flux VS-01/VS-02 et aux processus concernés.
- Chaque processus liste ses capacités de façon granulaire (non par copie du flux parent).
- La relation *service* entre processus et composants est portée par `PRC.uses` (processus → composant) et `CMP.applies_to` (composant → processus).
