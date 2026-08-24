# Plan de restructuration : Découpage des fichiers volumineux en documents séparés

**Date :** 2026-08-13
**Objectif :** Découper les fichiers volumineux (>200 lignes) en documents séparés par section, tout en préservant la cohérence de l'architecture existante.

---

## 1. Contexte et contraintes

### Architecture existante
- **Couche référentiel** : 219+ objets atomiques dans `referentiel/`
- **Couche wrappers** : Documents narratifs qui agrègent le référentiel via `<!-- BEGIN:GENERATED -->`
- **Script `build_wrappers.py`** : injecte le contenu du référentiel dans les wrappers

### Règles à respecter
1. Préserver la lisibilité séquentielle (chaque niveau reste un « livre »)
2. Maintenir les liens existants (frontmatter `domain:`, `maps_to`, `implements`, etc.)
3. Mettre à jour `scripts/manifest.json` et `build_wrappers.py` si nécessaire
4. Vérifier qu'aucun lien n'est cassé après le découpage

---

## 2. Fichiers à découper par niveau

### Niveau 1 : `00_caesn/` (CAESN) — Déjà bien structuré
**Statut :** ✅ Pas de découpage nécessaire — chaque sujet est déjà un fichier séparé.

### Niveau 2 : `01_cnisn/` (CNISN) — Fichiers candidates
| Fichier | Lignes | Sections | Découpage proposé |
|---------|--------|----------|-------------------|
| `01_principes.md` | 526 | 6 catégories (A-F) | 6 fichiers : `01a-principes-categorie-a.md` etc. |
| `02_capacites.md` | 408 | 5 familles | 5 fichiers : `02a-capacites-famille-1.md` etc. |
| `03_gouvernance.md` | 140 | 6 fonctions | 6 fichiers : `03a-gouvernance-instance.md` etc. |

### Niveau 3 : `02_artsn/` (ARTSN) — Fichiers candidates
| Fichier | Lignes | Sections | Découpage proposé |
|---------|--------|----------|-------------------|
| `05_cartographie.md` | 350 | 6 couches + 2 axes | 8 fichiers : `04a-couche-1-infrastructure.md` etc. |
| `03_objets-de-donnees.md` | ~200 | Variables du dictionnaire | 1 fichier par groupe logique |

### Niveau 4 : `03_ptisn/` (PTISN) — Déjà bien structuré
**Statut :** ✅ Pas de découpage nécessaire — les profils sont déjà dans `03_profils/`.

---

## 3. Stratégie de découpage pour chaque fichier

### 3.1 `01_cnisn/01_principes.md` → 6 fichiers

**Structure actuelle :**
```
## Catégorie A — Autorité et mandat (P-INT-01..04)
## Catégorie B — Contrat et interface (P-INT-05..09)
## Catégorie C — Versionnement et compatibilité (P-INT-10..13)
## Catégorie D — Sécurité et confiance (P-INT-14..18)
## Catégorie E — Qualité et monitoring (P-INT-19..22)
## Catégorie F — Gouvernance et évolution (P-INT-23..25)
```

**Proposition :**
- `01_principes.md` → fichier d'index qui renvoie aux 6 catégories
- `01_principes/01-categorie-a.md` (Autorité et mandat)
- `01_principes/02-categorie-b.md` (Contrat et interface)
- `01_principes/03-categorie-c.md` (Versionnement)
- `01_principes/04-categorie-d.md` (Sécurité)
- `01_principes/05-categorie-e.md` (Qualité)
- `01_principes/06-categorie-f.md` (Gouvernance)

### 3.2 `01_cnisn/02_capacites.md` → 5 fichiers

**Structure actuelle :**
```
## Famille 1 — Référentiels et identités (CAP-INT-01..05)
## Famille 2 — Échange et médiation (CAP-INT-03,06)
## Famille 3 — Données analytiques (CAP-INT-07)
## Famille 4 — Confiance et sécurité (CAP-INT-08..10)
## Famille 5 — Qualité et conformité (CAP-INT-11..12)
```

**Proposition :**
- `02_capacites.md` → fichier d'index
- `02_capacites/01-famille-1-referentiels.md`
- `02_capacites/02-famille-2-echange.md`
- `02_capacites/03-famille-3-analytique.md`
- `02_capacites/04-famille-4-confiance.md`
- `02_capacites/05-famille-5-qualite.md`

