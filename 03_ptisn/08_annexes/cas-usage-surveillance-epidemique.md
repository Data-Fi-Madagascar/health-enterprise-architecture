---
title: "Cas d'usage — Surveillance et riposte épidémique"
id: ptisn-cas-usage-surveillance
domain: 03_ptisn
version: "1.0.0"
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

## Objectif

Ce document montre comment les **profils techniques existants** composent pour couvrir le cycle complet de la surveillance et de la riposte épidémique : détection, notification, alerte, investigation, riposte et capitalisation.

## Principe architectural

Le cycle épidémique est un **cas d'usage métier** qui consomme plusieurs profils existants. Il ne nécessite pas de profil dédié car chaque étape mobilise des briques techniques déjà définies.

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

## Scénario — Cycle complet de surveillance épidémique

### Phase 1 — Détection et collecte (EV-09)

La phase de détection et de collecte vise à collecter les données de routine des formations sanitaires et des agents communautaires afin d'identifier les signaux sanitaires émergents. Les formations sanitaires transmettent leurs données cliniques au format FHIR `Observation` via la médiation (PT-02), qui assure la normalisation et la validation avant insertion dans l'entrepôt (CMP-03). Les agents communautaires transmettent leurs rapports mobiles — initialement collectés en mode hors ligne puis synchronisés — via la médiation vers le moteur analytique (CMP-04).

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

