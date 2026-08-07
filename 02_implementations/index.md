---
title: Spécifications d'implémentation par initiative
id: implementations
domain: implementations
version: "0.0.1"
status: draft
last_reviewed: 2026-08-07
owner: Équipes techniques des initiatives
tags: [implementations, niveau-3]
---

# Spécifications d'implémentation par initiative

## Place dans la hiérarchie documentaire

Niveau **3** de la hiérarchie du [Cadre d'Architecture d'Entreprise](../00_framework/00_overview/index.md). Chaque document de ce dossier correspond à **une initiative** inscrite au [portefeuille national](../00_framework/06_portfolio/index.md).

| Niveau | Dossier | Document |
|--------|---------|----------|
| 1 | [`00_framework/`](../00_framework/) | Cadre d'Architecture d'Entreprise (CAESN) |
| 2 | [`reference-technique/`](../01_reference-technique/) | Architecture de Référence Technique (ART) |
| 3 | [`implementations/`](./index.md) | Spécifications par initiative (ce dossier) |

## Rôle

Les spécifications d'implémentation déclinent, pour chaque initiative, le niveau 2 (ART) au niveau propre de la solution : **configurations**, **API**, **contrats d'interfaces**, paramétrages, scénarios de déploiement et de test. Elles s'adressent aux développeurs, fournisseurs et équipes techniques.

Elles sont encadrées par la [fiche d'initiative](../00_framework/06_portfolio/initiative-card.md) (alignement valeur) et doivent respecter :
- les [principes](../00_framework/02_principles/index.md) du niveau 1 ;
- les standards techniques du niveau 2 (déclinés de l'ART) ;
- les [critères d'homologation](../00_framework/05_application/lifecycle.md).

## Convention de nommage

Un dossier (ou préfixe) par initiative du portefeuille, avec l'**identifiant du registre national des initiatives** comme racine :

```
implementations/
├── <initiative-id-N>/    # un dossier par initiative
│   ├── index.md            # périmètre, objectifs, responsables
│   ├── interface.md        # API, contrat d'interface, échanges
│   ├── configuration.md    # paramétrage, déploiement
│   └── tests.md            # scénarios de validation et d'homologation
```

## Liens

- [Cadre (niveau 1)](../00_framework/00_overview/index.md)
- [ART (niveau 2)](../01_reference-technique/index.md)