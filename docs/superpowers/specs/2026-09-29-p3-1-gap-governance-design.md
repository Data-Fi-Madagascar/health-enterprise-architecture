# P3.1 — Gouvernance opérationnelle des gaps

**Date :** 2026-09-29
**Statut :** design validé
**Base :** `main` après P2.1
**Périmètre TOGAF :** phases E (Opportunities & Solutions), F (Migration Planning) et G (Implementation Governance)

## 1. Objectif

Transformer les trois gaps existants du repository d'architecture en objets de transition pilotables. Chaque gap doit indiquer son état opérationnel, le plateau cible, les work packages responsables, ses critères de fermeture et la spécification des preuves attendues.

Le résultat doit permettre de dériver automatiquement la chaîne :

```text
GAP → état → transition → plateau cible → WP → objets impactés → critères → preuve
```

`04_architecture-repository` reste la source canonique. Les enveloppes ARTSN, les vues TOGAF et la publication Mintlify restent dérivées.

## 2. Limites du lot

P3.1 couvre uniquement la gouvernance de fermeture des gaps déjà présents :

- `GAP-01` — couverture terrain en zone isolée ;
- `GAP-02` — interopérabilité transfrontalière et One Health ;
- `GAP-03` — cadre légal et gouvernance publié.

Le lot ne couvre pas :

- l'harmonisation des 13 critères CNISN avec les 5 critères ARTSN/CNASN, réservée à P3.2 ;
- le choix de produits ou de solutions techniques ;
- la création de nouvelles capacités ou de nouveaux flux de valeur ;
- la production effective des preuves, qui relève de l'exécution des work packages ;
- l'invention de seuils chiffrés ou de décisions juridiques non approuvés.

## 3. Décisions de modélisation

### 3.1 Maturité documentaire et état opérationnel

Le champ existant `status` conserve son sens documentaire et son vocabulaire contrôlé :

```text
draft | active | stable | candidate | deprecated
```

Un champ distinct `gap_state` décrit l'avancement opérationnel :

```text
identified | planned | in-remediation | closed | accepted-risk
```

Les trois gaps existants prennent initialement `gap_state: planned`, car des work packages leur sont déjà associés mais les preuves de fermeture ne sont pas encore produites.

### 3.2 Échéance sans duplication calendaire

Les dates et périodes restent portées par les work packages. Un gap ne recopie pas de date. Son échéance est exprimée par :

- `target_plateau` : exactement un plateau cible ;
- `addressed_by` : un ou plusieurs work packages responsables.

Le champ existant `between` continue de décrire la transition. Il contient un seul plateau lorsque l'état source est l'état initial non modélisé, et deux plateaux lorsque la transition relie deux plateaux explicites.

### 3.3 Critères et preuves

Chaque gap porte :

- `closure_criteria` : liste non vide de critères courts et vérifiables ;
- `evidenced_by` : relation non vide vers des objets canoniques de type `evidence`.

Une fiche `EVID-*` dédiée est créée par gap. Ces fiches sont `candidate` : elles spécifient les pièces attendues mais n'affirment pas que ces pièces existent déjà.

## 4. Extension du métamodèle

Les champs suivants sont ajoutés à `04_architecture-repository/00_metamodel/schema.md` :

| Champ | Cardinalité pour `gap` | Cible ou vocabulaire |
|-------|-------------------------|----------------------|
| `gap_state` | exactement 1 | `identified`, `planned`, `in-remediation`, `closed`, `accepted-risk` |
| `target_plateau` | exactement 1 | objet de type `plateau` |
| `addressed_by` | au moins 1 | objets de type `work-package` |
| `evidenced_by` | au moins 1 | objets de type `evidence` |
| `closure_criteria` | au moins 1 | chaînes non vides |

`target_plateau`, `addressed_by` et `evidenced_by` sont des relations typées et participent au graphe canonique. `closure_criteria` est une propriété structurée, pas une relation.

## 5. Contenu des gaps

### 5.1 GAP-01 — couverture terrain en zone isolée

- **Plateau cible :** `PL-02`.
- **Work package :** `WP-02`.
- **Objets impactés :** `LOC-04`, `CAP-01` et les objets offline déjà reliés par le repository.
- **Critères de fermeture :** fonctionnement hors ligne qualifié ; reprise de synchronisation qualifiée ; absence de perte critique démontrée sur un terrain représentatif de `LOC-04`.
- **Preuve attendue :** `EVID-GAP-01-QUALIFICATION-OFFLINE`, rapport de qualification hors ligne et de synchronisation.

Les critères ne fixent aucun seuil numérique nouveau. Ils exigent que le protocole de qualification rende explicites ses seuils et résultats au moment de l'exécution.

### 5.2 GAP-02 — interopérabilité transfrontalière et One Health

