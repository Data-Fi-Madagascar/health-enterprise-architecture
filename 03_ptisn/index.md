---
title: Profils techniques d'implémentation de la Santé Numérique (PTISN)
id: ptisn
domain: 03_ptisn
version: "0.0.1"
status: draft
last_reviewed: 2026-08-08
owner: Équipes techniques des initiatives
tags: [ptisn, niveau-4]
---

# Profils techniques d'implémentation de la Santé Numérique (PTISN)

## Place dans la hiérarchie documentaire

Niveau **4** de la hiérarchie du [Cadre d'Architecture d'Entreprise](../00_caesn/00_overview/index.md). Chaque document de ce dossier correspond à **une initiative** inscrite au [portefeuille national](../00_caesn/06_portfolio/index.md).

| Niveau | Dossier | Document |
|--------|---------|----------|
| 1 | [`00_caesn/`](../00_caesn/) | Cadre d'Architecture d'Entreprise de la Santé Numérique (CAESN) |
| 2 | [`01_cnisn/`](../01_cnisn/) | Cadre National d'Interopérabilité de la Santé Numérique (CNISN) |
| 3 | [`02_artsn/`](../02_artsn/) | Architecture de Référence Technique de la Santé Numérique (ARTSN) |
| 4 | [`ptisn/`](./index.md) | Profils techniques d'implémentation par initiative (ce dossier) |

## Rôle

Les profils techniques d'implémentation déclinent, pour chaque initiative, le niveau 3 (ARTSN) au niveau propre de la solution : **configurations**, **API**, **contrats d'interfaces**, paramétrages, scénarios de déploiement et de test. Ils s'adressent aux développeurs, fournisseurs et équipes techniques.

Elles sont encadrées par la [fiche d'initiative](../00_caesn/06_portfolio/initiative-card.md) (alignement valeur) et doivent respecter :
- les [principes](../00_caesn/02_principles/index.md) du niveau 1 ;
- les standards d'interopérabilité du niveau 2 (CNISN) ;
- les standards techniques du niveau 3 (déclinés de l'ARTSN) ;
- les [critères d'homologation](../00_caesn/05_application/lifecycle.md).

## Convention de nommage

Un dossier (ou préfixe) par initiative du portefeuille, avec l'**identifiant du registre national des initiatives** comme racine :

```
ptisn/
├── <initiative-id-N>/    # un dossier par initiative
│   ├── index.md            # périmètre, objectifs, responsables
│   ├── interface.md        # API, contrat d'interface, échanges
│   ├── configuration.md    # paramétrage, déploiement
│   └── tests.md            # scénarios de validation et d'homologation
```

## Liens

- [Cadre (niveau 1)](../00_caesn/00_overview/index.md)
- [CNISN (niveau 2)](../01_cnisn/index.md)
- [ARTSN (niveau 3)](../02_artsn/index.md)
