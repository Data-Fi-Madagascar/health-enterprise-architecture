---
title: Profils techniques d'implémentation de la Santé Numérique (PTISN)
id: ptisn
domain: 03_ptisn
version: "1.0.0"
status: draft
last_reviewed: 2026-08-08
owner: Équipes techniques des initiatives
tags: [ptisn, niveau-4]
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
