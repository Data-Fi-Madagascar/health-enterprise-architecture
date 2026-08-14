---
title: "PT-14 — Interopérabilité transfrontalière"
id: pt-14-wrapper
domain: 03_ptisn
version: "0.1"
status: draft
last_reviewed: 2026-08-13
owner: DEPSI
tags: ["ptisn", "niveau-4", "profil", "transfrontalier", "gdhcn"]
---

# PT-14 — Interopérabilité transfrontalière

> **Objet** — Ce profil technique définit les standards, protocoles et configurations pour les échanges de données de santé au-delà des frontières nationales, en garantissant la confiance mutuelle, la souveraineté des données et la conformité aux cadres internationaux (GDHCN, SADC, OMS AFRO). Le **Résumé International du Patient (IPS)** — profil FHIR R4 — constitue le standard de référence pour l'échange de données cliniques transfrontalières.

**Référentiel :** [`referentiel/profils/pt-14.md`](../../referentiel/profils/pt-14.md)

---

## Standards IPS

| Standard | Usage | Profil |
|----------|-------|--------|
| **HL7 FHIR IPS** | Résumé international du patient — document clinique minimal pour la continuité des soins transfrontaliers | [hl7.org/fhir/uv/ips](https://hl7.org/fhir/uv/ips) |
| **GDHCN** | Confiance mutuelle et certification des systèmes échangeant des IPS | Global Digital Health Certification Network |
| **IHE PIX/PDQ** | Résolution d'identité transfrontalière pour le mapping patient | — |

### Sections IPS minimales (échange obligatoire)

| Code | Section | Description |
|------|---------|-------------|
| **ALGY** | Allergies et intolérances | Substance, réaction, sévérité, statut |
| **MDCA** | Médicaments actuels | Produit, dosage, statut, indication |
| **PROB** | Problèmes de santé | Code CIM-10, onset, statut |
| **IDOI** | Identité du patient | NIN, nom, naissance, sexe |

---

## Rattachement

| Niveau | Objet | Identifiant |
|--------|-------|-------------|
| **Niveau 2** | Capacité d'interopérabilité | [CAP-INT-13](../../referentiel/capacites/cap-int-13.md) — Interopérabilité transfrontalière et confiance internationale |
| **Niveau 2** | Capacité d'interopérabilité | [CAP-INT-03](../../referentiel/capacites/cap-int-03.md) — Échange et médiation inter-systèmes |
| **Niveau 1** | Capabilité métier | [CAP-15](../../referentiel/capabilites/cap-15.md) — Cybersécurité, contrôle d'accès et résidence |
| **Niveau 1** | Capabilité métier | [CAP-17](../../referentiel/capabilites/cap-17.md) — Engagement patient et identité numérique |
| **Niveau 3** | Chapitre ARTSN | [ART-7](../../referentiel/chapitres/art-7.md) — Sécurité, contrôle d'accès et résidence |
| **Niveau 3** | Chapitre ARTSN | [ART-0](../../referentiel/chapitres/art-0.md) — Accords de partage inter-institutionnels |
| **Niveau 3** | Chapitre ARTSN | [ART-1](../../referentiel/chapitres/art-1.md) — Intégration |
| **Niveau 3** | Composant applicatif | [CMP-06](../../referentiel/composants/cmp-06.md) — Intégration, Médiation, API Gateway |
| **Niveau 3** | Composant applicatif | [CMP-15](../../referentiel/composants/cmp-15.md) — API Gateway (confiance GDHCN) |
