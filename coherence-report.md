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
| 4 | ART-8 / ART-8a doublon d'intitulé | ✓ Résolu |
| 4 | ART-SN sans renvoi de contenu vers CNISN/PTISN | Ouvert (par conception) |
| 5 | Versions hétérogènes | ✓ Résolu (semver `1.0.0` partout) |
| 5 | `scripts/manifest.json` incomplet (cnisn, ptisn) | ✓ Résolu |
| 5 | `docs.json` racine = template Mintlify | ✓ Résolu (reconstruit) |
| 6 | Points de cohérence confirmés | ✓ Vérifié |
| 7 | Correctifs recommandés | → voir §7 |
| 9 | Topologie nationale cible (PTISN) vs architecture conceptuelle (ARTSN) | ✓ Résolu (6 couches + 2 axes alignés, orchestration Couche 4) |
| 10 | CNISN vs ARTSN — traçabilité, taxonomie annexe B, homologation | ◐ Taxonomie résolue (5 familles) ; traçabilité ARTSN→CNISN, CNASN, logistique ouverts |
| 11 | Ré-ancrage CAESN : processus, composants, parties prenantes | ✓ Résolu (51 objets, graphe VS → PRC → CMP ↔ CAP-INT/ART) |
| 14 | **Restructuration post-restructuration** (2026-08-17) | ✓ Standards/ADR déplacés, 0 lien cassé, hiérarchie conforme, UGD référencée, X-Road Couche 3 |
| 15 | **Session 2026-08-18** : versions, docs.json, traçabilité, OpenFn | ✓ 181 fichiers `1.0.0`, 160 pages navigation, 20 chapitres ARTSN tracés, OpenFn PT-02 |

---

## 1. Numérotation des capacités (PTISN vs CNISN) — ✓ Résolu

Le CNISN définit **12 capacités** (`01_cnisn/02_capacites.md`, Partie II) :

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

Le PTISN était rédigé contre une version antérieure du CNISN à **6 capacités**, décalée de la numérotation canonique (ex. « CAP-INT-02 Échange et médiation » au lieu de **CAP-INT-03**). Toutes les références des profils et de la matrice d'alignement étaient fausses.

**Correctifs appliqués (✓) :**
- Corps des 13 profils PTISN (`03_ptisn/03_profils/pt-*.md`) **et** de leurs 13 sources (`referentiel/profils/pt-*.md`) corrigés vers les numéros CNISN canoniques — chaque corps correspond désormais à son `maps_to` de frontmatter ;
- §1 de `03_ptisn/04_matrice-alignement.md` réécrit sur les 12 capacités, PT-03 mappé → **CAP-INT-06**, capacités 07-12 couvertes ;
- Libellé de CAP-INT-01 aligné sur « Résolution d'identité du bénéficiaire » ;
- Contrôle post-fix : **0 écart** entre `pt-00-index.md`, matrice §1/§2, frontmatter et corps de profils.

