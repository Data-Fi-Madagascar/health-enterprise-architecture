---
title: "Cas d'usage — Surveillance et riposte épidémique"
id: ptisn-cas-usage-surveillance
domain: 03_ptisn
version: "0.1"
status: draft
last_reviewed: 2026-08-13
owner: DEPSI
tags: ["ptisn", "niveau-4", "cas-usage", "surveillance", "epidemiologie", "riposte", "vs-02"]
---

# Cas d'usage — Surveillance et riposte épidémique (VS-02)

## Pour qui lire ce document

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| Partenaires techniques et financiers | ◐ |

---

## Objectif

Ce document montre comment les **profils techniques existants** composent pour couvrir le cycle complet de la surveillance et de la riposte épidémique : détection, notification, alerte, investigation, riposte et capitalisation.

## Principe architectural

Le cycle épidémique est un **cas d'usage métier** qui consomme plusieurs profils existants. Il ne nécessite pas de profil dédié car chaque étape mobilise des briques techniques déjà définies :

```
┌─────────────────────────────────────────────────────────────────────┐
│                    CYCLE ÉPIDÉMIQUE (VS-02)                        │
│  Détection → Notification → Alert → Investigation → Riposte → Clôture │
└──────┬──────────┬──────────┬──────────┬──────────┬─────────────────┘
       │          │          │          │          │
       ▼          ▼          ▼          ▼          ▼
┌─────────────────────────────────────────────────────────────────────┐
│                    PROFILS TECHNIQUES                              │
│  PT-08    │  PT-02   │  PT-10  │  PT-05  │  PT-15  │  PT-12     │
│  Données  │ Médiation│ Alertes │ Labo    │ One H.  │  Audit     │
│  agrégées │          │ & conf. │         │         │            │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Scénario — Cycle complet de surveillance épidémique

### Phase 1 — Détection et collecte (EV-09)

**Objectif** : Collecter les données de routine des formations sanitaires et des agents communautaires pour identifier les signaux sanitaires.

```
Formations sanitaires     Médiation (PT-02)       Entrepôt (CMP-03)
        │                       │                       │
        │ Données cliniques     │                       │
        │ (FHIR Observation)    │                       │
        │──────────────────────▶│  Normalisation +       │
        │                       │  validation            │
        │                       │──────────────────────▶│
        │                       │                       │
Agents communautaires     Médiation (PT-02)       Moteur analytique
        │                       │                 (CMP-04)
        │ Rapport mobile         │                       │
        │ (offline → sync)       │                       │
        │──────────────────────▶│──────────────────────▶│
```

**Profils mobilisés** :

| Profil | Rôle |
|--------|------|
| **PT-08** | Échange de données agrégées (mADX) avec OMS AFRO |
| **PT-02** | Médiation sémantique (données terrain → FHIR) |
| **PT-07** | Mapping terminologique (CIM-10, LOINC) |
| **PT-12** | Traçabilité des événements de collecte |

**Données échangées** :
- `Observation` (FHIR) — cas cliniques signalés
- `Bundle` (mADX) — données agrégées hebdomadaires
- `Device` — capteurs IoT (météo, vecteurs)

---

### Phase 2 — Notification et alerte (EV-10)

**Objectif** : Notifier formellement un signal validé aux autorités compétentes et déclencher l'alerte.

```
Moteur analytique (CMP-04)    Centre de commande (CMP-02)
        │                            │
        │ Signal de dépassement       │
        │ seuil (ART-5)               │
        │───────────────────────────▶│
        │                            │  Alerte temps réel
        │                            │──────────────────▶ Ministère
        │                            │                   District
        │                            │                   OMS
        │                            │
        │                            │  Notification
        │◀───────────────────────────│  automatique
```

**Profils mobilisés** :

| Profil | Rôle |
|--------|------|
| **PT-10** | Confiance et autorisation (RBAC, alertes) |
| **PT-02** | Médiation (formatage des alertes) |
| **PT-12** | Audit trail de la notification |

**Données échangées** :
- `Bundle` (alerte) — signal épidémique structuré
- `Communication` (FHIR) — notification officielle

---

### Phase 3 — Investigation et confirmation (EV-11)

**Objectif** : Vérifier le signal sur le terrain, prélever des échantillons, confirmer ou infirmer le cas.

```
Équipe d'investigation     Application terrain     Labo national
        │                       │                      │
        │ Formulaire            │                      │
        │ d'investigation       │                      │
        │──────────────────────▶│  Envoi résultats     │
        │                       │─────────────────────▶│
        │                       │                      │
        │                       │  Résultat labo       │
        │                       │◀─────────────────────│
        │                       │                      │
        │  Rapport d'investigation                      │
        │◀──────────────────────│                      │
