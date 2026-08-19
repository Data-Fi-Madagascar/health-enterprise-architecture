---
title: "Cartographie HEA → GDHM — Auto-évaluation de maturité numérique santé"
id: evaluation-gdhm
domain: 10_annexes
version: "1.0.0"
status: draft
last_reviewed: 2026-08-19
owner: Bureau de Réalisation de la Valeur
tags: [gdhm, maturite, oms, afrique, auto-evaluation]
---

# Cartographie HEA → GDHM — Auto-évaluation de maturité numérique santé

## Pour qui lire ce document

**Niveau :** niveau 1 — Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ● |
| Directions métier / programmes | ● |
| DEPSI / équipes techniques | ◐ |
| SIS / données / suivi-évaluation | ● |
| Partenaires techniques et financiers | ● |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

## Contexte

Le Global Digital Health Monitor (GDHM) de l'OMS est l'outil de référence pour évaluer la maturité de l'écosystème numérique santé des États membres. Il comprend **7 domaines, 23 indicateurs**, notés sur une échelle de **5 phases** (1 = naissant, 5 = optimisé).

Madagascar n'a pas encore soumis de données au GDHM. Cette cartographie croise l'HEA existante avec les 23 indicateurs du GDHM pour :
1. **Identifier les écarts** — ce que l'HEA couvre déjà vs ce qui manque
2. **Prioriser les actions** — quoi construire en premier pour atteindre Phase 3+
3. **Préparer la soumission** documenter les preuves existantes pour l'enquête GDHM

