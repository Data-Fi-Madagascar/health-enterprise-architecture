# P3.1 Gap Governance Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. This plan is intentionally sequential and must not use subagents.

**Goal:** Make every migration gap a governed, testable closure path from the current plateau to a target plateau, through work packages and explicit evidence.

**Architecture:** `04_architecture-repository` remains the canonical source. Gap lifecycle metadata and `EVID-*` objects are authored there; validators enforce their semantics; builders derive the repository roadmap and refresh existing published envelopes without duplicating architectural objects.

**Tech Stack:** Markdown/YAML frontmatter, Python 3 standard library, `unittest`, Make.

**Spec:** `docs/superpowers/specs/2026-09-29-p3-1-gap-governance-design.md`

## Global constraints

- Execute locally and sequentially; do not use subagents.
- Preserve the controlled object status vocabulary: `draft|active|stable|candidate|deprecated`.
- Use the separate controlled gap lifecycle: `identified|planned|in-remediation|closed|accepted-risk`.
- Keep dates in work packages only; gaps reference plateaux and work packages.
- Do not create new products, capabilities, value streams, or duplicate architecture objects.
- Start closure evidence as `candidate` until independently accepted.
- After changing `referentiel/`, regenerate wrappers; after any canonical change, regenerate all impacted derived artifacts.
- Never commit `graphify-out/` or `.obsidian/`.
- Finish with the full unit suite and `make check`; open a PR for review without merging.

## Task 1: Define the blocking gap-governance validator with tests

**Files:**

- Modify: `tests/test_validate_ref.py`
- Modify: `scripts/validate_ref.py`

- [ ] **Step 1: Add focused validator fixtures and a valid-path test**

Add a `GapGovernanceTests` class whose helper builds an in-memory graph containing:

```python
{
    "PL-01": {"type": "plateau", "relations": {}},
    "PL-02": {"type": "plateau", "relations": {}},
    "WP-01": {"type": "work-package", "relations": {}},
    "EVID-GAP-01": {"type": "evidence", "relations": {}},
    "GAP-01": {
        "type": "gap",
        "relations": {
            "between": ["PL-01", "PL-02"],
            "target_plateau": ["PL-02"],
            "addressed_by": ["WP-01"],
            "evidenced_by": ["EVID-GAP-01"],
            "gap_state": ["planned"],
            "closure_criteria": ["Qualification terrain acceptée"],
        },
    },
}
```

Assert that `check_gap_governance(objects)` returns no error for this graph.

- [ ] **Step 2: Add one failing test for each required failure class**

Cover all of the following independently and assert that the message names `GAP-01` and the offending field:

```python
def test_rejects_missing_or_invalid_gap_state(self): ...
def test_rejects_zero_or_multiple_target_plateaux(self): ...
def test_rejects_wrong_relation_target_types(self): ...
def test_rejects_empty_closure_criteria(self): ...
def test_rejects_target_plateau_outside_between(self): ...
```

For wrong target types, exercise all three typed relations: `target_plateau -> plateau`, `addressed_by -> work-package`, and `evidenced_by -> evidence`.

- [ ] **Step 3: Run the new tests and confirm they fail because the API is absent**

Run:

```bash
python3 -m unittest tests.test_validate_ref.GapGovernanceTests -v
```

Expected: `ImportError` or missing-function failures for `check_gap_governance`.

- [ ] **Step 4: Implement the smallest validator API**

In `scripts/validate_ref.py`, add:

```python
TYPE_GAP = "gap"
TYPE_PLATEAU = "plateau"
TYPE_WORK_PACKAGE = "work-package"
TYPE_EVIDENCE = "evidence"
GAP_STATES = {"identified", "planned", "in-remediation", "closed", "accepted-risk"}
```

Extend `RELATION_KEYS` with:

```python
"between",
"target_plateau",
"addressed_by",
"evidenced_by",
"gap_state",
"closure_criteria",
```

Implement `check_gap_governance(objects)` to return a list of human-readable errors. For each object of type `gap`, it must:

1. require exactly one `gap_state` in `GAP_STATES`;
2. require exactly one `target_plateau`, resolving to type `plateau`;
3. require at least one `addressed_by`, each resolving to type `work-package`;
4. require at least one `evidenced_by`, each resolving to type `evidence`;
5. require at least one non-empty `closure_criteria` item;
6. require the target plateau to be one of the gap's `between` plateaux.

Do not call it from `main()` yet: the three canonical gaps are intentionally migrated in Task 2 so the branch stays green between commits.

- [ ] **Step 5: Run focused and complete validator tests**

Run:

```bash
python3 -m unittest tests.test_validate_ref.GapGovernanceTests -v
python3 -m unittest tests.test_validate_ref -v
```

Expected: all tests pass.

- [ ] **Step 6: Commit the validator contract**

```bash
git add tests/test_validate_ref.py scripts/validate_ref.py
git diff --cached --check
git commit -m "test: define gap governance validation"
```

## Task 2: Govern the canonical gaps and introduce closure evidence

**Files:**

- Modify: `04_architecture-repository/_schema.md`
- Modify: `04_architecture-repository/07_migration/gaps/gap-01.md`
- Modify: `04_architecture-repository/07_migration/gaps/gap-02.md`
- Modify: `04_architecture-repository/07_migration/gaps/gap-03.md`
- Create: `04_architecture-repository/06_governance/evidence/evid-gap-01-qualification-offline.md`
- Create: `04_architecture-repository/06_governance/evidence/evid-gap-02-interoperabilite-etendue.md`
- Create: `04_architecture-repository/06_governance/evidence/evid-gap-03-cadre-legal.md`
- Modify: `scripts/build_wrappers.py`
- Modify: `scripts/validate_ref.py`
- Modify: `tests/test_validate_ref.py`
- Regenerate: repository indexes, existing derived views, wrappers, and Mintlify pages

- [ ] **Step 1: Add a real-repository mapping test before editing sources**

Add a test that loads the repository graph and asserts this exact mapping:

```python
EXPECTED = {
    "GAP-01": {
        "target_plateau": {"PL-02"},
        "addressed_by": {"WP-02"},
        "evidenced_by": {"EVID-GAP-01-QUALIFICATION-OFFLINE"},
    },
    "GAP-02": {
        "target_plateau": {"PL-03"},
        "addressed_by": {"WP-06", "WP-07"},
        "evidenced_by": {"EVID-GAP-02-INTEROPERABILITE-ETENDUE"},
    },
    "GAP-03": {
        "target_plateau": {"PL-01"},
        "addressed_by": {"WP-01"},
        "evidenced_by": {"EVID-GAP-03-CADRE-LEGAL"},
    },
}
```

For every gap also assert `gap_state == {"planned"}` and non-empty `closure_criteria`.

- [ ] **Step 2: Run the mapping test and confirm it fails on the placeholders**

Run:

```bash
python3 -m unittest tests.test_validate_ref.GapGovernanceRepositoryTests -v
```

Expected: failures list the missing lifecycle and closure mappings.

- [ ] **Step 3: Document the schema contract**

In `04_architecture-repository/_schema.md`, document these gap-only fields and their cardinality/type rules:

```yaml
gap_state: planned
target_plateau: [PL-02]
addressed_by: [WP-02]
evidenced_by: [EVID-GAP-01-QUALIFICATION-OFFLINE]
closure_criteria: ["Qualification terrain acceptée", "Synchronisation sans perte démontrée"]
```

State explicitly that `status` remains the general repository lifecycle, while `gap_state` represents remediation progress.

- [ ] **Step 4: Enrich all three canonical gap objects**

Keep their existing identity, title, description, `between`, `impacts`, and ownership semantics. Add the approved lifecycle fields and business-specific criteria:

- `GAP-01`: `planned`, target `PL-02`, WP `WP-02`, evidence `EVID-GAP-01-QUALIFICATION-OFFLINE`; criteria must cover offline qualification and lossless synchronization.
- `GAP-02`: `planned`, target `PL-03`, WPs `WP-06` and `WP-07`, evidence `EVID-GAP-02-INTEROPERABILITE-ETENDUE`; criteria must cover the intended interoperability perimeter and successful controlled exchanges.
- `GAP-03`: `planned`, target `PL-01`, WP `WP-01`, evidence `EVID-GAP-03-CADRE-LEGAL`; criteria must cover formal approval/publication and applicability of the legal or governance framework.

