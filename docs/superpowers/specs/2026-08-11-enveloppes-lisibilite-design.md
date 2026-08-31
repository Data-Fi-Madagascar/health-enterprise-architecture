# Conception — Restaurer la lisibilité des enveloppes par transclusion générée

> **Note :** Document historique de spécification. La structure du dépôt a été refactorisée ; les liens internes font référence à des chemins obsolètes. Ce document est conservé à titre d'archive.

**Date :** 2026-08-11
**Statut :** validé pour implémentation
**Périmètre :** les 4 niveaux du dépôt (`00_caesn/`, `01_cnisn/`, `02_artsn/`, `03_ptisn/`) et `referentiel/`

## 1. Problème

Le refactor « architecture as code » a extrait le contenu normatif des documents vers `referentiel/<type>/<id>.md`, en laissant dans les documents d'origine — les **enveloppes** — de simples listes d'identifiants. Trois conséquences mesurées :

1. **Lisibilité détruite au niveau 1.** `00_caesn/02_principles/transversal.md` portait les 12 principes en texte complet (**Signification** / **Implications**) ; il ne contient plus que 12 puces `- [PA-01](…)`. La matrice de lecture destine pourtant cette page aux directions métier en lecture prioritaire.
2. **215 liens cassés dans 17 fichiers.** Les enveloppes situées à deux niveaux de profondeur écrivent `../referentiel/…` là où il faut `../../referentiel/…`. Les catalogues étant le seul accès au contenu, aucun principe, capabilité ni flux de valeur n'est atteignable depuis le CAESN.
3. **Publication creuse.** `scripts/manifest.json` ne référence aucun objet du référentiel, et `scripts/build_mintlify.py:167-168` dégrade tout lien non résolu en texte brut. Dans le PDF et sur le site, le chapitre « Principes d'architecture transversaux » se rend comme une liste de codes sans une seule définition.

Une quatrième anomalie est apparue lors du cadrage : les **13 profils PTISN existent en double**, à 98 % d'identité entre l'enveloppe et l'objet (mesuré : PT-04 98,5 %, PT-10 98,1 %). C'est cette duplication qui a contraint l'audit de cohérence à corriger « les 13 profils **et** leurs 13 sources » (§1 de `coherence-report.md`).

## 2. Objectif

Rendre chaque enveloppe autoportante et lisible sans réintroduire de duplication maintenue à la main : le référentiel reste la source unique de vérité, les enveloppes en sont une **projection générée et committée**.

## 3. Décisions de conception

| # | Décision | Justification |
|---|----------|---------------|
| D1 | **Transclusion du corps complet**, pas un tableau de synthèse | Le PDF et le site doivent porter le texte normatif ; un résumé obligerait à publier en plus les 151 objets |
| D2 | **Contenu écrit dans les fichiers et committé**, avec garde-fou `--check` en CI | Les enveloppes restent lisibles sur GitHub et dans l'éditeur, et les diffs montrent les évolutions normatives |
| D3 | **Le champ `source:` des objets est le mapping**, aucune configuration | Vérifié : 150/151 objets renseignés (`_schema.md` excepté, à raison), 49 chemins distincts, **tous existants** |
| D4 | Les fichiers d'**index et de matrices** reçoivent un tableau généré, pas une transclusion | Leur rôle est la navigation ; transclure 13 profils dans `pt-00-index.md` dupliquerait le texte à l'intérieur du même document |
| D5 | Les **13 profils PTISN entrent dans le lot** | Supprime la duplication à 98 % et le piège de double correction |
| D6 | Les **notes de migration sortent des objets** avant transclusion | Trace d'audit interne ; leur place est `coherence-report.md` et l'historique Git, pas un document publié aux décideurs |

## 4. Périmètre exact

**51 fichiers distincts touchés**, couvrant les **150 objets** du référentiel — chaque objet est publié exactement une fois.

