---
title: "Annexe E — SLA et métriques de performance par profil"
id: artsn-sla-performance
domain: 02_artsn
version: "1.0.0"
status: draft
last_reviewed: 2026-08-13
owner: DEPSI
tags: [artsn, annexe, SLA, performance, métriques, niveau-3]
---

# Annexe E — SLA et métriques de performance par profil

## Pour qui lire ce document

**Niveau :** niveau 3 — Architecture de Référence Technique de la Santé Numérique.

La lecture de ce document est **complémentaire** pour les décideurs institutionnels et les directions métier et programmes, et **prioritaire** pour l'équipe DEPSI et ses équipes techniques, les équipes SIS, données et suivi-évaluation, ainsi que les partenaires techniques et financiers. Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle.

## Objectif

Ce document définit les objectifs de niveau de service (SLA) et les métriques de performance pour chaque profil technique national. Ces indicateurs servent de base contractuelle pour les prestataires, de cibles opérationnelles pour les équipes techniques et de référentiel de monitoring pour le Centre national des systèmes d'information (CNSI).

## 1. Définitions

| Terme | Définition |
|-------|------------|
| **SLA** (Service Level Agreement) | Engagement formel sur le niveau de service fourni, mesuré par des indicateurs quantifiables |
| **Uptime** | Pourcentage de temps pendant lequel le service est disponible et opérationnel |
| **Latence** | Temps écoulé entre l'envoi d'une requête et la réception de la réponse complète |
| **Throughput** | Nombre de transactions traitées par unité de temps |
| **RTO** (Recovery Time Objective) | Durée maximale d'interruption acceptable en cas de panne |
| **RPO** (Recovery Point Objective) | Perte de données maximale acceptable (en temps) |

## 2. SLA globaux de la plateforme

| Métrique | Niveau 1 (critique) | Niveau 2 (important) | Niveau 3 (standard) |
|----------|---------------------|----------------------|---------------------|
| **Uptime** | 99,95% (< 22min/mois indispo) | 99,9% (< 44min/mois) | 99,5% (< 3,6h/mois) |
| **Latence P95** | < 500ms | < 2s | < 5s |
| **Throughput** | > 1000 req/s | > 100 req/s | > 10 req/s |
| **RTO** | < 15min | < 1h | < 4h |
| **RPO** | < 1min | < 5min | < 1h |
| **Disponibilité annuelle** | 99,9% | 99,5% | 99% |

## 3. SLA par profil technique

### 3.1 PT-01 — Échange interinstitutionnel

| Métrique | SLA | Mesure | Seuil d'alerte |
|----------|-----|--------|----------------|
| Latence transaction | < 2s (P95) | Temps de bout en bout | > 3s |
| Taux de succès | > 99,5% | Transactions réussies / total | < 99% |
| Taux de disponibilité | 99,95% | Uptime monthly | < 99,9% |
| File d'attente max | < 10 000 messages | Messages en attente | > 5 000 |
| Durée retention message | 72h avant échec | Avant rejet définitif | — |
| Taux de duplication | < 0,1% | Messages dupliqués | > 0,5% |

### 3.2 PT-02 — Médiation intra-secteur

| Métrique | SLA | Mesure | Seuil d'alerte |
|----------|-----|--------|----------------|
| Taux de transformation | > 98% | Données converties sans erreur | < 95% |
| Latence transformation | < 500ms | Par message | > 1s |
| Couverture mapping | > 95% | Codes mappés / codes reçus | < 90% |
| Taux d'erreur mapping | < 2% | Erreurs de conversion | > 5% |
| Disponibilité | 99,9% | Uptime monthly | < 99,5% |

### 3.3 PT-04 — Résolution d'identité

| Métrique | SLA | Mesure | Seuil d'alerte |
|----------|-----|--------|----------------|
| Latence recherche | < 500ms (P95) | Recherche par NIN | > 1s |
| Taux d'unicité | 100% | Pas de doublons | > 0 doublons |
| Taux de matching | > 95% | Résultats corrects / recherches | < 90% |
| Temps création NIN | < 3s | Depuis soumission | > 5s |
| Disponibilité | 99,95% | Uptime monthly | < 99,9% |
| Capacité | > 10 000 créations/jour | Nouveaux NIN | — |

### 3.4 PT-07 — Mapping terminologique

| Métrique | SLA | Mesure | Seuil d'alerte |
|----------|-----|--------|----------------|
| Couverture CIM-10 | > 98% | Codes mappés | < 95% |
| Couverture LOINC | > 95% | Codes mappés | < 90% |
| Temps de mapping | < 100ms | Par code | > 500ms |
| Taux d'ambiguïté | < 3% | Codes sans mapping unique | > 5% |
| Mise à jour référentiel | < 7 jours | Après publication OMS | > 14 jours |

