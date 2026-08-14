---
title: "Veille architecturale"
id: veille-architecturale
domain: 02_artsn
version: "0.1"
status: draft
last_reviewed: 2026-08-13
owner: DEPSI
tags: [artsn, gouvernance, veille, standards, tendances, niveau-3]
---

# Veille architecturale

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

## Objet

Ce document définit le processus de veille architecturale pour maintenir l'ARTSN alignée sur les standards en vigueur, les évolutions technologiques et les besoins métier émergents. La veille alimente le processus de décision du CNASN et garantit la pertinence continue du cadre.

---

## 1. Périmètre de la veille

### 1.1 Domaines de veille

| Domaine | Sujet | Priorité |
|---------|-------|----------|
| **Standards de données** | HL7 FHIR, IHE, CIM-10, LOINC, SNOMED CT | Haute |
| **Interopérabilité** | X-Road, mADX, GDHCN, API REST | Haute |
| **Sécurité** | OAuth 2.0, OpenID Connect, chiffrement, zero-trust | Haute |
| **Souveraineté** | RGPD-like, protection des données, hébergement | Haute |
| **Tendances technologiques** | IA en santé, IoT médical, blockchain, FHIR R6 | Moyenne |
| **Réglementation** | Lois nationales, accords SADC, politiques OMS | Haute |
| **Concurrence** | Architectures similaires (Sénégal, Rwanda, Tunisie) | Basse |

### 1.2 Sources de veille

| Source | Type | Fréquence | Responsable |
|--------|------|-----------|-------------|
| **HL7 International** | Standard FHIR, IG, ballotages | Continue | DEPSI |
| **IHE International** | Profils d'intégration | Trimestriel | DEPSI |
| **OMS / OMS-AFRO** | Politiques santé, standards numériques | Mensuel | DEPSI |
| **Banque Mondiale** | Projets eHealth, financements | Trimestriel | BRV |
| **SADC / AMSP** | Interopérabilité régionale | Trimestriel | DEPSI |
| **OMS GDHCN** | Confiance numérique | Mensuel | DEPSI |
| **DHIS2 Community** | Évolutions DHIS2, mADX | Mensuel | DEPSI |
| **OpenHIE** | Patterns d'interopérabilité | Trimestriel | DEPSI |
| **GovStack** | Standards gouvernementaux | Semestriel | DEPSI |
| **Articles scientifiques** | Recherche en eHealth | Trimestriel | DEPSI |
| **Pays similaires** | Retours d'expérience | Semestriel | DEPSI |

---

## 2. Processus de veille

### 2.1 Collecte

| Étape | Action | Responsable | Fréquence |
|-------|--------|-------------|-----------|
| 2.1.1 | Consulter les sources identifiées | Chargé de veille | Continue |
| 2.1.2 | Enregistrer les veilles dans la fiche | Chargé de veille | À chaque découverte |
| 2.1.3 | Classifier par domaine et priorité | Chargé de veille | À chaque découverte |

### 2.2 Analyse

| Étape | Action | Responsable | Fréquence |
|-------|--------|-------------|-----------|
| 2.2.1 | Évaluer l'impact sur l'ARTSN | Comité technique | Trimestriel |
| 2.2.2 | Identifier les actions requises | Comité technique | Trimestriel |
| 2.2.3 | Prioriser les actions | CNASN | Trimestriel |

### 2.3 Intégration

| Étape | Action | Responsable | Fréquence |
|-------|--------|-------------|-----------|
| 2.3.1 | Soumettre les modifications au CNASN | Chargé de veille | Selon priorité |
| 2.3.2 | Mettre à jour l'ARTSN si nécessaire | DEPSI | Après décision |
| 2.3.3 | Communiquer les changements | CNASN | Après publication |

---

## 3. Fiche de veille

### 3.1 Template

| Champ | Description |
|-------|-------------|
| **ID** | VEE-XXXX (numéro séquentiel) |
| **Date** | Date de découverte |
| **Source** | Source de l'information |
| **Domaine** | Standards, interopérabilité, sécurité, souveraineté, tendances, réglementation |
| **Titre** | Résumé en une phrase |
| **Description** | Détail de l'évolution détectée |
| **Impact ARTSN** | Nul / Faible / Moyen / Élevé / Critique |
| **Composant impacté** | Chapitre, profil, fondation concerné(s) |
| **Action recommandée** | Aucune / Veille / Modification / Nouvelle ADR |
| **Statut** | Nouveau / En analyse / Traité / Archivé |

### 3.2 Exemples de fiches

| ID | Date | Source | Titre | Impact | Action |
|----|------|--------|-------|--------|--------|
| VEE-0001 | 2026-08-13 | HL7 | Publication FHIR R6 (draft) | Élevé | Veille — analyse impact |
| VEE-0002 | 2026-08-13 | IHE | Nouveau profil mCSD pour le community health | Moyen | Veille — à évaluer |
| VEE-0003 | 2026-08-13 | OMS | Mise à jour GDHCN v2.0 | Élevé | Modification PT-14 |

---

## 4. Revue trimestrielle

### 4.1 Ordre du jour type

1. **Bilan des veilles** : nombre de fiches, répartition par domaine
2. **Impact ARTSN** : modifications à programmer
3. **Standards émergents** : technologies à surveiller
4. **Pays similaires** : retours d'expérience pertinentes
5. **Plan d'action** : priorités du trimestre suivant

### 4.2 Participants

| Rôle | Participation |
|------|---------------|
| Chargé de veille | Présentation |
| Comité technique | Analyse |
| CNASN | Décision |
| DEPSI | Compte-rendu |

### 4.3 Livrables

| Livrable | Description |
|----------|-------------|
| **Rapport de veille trimestriel** | Synthèse des veilles et impacts |
| **Plan d'action** | Modifications à programmer |
| **Mise à jour des fiches** | Statuts et actions |

---

## 5. Intégration avec les autres processus

| Processus | Lien avec la veille |
|-----------|---------------------|
| **Décisions d'architecture (ADR)** | La veille alimente les propositions d'ADR |
| **Homologation** | La veille informe les critères de conformité |
| **Dépréciation** | La veille détecte les standards abandonnés |
| **Roadmap** | La veille influence la priorisation |

---

## Liens

- [Gouvernance ARTSN](./index.md)
- [Processus de dépréciation](./depreciation.md)
- [Registre des décisions](../../00_caesn/08_decisions/registre-decisions.md)
- [Feuille de route](../09_feuille-route/index.md)
