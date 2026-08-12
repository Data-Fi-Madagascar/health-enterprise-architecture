---
title: Domaines applicatifs cibles par flux de valeur
id: application-domains
domain: 05_application
version: "0.0.1"
status: draft
last_reviewed: 2026-07-03
owner: Direction des Systèmes d'Information
tags: [applications, domaines, flux]
---

# Domaines applicatifs cibles par flux de valeur

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

Le cadre retient les domaines applicatifs suivants, qui décrivent des familles de systèmes sans imposer un logiciel particulier.

| Flux de valeur | Domaine applicatif | Services numériques | Capabilités |
|----------------|--------------------|---------------------|-------------|
| VS-01 | Dossier patient et parcours de soins | Identification patient, dossier de soins, historique, consultation, référence, contre-référence, suivi | CAP-01, 02, 03, 14, 15 |
| VS-01 | Système d'information hospitalier et formation sanitaire | Admissions, consultations, actes, services, statistiques opérationnelles | CAP-01, 03, 13 |
| VS-01 / VS-02 | Santé communautaire | Suivi communautaire, sensibilisation, remontée d'alertes, visites à domicile, suivi des ménages, supervision | CAP-04, 05, 06 |
| VS-02 | Surveillance épidémiologique et riposte | Notification des cas, alertes, investigation, confirmation, riposte, clôture | CAP-05, 06, 13, 14 |
| VS-02 | Vaccination, prévention et promotion de la santé | Registre vaccinal, suivi des campagnes, rappels, couverture, chaîne du froid | CAP-06, 10, 13 |
| VS-03 | Couverture santé universelle et gestion des bénéficiaires | Enregistrement des bénéficiaires, vérification des droits, exemptions, panier de soins, éligibilité | CAP-07, 14, 15 |
| VS-03 | Facturation, remboursement et achat stratégique | Facturation des prestations, validation, remboursement, contrôle, audit, suivi des coûts | CAP-07, 08, 12, 13 |
| VS-01 / VS-02 / VS-04 | Logistique et chaîne d'approvisionnement | Gestion des stocks, commandes, distribution, ruptures, traçabilité, chaîne du froid | CAP-10, 13, 14 |
| VS-04 | Ressources humaines en santé | Référentiel agents, affectation, disponibilité, formation, supervision, compétences | CAP-09, 13, 14 |
| VS-04 | Entrepôt national de données et tableaux de bord | Consolidation, analyse, indicateurs, visualisation, revues de performance | CAP-13, 08, 16 |
| VS-04 | Gestion du portefeuille numérique | Registre des initiatives, suivi des financements, alignement stratégique, maturité des capabilités, bénéfices | CAP-16, 08, 13 |
| Tous les VS | Référentiels nationaux et services partagés | FOSA, géographie, indicateurs, agents, produits, bénéficiaires, terminologies, identité, accès, consentement | CAP-13, 14, 15 |

## Composants applicatifs cibles

<!-- BEGIN:GENERATED source=referentiel/composants/cmp-01.md,referentiel/composants/cmp-02.md,referentiel/composants/cmp-03.md,referentiel/composants/cmp-04.md,referentiel/composants/cmp-05.md,referentiel/composants/cmp-06.md,referentiel/composants/cmp-07.md,referentiel/composants/cmp-08.md,referentiel/composants/cmp-09.md,referentiel/composants/cmp-10.md,referentiel/composants/cmp-11.md -->
<!-- Généré par scripts/build_wrappers.py — ne pas éditer à la main -->

### CMP-01 — Dossier patient et parcours de soins

#### Services numériques

Identification patient, dossier de soins, historique, consultation, référence, contre-référence, suivi

#### Flux de valeur soutenus

- [VS-01 — Accéder à des services de santé essentiels, intégrés, équitables et de qualité](../../referentiel/flux-valeur/vs-01.md)

*Rattachement : [EV-02](../../referentiel/etapes-valeur/ev-02.md), [EV-03](../../referentiel/etapes-valeur/ev-03.md), [EV-05](../../referentiel/etapes-valeur/ev-05.md), [EV-06](../../referentiel/etapes-valeur/ev-06.md), [CAP-INT-01](../../referentiel/capacites/cap-int-01.md), [CAP-INT-03](../../referentiel/capacites/cap-int-03.md), [ART-4A](../../referentiel/chapitres/art-4a.md), [ART-2](../../referentiel/chapitres/art-2.md) · [fiche](../../referentiel/composants/cmp-01.md)*

### CMP-02 — Système d'information hospitalier et formation sanitaire

#### Services numériques