Décompte : 35 monographies + 14 catalogues + 2 fichiers de tableau. `02_artsn/04_patterns/index.md` relève à la fois du mode catalogue (il est le `source:` de `ART-10` et `ART-11`) et du mode tableau (il indexe les 20 chapitres) ; il n'est compté qu'une fois.

### 4.1 Mode monographie — 35 fichiers (1 objet par enveloppe)

L'objet **est** le document. Vérifié : les 35 titres H1 de l'enveloppe sont **identiques** au H1 de l'objet, donc le H1 de l'objet est supprimé à l'insertion et les `##` de l'objet restent des `##`.

| Fichiers | Nombre | Objets |
|---|---|---|
| `00_caesn/01_value-streams/vs-0{1..4}-*.md` | 4 | `VS-01`…`VS-04` |
| `02_artsn/04_patterns/art-*.md` | 18 | `ART-0`…`ART-9`, `ART-4A-d`, `ART-8A-d` |
| `03_ptisn/03_profils/pt-{01..13}-*.md` | 13 | `PT-01`…`PT-13` |

### 4.2 Mode catalogue — 14 fichiers (N objets par enveloppe)

Les objets s'insèrent sous un titre `## Catalogue …` existant, en `###`.

| Fichier | Objets |
|---|---|
| `00_caesn/02_principles/transversal.md` | 12 (`PA-01`…`PA-12`) |
| `00_caesn/02_principles/domain/vs0{1..4}.md` | 20 (5 par flux) |
| `00_caesn/03_capabilities/business.md` | 8 (`CAP-01`…`CAP-08`) |
| `00_caesn/03_capabilities/enabling.md` | 8 (`CAP-09`…`CAP-16`) |
| `00_caesn/04_data/principles.md` | 8 (`DA-01`…`DA-08`) |
| `00_caesn/05_application/principles.md` | 9 (`AA-01`…`AA-09`) |
| `01_cnisn/01_principes.md` | 25 (`P-INT-01`…`P-INT-25`, groupés par catégorie A-F) |
| `01_cnisn/02_capacites.md` | 12 (`CAP-INT-01`…`CAP-INT-12`) |
| `02_artsn/00_fondations.md` | 6 (`F-1`…`F-6`) |
| `02_artsn/02_exigences-contextuelles.md` | 5 (`ENF-1`…`ENF-5`) |
| `02_artsn/04_patterns/index.md` | 2 (`ART-10`, `ART-11`) + tableau de navigation (cf. 4.3) |

Effet de bord voulu : `F-5`/`F-6` et `ART-10`/`ART-11`, aujourd'hui `status: candidate` et **absents des catalogues**, deviennent visibles avec un badge de statut.

### 4.3 Mode tableau — 3 fichiers

Tableau généré `code | titre canonique | rattachement | statut | fiche`.

- `02_artsn/04_patterns/index.md` — les 20 chapitres (ce fichier combine tableau et catalogue)
- `03_ptisn/03_profils/pt-00-index.md` — les 13 profils
- `01_cnisn/08_annexes/a-matrice-principes-capacites.md` — les 16 capacités et 25 principes

Effet de bord voulu : la dérive de libellés (10 capabilités sur 16 divergent entre `00_caesn/03_capabilities/maturity.md` et le titre canonique) disparaît, le titre provenant de l'objet.

## 5. Convention de marqueurs

```markdown
## Catalogue des principes

<!-- BEGIN:GENERATED source=referentiel/principes/pa-*.md -->
<!-- Généré par scripts/build_wrappers.py — ne pas éditer à la main -->

### PA-01 — La valeur pour la population est la finalité de tout investissement numérique

- **Signification** : …
- **Implications** : …

*Rattachement : tous flux de valeur · [fiche](../../../referentiel/principes/pa-01.md)*

<!-- END:GENERATED -->
```

Règles :

