---
id: pt-15
domain: 03_ptisn
type: profil
niveau: "4"
title: PT-15 — Surveillance One Health
status: draft
owner: DEPSI
version: "0.1"
source: 03_ptisn/03_profils/pt-15-surveillance-one-health.md
maps_to: ["cap-int-14", "cap-18", "cap-05", "art-11", "art-0", "art-4d", "art-8b", "cmp-02", "cmp-04", "cmp-06"]
tags: ["ptisn", "niveau-4", "profil", "one-health", "surveillance"]
---

# PT-15 — Surveillance One Health

## Objet

Ce profil technique définit les standards, profils d'interface et configurations pour les échanges de données entre le secteur santé et les autres secteurs (élevage, environnement, météorologie) dans le cadre de l'approche One Health.

## Périmètre

| Dimension | Portée |
|-----------|--------|
| **Secteurs** | Santé humaine (MSP), Élevage (MINAE), Environnement (MEEF), Météo (DGM) |
| **Flux** | Alertes intersectorielles, données agrégées de surveillance, corrélation signaux faibles |
| **Standards** | FHIR R4 (santé humaine), OIE-WAHIS (animaux), GBIF (environnement), WMO (météo) |
| **Chapitres ARTSN** | ART-11, ART-0, ART-4d, ART-8b |

## Standards et profils applicables

### Santé humaine

| Standard | Usage | Version |
|----------|-------|---------|
| HL7 FHIR | Échange de données cliniques et de surveillance | R4 |
| IHE PCD | Surveillance des événements indésirables | — |
| IHE ADX | Échange de données agrégées (mADX) | — |

### Santé animale

| Standard | Usage | Version |
|----------|-------|---------|
| OIE-WAHIS | Système mondial d'information sur la santé animale | — |
| FHIR Veterinary Medicine | Données vétérinaires (en développement) | — |
| RVF-FMIS | Fièvre de la Vallée du Rift — gestion des intrants | — |

### Environnement

| Standard | Usage | Version |
|----------|-------|---------|
| GBIF | Système mondial d'information sur la biodiversité | — |
| INSPIRE | Données spatiales environnementales (UE) | — |
| OGC SensorThings | Capteurs IoT environnementaux | — |

### Météorologie

| Standard | Usage | Version |
|----------|-------|---------|
| WMO BUFR | Données météorologiques binaires | — |
| WMO GRIB | Données de grille | — |

## Interfaces d'échange

### Interface 1 — Alertes intersectorielles

| Propriété | Valeur |
|-----------|--------|
| **Producteur** | CMP-04 (Moteur analytique) |
| **Consommateur** | CMP-02 (Centre de commande) |
| **Format** | FHIR R4 — Bundle de type alerte |
| **Protocole** | REST (synchrone) + Broker asynchrone |
| **Fréquence** | Temps réel (alertes) |

### Interface 2 — Données agrégées animales

| Propriété | Valeur |
|-----------|--------|
| **Producteur** | Système OIE-WAHIS |
| **Consommateur** | CMP-03 (Entrepôt Lakehouse) |
| **Format** | CSV/OIE standard → FHIR via médiation |
| **Protocole** | API REST (polling) |
| **Fréquence** | Quotidienne |

### Interface 3 — Données environnementales

| Propriété | Valeur |
|-----------|--------|
| **Producteur** | Système MEEF/GBIF |
| **Consommateur** | CMP-05 (Moteur de graphes) |
| **Format** | JSON-LD (GBIF) → RDF via médiation |
| **Protocole** | API REST |
| **Fréquence** | Horaire |

### Interface 4 — Données météo

| Propriété | Valeur |
|-----------|--------|
| **Producteur** | DGM (WMO BUFR/GRIB) |
| **Consommateur** | CMP-03 (Entrepôt Lakehouse) |
| **Format** | BUFR/GRIB → FHIR via médiation |
| **Protocole** | FTP/API |
| **Fréquence** | Horaire |

## Règles de cloisonnement

| Règle | Description |
|-------|-------------|
| **Règle 1** | Les identités humaines (INP) ne sont jamais croisées avec les identités animales (OIE ID) |
| **Règle 2** | L'agrégation croisée spatiale/temporelle est autorisée sans désanonymisation |
| **Règle 3** | Chaque secteur conserve la souveraineté sur ses données source |
| **Règle 4** | Les données croisées sont irréversiblement agrégées avant exposition |
| **Règle 5** | La journalisation est distincte par secteur avec audit séparé |

## Exigences de sécurité

| Exigence | Description |
|----------|-------------|
| **EXG-S1** | Authentification mutuelle entre systèmes sectoriels (mTLS) |
| **EXG-S2** | Chiffrement TLS 1.3 pour tous les échanges |
| **EXG-S3** | RBAC différencié par rôle sectoriel |
| **EXG-S4** | Journalisation de tous les accès intersectoriels |
| **EXG-S5** | Accord de partage (ART-0) préalable à tout flux |

## Indicateurs de performance

| Indicateur | Cible |
|------------|-------|
| Délai détection cluster intersectoriel | < 24h |
| Volume données agrégées croisées/jour | 10 000 |
| Disponibilité service alertes | 99,9% |
| Taux de conformité accords de partage | 100% |

## Dépendances

| Dépendance | Type | Statut |
|------------|------|--------|
| FHIR R4 | Standard | ✅ Validé |
| OIE-WAHIS | Standard international | ✅ Disponible |
| GBIF | Standard international | ✅ Disponible |
| ART-11 | Chapitre ARTSN | Candidate → à promouvoir Stable |
| CAP-INT-14 | Capacité CNISN | Créée |
| CAP-18 | Capabilité CAESN | Active |
