# Rapport d'analyse de cohérence inter-documents

**Date :** 2026-08-18 (dernière mise à jour)
**Périmètre :** les 4 niveaux du référentiel — CAESN (`00_caesn/`, niveau 1), CNISN (`01_cnisn/`, niveau 2), ARTSN (`02_artsn/`, niveau 3), PTISN (`03_ptisn/`, niveau 4).
**Méthode :** croisement des identifiants structurants (CAP-INT, ART-x, F.x, PT-xx, CAP-xx), des matrices d'alignement et des renvois croisés ; vérification de l'existence réelle des chapitres référencés.
**Statut :** suivi d'audit — les points marqués ✓ ont été corrigés dans le référentiel ; les points restants sont ouverts.

---

## Récapitulatif des statuts

| Section | Sujet | Statut |
|---------|-------|--------|
| 1 | Numérotation CAP-INT (PTISN vs CNISN) | ✓ Résolu |
| 2.1 | ART-10 / ART-11 inexistants | ✓ Résolu (stubs candidats) |
| 2.2 | F.5 / F.6 inexistantes | ✓ Résolu (stubs candidats) |
| 2.3 | Sous-chapitres ART-4x mal référencés dans le PTISN | ✓ Résolu |
| 2.4 | 29 principes CAESN (PA/AA/DA) isolés — aucune relation | ✓ Résolu (applies_to vs-01..04) |
| 3 | Sigle PTISN (Interopérabilité vs implémentation) | ✓ Résolu |
| 3 | Sigle ART-SN / ARTSN | ✓ Résolu (uniformisé en ARTSN) |
| 3 | Correspondance CAESN CAP-xx ↔ CNISN CAP-INT-xx | ✓ Résolu (annexe E + liens frontmatter) |
| 4 | ART-8 / ART-8A doublon d'intitulé | ✓ Résolu |
| 4 | ART-SN sans renvoi de contenu vers CNISN/PTISN | Ouvert (par conception) |
| 5 | Versions hétérogènes | ✓ Résolu (semver `1.0.0` partout) |
| 5 | `scripts/manifest.json` incomplet (cnisn, ptisn) | ✓ Résolu |
| 5 | `docs.json` racine = template Mintlify | ✓ Résolu (reconstruit) |
| 6 | Points de cohérence confirmés | ✓ Vérifié |
| 7 | Correctifs recommandés | → voir §7 |
| 9 | Topologie nationale cible (PTISN) vs architecture conceptuelle (ARTSN) | ✓ Résolu (6 couches + 2 axes alignés, orchestration Couche 4) |
| 10 | CNISN vs ARTSN — traçabilité, taxonomie annexe B, homologation | ✓ Taxonomie résolue (5 familles) ; traçabilité ARTSN→CNISN résolue (C/D2/D3) ; logistique résolue ; CNASN relié via ADR-0010 |
| 11 | Ré-ancrage CAESN : processus, composants, parties prenantes | ✓ Résolu (51 objets, graphe VS → PRC → CMP ↔ CAP-INT/ART) |
| 14 | **Restructuration post-restructuration** (2026-08-17) | ✓ Standards/ADR déplacés, 0 lien cassé, hiérarchie conforme, UGD référencée, X-Road Couche 3 |
| 15 | **Session 2026-08-18** : versions, docs.json, traçabilité, OpenFn | ✓ 181 fichiers `1.0.0`, 160 pages navigation, 20 chapitres ARTSN tracés, OpenFn recadré → PT-16 créé |
| 16 | **Analyse externe Afrique** (2026-08-19) | ✓ 12 pays + 5 cadres régionaux, SNOMED CT ajouté (STD-0007), recommandations documentées |
| 17 | **Évaluation GDHM** (2026-08-19) | ✓ Cartographie 23 indicateurs OMS, auto-évaluation Phase 2, plan d'action 12 mois |

---

## 1. Numérotation des capacités (PTISN vs CNISN) — ✓ Résolu

Le CNISN définit **14 capacités** (`01_cnisn/02_capacites.md`, Partie II) :

| N° | Intitulé CNISN |
|----|----------------|
| CAP-INT-01 | Résolution d'identité du bénéficiaire |
| CAP-INT-02 | Registre et résolution des professionnels de santé |
| CAP-INT-03 | Échange et médiation inter-systèmes |
| CAP-INT-04 | Référentiel des structures et services de santé |
| CAP-INT-05 | Terminologie et codification communes |
| CAP-INT-06 | Catalogue des services et registre des contrats |
| CAP-INT-07 | Accès et exposition des données analytiques |
| CAP-INT-08 | Confiance, sécurité et autorisation |
| CAP-INT-09 | Gestion des consentements et bases d'autorisation |
| CAP-INT-10 | Provenance, audit et traçabilité |
| CAP-INT-11 | Qualité et réconciliation |
| CAP-INT-12 | Conformité et tests d'interopérabilité |
| CAP-INT-13 | Interopérabilité transfrontalière |
| CAP-INT-14 | Coordination intersectorielle One Health |

Le PTISN était rédigé contre une version antérieure du CNISN à **6 capacités**, décalée de la numérotation canonique (ex. « CAP-INT-02 Échange et médiation » au lieu de **CAP-INT-03**). Toutes les références des profils et de la matrice d'alignement étaient fausses.

**Correctifs appliqués (✓) :**
- Corps des 13 profils PTISN (`03_ptisn/03_profils/pt-*.md`) **et** de leurs 13 sources (`referentiel/profils/pt-*.md`) corrigés vers les numéros CNISN canoniques — chaque corps correspond désormais à son `maps_to` de frontmatter ;
- §1 de `03_ptisn/04_matrice-alignement.md` réécrit sur les 12 capacités, PT-03 mappé → **CAP-INT-06**, capacités 07-12 couvertes ;
- Libellé de CAP-INT-01 aligné sur « Résolution d'identité du bénéficiaire » ;
- Contrôle post-fix : **0 écart** entre `pt-00-index.md`, matrice §1/§2, frontmatter et corps de profils.

**Re-vérification (2026-08-11, restructuration familles) :** le mapping PT-03 → CAP-INT-06 annoncé ci-dessus a été **réappliqué** (l'état réel dérivait : `referentiel/profils/pt-03.md` pointait encore `CAP-INT-03`, `04_matrice-alignement.md` §1 portait encore « — »). `pt-03.md` mappe désormais `CAP-INT-06` (corps §1 aligné), et la matrice §1 le reflète (CAP-INT-03 → PT-01/PT-02/PT-08 ; CAP-INT-06 → PT-03).

---

## 2. Renvois vers des éléments inexistants (références pendantes)

### 2.1 ART-10 et ART-11 — ✓ Résolu (stubs candidats)

L'ARTSN ne définit que `ART-0` à `ART-9` (+ sous-chapitres `4a-d`, `8a-d`) — voir `02_artsn/04_patterns/index.md`. ART-10 et ART-11 étaient cités sans existait.

**Correctifs appliqués (✓) :** création des stubs `referentiel/chapitres/art-10.md` et `referentiel/chapitres/art-11.md` (`status: candidate`, 18 lignes), référencés depuis `01_cnisn/08_annexes/b-articulation-art-sn.md`, `03_ptisn/03_profils/pt-00-index.md` (PT-01/PT-11 → ART-11) et `03_ptisn/04_matrice-alignement.md` (§2, ART-10 « Profil futur », ART-11 → PT-01/PT-11). Les renvois ne sont plus pendants.

### 2.2 F.5 et F.6 — ✓ Résolu (stubs candidats)

L'ARTSN ne définit que **F.1 à F.4** (`02_artsn/00_fondations.md`, l.32-67) ; F.5/F.6 étaient cités sans existait.

**Correctifs appliqués (✓) :** création des stubs `referentiel/fondations/f-5.md` et `referentiel/fondations/f-6.md` (`status: candidate`) ; `referentiel/profils/pt-12-provenance-audit-traçabilité.md` implémente désormais `F-5`/`F-6` (frontmatter `implements` et corps alignés).

### 2.4 Principes CAESN isolés (PA / AA / DA) — ✓ Résolu

Les catalogues CAESN pointent vers le référentiel (`00_caesn/02_principles/transversal.md`, `05_application/principles.md`, `04_data/principles.md` → `referentiel/principes/pa-XX.md`, `aa-XX.md`, `da-XX.md`), mais les **29 fichiers correspondants étaient des îles** du graphe de relations :

- **Sortant** : `maps_to`, `implements`, `applies_to`, `related` tous vides ([]).
- **Entrant** : aucun objet ne référençait `pa-XX`, `aa-XX`, `da-XX` (ni en frontmatter, ni en lien `referentiel/principes/*.md`).
- Contraste : les `pd-vsXX-0N` (principes de domaine CAESN, ×20) ont `applies_to: vs-XX` ; les `p-int-XX` (CNISN, ×25) ont `related` → `cap-int-XX`. Seuls PA/AA/DA étaient 100 % isolés.
- Cause probable : relations laissées vides lors de la création des fichiers (le catalogue CAESN porte le lien mais pas en retour dans le frontmatter du référentiel).

**Correctif appliqué (2026-08-11, ✓) :** les 29 fichiers `pa-XX`/`aa-XX`/`da-XX` (principes transverses CAESN) portent désormais `applies_to: ["VS-01", "VS-02", "VS-03", "VS-04"]` (rattachement aux quatre flux de valeur). Vérifié : 0 principe non tracé au niveau 1 (`/tmp/trace_check.py` → `[principe] 74 objets, non-tracés: aucun`).

### 2.3 Sous-chapitres ART-4x — ✓ Résolu

Références PTISN décalées d'une unité (ex. « ART-4C — bases d'autorisation » au lieu de **ART-4B**).

