---

title: Domaines applicatifs cibles par flux de valeur
id: application-domains
domain: 05_application
version: "1.0.0"
status: draft
last_reviewed: 2026-07-03
owner: Direction des Systèmes d'Information
tags: ["applications", "domaines", "flux"]
---

# Domaines applicatifs cibles par flux de valeur

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
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

### CMP-01 : Dossier patient et parcours de soins

#### Services numériques

Identification patient, dossier de soins, historique, consultation, référence, contre-référence, suivi

#### Flux de valeur soutenus

- VS-01 : Accéder à des services de santé essentiels, intégrés, équitables et de qualité

*Rattachement : PRC-01, PRC-02, PRC-03, CAP-INT-01, CAP-INT-03, ART-4A, ART-2 · fiche*

### CMP-02 : Système d'information hospitalier et formation sanitaire

#### Services numériques

Admissions, consultations, actes, services, statistiques opérationnelles

#### Flux de valeur soutenus

- VS-01 : Accéder à des services de santé essentiels, intégrés, équitables et de qualité

*Rattachement : PRC-01, PRC-02, CAP-INT-03, ART-1 · fiche*

### CMP-03 : Santé communautaire

#### Services numériques

Suivi communautaire, sensibilisation, remontée d'alertes, visites à domicile, suivi des ménages, supervision

#### Flux de valeur soutenus

- VS-01 : Accéder à des services de santé essentiels, intégrés, équitables et de qualité
- VS-02 : Prévenir, détecter et répondre aux risques sanitaires

*Rattachement : PRC-01, PRC-03, PRC-04, CAP-INT-03, ART-8D · fiche*

### CMP-04 : Surveillance épidémiologique et riposte

#### Services numériques

Notification des cas, alertes, investigation, confirmation, riposte, clôture

#### Flux de valeur soutenus

- VS-02 : Prévenir, détecter et répondre aux risques sanitaires

*Rattachement : PRC-04, PRC-05, PRC-06, CAP-INT-03, CAP-INT-07, ART-0, ART-8D · fiche*

### CMP-05 : Vaccination, prévention et promotion de la santé

#### Services numériques

Registre vaccinal, suivi des campagnes, rappels, couverture, chaîne du froid

#### Flux de valeur soutenus

- VS-02 : Prévenir, détecter et répondre aux risques sanitaires

*Rattachement : PRC-04, CAP-INT-05, ART-4 · fiche*

### CMP-06 : Couverture santé universelle et gestion des bénéficiaires

#### Services numériques

Enregistrement des bénéficiaires, vérification des droits, exemptions, panier de soins, éligibilité

#### Flux de valeur soutenus

- VS-03 : Protéger financièrement la population face aux dépenses de santé

*Rattachement : PRC-07, PRC-08, CAP-INT-01, CAP-INT-09, ART-4C · fiche*

### CMP-07 : Facturation, remboursement et achat stratégique

#### Services numériques

Facturation des prestations, validation, remboursement, contrôle, audit, suivi des coûts

#### Flux de valeur soutenus

- VS-03 : Protéger financièrement la population face aux dépenses de santé

*Rattachement : PRC-09, CAP-INT-03, CAP-INT-10, ART-8C, ART-9 · fiche*

### CMP-08 : Logistique et chaîne d'approvisionnement

#### Services numériques

Gestion des stocks, commandes, distribution, ruptures, traçabilité, chaîne du froid

#### Flux de valeur soutenus

- VS-01 : Accéder à des services de santé essentiels, intégrés, équitables et de qualité
- VS-02 : Prévenir, détecter et répondre aux risques sanitaires
- VS-04 : Piloter, coordonner et améliorer la performance du système de santé

*Rattachement : PRC-02, PRC-05, PRC-08, CAP-INT-05, ART-8C, ART-10 · fiche*

### CMP-09 : Ressources humaines en santé

#### Services numériques

Référentiel agents, affectation, disponibilité, formation, supervision, compétences

#### Flux de valeur soutenus

- VS-04 : Piloter, coordonner et améliorer la performance du système de santé

*Rattachement : PRC-10, PRC-11, CAP-INT-02, ART-4 · fiche*

### CMP-10 : Entrepôt national de données et tableaux de bord

#### Services numériques

Consolidation, analyse, indicateurs, visualisation, revues de performance

#### Flux de valeur soutenus

- VS-04 : Piloter, coordonner et améliorer la performance du système de santé

*Rattachement : PRC-03, PRC-06, PRC-09, PRC-11, PRC-12, CAP-INT-07, CAP-INT-11, ART-6 · fiche*

### CMP-11 : Gestion du portefeuille numérique

#### Services numériques

Registre des initiatives, suivi des financements, alignement stratégique, maturité des capabilités, bénéfices

#### Flux de valeur soutenus

- VS-04 : Piloter, coordonner et améliorer la performance du système de santé

*Rattachement : PRC-10, PRC-12, CAP-INT-06, CAP-INT-12, ART-8D · fiche*

<!-- END:GENERATED -->
## Liens

- Paysage applicatif cible
- Services numériques partagés
- Flux de valeur