**Re-vérification (2026-08-11, restructuration familles) :** le mapping PT-03 → CAP-INT-06 annoncé ci-dessus a été **réappliqué** (l'état réel dérivait : `referentiel/profils/pt-03.md` pointait encore `cap-int-03`, `04_matrice-alignement.md` §1 portait encore « — »). `pt-03.md` mappe désormais `cap-int-06` (corps §1 aligné), et la matrice §1 le reflète (CAP-INT-03 → PT-01/PT-02/PT-08 ; CAP-INT-06 → PT-03).

---

## 2. Renvois vers des éléments inexistants (références pendantes)

### 2.1 ART-10 et ART-11 — ✓ Résolu (stubs candidats)

L'ARTSN ne définit que `ART-0` à `ART-9` (+ sous-chapitres `4a-d`, `8a-d`) — voir `02_artsn/03_chapitres/index.md`. ART-10 et ART-11 étaient cités sans existait.

**Correctifs appliqués (✓) :** création des stubs `referentiel/chapitres/art-10.md` et `referentiel/chapitres/art-11.md` (`status: candidate`, 18 lignes), référencés depuis `01_cnisn/08_annexes/b-articulation-art-sn.md`, `03_ptisn/03_profils/pt-00-index.md` (PT-01/PT-11 → ART-11) et `03_ptisn/04_matrice-alignement.md` (§2, ART-10 « Profil futur », ART-11 → PT-01/PT-11). Les renvois ne sont plus pendants.

### 2.2 F.5 et F.6 — ✓ Résolu (stubs candidats)

L'ARTSN ne définit que **F.1 à F.4** (`02_artsn/00_fondations.md`, l.32-67) ; F.5/F.6 étaient cités sans existait.

**Correctifs appliqués (✓) :** création des stubs `referentiel/fondations/f-5.md` et `referentiel/fondations/f-6.md` (`status: candidate`) ; `referentiel/profils/pt-12-provenance-audit-traçabilité.md` implémente désormais `f-5`/`f-6` (frontmatter `implements` et corps alignés).

### 2.4 Principes CAESN isolés (PA / AA / DA) — ✓ Résolu

Les catalogues CAESN pointent vers le référentiel (`00_caesn/02_principles/transversal.md`, `05_application/principles.md`, `04_data/principles.md` → `referentiel/principes/pa-XX.md`, `aa-XX.md`, `da-XX.md`), mais les **29 fichiers correspondants étaient des îles** du graphe de relations :

- **Sortant** : `maps_to`, `implements`, `applies_to`, `related` tous vides ([]).
- **Entrant** : aucun objet ne référençait `pa-XX`, `aa-XX`, `da-XX` (ni en frontmatter, ni en lien `referentiel/principes/*.md`).
- Contraste : les `pd-vsXX-0N` (principes de domaine CAESN, ×20) ont `applies_to: vs-XX` ; les `p-int-XX` (CNISN, ×25) ont `related` → `cap-int-XX`. Seuls PA/AA/DA étaient 100 % isolés.
- Cause probable : relations laissées vides lors de la création des fichiers (le catalogue CAESN porte le lien mais pas en retour dans le frontmatter du référentiel).

**Correctif appliqué (2026-08-11, ✓) :** les 29 fichiers `pa-XX`/`aa-XX`/`da-XX` (principes transverses CAESN) portent désormais `applies_to: ["vs-01", "vs-02", "vs-03", "vs-04"]` (rattachement aux quatre flux de valeur). Vérifié : 0 principe non tracé au niveau 1 (`/tmp/trace_check.py` → `[principe] 74 objets, non-tracés: aucun`).

### 2.3 Sous-chapitres ART-4x — ✓ Résolu

Références PTISN décalées d'une unité (ex. « ART-4c — bases d'autorisation » au lieu de **ART-4b**).

| Profil | Problème initial | Correctif appliqué |
|--------|------------------|--------------------|
| `pt-04` | « ART-4a identité individuelle ; ART-4c bases d'autorisation » | libellé ART-4a aligné ; ART-4c → **ART-4b** |
| `pt-05` | « ART-4b identité professionnelle » (inexistant) | → **ART-4a** |
| `pt-10` | ART-4c | → **ART-4b** |
| `pt-11` | ART-4c | → **ART-4b** |
| `04_matrice-alignement.md` §2 | ART-4a/ART-4b/ART-4c | aligné sur ART-4a/ART-4b/ART-4b |

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

- **ART-8 / ART-8a — doublon d'intitulé — ✓ Résolu** : ART-8 (chapitre-cadre décliné en 8a-d) et ART-8a portaient le même libellé « Orchestration de processus borné ». ART-8 est désormais **« Orchestration de processus »** (source `art-8-orchestration-processus-borne.md`, index §Catalogue, `referentiel/chapitres/art-8.md`), ART-8a conserve **« Orchestration de processus borné »** — cohérent avec `02_artsn/reading-matrix.md`. Aucune rupture de lien (les fichiers conservent leurs noms).
- **ARTSN sans renvoi de contenu vers CNISN/PTISN — Ouvert** : aucun corps d'ARTSN ne référence `CAP-INT-xx`, `PT-xx` ou les principes `P-INT-xx` — les niveaux 2/4 ne sont reliés que par navigation (`index.md`, `reading-matrix.md`). À traiter si l'on souhaite une traçabilité croisée dans les corps normatifs.

---

## 5. Écarts de gestion (versionnage, manifestes)