- Tout ce qui est **hors marqueurs est rédigé à la main et jamais modifié** : frontmatter, chapeau, « Pour qui lire ce document », section « Liens » de fin.
- L'attribut `source=` n'est **pas** le mapping : celui-ci vient du champ `source:` des objets (D3). C'est un **filtre** appliqué aux objets déjà rattachés à cette enveloppe, utile uniquement quand un fichier a besoin de plusieurs blocs. Un bloc sans attribut reçoit tous les objets de l'enveloppe.
- Un fichier peut donc contenir **plusieurs blocs générés** — cas de `01_cnisn/01_principes.md`, où les six titres de catégorie A-F restent rédigés à la main, chacun suivi de son bloc filtré. Le script vérifie que l'union des blocs couvre tous les objets de l'enveloppe, et échoue si un objet n'est capté par aucun filtre.
- Une enveloppe sans marqueurs est **signalée en erreur**, pas silencieusement ignorée : le script échoue en listant les fichiers à annoter.
- Un objet dont le `source:` ne correspond à aucun fichier existant fait échouer le script.

## 6. Transformations appliquées au corps transclus

| Transformation | Mode | Raison |
|---|---|---|
| Suppression du H1 de l'objet | monographie | L'enveloppe porte déjà le même H1 (vérifié 35/35) |
| `#` → `###` et `##` internes → `####` | catalogue | S'insérer sous le `## Catalogue` sans casser la hiérarchie ni la table des matières du PDF |
| Suppression de la section `## Liens` de l'objet | les deux | Redondante dans l'hôte ; remplacée par la ligne *Rattachement* construite depuis `applies_to` / `maps_to` / `implements` |
| **Recalcul de tous les liens relatifs** | les deux | Un lien valide depuis `referentiel/capabilites/` ne l'est pas depuis `00_caesn/03_capabilities/` : `../flux-valeur/vs-01.md` devient `../../referentiel/flux-valeur/vs-01.md` |
| Badge `**Statut : candidate**` si `status ≠ active` | les deux | Rend l'état de maturité visible au lecteur |
| Tri naturel des identifiants | catalogue | `PA-02` avant `PA-10` |
| Conservation des sous-titres de regroupement | `01_cnisn/01_principes.md` | Les catégories A-F rédigées à la main restent hors marqueurs, un bloc généré par catégorie |

Le recalcul de liens est le mécanisme qui **élimine les 215 liens cassés par construction** : aucun chemin vers le référentiel n'est plus saisi à la main, l'erreur `../` vs `../../` devient impossible.

## 7. Réconciliation préalable des objets (bloquant)

Avant toute génération sur les 13 profils PTISN, réconcilier le delta enveloppe/objet **dans l'objet**, qui est la source de vérité. Anomalies identifiées :

| Anomalie | Exemple | Traitement |
|---|---|---|
| Gras non fermé | `**CAP-INT-01 — Résolution d'identité du bénéficiaire` (sans `**` final) | Corriger dans l'objet |
| Note de migration publiée | `> **Note de migration** : le numéro de capacité a été aligné sur le CNISN.` | Retirer de l'objet (D6) ; l'information reste dans `coherence-report.md` et l'historique Git |
| Apostrophes divergentes | `bases d’autorisation` vs `bases d'autorisation` | Normaliser sur l'apostrophe typographique `’` dans tout le référentiel |

Procédure : pour chacun des 13 profils, produire le diff enveloppe ↔ objet, examiner chaque écart, reporter dans l'objet ce qui est normatif, écarter ce qui est trace d'audit. **Aucune enveloppe n'est écrasée avant validation de son diff.**

## 8. Outillage

`scripts/build_wrappers.py` :

```
python scripts/build_wrappers.py              # écrit les 51 enveloppes
python scripts/build_wrappers.py --check      # exit 1 + diff si dérive, n'écrit rien
python scripts/build_wrappers.py --only 00_caesn/02_principles/transversal.md
```

- `make wrappers` (génération) et `make check` (vérification), alignés sur le `Makefile` existant.
- `--check` en tête de `.github/workflows/release.yml`, **avant** la construction du PDF : une enveloppe dérivée casse la release plutôt que de produire un PDF faux.
- `scripts/check_links.py` : vérifie que **0 lien relatif** est cassé sur l'ensemble du dépôt. Ce contrôle manque au validateur actuel, qui annonce « Broken links : 0 » alors que 215 liens sont cassés dans l'arbre de travail.

