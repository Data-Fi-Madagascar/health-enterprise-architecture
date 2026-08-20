---

title: "Workflow d'homologation architecturale"
id: homologation
domain: 07_governance
version: "1.0.0"
status: draft
last_reviewed: 2026-08-13
owner: CNASN
tags: ["gouvernance", "homologation", "workflow", "conformité", "niveau-2"]
---

# Workflow d'homologation architecturale

## Pour qui lire ce document

**Niveau :** niveau 1 : Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ● |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle.

---

## Objet

Ce document définit le workflow concret d'homologation des initiatives numériques sanitaires. Il transforme les principes de gouvernance en étapes opérationnelles avec des livrables, des délais et des responsabilités clairement définis.

---

## 1. Périmètre de l'homologation

Toute initiative numérique sanitaire recevant un financement public ou utilisant des infrastructures nationales doit être homologuée par le CNASN avant sa mise en production.

**Sont soumis à homologation :**
- Nouvelles applications ou plateformes
- Intégrations avec la plateforme nationale d'échange (X-Road)
- Utilisation de données du référentiel national (INP, formations sanitaires)
- Échanges de données cliniques ou de surveillance
- Projets de migration de systèmes existants

**Sont exemptés d'homologation complète (vérification simplifiée) :**
- Mises à jour correctives sans changement fonctionnel
- Outils internes ne touchant pas de données patient
- Pilotes limités (< 3 mois, < 2 formations sanitaires)

---

## 2. Checklist d'homologation

### 2.1 Critères obligatoires

| # | Critère | Question de vérification | Preuve attendue |
|---|---------|--------------------------|-----------------|
| **C1** | Alignement flux de valeur | L'initiative contribue-t-elle à un flux VS-01 à VS-04 ? | Cartographie flux initiative → capabilité |
| **C2** | Renforcement capabilité | L'initiative renforce-t-elle au moins une capabilité CAESN/CNISN ? | Fiche capabilité avec delta de maturité |
| **C3** | Standards d'interopérabilité | Utilise-t-elle les standards approuvés (FHIR, mADX, etc.) ? | Matrice standards utilisés |
| **C4** | Connexion X-Road | Les échanges inter-systèmes passent-ils par X-Road ? | Architecture d'intégration |
| **C5** | Sécurité et RBAC | Le RBAC PT-10 est-il implémenté ? | Matrice rôles/permissions |
| **C6** | Consentement | Le consentement patient (PT-11) est-il géré ? | Architecture du module consentement |
| **C7** | Souveraineté données | Les données sont-elles hébergées sur le territoire national (Madagascar) ou dans un environnement conforme à la résidence des données exigée par le cadre ? | Plan d'hébergement |
| **C8** | Identité nationale | Utilise-t-elle l'INP (pas d'ID parallèle) ? | Architecture identité |
| **C9** | Traçabilité | L'audit trail (PT-12) est-il implémenté ? | Architecture journalisation |
| **C10** | Coût total de possession | Le budget est-il réaliste et soutenable ? | Business case 5 ans |
| **C11** | Plan de migration | La transition depuis l'existant est-elle planifiée ? | Plan de migration documenté |
| **C12** | Indicateurs de valeur | Les KPI de mesure sont-ils définis ? | Tableau de bord indicateurs |

### 2.2 Critères complémentaires (selon contexte)

| # | Critère | Applicable si |
|---|---------|---------------|
| **C13** | IPS transfrontalier | Échange avec un pays étranger |
| **C14** | One Health | Données animales/environnementales |
| **C15** | Mode dégradé | Zone à connectivité limitée |
| **C16** | Accessibilité | Application grand public |

