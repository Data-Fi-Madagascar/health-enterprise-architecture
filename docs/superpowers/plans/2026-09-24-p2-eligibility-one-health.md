# P2 Eligibility and One Health Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Introduire un ABB et un profil PTISN dédiés à l'éligibilité, puis rendre complète et vérifiable la traçabilité One Health vers VS-02 et VS-04.

**Architecture:** `04_architecture-repository` demeure la source canonique. Les nouvelles relations sont d'abord protégées par des tests sémantiques, puis propagées par les générateurs existants vers les enveloppes CAESN/ARTSN/PTISN, la vue TOGAF, OpenAPI et Mintlify.

**Tech Stack:** Markdown avec frontmatter YAML, Python 3.12 `unittest`, générateurs HEA, FHIR R4, OpenAPI 3.0.3, Make.

**Spec:** `docs/superpowers/specs/2026-09-24-p2-eligibility-one-health-design.md`

## Global Constraints

- Conserver `04_architecture-repository` comme source canonique.
- Utiliser uniquement les statuts `draft|active|stable|candidate|deprecated`.
- Ne jamais committer `graphify-out/` ni `.obsidian/`.
- Régénérer les enveloppes après toute modification d'une source canonique.
- Les nouvelles décisions sont `ADR-0011` et `ADR-0012` ; elles restent `candidate`.
- `ABB-ELIGIBILITE-COUVERTURE` et `PT-20` restent `candidate`.
- Ne sélectionner aucun produit logiciel et ne créer aucun nouveau flux de valeur ou nouvelle capacité.
- Valider chaque tâche avant de la committer ; terminer par `make check` et une PR sans merge automatique.

---

### Task 1: Bloquer les partitions dont un flux déclaré n'a aucune capacité commune

**Files:**
- Modify: `scripts/validate_ref.py`
- Modify: `tests/test_validate_ref.py`

**Interfaces:**
- Consumes: graphe `objects` produit par `load_relation_graph()`, avec `type` et `relations` par objet.
- Produces: `check_partition_value_stream_coverage(objects) -> list[tuple[file, partition_id, value_stream_id, message]]`. Task 4 l'intègre dans `main()` au même commit que la correction One Health, afin de ne pas laisser la branche volontairement rouge entre deux lots.

- [ ] **Step 1: Écrire les tests en échec**

Ajouter à `tests/test_validate_ref.py` :

```python
class PartitionValueStreamCoverageTests(unittest.TestCase):
    def setUp(self):
        self.validator = load_validator()

    def graph(self, partition_caps):
        return {
            "PART-ONE-HEALTH": {
                "id": "PART-ONE-HEALTH",
                "file": "/tmp/part-one-health.md",
                "type": "architecture-partition",
                "relations": {
                    "applies_to": set(partition_caps) | {"VS-02", "VS-04"},
                },
            },
            "VS-02": {
                "id": "VS-02", "file": "/tmp/vs-02.md", "type": "flux-valeur",
                "relations": {"applies_to": {"CAP-18"}},
            },
            "VS-04": {
                "id": "VS-04", "file": "/tmp/vs-04.md", "type": "flux-valeur",
                "relations": {"applies_to": {"CAP-08"}},
            },
            "CAP-08": {"id": "CAP-08", "file": "/tmp/cap-08.md", "type": "capabilite", "relations": {}},
            "CAP-18": {"id": "CAP-18", "file": "/tmp/cap-18.md", "type": "capabilite", "relations": {}},
        }

    def test_rejects_explicit_value_stream_without_common_capability(self):
        errors = self.validator.check_partition_value_stream_coverage(
            self.graph({"CAP-18"})
        )
        self.assertEqual(["VS-04"], [error[2] for error in errors])

    def test_accepts_each_explicit_value_stream_with_common_capability(self):
        errors = self.validator.check_partition_value_stream_coverage(
            self.graph({"CAP-08", "CAP-18"})
        )
        self.assertEqual([], errors)
```