### 3.5 PT-08 — Échange données agrégées

| Métrique | SLA | Mesure | Seuil d'alerte |
|----------|-----|--------|----------------|
| Fréquence collecte | Hebdomadaire (min) | Rapports reçus | > 7 jours retard |
| Taux de complétude | > 90% | Districts rapportant | < 80% |
| Latence publication | < 24h | Après date de clôture | > 48h |
| Volume | > 500 rapports/semaine | Rapports traités | < 200 |
| Disponibilité | 99,9% | Uptime monthly | < 99,5% |

### 3.6 PT-09 — Analytique et dashboards

| Métrique | SLA | Mesure | Seuil d'alerte |
|----------|-----|--------|----------------|
| Temps rafraîchissement | < 24h (J+1) | Données actualisées | > 48h |
| Temps chargement dashboard | < 5s | Affichage initial | > 10s |
| Taux de disponibilité | 99,5% | Uptime monthly | < 99% |
| Capacité utilisateur | > 500 utilisateurs simultanés | Sessions concourantes | < 200 |
| Taux d'erreur calcul | < 0,1% | Indicateurs erronés | > 0,5% |

### 3.7 PT-10 — Confiance et autorisation

| Métrique | SLA | Mesure | Seuil d'alerte |
|----------|-----|--------|----------------|
| Temps authentification | < 500ms (P95) | Login → jeton | > 1s |
| Temps autorisation | < 100ms | Vérification RBAC | > 200ms |
| Taux d'échec auth | < 1% | Tentatives échouées / total | > 3% |
| Durée jeton | 8h | Expiration | — |
| Temps révocation | < 30s | Révocation effective | > 60s |
| Journalisation | 100% | Événements tracés | < 99,9% |

### 3.8 PT-11 — Consentement

| Métrique | SLA | Mesure | Seuil d'alerte |
|----------|-----|--------|----------------|
| Temps vérification | < 200ms | Vérification consentement | > 500ms |
| Taux de conformité | 100% | Accès avec consentement valide | < 100% |
| Temps révocation | < 10s | Révocation effective | > 30s |
| Notification consent | < 5min | Patient notifié | > 15min |
| Journalisation | 100% | Opérations tracées | < 99,9% |

### 3.9 PT-12 — Audit et traçabilité

| Métrique | SLA | Mesure | Seuil d'alerte |
|----------|-----|--------|----------------|
| Couverture événements | 100% | Événements tracés | < 99,9% |
| Latence écriture | < 100ms | Écriture audit | > 200ms |
| Rétention | 5 ans minimum | Conservation logs | — |
| Requête audit | < 3s | Recherche dans les logs | > 10s |
| Immutabilité | 100% | Logs non modifiables | — |

### 3.10 PT-14 — Interopérabilité transfrontalière

| Métrique | SLA | Mesure | Seuil d'alerte |
|----------|-----|--------|----------------|
| Temps génération IPS | < 5s | Composition FHIR IPS | > 10s |
| Conformité IPS | 100% | Validation profil HL7 | < 100% |
| Temps vérification GDHCN | < 2s | Vérification certificat | > 5s |
| Taux succès échange | > 99% | IPS échangés avec succès | < 98% |
| Disponibilité GDHCN | 99,99% | Uptime Trust Anchor | < 99,9% |

### 3.11 PT-15 — Surveillance One Health

| Métrique | SLA | Mesure | Seuil d'alerte |
|----------|-----|--------|----------------|
| Latence collecte zoonose | < 1h | Données OIE/FAO reçues | > 2h |
| Corrélation espèces | > 90% | Cas humains-animaux corrélés | < 80% |
| Disponibilité | 99,5% | Uptime monthly | < 99% |
| Intégration mADX | < 24h | Données intégrées | > 48h |

## 4. Métriques transversales

### 4.1 Qualité des données

| Métrique | SLA | Description |
|----------|-----|-------------|
| Complétude | > 95% | Champs obligatoires remplis |
| Exactitude | > 98% | Données validées par les règles métier |
| Cohérence | > 99% | Données cohérentes entre systèmes |
| Fraîcheur | < 24h | Données actualisées en J+1 |
| Unicité | 100% | Pas de doublons pour les entités clés |

### 4.2 Sécurité

