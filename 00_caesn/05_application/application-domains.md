---
title: Domaines applicatifs cibles par flux de valeur
id: application-domains
domain: 05_application
version: "0.1.0"
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

## Liens

- [Paysage applicatif cible](./layers.md)
- [Services numériques partagés](./shared-services.md)
- [Flux de valeur](../01_value-streams/index.md)