# Conception — Distinguer étapes de valeur et processus métier dans la modélisation CAESN

**Date :** 2026-08-12
**Statut :** proposé pour validation
**Périmètre :** `referentiel/`, les 4 enveloppes `00_caesn/01_value-streams/vs-0{1..4}-*.md`, les 13 composants `00_caesn/05_application/`, `coherence-report.md`

## 1. Problème

La modélisation actuelle confond deux concepts. Les tableaux CAESN décrivent des **étapes de valeur** (7 par flux, avec entrées/sorties/acteurs/ruptures/indicateurs) : ce sont des maillons séquentiels du cycle décrit par un flux, pas des processus métier. Or les 28 objets `referentiel/processus/prc-01…28.md` reproduisent ces étapes 1:1 sous le type `processus-metier` avec un Objectif rédigé « Réaliser l'étape de valeur … du flux VS-XX ». Trois conséquences :

1. **Le type `processus-metier` est utilisé à contresens** : aucun objet ne porte de vrai processus (régroupement cohérent d'activités) ; le mot « processus » désigne un maillon du tableau.
2. **Le maillage applicatif est illisible** : les 13 composants (`cmp-01…13`) pointent vers des étapes isolées (`applies_to` = listes de `prc-XX`), ce qui oblige à lister jusqu'à 6 étapes par composant et n'exprime pas ce qu'un composant supporte réellement.
3. **Traçabilité sans niveau intermédiaire** : la relation composant → étape → flux est plate ; il n'existe aucun objet auquel raccrocher une activité transverse ou un parcours complet.

## 2. Objectif

Faire du type `processus-metier` une **couche de régroupement** au-dessus des étapes : 28 objets `etape-valeur` (issus des tableaux, contenu inchangé) + 12 objets `processus-metier` (3 par flux, chacun regroupant 2 à 4 étapes d'un même flux). Chaque processus est un objet nouveau, strictement dérivé des étapes qu'il couvre, publié dans l'enveloppe de sa VS. Les composants s'y rattachent au niveau processus au lieu du niveau étape.

## 3. Décisions de conception

| # | Décision | Justification |
|---|----------|---------------|
| D1 | **Deux types distincts** : `etape-valeur` (préfixe `ev-`, dossier `referentiel/etapes-valeur/`) et `processus-metier` (préfixe `prc-`, dossier `referentiel/processus/`) | Supprime la confusion : une étape est un maillon de tableau, un processus est un régroupement d'étapes |
| D2 | **Rattachement Per-VS** : 3 processus par flux de valeur, `source:` = enveloppe VS-XX | Les processus restent dans la narration des enveloppes VS ; aucune enveloppe transversale nouvelle |
| D3 | **Contenu strictement dérivé des étapes** : Objectif (synthèse des intitulés), Étapes couvertes, Acteurs (union du « Qui intervient »), Indicateurs (union des indicateurs) | Aucun contenu inventé hors source CAESN (pas d'« activités principales », pas de « SI support ») |
| D4 | **Capabilités des processus = héritage intégral** de l'`applies_to` de la VS parente (cap-XX + pp-XX) | Le CAESN déclare les capabilités au niveau flux, pas par étape ; un sous-ensemble manuel inventerait un mapping absent de la source |
| D5 | **Relations** : `related` = étapes couvertes (`ev-XX`) + VS parente (`vs-XX`) ; `applies_to` = héritage D4 | Traçabilité processus → étapes → VS → capabilités complète et vérifiable |
| D6 | **Découpage Option 1 « Phases du cycle »** : étapes adjacentes groupées selon les phases du cycle de chaque flux (2/3/2, 2/3/2, 2/2/3, 3/2/2) | Fidèle à la narration des tableaux, blocs équilibrés, traçabilité annexe E intacte |
| D7 | **Renommage mécanique** `prc-01…28` → `ev-01…28` (1:1, contenu et `applies_to` granulaire conservés) ; le namespace `prc-01…12` est réutilisé par les 12 processus | Le mapping prc→VS a été vérifié (prc-01…07=VS-01, 08…14=VS-02, 15…21=VS-03, 22…28=VS-04) ; aucune réécriture de contenu |
| D8 | **Rattachement des composants au niveau processus** : l'`applies_to` de chaque `cmp-XX` passe des étapes aux processus qui les couvrent, par transformation mécanique depuis le tableau de régroupement | Un composant supporte un processus complet, pas des maillons isolés ; la transformation est déterministe, sans jugement |

## 4. Modèle cible

Cinq types d'objets CAESN dans le référentiel :

| Type | Répertoire | Préfixe | Objets |
|------|------------|---------|--------|
| `flux-valeur` | `referentiel/flux-valeur/` | `vs-` | vs-01…04 |
| `etape-valeur` | `referentiel/etapes-valeur/` | `ev-` | ev-01…28 (ex-prc-01…28) |
| `processus-metier` | `referentiel/processus/` | `prc-` | prc-01…12 (nouveaux) |
| `composant-applicatif` | `referentiel/composants/` | `cmp-` | cmp-01…13 |
| `partie-prenante` | `referentiel/parties-prenantes/` | `pp-` | pp-01…10 |

Total : **213 objets** (201 + 12 processus, les 28 étapes étant renumérotées sans changement de compte).

## 5. Découpage des 28 étapes en 12 processus

### 5.1 VS-01 — Accéder à des services de santé essentiels (ev-01…07)

| Processus | Étapes couvertes |
|-----------|------------------|
| PRC-01 — Accès, orientation et admission du patient | ev-01 Reconnaissance du besoin et orientation · ev-02 Accueil et enregistrement |
| PRC-02 — Prestation des soins cliniques | ev-03 Consultation et diagnostic · ev-04 Traitement et prise en charge · ev-05 Référence et contre-référence |
| PRC-03 — Continuité, suivi et qualité des soins | ev-06 Suivi et continuité des soins · ev-07 Amélioration de la qualité |

### 5.2 VS-02 — Prévenir, détecter et répondre aux risques sanitaires (ev-08…14)

| Processus | Étapes couvertes |
|-----------|------------------|
| PRC-04 — Veille, prévention et surveillance sanitaire | ev-08 Identification des risques et promotion de la santé · ev-09 Surveillance et détection |
| PRC-05 — Alerte, investigation et riposte | ev-10 Notification et alerte · ev-11 Vérification et investigation · ev-12 Riposte |
| PRC-06 — Clôture et capitalisation des épisodes | ev-13 Suivi de situation et clôture · ev-14 Capitalisation et amélioration |

### 5.3 VS-03 — Protéger financièrement la population (ev-15…21)

| Processus | Étapes couvertes |
|-----------|------------------|
| PRC-07 — Identification et droits des bénéficiaires | ev-15 Identification et enregistrement des bénéficiaires · ev-16 Définition des droits et du panier de soins |
| PRC-08 — Financement et exemption au point de service | ev-17 Mobilisation des financements · ev-18 Prise en charge et exemption au point de service |
| PRC-09 — Remboursement et régulation des mécanismes | ev-19 Facturation et traitement des demandes de remboursement · ev-20 Remboursement · ev-21 Contrôle, audit et ajustement des mécanismes |

### 5.4 VS-04 — Piloter, coordonner et améliorer la performance (ev-22…28)

| Processus | Étapes couvertes |
|-----------|------------------|
| PRC-10 — Planification et allocation des ressources | ev-22 Définition des priorités et planification · ev-23 Budgétisation et allocation des ressources · ev-24 Coordination des acteurs et alignement des partenaires |
| PRC-11 — Suivi et pilotage de la performance | ev-25 Suivi de l'exécution · ev-26 Analyse de la performance et prise de décision |
| PRC-12 — Redevabilité et amélioration continue | ev-27 Redevabilité et communication publique · ev-28 Amélioration continue |

Propriétés de la partition : chaque étape est couverte par **exactement un** processus ; chaque processus couvre 2 à 4 étapes adjacentes ; l'union couvre les 28 étapes.

## 6. Contenu et frontmatter des objets

### 6.1 Étapes `ev-XX` (conversion des `prc-XX` existants)

Conversion purement formelle, **contenu du corps inchangé** (Objectif / Entrées / Sorties / Acteurs / Ruptures fréquentes / Indicateurs) :

- Fichier : `referentiel/processus/prc-XX.md` → `referentiel/etapes-valeur/ev-XX.md`
- Frontmatter : `id: prc-XX` → `ev-XX` ; `type: processus-metier` → `etape-valeur` ; `title: PRC-XX — …` → `EV-XX — …` ; `tags`: remplacer `processus-metier`/`prc-XX` par `etape-valeur`/`ev-XX`
- `source:` (enveloppe VS-XX), `applies_to` (sous-ensembles de capabilités par étape), `related: ["vs-XX"]` : **inchangés**

### 6.2 Processus `prc-01…12` (nouveaux objets)

Frontmatter (exemple PRC-01, VS-01) :

```yaml
---
id: prc-01
type: processus-metier
niveau: "1"
title: PRC-01 — Accès, orientation et admission du patient
status: draft
owner: Direction des soins            # hérité de la VS-01
version: "0.0.1"
source: 00_caesn/01_value-streams/vs-01-access-care.md
maps_to: []
implements: []
applies_to: ["cap-01","cap-02","cap-03","cap-04","cap-09","cap-10","cap-11","cap-13","cap-14","cap-15","pp-01","pp-02","pp-04","pp-05","pp-06"]   # héritage intégral de VS-01 (D4)
related: ["ev-01","ev-02","vs-01"]
tags: ["caesn","niveau-1","processus-metier","prc-01"]
---
```

Corps (structure d'enveloppe en `####` après transclusion) :

| Section | Contenu |
|---------|---------|
| `## Objectif` | Synthèse des intitulés des étapes couvertes (ex. « Assurer l'accès du patient aux soins : reconnaissance du besoin, orientation, accueil et enregistrement ») |
| `## Étapes couvertes` | Liste liée des `ev-XX` avec leurs titres |
| `## Acteurs` | Union du champ « Qui intervient » des étapes couvertes |
| `## Indicateurs` | Union des indicateurs des étapes couvertes |
| (pas de section Entrées/Sorties globales ni de « SI support ») | Aucun contenu hors source (D3) |

Ligne `Rattachement` générée : capabilités + parties prenantes héritées (D4) + fiche `referentiel/processus/prc-XX.md`.

## 7. Migrations mécaniques

| Élément | Opération |
|---------|-----------|
| 28 fichiers `referentiel/processus/prc-XX.md` | Déplacés vers `referentiel/etapes-valeur/ev-XX.md` + frontmatter (D7) |
| 12 nouveaux fichiers `referentiel/processus/prc-01…12.md` | Créés selon §6.2 |
| 13 `referentiel/composants/cmp-XX.md` | `applies_to` : étapes → processus couvrants (D8), cf. §8 |
| 4 enveloppes `vs-0{1..4}-*.md` | Bloc catalogue « Étapes de valeur » (ev-XX) + bloc catalogue « Processus métier » (prc-XX), cf. §9 |
| `referentiel/_schema.md` | Tableau des types : ligne `etape-valeur` ajoutée, ligne `processus-metier` mise à jour (PRC-01…12) |
| `referentiel/_index.yaml` | 28 entrées `prc-XX` → `ev-XX` (chemin `processus/…` → `etapes-valeur/…`) + 12 entrées `prc-XX` |
| `coherence-report.md` | §11 et ligne récapitulative : « 28 processus … un par étape » → « 28 étapes de valeur + 12 processus métier » ; re-baseline des comptes |
| `00_caesn/10_annexes/glossary.md` | Ajout des définitions « étape de valeur » et « processus métier » (lève l'ambiguïté à la source) |
| `00_caesn/05_application/application-domains.md`, `shared-services.md` | Régénérés par `build_wrappers.py` (lignes `Rattachement` issues du frontmatter des cmp) |

Ordre impératif (évite la collision d'id dans le namespace `prc-`) : **1)** convertir les 28 `prc-XX` en `ev-XX` et régénérer ; **2)** créer les 12 `prc-XX` processus et ré-ancrer les blocs ; **3)** mettre à jour les cmp ; **4)** index/schema/coherence/glossaire.

## 8. Réaffectation des composants (D8)

Transformation mécanique : chaque `applies_to` de `cmp-XX` remplace chaque étape référencée par l'ensemble des processus la couvrant (dédupliqué). Résultat :

| Composant | avant (`applies_to`) | après |
|-----------|----------------------|-------|
| cmp-01 | prc-02, 03, 05, 06 | prc-01, 02, 03 |
| cmp-02 | prc-02, 03, 04 | prc-01, 02 |
| cmp-03 | prc-01, 06, 08, 09 | prc-01, 03, 04 |
| cmp-04 | prc-09…13 | prc-04, 05, 06 |
| cmp-05 | prc-08, 09 | prc-04 |
| cmp-06 | prc-15, 16, 18 | prc-07, 08 |
| cmp-07 | prc-19, 20, 21 | prc-09 |
| cmp-08 | prc-04, 12, 18 | prc-02, 05, 08 |
| cmp-09 | prc-22, 23, 25 | prc-10, 11 |
| cmp-10 | prc-07, 14, 21, 25, 26, 27 | prc-03, 06, 09, 11, 12 |
| cmp-11 | prc-22, 24, 28 | prc-10, 12 |
| cmp-12 | prc-02, 15, 23 | prc-01, 07, 10 |
| cmp-13 | prc-02, 10, 12, 19 | prc-01, 05, 09 |

## 9. Évolution des enveloppes VS

L'enveloppe `vs-01-access-care.md` passe de 2 blocs à 3 :

```
# VS-01 — …                     (H1 manuscrit)
… chapeau / « Pour qui lire » …
<!-- BEGIN:GENERATED mode=monographie -->      ← VS-01 (inchangé)
… VS-01 …
<!-- END:GENERATED -->

## Étapes de valeur            (titre manuscrit)
<!-- BEGIN:GENERATED mode=catalogue source=referentiel/etapes-valeur/ev-01.md,…,ev-07.md -->
### EV-01 — …                 (7 étapes, contenu inchangé, fiche → referentiel/etapes-valeur/ev-XX.md)
<!-- END:GENERATED -->

## Processus métier            (titre manuscrit)
<!-- BEGIN:GENERATED mode=catalogue source=referentiel/processus/prc-01.md,…,prc-03.md -->
### PRC-01 — …                 (3 processus, fiche → referentiel/processus/prc-XX.md)
<!-- END:GENERATED -->
```

L'invariant de `build_wrappers.py` est respecté : l'union des blocs couvre les 10 objets rattachés à l'enveloppe (1 VS + 7 étapes + 3 processus). Même schéma pour vs-02 (ev-08…14 + prc-04…06), vs-03 (ev-15…21 + prc-07…09), vs-04 (ev-22…28 + prc-10…12).

## 10. Outillage

- Aucune modification de `build_wrappers.py` : les marqueurs `source=` en liste littérale et l'attribut `mode=` existant suffisent.
- `scripts/manifest.json` inchangé (les objets transitent par les enveloppes).
- `make check` (wrappers + liens) et validateurs locaux `validate_ref.rb` / `trace_check.py` comme vérification finale.

## 11. Critères d'acceptation

| # | Critère | Vérification |
|---|---------|--------------|
| A1 | `make check` vert | 54 enveloppes à jour, 0 lien cassé |
| A2 | Référentiel cohérent | `validate_ref.rb` : 213 fichiers / 212 ids, 0 lien cassé, 0 relation non résolue (2 erreurs méta connues `_schema.md` exclues) |
| A3 | Traçabilité complète | `trace_check.py` : 212/212 objets tracés (les 12 processus via `related` → ev → vs → cap) |
| A4 | Partition correcte | Chaque `ev-XX` couvert par exactement 1 processus ; chaque processus couvre 2 à 4 étapes ; union = 28 |
| A5 | Contenu des étapes préservé | Diff des 28 `ev-XX` limité à id/type/title/tags/chemin |
| A6 | Aucun contenu inventé | Les 12 processus ne contiennent que des dérivés des étapes (Objectif de synthèse, unions Acteurs/Indicateurs) |
| A7 | Composants réaffectés mécaniquement | Les 13 `applies_to` correspondent au tableau §8 |
| A8 | Publication | PDF/site : les 4 enveloppes VS rendent étapes + processus |

## 12. Risques

| Risque | Mitigation |
|--------|------------|
| Collision d'id pendant la transition (prc-XX réutilisé) | Ordre impératif §7 ; commit par étape |
| Références oubliées vers `prc-XX` (sens « étape ») | `grep` de contrôle avant/après ; `check_links.py` ; revue des diffs cmp |
| Baseline de cohérence changée (201 → 213, trace 197/201 → 212/212) | Consignée dans `coherence-report.md` au moment de la migration |
| Diff volumineux (28 déplacements + 12 créations + 4 enveloppes + 13 cmp + index/schema/coherence) | Commit préalable de l'état courant ; lot séquencé selon §7 |
| Les 4 enveloppes VS passent à 3 blocs (perte de lisibilité ?) | Titres manuscrits « Étapes de valeur » / « Processus métier » préservés hors marqueurs |

## 13. Hors périmètre

- Processus transverses inter-flux (écartés en clarification : rattachement Per-VS, 3/VS).
- Arbitrages de contenu CAESN (correspondance CAP-xx ↔ CAP-INT-xx, taxonomie DIG, décisions D-1…D-5 de `point-de-vigilance-caesn.md`).
- Refonte du CNISN / ARTSN.
- Versionnement Git (préalable : committer l'état courant avant la migration).