- [ ] **Step 2: Vérifier l'échec**

Run: `python3 -m unittest tests.test_validate_ref.PartitionValueStreamCoverageTests -v`

Expected: FAIL avec `AttributeError: module 'validate_ref' has no attribute 'check_partition_value_stream_coverage'`.

- [ ] **Step 3: Implémenter le contrôle minimal**

Dans `scripts/validate_ref.py`, ajouter une fonction qui :

1. sélectionne les objets `architecture-partition` ;
2. extrait les cibles `flux-valeur` et `capabilite` de `applies_to` et `related` ;
3. ajoute aux capacités de la partition celles des ABB dont `partitions` contient l'identifiant de la partition ;
4. compare ces capacités aux capacités `applies_to`/`related` de chaque flux explicitement déclaré ;
5. retourne une erreur lorsqu'aucune capacité n'est commune ;
6. ignore les partitions sans capacité directe ou dérivée, afin que les partitions purement structurelles `PART-VS-*` restent valides.

Ne pas encore l'intégrer dans `main()` : le référentiel courant contient précisément le gap One Health que la fonction doit détecter. L'intégration bloquante est atomique avec la correction dans Task 4.

- [ ] **Step 4: Vérifier le test et le référentiel courant**

Run: `python3 -m unittest tests.test_validate_ref.PartitionValueStreamCoverageTests -v`

Expected: PASS pour les deux tests.

Run: `python3 scripts/validate_ref.py`

Expected: `Résumé : CONFORME`, car le nouveau contrôle n'est pas encore branché dans `main()`.

- [ ] **Step 5: Committer le garde-fou**

```bash
git add scripts/validate_ref.py tests/test_validate_ref.py
git commit -m "test: enforce partition value-stream coverage"
```

---

### Task 2: Créer l'ABB d'éligibilité et corriger les relations héritées

**Files:**
- Create: `04_architecture-repository/05_building-blocks/abb/abb-eligibilite-couverture.md`
- Create: `01_cnisn/06_decisions/adr-0011-eligibilite-couverture.md`
- Modify: `04_architecture-repository/05_building-blocks/abb/legacy-components/cmp-12.md`
- Modify: `04_architecture-repository/05_building-blocks/abb/abb-registre-professionnels.md`
- Modify: `04_architecture-repository/05_building-blocks/sbb/legacy-profiles/pt-05.md`
- Modify: `04_architecture-repository/05_building-blocks/sbb/legacy-profiles/pt-11.md`
- Modify: `04_architecture-repository/07_migration/work-packages/wp-03.md`
- Modify: `04_architecture-repository/02_architecture-elements/data/data-objects/do-14.md`
- Modify: `04_architecture-repository/02_architecture-elements/data/data-objects/do-15.md`
- Modify: `04_architecture-repository/02_architecture-elements/data/data-objects/do-16.md`
- Modify: `04_architecture-repository/02_architecture-elements/data/data-objects/do-17.md`
- Modify: `tests/test_validate_ref.py`

**Interfaces:**
- Consumes: `CAP-07`, `PART-VS-03`, `ART-4C`, `ART-9`, `PRC-09`, `PRC-10`, `DO-14..DO-17`.
- Produces: objet canonique `ABB-ELIGIBILITE-COUVERTURE` et décision `ADR-0011` ; Task 3 rattache PT-20 à cet ABB.

- [ ] **Step 1: Mettre les attentes sémantiques en échec**

Dans `CanonicalMappingTests.test_legacy_components_map_to_semantically_matching_targets`, remplacer l'attente de CMP-12 par `{"ABB-ELIGIBILITE-COUVERTURE"}`.

Ajouter :

