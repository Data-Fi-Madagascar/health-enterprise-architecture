---
title: "ADR-0008 — Adoption d'ATNA et journalisation pour l'audit et la traçabilité"
id: adr-0008
domain: 08_decisions
version: "0.1.0"
status: proposé
date: 2026-08-13
owner: DEPSI
tags: [adr, audit, traçabilité, atna, journalisation]
---

# ADR-0008 — Adoption d'ATNA et journalisation pour l'audit et la traçabilité

## Pour qui lire ce document

**Niveau :** niveau 1 — Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ○ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle.

- **Statut** : proposé
- **Date** : 2026-08-13
- **Groupe concerné** : DEPSI, CNASN, directions juridiques

## Contexte

La traçabilité des accès et des modifications de données de santé est une exigence réglementaire (Loi 2014-038) et un principe fondamental de l'ARTSN (ART-7). Sans mécanisme d'audit robuste, il est impossible de :
- Détecter les accès non autorisés
- Prouver la conformité aux réglementations
- Résoudre les incidents de sécurité
- Produire des rapports d'activité fiables

Actuellement, la journalisation est partielle (DHIS2 uniquement) et non centralisée. Il n'existe pas de piste d'audit unifiée couvrant tous les systèmes.

## Décision

Adopter le profil **IHE ATNA** (Audit Trail and Node Authentication) comme standard national pour l'audit et la traçabilité, complété par un mécanisme de journalisation centralisé.

## Justification

ATNA répond aux exigences du cadre :

- **ART-7** : Sécurité, contrôle d'accès et résidence des données
- **CAP-INT-10** : Audit et traçabilité
- **PT-12** : Audit et traçabilité
- **Loi 2014-038** : Protection des données personnelles
- **STD-0002** : Chiffrement et RBAC

ATNA doit :
- Journaliser tous les accès (lecture, écriture, modification, suppression)
- Être immuable (les logs ne peuvent pas être modifiés)
- Être centralisé (aggrégation de tous les systèmes)
- Supporter la rétention réglementaire (5 ans minimum)
- Permettre les requêtes d'audit (< 3 secondes)

## Conséquences

### Positives
- Conformité réglementaire renforcée
- Détection précoce des incidents de sécurité
- Piste d'audit complète et immuable
- Capacité d'investigation forensique
- Rapports d'activité fiables

### Négatives
- Coût de stockage des logs (volume croissant)
- Complexité de l'infrastructure de journalisation
- Nécessite un SIEM (Security Information and Event Management)
- Formation des équipes sécurité

## Alternatives considérées

| Alternative | Raison du refus |
|-------------|-----------------|
| Logs applicatifs isolés | Pas centralisés, pas immuables, pas interopérables |
| Journalisation basique (fichiers texte) | Pas structuré, pas interrogeable, pas sécurisé |
| SIEM propriétaire | Dépendance éditeur, coût élevé, pas standard |
| Blockchain d'audit | Technologie immature, coût excessif, pas nécessaire |

## Références

- [PT-12 — Audit et traçabilité](../../03_ptisn/03_profils/pt-12-audit-provenance-traçabilité.md)
- [ART-7 — Sécurité](../../referentiel/chapitres/art-7.md)
- [CAP-INT-10 — Audit et traçabilité](../../referentiel/capacites/cap-int-10.md)
- [IHE ATNA — Audit Trail and Node Authentication](https://www.ihe.net)