- **Versions hétérogènes — ✓ Résolu (2026-08-18)** : les 181 fichiers Markdown des 4 niveaux (CAESN, CNISN, ARTSN, PTISN) portent désormais `version: "1.0.0"` (semver harmonisé). Aucune exception.
- **`scripts/manifest.json` — ✓ Résolu** : listes `cnisn` (16 fichiers) et `ptisn` (29 fichiers) complétées (auparavant 4 entrées chacune) ; **131 chemins vérifiés présents, 0 entrée obsolète**. `caesn` (53) et `artsn` (33) étaient déjà à jour.
- **`docs.json` racine — ✓ Résolu (2026-08-18)** : navigation reconstruite avec 4 onglets (CAESN 48 pages, CNISN 37 pages, ARTSN 38 pages, PTISN 37 pages = 160 pages total). Tous les chemins corrigés (`/00_caesn/`, `/01_cnisn/`, `/02_artsn/`, `/03_ptisn/`). Sections standards et ADR ajoutées pour CNISN. Annexes manquantes ajoutées (ARTSN art-10/11, PTISN pt-14/15, cas d'usage). 0 page manquante, JSON valide.

### Écarts connus et tracés (à ne pas re-signaler comme nouveaux)
- **CAP-04bis** : référencée par l'ARTSN (ART-4a, ART-4b) mais absente du catalogue CAESN → écart documenté dans `00_caesn/07_governance/point-de-vigilance-caesn.md` (décision D-1) et `02_artsn/07_annexes/c-renvoi-capacites-candidates.md` (point 3).
- **ART-4d → capabilité candidate** « surveillance spatio-temporelle » : absence tracée dans `02_artsn/07_annexes/c-renvoi-capacites-candidates.md` (point 2).

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
| 2 | ART-4x renumérotés dans les profils et la matrice | `pt-04`, `pt-05`, `pt-10`, `pt-11`, `04_matrice-alignement.md` |
| 2 | Stubs candidats ART-10, ART-11, F.5, F.6 | `referentiel/chapitres/{art-10,art-11}.md`, `referentiel/fondations/{f-5,f-6}.md` |
| 3 | Nomenclature PTISN → « implémentation » | `03_ptisn/00_introduction.md` |
| 4 | ART-8 vs ART-8a : intitulés distincts | `02_artsn/03_chapitres/{art-8,index}.md`, `referentiel/chapitres/art-8.md` |
| 4 | Manifestes cnisn/ptisn complétés (16 + 29) | `scripts/manifest.json` |
| 5 | Restructuration des capacités CNISN en 5 familles de réponse (family: sur les 12 cap-int ; catalogue `02_capacites.md` scindé en 5 blocs ; PT-03 remappé → CAP-INT-06) | `referentiel/capacites/cap-int-*.md`, `01_cnisn/02_capacites.md`, `referentiel/profils/pt-03.md`, `03_ptisn/04_matrice-alignement.md` |
| 5 | Annexe B réécrite sur les 5 familles CAP-INT (remplace la taxonomie des 12 « domaines ») | `01_cnisn/08_annexes/b-articulation-art-sn.md` |
| 5 | Correspondance CAESN CAP-xx ↔ CNISN CAP-INT-xx : `maps_to` → `cap-XX` sur les 12 `cap-int-*` et 25 `p-int-*` ; f-4 rattachée à `cap-int-12`/`cap-16` ; 29 PA/AA/DA → `applies_to` vs-01..04 | `referentiel/capacites/cap-int-*.md`, `referentiel/principes/p-int-*.md`, `referentiel/principes/{pa,aa,da}-*.md`, `referentiel/fondations/f-4.md` |
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

Croisement de `03_ptisn/02_topologie-nationale-cible.md` (Partie II) avec `02_artsn/04_cartographie-cible.md` (l'architecture conceptuelle de l'ARTSN : 6 couches horizontales + 2 axes verticaux).

### 9.1 Correspondance couche à couche

| Topologie PTISN (p.II) | Cartographie ARTSN | Verdict |
|-------------------------|--------------------|---------|
| Applications et systèmes du secteur santé | **Couche 2 — Point de service** (F.1, ENF-1) | ✓ conforme (PTISN plus large, ARTSN focalisé logiciel terrain) |
| Couche de médiation sectorielle (normalisation, routage, orchestration légère) | **Couche 3** (échange/transport, ART-1, F.3) **+ Couche 4** (médiation ART-2, orchestration ART-8a) | ⚠ conflation de 2 couches ARTSN |
| Services et registres nationaux de santé | **Couche 4** — registres (ART-4, INP ART-4a, éligibilité ART-4c, terminologies, personnels) | ✓ conforme |
| Services analytiques et de restitution | **Couche 5** — projections analytiques (ART-6, Lakehouse, ART-8b/ART-9) | ✓ conforme (position verticale différente, cf. 9.3) |
| Point d'échange sectoriel sécurisé | **Couche 3** — API Gateway / broker (ART-1) | ✓ conforme (collision de nom, cf. 9.3) |
| Plateforme nationale d'échange interinstitutionnel (X-Road) | **Aucun composant/couche explicite** | ✗ écart majeur |
| Institutions et registres d'autres secteurs | Couche 6 (intersectoriel) + Axe 2 (ART-0, accords de partage) | ◐ partiel (conventionnel, pas technique) |
| *(absent)* | **Couche 6 — Pilotage / gouvernance** | ✗ absent de la topologie PTISN |
| *(absent en transversal)* | **Axe 1 — Sécurité et confiance** · **Axe 2 — Gouvernance de données** | ◐ implicite, jamais rendu transversal |

### 9.2 Points de cohérence confirmés ✓

- **Médiation** : normalisation ↔ ART-2 ; routage/ingestion ↔ ART-1/Couche 3 ; orchestration ↔ ART-8a/Couche 4. `03_ptisn/08_annexes/a-synthese-choix.md` (OpenHIM = contrats ART-1/ART-2) confirme.
- **Séparation des responsabilités** (p.II §2.3 « la couche d'échange ne remplace pas ces responsabilités ») ↔ Couche 3 ARTSN explicitement « dépourvue de toute logique ou intelligence métier ».
- **X-Road / auth utilisateur final** : « le SI connecté reste responsable de l'authentification de l'utilisateur final et du contrôle d'accès métier » ↔ Couche 3 sans logique métier + Axe 1 (authentification à la périphérie).
- **Consentement / base d'autorisation** (p.II §2.3) ↔ Axe 1 (gestion des consentements), ART-4b, PT-11.
- **Règle « les échanges internes ne transitent pas par la plateforme interinstitutionnelle »** ↔ ARTSN où l'interop sectorielle est portée par la Couche 4 directement.
- **Autorité sur les données** (p.II §2.3) ↔ Axe 2 (gouvernance) + Couche 4 (source de vérité au présent).
- **CNISN agnostique** (« aucune plateforme particulière », `01_cnisn/00_introduction.md:37`) : le choix X-Road relève bien du PTISN — pas de contradiction.

### 9.3 Écarts identifiés (ouverts)

1. ~~**X-Road absent de la cartographie ARTSN**~~ — **✓ Résolu** : X-Road placé en Couche 3 (§9.3.1).
2. ~~**Couche 6 (pilotage/gouvernance) absente de la topologie PTISN**~~ — **✓ Résolu** : diagramme PTISN réécrit avec les 6 couches ARTSN + 2 axes transversaux (2026-08-18).
3. ~~**Médiation conflation couches 3+4**~~ — **✓ Résolu** : orchestration déplacée vers Couche 4 (ART-8a) dans le PTISN ; Couche 3 explicitement « dépourvue de toute logique métier » (2026-08-18).
4. ~~**Collision « Point »**~~ — **✓ Résolu** : « Point de service » (Couche 2) et « Point d'échange » (Couche 3, API Gateway) clairement distingués (2026-08-18).
5. ~~**Analytique au même niveau que les registres**~~ — **✓ Résolu** : Couche 5 (projections) séparée de la Couche 4 (registres) (2026-08-18).
6. ~~**Résilience offline** (F.1/ENF-1) non évoquée dans la topologie PTISN~~ — **✓ Résolu** : §2.3 ajouté décrivant capture 100% locale, journaux inaltérables, synchronisation asynchrone (2026-08-18).

### 9.4 Recommandations (ouvertes — voir §7.6)

1. ~~Ancrer X-Road dans la cartographie ARTSN~~ — **✓ Résolu** : X-Road placé en Couche 3 (§9.3.1).
2. ~~Ajouter la couche « pilotage/gouvernance » et les axes sécurité/confiance et gouvernance en transversal dans la topologie PTISN~~ — **✓ Résolu** (2026-08-18).
3. ~~Aligner « orchestration » sur la Couche 4 (rattacher explicitement à ART-8a)~~ — **✓ Résolu** (2026-08-18).
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
| ARTSN → CNISN | Référentiel : chapitres `art-*`, exigences `enf-*`, fondations `f-1..f-4` — **zéro référence** à `cap-int-*`/`p-int-*` ; chapitres ART `maps_to` exclusivement vers CAESN (`cap-13/14/08`) ; wrapper ARTSN cite CNISN seulement en navigation | ✗ **absente** |

- `referentiel/capacites/cap-int-*.md` : `related: []` (aucun lien vers ART) ; leurs `maps_to` pointent vers `p-int-*` **et vers `cap-XX`** (CAESN, correspondance niveau 1 ↔ 2, depuis 2026-08-11).
- Seules les fondations candidates `f-5`/`f-6` citent P-INT (en prose).
- → Traçabilité **asymétrique** : le niveau 3 « flotte » par rapport au niveau 2 (précision du §4).

### 10.2 Taxonomie de l'annexe B vs taxonomies CNISN

L'annexe B utilisait une **3ᵉ taxonomie** (12 « domaines ») qui ne correspondait ni aux catégories P-INT (A–F) ni aux 12 CAP-INT : 9 capacités jamais couvertes, catégories P-INT E/F sans ligne, domaines sans équivalent CAP-INT.

**Correctifs appliqués (✓) :** l'annexe B est réécrite sur les **5 familles de réponse** du CNISN (alignées sur les couches 3-5 et les deux axes de la cartographie ARTSN, cf. `01_cnisn/02_capacites.md`). Chaque famille est explicitement rattachée à ses CAP-INT et à ses réponses ART-SN — les **12 capacités sont couvertes**, y compris CAP-INT-12 (conformité, porté par le processus d'homologation Axe 2/F.4/ART-0) et les catégories P-INT E/F (famille 5). L'ancien vocabulaire résiduel (Observabilité, Historisation, Logistique, Protection/minimisation) est remplacé par les réponses architecturales réelles (ART-0..9, ART-4a..4d, ART-8a/8b/8c, F.2..F.5).

### 10.3 Gouvernance et homologation — CNASN absent du CNISN

- **ARTSN** : homologation par le **CNASN** (Comité National d'Architecture Santé Numérique, `02_artsn/acronyms.md`) ; critères — ouverture, alignement normatif, interopérabilité, souveraineté des données, coût total de possession (`06_gouvernance.md`, `referentiel/fondations/f-3.md`).
- **CNISN** : homologation portée par le **comité sectoriel santé** (« organise l'homologation sectorielle », `03_gouvernance.md`) et l'instance sectorielle ; critères `04_conformite.md` §3 (13 critères). **Le CNASN n'apparaît nulle part dans le CNISN** (ni gouvernance, ni conformité, ni hiérarchie `00_introduction.md` §2).
- → **Conflit apparent d'autorité d'homologation** (comité sectoriel CNISN vs CNASN) et **listes de critères divergentes** (13 vs 5 ; chevauchement partiel : coût total de possession, souveraineté≈résidence).

### 10.4 Conformité CNISN ↔ F.4 / CNASN ARTSN — cohérent mais à articuler

- CNISN `04_conformite.md` : profil de conformité (inclut contrats ART + profils PTISN), dossier minimal, 7 statuts, réévaluation. ✓
- ARTSN : F.4 (homologation obligatoire), statuts de chapitres (Stable/Provisoire/Proposition ouverte), écart = dérogation explicite. ✓ Complémentaires (statuts « chapitres » vs « initiatives ») ; friction uniquement sur l'acteur (§10.3).

### 10.5 Traitement de la logistique — divergence CNISN vs ARTSN

**Statut : ✓ Résolu (2026-08-18)**

- ART-10 (Logistique) existe désormais dans l'ARTSN : chapitre complet (`02_artsn/03_chapitres/art-10-logistique.md`), fiche référentiel (`referentiel/chapitres/art-10.md`), listé dans l'index des chapitres (status `candidate`).
- La table de maturité ARTSN (`07_annexes/a-table-de-maturite.md`) intègre désormais ART-10 au statut **Proposition ouverte**, avec pour condition de passage : « Confirmation par une initiative LMIS/logistique déployant la traçabilité de bout en bout des mouvements de stock ».
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

> **NB (2026-08-12) :** les 28 objets décrits ci-dessous sont reclassés en **étapes de valeur** (`referentiel/etapes-valeur/ev-01…28.md`). Les **processus métier** (`referentiel/processus/prc-01…12.md`) les regroupent désormais — voir §12.

**Constat :** le graphe CAESN s'arrêtait aux flux de valeur (VS-01…04) et aux capabilités (CAP-01…16) : ni les étapes de valeur (processus métier), ni les familles de systèmes (composants applicatifs), ni les bénéficiaires (parties prenantes) n'étaient représentés comme objets du référentiel, alors que les tables CAESN les décrivent (`01_value-streams/*.md`, `05_application/application-domains.md`, `05_application/shared-services.md`, `00_overview/value-model.md`).

**Correctif appliqué (✓) — 51 nouveaux objets, ré-ancrage additif :**
- **28 processus métier** (`referentiel/processus/prc-01…28.md`) — un par étape de valeur (7 × 4 flux) : `source:` = enveloppe VS-XX, `applies_to` = capabilités mobilisées, `related` = flux de valeur.
- **13 composants applicatifs** (`referentiel/composants/cmp-01…13.md`) — 11 domaines applicatifs (dont cmp-12 Référentiels nationaux) + 2 services partagés (cmp-13 confiance/interopérabilité) : `applies_to` = processus soutenus, `maps_to` = CAP-INT, `implements` = chapitres ART, `related` = exigences/capabilités/flux.
- **10 parties prenantes** (`referentiel/parties-prenantes/pp-01…10.md`) — `related` = flux de valeur ; les 4 VS gagnent `applies_to` → pp-XX (17 liens).
- Annexe E et traçabilité existantes **intactes** (aucun lien CAESN↔CNISN modifié) : approche strictement additive.
- Enveloppes enrichies : VS-01…04 (+ « Processus métier » en catalogue), `value-model.md` (+ Parties prenantes), `application-domains.md` (+ Composants applicatifs cibles), `shared-services.md` (+ Composants des services partagés). `scripts/build_wrappers.py` supporte désormais un attribut `mode=monographie|mode=catalogue` explicite sur les blocs d'enveloppes mixtes.

**Vérifications (✓) :**
- `make check` : **54 enveloppes à jour**, **0 lien relatif cassé sur 2819** vérifiés.
- `/tmp/validate_ref.rb` : **202 fichiers, 201 objets uniques**, 2 erreurs attendues (`_schema.md`), **0 lien cassé, 0 relation non résolue**.
- `/tmp/trace_check.py` : **197/201 objets tracés depuis les VS** — toutes les nouvelles familles couvertes (28/28 PRC, 13/13 CMP, 10/10 PP) ; seuls les 4 stubs candidats préexistants restent non tracés (art-10, art-11, f-5, f-6).

## 12. Migration étapes de valeur / processus métier (2026-08-12) ✓

**Constat :** les 28 objets créés en §11 sous le type `processus-metier` reproduisaient 1:1 les étapes des tables CAESN : le type était utilisé à contresens (une étape n'est pas un processus) et les 13 composants pointaient vers des maillons isolés.

**Correctif appliqué (✓) — reclassement + couche de régroupement :**
- **28 étapes de valeur** (`referentiel/etapes-valeur/ev-01…28.md`) — reclassement formel des ex-`prc-01…28` (id/type/title/tags, corps inchangé) ; `source:` = enveloppe VS-XX, `applies_to` granulaire conservé, `related` = flux.
- **12 processus métier** (`referentiel/processus/prc-01…12.md`) — 3 par flux de valeur (VS-01…04), contenus **strictement dérivés** des étapes (Objectif de synthèse, Étapes couvertes, Acteurs et Indicateurs = unions) ; `applies_to` = héritage intégral de la VS, `related` = étapes couvertes + flux.
- **13 composants** réaffectés au niveau processus (`applies_to` : étapes → processus couvrants, transformation mécanique depuis le découpage) — un composant soutient désormais des processus complets.
- **Enveloppes** VS-01…04 : deux blocs catalogue distincts « Étapes de valeur » et « Processus métier ».
- Traçabilité CAESN↔CNISN **intacte** ; aucun changement de `build_wrappers.py` ni de `manifest.json`.

**Vérifications (✓) :**
- `make check` : 54 enveloppes à jour, 0 lien relatif cassé.
- `validate_ref.rb` : 214 fichiers, 214 objets uniques, 2 erreurs méta connues (`_schema.md`), 0 lien cassé, 0 relation non résolue.
- `trace_check.py` : 209/213 objets tracés (les 12 processus via `related` → ev → vs → capabilités ; seuls les 4 stubs préexistants art-10, art-11, f-5, f-6 restent non tracés).

## 13. Restructuration CMP : 13 composants → 18 composants cartographie-cible (2026-08-13) ✓

**Constat :** les 13 composants applicatifs (`cmp-01…13`) ne couvraient pas fidèlement les « Composants associés » définis dans la cartographie conceptuelle cible (`02_artsn/04_cartographie-cible.md`). La cartographie définit 6 couches horizontales + 2 axes verticaux, chacun avec des composants spécifiques qui nécessitent un mapping un à un.

**Correctif appliqué (✓) — 18 CMPs applicatifs :**
- **18 composants applicatifs** (`referentiel/composants/cmp-01…18.md`) — mappés aux « Composants associés » de la cartographie-cible :
  - Couche 6 (Pilotage) : CMP-01 (tableaux de bord), CMP-02 (centre de commande)
  - Couche 5 (Projections) : CMP-03 (entrepôt Lakehouse), CMP-04 (moteur analytique & IA), CMP-05 (moteur de graphes)
  - Couche 4 (Interopérabilité) : CMP-06 (intégration/médiation), CMP-07 (orchestrateur de parcours), CMP-08 (répertoire clinique), CMP-09 (méta-données), CMP-10 (terminologies), CMP-11 (INP), CMP-12 (éligibilité/CSU), CMP-13 (personnels), CMP-14 (produits/intrants)
  - Couche 3 (Échange) : CMP-15 (API Gateway), CMP-16 (registre schémas), CMP-17 (message broker), CMP-18 (compensateur)
- **12 processus** (`prc-04…12`) mis à jour : `applies_to` enrichi avec les CMPs soutenus.
- **13 profils PTISN** (`pt-01…13`) mis à jour : `applies_to` enrichi avec les CMPs implémentés.
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
| ART-1 | [`cap-int-03`] | Échange et médiation inter-systèmes |
| ART-2 | [`cap-int-03`] | Échange et médiation inter-systèmes |
| ART-3 | [`cap-int-03`] | Échange et médiation inter-systèmes |
| ART-4 | [`cap-int-03`] | Échange et médiation inter-systèmes |
| ART-4a | [`cap-int-01`] | Résolution d'identité |
| ART-4b | [`cap-int-05`] | Données agrégées |
| ART-4c | [`cap-int-07`] | Éligibilité couverture |
| ART-4d | [] | — |
| ART-5 | [`cap-int-03`] | Échange et médiation inter-systèmes |
| ART-6 | [`cap-int-05`] | Données agrégées |
| ART-7 | [`cap-int-06`] | Sécurité et chiffrement |
| ART-8 | [`cap-int-03`] | Échange et médiation inter-systèmes |
| ART-8a | [`cap-int-03`] | Échange et médiation inter-systèmes |
| ART-8b | [`cap-int-03`] | Échange et médiation inter-systèmes |
| ART-8c | [`cap-int-03`] | Échange et médiation inter-systèmes |
| ART-8d | [`cap-int-03`] | Échange et médiation inter-systèmes |
| ART-9 | [`cap-int-07`] | Éligibilité couverture |
| ART-10 | [`cap-int-10`] | Audit et traçabilité |
| ART-11 | [`cap-int-13`, `cap-int-14`] | Interopérabilité transfrontalière, Échanges intersectoriels One Health |

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
6. **OpenFn** : candidate alternative ajoutée dans PT-02 ; à évaluer pour d'autres profils si pertinent

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

### 15.4 OpenFn ajouté comme candidate alternative

**Statut : ✓ Résolu**

OpenFn (plateforme d'intégration open-source orientée workflow) ajouté comme candidate alternative dans `03_ptisn/03_profils/pt-02-mediation-intra-secteur.md` :
- Table « Produit candidat » : row `Alternatives` enrichie
- Description ajoutée sous le paragraphe OpenHIM (connecteurs HL7 FHIR, DHIS2, moteur de règles métier)

### 15.5 Vérification finale

- **Liens cassés** : 0 (script Python, tous les fichiers `.md` du cadre)
- **JSON valide** : `python3 -c "import json; json.load(open('mintlify-site/docs.json'))"` → OK
- **Pages navigation** : 160 pages, toutes existent sur disque