**Référence :** [WHO GDHM](https://data.who.int/dashboards/gdhm/overview) — [Méthodologie](https://monitor.digitalhealthmonitor.org/methodology)

## Domaine 1 — Leadership et gouvernance

| Indicateur | Description GDHM | Phase estimée | Preuves HEA |
|------------|------------------|---------------|-------------|
| **1** | Organisme de gouvernance numérique santé dédié | **3** | CNASN (`01_cnisn/03_gouvernance/`), UGD (`03_ptisn/index.md`), sous-comité sectoriel |
| **2** | Santé numérique intégrée aux stratégies nationales | **2** | HEA documentée mais pas encore intégrée dans une stratégie nationale officielle |
| **2a** | Santé prioritaire dans la transformation numérique nationale | **2** | UGD existe mais la santé n'est pas explicitement prioritaire dans la politique numérique nationale |
| **3** | Plan pour les technologies émergentes (IA, IoT, etc.) | **1** | Aucun plan spécifique pour les technologies émergentes dans l'HEA |
| **4** | Équité et droits humains dans les stratégies | **2** | Principes CAESN mentionnent l'équité mais pas d'analyse formelle |
| **4a** | Genre dans les stratégies numérique santé | **1** | Aucune référence au genre dans l'HEA |

**Score domaine 1 : Phase 2-3** (moyenne ~2.0)

**Écarts critiques :**
- Pas de stratégie numérique santé nationale officielle (Phase 2要求é)
- Pas de plan technologies émergentes (Phase 1)
- Pas d'analyse genre (Phase 1)

**Correctifs recommandés :**
1. Formeliser l'HEA comme stratégie numérique santé nationale (→ Phase 3)
2. Créer un plan IA/IoT santé dans le cadre de l'ARTSN (→ Phase 2)
3. Intégrer une analyse genre dans les principes CAESN (→ Phase 2)

---

## Domaine 2 — Stratégie et investissement

| Indicateur | Description GDHM | Phase estimée | Preuves HEA |
|------------|------------------|---------------|-------------|
| **5** | Stratégie numérique santé nationale approuvée | **2** | HEA documentée mais pas encore approuvée formellement par un décret ou arrêté |
| **5a** | Alignement avec la couverture sanitaire universelle (CSU) | **2** | VS-02 (protection financière) et VS-03 (accès aux soins) couvrent la CSU |
| **6** | Financement public numérique santé | **1** | Pas de ligne budgétaire identifiée dans l'HEA |
| **6a** | Participation du secteur privé | **1** | Aucune mention du secteur privé dans l'HEA |

**Score domaine 2 : Phase 1-2** (moyenne ~1.5)

**Écarts critiques :**
- Pas de stratégie officiellement approuvée (Phase 2要求é)
- Pas de budget identifié (Phase 1)
- Pas d'engagement secteur privé (Phase 1)

**Correctifs recommandés :**
1. Soumettre l'HEA pour approbation officielle (→ Phase 2)
2. Identifier une ligne budgétaire pour la numérique santé (→ Phase 2)
3. Créer un Volet secteur privé dans le portfolio CAESN (→ Phase 2)

---

## Domaine 3 — Législation, politique et conformité

| Indicateur | Description GDHM | Phase estimée | Preuves HEA |
|------------|------------------|---------------|-------------|
| **7** | Loi protection des données | **1** | Aucune loi spécifique (mentionné dans `comparaison-architectures-africaines.md` comme lacune critique) |
| **8** | Lois vie privée, consentement, confidentialité | **1** | Aucune loi spécifique |
| **9** | Protocole régulation dispositifs/santé (dont IA) | **1** | Aucun protocole |
| **9a** | Protocole régulation IA santé | **1** | Aucun protocole |
| **10** | Sécurité échanges transfrontaliers | **2** | PT-14 (interopérabilité transfrontalière) existe mais pas de protocole officiel |

**Score domaine 3 : Phase 1-2** (moyenne ~1.2)

**Écarts critiques :**
- Pas de loi protection des données (Phase 1) — **lacune critique identifiée dans l'analyse externe**
- Pas de protocole régulation (Phase 1)

**Correctifs recommandés :**
1. Rédiger un projet de loi protection des données (→ Phase 2)
2. Rédiger un protocole de régulation des dispositifs numériques santé (→ Phase 2)
3. Formaliser le protocole transfrontalier PT-14 (→ Phase 2)

---

## Domaine 4 — Main-d'œuvre

| Indicateur | Description GDHM | Phase estimée | Preuves HEA |
|------------|------------------|---------------|-------------|
| **11** | Formation pré-service numérique santé | **1** | Aucune référence dans l'HEA |
| **12** | Formation continue numérique santé | **1** | Aucune référence dans l'HEA |
| **13** | Formation professionnels numérique santé | **1** | Aucune référence dans l'HEA |
| **14** | Parcours carrière numérique santé | **1** | Aucune référence dans l'HEA |

**Score domaine 4 : Phase 1** (moyenne 1.0)

**Écarts critiques :**
- Domaine le plus faible en Afrique (moyenne régionale ~1.5)
- Aucune couverture dans l'HEA
- **Lacune structurelle majeure**

**Correctifs recommandés :**
1. Créer un chapitre ARTSN sur la formation (→ Phase 2)
2. Intégrer la formation dans les profils PTISN (→ Phase 2)
3. Documenter les besoins en compétences dans la matrice de maturité ARTSN (→ Phase 2)

---

## Domaine 5 — Standards et interopérabilité

| Indicateur | Description GDHM | Phase estimée | Preuves HEA |
|------------|------------------|---------------|-------------|
| **15** | Architecture numérique santé / HIE national | **4** | 6 couches + 2 axes (`02_artsn/04_cartographie-cible/`), X-Road obligatoire |
| **16** | Standards de données interopérables | **4** | FHIR R4 obligatoire (STD-0001), SNOMED CT (STD-0007), CIM-10 + LOINC (STD-0006) |
| **17** | Disponibilité réseau | **2** | Layer 2 offline-first (ENF-1) mais pas de mesure réseau nationale |
| **18** | Maintenance infrastructure | **2** | Gouvernance ARTSN (F.3) mais pas de plan maintenance formalisé |

**Score domaine 5 : Phase 3-4** (moyenne ~3.0)

**Forces :**
- Architecture la plus complète d'Afrique (Phase 4)
- Standards les plus stricts d'Afrique (FHIR obligatoire)
- X-Road unique en Afrique

**Écarts :**
- Pas de mesure réseau nationale (Phase 2)
- Pas de plan maintenance formalisé (Phase 2)

**Correctifs recommandés :**
1. Intégrer les métriques réseau dans la Couche 1 (→ Phase 3)
2. Formaliser le plan de maintenance dans F.3 (→ Phase 3)

---

## Domaine 6 — Infrastructure

| Indicateur | Description GDHM | Phase estimée | Preuves HEA |
|------------|------------------|---------------|-------------|
| **19** | Connectivité santé | **2** | Couche 1 (datacenters, VPN, MPLS) documentée mais pas opérationnelle |
| **20** | Dispositifs et équipements | **2** | Couche 2 (Point de service) documentée mais pas déployée |
| **21** | Espace de stockage données | **2** | Couche 5 (Lakehouse) documentée mais pas opérationnelle |

**Score domaine 6 : Phase 2** (moyenne 2.0)

**Écarts :**
- Infrastructure documentée mais pas opérationnelle
- Pas de déploiement à grande échelle

**Correctifs recommandés :**
1. Pilote infrastructure dans 5 districts (→ Phase 3)
2. Documenter l'état actuel de l'infrastructure (→ Phase 2)

---

## Domaine 7 — Services et applications

| Indicateur | Description GDHM | Phase estimée | Preuves HEA |
|------------|------------------|---------------|-------------|
| **22** | Services santé numériques opérationnels | **2** | 16 profils PTISN définis mais aucun déployé |
| **23** | Applications santé mobiles/desktop | **2** | Couche 2 documentée mais pas de applications déployées |

**Score domaine 7 : Phase 2** (moyenne 2.0)

**Écarts :**
- Services documentés mais pas opérationnels
- Aucun déploiement à grande échelle

**Correctifs recommandés :**
1. Déployer PT-01 (échange interinstitutionnel) comme premier service (→ Phase 3)
2. Piloter 2-3 profils dans un district (→ Phase 3)

---

## Synthèse par domaine

| Domaine | Phase estimée | Phase cible (12 mois) | Priorité |
|---------|---------------|----------------------|----------|
| 1. Leadership et gouvernance | 2.0 | 3 | ÉLEVÉE |
| 2. Stratégie et investissement | 1.5 | 2 | CRITIQUE |
| 3. Législation, politique et conformité | 1.2 | 2 | CRITIQUE |
| 4. Main-d'œuvre | 1.0 | 2 | ÉLEVÉE |
| 5. Standards et interopérabilité | 3.0 | 4 | MOYENNE |
| 6. Infrastructure | 2.0 | 3 | ÉLEVÉE |
| 7. Services et applications | 2.0 | 3 | ÉLEVÉE |
| **Moyenne** | **1.96** | **2.7** | — |

## Comparaison avec les pairs africains

| Pays | Phase moyenne | Domaine le plus fort | Domaine le plus faible |
|------|---------------|---------------------|----------------------|
| Kenya | 3.5 | Standards (4) | Main-d'œuvre (2) |
| Afrique du Sud | 3.5 | Législation (4) | Main-d'œuvre (2) |
| Rwanda | 3.0 | Leadership (4) | Infrastructure (2) |
| Tanzanie | 3.0 | Standards (4) | Main-d'œuvre (2) |
| **Madagascar** | **2.0** | **Standards (3-4)** | **Main-d'œuvre (1)** |
| Moyenne AFRO | 3.0 | Leadership (3.75) | Main-d'œuvre (1.5) |

**Positionnement :** Madagascar est en Phase 2, en deçà de la moyenne régionale (Phase 3). Son point fort est les standards (Phase 3-4), son point critique est la main-d'œuvre (Phase 1).

## Plan d'action prioritaire (12 mois)

| Priorité | Action | Domaine GDHM | Phase impactée | Responsable |
|----------|--------|--------------|----------------|-------------|
| 1 | Soumettre l'HEA pour approbation officielle | Stratégie | 2→3 | UGD |
| 2 | Rédiger projet loi protection des données | Législation | 1→2 | Ministère Justice |
| 3 | Créer programme formation numérique santé | Main-d'œuvre | 1→2 | Ministère Santé |
| 4 | Lancer évaluation GDHM officielle | Tous | Baseline | CNASN |
| 5 | Pilote infrastructure 5 districts | Infrastructure | 2→3 | DEPSI |
| 6 | Déployer PT-01 comme premier service | Services | 2→3 | DEPSI |
| 7 | Identifier ligne budgétaire numérique santé | Stratégie | 1→2 | Ministère Finances |
| 8 | Rédiger plan technologies émergentes santé | Leadership | 1→2 | CNASN |

## Références

- **Comparaison des architectures africaines** — Positionnement HEA par rapport aux pairs (`00_caesn/10_annexes/comparaison-architectures-africaines.md`)
- **WHO GDHM** — Global Digital Health Monitor (`https://data.who.int/dashboards/gdhm/overview`)
- **Méthodologie GDHM** — Phases et indicateurs (`https://monitor.digitalhealthmonitor.org/methodology`)
- **État du numérique santé en Afrique** — Étude 32 pays WHO AFRO 2023-2025 (`https://www.dovepress.com/state-of-digital-health-in-32-countries-of-the-who-african-region-a-mu-peer-reviewed-fulltext-article-JHL`)
