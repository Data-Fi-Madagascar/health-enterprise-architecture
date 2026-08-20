---

title: Profils techniques d'implémentation de la Santé Numérique (PTISN)
id: ptisn
domain: 03_ptisn
version: "1.0.0"
status: draft
last_reviewed: 2026-08-08
owner: Équipes techniques des initiatives
tags: ["ptisn", "niveau-4"]
---

# Profils techniques d'implémentation de la Santé Numérique (PTISN)

## Pour qui lire ce document

**Niveau :** niveau 4 : Profils techniques d'implémentation de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

## Place dans la hiérarchie documentaire

Le PTISN constitue le niveau 4 de la hiérarchie documentaire du Cadre d'Architecture d'Entreprise. Il découle du cadre national d'interopérabilité défini par l'Unité de Gouvernance Digitale (UGD) et traduit, pour chaque initiative inscrite au portefeuille national, les principes des niveaux supérieurs en spécifications techniques opérationnelles.

| Niveau | Dossier | Document |
|--------|---------|----------|
| 1 | `00_caesn/` | Cadre d'Architecture d'Entreprise de la Santé Numérique (CAESN) |
| 2 | `01_cnisn/` | Cadre National d'Interopérabilité de la Santé Numérique (CNISN) + Standards |
| 3 | `02_artsn/` | Architecture de Référence Technique de la Santé Numérique (ARTSN) |
| 4 | `ptisn/` | Profils techniques d'implémentation par initiative (ce dossier) : découle de l'UGD |

## Rôle

Les profils techniques d'implémentation déclinent, pour chaque initiative, le niveau 3 (ARTSN) au niveau propre de la solution : configurations, API, contrats d'interfaces, paramétrages, scénarios de déploiement et de test. Ils s'adressent aux développeurs, fournisseurs et équipes techniques.

Le PTISN découle du cadre national d'interopérabilité défini par l'Unité de Gouvernance Digitale (UGD). Il intègre les standards du CNISN (niveau 2) et les patterns de l'ARTSN (niveau 3) pour les adapter à chaque initiative spécifique. Ces profils sont encadrés par la fiche d'initiative (alignement valeur) et doivent respecter les principes du niveau 1, les standards d'interopérabilité du niveau 2 (CNISN), les standards techniques du niveau 3 (déclinés de l'ARTSN), ainsi que les critères d'homologation.

## Convention de nommage

Chaque initiative du portefeuille se voit attribuer un dossier portant l'**identifiant du registre national des initiatives** comme racine. La structure attendue est la suivante :

```
ptisn/
├── <initiative-id-N>/    # un dossier par initiative
│   ├── index.md            # périmètre, objectifs, responsables
│   ├── interface.md        # API, contrat d'interface, échanges
│   ├── configuration.md    # paramétrage, déploiement
│   └── tests.md            # scénarios de validation et d'homologation
```

## Liens

- Guide de lecture du PTISN
- Matrice de lecture du PTISN
- Glossaire du PTISN
- Acronymes du PTISN

## Références

- **matrice de lecture** : Matrice de lecture du PTISN (niveau 4) (`03_ptisn/reading-matrix.md`)
- **Cadre d'Architecture d'Entreprise** : Cadre d'Architecture d'Entreprise de la Santé Numérique (CAESN) (`00_caesn/00_overview/index.md`)
- **portefeuille national** : Portefeuille d'initiatives orienté valeur (`00_caesn/06_portfolio/index.md`)
- **`ptisn/`** : Profils techniques d'implémentation de la Santé Numérique (PTISN) (`03_ptisn/index.md`)
- **fiche d'initiative** : Fiche standard d'initiative orientée valeur (`00_caesn/06_portfolio/initiative-card.md`)
- **principes** : Principes d'architecture (`00_caesn/02_principles/index.md`)
- **critères d'homologation** : Cycle de vie applicatif et critères d'homologation (`00_caesn/05_application/lifecycle.md`)
- **Guide de lecture du PTISN** : Guide de lecture du PTISN (niveau 4) (`03_ptisn/reading-guide.md`)
- **Matrice de lecture du PTISN** : Matrice de lecture du PTISN (niveau 4) (`03_ptisn/reading-matrix.md`)
- **Glossaire du PTISN** : Glossaire du PTISN (niveau 4) (`03_ptisn/glossary.md`)
- **Acronymes du PTISN** : Acronymes et abréviations du PTISN (niveau 4) (`03_ptisn/acronyms.md`)

## Documents de la section

