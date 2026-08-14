---
title: "Annexe D — Protocole de test d'interopérabilité"
id: artsn-protocole-test
domain: 02_artsn
version: "0.1"
status: draft
last_reviewed: 2026-08-13
owner: DEPSI
tags: [artsn, annexe, test, interopérabilité, validation, niveau-3]
---

# Annexe D — Protocole de test d'interopérabilité

## Pour qui lire ce document

**Niveau :** niveau 3 — Architecture de Référence Technique de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ○ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ● |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle.

---

## Objectif

Ce document définit le protocole de validation de l'interopérabilité entre les profils techniques nationaux (PTISN). Il fournit les scénarios de test, les critères de succès et les procédures de certification pour garantir que les briques techniques composent correctement entre elles.

---

## 1. Principes de test

### 1.1 Niveaux de test

| Niveau | Objectif | Exigence |
|--------|----------|----------|
| **N1 — Conformité** | Vérifier qu'un profil respecte son contrat d'interface | Obligatoire avant mise en production |
| **N2 — Composabilité** | Vérifier que deux profils s'assemblent correctement | Obligatoire pour tout couple de profils utilisés ensemble |
| **N3 — bout-en-bout** | Vérifier un scénario métier complet (use case) | Obligatoire pour chaque cas d'usage (VS-01 à VS-04) |
| **N4 — charge** | Vérifier les performances en conditions réelles | Recommandé avant déploiement national |

### 1.2 Règles de test

1. **Indépendance** : chaque test est exécuté de manière isolée, sans dépendance aux résultats des tests précédents
2. **Reproductibilité** : les tests doivent produire le même résultat quel que soit l'environnement
3. **Traçabilité** : chaque test est identifié par un code unique et tracer ses résultats
4. **Automatisation** : les tests N1 et N2 doivent pouvoir être automatisés via des scripts
5. **Régression** : tout correctif de bug doit être accompagné d'un test de régression

---

## 2. Scénarios de test par profil

### 2.1 PT-01 — Échange interinstitutionnel

| Code test | Scénario | Données d'entrée | Résultat attendu | Critère de succès |
|-----------|----------|-------------------|------------------|-------------------|
| PT01-T01 | Envoi d'un message FHIR entre deux systèmes | Bundle FHIR valide | Accusé de réception (202 Accepted) | Temps de réponse < 2s |
| PT01-T02 | Envoi d'un message invalide | Bundle FHIR malformé | Erreur 400 Bad Request | Message d'erreur explicite |
| PT01-T03 | Envoi en mode dégradé (hors-ligne) | Message + état hors-ligne | File d'attente locale | Synchronisation différée < 5min |
| PT01-T04 | Routage multi-destinataires | Message + 3 destinataires | 3 copies acheminées | Aucune perte, traçabilité complète |

### 2.2 PT-02 — Médiation intra-secteur

| Code test | Scénario | Données d'entrée | Résultat attendu | Critère de succès |
|-----------|----------|-------------------|------------------|-------------------|
| PT02-T01 | Transformation CSB → FHIR | Données CSB (format local) | Ressource FHIR valide | Conformité profil HL7 |
| PT02-T02 | Normalisation terminologique | Code CIM-9 local | Code CIM-10 validé | Taux de mapping > 98% |
| PT02-T03 | Médiation multi-format | HL7v2 + CSV + FHIR | Bundle FHIR normalisé | Aucune perte sémantique |
| PT02-T04 | Gestion des erreurs de mapping | Code sans équivalent | Warning + valeur conservée | Pas de rejet, traçabilité |

### 2.3 PT-04 — Résolution d'identité

| Code test | Scénario | Données d'entrée | Résultat attendu | Critère de succès |
|-----------|----------|-------------------|------------------|-------------------|
| PT04-T01 | Recherche patient existant | NIN valide | Dossier patient complet | Temps de réponse < 500ms |
| PT04-T02 | Création nouveau patient | Données démographiques complètes | NIN attribué | Unicité garantie |
| PT04-T03 | Détection de doublon | Données similaires à un existant | Alerte doublon | Taux de faux positifs < 5% |
| PT04-T04 | Recherche floue (nom partiel) | Nom + commune | Liste de candidats | Précision > 90% |

### 2.4 PT-10 — Confiance et autorisation

