# Baseline du refactor TOGAF HEA

## Contexte

Ce document capture l'état du dépôt avant le refactor `referentiel/` vers `04_architecture-repository/` et avant la suppression active des `CAP-INT-*`.

Le commit `HEAD` initial observé avant cette baseline est `c03f9f2 docs: finalize HEA TOGAF refactor plan`. Cette observation confirme que le plan et la spécification ont été intégrés avant l'exécution de la tâche 1.

## Etat git

La sortie suivante a été capturée avant la création du présent document. Elle constitue l'état de sécurité initial à préserver : la seule modification non liée à la tâche est `.gitignore`, qui ne doit pas être incluse dans le commit de baseline.

```bash
git branch --show-current
```

```text
codex/apply-audit-recommendations
```

```bash
git status --short
```

```text
 M .gitignore
```

## Validation initiale

Les contrôles ci-dessous ont été exécutés avant toute modification du référentiel documentaire. Ils établissent le nombre d'objets, l'état des liens, l'état de l'index et le nombre d'enveloppes générées au point de départ du refactor.

```bash
python3 scripts/validate_ref.py
```

```text
=== Validation du référentiel HEA ===
Objets indexés : 338
Liens relatifs vérifiés : 5885
[OK] Toutes les relations pointent vers un objet existant.
[OK] Aucun lien relatif cassé.
[OK] Tous les frontmatter sont du YAML valide.
[OK] Aucun objet isolé.
[OK] Tous les profils aboutissent à une capabilité CAESN.

[AVERTISSEMENT] Correspondances multi-niveaux : 4
  ~ referentiel/profils/pt-14.md (PT-14) : Profil mappe directement vers CAP-17 (capabilité CAESN, niveau 1) : vérifier si un CAP-INT intermédiaire est requis
  ~ referentiel/profils/pt-14.md (PT-14) : Profil mappe directement vers CAP-15 (capabilité CAESN, niveau 1) : vérifier si un CAP-INT intermédiaire est requis
  ~ referentiel/profils/pt-15.md (PT-15) : Profil mappe directement vers CAP-18 (capabilité CAESN, niveau 1) : vérifier si un CAP-INT intermédiaire est requis
  ~ referentiel/profils/pt-15.md (PT-15) : Profil mappe directement vers CAP-05 (capabilité CAESN, niveau 1) : vérifier si un CAP-INT intermédiaire est requis
  [INFO] CAP atteints par au moins un PT : 18/18
[OK] Toutes les capabilités CAESN sont atteintes par au moins un PT.

Résumé : CONFORME
```

```bash
python3 scripts/build_ref_index.py --check
```

```text
[OK] referentiel/_index.yaml à jour.
```

```bash
python3 scripts/build_wrappers.py --check
```

```text
OK : 101 enveloppes à jour
```

## Inventaire des références actives

La commande d'inventaire demandée a été exécutée sur le périmètre actif : `README.md`, `AGENTS.md`, `00_caesn/`, `01_cnisn/`, `02_artsn/`, `03_ptisn/` et `scripts/`.

```bash
rg -n "referentiel/|CAP-INT-[0-9]{2}" README.md AGENTS.md 00_caesn 01_cnisn 02_artsn 03_ptisn scripts
```

Synthèse comptée de la sortie `rg` :

| Indicateur | Total |
|------------|-------|
| Lignes correspondantes | 2429 |
| Fichiers contenant au moins une correspondance | 187 |
| Occurrences `referentiel/` | 3245 |
| Occurrences `CAP-INT-[0-9]{2}` | 697 |

Répartition par zone du dépôt :

| Zone | Fichiers | Lignes correspondantes | Occurrences `referentiel/` | Occurrences `CAP-INT-*` |
|------|----------|------------------------|-----------------------------|--------------------------|
| `README.md` | 1 | 17 | 32 | 1 |
| `AGENTS.md` | 0 | 0 | 0 | 0 |
| `00_caesn/` | 50 | 736 | 1331 | 65 |
| `01_cnisn/` | 23 | 482 | 320 | 327 |
| `02_artsn/` | 55 | 757 | 1229 | 93 |
| `03_ptisn/` | 50 | 413 | 311 | 202 |
| `scripts/` | 8 | 24 | 22 | 9 |

Répartition des occurrences `CAP-INT-*` par identifiant :

```text
  65 CAP-INT-01
  41 CAP-INT-02
  98 CAP-INT-03
  35 CAP-INT-04
  48 CAP-INT-05
  36 CAP-INT-06
  58 CAP-INT-07
  54 CAP-INT-08
  41 CAP-INT-09
  56 CAP-INT-10
  43 CAP-INT-11
  28 CAP-INT-12
  34 CAP-INT-13
  33 CAP-INT-14
  16 CAP-INT-15
  11 CAP-INT-16
```

Principaux fichiers par nombre d'occurrences combinées :

```text
00_caesn/10_annexes/matrice-tracabilite.md:521
02_artsn/03_objets-de-donnees/index.md:482
02_artsn/05_cartographie/composants.md:238
01_cnisn/08_annexes/e-correspondance-caesn.md:202
01_cnisn/02_capacites/index.md:181
00_caesn/00_overview/value-model.md:122
02_artsn/05_cartographie/index.md:114
01_cnisn/08_annexes/f-articulation-complete.md:106
00_caesn/03_capabilities/enabling.md:90
00_caesn/05_application/application-domains.md:76
00_caesn/04_data/objets.md:71
03_ptisn/04_matrice-alignement/index.md:69
00_caesn/03_capabilities/business.md:66
02_artsn/02_exigences-contextuelles/index.md:57
00_caesn/01_value-streams/vs-02-risk-protection.md:50
00_caesn/01_value-streams/vs-01-access-care.md:47
00_caesn/01_value-streams/vs-04-system-steering.md:43
00_caesn/01_value-streams/vs-03-financial-protection.md:42
00_caesn/05_application/shared-services.md:40
01_cnisn/08_annexes/a-matrice-principes-capacites.md:34
03_ptisn/03_profils/pt-14-interopabilite-transfrontaliere.md:34
README.md:33
02_artsn/08_annexes/a-table-de-maturite.md:32
03_ptisn/03_profils/pt-15-surveillance-one-health.md:28
01_cnisn/08_annexes/b-articulation-art-sn.md:27
01_cnisn/01_principes/index.md:26
03_ptisn/03_profils/pt-00-index.md:25
02_artsn/07_lots/index.md:21
03_ptisn/03_profils/pt-01-echange-interinstitutionnel.md:21
03_ptisn/03_profils/pt-02-mediation-intra-secteur.md:20
```