## 9. Impact sur la publication

Les enveloppes redevenant autoportantes, **`scripts/manifest.json` reste inchangé** : ni les 150 objets ni un nouveau niveau ne s'y ajoutent. Le PDF et le site retrouvent la substance normative sans page supplémentaire, et la dégradation des liens non résolus de `build_mintlify.py:167-168` ne mord plus sur les catalogues. Le constat « publication creuse » se résout sans toucher à la chaîne de publication.

## 10. Corrections manuelles dans le même lot

Hors marqueurs, donc hors génération :

1. Les 4 liens `../reading-matrix.md` de `00_caesn/02_principles/domain/vs0{1..4}.md` → `../../reading-matrix.md`.
2. `referentiel/_schema.md:19` — la règle « les documents historiques référencent les objets par lien » devient fausse. Nouvelle formulation : les enveloppes transcluent le corps des objets par génération ; le référentiel reste la source unique de vérité ; toute édition se fait dans l'objet, jamais dans le bloc généré.
3. `00_caesn/00_overview/value-model.md:55` — « Valeur équitée » → « Valeur équité ».

## 11. Hors périmètre

Explicitement exclu de ce lot, à traiter séparément :

- Le versionnement Git du référentiel et des corps CNISN/PTISN, aujourd'hui non suivis (25 entrées `??`). **Préalable opérationnel** : committer avant de lancer la génération, pour que les diffs soient lisibles.
- Les arbitrages de contenu : décisions D-1 à D-5 de `00_caesn/07_governance/point-de-vigilance-caesn.md`, table de correspondance CAP-xx ↔ CAP-INT-xx, articulation des couches CAESN ↔ ARTSN, taxonomie DIG-01…04.
- Le rattachement des 29 principes PA/AA/DA aux capabilités et flux (`maps_to` / `applies_to` vides).
- L'alignement des libellés de `maturity.md` sur les titres canoniques : traité par la génération pour les tableaux d'index, mais le tableau de maturité lui-même reste rédigé à la main dans ce lot.

## 12. Critères d'acceptation

| # | Critère | Vérification |
|---|---|---|
| A1 | Idempotence | Deux exécutions consécutives ne produisent aucun diff |
| A2 | Zéro lien cassé | `scripts/check_links.py` : 0 cassé sur les 1 222 liens relatifs du dépôt (215 cassés avant le lot) |
| A3 | Intégrité du texte | Le corps de chacun des 150 objets apparaît verbatim (aux espaces près) dans son enveloppe hôte |
| A4 | Garde-fou actif | Après édition délibérée d'un bloc généré, `--check` renvoie 1 ; après régénération, 0 |
| A5 | Contenu manuel préservé | Frontmatter, chapeau, « Pour qui lire », « Liens » inchangés sur les 51 fichiers (diff limité aux blocs générés) |
| A6 | Aucun objet orphelin | Les 150 objets ont une enveloppe hôte ; le script échoue si un `source:` ne résout pas |
| A7 | Publication | Le PDF du niveau 1 contient le texte des 12 PA, des 20 PD, des 16 CAP et des 4 VS |
| A8 | Profils PTISN | Les 13 enveloppes ne contiennent plus de texte propre ; aucune « Note de migration » ne subsiste dans un document publié |

## 13. Risques

| Risque | Mitigation |
|---|---|
| Écrasement d'un contenu d'enveloppe plus riche que l'objet | Réconciliation §7 obligatoire avant écriture ; revue du diff des 13 profils |
| Perte de contenu non versionné pendant l'opération | Commit préalable du référentiel (§11) |
| Fichiers longs après transclusion (`01_cnisn/01_principes.md` ≈ 25 principes) | Acceptable : c'est le format d'origine du document, et la table des matières du PDF reste hiérarchisée |
| Édition future dans le bloc généré au lieu de l'objet | Bannière « ne pas éditer à la main » dans chaque bloc + `--check` en CI |
