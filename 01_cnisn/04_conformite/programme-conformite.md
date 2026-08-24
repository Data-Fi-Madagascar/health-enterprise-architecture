---
title: Partie IV bis : Programme de conformité opérationnel
id: cnisn-programme-conformite
domain: 04_conformite
version: "1.0.0"
status: candidate
last_reviewed: 2026-08-20
owner: CNASN
tags: ["cnisn", "niveau-2", "conformite", "programme"]
---

# Partie IV bis : Programme de conformité opérationnel

## Pour qui lire ce document

**Niveau :** niveau 2 : Cadre National d'Interopérabilité de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ○ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

## Objet

La conformité définie en `04_conformite/index.md` (critères, statuts, dérogations) n'a de valeur que si elle est **vérifiée**. Ce document instancie un **programme de test de conformité** opérationnel, sur le modèle du CSIR (Afrique du Sud), pour transformer l'homologation d'un exercice théorique en un contrôle effectif.

> **Statut :** *proposé* — conditionné à l'adoption de l'ADR-0010 (cadre légal) et à la dotation en moyens.

## 1. Périmètre des tests

| Type de test | Cible | Fréquence |
|--------------|-------|-----------|
| Conformité standards | Implémentation FHIR R4, mADX, PIXm/PDQm, ATNA | Par initiative, avant homologation |
| Interopérabilité | Scénarios de bout en bout X-Road ↔ médiation (PT-01/PT-02) | Par initiative |
| Sécurité et résidence | Chiffrement, hébergement national, RBAC (PT-10) | Annuelle + après incident |
| Qualité et réconciliation | Complétude, promptitude, réconciliation (PT-13) | Trimestrielle |
| Audit et provenance | Pistes d'audit (PT-12), traçabilité | Annuelle |

## 2. Acteurs et responsabilités

| Acteur | Rôle |
|--------|------|
| CNASN | Autorité de conformité ; valide les résultats et les sanctions |
| Équipe technique CNASN / DEPSI | Exécute les tests, tient le registre de conformité |
| Initiative | Fournit l'environnement de test et les preuves |
| CMIL | Co-contrôle sur la protection des données |

## 3. Sanctions et suivi

- **Non-conformité bloquante** : refus d'homologation (voir `00_caesn/07_governance/homologation.md`).
- **Dérive de conformité** : rétrogradation du statut (conforme → conforme sous conditions → suspendue).
- **Tableau de bord** : taux de conformité par initiative, par standard, alertes (voir `02_artsn/06_gouvernance/conformite.md`).
- **Rapport annuel** : publié par le CNASN, alimente la revue stratégique.

## 4. Jalon de démarrage

1. Adoption ADR-0010 (cadre légal) ;
2. Dotation du CNASN en moyens de test (environnement, compétences) ;
3. Prototype sur 2 initiatives pilotes (modèle CSIR) ;
4. Généralisation.

## Liens

- Critères de conformité
- Workflow d'homologation
- ADR-0010 (cadre légal)

## Références

- **Conformité** : Critères de conformité (`01_cnisn/04_conformite/index.md`)
- **Homologation** : Workflow d'homologation (`00_caesn/07_governance/homologation.md`)
- **ADR-0010** : Cadre légal (`01_cnisn/06_decisions/adr-0010-cadre-legal.md`)
- **Modèle CSIR** : Conseil sud-africain de la recherche scientifique et industrielle
