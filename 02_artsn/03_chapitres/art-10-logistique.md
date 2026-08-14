---
title: "ART-10 — Logistique"
id: art-10
domain: 02_artsn
version: "0.0.1"
status: draft
last_reviewed: 2026-08-12
owner: DEPSI
tags: [artsn, chapitres, art-10, niveau-3]
---
# ART-10 — Logistique

## Pour qui lire ce document

**Niveau :** niveau 3 — Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : [matrice de lecture](../reading-matrix.md).


ART-10 — Logistique constitue un chapitre du **cadre normatif opposable** de l'ARTSN (règles d'or et contrats techniques d'interfaces obligatoires). Le texte de référence vit dans le référentiel : [`art-10`](../../referentiel/chapitres/art-10.md).

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py — ne pas éditer à la main -->

**Contenu normatif.** La continuité de la chaîne d'approvisionnement (médicaments, vaccins, intrants, équipements) conditionne l'exécution des flux de valeur de soins. L'architecture impose une traçabilité de bout en bout des mouvements de produits, de la centrale d'achat jusqu'au point de service : chaque mouvement (livraison, dispensation, transfert, destruction) est un événement immuable, horodaté, adossé aux référentiels de produits, et réconcilié selon les règles comptables de conservation de quantité (Entrées − Sorties = Solde).

**Discipline existentielle.** Dès lors qu'une source échappe à la gouvernance directe de l'initiative (centres de stockage isolés, ruptures de connectivité, circuits parallèles de distribution) : elle seule permet de garantir la disponibilité des intrants et la réconciliation à somme nulle des stocks sans rompre le pipeline.

- **Rattachement** : [CAP-10](../../referentiel/capabilites/cap-10.md) (chaîne d'approvisionnement), [CAP-11](../../referentiel/capabilites/cap-11.md) (infrastructures et équipements).
- **Modèles cibles** : événementisation des mouvements de stock, registres logistiques (ex. OpenLMIS), traçabilité par lot.
- **Déduit selon** : [ENF-2](../../referentiel/exigences/enf-2.md) (traçabilité des valeurs).
- **Statut : Provisoire.**

*Rattachement : [ENF-2](../../referentiel/exigences/enf-2.md), [CAP-10](../../referentiel/capabilites/cap-10.md), [CAP-11](../../referentiel/capabilites/cap-11.md) · [fiche](../../referentiel/chapitres/art-10.md)*

<!-- END:GENERATED -->
## Liens

- [Index des chapitres](./index.md)
- [Exigences contextuelles — Partie III](../02_exigences-contextuelles/index.md)