```python
def test_eligibility_is_separate_from_identity_and_consent(self):
    abb = Path("04_architecture-repository/05_building-blocks/abb/abb-eligibilite-couverture.md")
    self.assertEqual({"CAP-07"}, self.relation_values(abb, "maps_to"))
    self.assertEqual({"PART-VS-03"}, self.relation_values(abb, "partitions"))
    self.assertEqual({"ART-4C", "ART-9"}, self.relation_values(abb, "implements"))
    self.assertEqual(
        {"DO-14", "DO-15", "DO-16", "DO-17"},
        self.relation_values(abb, "accesses"),
    )

    professionals = Path("04_architecture-repository/05_building-blocks/abb/abb-registre-professionnels.md")
    pt05 = Path("04_architecture-repository/05_building-blocks/sbb/legacy-profiles/pt-05.md")
    pt11 = Path("04_architecture-repository/05_building-blocks/sbb/legacy-profiles/pt-11.md")
    self.assertNotIn("ART-4C", self.relation_values(professionals, "implements"))
    self.assertNotIn("ART-4C", self.relation_values(pt05, "implements"))
    self.assertNotIn("CMP-12", self.relation_values(pt11, "applies_to"))
```

- [ ] **Step 2: Vérifier l'échec**

Run: `python3 -m unittest tests.test_validate_ref.CanonicalMappingTests -v`

Expected: FAIL parce que l'ABB n'existe pas et CMP-12 pointe encore vers `CAP-07`.

- [ ] **Step 3: Créer l'ABB canonique**

Créer `abb-eligibilite-couverture.md` avec :

```yaml
id: ABB-ELIGIBILITE-COUVERTURE
type: architecture-building-block
status: candidate
building_block_role: ABB
building_block_domain: application
togaf_repository_section: reference-library
togaf_adm_phase: C
architecture_level: enterprise
architecture_domain: application
architecture_scope: financial-protection
architecture_state: target
partitions: ["PART-VS-03"]
maps_to: ["CAP-07"]
implements: ["ART-4C", "ART-9"]
accesses: ["DO-14", "DO-15", "DO-16", "DO-17"]
related: ["PART-VS-03", "PRC-09", "PRC-10"]
```

Le corps doit décrire les services de consultation de couverture, vérification des droits, décision temporelle, preuve et audit, ainsi que la séparation explicite d'avec l'identité et le consentement.

- [ ] **Step 4: Corriger les relations canoniques et inverses**

- CMP-12 : `maps_to: ["ABB-ELIGIBILITE-COUVERTURE"]`, conserver `implements: ["ART-4C"]` et expliquer la réalisation de l'ABB.
- `ABB-REGISTRE-PROFESSIONNELS` et PT-05 : retirer `ART-4C` de `implements` et du corps.
- PT-11 : remplacer `applies_to: ["CMP-12"]` par `applies_to: []`.
- WP-03 : ajouter l'ABB à `realizes`, `related` et au texte des objectifs.
- DO-14..DO-17 : ajouter `ABB-ELIGIBILITE-COUVERTURE` à `related` pour assurer le lien inverse sans introduire une nouvelle clé de relation.

- [ ] **Step 5: Rédiger ADR-0011**

Créer une ADR conforme au template avec `id: adr-0011`, statut `candidate`, et les sections obligatoires. La décision doit imposer : ABB distinct, séparation identité/consentement, FHIR R4, traçabilité temporelle et absence de choix produit.

- [ ] **Step 6: Régénérer les index et enveloppes affectés**

Run:

```bash
python3 scripts/build_adr_index.py
python3 scripts/build_wrappers.py
python3 scripts/build_ref_index.py
```

Expected: ADR-0011 apparaît dans l'index et le registre ; les enveloppes reflètent le nouvel ABB et les relations corrigées ; `_index.yaml` contient `ABB-ELIGIBILITE-COUVERTURE`.

- [ ] **Step 7: Valider le lot éligibilité**

Run: `python3 -m unittest tests.test_validate_ref.CanonicalMappingTests -v`

Expected: PASS.

Run: `python3 scripts/validate_adr.py --check`

Expected: `TOUT EST CONFORME` avec 11 ADR.