Admissions, consultations, actes, services, statistiques opérationnelles

#### Flux de valeur soutenus

- [VS-01 — Accéder à des services de santé essentiels, intégrés, équitables et de qualité](../../referentiel/flux-valeur/vs-01.md)

*Rattachement : [EV-02](../../referentiel/etapes-valeur/ev-02.md), [EV-03](../../referentiel/etapes-valeur/ev-03.md), [EV-04](../../referentiel/etapes-valeur/ev-04.md), [CAP-INT-03](../../referentiel/capacites/cap-int-03.md), [ART-1](../../referentiel/chapitres/art-1.md) · [fiche](../../referentiel/composants/cmp-02.md)*

### CMP-03 — Santé communautaire

#### Services numériques

Suivi communautaire, sensibilisation, remontée d'alertes, visites à domicile, suivi des ménages, supervision

#### Flux de valeur soutenus

- [VS-01 — Accéder à des services de santé essentiels, intégrés, équitables et de qualité](../../referentiel/flux-valeur/vs-01.md)
- [VS-02 — Prévenir, détecter et répondre aux risques sanitaires](../../referentiel/flux-valeur/vs-02.md)

*Rattachement : [EV-01](../../referentiel/etapes-valeur/ev-01.md), [EV-06](../../referentiel/etapes-valeur/ev-06.md), [EV-08](../../referentiel/etapes-valeur/ev-08.md), [EV-09](../../referentiel/etapes-valeur/ev-09.md), [CAP-INT-03](../../referentiel/capacites/cap-int-03.md), [ART-8D](../../referentiel/chapitres/art-8d.md) · [fiche](../../referentiel/composants/cmp-03.md)*

### CMP-04 — Surveillance épidémiologique et riposte

#### Services numériques

Notification des cas, alertes, investigation, confirmation, riposte, clôture

#### Flux de valeur soutenus

- [VS-02 — Prévenir, détecter et répondre aux risques sanitaires](../../referentiel/flux-valeur/vs-02.md)

*Rattachement : [EV-09](../../referentiel/etapes-valeur/ev-09.md), [EV-10](../../referentiel/etapes-valeur/ev-10.md), [EV-11](../../referentiel/etapes-valeur/ev-11.md), [EV-12](../../referentiel/etapes-valeur/ev-12.md), [EV-13](../../referentiel/etapes-valeur/ev-13.md), [CAP-INT-03](../../referentiel/capacites/cap-int-03.md), [CAP-INT-07](../../referentiel/capacites/cap-int-07.md), [ART-0](../../referentiel/chapitres/art-0.md), [ART-8D](../../referentiel/chapitres/art-8d.md) · [fiche](../../referentiel/composants/cmp-04.md)*

### CMP-05 — Vaccination, prévention et promotion de la santé

#### Services numériques

Registre vaccinal, suivi des campagnes, rappels, couverture, chaîne du froid

#### Flux de valeur soutenus

- [VS-02 — Prévenir, détecter et répondre aux risques sanitaires](../../referentiel/flux-valeur/vs-02.md)

*Rattachement : [EV-08](../../referentiel/etapes-valeur/ev-08.md), [EV-09](../../referentiel/etapes-valeur/ev-09.md), [CAP-INT-05](../../referentiel/capacites/cap-int-05.md), [ART-4](../../referentiel/chapitres/art-4.md) · [fiche](../../referentiel/composants/cmp-05.md)*

### CMP-06 — Couverture santé universelle et gestion des bénéficiaires

#### Services numériques

Enregistrement des bénéficiaires, vérification des droits, exemptions, panier de soins, éligibilité

#### Flux de valeur soutenus

- [VS-03 — Protéger financièrement la population face aux dépenses de santé](../../referentiel/flux-valeur/vs-03.md)

*Rattachement : [EV-15](../../referentiel/etapes-valeur/ev-15.md), [EV-16](../../referentiel/etapes-valeur/ev-16.md), [EV-18](../../referentiel/etapes-valeur/ev-18.md), [CAP-INT-01](../../referentiel/capacites/cap-int-01.md), [CAP-INT-09](../../referentiel/capacites/cap-int-09.md), [ART-4C](../../referentiel/chapitres/art-4c.md) · [fiche](../../referentiel/composants/cmp-06.md)*

### CMP-07 — Facturation, remboursement et achat stratégique

#### Services numériques

Facturation des prestations, validation, remboursement, contrôle, audit, suivi des coûts

#### Flux de valeur soutenus

- [VS-03 — Protéger financièrement la population face aux dépenses de santé](../../referentiel/flux-valeur/vs-03.md)

