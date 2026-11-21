---
title: "Table de correspondance : Principes CAESN ↔ CNISN"
id: mapping-principes-caesn-cnisn
domain: 02_principles
version: "1.1.0"
status: draft
last_reviewed: 2026-11-21
owner: DEPSI
tags: ["principes", "caesn", "cnisn", "mapping", "correspondance"]
---

# Table de correspondance : Principes CAESN ↔ CNISN

## Pour qui lire ce document

**Niveau :** niveau 1 : Cadre d'Architecture d'Entreprise de la Santé Numérique.

| Profil | Lecture |
|--------|---------|
| Décideurs institutionnels | ◐ |
| Directions métier / programmes | ◐ |
| DEPSI / équipes techniques | ● |
| SIS / données / suivi-évaluation | ◐ |
| Partenaires techniques et financiers | ◐ |

Légende : ● prioritaire · ◐ complémentaire · ○ ponctuelle. Vue d'ensemble : matrice de lecture.

## Contexte

Le CAESN structure les principes en **12 principes architecturaux transversaux (PA-01 à PA-12)** et en **principes de domaine (PD)** par flux de valeur. Le CNISN décline ces principes en **25 règles d'interopérabilité (P-INT-01 à P-INT-25)** qui portent la contrainte technique : autorité de la donnée, contractualisation, versionnement, résidence, minimisation, dérogations, preuve de conformité.

Cette table établit la correspondance entre les deux nomenclatures. Les principes PA et PD sont la référence : les niveaux ARTSN et PTISN les référencent sans renumérotation, et les règles P-INT en constituent l'application opérationnelle.

