---

title: "Guides de démarrage rapide"
id: quick-start-guides
domain: root
version: "1.0.0"
status: approved
last_reviewed: 2026-08-13
owner: Bureau de Réalisation de la Valeur
tags: ["guide", "démarrage", "quick-start", "profil"]
---

# Guides de démarrage rapide

Chaque profil d'utilisateur dispose d'un parcours pratique pour commencer à utiliser le dépôt HEA. Ces guides complètent les [guides de lecture](00_caesn/reading-guide.md) en ajoutant des **actions concrètes**.

---

## 1. Décideur institutionnel

**Objectif :** Comprendre la valeur战略 et évaluer les initiatives.

### Premier pas

1. Lire la [vue d'ensemble du CAESN](00_caesn/00_overview/index.md) (5 min)
2. Consulter les [4 flux de valeur](00_caesn/01_value-streams/index.md) — chacun décrit un résultat attendu pour la population
3. Voir la [matrice de lecture](00_caesn/reading-matrix.md) pour identifier les documents pertinents

### Actions courantes

| Action | Document | Comment |
|--------|----------|---------|
| Évaluer une initiative | [Registre des initiatives](00_caesn/06_portfolio/index.md) | Vérifier l'alignement avec les flux de valeur |
| Lire une décision architecture | [Registre ADR](01_cnisn/06_decisions/registre-decisions.md) | 9 ADR classées par statut |
| Suivre la roadmap | [Feuille de route ARTSN](02_artsn/07_lots/index.md) | 6 phases, jalons, budget 98 MGA |
| Comprendre la gouvernance | [Processus gouvernance](00_caesn/07_governance/processus-gouvernance.md) | Workflows de validation |

### Check-list d'évaluation d'une initiative

- [ ] La initiative s'aligne-t-elle sur un flux de valeur (VS-01..04) ?
- [ ] Quelles capabilités CAESN renforce-t-elle ?
- [ ] Existe-t-il un ADR pertinent ?
- [ ] Quel est l'impact budgétaire et le calendrier ?

---

## 2. Direction métier / Programme

**Objectif :** Décrire les besoins métier et les relier à l'architecture.

### Premier pas

1. Lire les [capabilités CAESN](00_caesn/03_capabilities/index.md) — 18 capabilités organisées par domaine
2. Consulter le [cas d'usage correspondant](03_ptisn/08_annexes/) à votre domaine
3. Identifier les [profils PTISN](03_ptisn/03_profils/pt-00-index.md) associés

### Actions courantes

| Action | Document | Comment |
|--------|----------|---------|
| Décrire un besoin | [Template modification](01_cnisn/06_decisions/template-modification.md) | Formulaire MOD-XXXX |
| Vérifier la maturité | [Matrice de maturité](02_artsn/08_annexes/a-table-de-maturite.md) | Évaluation par capabilité |
| Comprendre l'interopérabilité | [CNISN capacités](01_cnisn/02_capacites/index.md) | 14 capacités, 7 familles |
| Lire les cas d'usage | [VS-01](03_ptisn/08_annexes/cas-usage-reference-evacuation.md), [VS-02](03_ptisn/08_annexes/cas-usage-surveillance-epidemique.md), [VS-03](03_ptisn/08_annexes/cas-usage-couverture-sanitaire.md), [VS-04](03_ptisn/08_annexes/cas-usage-pilotage-systeme.md) | Exemples concrets par flux |

### Check-list de rédaction d'un besoin

- [ ] Identifier le flux de valeur concerné
- [ ] Lister les capabilités impactées
- [ ] Consulter les profils PTISN existants
- [ ] Rédiger via le template MOD-XXXX
- [ ] Soumettre au CNASN

---

## 3. DEPSI / Équipes techniques

**Objectif :** Implémenter les profils techniques et valider l'interopérabilité.

### Premier pas

1. Lire les [15 profils PTISN](03_ptisn/03_profils/pt-00-index.md) — chaque profil définit un service technique national
2. Consulter le [protocole de test](02_artsn/08_annexes/d-protocole-test-interopabilite.md) — 4 niveaux (N1 à N4)
3. Vérifier les [SLA](02_artsn/08_annexes/e-sla-performance.md) requis par profil

### Actions courantes

| Action | Document | Comment |
|--------|----------|---------|
| Créer un nouveau profil | [Règles d'utilisation](03_ptisn/01_regles-utilisation/index.md) | Template PT-XXXX |
| Vérifier la conformité | [Conformité](02_artsn/06_gouvernance/conformite.md) | Dashboard de conformité |
| Lister les composants | [Référentiel composants](referentiel/composants/) | Composants logiques |
| Lire les standards | [std-0001: STD-0001 : Norme d'interopérabilité : HL7 FHIR R4](01_cnisn/05_standards/std-0001-interopabilite-fhir.md), [std-0002: STD-0002 : Norme de sécurité : Chiffrement et contrôle d'accès](01_cnisn/05_standards/std-0002-securite-chiffrement.md) | Normes obligatoires |
| Consulter le RBAC | [PT-10 RBAC](03_ptisn/03_profils/pt-10-confiance-authentification-autorisation.md) | 13 rôles, 10 politiques |

### Check-list d'implémentation d'un profil

- [ ] Identifier le profil PT-XX concerné
- [ ] Lire le contrat d'interface dans le profil
- [ ] Vérifier les chapitres ART associés
- [ ] Implémenter les tests N1 (conformité)
- [ ] Exécuter les tests N2 (composabilité)
- [ ] Soumettre à l'homologation

---

## 4. SIS / Données / Suivi-évaluation

**Objectif :** Gouverner les données et piloter avec des indicateurs fiables.

### Premier pas

1. Lire le [dictionnaire de données](02_artsn/03_objets-de-donnees/index.md) — 33 concepts, 7 domaines
2. Consulter la [cartographie cible](02_artsn/05_cartographie/index.md) — architecture du SI cible
3. Vérifier les [indicateurs CNISN](01_cnisn/06_indicateurs/index.md)

### Actions courantes

| Action | Document | Comment |
|--------|----------|---------|
| Ajouter un concept | [Dictionnaire](02_artsn/03_objets-de-donnees/index.md) | Template concept, 7 champs |
| Mapper vers FHIR | [Champs "Référentiel source"](02_artsn/03_objets-de-donnees/index.md) | Champ technique dans le dictionnaire |
| Consulter les flux | [Flux de valeur](referentiel/flux-valeur/) | VS-01..04 |
| Suivre la trajectoire | [Trajectoire CNISN](01_cnisn/05_trajectoire/index.md) | 7 phases T4 2026–T2 2030 |
| Vérifier la qualité | [CAP-INT-11: Qualité et réconciliation](referentiel/capacites/cap-int-11.md) | Qualité et réconciliation |

### Check-list de définition d'un concept de données

- [ ] Vérifier qu'il n'existe pas déjà dans le dictionnaire
- [ ] Définir : nom, description, type, source, propriétaire, cycle de vie
- [ ] Ajouter le mapping FHIR dans "Référentiel source"
- [ ] Soumettre via le template MOD-XXXX
- [ ] Mettre à jour la matrice d'alignement

---

## 5. Partenaires techniques et financiers

**Objectif :** Évaluer la compatibilité et contribuer au cadre.

### Premier pas

1. Lire la [vue d'ensemble](00_caesn/00_overview/index.md) — contexte stratégique Madagascar
2. Consulter la [feuille de route](02_artsn/07_lots/index.md) — phases de déploiement
3. Vérifier les [standards obligatoires](01_cnisn/05_standards/) — FHIR, sécurité, chiffrement

### Actions courantes

| Action | Document | Comment |
|--------|----------|---------|
| Évaluer la compatibilité | [Matrice d'alignement](03_ptisn/04_matrice-alignement/index.md) | Profils ↔ capacités |
| Comprendre le budget | [Feuille de route](02_artsn/07_lots/index.md) | 98 MGA, 6 phases |
| Lister les initiatives | [Portefeuille](00_caesn/06_portfolio/index.md) | Portefeuille orienté valeur |
| Vérifier la sécurité | [ATNA](01_cnisn/06_decisions/adr-0008-atna.md), [Chiffrement](01_cnisn/05_standards/std-0002-securite-chiffrement.md) | Exigences sécurité |
| Consulter le glossaire | [Glossaire](00_caesn/10_annexes/glossary.md) | Termes transverses |

### Check-list d'évaluation d'un partenaire

- [ ] Le partenaire couvre-t-il un profil PTISN existant ?
- [ ] Conformité avec STD-0001 (FHIR) et STD-0002 (sécurité) ?
- [ ] Alignement avec la phase de déploiement en cours ?
- [ ] Impact sur les capabilités CNISN ?

---

## Liens rapides

| Ressource | Chemin |
|-----------|--------|
| README du dépôt | [`README.md`](./README.md) |
| Matrice de lecture CAESN | [`00_caesn/reading-matrix.md`](./00_caesn/reading-matrix.md) |
| Registre des ADR | [`01_cnisn/06_decisions/registre-decisions.md`](./01_cnisn/06_decisions/registre-decisions.md) |
| Profils PTISN | [`03_ptisn/03_profils/pt-00-index.md`](./03_ptisn/03_profils/pt-00-index.md) |
| Dictionnaire | [`02_artsn/03_objets-de-donnees/index.md`](./02_artsn/03_objets-de-donnees/index.md) |
| Protocole de test | [`02_artsn/08_annexes/d-protocole-test-interopabilite.md`](./02_artsn/08_annexes/d-protocole-test-interopabilite.md) |
