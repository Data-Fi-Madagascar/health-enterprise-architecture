# Plan d'alignement structurel : Fichiers directs → Sous-dossiers

> **Note :** Document historique de planification. La restructuration a été réalisée ; les liens internes font référence à des chemins obsolètes. Ce document est conservé à titre d'archive.

**Date :** 2026-08-13
**Objectif :** Aligner la structure des niveaux 01_cnisn, 02_artsn, 03_ptisn sur le pattern 00_caesn.
**Règle :** Seuls `glossary.md`, `acronyms.md`, `reading-matrix.md`, `index.md` restent en fichiers directs.

---

## 1. État actuel vs cible

### 01_cnisn — À restructurer

| Fichier actuel | Destination |
|----------------|-------------|
| `00_introduction.md` | `00_introduction/index.md` |
| `01_principes.md` | `01_principes/index.md` |
| `02_capacites.md` | `02_capacites/index.md` |
| `03_gouvernance.md` | `03_gouvernance/index.md` |
| `04_conformite.md` | `04_conformite/index.md` |
| `05_trajectoire.md` | `05_trajectoire/index.md` |
| `06_indicateurs.md` | `06_indicateurs/index.md` |
| `07_conclusion.md` | `07_conclusion/index.md` |
| `08_annexes/` | `08_annexes/` (déjà un dossier) |

### 02_artsn — À restructurer

| Fichier actuel | Destination |
|----------------|-------------|
| `00_fondations.md` | `00_fondations/index.md` |
| `01_flux-de-valeur.md` | `01_flux-de-valeur/index.md` |
| `02_exigences-contextuelles.md` | `02_exigences-contextuelles/index.md` |
| `03_chapitres/` | `03_chapitres/` (déjà un dossier) |
| `04_cartographie-cible.md` | `04_cartographie-cible/index.md` |
| `05_dictionnaire.md` | `05_dictionnaire/index.md` |
| `06_gouvernance.md` | `06_gouvernance/index.md` |
| `07_annexes/` | `07_annexes/` (déjà un dossier) |

### 03_ptisn — À restructurer

| Fichier actuel | Destination |
|----------------|-------------|
| `00_introduction.md` | `00_introduction/index.md` |
| `01_regles-utilisation.md` | `01_regles-utilisation/index.md` |
| `02_topologie-nationale-cible.md` | `02_topologie-nationale-cible/index.md` |
| `03_profils/` | `03_profils/` (déjà un dossier) |
| `04_matrice-alignement.md` | `04_matrice-alignement/index.md` |
| `05_profil-initiative.md` | `05_profil-initiative/index.md` |
| `06_gouvernance.md` | `06_gouvernance/index.md` |
| `07_conclusion.md` | `07_conclusion/index.md` |
| `08_annexes/` | `08_annexes/` (déjà un dossier) |

---

## 2. Fichiers à conserver en direct (tous niveaux)

- `index.md`
- `glossary.md`
- `acronyms.md`
- `reading-matrix.md`

---

## 3. Impact sur les liens

### 3.1 Liens relatifs internes
Après déplacement, les liens comme `[texte](../01_principes.md)` deviennent `[texte](../01_cnisn/01_principes/index.md)`.

### 3.2 Liens dans le referentiel
Les fichiers `referentiel/` ne changent pas — ils sont indépendants de la structure des wrappers.

### 3.3 Liens dans les enveloppes generated
Les blocs `<!-- BEGIN:GENERATED -->` utilisent des chemins absolus basés sur `domain:` — pas d'impact.

---

## 4. Plan d'implémentation

### Étape 1 : Créer les sous-dossiers (01_cnisn)
```
mkdir -p 01_cnisn/{00_introduction,01_principes,02_capacites,03_gouvernance,04_conformite,05_trajectoire,06_indicateurs,07_conclusion}
```

### Étape 2 : Déplacer les fichiers (01_cnisn)
```
mv 01_cnisn/00_introduction.md 01_cnisn/00_introduction/index.md
mv 01_cnisn/01_principes.md 01_cnisn/01_principes/index.md
... etc.
```

### Étape 3 : Répéter pour 02_artsn et 03_ptisn

### Étape 4 : Mettre à jour tous les liens relatifs
- Chercher tous les fichiers qui référencent les anciens chemins
- Remplacer `](../0X_*.md` par `](../0X_*/index.md`

### Étape 5 : Mettre à jour manifest.json

### Étape 6 : Vérifier les liens cassés

---

## 5. Vérification

```bash
# Vérifier les liens cassés
python3 -c "
import glob, os, re
for f in glob.glob('**/*.md', recursive=True):
    for m in re.finditer(r'\[[^\]]*\]\(([^)]+)\)', open(f).read()):
        link = m.group(1).split('#')[0]
        if link and not link.startswith(('http://','https://')) \
           and not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(f), link))):
            print('BROKEN', f, '->', link)
"
```