*Rattachement : [EV-19](../../referentiel/etapes-valeur/ev-19.md), [EV-20](../../referentiel/etapes-valeur/ev-20.md), [EV-21](../../referentiel/etapes-valeur/ev-21.md), [CAP-INT-03](../../referentiel/capacites/cap-int-03.md), [CAP-INT-10](../../referentiel/capacites/cap-int-10.md), [ART-8C](../../referentiel/chapitres/art-8c.md), [ART-9](../../referentiel/chapitres/art-9.md) · [fiche](../../referentiel/composants/cmp-07.md)*

### CMP-08 — Logistique et chaîne d'approvisionnement

#### Services numériques

Gestion des stocks, commandes, distribution, ruptures, traçabilité, chaîne du froid

#### Flux de valeur soutenus

- [VS-01 — Accéder à des services de santé essentiels, intégrés, équitables et de qualité](../../referentiel/flux-valeur/vs-01.md)
- [VS-02 — Prévenir, détecter et répondre aux risques sanitaires](../../referentiel/flux-valeur/vs-02.md)
- [VS-04 — Piloter, coordonner et améliorer la performance du système de santé](../../referentiel/flux-valeur/vs-04.md)

*Rattachement : [EV-04](../../referentiel/etapes-valeur/ev-04.md), [EV-12](../../referentiel/etapes-valeur/ev-12.md), [EV-18](../../referentiel/etapes-valeur/ev-18.md), [CAP-INT-05](../../referentiel/capacites/cap-int-05.md), [ART-8C](../../referentiel/chapitres/art-8c.md), [ART-10](../../referentiel/chapitres/art-10.md) · [fiche](../../referentiel/composants/cmp-08.md)*

### CMP-09 — Ressources humaines en santé

#### Services numériques

Référentiel agents, affectation, disponibilité, formation, supervision, compétences

#### Flux de valeur soutenus

- [VS-04 — Piloter, coordonner et améliorer la performance du système de santé](../../referentiel/flux-valeur/vs-04.md)

*Rattachement : [EV-22](../../referentiel/etapes-valeur/ev-22.md), [EV-23](../../referentiel/etapes-valeur/ev-23.md), [EV-25](../../referentiel/etapes-valeur/ev-25.md), [CAP-INT-02](../../referentiel/capacites/cap-int-02.md), [ART-4](../../referentiel/chapitres/art-4.md) · [fiche](../../referentiel/composants/cmp-09.md)*

### CMP-10 — Entrepôt national de données et tableaux de bord

#### Services numériques

Consolidation, analyse, indicateurs, visualisation, revues de performance

#### Flux de valeur soutenus

- [VS-04 — Piloter, coordonner et améliorer la performance du système de santé](../../referentiel/flux-valeur/vs-04.md)

*Rattachement : [EV-07](../../referentiel/etapes-valeur/ev-07.md), [EV-14](../../referentiel/etapes-valeur/ev-14.md), [EV-21](../../referentiel/etapes-valeur/ev-21.md), [EV-25](../../referentiel/etapes-valeur/ev-25.md), [EV-26](../../referentiel/etapes-valeur/ev-26.md), [EV-27](../../referentiel/etapes-valeur/ev-27.md), [CAP-INT-07](../../referentiel/capacites/cap-int-07.md), [CAP-INT-11](../../referentiel/capacites/cap-int-11.md), [ART-6](../../referentiel/chapitres/art-6.md) · [fiche](../../referentiel/composants/cmp-10.md)*

### CMP-11 — Gestion du portefeuille numérique

#### Services numériques

Registre des initiatives, suivi des financements, alignement stratégique, maturité des capabilités, bénéfices

#### Flux de valeur soutenus

- [VS-04 — Piloter, coordonner et améliorer la performance du système de santé](../../referentiel/flux-valeur/vs-04.md)

*Rattachement : [EV-22](../../referentiel/etapes-valeur/ev-22.md), [EV-24](../../referentiel/etapes-valeur/ev-24.md), [EV-28](../../referentiel/etapes-valeur/ev-28.md), [CAP-INT-06](../../referentiel/capacites/cap-int-06.md), [CAP-INT-12](../../referentiel/capacites/cap-int-12.md), [ART-8D](../../referentiel/chapitres/art-8d.md) · [fiche](../../referentiel/composants/cmp-11.md)*

<!-- END:GENERATED -->
## Liens

- [Paysage applicatif cible](./layers.md)
- [Services numériques partagés](./shared-services.md)
- [Flux de valeur](../01_value-streams/index.md)