| Code test | Scénario | Données d'entrée | Résultat attendu | Critère de succès |
|-----------|----------|-------------------|------------------|-------------------|
| PT10-T01 | Authentification réussie | Identifiants valides | Jeton JWT | Durée jeton = 8h |
| PT10-T02 | Authentification échouée | Mauvais mot de passe | Erreur 401 | Verrouillage après 5 tentatives |
| PT10-T03 | Accès autorisé | Jeton valide + rôle approprié | Données retournées | Autorisation < 100ms |
| PT10-T04 | Accès refusé | Jeton valide mais rôle insuffisant | Erreur 403 | Journalisation de la tentative |
| PT10-T05 | Jeton expiré | Jeton périmé | Erreur 401 | Redirection vers renouvellement |
| PT10-T06 | Révocation temps réel | Jeton révoqué manuellement | Erreur 401 immédiate | Délai de propagation < 30s |

### 2.5 PT-11 — Consentement

| Code test | Scénario | Données d'entrée | Résultat attendu | Critère de succès |
|-----------|----------|-------------------|------------------|-------------------|
| PT11-T01 | Consentement accordé | Patient consent + scope | Accès autorisé | Traçabilité du consentement |
| PT11-T02 | Consentement refusé | Patient refuse l'accès | Accès bloqué | Message explicatif au demandeur |
| PT11-T03 | Consentement expiré | Date de fin dépassée | Accès bloqué | Notification au patient |
| PT11-T04 | Révocation de consentement | Patient révoque | Accès immédiatement bloqué | Notification aux destinataires |

### 2.6 PT-14 — Interopérabilité transfrontalière

| Code test | Scénario | Données d'entrée | Résultat attendu | Critère de succès |
|-----------|----------|-------------------|------------------|-------------------|
| PT14-T01 | Émission IPS | Dossier patient national | Composition IPS conforme | Validation contre profil HL7 IPS |
| PT14-T02 | Vérification GDHCN | IPS + certificat | Statut de confiance vérifié | Vérification < 2s |
| PT14-T03 | Échange transfrontalier | IPS vers pays partenaire | Accusé de réception pays | Protocole bilingue (FR/EN) |
| PT14-T04 | Rejet IPS non conforme | IPS avec sections manquantes | Erreur de validation | Liste des sections manquantes |

---

## 3. Scénarios de test bout-en-bout (use cases)

### 3.1 VS-01 — Référence / Évacuation

| Code test | Scénario | Étapes | Résultat attendu |
|-----------|----------|--------|------------------|
| VS01-E2E-01 | Référence CSB → Hôpital | 1. CSB crée ServiceRequest → 2. Médiation transforme → 3. Hôpital reçoit et accepte → 4. IPS transmis | Parcours complet en < 5min |
| VS01-E2E-02 | Contre-référence Hôpital → CSB | 1. Hôpital émet retour + CR → 2. CSB reçoit → 3. Plan de suivi validé | Données cohérentes aller-retour |
| VS01-E2E-03 | Évacuation nationale urgente | 1. ServiceRequest URGENCE → 2. Routage auto → 3. Destination accepte → 4. Transport lancé → 5. Arrivée confirmée | Temps total < 30min (hors transport) |
| VS01-E2E-04 | Évacuation internationale | 1. Demande EVA-I → 2. Vérification GDHCN → 3. Accord bilatéral → 4. IPS transmis → 5. Acceptation | Conformité IPS validée |

### 3.2 VS-02 — Surveillance épidémique

| Code test | Scénario | Étapes | Résultat attendu |
|-----------|----------|--------|------------------|
| VS02-E2E-01 | Détection signal → Notification | 1. Agent déclare signal → 2. Médiation valide → 3. Notification auto district | Notification < 1h après détection |
| VS02-E2E-02 | Seuil dépassé → Alerte | 1. Indicateur > seuil → 2. Alerte déclenchée → 3. Notif. ministère + OMS | Alerte < 15min après dépassement |
| VS02-E2E-03 | Investigation → Confirmation | 1. Équipe enquête → 2. Résultat labo → 3. Cas confirmé → 4. Mise à jour dashboard | Données cohérentes terrain/labo |
| VS02-E2E-04 | Riposte coordonnée | 1. Plan activé → 2. Tâches assignées → 3. Suivi avancement → 4. Clôture | Tâches traçables de bout en bout |

### 3.3 VS-03 — Couverture sanitaire

| Code test | Scénario | Étapes | Résultat attendu |
|-----------|----------|--------|------------------|
| VS03-E2E-01 | Identification bénéficiaire | 1. Inscription Fokontany → 2. NIN attribué → 3. Carte électronique | NIN unique et vérifié |
| VS03-E2E-02 | Vérification éligibilité → Exemption | 1. Recherche patient → 2. Vérif. couverture → 3. Exemption validée → 4. Soins dispensés | Réponse éligibilité < 3s |
| VS03-E2E-03 | Facturation → Remboursement | 1. Claim soumis → 2. Validation → 3. Instruction → 4. Paiement | Cycle complet < 30 jours |
| VS03-E2E-04 | Audit fraude | 1. Données agrégées → 2. Détection anomalies → 3. Investigation | Patterns suspects identifiés |