Les profils mobilisés sont le PT-08 (échange de données agrégées au format mADX avec l'OMS AFRO), le PT-02 (médiation sémantique pour la conversion des données terrain en FHIR), le PT-07 (mapping terminologique vers la CIM-10 et LOINC) et le PT-12 (traçabilité des événements de collecte). Les données échangées comprennent l'`Observation` FHIR (cas cliniques signalés), le `Bundle` mADX (données agrégées hebdomadaires) et le `Device` (capteurs IoT de météo et de vecteurs).

| Profil | Rôle |
|--------|------|
| **PT-08** | Échange de données agrégées (mADX) avec OMS AFRO |
| **PT-02** | Médiation sémantique (données terrain → FHIR) |
| **PT-07** | Mapping terminologique (CIM-10, LOINC) |
| **PT-12** | Traçabilité des événements de collecte |

### Phase 2 — Notification et alerte (EV-10)

La phase de notification et d'alerte consiste à notifier formellement un signal validé aux autorités compétentes et à déclencher l'alerte. Lorsque le moteur analytique (CMP-04) détecte un signal de dépassement de seuil conformément à l'ART-5, il transmet l'alerte au centre de commande (CMP-02). Ce dernier déclenche une alerte temps réel adressée au Ministère, au District et à l'OMS, puis notifie automatiquement l'issue de l'alerte au moteur analytique.

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

Les profils mobilisés sont le PT-10 (confiance et autorisation avec RBAC pour les alertes), le PT-02 (médiation pour le formatage des alertes) et le PT-12 (audit trail de la notification). Les données échangées comprennent le `Bundle` d'alerte (signal épidémique structuré) et la `Communication` FHIR (notification officielle).

| Profil | Rôle |
|--------|------|
| **PT-10** | Confiance et autorisation (RBAC, alertes) |
| **PT-02** | Médiation (formatage des alertes) |
| **PT-12** | Audit trail de la notification |

### Phase 3 — Investigation et confirmation (EV-11)

La phase d'investigation et de confirmation consiste à vérifier le signal sur le terrain, à prélever des échantillons et à confirmer ou infirmer le cas. L'équipe d'investigation transmet le formulaire d'investigation à l'application terrain, qui envoie les résultats au laboratoire national. Ce dernier retourne les résultats d'analyse, et l'équipe d'investigation élabore le rapport d'investigation final.

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

Les profils mobilisés sont le PT-02 (médiation pour la conversion des données terrain en FHIR), le PT-04 (résolution d'identité pour le patient investigateur et le cas), le PT-07 (mapping des codes laboratoire vers LOINC) et le PT-12 (traçabilité complète de l'investigation).

| Profil | Rôle |
|--------|------|
| **PT-02** | Médiation (données terrain → FHIR) |
| **PT-04** | Résolution d'identité (patient investigateur + cas) |
| **PT-07** | Mapping (codes labo → LOINC) |
| **PT-12** | Traçabilité complète de l'investigation |

### Phase 4 — Riposte et coordination (EV-12)

La phase de riposte et de coordination consiste à déployer les mesures de contrôle : vaccination de masse, distribution de moustiquaires, campagne de communication et isolation. Le centre de commande (CMP-02) active le plan de riposte et transmet les instructions aux districts et régions via la médiation (CMP-06). Les districts retournent les rapports d'avancement terrain, et le centre de commande diffuse un dashboard temps réel.

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

Les profils mobilisés sont le PT-10 (confiance avec RBAC riposte et accès restreint), le PT-15 (surveillance One Health pour les cas de zoonose), le PT-06 (référentiel des structures pour la localisation des actions de riposte) et le PT-12 (audit des actions de riposte). Les données échangées comprennent le `Task` FHIR (tâches de riposte assignées), le `SupplyDelivery` (logistique des intrants) et l'`Observation` (résultats de riposte tels que la couverture vaccinale).

| Profil | Rôle |
|--------|------|
| **PT-10** | Confiance (RBAC riposte, accès restreint) |
| **PT-15** | Surveillance One Health (si zoonose) |
| **PT-06** | Référentiel structures (localisation riposte) |
| **PT-12** | Audit des actions de riposte |

### Phase 5 — Suivi et clôture (EV-13)

La phase de suivi et de clôture consiste à suivre l'évolution de la situation épidémique et à clore l'épisode lorsque la situation est sous contrôle. Le moteur analytique (CMP-04) transmet la courbe épidémique en décrue au centre de commande (CMP-02), qui formule une recommandation de clôture au comité de gestion de crise. Après validation, la clôture est officialisée.

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

### Phase 6 — Capitalisation (EV-14)

La phase de capitalisation vise à documenter les leçons tirées, à mettre à jour les protocoles et à renforcer la préparation aux épisodes futurs. Le centre de commande (CMP-02) élabore un bilan structuré de l'épisode, qu'il transmet à l'entrepôt (CMP-03) pour archivage et analyse rétrospective. Le rapport final est ensuite publié via DHIS2 et transmis à l'OMS.

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

## Exigences transversales

| Exigence | Source | Applicable à |
|----------|--------|--------------|
| ENF-5 — Coordination processus complexes | ART-8a | Riposte coordonnée multi-districts |
| ART-5 — Qualité des données | ART-5 | Détection (seuils, complétude) |
| PT-15 — One Health | CAP-INT-14 | Si zoonose (peste, rage, Fièvre de la Vallée du Rift) |

## Liens

- VS-02 — Prévenir, détecter et répondre aux risques sanitaires
- PT-02 — Médiation intra-secteur
- PT-08 — Échange données agrégées
- PT-10 — Confiance et autorisation
- PT-12 — Audit et traçabilité
- PT-15 — Surveillance One Health
- ENF-5 — Coordination processus complexes

## Références

- **VS-02 — Prévenir, détecter et répondre aux risques sanitaires** — Prévenir, détecter et répondre aux risques sanitaires (`00_caesn/01_value-streams/vs-02-risk-protection.md`)
- **PT-02 — Médiation intra-secteur** — Profil technique national (`03_ptisn/03_profils/pt-02-mediation-intra-secteur.md`)
- **PT-08 — Échange données agrégées** — Profil technique national (`03_ptisn/03_profils/pt-08-echange-donnees-agregees.md`)
- **PT-10 — Confiance et autorisation** — Profil technique national (`03_ptisn/03_profils/pt-10-confiance-authentification-autorisation.md`)
- **PT-12 — Audit et traçabilité** — Profil technique national (`03_ptisn/03_profils/pt-12-audit-provenance-traçabilité.md`)
- **PT-15 — Surveillance One Health** — Surveillance One Health (`03_ptisn/03_profils/pt-15-surveillance-one-health.md`)
- **ENF-5 — Coordination processus complexes** — Coordination des processus complexes décentralisés et asynchrones (`referentiel/exigences/enf-5.md`)