> **Cohérence inter-niveaux.** Cette checklist d'admission (niveau 1) se superpose aux 13 dimensions de conformité du CNISN (`01_cnisn/04_conformite/index.md` §3) et aux 5 portes architecturales de l'ARTSN. L'autorité d'homologation unique est le **CNASN** ; les critères ne sont pas redondants mais déclinés par couche (voir l'articulation détaillée en §3.1 du CNISN).

---

## 3. Matrice de décision

### 3.1 Par conformité

| Conformité | Impact faible | Impact moyen | Impact élevé |
|------------|---------------|--------------|--------------|
| **12/12 critères** | Validation directe (N1) | Validation N2 | Validation N3 |
| **10-11/12** | Validation N1 + plan corrective | Validation N2 + plan corrective | Validation N3 + plan corrective |
| **8-9/12** | Plan corrective + validation N2 | Rejet, nouvelle soumission | Rejet, refonte |
| **< 8/12** | Rejet | Rejet | Rejet |

### 3.2 Par type d'initiative

| Type d'initiative | Niveau de validation | Délai cible |
|-------------------|---------------------|-------------|
| **Pilote** (< 3 mois, < 2 sites) | N1 seule | 2 semaines |
| **Déploiement régional** | N1 + N2 | 4 semaines |
| **Déploiement national** | N1 + N2 + N3 | 6 semaines |
| **Système critique** (données patient à grande échelle) | N1 + N2 + N3 + audit sécurité | 8 semaines |

---

## 4. Workflow détaillé

### 4.1 Phase 1 : Constitution du dossier (Auteur)

| Étape | Action | Livrable | Délai |
|-------|--------|----------|-------|
| 1.1 | Remplir la checklist d'homologation | Checklist complétée | 5 jours |
| 1.2 | Joindre les preuves techniques | Dossier technique | 5 jours |
| 1.3 | Soumettre au secrétariat CNASN | Dossier complet | 1 jour |

### 4.2 Phase 2 : Instruction (Secrétariat CNASN)

| Étape | Action | Livrable | Délai |
|-------|--------|----------|-------|
| 2.1 | Vérifier la complétude du dossier | Rapport de complétude | 2 jours |
| 2.2 | Affecter au comité technique | Fiche d'affectation | 1 jour |
| 2.3 | Planifier la revue | Ordre du jour | 2 jours |

### 4.3 Phase 3 : Revue technique (Comité technique)

| Étape | Action | Livrable | Délai |
|-------|--------|----------|-------|
| 3.1 | Analyser la conformité aux critères | Grille d'analyse | 5 jours |
| 3.2 | Identifier les écarts | Liste des écarts | 2 jours |
| 3.3 | Rédiger le rapport de revue | Rapport technique | 3 jours |
| 3.4 | Recommander (approuver / rejeter / dérogation) | Recommandation | 1 jour |

### 4.4 Phase 4 : Décision (CNASN)

| Étape | Action | Livrable | Délai |
|-------|--------|----------|-------|
| 4.1 | Examiner le rapport de revue | Notes de préparation | 2 jours |
| 4.2 | Statuer en réunion | Décision CNASN | 1 jour |
| 4.3 | Si dérogation : instruire le dossier | Note de dérogation | 3 jours |
| 4.4 | Si N3 requis : soumettre à la direction | Note stratégique | 5 jours |

### 4.5 Phase 5 : Publication (DEPSI)

| Étape | Action | Livrable | Délai |
|-------|--------|----------|-------|
| 5.1 | Enregistrer la décision | ADR ou rapport d'homologation | 1 jour |
| 5.2 | Mettre à jour le registre | Registre mis à jour | 1 jour |
| 5.3 | Communiquer aux parties prenantes | Notification | 1 jour |

---

## 5. Rôles et responsabilités

| Rôle | Responsabilité dans l'homologation |
|------|-------------------------------------|
| **Auteur de l'initiative** | Constitue le dossier, fournit les preuves, corrige les écarts |
| **Relecteur technique** | Vérifie la conformité technique, identifie les risques |
| **Secrétariat CNASN** | Instruit le dossier, planifie les revues, gère le registre |
| **Comité technique CNASN** | Analyse la conformité, recommande une décision |
| **Président CNASN** | Statue sur l'homologation ou la dérogation |
| **BRV** | Valide l'impact business si nécessaire |
| **Secrétaire Général** | Approuve les systèmes critiques et les dérogations majeures |

---

## 6. Cas types

### 6.1 Homologation standard

```
Dossier complet → Conforme (12/12) → Approuvé → Publié
Durée totale : 4 semaines
```

### 6.2 Homologation avec écarts mineurs

```
Dossier complet → Écarts (10-11/12) → Plan corrective → Approuvé sous réserve
Durée totale : 6 semaines
```

### 6.3 Dérogation temporaire

```
Dossier avec dérogation → Instruit → Approuvé (durée limitée) → Suivi trimestriel
Durée totale : 6 semaines + suivi
```

### 6.4 Rejet

```
Dossier incomplet ou non conforme (< 8/12) → Rejet → Nouvelle soumission après correction
Durée totale : variable
```

---

## 7. Indicateurs de performance du processus

| Indicateur | Cible | Mesure |
|------------|-------|--------|
| Délai moyen d'homologation | < 4 semaines | Date soumission → date décision |
| Taux de première soumission conforme | > 70% | Dossiers complets / total |
| Taux d'homologation | > 80% | Dossiers approuvés / total |
| Taux de dérogation | < 15% | Dérogations / total |
| Taux de rejet | < 10% | Rejets / total |
| Satisfaction des demandeurs | > 80% | Enquête post-processus |

---

## Liens

- Guide du processus de gouvernance
- RACI de gouvernance
- Registre des décisions
- Template de modification

## Références

- **Guide du processus de gouvernance** : Guide du processus de gouvernance (`00_caesn/07_governance/processus-gouvernance.md`)
- **RACI de gouvernance** : RACI de gouvernance et responsabilités (`00_caesn/07_governance/raci.md`)
- **Registre des décisions** : Registre des décisions d'architecture (ADR) (`01_cnisn/06_decisions/registre-decisions.md`)
- **Template de modification** : Template : Demande de modification architecturale (`01_cnisn/06_decisions/template-modification.md`)