## Références

- **matrice de lecture** : Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
- **VS-01 : Accéder à des services de santé essentiels, intégrés, équitables et de qualité** : Accéder à des services de santé essentiels, intégrés, équitables et de qualité (`referentiel/flux-valeur/vs-01.md`)
- **PRC-01** : Accès, orientation et admission du patient (`referentiel/processus/prc-01.md`)
- **PRC-02** : Prestation des soins cliniques (`referentiel/processus/prc-02.md`)
- **PRC-03** : Continuité, suivi et qualité des soins (`referentiel/processus/prc-03.md`)
- **CAP-INT-01** : CAP-INT-01 : Résolution d’identité du bénéficiaire (`referentiel/capacites/cap-int-01.md`)
- **CAP-INT-03** : CAP-INT-03 : Échange et médiation inter-systèmes (`referentiel/capacites/cap-int-03.md`)
- **ART-4A** : Résolution d'identité (`referentiel/chapitres/art-4a.md`)
- **ART-2** : Médiation et normalisation (`referentiel/chapitres/art-2.md`)
- **fiche** : Tableaux de bord & Portails nationaux (performance, CSU, ressources, veille) (`referentiel/composants/cmp-01.md`)
- **ART-1** : Intégration et ingestion (`referentiel/chapitres/art-1.md`)
- **VS-02 : Prévenir, détecter et répondre aux risques sanitaires** : Prévenir, détecter et répondre aux risques sanitaires (`referentiel/flux-valeur/vs-02.md`)
- **PRC-04** : Veille, prévention et surveillance sanitaire (`referentiel/processus/prc-04.md`)
- **ART-8D** : Chorégraphie inter-institutionnelle (`referentiel/chapitres/art-8d.md`)
- **PRC-05** : Alerte, investigation et riposte (`referentiel/processus/prc-05.md`)
- **PRC-06** : Clôture et capitalisation des épisodes (`referentiel/processus/prc-06.md`)
- **CAP-INT-07** : CAP-INT-07 : Accès et exposition des données analytiques (`referentiel/capacites/cap-int-07.md`)
- **ART-0** : Accords de partage inter-institutionnels (`referentiel/chapitres/art-0.md`)
- **CAP-INT-05** : CAP-INT-05 : Terminologie et codification communes (`referentiel/capacites/cap-int-05.md`)
- **ART-4** : Référentiels de métadonnées de gestion (`referentiel/chapitres/art-4.md`)
- **VS-03 : Protéger financièrement la population face aux dépenses de santé** : Protéger financièrement la population face aux dépenses de santé (`referentiel/flux-valeur/vs-03.md`)
- **PRC-07** : Identification et droits des bénéficiaires (`referentiel/processus/prc-07.md`)
- **PRC-08** : Financement et exemption au point de service (`referentiel/processus/prc-08.md`)
- **CAP-INT-09** : CAP-INT-09 : Gestion des consentements et bases d’autorisation (`referentiel/capacites/cap-int-09.md`)
- **ART-4C** : Éligibilité et couverture (`referentiel/chapitres/art-4c.md`)
- **PRC-09** : Remboursement et régulation des mécanismes (`referentiel/processus/prc-09.md`)
- **CAP-INT-10** : CAP-INT-10 : Provenance, audit et traçabilité (`referentiel/capacites/cap-int-10.md`)
- **ART-8C** : Agrégation par lot (`referentiel/chapitres/art-8c.md`)
- **ART-9** : Garanties transactionnelles fortes (`referentiel/chapitres/art-9.md`)
- **VS-04 : Piloter, coordonner et améliorer la performance du système de santé** : Piloter, coordonner et améliorer la performance du système de santé (`referentiel/flux-valeur/vs-04.md`)
- **ART-10** : Logistique (`referentiel/chapitres/art-10.md`)
- **PRC-10** : Planification et allocation des ressources (`referentiel/processus/prc-10.md`)
- **PRC-11** : Suivi et pilotage de la performance (`referentiel/processus/prc-11.md`)
- **CAP-INT-02** : CAP-INT-02 : Registre et résolution des professionnels de santé (`referentiel/capacites/cap-int-02.md`)
- **PRC-12** : Redevabilité et amélioration continue (`referentiel/processus/prc-12.md`)
- **CAP-INT-11** : CAP-INT-11 : Qualité et réconciliation (`referentiel/capacites/cap-int-11.md`)
- **ART-6** : Analytique et restitution (`referentiel/chapitres/art-6.md`)
- **CAP-INT-06** : CAP-INT-06 : Catalogue des services et registre des contrats (`referentiel/capacites/cap-int-06.md`)
- **CAP-INT-12** : CAP-INT-12 : Conformité et tests d’interopérabilité (`referentiel/capacites/cap-int-12.md`)
- **Paysage applicatif cible** : Paysage applicatif cible (`00_caesn/05_application/layers.md`)
- **Services numériques partagés** : Services numériques partagés prioritaires (`00_caesn/05_application/shared-services.md`)
- **Flux de valeur** : Flux de valeur nationaux de santé (`00_caesn/01_value-streams/index.md`)