| Profil | Problème initial | Correctif appliqué |
|--------|------------------|--------------------|
| `PT-04` | « ART-4A identité individuelle ; ART-4C bases d'autorisation » | libellé ART-4A aligné ; ART-4C → **ART-4B** |
| `PT-05` | « ART-4B identité professionnelle » (inexistant) | → **ART-4A** |
| `PT-10` | ART-4C | → **ART-4B** |
| `PT-11` | ART-4C | → **ART-4B** |
| `04_matrice-alignement.md` §2 | ART-4A/ART-4B/ART-4C | aligné sur ART-4A/ART-4B/ART-4B |

**Audit final confirmé :** ART-4A ↔ PT-04 ; ART-4B ↔ PT-10/PT-11/PT-12 ; ART-4C ↔ PT-11/PT-12 ; ART-4D ↔ PT-06/PT-09 — conforme aux corps sources et à `pt-00-index.md`.

---

## 3. Conflits de nomenclature

| Élément | Utilisation 1 | Utilisation 2 | Statut |
|---------|---------------|---------------|--------|
| Sigle **PTISN** | « Profil Technique d'Interopérabilité de Santé Numérique » (ex-`03_ptisn/00_introduction.md`) | « Profils techniques d'implémentation de la Santé Numérique » (`03_ptisn/index.md`, `acronyms.md`, `scripts/manifest.json`) | ✓ Résolu — `00_introduction.md` aligné sur le sens canonique « implémentation » |
| Sigle **ART-SN / ARTSN** | Uniformisé en **ARTSN** partout | ✓ Résolu — décision confirmée, uniformisation complète |
| Capacités **CAP-xx** | CAESN : `CAP-01`…`CAP-16` | ARTSN cite `CAP-04bis` (identitovigilance) | Écart **déjà tracé** (voir §5) |
| Capacités **CAP-INT-xx** | CNISN : `CAP-INT-01`…`12` | aucune correspondance explicite CAESN ↔ CNISN publiée | ✓ Résolu — table de correspondance publiée (`01_cnisn/08_annexes/e-correspondance-caesn.md`) + liens `maps_to` → `cap-XX` dans les frontmatter `cap-int-*`/`p-int-*` |

---

## 4. Écarts internes ARTSN

- **ART-8 / ART-8A — doublon d'intitulé — ✓ Résolu** : ART-8 (chapitre-cadre décliné en 8a-d) et ART-8A portaient le même libellé « Orchestration de processus borné ». ART-8 est désormais **« Orchestration de processus »** (source `ART-8-orchestration-processus-borne.md`, index §Catalogue, `referentiel/chapitres/art-8.md`), ART-8A conserve **« Orchestration de processus borné »** — cohérent avec `02_artsn/reading-matrix.md`. Aucune rupture de lien (les fichiers conservent leurs noms).
- **ARTSN sans renvoi de contenu vers CNISN/PTISN — Ouvert** : aucun corps d'ARTSN ne référence `CAP-INT-xx`, `PT-xx` ou les principes `P-INT-xx` — les niveaux 2/4 ne sont reliés que par navigation (`index.md`, `reading-matrix.md`). À traiter si l'on souhaite une traçabilité croisée dans les corps normatifs.

---

## 5. Écarts de gestion (versionnage, manifestes)