### 3.4 VS-04 — Pilotage système

| Code test | Scénario | Étapes | Résultat attendu |
|-----------|----------|--------|------------------|
| VS04-E2E-01 | Collecte → Dashboard | 1. Données terrain → 2. Agrégation → 3. Indicateurs → 4. Dashboard | Données actualisées en J+1 |
| VS04-E2E-02 | Alerte performance | 1. Indicateur < seuil → 2. Alerte direction → 3. Validation | Alerte < 1h après dérive |
| VS04-E2E-03 | Rapport annuel | 1. Consolidation annuelle → 2. Production rapport → 3. Publication | Rapport conforme aux standards |

---

## 4. Environnement de test

### 4.1 Configuration minimale

| Composant | Spécification |
|-----------|---------------|
| Serveur FHIR | HAPI FHIR R4 (ou équivalent) |
| Base de données | PostgreSQL 14+ |
| Annuaire | LDAP ou OpenID Connect |
| Réseau | LAN dédié au test (pas de production) |
| Données | Jeux de données de test standardisés (anonymisés) |

### 4.2 Données de test

| Jeu de données | Contenu | Utilisation |
|----------------|---------|-------------|
| **TD-01** | 100 patients, 50 formations sanitaires | Tests de base (N1, N2) |
| **TD-02** | 1000 patients, 200 formations, couverture multi-programme | Tests de charge (N4) |
| **TD-03** | Cas limites (doublons, données incomplètes, codes inconnus) | Tests de robustesse |
| **TD-04** | Données transfrontalières (IPS, accords bilatéraux) | Tests PT-14 |

### 4.3 Outils recommandés

| Outil | Usage |
|-------|-------|
| **HAPI FHIR Tester** | Validation de conformité FHIR |
| **Postman / Newman** | Tests d'API automatisés |
| **JMeter** | Tests de charge |
| **Schematron** | Validation de profils FHIR |
| **Certif** (HL7) | Validation de conformité IPS |

---

## 5. Critères de certification

### 5.1 Niveaux de certification

| Niveau | Label | Critères |
|--------|-------|----------|
| **Conforme** | PT-XX-C | Tests N1 passés à 100% |
| **Interopérable** | PT-XX-I | Tests N1 + N2 passés à 100% |
| **Production** | PT-XX-P | Tests N1 + N2 + N3 passés, N4 recommandé |

### 5.2 Procédure de certification

```
1. Candidat soumet demande + preuves de test
2. Vérification indépendante (labo de test accrédité)
3. Comité de validation examine les résultats
4. Délivrance du label (valable 12 mois)
5. Audit annuel de renouvellement
```

### 5.3 Non-conformités bloquantes

| Type | Exemple | Action |
|------|---------|--------|
| **Bloquante** | Perte de données, faille sécurité | Rejet immédiat, correction obligatoire |
| **Majeure** | Temps de réponse > SLA, mapping erroné | Correction sous 30 jours |
| **Mineure** | Message d'erreur non explicite | Correction sous 90 jours |

---

## 6. Plan de test par phase de déploiement

| Phase | Profils testés | Niveaux requis | Échéance |
|-------|----------------|----------------|----------|
| **Phase 1** (T4 2026) | PT-01, PT-02, PT-04 | N1 + N2 | Nov 2026 |
| **Phase 2** (T1 2027) | PT-07, PT-10, PT-12 | N1 + N2 | Fév 2027 |
| **Phase 3** (T2 2027) | PT-03, PT-05, PT-06, PT-08 | N1 + N2 | Mai 2027 |
| **Phase 4** (T3 2027) | PT-09, PT-11, PT-13 | N1 + N2 | Août 2027 |
| **Phase 5** (T4 2027) | PT-14 | N1 + N2 + N3 | Nov 2027 |
| **Phase 6** (T1 2028) | PT-15 | N1 + N2 | Fév 2028 |
| **Validation bout-en-bout** | Tous | N3 | T2 2028 |
| **Tests de charge** | Tous | N4 | T3 2028 |

---

## Liens

- [ART-7 — Sécurité, contrôle d'accès et résidence](../../referentiel/chapitres/art-7.md)
- [PT-10 — Confiance et autorisation](../../03_ptisn/03_profils/pt-10-confiance-authentification-autorisation.md)
- [Feuille de route](../09_feuille-route/index.md)
- [Cartographie cible](../04_cartographie-cible/index.md)