- [ptisn-glossary: Glossaire du PTISN (niveau 4)](glossary.md)
- [ptisn-reading-matrix: Matrice de lecture du PTISN (niveau 4)](reading-matrix.md)
- [ptisn-acronyms: Acronymes et abréviations du PTISN (niveau 4)](acronyms.md)
- [ptisn-reading-guide: Guide de lecture du PTISN (niveau 4)](reading-guide.md)
- [ptisn-PT-11: PT-11 : Profil technique national](03_profils/pt-11-consentement-bases-autorisation.md)
- [ptisn-PT-05: PT-05 : Profil technique national](03_profils/pt-05-registre-professionnels.md)
- [ptisn-PT-02: PT-02 : Profil technique national](03_profils/pt-02-mediation-intra-secteur.md)
- [ptisn-PT-11-analyse: Analyse PT-11 : Profil technique du consentement](03_profils/pt-11-analyse-consentement.md)
- [ptisn-PT-13: PT-13 : Profil technique national](03_profils/pt-13-qualite-reconciliation.md)
- [ptisn-PT-01: PT-01 : Profil technique national](03_profils/pt-01-echange-interinstitutionnel.md)
- [ptisn-profils: Partie III : Profils techniques nationaux](03_profils/pt-00-index.md)
- [ptisn-PT-07: PT-07 : Profil technique national](03_profils/pt-07-terminologie-codification.md)
- [ptisn-PT-04: PT-04 : Profil technique national](03_profils/pt-04-resolution-identite-beneficiaire.md)
- [ptisn-PT-10: PT-10 : Profil technique national](03_profils/pt-10-confiance-authentification-autorisation.md)
- [ptisn-PT-12: PT-12 : Profil technique national](03_profils/pt-12-audit-provenance-traçabilité.md)
- [ptisn-PT-09: PT-09 : Profil technique national](03_profils/pt-09-analytique-exposition-donnees.md)
- [PT-15: PT-15 : Surveillance One Health](03_profils/pt-15-surveillance-one-health.md)
- [ptisn-PT-03: PT-03 : Profil technique national](03_profils/pt-03-catalogue-services-registre-contrats.md)
- [ptisn-PT-16: PT-16 : Orchestration de processus bornés](03_profils/pt-16-orchestration-processus.md)
- [ptisn-PT-08: PT-08 : Profil technique national](03_profils/pt-08-echange-donnees-agregees.md)
- [ptisn-PT-06: PT-06 : Profil technique national](03_profils/pt-06-referentiel-structures-services.md)
- [ptisn-PT-14: PT-14 : Interopérabilité transfrontalière](03_profils/pt-14-interopabilite-transfrontaliere.md)
- [ptisn-exemples: Exemples de profils d'initiative remplis](05_exemples/index.md)
- [ptisn-matrice-alignement: Partie IV : Matrice d'alignement](04_matrice-alignement/index.md)
- [ptisn-regles-utilisation: Partie I : Règles d'utilisation du PTISN](01_regles-utilisation/index.md)
- [ptisn-introduction: Préambule du PTISN](00_introduction/index.md)
- [ptisn-profil-initiative: Partie V : Profil technique d'une initiative](05_profil-initiative/index.md)
- [ptisn-cas-usage-pilotage: Cas d'usage : Remontée de données et pilotage du système](08_annexes/cas-usage-pilotage-systeme.md)
- [ptisn-cas-usage-couverture: Cas d'usage : Couverture sanitaire et protection financière](08_annexes/cas-usage-couverture-sanitaire.md)
- [ptisn-cas-usage-surveillance: Cas d'usage : Surveillance et riposte épidémique](08_annexes/cas-usage-surveillance-epidemique.md)
- [ptisn-annexe-a: Annexe A : Synthèse des choix](08_annexes/a-synthese-choix.md)
- [ptisn-cas-usage-reference: Cas d'usage : Référence, contre-référence et évacuation sanitaire](08_annexes/cas-usage-reference-evacuation.md)
- [ptisn-annexe-c: Annexe C : Principes de mise en œuvre](08_annexes/c-principes-mise-en-oeuvre.md)
- [ptisn-priorisation-decisions: Priorisation et calendrier : 5 premières décisions PTISN](08_annexes/e-priorisation-decisions.md)
- [ptisn-annexe-b: Annexe B : Décisions à instruire](08_annexes/b-decisions-instruire.md)
- [ptisn-annexe-d: Annexe D : Glossaire](08_annexes/d-glossaire.md)
- [ptisn-topologie: Partie II : Topologie nationale cible](02_topologie-nationale-cible/index.md)
- [ptisn-conclusion: Conclusion du PTISN](07_conclusion/index.md)
- [ptisn-gouvernance: Partie VI : Gouvernance du PTISN](06_gouvernance/index.md)

<!-- liens-section-auto -->