```

**Profils mobilisés** :

| Profil | Rôle |
|--------|------|
| **PT-02** | Médiation (données terrain → FHIR) |
| **PT-04** | Résolution d'identité (patient investigateur + cas) |
| **PT-07** | Mapping (codes labo → LOINC) |
| **PT-12** | Traçabilité complète de l'investigation |

---

### Phase 4 — Riposte et coordination (EV-12)

**Objectif** : Déployer les mesures de contrôle : vaccination de masse, distribution de moustiquaires, campagne de communication, isolation.

```
Centre de commande (CMP-02)    CMP-06 (Médiation)    Districts/Régions
        │                            │                      │
        │ Plan de riposte            │                      │
        │ (activé)                   │                      │
        │───────────────────────────▶│  Instructions        │
        │                            │  aux districts       │
        │                            │─────────────────────▶│
        │                            │                      │
        │  État d'avancement         │  Rapports terrain    │
        │◀───────────────────────────│◀─────────────────────│
        │                            │                      │
        │  Dashboard temps réel      │                      │
        │───────────────────────────▶│  Affichage           │
        │                            │  centre de commande  │
```

**Profils mobilisés** :

| Profil | Rôle |
|--------|------|
| **PT-10** | Confiance (RBAC riposte, accès restreint) |
| **PT-15** | Surveillance One Health (si zoonose) |
| **PT-06** | Référentiel structures (localisation riposte) |
| **PT-12** | Audit des actions de riposte |

**Données échangées** :
- `Task` (FHIR) — tâches de riposte assignées
- `SupplyDelivery` — logistique intrants
- `Observation` — résultats de riposte (couverture vaccinale, etc.)

---

### Phase 5 — Suivi et clôture (EV-13)

**Objectif** : Suivre l'évolution de la situation et clore l'épisode quand la situation est sous contrôle.

```
Moteur analytique (CMP-04)    Centre de commande (CMP-02)
        │                            │
        │ Courbe épidémique           │
        │ en décrue                   │
        │───────────────────────────▶│
        │                            │  Recommandation
        │                            │  de clôture
        │                            │──────────────────▶ Comité
        │                            │                   de gestion
        │                            │                   de crise
        │                            │
        │  Validation clôture        │
        │◀───────────────────────────│
```

---

### Phase 6 — Capitalisation (EV-14)

**Objectif** : Documenter les leçons, mettre à jour les protocoles, renforcer la préparation.

```
Centre de commande (CMP-02)    Entrepôt (CMP-03)
        │                            │
        │  Bilan de l'épisode         │
        │  (structuré)                │
        │───────────────────────────▶│
        │                            │  Archivage +
        │                            │  analyse rétrospective
        │                            │
        │  Rapport final              │
        │───────────────────────────▶│  Publication
        │                            │  (DHIS2, OMS)
```

---

## Matrice de composition

| Étape | PT-02 | PT-04 | PT-06 | PT-07 | PT-08 | PT-10 | PT-12 | PT-15 |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| Détection (EV-09) | ● | ○ | — | ● | ● | — | ● | — |
| Notification (EV-10) | ● | — | — | — | — | ● | ● | — |
| Investigation (EV-11) | ● | ● | ○ | ● | — | — | ● | — |
| Riposte (EV-12) | — | — | ● | — | — | ● | ● | ●* |
| Suivi (EV-13) | — | — | — | — | ● | — | ● | — |
| Capitalisation (EV-14) | — | — | — | — | ● | — | ● | — |

*●* PT-15 applicable uniquement pour les zoonoses (One Health)

---

## Exigences transversales

| Exigence | Source | Applicable à |
|----------|--------|--------------|
| ENF-5 — Coordination processus complexes | ART-8a | Riposte coordonnée multi-districts |
| ART-5 — Qualité des données | ART-5 | Détection (seuils, complétude) |
| PT-15 — One Health | CAP-INT-14 | Si zoonose (peste, rage, Fièvre de la Vallée du Rift) |

---

## Liens

- [VS-02 — Prévenir, détecter et répondre aux risques sanitaires](../../00_caesn/01_value-streams/vs-02-risk-protection.md)
- [PT-02 — Médiation intra-secteur](../03_profils/pt-02-mediation-intra-secteur.md)
- [PT-08 — Échange données agrégées](../03_profils/pt-08-echange-donnees-agregees.md)
- [PT-10 — Confiance et autorisation](../03_profils/pt-10-confiance-authentification-autorisation.md)
- [PT-12 — Audit et traçabilité](../03_profils/pt-12-audit-provenance-traçabilité.md)
- [PT-15 — Surveillance One Health](../03_profils/pt-15-surveillance-one-health.md)
- [ENF-5 — Coordination processus complexes](../../referentiel/exigences/enf-5.md)
