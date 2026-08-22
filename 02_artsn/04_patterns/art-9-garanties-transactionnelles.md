---

title: "Garanties transactionnelles fortes"
id: artsn-ART-9
domain: 04_patterns
version: "1.0.0"
status: draft
last_reviewed: 2026-08-08
owner: DEPSI
tags: ["artsn", "chapitres", "ART-9", "niveau-3"]
related: ["CAP-INT-07"]
---

# Garanties transactionnelles fortes

## Pour qui lire ce document

**Niveau :** niveau 3 : Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.


ART-9 : Garanties transactionnelles fortes constitue un chapitre du **cadre normatif opposable** de l'ARTSN (règles d'or et contrats techniques d'interfaces obligatoires). Le texte de référence vit dans le référentiel : `ART-9`.

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

**Statut : candidate**

**Contenu normatif.** Pour tout mouvement de valeur monétaire ou physique, l’architecture impose une contrainte de **grade comptable strict** basée sur un registre immuable, garantissant l’équilibre parfait des comptes (équation cible : *entrées − sorties = solde*). Toute écriture doit être associée à une signature non répudiable et un numéro de suivi de lot.

**Discipline de mise en œuvre.** Dès qu’une source échappe à la gouvernance directe de l’initiative (officines pharmaceutiques privées, gestionnaires de stocks régionaux, caisses de subventions), cette discipline seule permet d’empêcher les détournements de médicaments, de bloquer les marchés noirs et d’assurer la réconciliation à somme nulle de l’argent public, sans rompre le pipeline.

- **Rattachement** : recouvre partiellement [CAP-07: Protection financière, couverture santé universelle](../../referentiel/capabilites/cap-07.md) (protection financière).
- **Normes CNISN** : [ADR-0008: Audit ATNA](../../01_cnisn/06_decisions/adr-0008-atna.md) (journal d'audit immuable), [STD-0002: Sécurité et chiffrement](../../01_cnisn/05_standards/std-0002-securite-chiffrement.md).
- **Objets de données** : [BO-03 Dispensation & produits](../../00_caesn/04_data/objets.md), [BO-04 Financement & couverture](../../00_caesn/04_data/objets.md) (objets métier CAESN) ; voir aussi le [dictionnaire des objets de données ARTSN](../03_objets-de-donnees/index.md).
- **Équation cible** : entrées − sorties = solde.
- **Déduit selon** : [ENF-2: Intégrité des flux et traçabilité des valeurs](../../referentiel/exigences/enf-2.md) (grade comptable anti-fraude).
- **Statut : Proposition ouverte.**

<!-- END:GENERATED -->
## Liens

- Index des chapitres
- Exigences contextuelles : Partie III

## Références

- **matrice de lecture** : Matrice de lecture de l'ARTSN (niveau 3) (`02_artsn/reading-matrix.md`)
- **`ART-9`** : Garanties transactionnelles fortes (`referentiel/chapitres/art-9.md`)
- **Index des chapitres** : Chapitres et patterns de référence (`02_artsn/04_patterns/index.md`)
- **Exigences contextuelles : Partie III** : Exigences contextuelles nationales (`02_artsn/02_exigences-contextuelles/index.md`)