Use inline YAML lists and avoid commas inside individual criterion strings because the repository parser handles simple inline lists.

- [ ] **Step 5: Create the three canonical evidence objects**

Each evidence file must be a standalone repository object with:

```yaml
type: evidence
status: candidate
niveau: "3"
owner: DNS
togaf_repository_section: governance-repository
togaf_adm_phase: G
architecture_level: implementation
architecture_domain: cross-domain
architecture_scope: national
architecture_state: target
```

Give it the approved `EVID-*` ID, a meaningful title and acceptance description, and `related` links back to its gap and work package(s). Do not add an envelope; it is canonical evidence, not a manually duplicated publication page.

- [ ] **Step 6: Make builders preserve and render the new metadata**

In `scripts/build_wrappers.py`, load these fields into every object record:

```python
"owner",
"between",
"gap_state",
"target_plateau",
"addressed_by",
"evidenced_by",
"closure_criteria",
```

Extend `RATTACHEMENT_KEYS` with `between`, `target_plateau`, `addressed_by`, and `evidenced_by` so enriched existing gap envelopes expose navigable relationships. Render lifecycle and criteria in the gap body without manually copying source objects.

- [ ] **Step 7: Wire the blocking validator into the full validation path**

Call `check_gap_governance(objects)` from `main()` after graph loading and alongside the existing semantic checks. Print every error and make any error contribute to a non-zero exit code.

Add an integration test that invokes the validator against a temporary repository containing an invalid gap plus otherwise resolvable plateau/WP/evidence objects; assert exit code `1` and an error mentioning both the gap ID and invalid field.

- [ ] **Step 8: Regenerate impacted artifacts**

Run the repository's actual generation entry points after confirming their help or Make targets:

```bash
python3 scripts/build_ref_index.py
python3 scripts/build_wrappers.py
python3 scripts/build_mintlify.py
```

If a script requires explicit flags discovered from `--help`, use those exact flags and record the effective command in the commit/PR notes.

- [ ] **Step 9: Validate the canonical batch**

Run:

```bash
python3 -m unittest tests.test_validate_ref -v
python3 scripts/validate_ref.py
python3 scripts/build_wrappers.py --check
git diff --check
```

Expected: mapping tests pass; validator is `CONFORME`; wrappers are current.

- [ ] **Step 10: Commit canonical governance and generated envelopes together**

```bash
git add 04_architecture-repository scripts tests 02_artsn docs
git diff --cached --check
git commit -m "feat: govern migration gap closure"
```

Before committing, inspect the staged file list and unstage anything unrelated or under `graphify-out/` or `.obsidian/`.

## Task 3: Derive the TOGAF gap-closure roadmap

**Files:**

- Create: `tests/test_gap_view.py`
- Modify: `scripts/build_wrappers.py`
- Modify: `scripts/validate_ref.py`
- Modify: `scripts/build_ref_index.py`
- Create: `04_architecture-repository/08_views/togaf/gap-closure-roadmap.md`

- [ ] **Step 1: Write renderer tests first**

Test a small shuffled object set and assert that the rendered Markdown:

- sorts gaps deterministically by natural ID order;
- includes the chain `between -> gap -> target plateau -> work package -> evidence`;
- includes state, owner, impacted objects, and closure criteria;
- contains links resolved from canonical object paths rather than copied descriptions.

Add a real-repository test that renders current data and asserts all of these IDs appear:

```text
GAP-01 PL-02 WP-02 EVID-GAP-01-QUALIFICATION-OFFLINE
GAP-02 PL-03 WP-06 WP-07 EVID-GAP-02-INTEROPERABILITE-ETENDUE
GAP-03 PL-01 WP-01 EVID-GAP-03-CADRE-LEGAL
```

- [ ] **Step 2: Run the view tests and confirm the renderer is missing**

```bash
python3 -m unittest tests.test_gap_view -v
```

Expected: import or missing-renderer failure.

- [ ] **Step 3: Implement `render_gap_closure_roadmap`**

