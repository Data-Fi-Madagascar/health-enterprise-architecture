---
title: "Registre des décisions d'architecture (ADR)"
id: registre-decisions
domain: 08_decisions
version: "0.1"
status: draft
last_reviewed: 2026-08-13
owner: Bureau de Réalisation de la Valeur
tags: [decisions, adr, registre, gouvernance, niveau-1]
---

# Registre des décisions d'architecture (ADR)

## Pour qui lire ce document

**Niveau :** niveau 1 — Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle.

---

## Objet

Ce registre centralise l'ensemble des Architecture Decision Records (ADR) du cadre HEA. Il constitue la **source unique de vérité** pour les choix d'architecture documentés, leur statut et leur évolution.

Chaque ADR enregistrée ici est un choix structurant, daté et traçable, produite par le Comité National d'Architecture Santé Numérique (CNASN) ou validée par lui.

---

## Légende des statuts

| Statut | Signification |
|--------|---------------|
| **proposé** | Soumis au CNASN, en attente de décision |
| **accepté** | Décision validée, en cours d'implémentation |
| **appliqué** | Décision pleinement déployée et opérationnelle |
| **remplacé** | Succédé par une ADR plus récente |
| **déprécié** | N'est plus applicable (technologie obsolète, standard abandonné) |

---

## Registre

### Interopérabilité et standards

| ID | Titre | Statut | Date | Propriétaire | Impact |
|----|-------|--------|------|--------------|--------|
| [ADR-0001](./adr-0001-x-road.md) | Adoption de X-Road comme plateforme d'échange interinstitutionnel | **appliqué** | 2026-07-01 | DEPSI | Élevé — infrastructure nationale |
| [ADR-0002](./adr-0002-madx.md) | Adoption du profil IHE mADX pour l'échange de données agrégées | **appliqué** | 2026-07-01 | DEPSI | Élevé — collecte nationale |
| [ADR-0003](./adr-0003-fhir.md) | Utilisation de HL7 FHIR comme standard d'interopérabilité | **appliqué** | 2026-07-01 | DEPSI | Critique — standard transversal |
| [ADR-0004](./adr-0004-identite.md) | Adoption des profils IHE PIXm/PDQm pour la résolution d'identité | **appliqué** | 2026-07-01 | DEPSI | Élevé — identité nationale |

### Identité et consentement

| ID | Titre | Statut | Date | Propriétaire | Impact |
|----|-------|--------|------|--------------|--------|
| [ADR-0005](./adr-0005-consentement.md) | Consentement structuré via FHIR Consent | **proposé** | 2026-08-13 | DEPSI | Élevé — souveraineté données |
| [ADR-0006](./adr-0006-inp.md) | Identité nationale patient (INP) via PIXm/PDQm | **proposé** | 2026-08-13 | DEPSI | Critique — identité unique |

### Confiance et sécurité

| ID | Titre | Statut | Date | Propriétaire | Impact |
|----|-------|--------|------|--------------|--------|
| [ADR-0007](./adr-0007-gdhcn.md) | Confiance transfrontalière via GDHCN | **proposé** | 2026-08-13 | DEPSI | Élevé — transfrontalier |
| [ADR-0008](./adr-0008-atna.md) | Audit et traçabilité via ATNA + journalisation | **proposé** | 2026-08-13 | DEPSI | Moyen — conformité |

### Terminologie

| ID | Titre | Statut | Date | Propriétaire | Impact |
|----|-------|--------|------|--------------|--------|
| [ADR-0009](./adr-0009-terminologie.md) | Terminologie nationale (CIM-10 + LOINC + mapping) | **proposé** | 2026-08-13 | DEPSI | Élevé — sémantique commune |

---

## Processus d'enregistrement

```
1. Le CNASN statue sur un choix d'architecture
2. Le secrétariat rédige l'ADR selon le template (adr-0000-template.md)
3. L'ADR est ajoutée au registre avec le statut « proposé »
4. Après validation, le statut passe à « accepté »
5. Après déploiement complet, le statut passe à « appliqué »
6. Si remplacé, le statut passe à « remplacé » avec référence à la nouvelle ADR
7. Si abandonné, le statut passe à « déprécié » avec justification
```

---

## Statistiques

| Statut | Nombre |
|--------|--------|
| Proposé | 5 |
| Accepté | 0 |
| Appliqué | 4 |
| Remplacé | 0 |
| Déprécié | 0 |
| **Total** | **9** |

---

## Liens

- [Template ADR](./adr-0000-template.md)
- [Index des décisions](./index.md)
- [Gouvernance](../07_governance/index.md)
- [Guide du processus](../07_governance/processus-gouvernance.md)
