---
title: "Interopérabilité transfrontalière"
id: ptisn-PT-14
domain: 03_profils
version: "1.0.0"
status: draft
last_reviewed: 2026-08-13
owner: DEPSI
tags: ["ptisn", "niveau-4", "profil", "transfrontalier", "gdhcn"]
---

# Interopérabilité transfrontalière

<!-- BEGIN:GENERATED -->
<!-- Généré par scripts/build_wrappers.py : ne pas éditer à la main -->

## Objet

Ce profil technique définit les standards, protocoles et configurations pour les échanges de données de santé au-delà des frontières nationales, en garantissant la confiance mutuelle, la souveraineté des données et la conformité aux cadres internationaux (GDHCN, SADC, OMS AFRO).

## Périmètre

| Dimension | Portée |
|-----------|--------|
| **Partenaires** | SADC (Afrique australe), UA/CEUA (Afrique), OMS AFRO, OIF, CDC Africa |
| **Flux** | Surveillance épidémique régionale, actes médicaux transfrontaliers, logistique pharmaceutique, recherche clinique |
| **Standards** | GDHCN (Trust Anchor), FHIR R4, HL7 v2.x (legacy), OID (ISO), IHE |
| **Chapitres ARTSN** | [ART-7: Sécurité](../../referentiel/chapitres/art-7.md), [ART-0: Accords](../../referentiel/chapitres/art-0.md), [ART-1: Intégration](../../referentiel/chapitres/art-1.md) |

## Standards et profils applicables

### Confiance et certificats

| Standard | Usage | Version |
|----------|-------|---------|
| GDHCN | Référentiel de confiance mondial pour la santé numérique | — |
| X.509v3 | Certificats de confiance mutuelle | v3 |
| EAL 4+ | Évaluation de la conformité des systèmes partenaires | — |

### Échange de données

| Standard | Usage | Version |
|----------|-------|---------|
| HL7 FHIR | Échange de données cliniques et de surveillance | R4 |
| HL7 FHIR IPS | Résumé international du patient — document clinique minimal transfrontalier | R4 (IPS) |
| HL7 v2.x | Interopérabilité legacy avec systèmes partenaires | 2.x |
| IHE PIX/PDQ | Résolution et recherche d'identité transfrontalière | — |
| IHE XDS.b | Partage de documents cliniques | — |

### Identification

| Standard | Usage | Version |
|----------|-------|---------|
| OID (ISO) | Identifiants d'organisation internationaux | — |
| HL7 II | Identifiant patient international | R4 |
| ISO 2108 | Code pays (ISO 3166-1) | — |

## Interfaces d'échange

### Interface 1 — Confiance GDHCN

| Propriété | Valeur |
|-----------|--------|
| **Producteur** | [CMP-15: API Gateway](../../referentiel/composants/cmp-15.md) |
| **Consommateur** | Systèmes partenaires SADC/UA |
| **Format** | X.509v3 + GDHCN Trust Anchor |
| **Protocole** | mTLS |
| **Fréquence** | Continuous (TLS handshake) |

### Interface 2 — Échange clinique transfrontalier (IPS)

| Propriété | Valeur |
|-----------|--------|
| **Producteur** | [CMP-06: Intégration/Médiation](../../referentiel/composants/cmp-06.md) |
| **Consommateur** | Système santé partenaire étranger |
| **Format** | FHIR R4 — IPS Composition (résumé patient) |
| **Protocole** | REST (synchrone) |
| **Fréquence** | À la demande |
| **Sections minimales** | ALGY (allergies), MDCA (médicaments), PROB (problèmes), IDOI (identité) |

### Interface 3 — Surveillance épidémique régionale

| Propriété | Valeur |
|-----------|--------|
| **Producteur** | [CMP-04: Moteur analytique](../../referentiel/composants/cmp-04.md) |
| **Consommateur** | OMS AFRO / CDC Africa |
| **Format** | IHE ADX (mADX) — données agrégées |
| **Protocole** | REST (asynchrone) |
| **Fréquence** | Quotidienne |

### Interface 4 — Résolution d'identité transfrontalière