### 3.3 `01_cnisn/03_gouvernance.md` → 6 fichiers

**Structure actuelle :**
```
## 1. Instance porteuse
## 2. Fonctions
### 2.1 Stratégie d'interopérabilité
### 2.2 Normalisation
### 2.3 Conformité
### 2.4 Gestion des référentiels
### 2.5 Coordination
### 2.6 Support
```

**Proposition :**
- `03_gouvernance.md` → fichier d'index
- `03_gouvernance/01-instance.md`
- `03_gouvernance/02-strategie.md`
- `03_gouvernance/03-normalisation.md`
- `03_gouvernance/04-conformite.md`
- `03_gouvernance/05-referentiels.md`
- `03_gouvernance/06-coordination.md`
- `03_gouvernance/07-support.md`

### 3.4 `02_artsn/05_cartographie.md` → 8 fichiers

**Structure actuelle :**
```
## Vue d'ensemble
## Couche 1 — Infrastructure
## Couche 2 — Point de service
## Couche 3 — Échange
## Couche 4 — Interopérabilité
## Couche 5 — Projections analytiques
## Couche 6 — Pilotage
## Axe 1 — Sécurité et confiance
## Axe 2 — Gouvernance de données
```

**Proposition :**
- `05_cartographie.md` → fichier d'index
- `04_cartographie/01-couche-1-infrastructure.md`
- `04_cartographie/02-couche-2-point-service.md`
- `04_cartographie/03-couche-3-echange.md`
- `04_cartographie/04-couche-4-interop.md`
- `04_cartographie/05-couche-5-projections.md`
- `04_cartographie/06-couche-6-pilotage.md`
- `04_cartographie/07-axe-1-securite.md`
- `04_cartographie/08-axe-2-gouvernance.md`

---

## 4. Impact sur les scripts et le référentiel

### 4.1 `scripts/manifest.json`
- Ajouter les nouveaux fichiers aux listes `cnisn` et `artsn`
- Vérifier que les chemins sont corrects

### 4.2 `scripts/build_wrappers.py`
- Vérifier que les blocs `<!-- BEGIN:GENERATED -->` fonctionnent avec les nouveaux fichiers
- Si nécessaire, ajuster les modes `monographie` et `catalogue`

### 4.3 Liens relatifs
- Mettre à jour tous les liens relatifs dans les fichiers qui référencent les anciens fichiers
- Vérifier avec le script de vérification des liens

---

## 5. Plan d'implémentation

### Phase 1 : Préparation (1 jour)
1. Sauvegarder l'état actuel (`git stash` ou branche)
2. Lister tous les liens qui pointent vers les fichiers à découper
3. Créer les sous-dossiers nécessaires

### Phase 2 : Découpage CNISN (2 jours)
1. Découper `01_principes.md` en 6 fichiers + index
2. Découper `02_capacites.md` en 5 fichiers + index
3. Découper `03_gouvernance.md` en 6 fichiers + index
4. Mettre à jour `manifest.json`
5. Vérifier les liens

### Phase 3 : Découpage ARTSN (1 jour)
1. Découper `05_cartographie.md` en 8 fichiers + index
2. Mettre à jour `manifest.json`
3. Vérifier les liens

### Phase 4 : Validation (1 jour)
1. Exécuter `make check` ou équivalent
2. Exécuter `validate_ref.rb`
3. Exécuter `trace_check.py`
4. Vérifier que Mintlify/PDF se génèrent correctement

---

## 6. Risques et mitigations

| Risque | Impact | Mitigation |
|--------|--------|------------|
| Liens cassés | Élevé | Script de vérification avant/après |
| Perte de lisibilité séquentielle | Moyen | Créer des fichiers d'index avec navigation |
| Incompatibilité `build_wrappers.py` | Élevé | Tester chaque fichier avant commit |
| Duplication de contenu | Faible | Le référentiel reste la source unique |

---

## 7. Critères de succès

- [ ] Aucun lien cassé après le découpage
- [ ] Tous les fichiers ont un frontmatter conforme
- [ ] `manifest.json` est à jour
- [ ] `build_wrappers.py` fonctionne correctement
- [ ] La lecture séquentielle reste possible via les fichiers d'index
- [ ] Le coherence-report.md n'a plus d'écarts liés à la structure
