---
title: Dictionnaire de données fonctionnelles
id: artsn-dictionnaire-donnees
domain: 02_artsn
version: "0.0.1"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: [artsn, dictionnaire, donnees, semantique, niveau-3]
---

# Dictionnaire de données fonctionnelles

## Pour qui lire ce document

**Niveau :** niveau 3 — Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](reading-matrix.md).

Le dictionnaire de données fixe l'**atome d'information métier pur**, exempt de toute abréviation ou contrainte technologique. Il sert de **référentiel de sémantique universelle** pour la validation inter-ministérielle des contrats d'interfaces, conformément au [chapitre ART-2 (médiation et normalisation)](../referentiel/chapitres/art-2.md) et aux fondations [F.2](../referentiel/fondations/f-2.md) et [F.3](../referentiel/fondations/f-3.md).

Chaque contrat technique d'interface publié dans le registre de schémas doit s'appuyer sur les concepts sémantiques définis dans ce dictionnaire. Les définitions s'organisent par domaines fonctionnels du [CAESN](../00_caesn/00_overview/index.md) :

## Domaines du dictionnaire

| Domaine | Objet | Exemples de concepts |
|---------|-------|----------------------|
| Patient & identité | Identité de la personne prise en charge | identité, enregistrement pivot, dossier de santé |
| Prestation & soins | Actes cliniques et parcours | consultation, référence, contre-référence |
| Dispensation & produits | Médicaments et intrants de santé | dispensation, stock, lot, solde |
| Financement & couverture | Droits, tiers-payant, subventions | éligibilité, couverture, gratuité, facturation |
| Risque & surveillance | Épidémiologie, alerte, One Health | signal, foyer, chaîne de transmission |
| Exploitation & gestion | Établissements, ressources, indicateurs | établissement, personnel, indicateur |

> **État de la version 0.1.0** : le dictionnaire fonctionnel détaillé (définition canonique de chaque concept, avec types et contraintes de validation interministérielle) est en cours de constitution. Cette page pose le cadre ; les concepts seront rattachés aux contrats d'interface lors du peuplement des [PTISN](../03_ptisn/index.md).

## Liens

- [Chapitres et patterns de référence](./03_chapitres/index.md)
- [ART-2 — Médiation et normalisation](../referentiel/chapitres/art-2.md)
- [CAESN — données](../00_caesn/04_data/index.md)