Run: `python3 scripts/build_wrappers.py --check && python3 scripts/build_ref_index.py --check`

Expected: enveloppes et index à jour.

- [ ] **Step 8: Committer l'ABB et la décision**

```bash
git add 00_caesn 01_cnisn 02_artsn 03_ptisn 04_architecture-repository tests/test_validate_ref.py
git commit -m "feat: model eligibility coverage building block"
```

---

### Task 3: Ajouter PT-20 et son contrat OpenAPI

**Files:**
- Create: `04_architecture-repository/05_building-blocks/sbb/legacy-profiles/pt-20.md`
- Create: `03_ptisn/03_profils/pt-20-eligibilite-couverture.md`
- Create: `03_ptisn/schemas/openapi/pt-20.json` (généré)
- Modify: `scripts/compilers/compile_openapi.py`
- Create: `tests/test_compile_openapi.py`
- Modify: `tests/test_validate_ref.py`
- Modify: `scripts/manifest.json`
- Modify: `03_ptisn/index.md`
- Modify: `03_ptisn/reading-guide.md`
- Modify: `03_ptisn/reading-matrix.md`
- Modify: `03_ptisn/glossary.md`
- Modify: `03_ptisn/04_matrice-alignement/index.md`

**Interfaces:**
- Consumes: `ABB-ELIGIBILITE-COUVERTURE`, CMP-12, ART-4C, ART-9 et les ressources FHIR R4.
- Produces: profil canonique `PT-20`, enveloppe publiée et OpenAPI `pt-20.json`.

- [ ] **Step 1: Écrire les tests OpenAPI et de mapping en échec**

Créer `tests/test_compile_openapi.py` :

```python
import unittest
from scripts.compilers import compile_openapi


class EligibilityOpenApiTests(unittest.TestCase):
    def test_discovers_all_pt20_fhir_resources(self):
        text = (
            "FHIR R4 Coverage, CoverageEligibilityRequest, "
            "CoverageEligibilityResponse et InsurancePlan"
        )
        self.assertEqual(
            ["Coverage", "CoverageEligibilityRequest", "CoverageEligibilityResponse", "InsurancePlan"],
            compile_openapi.find_fhir_resources(text),
        )


if __name__ == "__main__":
    unittest.main()
```

Ajouter dans `CanonicalMappingTests` un test qui exige :

```python
pt20 = Path("04_architecture-repository/05_building-blocks/sbb/legacy-profiles/pt-20.md")
self.assertEqual(
    {"ABB-ELIGIBILITE-COUVERTURE", "CAP-07"},
    self.relation_values(pt20, "maps_to"),
)
self.assertEqual({"CMP-12"}, self.relation_values(pt20, "applies_to"))
self.assertEqual({"ART-4C", "ART-9"}, self.relation_values(pt20, "implements"))
```

- [ ] **Step 2: Vérifier les échecs**

Run: `python3 -m unittest tests.test_compile_openapi tests.test_validate_ref.CanonicalMappingTests -v`

Expected: FAIL parce que `Coverage` et `InsurancePlan` ne sont pas découverts et que PT-20 n'existe pas.

- [ ] **Step 3: Étendre le compilateur générique**

Dans `FHIR_RESOURCES`, ajouter `Coverage` et `InsurancePlan`. Dans `SERVER_BY_PROFILE`, ajouter :

```python
"PT-20": (
    "https://coverage.health.mg/fhir",
    "Registre national d'éligibilité et de couverture",
),
```

Mettre à jour les docstrings qui annoncent 19 profils afin qu'elles parlent du catalogue de profils sans nombre codé en dur.

- [ ] **Step 4: Créer la source canonique PT-20**

Le frontmatter doit contenir :

