---

title: "Journal des modifications des ADR"
id: adr-change-log
domain: 06_decisions
version: "1.0.0"
status: active
date: 2026-07-01
owner: DEPSI
tags: ["adr", "changelog", "suivi"]
---

# Journal des modifications des ADR

## A propos de ce document

Ce document suit l'historique des modifications apportees aux Architecture Decision Records (ADR) du cadre HEA. Il permet de :

- **Traquer les evolutions** : Suivre les changements de statut, les mises a jour et les remplacements d'ADR
- **Maintenir la tracabilite** : Conserver un historique complet des decisions architecturales
- **Faciliter l'audit** : Fournir une vue d'ensemble des decisions et de leur cycle de vie

## Format du journal

Chaque entree suit le format :

```markdown
### [Date] - [Type de modification] - [ADR concerne]
- **Auteur** : [Nom/Role]
- **Description** : [Description detaillee du changement]
- **Justification** : [Raison du changement, le cas echeant]
- **Liens** : [References vers d'autres documents ou ADR]
- **Impact** : [Consequences sur le systeme ou les autres ADR]
```

## Types de modifications

| Type | Description | Exemple |
|------|-------------|---------|
| **Creation** | Nouvel ADR ajoute | ADR-XXXX : Nouvelle decision sur X |
| **Acceptation** | ADR passe en statut "accepte" | ADR-0001 : Valide par le comite |
| **Application** | ADR passe en statut "applique" | ADR-0002 : Deployment termine |
| **Modification** | Mise a jour du contenu | ADR-0003 : Ajout de precisions |
| **Remplacement** | ADR remplace par une nouvelle decision | ADR-0004 remplace par ADR-XXXX |
| **Depreciation** | ADR marque comme deprecie | ADR-0005 : Plus pertinent |
| **Retrait** | ADR retire du registre | ADR-0006 : Decision abandonnee |

## Historique des modifications

### [2026-07-01] - Creation - ADR-0001 a ADR-0010
- **Auteur** : Equipes DEPSI
- **Description** : Creation initiale des 10 premiers ADR couvrant les decisions architecturales fondamentales du CNISN
- **ADR concernes** : ADR-0001 (X-Road), ADR-0002 (mADX), ADR-0003 (FHIR), ADR-0004 (Identite), ADR-0005 (Consentement), ADR-0006 (INP), ADR-0007 (GDHCN), ADR-0008 (ATNA), ADR-0009 (Terminologie), ADR-0010 (Cadre legal)
- **Statut initial** : Tous en statut "accepte" (accepted)
- **Justification** : Etablir les fondations de l'architecture d'interoperabilite du systeme de sante national
- **Impact** : Definition des standards techniques et organisationnels pour l'echange de donnees de sante

### [2026-07-01] - Acceptation - ADR-0006
- **Auteur** : Comite de gouvernance CNISN
- **Description** : Validation officielle de l'ADR-0006 sur l'adoption de l'Identite Nationale Patient (INP)
- **ADR concerne** : ADR-0006
- **Ancien statut** : proposee (proposed)
- **Nouveau statut** : acceptee (accepted)
- **Justification** : Consensus atteint sur l'approche d'identification des patients
- **Liens** : 
  - ADR-0004 : PIXm/PDQm (reference dans la decision)
  - ART-4 : Referentiels nationaux
  - CAP-INT-01 : Resolution d'identite
- **Impact** : Permet la mise en oeuvre de l'identification unique des patients a travers le systeme

## Prochaines etapes

1. **Mettre a jour ce journal** a chaque modification d'un ADR
2. **Valider les changements** via le processus de revue de code
3. **Synchroniser avec le registre** des decisions pour maintenir la coherence
4. **Archiver les versions precedentes** des ADR modifies pour reference historique

## Bonnes pratiques

- **Tracabilite** : Chaque modification doit etre documentee dans ce journal
- **Clarte** : Les descriptions doivent etre suffisamment detaillees pour comprendre le changement
- **Liens croises** : Toujours referencer les ADR, articles ou capacites concernes
- **Validation** : Les modifications doivent etre validees par le proprietaire de l'ADR ou le comite de gouvernance

## Annexe : Statuts des ADR

| Statut | Description | Couleur |
|--------|-------------|---------|
| **proposee** (proposed) | Decision en cours d'elaboration | Jaune |
| **acceptee** (accepted) | Decision validee par le comite | Vert |
| **appliquee** (applied) | Decision mise en oeuvre | Vert |
| **remplacee** (replaced) | Decision remplacee par une nouvelle | Rouge |
| **depreciee** (deprecated) | Decision obsolete | Rouge |
| **brouillon** (draft) | Ebauche de decision | Gris |
| **active** (active) | Decision active (variante de acceptee) | Vert |

## References

- [ADR Template](adr-0000-template.md) - Modele pour les nouveaux ADR
- [Registre des decisions](registre-decisions.md) - Liste complete des ADR
- [Index des ADR](index.md) - Index des decisions architecturales