- **Plateau cible :** `PL-03`.
- **Work packages :** `WP-06` et `WP-07`.
- **Objets impactés :** `ABB-CONFIANCE-AUTORISATION`, `PT-14`, `PT-15`, `ABB-ECHANGE-MEDIATION` et `ABB-EXPOSITION-DONNEES-ANALYTIQUES`.
- **Critères de fermeture :** accord de gouvernance disponible pour chacun des deux périmètres ; contrats d'échange applicables identifiés ; échange transfrontalier testé ; échange One Health testé ; responsabilités et remédiations documentées.
- **Preuve attendue :** `EVID-GAP-02-INTEROPERABILITE-ETENDUE`, dossier conjoint d'interopérabilité transfrontalière et One Health.

La preuve commune regroupe deux volets distincts afin de ne pas confondre les responsabilités transfrontalières et intersectorielles.

### 5.3 GAP-03 — cadre légal et gouvernance publié

- **Plateau cible :** `PL-01`.
- **Work package :** `WP-01`.
- **Objets impactés :** `CMP-39`, `ABB-IDENTITE-BENEFICIAIRE`, `ADR-0010` et les documents de gouvernance déjà présents.
- **Critères de fermeture :** cadre CNASN publié ; charte de protection publiée ; références officielles enregistrées ; pièces utilisables dans le processus d'homologation.
- **Preuve attendue :** `EVID-GAP-03-CADRE-LEGAL`, dossier de publication et d'opposabilité du cadre légal.

P3.1 ne déclare pas ces textes juridiquement opposables. La preuve candidate décrit les pièces qui permettront de le démontrer.

## 6. Vue dérivée

Une vue `04_architecture-repository/08_views/togaf/gap-closure-roadmap.md` est générée par `scripts/build_wrappers.py` depuis les objets canoniques.

La vue contient une ligne par gap avec les colonnes :

| Colonne | Source canonique |
|---------|------------------|
| Gap | `id`, `title` |
| État | `gap_state` |
| Transition | `between` |
| Plateau cible | `target_plateau` |
| Responsable | `owner` |
| Work packages | `addressed_by` |
| Objets impactés | relations existantes, notamment `related` |
| Critères de fermeture | `closure_criteria` |
| Preuves attendues | `evidenced_by` |

La vue ne contient aucune copie manuelle des relations. Elle est ajoutée aux ensembles de vues dérivées du builder et du validateur. Elle reste une vue interne du repository TOGAF, comme les autres fichiers de `08_views/togaf/` : aucune nouvelle page Mintlify autonome n'est créée. La publication externe reçoit le contenu enrichi par la régénération des trois enveloppes ARTSN existantes, puis par leur miroir Mintlify.

## 7. Validation bloquante

`scripts/validate_ref.py` ajoute un contrôle spécifique aux objets `gap`.

Le contrôle rejette :

- un `gap_state` absent ou hors vocabulaire ;
- un `target_plateau` absent, multiple, non résolu ou ne ciblant pas un `plateau` ;
- un `addressed_by` vide, non résolu ou ciblant autre chose qu'un `work-package` ;
- un `evidenced_by` vide, non résolu ou ciblant autre chose qu'un `evidence` ;
- un `closure_criteria` absent ou contenant une valeur vide ;
- un `target_plateau` qui n'apparaît pas dans `between`.

Les nouvelles relations sont ajoutées au graphe général afin que les contrôles d'existence, d'îlots et de portée restent cohérents.

## 8. Tests et méthode d'implémentation

L'implémentation suit TDD, sans sous-agent :

1. tests rouges du métamodèle et des relations typées ;
2. tests rouges du validateur pour chaque règle de rejet et pour un gap conforme ;
3. tests rouges de la vue dérivée ;
4. implémentation minimale ;
5. enrichissement des trois gaps et création des trois preuves ;
6. régénération des enveloppes, vues, index et publication ;
7. suite unitaire complète puis `make check`.

Les tests doivent exercer les fonctions réelles du validateur et du builder. Ils ne se limitent pas à rechercher des chaînes dans les fichiers générés.

## 9. Artefacts concernés

Principaux fichiers attendus :

- `04_architecture-repository/00_metamodel/schema.md` ;
- `04_architecture-repository/07_migration/gaps/gap-01.md` à `gap-03.md` ;
- trois nouvelles fiches dans `04_architecture-repository/06_governance/evidence/` ;
- `scripts/validate_ref.py` ;
- `scripts/build_wrappers.py` ;
- tests unitaires du validateur et de la vue ;
- `04_architecture-repository/08_views/togaf/gap-closure-roadmap.md` ;
- enveloppes ARTSN des gaps, index canonique et artefacts Mintlify affectés.

## 10. Critères d'acceptation

P3.1 est terminé lorsque :

- les trois gaps respectent le métamodèle et portent `gap_state: planned` ;
- chacun cible un plateau, au moins un WP et une preuve candidate ;
- les critères de fermeture sont explicites et vérifiables sans inventer de seuil officiel ;
- la vue dérivée expose la chaîne complète pour les trois gaps ;
- chaque règle de validation possède un test de régression rouge puis vert ;
- les enveloppes et artefacts dérivés sont à jour ;
- `python3 -m unittest discover -s tests -v` passe ;
- `make check` passe ;
- aucun fichier `graphify-out/` ou `.obsidian/` n'est ajouté ;
- une PR est ouverte vers `main`, sans merge automatique.