```yaml
id: PT-20
type: profil
status: candidate
envelope: 03_ptisn/03_profils/pt-20-eligibilite-couverture.md
maps_to: ["ABB-ELIGIBILITE-COUVERTURE", "CAP-07"]
implements: ["ART-4C", "ART-9"]
applies_to: ["CMP-12"]
related: ["DO-14", "DO-15", "DO-16", "DO-17"]
```

La section Transactions doit contenir exactement :

| Transaction | Acteurs | R/O | Standard |
|---|---|---|---|
| T1 — Consultation d'une couverture | Application métier → Registre d'éligibilité | R | FHIR R4 `Coverage` search |
| T2 — Demande de vérification des droits | Application métier → Registre d'éligibilité | R | FHIR R4 `CoverageEligibilityRequest` |
| T3 — Réponse d'éligibilité | Registre d'éligibilité → Application métier | R | FHIR R4 `CoverageEligibilityResponse` |
| T4 — Consultation d'un régime de couverture | Application métier → Registre d'éligibilité | O | FHIR R4 `InsurancePlan` search |

Décrire acteurs, content modules, options, exigences de sécurité/audit, SLA, déclaration de conformité et dépendances PT-04/PT-10/PT-12, sans choisir de produit.

- [ ] **Step 5: Créer l'enveloppe et enregistrer la page**

Créer l'enveloppe PTISN avec frontmatter public et un bloc vide `BEGIN:GENERATED`/`END:GENERATED`. Ajouter son chemin après PT-19 dans `scripts/manifest.json`. Mettre à jour les mentions `PT-01…PT-19`, le guide de lecture, la matrice de lecture, le glossaire et la matrice ART-4C/L3 pour inclure PT-20.

- [ ] **Step 6: Générer et valider PT-20**

Run: `python3 scripts/build_wrappers.py --only 03_ptisn/03_profils/pt-20-eligibilite-couverture.md`

Expected: `1 enveloppes écrites`.

Run: `python3 scripts/build_wrappers.py && python3 scripts/build_ref_index.py`

Expected: 114 enveloppes écrites et index du repository régénéré avec PT-20.

Run: `python3 scripts/compilers/compile_openapi.py`

Expected: 20 spécifications générées, dont `pt-20.json` avec les quatre ressources FHIR.

Run: `python3 -m unittest tests.test_compile_openapi tests.test_validate_ref.CanonicalMappingTests -v`

Expected: PASS.

Run: `python3 scripts/compilers/compile_openapi.py --check`

Expected: `[OK] 20 spécifications OpenAPI à jour.`

Run: `python3 scripts/build_wrappers.py --check && python3 scripts/check_manifests.py`

Expected: 114 enveloppes à jour et manifestes valides.

- [ ] **Step 7: Committer PT-20**

```bash
git add 00_caesn 01_cnisn 02_artsn 03_ptisn 04_architecture-repository scripts/compilers/compile_openapi.py scripts/manifest.json tests
git commit -m "feat: add eligibility coverage profile PT-20"
```

---

### Task 4: Compléter la chaîne One Health vers VS-02 et VS-04

**Files:**
- Create: `01_cnisn/06_decisions/adr-0012-one-health-pilotage.md`
- Modify: `04_architecture-repository/01_partitions/sectorielles/part-one-health.md`
- Modify: `04_architecture-repository/05_building-blocks/abb/abb-echange-mediation.md`
- Modify: `04_architecture-repository/05_building-blocks/abb/abb-exposition-donnees-analytiques.md`
- Modify: `04_architecture-repository/05_building-blocks/sbb/legacy-profiles/pt-15.md`
- Modify: `04_architecture-repository/07_migration/work-packages/wp-07.md`
- Modify: `tests/test_validate_ref.py`
- Modify: `tests/test_partition_view.py`

**Interfaces:**
- Consumes: garde-fou de Task 1 et vue `render_partition_traceability()` existante.
- Produces: deux chaînes One Health complètes et dérivables, protégées par tests.

- [ ] **Step 1: Écrire les tests sémantiques en échec**

Ajouter à `CanonicalMappingTests` :