Les définitions canoniques sont les fiches du [référentiel d'architecture](../../04_architecture-repository/03_business-architecture/motivation/principles) : `pa-01.md` à `pa-12.md` pour les principes transversaux, `p-int-01.md` à `p-int-25.md` pour les règles d'interopérabilité, `pd-vs01-01.md` à `pd-vs04-05.md` pour les principes de domaine.

## Correspondance PA ↔ P-INT

| PA CAESN | Titre PA | Règles CNISN (P-INT) | Titre P-INT |
|----------|----------|----------------------|-------------|
| PA-01 | La valeur pour la population est la finalité de tout investissement numérique | aucun rattachement direct | - |
| PA-02 | Les flux de valeur précèdent les systèmes | aucun rattachement direct | - |
| PA-03 | Les bénéfices doivent être mesurés, pas seulement déclarés | P-INT-23, P-INT-25 | Conformité fondée sur des preuves, Réévaluation continue |
| PA-04 | Les données de santé sont un actif stratégique national | P-INT-07, P-INT-16, P-INT-20 | Responsabilité de la donnée, Résidence et non-réplication, Portabilité et réversibilité |
| PA-05 | Une donnée doit être collectée une seule fois et réutilisée plusieurs fois | P-INT-01, P-INT-02, P-INT-03, P-INT-04 | Autorité désignée, Résolution contre l'autorité, Copies locales non autoritatives, Historisation des références |
| PA-06 | L'interopérabilité est une exigence non négociable | P-INT-05, P-INT-06, P-INT-08, P-INT-09 | Contrat explicite, Versionnement et compatibilité, Publication au catalogue des services, Publication des contrats |
| PA-07 | Les référentiels nationaux sont des biens communs indivisibles | P-INT-08, P-INT-09 | Publication au catalogue des services, Publication des contrats |
| PA-08 | Les systèmes doivent être soutenables sans dépendance externe permanente | P-INT-19, P-INT-20, P-INT-21 | Neutralité technologique, Portabilité et réversibilité, Progressivité |
| PA-09 | L'architecture doit être adaptée aux réalités du terrain | P-INT-21, P-INT-22 | Progressivité, Fonctionnement en connectivité contrainte |
| PA-10 | La souveraineté nationale du système d'information sanitaire est non négociable | P-INT-01, P-INT-10, P-INT-11 | Autorité désignée, Accord préalable, Arbitrage des conflits d'autorité |
| PA-11 | La protection des données personnelles est une condition de confiance | P-INT-14, P-INT-15, P-INT-16, P-INT-17, P-INT-18 | Base d'autorisation explicite, Limitation à la finalité, Résidence et non-réplication, Minimisation, Traçabilité différenciée |
| PA-12 | Toute initiative numérique doit être conforme au cadre national | P-INT-12, P-INT-13, P-INT-23, P-INT-24, P-INT-25 | Dérogation explicite, Dérogation d'urgence, Conformité fondée sur des preuves, Applicabilité déclarée, Réévaluation continue |

PA-01 et PA-02 n'ont pas de rattachement P-INT direct parce qu'ils ne fixent pas de contrainte d'échange : PA-01 énonce la finalité du niveau 1, PA-02 l'ordre de dérivation entre flux de valeur et systèmes. Leur déclinaison opère au niveau des flux, par les principes de domaine et par la matrice de maturité des capabilités.

Les 25 règles P-INT sont couvertes. Huit règles portent un rattachement multiple (P-INT-01, P-INT-08, P-INT-09, P-INT-16, P-INT-20, P-INT-21, P-INT-23, P-INT-25) : elles traduisent un même principe sous plusieurs contraintes indépendantes, le principe PA exprimant une finalité et la règle P-INT en énonçant le contrôle vérifiable.

## Principes de domaine (PD) : uniques au CAESN

Les principes de domaine sont spécifiques aux flux de valeur. Ils n'ont pas de pendant dans la nomenclature P-INT, qui ne connaît pas la finalité métier : le CNISN les intègre implicitement via les chapitres ART et les profils PT.

Chaque flux de valeur porte un ensemble de cinq principes de domaine, identifié `PD-VS<flux>-<rang>`. L'ensemble du flux est introductible sous l'identifiant `PD-VS-<flux>`.

| Flux | Principe | Titre |
|------|----------|-------|
| VS-01 | PD-VS01-01 | Le parcours du patient est l'unité de mesure de la performance |
| VS-01 | PD-VS01-02 | Le dossier du patient suit le patient, pas l'institution |
| VS-01 | PD-VS01-03 | La continuité des soins prime sur la logique des programmes |
| VS-01 | PD-VS01-04 | Le patient et la communauté sont acteurs du parcours de santé |
| VS-01 | PD-VS01-05 | L'accès numérique ne doit jamais devenir une barrière à l'accès aux soins |
| VS-02 | PD-VS02-01 | La détection précoce prime sur la production tardive de rapports |
| VS-02 | PD-VS02-02 | Toute alerte sanitaire doit être traçable de sa notification à sa clôture |
| VS-02 | PD-VS02-03 | Les données communautaires et institutionnelles doivent converger |
| VS-02 | PD-VS02-04 | La riposte doit être pilotée par des données exploitables en temps utile |
| VS-02 | PD-VS02-05 | La surveillance sanitaire est une capabilité nationale permanente |
| VS-03 | PD-VS03-01 | Les droits des bénéficiaires doivent être vérifiables au point de service |
| VS-03 | PD-VS03-02 | La protection financière doit être liée au parcours réel de soins |
| VS-03 | PD-VS03-03 | Les mécanismes d'exemption, de facturation et de remboursement doivent être traçables |
| VS-03 | PD-VS03-04 | Aucun mécanisme numérique de financement ne doit créer une barrière supplémentaire à l'accès aux soins |
| VS-03 | PD-VS03-05 | Le financement doit soutenir la qualité et la continuité des services |
| VS-04 | PD-VS04-01 | La décision sanitaire doit s'appuyer sur des données fiables, traçables et réutilisables |
| VS-04 | PD-VS04-02 | Le pilotage doit mesurer les résultats, pas seulement les activités |
| VS-04 | PD-VS04-03 | Le portefeuille numérique doit être gouverné par la valeur produite |
| VS-04 | PD-VS04-04 | Les partenaires contribuent au portefeuille national, ils ne le fragmentent pas |
| VS-04 | PD-VS04-05 | L'amélioration continue doit être intégrée dans le système, pas ajoutée après coup |

## Conclusion

La nomenclature CAESN (12 PA + 20 PD) est la référence. Le CNISN en constitue l'application vérifiable par les 25 règles P-INT, dont chacune se rapporte à un principe PA unique ou à un petit nombre d'entre eux. Cette table est le point de correspondance unique entre le niveau 1 et le niveau 2 : les identifiants PA, PD et P-INT sont repris tels quels dans les niveaux supérieurs, sans renumérotation.

**Point de vigilance.** La reprise descendante reste incomplète au-delà du niveau 2 : les chapitres ARTSN et les profils PTISN ne référencent aujourd'hui ni les principes de domaine `PD-VS…` ni, pour l'essentiel, les principes `PA-…`. La table documente la correspondance au niveau 2 ; l'établissement de la chaîne descendante jusqu'aux profils PTISN constitue un chantier ouvert.

## Liens

- CAESN : Principes architecturaux
- CNISN : Principes d'interopérabilité
- Point de vigilance CAESN

## Références

- **matrice de lecture** : Matrice de lecture du CAESN (niveau 1) (`00_caesn/reading-matrix.md`)
- **CAESN : Principes architecturaux** : Principes d'architecture (`00_caesn/02_principles/index.md`)
- **CNISN : Principes d'interopérabilité** : Principes d'interopérabilité (`01_cnisn/01_principes/index.md`)
- **Point de vigilance CAESN** : Point de vigilance CAESN : capacité et référentiel manquants pour la coordination intersectorielle (One Health) (`00_caesn/07_governance/point-de-vigilance-caesn.md`)