In `scripts/build_wrappers.py`, implement a deterministic table renderer with these columns:

```text
Gap | État | Transition | Plateau cible | Responsable | Work packages | Objets impactés | Critères de clôture | Preuves
```

Use existing path/link helpers and natural sorting. Escape Markdown pipes in scalar values and join multiple criteria with `<br>`. The renderer must consume only loaded canonical metadata.

- [ ] **Step 4: Register the derived view**

Create `04_architecture-repository/08_views/togaf/gap-closure-roadmap.md` with repository-view frontmatter and:

```markdown
<!-- BEGIN:GENERATED mode=gap-closure-roadmap -->
<!-- END:GENERATED -->
```

Add the `gap-closure-roadmap` generation mode to the wrapper dispatcher.

Add the path to `DERIVED_ARCH_REPOSITORY_DOCS` in all three scripts:

- `scripts/build_wrappers.py`
- `scripts/validate_ref.py`
- `scripts/build_ref_index.py`

This ensures the view is generated and excluded from canonical object indexing/validation as appropriate.

- [ ] **Step 5: Generate and validate the view**

```bash
python3 scripts/build_wrappers.py
python3 -m unittest tests.test_gap_view -v
python3 scripts/build_wrappers.py --check
python3 scripts/validate_ref.py
git diff --check
```

Expected: all three closure chains are present, the second wrapper run makes no change, and validation is `CONFORME`.

- [ ] **Step 6: Commit the derived roadmap**

```bash
git add tests/test_gap_view.py scripts/build_wrappers.py scripts/validate_ref.py scripts/build_ref_index.py 04_architecture-repository/08_views/togaf/gap-closure-roadmap.md
git diff --cached --check
git commit -m "feat: derive gap closure roadmap"
```

## Task 4: Full regeneration, verification, and review handoff

**Files:**

- Regenerate: every artifact affected by the canonical and generator changes
- Inspect: all branch commits and final diff against `main`

- [ ] **Step 1: Run every generator and prove idempotence**

```bash
python3 scripts/build_ref_index.py
python3 scripts/build_wrappers.py
python3 scripts/build_mintlify.py
git status --short
python3 scripts/build_wrappers.py --check
```

If regeneration changes tracked files, inspect and commit only legitimate derived updates. Run the generators once more and require a clean result.

- [ ] **Step 2: Run focused and complete verification**

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_ref.py
python3 scripts/build_wrappers.py --check
make check
```

Expected: all commands exit `0`; the validator reports `CONFORME`; wrapper count matches the repository's newly generated truth.

- [ ] **Step 3: Audit the final diff**

```bash
git diff --check main...HEAD
git status --short
git log --oneline main..HEAD
git diff --stat main...HEAD
git diff --name-only main...HEAD
```

Confirm:

- every gap has one valid state and one target plateau;
- all WP/evidence references resolve to the correct types;
- each target belongs to `between`;
- closure criteria are non-empty and business-specific;
- evidence remains `candidate`;
- the derived roadmap contains no duplicated canonical declarations;
- P3.2 compliance harmonization is absent;
- `graphify-out/` and `.obsidian/` are absent.

- [ ] **Step 4: Commit any final generated artifacts**

```bash
git add <only-reviewed-generated-files>
git diff --cached --check
git commit -m "chore: regenerate gap governance artifacts"
```

Skip this commit if the tree is already clean.

- [ ] **Step 5: Push and open a PR without merging**

```bash
git push -u origin codex/p3-1-gap-governance
gh pr create --base main --head codex/p3-1-gap-governance --title "P3.1: govern migration gap closure" --body-file <reviewed-pr-body-file>
```

The PR body must separate:

- canonical gap lifecycle and evidence changes;
- blocking semantic validation;
- generated TOGAF roadmap and refreshed publication artifacts;
- executed validation commands and outcomes;
- remaining ambiguity, explicitly stating that P3.2 compliance harmonization remains out of scope.

- [ ] **Step 6: Observe CI and hand off for review**

Use `gh pr checks <PR-number> --watch` or bounded status checks. Fix only failures caused by this branch, rerun the relevant local checks, push, and leave the PR unmerged for user review.