```python
def test_one_health_covers_surveillance_and_governance(self):
    partition = Path("04_architecture-repository/01_partitions/sectorielles/part-one-health.md")
    self.assertEqual(
        {"CAP-08", "CAP-18", "VS-02", "VS-04"},
        self.relation_values(partition, "applies_to"),
    )
    pt15 = Path("04_architecture-repository/05_building-blocks/sbb/legacy-profiles/pt-15.md")
    self.assertTrue(
        {"ABB-ECHANGE-MEDIATION", "ABB-EXPOSITION-DONNEES-ANALYTIQUES", "CAP-05", "CAP-08", "CAP-18"}
        <= self.relation_values(pt15, "maps_to")
    )
```

Ajouter à `PartitionTraceabilityViewTests` un test qui charge les objets réels avec `builder.load_objects()`, rend la vue, sélectionne les lignes commençant par `| PART-ONE-HEALTH |`, puis exige deux lignes : l'une avec `VS-02`, l'autre avec `VS-04`; aucune ne doit contenir `| n/a |` dans CAP ou PRC, et toutes doivent contenir les ABB attendus et `PT-15`.

- [ ] **Step 2: Vérifier les échecs**

Run: `python3 -m unittest tests.test_validate_ref.CanonicalMappingTests tests.test_partition_view.PartitionTraceabilityViewTests -v`

Expected: FAIL sur l'absence de CAP-08 et des rattachements ABB de PT-15.

- [ ] **Step 3: Corriger la partition et les ABB**

- `PART-ONE-HEALTH.applies_to`: `CAP-08`, `CAP-18`, `VS-02`, `VS-04`.
- Ajouter `PART-ONE-HEALTH` à `partitions` et `related` de `ABB-ECHANGE-MEDIATION`.
- Ajouter `PART-ONE-HEALTH` à `partitions` et `related` de `ABB-EXPOSITION-DONNEES-ANALYTIQUES`.

Ne retirer aucune partition transverse existante : `partitions` est une liste multi-valuée.

Dans `scripts/validate_ref.py`, intégrer maintenant `check_partition_value_stream_coverage()` dans `main()` immédiatement après `check_partition_relation_types()` et mettre `ok = False` lorsqu'une erreur est retournée.

- [ ] **Step 4: Réaligner PT-15 et WP-07**

- PT-15 : ajouter les deux ABB et `CAP-08` à `maps_to`; conserver `CAP-05`, `CAP-18`, la partition et les composants réellement utilisés.
- WP-07 : remplacer `CAP-03` par `CAP-08` et `CAP-18`, ajouter PT-15 et les deux ABB à `realizes`/`related`, et corriger le texte des objectifs.
- Conserver CMP-02, CMP-04 et CMP-06 comme composants de solution du profil.

- [ ] **Step 5: Rédiger ADR-0012**

L'ADR doit expliquer pourquoi VS-04 est conservé : gouvernance intersectorielle CAP-08, centre de commande CMP-02, pilotage et redevabilité. Elle doit explicitement rejeter la création d'un nouveau flux One Health et préserver VS-02 pour la surveillance/riposte.

- [ ] **Step 6: Régénérer ADR, enveloppes et vues**

Run:

```bash
python3 scripts/build_adr_index.py
python3 scripts/build_wrappers.py
python3 scripts/build_ref_index.py
```

Expected: ADR-0012 est indexée, les enveloppes sont à jour et les deux lignes One Health de la vue dérivée contiennent des CAP et PRC.

- [ ] **Step 7: Valider One Health**

Run: `python3 -m unittest tests.test_validate_ref tests.test_partition_view -v`

Expected: PASS.

Run: `python3 scripts/validate_ref.py`

Expected: `Résumé : CONFORME`, notamment pour la couverture des flux de partition.

Run: `python3 scripts/validate_adr.py --check && python3 scripts/build_wrappers.py --check`

Expected: 12 ADR conformes et 114 enveloppes à jour.