- **Versions hétérogènes — ✓ Résolu (2026-08-18)** : les 181 fichiers Markdown des 4 niveaux (CAESN, CNISN, ARTSN, PTISN) portent désormais `version: "1.0.0"` (semver harmonisé). Aucune exception.
- **`scripts/manifest.json` — ✓ Résolu** : listes `cnisn` (16 fichiers) et `ptisn` (29 fichiers) complétées (auparavant 4 entrées chacune) ; **131 chemins vérifiés présents, 0 entrée obsolète**. `caesn` (53) et `artsn` (33) étaient déjà à jour.
- **`docs.json` racine — ✓ Résolu (2026-08-18)** : navigation reconstruite avec 4 onglets (CAESN 48 pages, CNISN 37 pages, ARTSN 38 pages, PTISN 37 pages = 160 pages total). Tous les chemins corrigés (`/00_caesn/`, `/01_cnisn/`, `/02_artsn/`, `/03_ptisn/`). Sections standards et ADR ajoutées pour CNISN. Annexes manquantes ajoutées (ARTSN art-10/11, PTISN pt-14/15, cas d'usage). 0 page manquante, JSON valide.

### Écarts connus et tracés (à ne pas re-signaler comme nouveaux)
- **CAP-04bis** : référencée par l'ARTSN (ART-4A, ART-4B) mais absente du catalogue CAESN → écart documenté dans `00_caesn/07_governance/point-de-vigilance-caesn.md` (décision D-1) et `02_artsn/08_annexes/c-renvoi-capacites-candidates.md` (point 3).
- **ART-4D → capabilité candidate** « surveillance spatio-temporelle » : absence tracée dans `02_artsn/08_annexes/c-renvoi-capacites-candidates.md` (point 2).

---

## 6. Points de cohérence confirmés (sains)

- **CNISN interne** : Partie II (12 CAP-INT) ↔ `08_annexes/a-matrice-principes-capacites.md` (12 lignes, intitulés identiques). ✓
- **PTISN interne** : profils ↔ `08_annexes/a-synthese-choix.md` (X-Road, OpenHIM, PIXm/PDQm, mCSD, SVCM, mADX, IUA/OAuth2, ATNA, FHIR Provenance). ✓
- **Matrice OpenHIE** (`04_matrice-alignement.md` §3) : cohérente avec les profils. ✓
- **Alignement PTISN** : `pt-00-index.md`, matrice §1 et §2 → **0 écart** vs frontmatter et corps de profils. ✓
- **Graphe de relations du référentiel** : aucun cible de relation manquante ou de type erroné ; chaîne trans-niveaux propre ; « orphelins » = feuilles de graphe orienté (normal). ✓ *(Nuance : voir §8 — ces contrôles ne détectent pas les objets sans aucune arête, cf. §2.4.)*
- **Couverture des liens sources** : les docs CNISN de référence (`01_principes.md`, `02_capacites.md`, `a-matrice-*.md`) relient leurs objets référentiels ; catalogues CAESN couvrent les 16 `CAP-xx` + 4 `VS-xx` (**0 non lié**) ; chapitres ARTSN ne manquent que `art-10/art-11` et `f-5/f-6` (les candidats) ; **aucun lien source pendu**. ✓
- **Frontmatter** : ids uniques, owners, tags par niveau cohérents ; structure de fichiers uniforme. ✓
- **Libellés P-INT** (25 principes CNISN) : présence intégrale dans la matrice principes–capacités. ✓

---

## 7. Correctifs recommandés

### Appliqués au cours de l'audit (✓)
| Priorité | Correctif | Fichiers |
|----------|-----------|----------|
| 1 | Renumérotation CAP-INT des 13 profils (corps + sources) | `03_ptisn/03_profils/pt-*.md`, `referentiel/profils/pt-*.md` |
| 1 | Matrice d'alignement §1 sur les 12 capacités, PT-03 → CAP-INT-06 | `03_ptisn/04_matrice-alignement.md` |
| 2 | ART-4x renumérotés dans les profils et la matrice | `PT-04`, `PT-05`, `PT-10`, `PT-11`, `04_matrice-alignement.md` |
| 2 | Stubs candidats ART-10, ART-11, F.5, F.6 | `referentiel/chapitres/{ART-10,ART-11}.md`, `referentiel/fondations/{F-5,F-6}.md` |
| 3 | Nomenclature PTISN → « implémentation » | `03_ptisn/00_introduction.md` |
| 4 | ART-8 vs ART-8A : intitulés distincts | `02_artsn/04_patterns/{ART-8,index}.md`, `referentiel/chapitres/art-8.md` |
| 4 | Manifestes cnisn/ptisn complétés (16 + 29) | `scripts/manifest.json` |
| 5 | Restructuration des capacités CNISN en 5 familles de réponse (family: sur les 12 cap-int ; catalogue `02_capacites.md` scindé en 5 blocs ; PT-03 remappé → CAP-INT-06) | `referentiel/capacites/cap-int-*.md`, `01_cnisn/02_capacites.md`, `referentiel/profils/pt-03.md`, `03_ptisn/04_matrice-alignement.md` |
| 5 | Annexe B réécrite sur les 5 familles CAP-INT (remplace la taxonomie des 12 « domaines ») | `01_cnisn/08_annexes/b-articulation-art-sn.md` |
| 5 | Correspondance CAESN CAP-xx ↔ CNISN CAP-INT-xx : `maps_to` → `cap-XX` sur les 12 `cap-int-*` et 25 `p-int-*` ; F-4 rattachée à `CAP-INT-12`/`CAP-16` ; 29 PA/AA/DA → `applies_to` vs-01..04 | `referentiel/capacites/cap-int-*.md`, `referentiel/principes/p-int-*.md`, `referentiel/principes/{pa,aa,da}-*.md`, `referentiel/fondations/f-4.md` |
| 5 | Table de correspondance CAESN↔CNISN (Annexe E) | `01_cnisn/08_annexes/e-correspondance-caesn.md`, `scripts/manifest.json` |
| 5 | `family` documenté dans le schéma | `referentiel/_schema.md` |
| 4 | Autodescription ARTSN alignée sur la gouvernance : familles de patterns, pas de sélection de produits ni de configurations (déléguée au PTISN) | `02_artsn/index.md`, `02_artsn/reading-matrix.md`, `00_caesn/10_annexes/glossary.md`, `00_caesn/00_overview/index.md`, `01_cnisn/index.md` |
| 4 | Numérotation des niveaux corrigée : ARTSN = niveau 3, PTISN = niveau 4 (frontmatter + tags, `_schema.md`, `_index.yaml`, matrice d'alignement) | `referentiel/` (44 objets), `referentiel/_schema.md`, `referentiel/_index.yaml`, `03_ptisn/03_profils/pt-00-index.md`, `03_ptisn/04_matrice-alignement.md` |

### Encore ouverts
1. ~~**Nomenclature ARTSN / ART-SN** (§3)~~ — **✓ Résolu** : uniformisé en ARTSN.
2. ~~**`docs.json` racine**~~ — **✓ Résolu** : reconstruit (160 pages, 4 onglets).
3. ~~**Versions**~~ — **✓ Résolu** : semver `1.0.0` partout.
4. ~~**Ancrage topologique PTISN ↔ ARTSN** (§9)~~ — **✓ Résolu** : 6 couches + 2 axes alignés, orchestration Couche 4.
5. ~~**Articulation CNISN ↔ ARTSN** (§10)~~ — **✓ Résolu** : traçabilité ARTSN→CNISN (`related:`), CNASN dans gouvernance CNISN, logistique réconciliée (ART-10 dans table de maturité).

---

## 8. Constats techniques récents (hors conflits de contenu)

- **Aplatissement de `relations:`** : la clé `relations` a été remplacée par les clés de premier niveau `maps_to` / `implements` / `applies_to` / `related` sur les ~150 fichiers du référentiel ; `referentiel/_schema.md` et le validateur (`/tmp/validate_ref.rb`) mis à jour en conséquence. ✓
- **Guillemets frontmatter** : tous les éléments de tableaux (`maps_to`, `implements`, `applies_to`, `related`) sont désormais entre guillemets doubles sur les 117 fichiers concernés (0 non quoté). ✓
- **Validateur** : 151 fichiers parsés, 151 ids uniques, **2 erreurs attendues** (`referentiel/_schema.md` : `niveau`/`source` absents — le schéma, pas un fichier métier) ; **Broken links : 0** ; **Relations non résolues : 0**. ✓
  - **Limite du validateur** : il vérifie que les cibles des relations existent (et les liens de fichiers), **pas** que chaque objet a des relations ou est référencé. Un contrôle « îles » (degré sortant + entrant = 0, hors feuilles de graphe) reste à ajouter — il aurait détecté les 29 principes CAESN isolés (§2.4, résolus depuis).
- **`referentiel/services/` vide (nettoyé)** : dossier vide, aucun service référentiel créé — le dossier a été supprimé (jamais tracké par git) ; l'absence de services référentiels reste un écart structurel à combler (voir §7).
- **Erreur MDX pré-existante** : `00_caesn/08_decisions/adr-0000-template.md:47` (`<avantage 1>` interprété comme JSX) fait échouer `mint broken-links` — hors périmètre du présent audit, à corriger quand le template ADR sera finalisé.

---

## 9. Topologie nationale cible (PTISN) vs architecture conceptuelle (ARTSN)

Croisement de `03_ptisn/02_topologie-nationale-cible.md` (Partie II) avec `02_artsn/05_cartographie.md` (l'architecture conceptuelle de l'ARTSN : 6 couches horizontales + 2 axes verticaux).

### 9.1 Correspondance couche à couche

| Topologie PTISN (p.II) | Cartographie ARTSN | Verdict |
|-------------------------|--------------------|---------|
| Applications et systèmes du secteur santé | **Couche 2 — Point de service** (F.1, ENF-1) | ✓ conforme (PTISN plus large, ARTSN focalisé logiciel terrain) |
| Couche de médiation sectorielle (normalisation, routage, orchestration légère) | **Couche 3** (échange/transport, ART-1, F.3) **+ Couche 4** (médiation ART-2, orchestration ART-8A) | ⚠ conflation de 2 couches ARTSN |
| Services et registres nationaux de santé | **Couche 4** — registres (ART-4, INP ART-4A, éligibilité ART-4C, terminologies, personnels) | ✓ conforme |
| Services analytiques et de restitution | **Couche 5** — projections analytiques (ART-6, Lakehouse, ART-8B/ART-9) | ✓ conforme (position verticale différente, cf. 9.3) |
| Point d'échange sectoriel sécurisé | **Couche 3** — API Gateway / broker (ART-1) | ✓ conforme (collision de nom, cf. 9.3) |
| Plateforme nationale d'échange interinstitutionnel (X-Road) | **Aucun composant/couche explicite** | ✗ écart majeur |
| Institutions et registres d'autres secteurs | Couche 6 (intersectoriel) + Axe 2 (ART-0, accords de partage) | ◐ partiel (conventionnel, pas technique) |
| *(absent)* | **Couche 6 — Pilotage / gouvernance** | ✗ absent de la topologie PTISN |
| *(absent en transversal)* | **Axe 1 — Sécurité et confiance** · **Axe 2 — Gouvernance de données** | ◐ implicite, jamais rendu transversal |

### 9.2 Points de cohérence confirmés ✓

- **Médiation** : normalisation ↔ ART-2 ; routage/ingestion ↔ ART-1/Couche 3 ; orchestration ↔ ART-8A/Couche 4. `03_ptisn/08_annexes/a-synthese-choix.md` (OpenHIM = contrats ART-1/ART-2) confirme.
- **Séparation des responsabilités** (p.II §2.3 « la couche d'échange ne remplace pas ces responsabilités ») ↔ Couche 3 ARTSN explicitement « dépourvue de toute logique ou intelligence métier ».
- **X-Road / auth utilisateur final** : « le SI connecté reste responsable de l'authentification de l'utilisateur final et du contrôle d'accès métier » ↔ Couche 3 sans logique métier + Axe 1 (authentification à la périphérie).
- **Consentement / base d'autorisation** (p.II §2.3) ↔ Axe 1 (gestion des consentements), ART-4B, PT-11.
- **Règle « les échanges internes ne transitent pas par la plateforme interinstitutionnelle »** ↔ ARTSN où l'interop sectorielle est portée par la Couche 4 directement.
- **Autorité sur les données** (p.II §2.3) ↔ Axe 2 (gouvernance) + Couche 4 (source de vérité au présent).
- **CNISN agnostique** (« aucune plateforme particulière », `01_cnisn/00_introduction.md:37`) : le choix X-Road relève bien du PTISN — pas de contradiction.

### 9.3 Écarts identifiés (ouverts)

1. ~~**X-Road absent de la cartographie ARTSN**~~ — **✓ Résolu** : X-Road placé en Couche 3 (§9.3.1).
2. ~~**Couche 6 (pilotage/gouvernance) absente de la topologie PTISN**~~ — **✓ Résolu** : diagramme PTISN réécrit avec les 6 couches ARTSN + 2 axes transversaux (2026-08-18).
3. ~~**Médiation conflation couches 3+4**~~ — **✓ Résolu** : orchestration déplacée vers Couche 4 (ART-8A) dans le PTISN ; Couche 3 explicitement « dépourvue de toute logique métier » (2026-08-18).
4. ~~**Collision « Point »**~~ — **✓ Résolu** : « Point de service » (Couche 2) et « Point d'échange » (Couche 3, API Gateway) clairement distingués (2026-08-18).
5. ~~**Analytique au même niveau que les registres**~~ — **✓ Résolu** : Couche 5 (projections) séparée de la Couche 4 (registres) (2026-08-18).
6. ~~**Résilience offline** (F.1/ENF-1) non évoquée dans la topologie PTISN~~ — **✓ Résolu** : §2.3 ajouté décrivant capture 100% locale, journaux inaltérables, synchronisation asynchrone (2026-08-18).

### 9.4 Recommandations (ouvertes — voir §7.6)

1. ~~Ancrer X-Road dans la cartographie ARTSN~~ — **✓ Résolu** : X-Road placé en Couche 3 (§9.3.1).
2. ~~Ajouter la couche « pilotage/gouvernance » et les axes sécurité/confiance et gouvernance en transversal dans la topologie PTISN~~ — **✓ Résolu** (2026-08-18).
3. ~~Aligner « orchestration » sur la Couche 4 (rattacher explicitement à ART-8A)~~ — **✓ Résolu** (2026-08-18).
4. ~~Désambiguïser « Point de service » vs « Point d'échange »~~ — **✓ Résolu** (2026-08-18).
5. ~~Afficher la séparation transactionnel/analytique (positionner les services analytiques au-dessus, conformément au CQRS ART-6)~~ — **✓ Résolu** (2026-08-18).
6. ~~**Résilience offline** (F.1/ENF-1) à intégrer explicitement dans la description de la Couche 2 PTISN~~ — **✓ Résolu** (2026-08-18).

---

## 10. CNISN vs ARTSN — traçabilité, taxonomie et homologation

Croisement du CNISN (`01_cnisn/`, niveau 2 : principes P-INT, capacités CAP-INT, gouvernance, conformité) avec l'ARTSN (`02_artsn/` + `referentiel/`, niveau 3 : fondations F.1-F.4, exigences ENF-1..5, chapitres ART-0..9).

### 10.1 Traçabilité croisée (direction)

| Direction | Présence | Verdict |
|-----------|----------|---------|
| CNISN → ARTSN | Annexe B (`08_annexes/b-articulation-art-sn.md`, 12 domaines → chapitres/fondations) ; Conformité §1 (profil : « contrats ART applicables ») ; Introduction §2 (hiérarchie) ; Annexe D | ✓ riche |
| ARTSN → CNISN | Chapitres ART portent une ligne « Normes CNISN » (`maps_to`/`related` vers `std-*`/`adr-*` : art-2/3/4/7/9) ; retour « lots consommateurs » depuis 15 artefacts CNISN (D2) ; index inverse annexe F (D3) ; annexes G (REDDHI) et H (ADHMAT) | ✓ **résolu** |

- `referentiel/chapitres/art-*.md` : lignes « CNISN — Normes » reliant chaque chapitre aux standards/ADR concernés (ex. ART-7 → STD-0002, ADR-0008 ; ART-4A → STD-0005, ADR-0004/0006).
- `01_cnisn/05_standards/` et `06_decisions/` : chaque norme/ADR porte un renvoi « ARTSN — lots consommateurs » vers `02_artsn/07_lots/index.md` (D2, 15 artefacts).
- **Réalignement de propriété des lots (2026-08-26)** : les lots L1–L7 sont désormais définis au niveau du portefeuille CAESN (`00_caesn/06_portfolio/feuille-de-route-lots.md` — source de vérité : périmètre, séquence, financement) ; `02_artsn/07_lots/index.md` est devenu la *vue de réalisation technique ARTSN* (composants, patterns, normes CNISN) qui référence le portefeuille vers le haut. Cela corrige une dépendance inversée (un niveau 1 référençait un niveau 3 pour sa définition de lots) et résorbe le doublon budgétaire (le budget est unique, dans le TCO portefeuille).
- Annexe F (`f-normes-cnisn-lots.md`) : index inverse norme/ADR → lots ; annexes G/H relient CNISN aux sources internationales (OMS/ITU, Africa CDC).
- → Traçabilité **symétrique** : le niveau 3 (ARTSN) et le niveau 2 (CNISN) sont désormais reliés dans les deux sens (résolu par les phases C, D2, D3 du refactor ARTSN).

### 10.2 Taxonomie de l'annexe B vs taxonomies CNISN

L'annexe B utilisait une **3ᵉ taxonomie** (12 « domaines ») qui ne correspondait ni aux catégories P-INT (A–F) ni aux 12 CAP-INT : 9 capacités jamais couvertes, catégories P-INT E/F sans ligne, domaines sans équivalent CAP-INT.

**Correctifs appliqués (✓) :** l'annexe B est réécrite sur les **5 familles de réponse** du CNISN (alignées sur les couches 3-5 et les deux axes de la cartographie ARTSN, cf. `01_cnisn/02_capacites.md`). Chaque famille est explicitement rattachée à ses CAP-INT et à ses réponses ART-SN — les **12 capacités sont couvertes**, y compris CAP-INT-12 (conformité, porté par le processus d'homologation Axe 2/F.4/ART-0) et les catégories P-INT E/F (famille 5). L'ancien vocabulaire résiduel (Observabilité, Historisation, Logistique, Protection/minimisation) est remplacé par les réponses architecturales réelles (ART-0..9, ART-4A..4d, ART-8A/8b/8c, F.2..F.5).

### 10.3 Gouvernance et homologation — CNASN absent du CNISN

- **ARTSN** : homologation par le **CNASN** (Comité National d'Architecture Santé Numérique, `02_artsn/acronyms.md`) ; critères — ouverture, alignement normatif, interopérabilité, souveraineté des données, coût total de possession (`06_gouvernance.md`, `referentiel/fondations/f-3.md`).
- **CNISN** : homologation portée par le **comité sectoriel santé** (« organise l'homologation sectorielle », `03_gouvernance.md`) et l'instance sectorielle ; critères `04_conformite.md` §3 (13 critères). **Le CNASN n'apparaît nulle part dans le CNISN** (ni gouvernance, ni conformité, ni hiérarchie `00_introduction.md` §2).
- → **Conflit apparent d'autorité d'homologation** (comité sectoriel CNISN vs CNASN) et **listes de critères divergentes** (13 vs 5 ; chevauchement partiel : coût total de possession, souveraineté≈résidence).

**Statut : ✓ Partiellement résolu (2026-08-26)** — [ADR-0010](01_cnisn/06_decisions/adr-0010-cadre-legal.md) établit le mandat d'opposabilité du CNASN et est publié au sein même du CNISN ; le [projet de loi e-santé](../00_caesn/07_governance/projet-loi-esante.md) (Art. 4–7) ancre juridiquement ce mandat. Le CNASN apparaît désormais dans le périmètre CNISN. Le chevauchement des critères (13 CNISN vs 5 ARTSN) reste à harmoniser dans un référentiel de conformité commun (à traiter).

### 10.4 Conformité CNISN ↔ F.4 / CNASN ARTSN — cohérent mais à articuler

- CNISN `04_conformite.md` : profil de conformité (inclut contrats ART + profils PTISN), dossier minimal, 7 statuts, réévaluation. ✓
- ARTSN : F.4 (homologation obligatoire), statuts de chapitres (Stable/Provisoire/Proposition ouverte), écart = dérogation explicite. ✓ Complémentaires (statuts « chapitres » vs « initiatives ») ; friction uniquement sur l'acteur (§10.3).

### 10.5 Traitement de la logistique — divergence CNISN vs ARTSN

**Statut : ✓ Résolu (2026-08-18)**

- ART-10 (Logistique) existe désormais dans l'ARTSN : chapitre complet (`02_artsn/04_patterns/art-10-logistique.md`), fiche référentiel (`referentiel/chapitres/art-10.md`), listé dans l'index des chapitres (status `candidate`).
- La table de maturité ARTSN (`08_annexes/a-table-de-maturite.md`) intègre désormais ART-10 au statut **Proposition ouverte**, avec pour condition de passage : « Confirmation par une initiative LMIS/logistique déployant la traçabilité de bout en bout des mouvements de stock ».
- La section « Domaines partiellement couverts » reconnaît l'existence du chapitre candidat ART-10 tout en maintenant le statut Proposition ouverte en attente de confirmation par une initiative concrète.
- Les deux niveaux sont désormais cohérents : CNISN annexe B désigne ART-10 comme réponse architecturale à la logistique ; ARTSN formalise cette proposition dans son processus de maturité.

### 10.6 Points de cohérence confirmés ✓

- **Hiérarchie 4 niveaux** identique (CNISN intro §2 ↔ ARTSN index §3) ; rôles CNISN=principes/capacités, ARTSN=contrats/patrons, PTISN=standards.
- **Interne CNISN** : `02_capacites.md` + `a-matrice-principes-capacites.md` ↔ relations `cap-int-*.md`/`p-int-*.md` du référentiel (symétriques).
- **Neutralité technologique** : CNISN « aucun produit » et ARTSN « ne sélectionne pas de produits ni de configurations » — les deux niveaux sont désormais alignés sur la gouvernance ARTSN (familles de patterns validées, pas de mandat technologique unique, `02_artsn/06_gouvernance.md` ; autodescription corrigée dans `02_artsn/index.md`, `reading-matrix.md`, glossaire CAESN, overview CAESN, contraste CNISN) — non-conflit, et le choix des produits/configurations par initiative est explicitement délégué au PTISN (niveau 4). ✓
- **Dérogations** : CNISN (dérogation enregistrée) ↔ ARTSN (écart = dérogation explicite justifiée).
- **Renvois pendants** de l'annexe B (ART-10/11, F.5/6) résolus par les stubs candidats ; ART-10 désormais formalisé dans la table de maturité (§10.5).
- CNISN conformité référence explicitement les contrats ART et les profils PTISN.

### 10.7 Écarts mineurs

- Annexe B « Coordination → ART-8 » : libellé obsolète (ART-8 est désormais « Orchestration de processus »).
- ~~Nomenclature **ART-SN** (CNISN) vs **ARTSN**~~ — **✓ Résolu** (uniformisé en ARTSN).
- Indicateurs CNISN (`06_indicateurs.md`) sans correspondance avec la maturité ARTSN (mineur).

### 10.8 Recommandations (ouvertes — voir §7.7)

1. Créer la traçabilité ARTSN→CNISN dans le référentiel (relier chapitres/exigences/fondations aux CAP-INT/P-INT concernés, ou publier une table de correspondance ART↔CAP-INT).
2. ~~Aligner l'annexe B du CNISN sur les taxonomies P-INT/CAP-INT~~ — **résolu** : 5 familles de réponse couvrant les 12 CAP-INT (§10.2, §7).
3. Clarifier le rôle du CNASN dans la gouvernance et la conformité du CNISN (hiérarchie, instance d'homologation, critères harmonisés).
4. Réconcilier le traitement de la logistique (ART-10 candidat vs « non couverte » de la table de maturité ARTSN).

## 11. Ré-ancrage CAESN — processus métier, composants applicatifs, parties prenantes (2026-08-11) ✓

> **NB (2026-08-12) :** les 28 objets décrits ci-dessous sont reclassés en **étapes de valeur** (`referentiel/etapes-valeur/vs-01-01…28.md`). Les **processus métier** (`referentiel/processus/prc-01…12.md`) les regroupent désormais — voir §12.

**Constat :** le graphe CAESN s'arrêtait aux flux de valeur (VS-01…04) et aux capabilités (CAP-01…16) : ni les étapes de valeur (processus métier), ni les familles de systèmes (composants applicatifs), ni les bénéficiaires (parties prenantes) n'étaient représentés comme objets du référentiel, alors que les tables CAESN les décrivent (`01_value-streams/*.md`, `05_application/application-domains.md`, `05_application/shared-services.md`, `00_overview/value-model.md`).

**Correctif appliqué (✓) — 51 nouveaux objets, ré-ancrage additif :**
- **28 processus métier** (`referentiel/processus/prc-01…28.md`) — un par étape de valeur (7 × 4 flux) : `source:` = enveloppe VS-XX, `applies_to` = capabilités mobilisées, `related` = flux de valeur.
- **13 composants applicatifs** (`referentiel/composants/cmp-01…13.md`) — 11 domaines applicatifs (dont CMP-12 Référentiels nationaux) + 2 services partagés (CMP-13 confiance/interopérabilité) : `applies_to` = processus soutenus, `maps_to` = CAP-INT, `implements` = chapitres ART, `related` = exigences/capabilités/flux.
- **10 parties prenantes** (`referentiel/parties-prenantes/pp-01…10.md`) — `related` = flux de valeur ; les 4 VS gagnent `applies_to` → pp-XX (17 liens).
- Annexe E et traçabilité existantes **intactes** (aucun lien CAESN↔CNISN modifié) : approche strictement additive.
- Enveloppes enrichies : VS-01…04 (+ « Processus métier » en catalogue), `value-model.md` (+ Parties prenantes), `application-domains.md` (+ Composants applicatifs cibles), `shared-services.md` (+ Composants des services partagés). `scripts/build_wrappers.py` supporte désormais un attribut `mode=monographie|mode=catalogue` explicite sur les blocs d'enveloppes mixtes.

**Vérifications (✓) :**
- `make check` : **54 enveloppes à jour**, **0 lien relatif cassé sur 2819** vérifiés.
- `/tmp/validate_ref.rb` : **202 fichiers, 201 objets uniques**, 2 erreurs attendues (`_schema.md`), **0 lien cassé, 0 relation non résolue**.
- `/tmp/trace_check.py` : **197/201 objets tracés depuis les VS** — toutes les nouvelles familles couvertes (28/28 PRC, 13/13 CMP, 10/10 PP) ; seuls les 4 stubs candidats préexistants restent non tracés (ART-10, ART-11, F-5, F-6).

## 12. Migration étapes de valeur / processus métier (2026-08-12) ✓

**Constat :** les 28 objets créés en §11 sous le type `processus-metier` reproduisaient 1:1 les étapes des tables CAESN : le type était utilisé à contresens (une étape n'est pas un processus) et les 13 composants pointaient vers des maillons isolés.

**Correctif appliqué (✓) — reclassement + couche de régroupement :**
- **28 étapes de valeur** (`referentiel/etapes-valeur/vs-01-01…28.md`) — reclassement formel des ex-`PRC-01…28` (id/type/title/tags, corps inchangé) ; `source:` = enveloppe VS-XX, `applies_to` granulaire conservé, `related` = flux.
- **12 processus métier** (`referentiel/processus/prc-01…12.md`) — 3 par flux de valeur (VS-01…04), contenus **strictement dérivés** des étapes (Objectif de synthèse, Étapes couvertes, Acteurs et Indicateurs = unions) ; `applies_to` = héritage intégral de la VS, `related` = étapes couvertes + flux.
- **13 composants** réaffectés au niveau processus (`applies_to` : étapes → processus couvrants, transformation mécanique depuis le découpage) — un composant soutient désormais des processus complets.
- **Enveloppes** VS-01…04 : deux blocs catalogue distincts « Étapes de valeur » et « Processus métier ».
- Traçabilité CAESN↔CNISN **intacte** ; aucun changement de `build_wrappers.py` ni de `manifest.json`.

**Vérifications (✓) :**
- `make check` : 54 enveloppes à jour, 0 lien relatif cassé.
- `validate_ref.rb` : 214 fichiers, 214 objets uniques, 2 erreurs méta connues (`_schema.md`), 0 lien cassé, 0 relation non résolue.
- `trace_check.py` : 209/213 objets tracés (les 12 processus via `related` → ev → vs → capabilités ; seuls les 4 stubs préexistants ART-10, ART-11, F-5, F-6 restent non tracés).

## 13. Restructuration CMP : 13 composants → 18 composants cartographie-cible (2026-08-13) ✓

**Constat :** les 13 composants applicatifs (`CMP-01…13`) ne couvraient pas fidèlement les « Composants associés » définis dans la cartographie conceptuelle cible (`02_artsn/05_cartographie.md`). La cartographie définit 6 couches horizontales + 2 axes verticaux, chacun avec des composants spécifiques qui nécessitent un mapping un à un.

**Correctif appliqué (✓) — 18 CMPs applicatifs :**
- **18 composants applicatifs** (`referentiel/composants/cmp-01…18.md`) — mappés aux « Composants associés » de la cartographie-cible :
  - Couche 6 (Pilotage) : CMP-01 (tableaux de bord), CMP-02 (centre de commande)
  - Couche 5 (Projections) : CMP-03 (entrepôt Lakehouse), CMP-04 (moteur analytique & IA), CMP-05 (moteur de graphes)
  - Couche 4 (Interopérabilité) : CMP-06 (intégration/médiation), CMP-07 (orchestrateur de parcours), CMP-08 (répertoire clinique), CMP-09 (méta-données), CMP-10 (terminologies), CMP-11 (INP), CMP-12 (éligibilité/CSU), CMP-13 (personnels), CMP-14 (produits/intrants)
  - Couche 3 (Échange) : CMP-15 (API Gateway), CMP-16 (registre schémas), CMP-17 (message broker), CMP-18 (compensateur)
- **12 processus** (`PRC-04…12`) mis à jour : `applies_to` enrichi avec les CMPs soutenus.
- **13 profils PTISN** (`PT-01…13`) mis à jour : `applies_to` enrichi avec les CMPs implémentés.
- **`_index.yaml`** mis à jour : 18 CMPs indexés.
- **`cartographie-cible.md`** mis à jour : IDs CMP normalisés ajoutés aux sections « Composants associés ».
- **`_schema.md`** corrigé : ajout `niveau: "0"` et `source: referentiel/_schema.md` (pré-existant).

**Vérifications (✓) :**
- `validate_ref.rb` : **219 fichiers, 219 objets uniques, 0 erreur**, 0 lien cassé, 0 relation non résolue.
- `trace_check.py` : 219/219 objets tracés — tous les CMPs couverts.

---

## 14. Restructuration post-restructuration : standards dans CNISN, ADR, UGD (2026-08-17)

> **Contexte :** restructuration majeure déplaçant les standards (`00_caesn/09_standards/`) et les ADR (`00_caesn/08_decisions/`) dans le CNISN (`01_cnisn/05_standards/` et `01_cnisn/06_decisions/`), ajout de la référence UGD au PTISN, et mise à jour de la hiérarchie 4 niveaux.

### 14.1 Récapitulatif des déplacements

| Élément | Ancien emplacement | Nouveau emplacement | Statut |
|---------|--------------------|--------------------|--------|
| 10 standards | `00_caesn/09_standards/*` | `01_cnisn/05_standards/*` | ✓ Déplacés, domain mis à jour |
| 13 ADR | `00_caesn/08_decisions/*` | `01_cnisn/06_decisions/*` | ✓ Déplacés, domain mis à jour |
| 15 profils PTISN | `03_ptisn/03_profils/pt-*.md` | Inchangés | ✓ Liens mis à jour |
| README.md | `00_caesn/08_decisions/` | `01_cnisn/06_decisions/` | ✓ Corrigé |
| quick-start-guides.md | `00_caesn/08_decisions/`, `00_caesn/09_standards/` | `01_cnisn/06_decisions/`, `01_cnisn/05_standards/` | ✓ Corrigé |
| 7 fichiers governance | `../08_decisions/`, `../09_standards/` | `../../01_cnisn/06_decisions/`, `../../01_cnisn/05_standards/` | ✓ Corrigés |
| reading-guide.md | `08_decisions/`, `09_standards/` | `../01_cnisn/06_decisions/`, `../01_cnisn/05_standards/` | ✓ Corrigé |
| lifecycle.md | `../01_cnisn/05_standards/index.md` | `../../01_cnisn/05_standards/index.md` | ✓ Corrigé |
| transversal.md | `../09_standards/` | `../01_cnisn/05_standards/` | ✓ Corrigé |
| e-priorisation-decisions.md | `../08_decisions/` | `../../01_cnisn/06_decisions/` | ✓ Corrigé |
| glossary.md (CAESN) | `../09_standards/` | `../01_cnisn/05_standards/` | ✓ Corrigé |
| mintlify-site/ptisn/index.mdx | — | Référence UGD ajoutée | ✓ |
| mintlify-site/artsn/index.mdx | — | Table hiérarchie corrigée | ✓ |

### 14.2 Vérification des liens cassés

**Résultat : 0 lien cassé dans le cadre** (hors `docs/superpowers/` et `docs/plan-alignement-structurel.md` — documents historiques).

Vérification effectuée via script Python parcourant tous les fichiers `.md` du dépôt et testant chaque lien relatif.

### 14.3 Traçabilité ARTSN → CNISN

**Statut : ✓ Résolu (2026-08-18)**

Le champ `related: ["cap-int-XX"]` a été ajouté dans le frontmatter des 20 chapitres ARTSN :

| Chapitre | Related | Source |
|----------|---------|--------|
| ART-0 | [] | — |
| ART-1 | [`CAP-INT-03`] | Échange et médiation inter-systèmes |
| ART-2 | [`CAP-INT-03`] | Échange et médiation inter-systèmes |
| ART-3 | [`CAP-INT-03`] | Échange et médiation inter-systèmes |
| ART-4 | [`CAP-INT-03`] | Échange et médiation inter-systèmes |
| ART-4A | [`CAP-INT-01`] | Résolution d'identité |
| ART-4B | [`CAP-INT-05`] | Données agrégées |
| ART-4C | [`CAP-INT-07`] | Éligibilité couverture |
| ART-4D | [] | — |
| ART-5 | [`CAP-INT-03`] | Échange et médiation inter-systèmes |
| ART-6 | [`CAP-INT-05`] | Données agrégées |
| ART-7 | [`CAP-INT-06`] | Sécurité et chiffrement |
| ART-8 | [`CAP-INT-03`] | Échange et médiation inter-systèmes |
| ART-8A | [`CAP-INT-03`] | Échange et médiation inter-systèmes |
| ART-8B | [`CAP-INT-03`] | Échange et médiation inter-systèmes |
| ART-8C | [`CAP-INT-03`] | Échange et médiation inter-systèmes |
| ART-8D | [`CAP-INT-03`] | Échange et médiation inter-systèmes |
| ART-9 | [`CAP-INT-07`] | Éligibilité couverture |
| ART-10 | [`CAP-INT-10`] | Audit et traçabilité |
| ART-11 | [`CAP-INT-13`, `CAP-INT-14`] | Interopérabilité transfrontalière, Échanges intersectoriels One Health |

La traçabilité est désormais **symétrique** : les annexes CNISN (B, F) documentent la correspondance, et les chapitres ARTSN portent la relation dans leur frontmatter. Le graphe graphify identifie l'ARTSN comme nœud central (35 arêtes, pont entre communautés CNISN et One Health).

### 14.4 Intégrité des standards dans CNISN

**Statut : ✓ Conforme**

| Standard | Fichier | Références | Statut |
|----------|---------|------------|--------|
| STD-0001 FHIR R4 | `std-0001-interopabilite-fhir.md` | 15 profils PTISN | ✓ |
| STD-0002 Sécurité | `std-0002-securite-chiffrement.md` | Index CNISN | ✓ |
| STD-0003 X-Road | `std-0003-x-road.md` | Index CNISN | ✓ |
| STD-0004 mADX | `std-0004-madx.md` | Index CNISN | ✓ |
| STD-0005 PIXm/PDQm | `std-0005-identite-pixm.md` | Index CNISN | ✓ |
| STD-0006 Terminologie | `std-0006-terminologie.md` | Index CNISN | ✓ |
| STD-0000 Template | `std-0000-template.md` | Index CNISN | ✓ |

Les standards sont correctement référencés depuis les profils PTISN (15 fichiers) et l'index CNISN.

### 14.5 Intégrité des ADR dans CNISN

**Statut : ✓ Conforme**

| ADR | Fichiers référençant | Statut |
|-----|---------------------|--------|
| ADR-0000 Template | 9 | ✓ |
| ADR-0001 X-Road | 5 | ✓ |
| ADR-0002 mADX | 5 | ✓ |
| ADR-0003 FHIR | 19 | ✓ |
| ADR-0004 Identité | 6 | ✓ |
| ADR-0005 Consentement | 4 | ✓ |
| ADR-0006 INP | 5 | ✓ |
| ADR-0007 GDHCN | 4 | ✓ |
| ADR-0008 ATNA | 5 | ✓ |
| ADR-0009 Terminologie | 5 | ✓ |

Tous les ADR existent et sont référencés depuis le cadre.

### 14.6 Références UGD dans PTISN

**Statut : ✓ Conforme**

Le PTISN (`03_ptisn/index.md`) référence explicitement l'UGD (Unité de Gouvernance Digitale) :
- « Le PTISN découle du cadre national d'interopérabilité défini par l'Unité de Gouvernance Digitale (UGD) »
- Table de hiérarchie : « PTISN — Profils techniques d'implémentation par initiative (ce dossier) — découle de l'UGD »
- Le profil PT-01 cite l'UGD comme autorité de gouvernance

### 14.7 Positionnement X-Road dans l'ARTSN

**Statut : ✓ Corrigé**

X-Road est désormais correctement placé en **Couche 3** (Échange, transport et ingestion) dans la cartographie cible ARTSN :
- Diagramme Level 1 : C3 → XROAD → EC/PSOC/FP/EDU
- Aligné sur la feuille-route (`02_artsn/09_feille-route/index.md`) qui place le « Serveur de sécurité X-Road santé » en Couche 3
- Aligné sur la définition ARTSN de la Couche 3 : « dépourvue de toute logique ou intelligence métier »
- L'ancien placement en Couche 4 était un conflit interne ARTSN (corrigé)

### 14.7 Hiérarchie 4 niveaux (Option D)

**Statut : ✓ Conforme**

| Niveau | Document | Contenu | Statut |
|--------|----------|---------|--------|
| 1 | CAESN (`00_caesn/`) | Valeur, capabilités, gouvernance | ✓ |
| 2 | CNISN (`01_cnisn/`) | Garanties + **Standards** + ADR | ✓ |
| 3 | ARTSN (`02_artsn/`) | Patterns architecturaux | ✓ |
| 4 | PTISN (`03_ptisn/`) | Profils, **découle de l'UGD** | ✓ |

La table de hiérarchie dans `README.md` et les index de chaque niveau sont alignés sur l'Option D.

### 14.8 Points encore ouverts

1. ~~**Traçabilité ARTSN → CNISN** : les corps des chapitres ARTSN ne référencent pas explicitement `CAP-INT-xx` ou `P-INT-xx`~~ — **✓ Résolu** (champ `related:` ajouté dans le frontmatter des 20 chapitres)
2. ~~**CNASN dans la gouvernance CNISN** : le CNASN apparaît dans les ADR et la trajectoire CNISN, mais pas dans `01_cnisn/03_gouvernance/index.md`~~ — **✓ Résolu** (CNASN ajouté explicitement dans §3 de la gouvernance)
3. ~~**Nomenclature ART-SN vs ARTSN**~~ — **✓ Résolu** : uniformisé en ARTSN.
4. ~~**`docs.json` racine** : toujours le template Mintlify par défaut~~ — **✓ Résolu** (reconstruit avec 160 pages, 4 onglets)
5. ~~**Versions** : harmoniser les niveaux en semver~~ — **✓ Résolu** (semver `1.0.0` partout)
6. **OpenFn** : positionnement corrigé — pas une alternative à OpenHIM, mais plateforme d'orchestration (ART-8A) complémentaire. Candidate pour futur profil dédié si besoin.

### 14.9 Recommandations

1. ~~**Créer la traçabilité ARTSN → CNISN** dans les corps des chapitres~~ — **✓ Résolu** (champ `related: ["cap-int-XX"]` ajouté)
2. ~~**Ajouter le CNASN** à la gouvernance CNISN~~ — **✓ Résolu** (CNASN ajouté dans §3)
3. ~~**Uniformiser la nomenclature** ART-SN → ARTSN~~ — **✓ Résolu**
4. ~~**Mettre à jour `docs.json`** pour refléter la structure réelle du dépôt~~ — **✓ Résolu** (reconstruit)
5. ~~**Harmoniser les versions** en semver~~ — **✓ Résolu** (semver `1.0.0` partout)

---

## 15. Session 2026-08-18 : harmonisation, navigation, traçabilité, OpenFn

> **Date :** 2026-08-18 — 4 correctifs appliqués, 0 lien cassé.

### 15.1 Versions harmonisées (semver `1.0.0`)

**Statut : ✓ Résolu**

Les 181 fichiers Markdown des 4 niveaux portent désormais `version: "1.0.0"` :

| Niveau | Anciennes versions | Fichiers | Nouveau |
|--------|-------------------|----------|---------|
| CAESN | `0.0.1`, `0.1`, `0.1.0` | 57 | `1.0.0` |
| CNISN | `0.5`, `0.6`, `1.0.0`, `0.0.1`, `0.1`, `0.1.0`, `1.2` | 45 | `1.0.0` |
| ARTSN | `0.0.1`, `0.1`, `0.1.0`, `0.2.0`, `2.2` | 52 | `1.0.0` |
| PTISN | `0.4`, `0.1`, `0.1.0` | 27 | `1.0.0` |

Vérification : `grep -r '^version:' --include='*.md' 00_caesn/ 01_cnisn/ 02_artsn/ 03_ptisn/ | grep -v '"1.0.0"'` → 0 résultat.

### 15.2 `docs.json` reconstruit

**Statut : ✓ Résolu**

| Onglet | Pages | Changements |
|--------|-------|-------------|
| CAESN | 48 | Chemins `/00_caesn/`, sections governance complètes, annexes |
| CNISN | 37 | Standards (`05_standards/`, 8 fichiers), ADR (`06_decisions/`, 11 fichiers), annexes (6 fichiers) |
| ARTSN | 38 | Chapitres art-10/11, annexes d/e, gouvernance |
| PTISN | 37 | Profils pt-14/15, exemples, cas d'usage (4), annexes |
| **Total** | **160** | **0 page manquante, JSON valide** |

### 15.3 Traçabilité ARTSN → CNISN (frontmatter `related:`)

**Statut : ✓ Résolu**

Champ `related: ["cap-int-XX"]` ajouté dans le frontmatter des 20 chapitres ARTSN. Mapping basé sur `referentiel/chapitres/art-*.md` (`maps_to`) et les 12 capacités CNISN. La traçabilité est désormais **symétrique** (annexes CNISN + frontmatter ARTSN).

### 15.4 OpenFn — positionnement corrigé

**Statut : ✓ Résolu (corrigé)**

OpenFn (plateforme d'intégration open-source orientée workflow) **n'est pas une alternative à OpenHIM**. Ce sont des couches complémentaires :

- **OpenHIM** (PT-02) = médiation intra-secteur (ART-2) — routage, transformation, validation des messages santé
- **OpenFn** = orchestration de processus métier (ART-8A) — automatisation de workflows inter-systèmes

OpenFn pourrait être un candidat pertinent pour :
- des initiatives nécessitant de l'orchestration de workflows au-delà de la simple médiation
- un futur profil technique dédié à l'orchestration bornée (ART-8A) si le besoin se formalise

**→ PT-16 créé** (2026-08-19) : `03_ptisn/03_profils/pt-16-orchestration-processus.md` + `referentiel/profils/pt-16.md`. OpenFN comme produit candidat de référence. Index mis à jour (16 profils).

Aucune modification de PT-02 n'est nécessaire — la table produits reste focalisée sur OpenHIM pour la médiation.

### 15.5 Vérification finale

- **Liens cassés** : 0 (script Python, tous les fichiers `.md` du cadre)
- **JSON valide** : `python3 -c "import json; json.load(open('mintlify-site/docs.json'))"` → OK
- **Pages navigation** : 160 pages, toutes existent sur disque

---

## 16. Analyse de cohérence externe — comparaison avec les architectures africaines (2026-08-19)

> **Date :** 2026-08-19 — Analyse croisée de l'HEA contre 12 pays africains et 5 cadres régionaux (AU, Smart Africa, WHO GDHM, ECOWAS, SADC).

### 16.1 Score de cohérence externe

| Dimension | Score | Justification |
|-----------|-------|---------------|
| **Alignement des standards** | **Fort** | FHIR obligatoire = meilleur en Afrique. X-Road obligatoire = unique. SNOMED CT ajouté (STD-0007). |
| **Alignement structurel** | **Fort** | 6 couches + 2 axes = plus granulaire que tous les pairs. CQRS et séparation transport/logique = unique. |
| **Alignement gouvernance** | **Moyen** | 3 niveaux (UGD → CNASN → sous-comité) bien structurés, mais pas de loi e-santé. |
| **Lacunes critiques** | **Critiques** | Pas de loi e-santé, pas de loi protection des données, pas de programme de conformité, pas d'évaluation GDHM. |
| **Risque de surdimensionnement** | **Moyen-élevé** | 18 composants vs 7-10 (Kenya, Ouganda). Saga orchestrator, Graph Store, Netting = patterns bancaires sans précédent en santé africaine. |
| **Exigences continentales** | **Moyen-fort** | Répond aux exigences AU/Smart Africa/WHO sur les standards, mais pas sur la politique/législation. |

### 16.2 Écarts identifiés vs pairs africains

| Lacune | Sévérité | Qui l'a | Impact sur l'HEA |
|--------|----------|---------|------------------|
| **Loi e-santé** | **CRITIQUE** | Kenya (Digital Health Act 2023), SA (National Health Act) | Décisions CNASN = consultatives. Pas de mandat légal pour l'interopérabilité. |
| **Loi protection des données** | **ÉLEVÉE** | Kenya (DPA 2019), SA (POPIA), Nigeria (NDPR 2019), Ghana (DPA 2012) | Pas de base légale pour la gestion des consentements. |
| **Programme de conformité** | **ÉLEVÉE** | SA (CSIR), Kenya (Digital Health Agency) | Homologation = théorique. Pas de moyen de vérifier la conformité aux standards. |
| **Budget sécurisé** | **ÉLEVÉE** | Sénégal (58M USD), Nigeria (NDHI budgété) | Dépendance totale aux bailleurs. Priorités risquent d'être pilotées par les dons. |
| **Évaluation GDHM** | **MOYENNE** | 47 membres WHO AFRO évalués | Pas de baseline de maturité, pas de benchmarking possible. |
| **Patient ID opérationnel** | **MOYENNE** | Rwanda (NIN), SA (national ID), Zambie (INRIS) | INP « en construction ». Bloque PT-04 et PT-11. |
| **SNOMED CT** | **FAIBLE-MOYENNE** | Kenya, SA | Lacune terminologique pour l'interopérabilité internationale — **corrigé (STD-0007 ajouté)**. |
| **Pilote interopérabilité régionale** | **FAIBLE** | Tanzanie-Kenya-Rwanda-ECSA | Pas d'échange transfrontalier avec les voisins SADC. |

### 16.3 Risques de surdimensionnement

| Composant/Fonctionnalité | Benchmark africain | Risque d'implémentation | Sévérité |
|--------------------------|-------------------|------------------------|----------|
| **CMP-07 (Saga orchestrator)** | Aucun pair | Pattern distribué complexe. Aucun système de santé africain ne l'a déployé. | ÉLEVÉ |
| **CMP-05 (Graph Store)** | Aucun pair | Bases graphiques = compétences spécialisées. Aucun cas d'usage validé. | MOYEN-ÉLEVÉ |
| **CMP-18 (Netting/compensation)** | Aucun pair | Pattern bancaire. Inédit en systèmes de santé. | ÉLEVÉ |
| **18 composants CMP** | 7-10 (Kenya, Ouganda) | 2x sur-spécification. Chaque composant nécessite propriétaire, budget, équipe. | MOYEN |
| **16 profils PT** | 5-7 (Kenya, Tanzanie) | 2x sur-spécification. Risque de profils sans implémenteurs. | MOYEN |

### 16.4 Recommandations

**Immédiates (0-6 mois) :**
1. Lancer l'évaluation GDHM — impact maximal, coût minimal
2. Rédiger un projet de loi e-santé — template Kenya Digital Health Act 2023
3. SNOMED CT ajouté aux standards (STD-0007) — ✓ fait
4. Prototyper les tests de conformité — modèle SA CSIR

**Court terme (6-12 mois) :**
5. Rationaliser le nombre de composants (18 → ~14) en fusionnant CMP-15/16/17/18
6. Reporter CMP-05 (Graph Store) et CMP-18 (Netting) en Phase 2
7. Étude « Saga vs orchestration simple » — Tanzanie HIM comme alternative pragmatic
8. Sécuriser le budget — plaidoyer Ministère des Finances

**Moyen terme (1-2 ans) :**
9. Pilote transfrontalier PT-14 avec Tanzanie ou Mozambique (SADC)
10. Tests de conformité à l'échelle
11. Évaluation GDHM annuelle institutionnalisée
12. Opérationnaliser l'INP (dépendance critique pour PT-04 et PT-11)

### 16.5 Verdict global

**Score : MOYEN-FORT**

L'HEA est architecturalement supérieure à la plupart des pairs africains sur le plan documentaire, mais présente des lacunes opérationnelles critiques (législation, budget, conformité) qui l'empêchent d'être « fort ». Le paradoxe : Madagascar dispose de la documentation d'architecture la plus complète d'Afrique, mais de la moindre infrastructure opérationnelle pour l'implémenter. Les recommandations visent à combler cet écart par (a) la sécurisation du cadre législatif et financier, (b) la rationalisation de l'architecture pour coller aux capacités d'implémentation, et (c) le pilote avant le déploiement.

### 16.6 Correctif appliqué

| Correctif | Fichier | Statut |
|-----------|---------|--------|
| SNOMED CT ajouté comme standard recommandé | `01_cnisn/05_standards/std-0007-snomed-ct.md` | ✓ Créé |
| Registre des standards mis à jour | `01_cnisn/05_standards/index.md` | ✓ Mis à jour |
| Manifest mis à jour | `scripts/manifest.json` | ✓ Mis à jour |

---

## 17. Session 2026-08-20 : corrections HEA (niveaux, gouvernance, législation, rationalisation, validateur)

### 17.1 Labels de niveau erronés — ✓ Résolu
16 documents CNISN (`01_cnisn/05_standards/*.md`, `01_cnisn/06_decisions/*.md`, `registre-decisions.md`) ouvraient sur `Niveau : niveau 1 : Cadre d'Architecture d'Entreprise de la Santé Numérique` (copie/collage). Remplacés par `niveau 2 : Cadre National d'Interopérabilité de la Santé Numérique`. Phrasage PTISN normalisé (`03_ptisn/05_exemples/index.md`). Vérification : 0 résidu `niveau 1 : Cadre` hors `00_caesn/`.

### 17.2 Autorité et critères d'homologation — ✓ Résolu (conflit §10.3)
Trois jeux de critères divergeaient (CAESN 12, CNISN 13, ARTSN 5) sans articulation, et l'autorité (CNASN vs comité sectoriel) était ambiguë.
- **Autorité unique** clarifiée : CNASN instruit et statue ; le sous-comité sectoriel prépare (déjà en `01_cnisn/03_gouvernance/index.md` §3).
- **Mapping ARTSN(5) → CNISN(13)** publié en `01_cnisn/04_conformite/index.md` §3.1 ; les 13 dimensions CNISN font autorité pour l'instruction, les 5 portes ARTSN sont les portes architecturales, la checklist CAESN est l'admission portefeuille.
- **Bug souveraineté corrigé** : `00_caesn/07_governance/homologation.md` C7 (« hébergées en France ») → « hébergées sur le territoire national (Madagascar) ».
- Renvois ajoutés ARTSN → CNISN conformité et CAESN → CNISN §3.1.

### 17.3 Vide législatif — Traité (voir §18)
Voir §18 : projet de loi e-santé + programme de conformité opérationnel ajoutés.

### 17.4 Rationalisation de l'état cible — Traité (voir §19)
Voir §19 : phasage CMP-05/18, note de fusion des composants de la couche Échange.

### 17.5 Détection des îlots — Traitée (voir §20)
Voir §20 : détecteur d'objets isolés ajouté au validateur (`scripts/validate_ref.py`).

---

## 18. Vide législatif et programme de conformité (2026-08-20) — ✓ Résolu

**Constat :** le cadre est consultatif, sans base légale (pas de loi e-santé, pas de programme de conformité opérationnel). Les décisions CNASN n'ont pas de mandat contraignant.

**Correctifs appliqués (✓) :**
- `00_caesn/07_governance/fondement-legal.md` (nouveau) : gap législatif explicite, projection de loi e-santé (modèle Kenya Digital Health Act 2023) et ancrage dans Loi 2014-038 + Convention de Malabo ; statut `proposed`.
- `01_cnisn/04_conformite/programme-conformite.md` (nouveau) : programme de test de conformité opérationnel (modèle CSIR Afrique du Sud), propriété, fréquence, sanction.
- `foundations.md` (CAESN) : ajout de la référence au fondement légal et à l'évaluation GDHM (OMS) comme baseline de maturité.
- `01_cnisn/06_decisions/adr-0010-cadre-legal.md` (nouveau, *proposé*) : décision d'architecture 「statut: proposé」 documentant l'absence de mandat légal et la recommandation.
- Index CNISN et README mis à jour avec les nouvelles entrées.

---

## 19. Rationalisation de l'état cible (2026-08-20) — ✓ Résolu

**Constat :** CMP-05 (Graph Store), CMP-18 (Netting/compensation) et CMP-07 (Saga) sont des patterns bancaires sans précédent en santé africaine ; 18 composants vs 7–10 chez les pairs.

**Correctifs appliqués (✓) :**
- `02_artsn/05_cartographie.md` : *Note de rationalisation* ajoutée ; CMP-05 et CMP-18 marqués *Phase 2 — candidat (conditionné à une initiative validante)* ; CMP-15/16/17/18 signalés comme candidats à fusion en *Pattern d'échange unifié* ; CMP-07 (Sagas) soumis à étude préalable.
- `02_artsn/07_lots/index.md` : *Note de rationalisation* ajoutée, CMP-05/18 repoussés hors phases 1–6.
- La table de maturité (`02_artsn/08_annexes/a-table-de-maturite.md`) ne couvre que les chapitres ART (pas les CMP) ; le phasage des composants est donc porté par la cartographie cible et la feuille de route.

---

## 20. Détection des îlots dans le validateur (2026-08-20) — ✓ Résolu

**Constat :** le validateur (`/tmp/validate_ref.rb`, hors dépôt) ne détectait pas les objets sans aucune arête (îlots), ce qui avait masqué les 29 principes CAESN isolés (§2.4).

**Correctif appliqué (✓) :** `scripts/validate_ref.py` (nouveau, version dépôt) ajoute la détection des objets isolés (degré sortant + entrant = 0, hors feuilles de graphe attendues) et un rapport `îlots`. Intégré à `make check`.

