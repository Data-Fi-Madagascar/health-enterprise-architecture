---
title: "Instances sectorielles et autorités spécialisées"
id: instances-sectorielles
domain: 07_governance
version: "1.0.0"
status: draft
last_reviewed: 2026-08-13
owner: Secrétariat Général
tags: [gouvernance, instances, sectorielles, autorites]
---

# Instances sectorielles et autorités spécialisées

## Pour qui lire ce document

**Niveau :** niveau 1 : Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ◐ |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

## 1. Instances sectorielles

### 1.1 Instance sectorielle de la Santé Numérique

| Champ | Valeur |
|-------|--------|
| **Mission** | Coordination opérationnelle de la mise en œuvre du cadre d'architecture au niveau sectoriel |
| **Composition** | Représentants des directions techniques, des programmes, des partenaires |
| **Fréquence** | Mensuelle |
| **Rapporte au** | CNASN |

**Responsabilités :**
- Suivi de l'implémentation des décisions du CNASN
- Coordination des équipes techniques
- Préparation des réunions du CNASN
- Suivi des indicateurs de performance

### 1.2 Comité technique de l'interopérabilité

| Champ | Valeur |
|-------|--------|
| **Mission** | Valider les profils techniques et les contrats d'interface |
| **Composition** | Experts techniques, éditeurs, intégrateurs |
| **Fréquence** | Bimensuelle |
| **Rapporte au** | Instance sectorielle |

**Responsabilités :**
- Examination des profils techniques (PTISN)
- Validation des contrats d'interface
- Tests de conformité
- Veille technique

## 2. Autorités spécialisées

### 2.1 Autorité nationale de cybersécurité santé

| Champ | Valeur |
|-------|--------|
| **Mission** | Définir et appliquer les règles de sécurité informatique pour le secteur santé |
| **Composition** | Experts sécurité, DEPSI, Direction Juridique |
| **Fréquence** | Selon besoin |
| **Rapporte au** | CNASN |

**Responsabilités :**
- Définition de la politique de sécurité
- Audit de sécurité des solutions
- Gestion des incidents de sécurité
- Formation à la sécurité
- Veille sur les menaces

### 2.2 Autorité nationale des données de santé

| Champ | Valeur |
|-------|--------|
| **Mission** | Garantir la qualité, la gouvernance et la protection des données de santé |
| **Composition** | Propriétaires de données, DEPSI, Direction Juridique |
| **Fréquence** | Mensuelle |
| **Rapporte au** | CNASN |

**Responsabilités :**
- Définition des règles de qualité des données
- Gestion des référentiels nationaux
- Protection des données personnelles
- Contrôle d'accès aux données
- Arbitrage sur les partages de données

## 3. Articulation entre instances

```
┌─────────────────────────────────────────────────────────────┐
│              Articulation des instances                      │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Leadership du Ministère                      │    │
│  │    (Portage politique, arbitrages finaux)            │    │
│  └──────────────────────┬──────────────────────────────┘    │
│                         │                                    │
│  ┌──────────────────────▼──────────────────────────────┐    │
│  │      Comité National (CNASN)                         │    │
│  │  (Cohérence, homologation, arbitrage)                │    │
│  └──────────────────────┬──────────────────────────────┘    │
│                         │                                    │
│  ┌──────────────────────▼──────────────────────────────┐    │
│  │      Bureau de Réalisation de la Valeur              │    │
│  │  (Portefeuille, bénéfices, redevabilité)             │    │
│  └──────────────────────┬──────────────────────────────┘    │
│                         │                                    │
│  ┌──────────────────────▼──────────────────────────────┐    │
│  │      Instance sectorielle                            │    │
│  │  (Coordination opérationnelle)                       │    │
│  └──────────────────────┬──────────────────────────────┘    │
│                         │                                    │
│  ┌─────────┬────────────┼────────────┬───────────────┐     │
│  │         │            │            │               │     │
│  ▼         ▼            ▼            ▼               ▼     │
│ Comité   Autorité    Autorité    Comités          Équipes   │
│ technique cybersécurité données  techniques      techniques │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## 4. Calendrier de mise en place

| Phase | Actions | Échéance |
|-------|---------|----------|
| **Phase 1** | Création du CNASN (décret ministériel) | T4 2026 |
| **Phase 2** | Mise en place de l'instance sectorielle | T1 2027 |
| **Phase 3** | Création des autorités spécialisées | T2 2027 |
| **Phase 4** | Constitutionalisation des comités techniques | T3 2027 |

## Liens

- Gouvernance du cadre
- Composition du CNASN
- Bureau de Réalisation de la Valeur
- RACI de gouvernance

## Références

- **matrice de lecture** : Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
- **Gouvernance du cadre** : Gouvernance du cadre d'architecture (`00_caesn/07_governance/index.md`)
- **Composition du CNASN** : Composition et fonctionnement du Comité National (`00_caesn/07_governance/cnasen-composition.md`)
- **Bureau de Réalisation de la Valeur** : Bureau de Réalisation de la Valeur (`00_caesn/07_governance/value-realization-office.md`)
- **RACI de gouvernance** : RACI de gouvernance et responsabilités (`00_caesn/07_governance/raci.md`)