| Propriété | Valeur |
|-----------|--------|
| **Producteur** | [CMP-11: INP](../../referentiel/composants/cmp-11.md) |
| **Consommateur** | [CMP-06: Médiation](../../referentiel/composants/cmp-06.md) → Système partenaire |
| **Format** | IHE PIX/PDQ — mapping OID ↔ INP |
| **Protocole** | REST |
| **Fréquence** | À la demande |

### Interface 5 — Évacuation sanitaire internationale

| Propriété | Valeur |
|-----------|--------|
| **Producteur** | [CMP-06: Intégration/Médiation](../../referentiel/composants/cmp-06.md) |
| **Consommateur** | Système santé du pays de destination |
| **Format** | FHIR R4 — ServiceRequest (transfer) + IPS Composition (données cliniques) |
| **Protocole** | REST (synchrone) |
| **Fréquence** | À la demande (événements urgentes) |
| **Prérequis** | Accord bilatéral ([ART-0: Accords de partage inter-institutionnels](../../referentiel/chapitres/art-0.md)) + autorisation de sortie du territoire |

## Règles de souveraineté

| Règle | Description |
|-------|-------------|
| **Règle 1** | L'identité nationale complète (INP + nom complet) ne quitte jamais le territoire sauf dérogation explicite du Ministre |
| **Règle 2** | Seules les données minimisées nécessaires à la finalité peuvent être exportées |
| **Règle 3** | Tout flux sortant doit être couvert par un accord bilatéral ou multilatéral explicite ([ART-0: Accords de partage inter-institutionnels](../../referentiel/chapitres/art-0.md)) |
| **Règle 4** | Le consentement du patient doit être obtenu pour tout échange sortant sauf obligation légale |
| **Règle 5** | Tous les flux transfrontaliers sont journalisés et auditable par la DEPSI |
| **Règle 6** | Les systèmes partenaires doivent démontrer leur conformité GDHCN avant tout accès |
| **Règle 7** | Les données génomiques et de recherche sont pseudonymisées avant export |

## Exigences de sécurité

| Exigence | Description |
|----------|-------------|
| **EXG-S1** | Authentification mutuelle (mTLS) entre systèmes nationaux et partenaires |
| **EXG-S2** | Chiffrement TLS 1.3 pour tous les échanges transfrontaliers |
| **EXG-S3** | RBAC différencié par rôle et par pays partenaire |
| **EXG-S4** | Journalisation de tous les accès transfrontaliers avec horodatage |
| **EXG-S5** | Accord de partage ([ART-0: Accords de partage inter-institutionnels](../../referentiel/chapitres/art-0.md)) préalable à tout flux sortant |
| **EXG-S6** | Vérification de conformité GDHCN avant chaque session |
| **EXG-S7** | Révocation immédiate en cas d'incident de sécurité |

## Indicateurs de performance

| Indicat | Cible |
|---------|-------|
| Délai de résolution d'identité transfrontalière | < 2s |
| Disponibilité service GDHCN Trust Anchor | 99,99% |
| Taux de conformité accords bilatéraux | 100% |
| Volume échanges transfrontaliers/jour | 500 |
| Taux de journalisation flux sortants | 100% |

## Dépendances

| Dépendance | Type | Statut |
|------------|------|--------|
| GDHCN | Standard international | ✅ Disponible |
| HL7 FHIR IPS | Standard international | ✅ Disponible |
| FHIR R4 | Standard | ✅ Validé |
| IHE PIX/PDQ | Standard | ✅ Disponible |
| [ART-7: Sécurité, contrôle d'accès et résidence de la donnée](../../referentiel/chapitres/art-7.md) | Chapitre ARTSN | Active |
| [ART-0: Accords de partage inter-institutionnels](../../referentiel/chapitres/art-0.md) | Chapitre ARTSN | Active |
| [CAP-INT-13: Interopérabilité transfrontalière et confiance internationale](../../referentiel/capacites/cap-int-13.md) | Capacité CNISN | Créée |
| [CAP-15: Cybersécurité, confidentialité et gouvernance des données personnelles](../../referentiel/capabilites/cap-15.md) | Capabilité CAESN | Active |
| [CAP-17: Engagement patient et identité numérique](../../referentiel/capabilites/cap-17.md) | Capabilité CAESN | Active |

<!-- END:GENERATED -->
