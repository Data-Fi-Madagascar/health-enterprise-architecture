---
title: "STD-0005 — Norme d'identité patient — PIXm/PDQm"
id: std-0005
domain: 05_standards
version: "1.0.0"
status: approved
last_reviewed: 2026-08-13
owner: Comité National d'Architecture Santé Numérique
tags: [standards, identite, pixm, pdqm, obligatoire]
---

# STD-0005 — Norme d'identité patient — PIXm/PDQm

## Pour qui lire ce document

**Niveau :** niveau 1 — Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ○ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

- **Type** : norme (obligatoire)
- **Statut** : approuvé
- **ADR de référence** : ADR-0004, ADR-0006
- **Date d'entrée en vigueur** : 2026-08-13

## Contexte

L'identité patient est l'actif fondamental du système d'information sanitaire. Sans identifiant unique national (INP), il est impossible de garantir la continuité des soins, d'éviter les doublons ou de croiser les données pour le pilotage. Les profils IHE PIXm et PDQm fournissent les transactions REST standardisées pour la gestion des identifiants et la recherche démographique.

## Énoncé

Toute solution gérant l'identité des bénéficiaires **doit** :

1. **Utiliser IHE PIXm** pour la gestion et le rapprochement des identifiants patients entre domaines
2. **Utiliser IHE PDQm** pour la recherche de patients à partir de données démographiques
3. **Attribuer un INP** conforme au format INSTAT (12 chiffres) à chaque patient
4. **Garantir l'unicité** de l'INP (une seule personne physique = un seul INP)
5. **Exposer des API REST** conformes aux spécifications IHE PIXm/PDQm
6. **Implémenter un seuil de rapprochement** national pour le matching démographique

## Champ d'application

Cette norme s'applique à :
- Tous les systèmes enregistrant ou identifiant des patients
- Le PT-04 (résolution d'identité)
- Les services de recherche démographique et de rapprochement de dossiers

## Références au cadre

- **Principes** : PA-05 (Interopérabilité), PA-06 (Gouvernance des données)
- **ARTSN** : ART-4 (Référentiels), ART-4a (Résolution d'identité), F.1 (Identité et registres)
- **PTISN** : PT-04 (Résolution d'identité)
- **CNISN** : CAP-INT-01 (Résolution d'identité)

## Contrôle et conformité

| Critère | Vérification |
|---------|--------------|
| PIXm | API PIXm opérationnelle |
| PDQm | API PDQm opérationnelle |
| INP | Format INSTAT (12 chiffres) |
| Unicité | Pas de doublons d'INP |
| Matching | Seuil de rapprochement défini |
| API REST | Conforme aux spécifications IHE |

## Dérogations

Les dérogations sont possibles pour :
- Les systèmes legacy utilisant des identifiants programmatiques (migration progressive vers l'INP)
- Les zones sans connectivité (mode hors-ligne avec synchronisation différée)

Toute dérogation doit être justifiée et approuvée par le Comité National.

## Références

- Normes et standards
- ADR-0004 — PIXm/PDQm
- ADR-0006 — INP
- PT-04 — Résolution d'identité
- ARTSN — Fondation F.1

- **matrice de lecture** — Matrice de lecture du CNISN (niveau 2) (`01_cnisn/reading-matrix.md`)