| Métrique | SLA | Description |
|----------|-----|-------------|
| Incidents sécurité / mois | < 2 | Incidents critiques et majeurs |
| Temps de réponse incident | < 15min | Détection à action |
| Vulnérabilités non corrigées | 0 (critiques) | Vulnérabilités CVSS > 9 |
| Audit sécurité | Trimestriel | Revue complète |
| Conformité RBAC | 100% | Tous les accès autorisés |

### 4.3 Expérience utilisateur

| Métrique | SLA | Description |
|----------|-----|-------------|
| Temps de réponse UI | < 3s | Affichage page |
| Taux d'erreur utilisateur | < 1% | Erreurs affichées / interactions |
| Satisfaction utilisateurs | > 80% | Enquête annuelle |
| Temps de formation | < 2 jours | Nouvel utilisateur opérationnel |
| Disponibilité support | 8h/24, 6j/7 | Assistance technique |

## 5. Monitoring et alerting

### 5.1 Architecture de monitoring

```
┌─────────────────────────────────────────────────────────────┐
│                 MONITORING NATIONAL                         │
│                                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ Métriques│  │ Logs     │  │ Traces   │  │ Alertes  │   │
│  │ (Prom.)  │  │ (ELK)    │  │ (Jaeger) │  │ (AlertM) │   │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘   │
│       │             │             │             │           │
│       └─────────────┼─────────────┼─────────────┘           │
│                     │             │                         │
│              ┌──────▼──────┐ ┌────▼─────┐                   │
│              │  Dashboard  │ │ Notification│                  │
│              │  (Grafana)  │ │  (SMS/Email)│                  │
│              └─────────────┘ └───────────┘                   │
└─────────────────────────────────────────────────────────────┘
```

### 5.2 Niveaux d'alerte

| Niveau | Couleur | Temps de réponse | Exemple |
|--------|---------|------------------|---------|
| **P1 — Critique** | Rouge | < 15min | Service indisponible, faille sécurité |
| **P2 — Majeur** | Orange | < 1h | Dégradation performance, erreurs > 5% |
| **P3 — Mineur** | Jaune | < 4h | Avertissement, tendance dégradante |
| **P4 — Info** | Bleu | Quotidien | Information, tendance positive |

### 5.3 Canaux de notification

| Canal | Usage | Disponibilité |
|-------|-------|---------------|
| **SMS** | Alertes P1/P2 aux responsables | 24/7 |
| **Email** | Rapports quotidiens, alertes P3 | 24/7 |
| **Dashboard** | Monitoring en temps réel | 24/7 |
| **Téléphone** | Escalade P1 uniquement | 24/7 |
| **Rapport hebdo** | Synthèse performance | Hebdomadaire |

## 6. Reporting et revue

### 6.1 Rapports automatisés

| Rapport | Fréquence | Destinataires | Contenu |
|---------|-----------|---------------|---------|
| **Quotidien** | 8h00 | Équipes techniques | Statut services, alertes P1/P2 |
| **Hebdomadaire** | Lundi 9h00 | Direction technique | SLA atteints, incidents, tendances |
| **Mensuel** | 1er du mois | Comité de pilotage | SLA globaux, évolutions, recommandations |
| **Trimestriel** | Fin trimestre | Direction ministérielle | Bilan performance, investissements |

### 6.2 Revue de service

| Événement | Fréquence | Participants | Objectif |
|-----------|-----------|-------------|----------|
| **Revue quotidienne** | Quotidienne | Équipes ops | Point blocages, actions immédiates |
| **Revue hebdomadaire** | Hebdomadaire | Techniques + métier | Bilan semaine, planification |
| **Revue mensuelle** | Mensuelle | Comité pilotage | SLA, budget, risques |
| **Revue trimestrielle** | Trimestrielle | Direction + partenaires | Stratégie, investissements |

## Liens

Les liens utiles pour approfondir ce document sont les suivants : le chapitre ART-7 — Sécurité, contrôle d'accès et résidence, le Protocole de test, la Feuille de route et le Plan de migration.

## Références

- **ART-7 — Sécurité, contrôle d'accès et résidence** — Sécurité, contrôle d'accès et résidence de la donnée (`referentiel/chapitres/art-7.md`)
- **Protocole de test** — Annexe D — Protocole de test d'interopérabilité (`02_artsn/07_annexes/d-protocole-test-interopabilite.md`)
- **Feuille de route** — Feuille de route de déploiement progressif de l'ARTSN (`02_artsn/09_feuille-route/index.md`)
- **Plan de migration** — Plan de migration — De l'existant au futur état (`00_caesn/06_portfolio/migration-existant.md`)
