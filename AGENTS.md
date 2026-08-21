# AGENTS.md

Règles de travail pour toute tâche dans ce dépôt. À lire avant de créer ou modifier un document.

## Projet

Dépôt d'architecture documentée **as code** du secteur santé numérique de Madagascar, organisé selon la hiérarchie documentaire du CAESN en **quatre familles de documents**, chacune dans un dossier numéroté à la racine.

## Structure : dossiers numérotés

Tout dossier structurel du dépôt reçoit un **préfixe numérique de tri** sur deux chiffres (`00_`, `01_`, `02_`, …). Le numéro définit l'ordre de lecture et la hiérarchie ; le suffixe décrit le contenu en kebab-case.

| Niveau | Dossier | Contenu |
|--------|---------|---------|
| 1 | `00_caesn/` | Cadre d'Architecture d'Entreprise de la Santé Numérique (CAESN) |
| 2 | `01_cnisn/` | Cadre National d'Interopérabilité de la Santé Numérique (CNISN) |
| 3 | `02_artsn/` | Architecture de Référence Technique de la Santé Numérique (ARTSN) |
| 4 | `03_ptisn/` | Profils techniques d'implémentation par initiative (PTISN) |

## Sous-dossiers numérotés de `00_caesn/`

| Dossier | Contenu |
|---------|---------|
| `00_overview/` | Vue d'ensemble, fondements, modèle de valeur |
| `01_value-streams/` | Flux de valeur nationaux (VS-01 à VS-04) |
| `02_principles/` | Principes transversaux (PA) et de domaine (PD) |
| `03_capabilities/` | Capabilités CAP-01..16, maturité, runway |
| `04_data/` | Architecture des données et de l'information sanitaire |
| `05_application/` | Architecture applicative et systèmes numériques |
| `06_portfolio/` | Portefeuille d'initiatives orienté valeur |
| `07_governance/` | Instances, RACI, Bureau de Réalisation de la Valeur |
| `08_decisions/` | Architecture Decision Records (ADR) |
| `09_standards/` | Normes obligatoires et standards recommandés |
| `10_annexes/` | Matrice de lecture, glossaire, acronymes |

## Conventions des fichiers Markdown

Chaque fichier (sauf `README.md` racine) commence par un frontmatter YAML. Les valeurs de `domain` et les identifiants suivent la règle **« le nom reflète la localisation »** :

- `domain:` : **obligatoire** — valeur = nom du dossier parent immédiat, **préfixe numérique inclus** (ex. `domain: 01_value-streams` pour un fichier dans `00_caesn/01_value-streams/`). Il reflète ainsi la localisation exacte du document.
- `id:` : identifiant sémantique stable en kebab-case (ex. `data-governance`, `capabilities-business`). Ne change pas lorsque le dossier est renommé.
- Autres champs : `title`, `version`, `status`, `last_reviewed`, `owner`, `tags`.

## Règle « aligné sur la localisation »

À appliquer à tout nouveau document et à tout renommage de dossier :

1. **Nommer** le dossier avec le préfixe numérique dans l'ordre de lecture.
2. **Renseigner** `domain:` avec le nom du dossier parent immédiat, **préfixe numérique inclus** (ex. `01_value-streams`).
3. **Mettre à jour** tous les liens relatifs Markdown quand un dossier est déplacé ou renommé.
4. **Vérifier** qu'aucun lien n'est cassé après chaque changement de structure (aucun lien `url:` ou `id:` vers un chemin obsolète).

## Vérification des liens

Après toute modification de structure, valider qu'il n'existe aucun lien relatif cassé :

```bash
python3 - <<'EOF'
import glob, os, re
for f in glob.glob('**/*.md', recursive=True):
    for m in re.finditer(r'\[[^\]]*\]\(([^)]+)\)', open(f).read()):
        link = m.group(1).split('#')[0]
        if link and not link.startswith(('http://','https://')) \
           and not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f), link))):
            print('BROKEN', f, '->', link)
EOF
```

## Langue

Les documents sont rédigés en **français**. Les noms de dossiers et identifiants sont en kebab-case anglais.