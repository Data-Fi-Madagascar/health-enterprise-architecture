---

title: "STD-0002 : Norme de sécurité : Chiffrement et contrôle d'accès"
id: std-0002
domain: 05_standards
version: "1.0.0"
status: active
last_reviewed: 2026-08-13
owner: Comité National d'Architecture Santé Numérique
tags: ["standards", "securite", "chiffrement", "obligatoire"]
---

# STD-0002 : Norme de sécurité : Chiffrement et contrôle d'accès

## Pour qui lire ce document

**Niveau :** niveau 2 : Cadre National d'Interopérabilité de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ○ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ● |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

- **Type** : norme (obligatoire)
- **Statut** : approuvé
- **ADR de référence** : ADR-0008
- **Date d'entrée en vigueur** : 2026-08-13

## Contexte

Les données de santé sont des données sensibles nécessitant une protection renforcée. La sécurité doit être intégrée dès la conception (Security by Design) et non ajoutée a posteriori. Cette norme définit les exigences minimales de sécurité pour toute solution échangeant ou stockant des données de santé.

## Énoncé

Toute solution numérique échangeant ou stockant des données de santé **doit** :

### 1. Chiffrement

| Exigence | Niveau |
|----------|--------|
| **Chiffrement en transit** | TLS 1.2 minimum pour tous les échanges réseau |
| **Chiffrement au repos** | AES-256 pour toutes les données stockées |
| **Chiffrement des sauvegardes** | Obligatoire pour toutes les sauvegardes |

### 2. Contrôle d'accès

| Exigence | Niveau |
|----------|--------|
| **Authentification** | Authentification forte (multi-facteur recommandé) |
| **Autorisation** | Contrôle d'accès basé sur les rôles (RBAC) |
| **Gestion des sessions** | Expiration automatique après inactivité |
| **Traçabilité** | Journalisation de tous les accès |

### 3. Protection des données

| Exigence | Niveau |
|----------|--------|
| **Minimisation** | Collecte limitée aux données strictement nécessaires |
| **Consentement** | Gestion du consentement patient pour le partage |
| **Anonymisation** | Anonymisation des données pour les usages analytiques |
| **Droit d'accès** | Droit du patient à accéder à ses données |

### 4. Infrastructure

| Exigence | Niveau |
|----------|--------|
| **Résidence des données** | Données stockées sur le territoire national |
| **Sauvegarde** | Sauvegardes régulières et testées |
| **Plan de reprise** | Plan de reprise d'activité documenté |
| **Audit de sécurité** | Audits de sécurité réguliers |

## Champ d'application

Cette norme s'applique à :
- Toutes les API échangeant des données de santé
- Tous les systèmes de stockage de données de santé
- Toutes les applications mobiles manipulant des données de santé
- Toutes les bases de données de santé

## Références au cadre

- **Principes** : PA-03 (Sécurité par conception), PA-04 (Protection de la vie privée)
- **ARTSN** : ART-7 (Sécurité et résidence), F.4 (Sécurité et protection)
- **ARTSN — lots consommateurs** : [L1 — Infrastructure & sécurité](../../02_artsn/07_lots/index.md)
- **PTISN** : PT-06 (Authentification), PT-10 (Confiance), PT-12 (Audit)
- **Standards internationaux** : OWASP, NIST, ISO 27001

## Contrôle et conformité

Lors de l'homologation, le Comité National vérifiera :

| Critère | Vérification |
|---------|--------------|
| Chiffrement en transit | TLS 1.2+ configuré |
| Chiffrement au repos | AES-256 activé |
| Authentification | Mécanisme d'authentification fort |
| Autorisation | RBAC implémenté |
| Journalisation | Logs d'accès activés |
| Résidence | Données stockées localement |

## Dérogations

Les dérogations sont possibles pour :
- Les systèmes legacy en phase de migration (plan de migration documenté)
- Les environnements de développement/test (données simulées uniquement)

Toute dérogation doit être justifiée et approuvée par le Comité National.

## Références

- Normes et standards
- ARTSN : Chapitre ART-7
- ARTSN : Fondation F.4
- CNISN : P-INT-03, P-INT-04
- **PTISN** :
  - PT-06 : Référentiel structures et services
  - PT-10 : Confiance, authentification et autorisation
  - PT-12 : Audit, provenance et traçabilité

- **matrice de lecture** : Matrice de lecture du CNISN (niveau 2) (`01_cnisn/reading-matrix.md`)
