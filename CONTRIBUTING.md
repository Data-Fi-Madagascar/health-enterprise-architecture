---
title: Guide de contribution au Cadre d'Architecture d'Entreprise de la Santé Numérique
domain: root
id: contributing
version: "1.0.0"
status: active
last_reviewed: 2026-09-03
owner: Bureau de Réalisation de la Valeur
tags: ["gouvernance", "contribution", "guide"]
---

# Guide de contribution

Merci de votre intérêt pour contribuer au **Cadre d'Architecture d'Entreprise de la Santé Numérique (HEA)** de Madagascar. Ce document explique comment contribuer efficacement au dépôt.

## 📋 Table des matières

1. [Prérequis](#prérequis)
2. [Configuration de l'environnement](#configuration-de-lenvironnement)
3. [Structure du dépôt](#structure-du-dépôt)
4. [Processus de contribution](#processus-de-contribution)
5. [Conventions de codage](#conventions-de-codage)
6. [Validation des modifications](#validation-des-modifications)
7. [Création de Pull Requests](#création-de-pull-requests)
8. [Revue de code](#revue-de-code)
9. [Gestion des ADR](#gestion-des-adr)
10. [Ressources utiles](#ressources-utiles)

---

## 🔧 Prérequis

### Outils requis

| Outil | Version | Installation | Usage |
|-------|---------|-------------|-------|
| **Git** | ≥ 2.30 | [git-scm.com](https://git-scm.com/) | Contrôle de version |
| **Python** | ≥ 3.10 | [python.org](https://python.org/) | Scripts de validation |
| **make** |Any | `brew install make` (Mac) / `sudo apt install make` (Linux) | Orchestration |
| **pandoc** | ≥ 2.0 | `brew install pandoc` / `sudo apt install pandoc` | Génération DOCX |
| **GitHub CLI** | ≥ 2.0 | `brew install gh` / [github.com/cli](https://cli.github.com/) | Gestion des PR |

### Dépendances Python

```bash
# Créer l'environnement virtuel
make venv

# Ou manuellement
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.\.venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

---

## 💻 Configuration de l'environnement

### 1. Cloner le dépôt

```bash
git clone https://github.com/Data-Fi-Madagascar/health-enterprise-architecture.git
cd health-enterprise-architecture
```

### 2. Configurer l'environnement Python

```bash
# Créer et activer l'environnement virtuel
make venv

# Vérifier l'installation
python -c "import rdflib, pyshacl, yaml; print('✓ Toutes les dépendances sont installées')"
```

### 3. Vérifier la configuration

```bash
# Exécuter toutes les validations
make check

# Si tout est vert : ✅
# Sinon, corriger les erreurs signalées
```

---

## 🗂️ Structure du dépôt

```
health-enterprise-architecture/
├── 00_caesn/          # Niveau 1: Cadre d'Architecture d'Entreprise
│   ├── 00_overview/   # Vue d'ensemble et modèle de valeur
│   ├── 01_value-streams/ # Flux de valeur (VS-01 à VS-04)
│   ├── 02_principles/ # Principes transversaux et de domaine
│   ├── 03_capabilities/ # Capabilités (CAP-01 à CAP-18)
│   └── ...
│
├── 01_cnisn/          # Niveau 2: Cadre National d'Interopérabilité
│   ├── 00_introduction/
│   ├── 01_principes/
│   ├── 02_capacites/  # Capacités d'interopérabilité
│   ├── 06_decisions/  # ADR (Architecture Decision Records)
│   └── ...
│
├── 02_artsn/          # Niveau 3: Architecture de Référence Technique
│   ├── 00_fondations/
│   ├── 03_objets-de-donnees/ # Dictionnaire de données
│   ├── 04_patterns/   # Chapitres ART (ART-0 à ART-11)
│   └── ...
│
├── 03_ptisn/          # Niveau 4: Profils Techniques
│   ├── 03_profils/    # Profils PT-01 à PT-19
│   └── ...
│
├── referentiel/       # Source de vérité (objets de référence)
│   ├── capabilites/
│   ├── capacites/
│   ├── chapitres/
│   ├── profils/
│   └── _index.yaml    # Registre de tous les objets
│
├── scripts/           # Scripts Python de validation et génération
│   ├── validate_ref.py
│   ├── build_wrappers.py
│   ├── compile_rdf.py
│   └── ...
│
├── .github/           # Configuration GitHub
│   └── workflows/
│       ├── ci.yml     # Validation continue
│       └── release.yml
│
├── Makefile           # Cibles de build
├── README.md          # Documentation principale
├── AGENTS.md          # Règles pour les agents (IA, scripts)
└── CONTRIBUTING.md    # Ce document
```

### Règle fondamentale : "Le nom reflète la localisation"

Chaque document doit avoir un champ `domain:` dans son frontmatter qui correspond **exactement** au nom de son dossier parent, préfixe numérique inclus.

```yaml
# Exemple pour un fichier dans 00_caesn/01_value-streams/
domain: 01_value-streams
```

---

## ✍️ Processus de contribution

### 1. Identifier le type de contribution

| Type | Exemple | Dossier concerné |
|------|---------|------------------|
| **Nouvelle capabilité** | Ajouter CAP-19 | `00_caesn/03_capabilities/` + `referentiel/capabilites/` |
| **Nouveau profil** | Ajouter PT-20 | `03_ptisn/03_profils/` + `referentiel/profils/` |
| **Modification de principe** | Mettre à jour PA-01 | `00_caesn/02_principles/` + `referentiel/principes/` |
| **Nouvelle décision** | ADR-0011 | `01_cnisn/06_decisions/` |
| **Correction de bug** | Fixer un lien cassé | Tous les dossiers |

### 2. Vérifier l'existence de l'objet dans le référentiel

```bash
# Rechercher un objet existant
grep -r "id: CAP-01" referentiel/

# Vérifier dans l'index
grep "CAP-01" referentiel/_index.yaml
```

### 3. Créer ou modifier les fichiers

#### Pour un nouvel objet :
1. Créer le fichier dans `referentiel/<type>/<id>.md`
2. Ajouter le frontmatter YAML avec tous les champs requis
3. Ajouter l'objet à `referentiel/_index.yaml`

#### Pour une modification :
1. Modifier le fichier source dans `referentiel/`
2. Régénérer les enveloppes : `make wrappers`
3. Vérifier les liens : `python scripts/check_links.py`

---

## 📜 Conventions de codage

### 1. Frontmatter YAML

**Champs obligatoires** pour chaque fichier Markdown (sauf README.md racine) :

```yaml
---
title: "Titre en français"
id: identifiant-en-kebab-case
domain: 01_value-streams  # Doit correspondre au dossier parent
version: "1.0.0"
status: draft | review | active | deprecated
date: YYYY-MM-DD  # Pour les ADR
last_reviewed: YYYY-MM-DD
owner: DEPSI | Bureau de Réalisation de la Valeur | etc.
tags: ["tag1", "tag2"]
---
```

### 2. Nommage des fichiers

| Type | Convention | Exemple |
|------|------------|---------|
| Capabilité | `cap-XX.md` | `cap-01.md` |
| Capacité | `cap-int-XX.md` | `cap-int-01.md` |
| Principe | `p-int-XX.md` | `p-int-01.md` |
| Profil | `pt-XX.md` | `pt-01.md` |
| ADR | `adr-XXXX-<sujet>.md` | `adr-0001-x-road.md` |
| Chapitre ART | `art-X.md` | `art-0.md` |

### 3. Liens Markdown

**Toujours utiliser des liens relatifs** :

```markdown
# ✅ Bon
[CAP-01](../capabilites/cap-01.md)
[ART-0](../chapitres/art-0.md)

# ❌ À éviter
[CAP-01](https://github.com/.../cap-01.md)  # Lien absolu
[CAP-01](#cap-01)  # Ancre sans fichier
```

### 4. Qualité rédactionnelle (norme Gartner)

Voir [AGENTS.md](AGENTS.md) pour les règles détaillées :

- ✅ **Paragraphes analytiques** : Chaque section doit contenir des paragraphes explicatifs
- ✅ **Pas de tableaux sans analyse** : Chaque tableau doit être précédé/suivi d'un commentaire
- ✅ **Vocabulaire formel** : Utiliser "constitué", "révèle", "conditionne", "traduit"
- ✅ **Connecteurs logiques** : "C'est précisément", "Cette observation", "Plus fondamentalement"
- ❌ **Interdits** : Caractères chinois, em-dashes (`—`), séparateurs horizontaux (`---`)

---

## ✅ Validation des modifications

### 1. Validation locale avant commit

```bash
# Vérifier que tout est valide
make check

# Ou individuellement
python scripts/validate_ref.py      # Vérifie le graphe de relations
python scripts/check_links.py       # Vérifie les liens cassés
python scripts/build_wrappers.py --check  # Vérifie la cohérence des enveloppes
```

### 2. Validation RDF/SHACL

```bash
# Compiler le graphe RDF
make rdf

# Valider avec SHACL
make rdf --validate
```

### 3. Génération des documents

```bash
# Générer les DOCX consolidés
make docx

# Générer les DOCX publics
make public

# Tout générer
make oda
```

---

## 🚀 Création de Pull Requests

### 1. Préparer la branche

```bash
# Créer une branche avec un nom descriptif
git checkout -b feature/nouvelle-capabilite-cap-19
git checkout -b fix/lien-casse-dans-pt-01
git checkout -b docs/mise-a-jour-readme

# Ou utiliser la convention vibe/ pour les contributions automatisées
git checkout -b vibe/<description>-a5f549
```

### 2. Commiter les modifications

```bash
# Ajouter tous les fichiers modifiés
git add -A

# Commiter avec un message clair
git commit -m "feat(capabilites): ajouter CAP-19 Gestion des urgences"
git commit -m "fix(pt-01): corriger lien cassé vers ART-0"
git commit -m "docs: mettre à jour la matrice de lecture"

# Conventions de messages de commit
# - feat: nouvelle fonctionnalité
# - fix: correction de bug
# - docs: modification de documentation
# - refactor: réorganisation de code
# - chore: maintenance
```

### 3. Pousser et créer la PR

```bash
# Pousser la branche
git push -u origin feature/nouvelle-capabilite-cap-19

# Créer la Pull Request via GitHub CLI
gh pr create --draft --title "feat: ajouter CAP-19 Gestion des urgences" \
  --body "Ajout de la nouvelle capabilité CAP-19 avec ses liens vers les principes et composants."

# Ou via l'interface web GitHub
```

### 4. Remplir le template de PR

Chaque PR doit inclure :
- **Titre** : Court et descriptif (utiliser les préfixes `feat:`, `fix:`, `docs:`, etc.)
- **Description** : Expliquer le **pourquoi**, pas juste le **quoi**
- **Validation** : Confirmer que `make check` passe
- **Impact** : Lister les fichiers modifiés et les dépendances
- **Liens** : Référencer les issues, ADR, ou discussions liées

---

## 👀 Revue de code

### Critères de revue

| Critère | Vérification |
|---------|--------------|
| **Frontmatter valide** | `domain:` correspond au dossier |
| **Liens valides** | `make check` passe |
| **Pas de liens cassés** | `scripts/check_links.py` passe |
| **Graphe cohérent** | `scripts/validate_ref.py` passe |
| **RDF valide** | `make rdf` passe |
| **Conformité Gartner** | Respect des règles de [AGENTS.md](AGENTS.md) |
| **Langue française** | Pas de termes anglais non expliqués |

### Processus de revue

1. **Auto-revue** : Exécuter `make check` avant de demander une revue
2. **Revue par les pairs** : Au moins 1 approbation requise
3. **Validation CI** : Tous les checks GitHub Actions doivent passer
4. **Merge** : Seulement après approbation et CI verte

---

## 📝 Gestion des ADR

### Quand créer un ADR ?

Un **Architecture Decision Record (ADR)** doit être créé lorsque :
- Un choix architectural structurant est fait
- Une décision impacte plusieurs composants
- Une alternative a été rejetée après analyse
- Une décision doit être documentée pour la postérité

### Processus ADR

1. **Créer le fichier ADR** :
   ```bash
   # Copier le template
   cp 01_cnisn/06_decisions/adr-0000-template.md 01_cnisn/06_decisions/adr-0011-nouveau-sujet.md
   ```

2. **Remplir le template** :
   - **Contexte** : Situation actuelle et problème
   - **Décision** : Choix fait (une phrase claire)
   - **Justification** : Pourquoi ce choix ?
   - **Conséquences** : Avantages et inconvénients
   - **Alternatives** : Autres options considérées et pourquoi rejetées

3. **Ajouter au registre** :
   - Mettre à jour `01_cnisn/06_decisions/index.md`
   - Mettre à jour `01_cnisn/06_decisions/registre-decisions.md`

4. **Valider et commiter** :
   ```bash
   git add 01_cnisn/06_decisions/adr-0011-*.md
   git commit -m "docs(adr): ajouter ADR-0011 sur [sujet]"
   ```

### Statuts des ADR

| Statut | Description | Transition |
|--------|-------------|------------|
| `proposé` | Décision en discussion | → `accepté` ou `rejeté` |
| `accepté` | Décision validée par le comité | → `appliqué` |
| `appliqué` | Décision implémentée | → `dépassé` ou `déprécié` |
| `remplacé` | Remplacé par un autre ADR | - |
| `déprécié` | Décision abandonnée | - |

---

## 🔗 Ressources utiles

### Documentation interne

- [README.md](README.md) - Vue d'ensemble du dépôt
- [AGENTS.md](AGENTS.md) - Règles pour les agents et scripts
- [quick-start-guides.md](quick-start-guides.md) - Guides par profil
- [00_caesn/reading-guide.md](00_caesn/reading-guide.md) - Guide de lecture CAESN
- [01_cnisn/reading-guide.md](01_cnisn/reading-guide.md) - Guide de lecture CNISN

### Outils externes

- [GitHub Docs](https://docs.github.com/) - Documentation GitHub
- [Git Handbook](https://guides.github.com/introduction/git-handbook/) - Guide Git
- [Markdown Guide](https://www.markdownguide.org/) - Syntaxe Markdown
- [YAML Spec](https://yaml.org/spec/) - Spécification YAML

### Contacts

| Rôle | Contact |
|------|---------|
| **Responsable Architecture** | Bureau de Réalisation de la Valeur |
| **Équipe Technique** | DEPSI |
| **Mainteneur du dépôt** | À définir |

---

## ✨ Bonnes pratiques

### Do's ✅
- [ ] Lire [AGENTS.md](AGENTS.md) avant toute modification
- [ ] Exécuter `make check` avant de commiter
- [ ] Utiliser des messages de commit clairs et descriptifs
- [ ] Documenter les décisions architecturales avec des ADR
- [ ] Respecter la règle "le nom reflète la localisation"
- [ ] Utiliser des liens relatifs dans le Markdown
- [ ] Inclure des paragraphes analytiques dans les documents

### Don'ts ❌
- [ ] Commiter des fichiers binaires (`.docx`, `.pdf`, `.xlsx`)
- [ ] Utiliser des liens absolus ou des URL externes sans validation
- [ ] Modifier les enveloppes générées manuellement (elles sont régénérées par `make wrappers`)
- [ ] Utiliser des em-dashes (`—`) ou des séparateurs horizontaux (`---`)
- [ ] Laisser des liens cassés dans la documentation
- [ ] Oublier de mettre à jour `referentiel/_index.yaml` pour les nouveaux objets

---

## 🚨 Résolution des problèmes courants

### Problème : `make check` échoue

```bash
# Voir quels checks échouent
make check 2>&1 | grep -E "(ERREUR|FAIL|Error)"

# Exécuter chaque validation individuellement
python scripts/validate_ref.py
python scripts/check_links.py
python scripts/build_wrappers.py --check
```

### Problème : Fichier binaire commité accidentellement

```bash
# Supprimer du tracking Git
git rm --cached fichier.docx

# Ajouter au .gitignore
echo "*.docx" >> .gitignore
git add .gitignore
git commit -m "chore: ajouter .docx au .gitignore"
```

### Problème : Lien cassé détecté

```bash
# Trouver les liens cassés
python scripts/check_links.py 2>&1 | grep "BROKEN"

# Corriger le lien dans le fichier
# Puis vérifier
python scripts/check_links.py
```

### Problème : Objet isolé dans le graphe

```bash
# Identifier les objets isolés
python scripts/validate_ref.py 2>&1 | grep -A 5 "isolé"

# Ajouter des relations dans le frontmatter
# Exemple : maps_to, implements, applies_to, related
```

---

*Document maintenu par le Bureau de Réalisation de la Valeur. Dernière révision : 2026-09-03.*