- [ ] **Step 8: Committer One Health**

```bash
git add 01_cnisn 00_caesn 02_artsn 03_ptisn 04_architecture-repository scripts/validate_ref.py tests
git commit -m "feat: complete One Health partition traceability"
```

---

### Task 5: Régénérer tous les artefacts et obtenir le pipeline vert

**Files:**
- Modify: `01_cnisn/06_decisions/index.md` (généré)
- Modify: `01_cnisn/06_decisions/registre-decisions.md` (généré)
- Modify: `01_cnisn/06_decisions/adr-change-log.md`
- Modify: `04_architecture-repository/_index.yaml` (généré)
- Modify: enveloppes CAESN/ARTSN/PTISN affectées (générées)
- Modify: `04_architecture-repository/08_views/togaf/partition-traceability.md` (généré)
- Modify: `03_ptisn/03_profils/pt-00-index.md` (généré)
- Modify: `mintlify-site/**` (généré)

**Interfaces:**
- Consumes: toutes les sources canoniques des Tasks 1 à 4.
- Produces: branche P2 entièrement synchronisée et prête pour PR.

- [ ] **Step 1: Documenter les deux décisions dans le journal ADR**

Ajouter deux entrées datées du 2026-09-24 dans `adr-change-log.md`, avec le statut `candidate` et un résumé des décisions ADR-0011 et ADR-0012.

- [ ] **Step 2: Régénérer dans l'ordre**

Run:

```bash
python3 scripts/build_adr_index.py
python3 scripts/build_wrappers.py
python3 scripts/build_ref_index.py
python3 scripts/compilers/compile_openapi.py
python3 scripts/build_mintlify.py
```

Expected: 114 enveloppes écrites, 20 OpenAPI générés et artefact Mintlify généré. Si le nombre d'enveloppes diffère, vérifier que PT-20 est l'unique nouvelle enveloppe avant de poursuivre.

- [ ] **Step 3: Contrôler la vue dérivée**

Run: `rg '^\| PART-ONE-HEALTH|^\| PART-VS-03' 04_architecture-repository/08_views/togaf/partition-traceability.md`

Expected:

- deux lignes One Health, VS-02 et VS-04, sans CAP/PRC `n/a` ;
- `ABB-ECHANGE-MEDIATION`, `ABB-EXPOSITION-DONNEES-ANALYTIQUES` et PT-15 ;
- la ligne PART-VS-03 contient `ABB-ELIGIBILITE-COUVERTURE` et PT-20.

- [ ] **Step 4: Exécuter toutes les validations à froid**

Run: `python3 -m unittest discover -s tests -v`

Expected: tous les tests PASS.

Run: `make check`

Expected: toutes les étapes vertes ; Graphify peut seulement être `SKIP` si `graphify-out/graph.json` est absent.

Run: `git diff --check && git status --short`

Expected: aucune erreur d'espaces ; aucun fichier sous `graphify-out/` ou `.obsidian/`.

- [ ] **Step 5: Committer les artefacts dérivés**

```bash
git add 00_caesn 01_cnisn 02_artsn 03_ptisn 04_architecture-repository mintlify-site scripts/manifest.json
git commit -m "docs: regenerate P2 architecture artifacts"
```

- [ ] **Step 6: Vérification finale et PR**

Run:

```bash
python3 -m unittest discover -s tests -v
make check
git diff --check
git status --short
git log --oneline origin/main..HEAD
```

Expected: branche propre et validations vertes.

Pousser `codex/p2-eligibility-one-health`, ouvrir une PR vers `main` sans merger, puis documenter dans la PR :

- ADR-0011 et la chaîne `CAP-07 → ABB → PT-20 → CMP-12` ;
- ADR-0012 et les deux chaînes One Health ;
- les relations héritées supprimées ;
- le résultat des tests et de `make check` ;
- l'absence de choix produit et les règles métier de couverture laissées hors périmètre.
