import importlib.util
from pathlib import Path
import re
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = REPO_ROOT / "scripts" / "validate_ref.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_ref", VALIDATOR_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ValidatorConfigurationTests(unittest.TestCase):
    def test_inline_list_preserves_apostrophes_inside_double_quoted_values(self):
        validator = load_validator()

        parsed = validator.list_value(
            '["Contrats d\'échange applicables identifiés", '
            '"Pièces utilisables dans le processus d\'homologation"]'
        )

        self.assertEqual(
            [
                "Contrats d'échange applicables identifiés",
                "Pièces utilisables dans le processus d'homologation",
            ],
            parsed,
        )

    def test_source_contains_no_git_conflict_markers(self):
        source = VALIDATOR_PATH.read_text(encoding="utf-8")

        self.assertNotIn("<<<<<<<", source)
        self.assertNotIn("=======", source)
        self.assertNotIn(">>>>>>>", source)

    def test_repository_and_adr_directories_are_canonical(self):
        validator = load_validator()

        self.assertEqual([validator.ARCH_REPOSITORY_DIR], validator.REL_DIRS)
        self.assertEqual(["01_cnisn/06_decisions"], validator.ADR_DIRS)

    def test_migrated_profiles_keep_only_canonical_mappings(self):
        expected = {
            "pt-14.md": "PART-ECHANGE-TRANSFRONTALIER",
            "pt-15.md": "PART-ONE-HEALTH",
        }
        profiles_dir = (
            REPO_ROOT
            / "04_architecture-repository"
            / "05_building-blocks"
            / "sbb"
            / "legacy-profiles"
        )

        for filename, replacement in expected.items():
            text = (profiles_dir / filename).read_text(encoding="utf-8")
            frontmatter = text.split("---", 2)[1]
            maps_to_lines = [
                line for line in frontmatter.splitlines()
                if line.startswith("maps_to:")
            ]

            self.assertEqual(1, len(maps_to_lines), filename)
            self.assertIn(replacement, maps_to_lines[0])
            self.assertNotIn("CAP-INT-", maps_to_lines[0])


class PartitionRelationTests(unittest.TestCase):
    def setUp(self):
        self.validator = load_validator()

    def test_partition_relation_accepts_architecture_partition_target(self):
        objects = {
            "ABB-EXEMPLE": {
                "id": "ABB-EXEMPLE",
                "file": "/tmp/abb-exemple.md",
                "type": "architecture-building-block",
                "relations": {"partitions": {"PART-VS-01"}},
            },
            "PART-VS-01": {
                "id": "PART-VS-01",
                "file": "/tmp/part-vs-01.md",
                "type": "architecture-partition",
                "relations": {},
            },
        }

        errors = self.validator.check_partition_relation_types(objects)

        self.assertEqual([], errors)

    def test_partition_relation_rejects_non_partition_target(self):
        objects = {
            "ABB-EXEMPLE": {
                "id": "ABB-EXEMPLE",
                "file": "/tmp/abb-exemple.md",
                "type": "architecture-building-block",
                "relations": {"partitions": {"CAP-14"}},
            },
            "CAP-14": {
                "id": "CAP-14",
                "file": "/tmp/cap-14.md",
                "type": "capabilite",
                "relations": {},
            },
        }

        errors = self.validator.check_partition_relation_types(objects)

        self.assertEqual(1, len(errors))
        self.assertEqual("ABB-EXEMPLE", errors[0][1])
        self.assertEqual("CAP-14", errors[0][2])
        self.assertIn("architecture-partition", errors[0][3])


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

    def test_accepts_value_stream_covered_only_by_assigned_abb_maps_to(self):
        graph = self.graph(set())
        graph["PART-ONE-HEALTH"]["relations"]["applies_to"] = {"VS-02", "CAP-08"}
        graph["VS-02"]["relations"]["applies_to"] = {"CAP-18"}
        graph["ABB-ONE-HEALTH"] = {
            "id": "ABB-ONE-HEALTH", "file": "/tmp/abb-one-health.md",
            "type": "architecture-building-block",
            "relations": {
                "partitions": {"PART-ONE-HEALTH"},
                "maps_to": {"CAP-18"},
            },
        }

        errors = self.validator.check_partition_value_stream_coverage(graph)

        self.assertEqual([], errors)

    def test_rejects_assigned_abb_maps_to_capability_without_value_stream_overlap(self):
        graph = self.graph(set())
        graph["PART-ONE-HEALTH"]["relations"]["applies_to"] = {"VS-02", "CAP-08"}
        graph["VS-02"]["relations"]["applies_to"] = {"CAP-18"}
        graph["ABB-ONE-HEALTH"] = {
            "id": "ABB-ONE-HEALTH", "file": "/tmp/abb-one-health.md",
            "type": "architecture-building-block",
            "relations": {
                "partitions": {"PART-ONE-HEALTH"},
                "maps_to": {"CAP-08"},
            },
        }

        errors = self.validator.check_partition_value_stream_coverage(graph)

        self.assertEqual(["VS-02"], [error[2] for error in errors])

    def test_main_rejects_partition_without_value_stream_capability_coverage(self):
        with TemporaryDirectory() as temp_dir:
            model_dir = Path(temp_dir) / self.validator.ARCH_REPOSITORY_DIR
            model_dir.mkdir()
            for object_id, obj in self.graph({"CAP-18"}).items():
                applies_to = sorted(obj["relations"].get("applies_to", set()))
                (model_dir / (object_id.lower() + ".md")).write_text(
                    "---\nid: %s\ntype: %s\napplies_to: %s\n---\n"
                    % (object_id, obj["type"], applies_to),
                    encoding="utf-8",
                )
            result = subprocess.run(
                [
                    sys.executable, "-c",
                    "import sys; from scripts import validate_ref; "
                    "validate_ref.REPO_ROOT = sys.argv[1]; "
                    "sys.exit(validate_ref.main())",
                    temp_dir,
                ],
                cwd=REPO_ROOT, capture_output=True, text=True,
            )

        self.assertEqual(1, result.returncode, result.stdout + result.stderr)
        self.assertIn("PART-ONE-HEALTH", result.stdout)
        self.assertIn("VS-04", result.stdout)


class GapGovernanceTests(unittest.TestCase):
    def setUp(self):
        self.validator = load_validator()

    def graph(self):
        return {
            "PL-01": {"type": "plateau", "relations": {}},
            "PL-02": {"type": "plateau", "relations": {}},
            "WP-01": {"type": "work-package", "relations": {}},
            "EVID-GAP-01": {"type": "evidence", "relations": {}},
            "GAP-01": {
                "file": "/tmp/gap-01.md",
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

    def assert_gap_error(self, errors, field):
        rendered = "\n".join(" | ".join(map(str, error)) for error in errors)
        self.assertIn("GAP-01", rendered)
        self.assertIn(field, rendered)

    def test_accepts_complete_gap_closure_path(self):
        self.assertEqual([], self.validator.check_gap_governance(self.graph()))

    def test_rejects_missing_or_invalid_gap_state(self):
        for value in ([], ["unknown"]):
            with self.subTest(value=value):
                graph = self.graph()
                graph["GAP-01"]["relations"]["gap_state"] = value

                errors = self.validator.check_gap_governance(graph)

                self.assert_gap_error(errors, "gap_state")

    def test_rejects_zero_or_multiple_target_plateaux(self):
        for value in ([], ["PL-01", "PL-02"]):
            with self.subTest(value=value):
                graph = self.graph()
                graph["GAP-01"]["relations"]["target_plateau"] = value

                errors = self.validator.check_gap_governance(graph)

                self.assert_gap_error(errors, "target_plateau")

    def test_rejects_wrong_relation_target_types(self):
        cases = (
            ("target_plateau", "WP-01"),
            ("addressed_by", "PL-02"),
            ("evidenced_by", "WP-01"),
        )
        for field, target_id in cases:
            with self.subTest(field=field):
                graph = self.graph()
                graph["GAP-01"]["relations"][field] = [target_id]

                errors = self.validator.check_gap_governance(graph)

                self.assert_gap_error(errors, field)

    def test_rejects_empty_closure_criteria(self):
        for value in ([], [" "]):
            with self.subTest(value=value):
                graph = self.graph()
                graph["GAP-01"]["relations"]["closure_criteria"] = value

                errors = self.validator.check_gap_governance(graph)

                self.assert_gap_error(errors, "closure_criteria")

    def test_rejects_target_plateau_outside_between(self):
        graph = self.graph()
        graph["GAP-01"]["relations"]["between"] = ["PL-01"]

        errors = self.validator.check_gap_governance(graph)

        self.assert_gap_error(errors, "target_plateau")

    def test_main_rejects_invalid_gap_state(self):
        with TemporaryDirectory() as temp_dir:
            model_dir = Path(temp_dir) / self.validator.ARCH_REPOSITORY_DIR
            model_dir.mkdir()
            fixtures = {
                "pl-01.md": "---\nid: PL-01\ntype: plateau\n---\n",
                "pl-02.md": "---\nid: PL-02\ntype: plateau\n---\n",
                "wp-01.md": "---\nid: WP-01\ntype: work-package\n---\n",
                "evid-gap-01.md": "---\nid: EVID-GAP-01\ntype: evidence\n---\n",
                "gap-01.md": (
                    "---\nid: GAP-01\ntype: gap\n"
                    "between: [PL-01, PL-02]\n"
                    "target_plateau: [PL-02]\n"
                    "addressed_by: [WP-01]\n"
                    "evidenced_by: [EVID-GAP-01]\n"
                    "gap_state: unknown\n"
                    "closure_criteria: [Qualification acceptée]\n---\n"
                ),
            }
            for filename, content in fixtures.items():
                (model_dir / filename).write_text(content, encoding="utf-8")
            result = subprocess.run(
                [
                    sys.executable, "-c",
                    "import sys; from scripts import validate_ref; "
                    "validate_ref.REPO_ROOT = sys.argv[1]; "
                    "sys.exit(validate_ref.main())",
                    temp_dir,
                ],
                cwd=REPO_ROOT, capture_output=True, text=True,
            )

        self.assertEqual(1, result.returncode, result.stdout + result.stderr)
        self.assertIn("GAP-01", result.stdout)
        self.assertIn("gap_state", result.stdout)


class GapGovernanceRepositoryTests(unittest.TestCase):
    def setUp(self):
        self.validator = load_validator()

    def test_canonical_gaps_define_approved_closure_paths(self):
        expected = {
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
        objects, _paths, _unresolved, _legacy = self.validator.load_relation_graph()

        for gap_id, expected_relations in expected.items():
            with self.subTest(gap_id=gap_id):
                relations = objects[gap_id]["relations"]
                for field, targets in expected_relations.items():
                    self.assertEqual(targets, relations[field], field)
                self.assertEqual({"planned"}, relations["gap_state"])
                self.assertTrue(relations["closure_criteria"])


class DataObjectGovernanceTests(unittest.TestCase):
    def setUp(self):
        self.validator = load_validator()

    def data_object(self, **relations):
        base = {
            "id": "DO-TEST",
            "file": "/tmp/do-test.md",
            "type": "objet-de-donnees",
            "out": set(),
            "relations": {},
        }
        base["relations"].update(relations)
        return base

    def composant(self, component_id="CMP-19"):
        return {
            "id": component_id,
            "file": "/tmp/%s.md" % component_id.lower(),
            "type": "composant-applicatif",
            "out": set(),
            "relations": {},
        }

    def test_rejects_missing_tier(self):
        objects = {
            "DO-TEST": self.data_object(system_of_record=["CMP-19"]),
            "CMP-19": self.composant(),
        }

        errors = self.validator.check_data_object_governance(objects)

        self.assertEqual(1, len(errors))
        self.assertEqual("tier", errors[0][2])

    def test_rejects_unknown_tier(self):
        objects = {
            "DO-TEST": self.data_object(tier=["D"], system_of_record=["CMP-19"]),
            "CMP-19": self.composant(),
        }

        errors = self.validator.check_data_object_governance(objects)

        self.assertEqual(1, len(errors))
        self.assertEqual("tier", errors[0][2])

    def test_rejects_missing_system_of_record(self):
        objects = {"DO-TEST": self.data_object(tier=["B"])}

        errors = self.validator.check_data_object_governance(objects)

        self.assertEqual(1, len(errors))
        self.assertEqual("system_of_record", errors[0][2])

    def test_rejects_system_of_record_targeting_a_data_object(self):
        objects = {
            "DO-TEST": self.data_object(tier=["B"], system_of_record=["DO-OTHER"]),
            "DO-OTHER": self.data_object(tier=["B"], system_of_record=["CMP-19"]),
            "CMP-19": self.composant(),
        }

        errors = self.validator.check_data_object_governance(objects)

        self.assertEqual(1, len(errors))
        self.assertEqual("DO-OTHER", errors[0][2])

    def test_accepts_a_governed_data_object(self):
        objects = {
            "DO-TEST": self.data_object(tier=["B"], system_of_record=["CMP-19"]),
            "CMP-19": self.composant(),
        }

        self.assertEqual([], self.validator.check_data_object_governance(objects))


class AccessSemanticsTests(unittest.TestCase):
    """Les deux emplois de `accesses` : adossement du processus, accès du
    système de référence, symétrie du couple PRC/CMP."""

    def setUp(self):
        self.validator = load_validator()

    def data_object(self, object_id="DO-TEST", **relations):
        base = {
            "id": object_id,
            "file": "/tmp/%s.md" % object_id.lower(),
            "type": "objet-de-donnees",
            "out": set(),
            "relations": {},
        }
        base["relations"].update(relations)
        return base

    def composant(self, component_id="CMP-19", **relations):
        base = {
            "id": component_id,
            "file": "/tmp/%s.md" % component_id.lower(),
            "type": "composant-applicatif",
            "out": set(),
            "relations": {},
        }
        base["relations"].update(relations)
        return base

    def processus(self, process_id="PRC-01", **relations):
        base = {
            "id": process_id,
            "file": "/tmp/%s.md" % process_id.lower(),
            "type": "processus-metier",
            "out": set(),
            "relations": {},
        }
        base["relations"].update(relations)
        return base

    def test_rejects_process_access_without_a_backing_component(self):
        objects = {
            "DO-TEST": self.data_object(accessed_by=["PRC-01"]),
            "PRC-01": self.processus(uses=["CMP-19"]),
            "CMP-19": self.composant(accesses=["DO-OTHER"]),
            "DO-OTHER": self.data_object("DO-OTHER"),
        }

        errors = self.validator.check_process_data_access_backing(objects)

        self.assertEqual(1, len(errors))
        self.assertEqual("PRC-01", errors[0][2])

    def test_rejects_process_access_when_the_holder_is_not_mobilised(self):
        objects = {
            "DO-TEST": self.data_object(accessed_by=["PRC-01"]),
            "PRC-01": self.processus(),
            "CMP-19": self.composant(accesses=["DO-TEST"]),
        }

        errors = self.validator.check_process_data_access_backing(objects)

        self.assertEqual(1, len(errors))
        self.assertEqual("PRC-01", errors[0][2])

    def test_accepts_process_access_backed_by_a_mobilised_component(self):
        objects = {
            "DO-TEST": self.data_object(accessed_by=["PRC-01"]),
            "PRC-01": self.processus(uses=["CMP-19"]),
            "CMP-19": self.composant(accesses=["DO-TEST"]),
        }

        self.assertEqual(
            [], self.validator.check_process_data_access_backing(objects)
        )

    def test_rejects_system_of_record_that_does_not_access_the_object(self):
        objects = {
            "DO-TEST": self.data_object(
                accessed_by=["CMP-19"], system_of_record=["CMP-19"]
            ),
            "CMP-19": self.composant(),
        }

        errors = self.validator.check_system_of_record_accessibility(objects)

        self.assertEqual(1, len(errors))
        self.assertEqual("CMP-19", errors[0][2])

    def test_accepts_system_of_record_that_accesses_the_object(self):
        objects = {
            "DO-TEST": self.data_object(
                accessed_by=["CMP-19"], system_of_record=["CMP-19"]
            ),
            "CMP-19": self.composant(accesses=["DO-TEST"]),
        }

        self.assertEqual(
            [], self.validator.check_system_of_record_accessibility(objects)
        )

    def test_rejects_component_applying_to_a_process_that_does_not_use_it(self):
        objects = {
            "PRC-01": self.processus(uses=["CMP-19"]),
            "CMP-19": self.composant(applies_to=["PRC-01"]),
        }
        objects["PRC-01"]["relations"]["uses"] = set()

        errors = self.validator.check_uses_applies_to_symmetry(objects)

        self.assertEqual(1, len(errors))
        self.assertEqual("PRC-01", errors[0][2])

    def test_rejects_process_using_a_component_that_does_not_apply_to_it(self):
        objects = {
            "PRC-01": self.processus(uses=["CMP-19"]),
            "CMP-19": self.composant(),
        }

        errors = self.validator.check_uses_applies_to_symmetry(objects)

        self.assertEqual(1, len(errors))
        self.assertEqual("CMP-19", errors[0][2])

    def test_accepts_a_symmetric_process_component_pair(self):
        objects = {
            "PRC-01": self.processus(uses=["CMP-19"]),
            "CMP-19": self.composant(applies_to=["PRC-01"]),
        }

        self.assertEqual(
            [], self.validator.check_uses_applies_to_symmetry(objects)
        )


class AccessSemanticsRepositoryTests(unittest.TestCase):
    """Le corpus réel respecte les trois règles de sémantique de l'accès."""

    def setUp(self):
        self.validator = load_validator()
        objects, _id_to_file, _unresolved, _legacy = (
            self.validator.load_relation_graph()
        )
        self.objects = objects

    def test_every_process_access_is_backed_by_a_mobilised_component(self):
        self.assertEqual(
            [], self.validator.check_process_data_access_backing(self.objects)
        )

    def test_every_system_of_record_accesses_its_object(self):
        self.assertEqual(
            [], self.validator.check_system_of_record_accessibility(self.objects)
        )

    def test_uses_and_applies_to_are_symmetric(self):
        self.assertEqual(
            [], self.validator.check_uses_applies_to_symmetry(self.objects)
        )


class RetiredDataObjectTests(unittest.TestCase):
    def setUp(self):
        self.validator = load_validator()

    def migration(self):
        return {
            "DO-02": {
                "legacy_id": "DO-02",
                "legacy_title": "Identifiant national d'identification",
                "disposition": "merged",
                "primary_replacement": "DO-01",
                "replacement_ids": {"DO-01"},
                "rationale": "",
            },
        }

    def data_object(self, object_id, **relations):
        return {
            "id": object_id,
            "file": "/tmp/%s.md" % object_id.lower(),
            "type": "objet-de-donnees",
            "out": set(),
            "relations": relations,
        }

    def test_rejects_retired_id_present_as_active_object(self):
        objects = {
            "DO-02": self.data_object("DO-02"),
            "DO-01": self.data_object("DO-01", absorbs={"DO-02"}),
        }

        errors = self.validator.check_retired_data_objects(objects, self.migration())

        self.assertEqual(1, len(errors))
        self.assertIn("objet actif", errors[0][3])

    def test_rejects_relation_targeting_a_retired_id(self):
        successor = self.data_object("DO-01", absorbs={"DO-02"})
        successor["out"] = {"DO-02"}

        errors = self.validator.check_retired_data_objects(
            {"DO-01": successor}, self.migration())

        self.assertEqual(1, len(errors))
        self.assertEqual("DO-02", errors[0][2])

    def test_requires_the_successor_to_declare_absorbs(self):
        objects = {"DO-01": self.data_object("DO-01")}

        errors = self.validator.check_retired_data_objects(objects, self.migration())

        self.assertEqual(1, len(errors))
        self.assertIn("absorbs", errors[0][3])

    def test_rejects_absorbs_not_declared_by_the_migration_trace(self):
        objects = {
            "DO-01": self.data_object("DO-01", absorbs={"DO-02", "DO-99"}),
        }

        errors = self.validator.check_retired_data_objects(objects, self.migration())

        self.assertEqual(1, len(errors))
        self.assertEqual("DO-99", errors[0][2])

    def test_accepts_a_traced_merger(self):
        objects = {"DO-01": self.data_object("DO-01", absorbs={"DO-02"})}

        errors = self.validator.check_retired_data_objects(objects, self.migration())

        self.assertEqual([], errors)


class DataObjectMigrationRepositoryTests(unittest.TestCase):
    def setUp(self):
        self.validator = load_validator()

    def test_migration_trace_declares_the_nine_retirements(self):
        migration = self.validator.load_do_migration()

        self.assertEqual(
            {
                "DO-02", "DO-04", "DO-08", "DO-13", "DO-15",
                "DO-21", "DO-22", "DO-28", "DO-30",
            },
            set(migration),
        )
        for legacy_id, entry in migration.items():
            self.assertTrue(entry["disposition"] in {"merged", "retired"}, legacy_id)
            self.assertTrue(entry["primary_replacement"], legacy_id)

    def test_repository_has_no_residual_reference_to_retired_objects(self):
        migration = self.validator.load_do_migration()

        errors = self.validator.check_retired_frontmatter_references(migration)

        self.assertEqual([], errors)

    def test_every_surviving_data_object_declares_its_governance(self):
        objects, _paths, _unresolved, _legacy = self.validator.load_relation_graph()
        data_objects = {
            oid: obj for oid, obj in objects.items()
            if obj.get("type") == "objet-de-donnees"
        }

        self.assertEqual(23, len(data_objects))
        self.assertEqual([], self.validator.check_data_object_governance(objects))
        self.assertEqual([], self.validator.check_retired_data_objects(
            objects, self.validator.load_do_migration()))


class ThemeAssignmentTests(unittest.TestCase):
    def setUp(self):
        self.validator = load_validator()

    def data_object(self, object_id, theme=None):
        relations = {}
        if theme is not None:
            relations["theme"] = {theme}
        return {
            "id": object_id,
            "file": "/tmp/%s.md" % object_id.lower(),
            "type": "objet-de-donnees",
            "out": set(),
            "relations": relations,
        }

    def test_rejects_a_data_object_without_theme(self):
        objects = {"DO-01": self.data_object("DO-01")}

        errors = self.validator.check_theme_assignment(objects, {}, {})

        self.assertEqual(1, len(errors))
        self.assertIn("sans thème", errors[0][3])

    def test_rejects_a_theme_outside_the_controlled_vocabulary(self):
        objects = {"DO-01": self.data_object("DO-01", "theme-inconnu")}

        errors = self.validator.check_theme_assignment(objects, {}, {})

        self.assertEqual(1, len(errors))
        self.assertIn("hors du vocabulaire", errors[0][3])

    def test_rejects_a_theme_of_the_vocabulary_without_any_object(self):
        objects = {"DO-01": self.data_object("DO-01", "patient-identite")}

        errors = self.validator.check_theme_assignment(
            objects, {"patient-identite": {}, "prestation-soins": {}}, {})

        self.assertEqual(1, len(errors))
        self.assertIn("sans objet de données", errors[0][3])

    def test_rejects_a_partition_that_differs_from_the_retired_scope(self):
        migration = {
            "BO-01": {
                "legacy_id": "BO-01",
                "disposition": "retired",
                "theme": "patient-identite",
                "replacement_ids": {"DO-01", "DO-03"},
            },
        }
        objects = {
            "DO-01": self.data_object("DO-01", "patient-identite"),
            "DO-02": self.data_object("DO-02", "patient-identite"),
        }

        errors = self.validator.check_theme_assignment(
            objects, {"patient-identite": {}}, migration)

        self.assertEqual(2, len(errors))
        self.assertEqual({"DO-02", "DO-03"}, {error[2] for error in errors})

    def test_accepts_a_partition_equal_to_the_retired_scope(self):
        migration = {
            "BO-01": {
                "legacy_id": "BO-01",
                "disposition": "retired",
                "theme": "patient-identite",
                "replacement_ids": {"DO-01", "DO-03"},
            },
        }
        objects = {
            "DO-01": self.data_object("DO-01", "patient-identite"),
            "DO-03": self.data_object("DO-03", "patient-identite"),
        }

        errors = self.validator.check_theme_assignment(
            objects, {"patient-identite": {}}, migration)

        self.assertEqual([], errors)


class ThemeVocabularyRepositoryTests(unittest.TestCase):
    def setUp(self):
        self.validator = load_validator()

    def test_vocabulary_declares_the_seven_themes(self):
        themes = self.validator.load_themes()

        self.assertEqual(
            {
                "patient-identite", "prestation-soins", "dispensation-produits",
                "financement-couverture", "risque-surveillance",
                "exploitation-gestion", "interop-transfrontalier",
            },
            set(themes),
        )
        for slug, theme in themes.items():
            self.assertTrue(theme["label"], slug)
            self.assertTrue(theme["description"], slug)
            self.assertTrue(theme["value_streams"], slug)

    def test_every_data_object_declares_a_theme_of_the_vocabulary(self):
        objects, _paths, _unresolved, _legacy = self.validator.load_relation_graph()
        themes = self.validator.load_themes()
        migration = self.validator.load_object_migration()

        self.assertEqual([], self.validator.check_theme_assignment(
            objects, themes, migration))

    def test_theme_partition_reproduces_the_sections_of_the_data_dictionary(self):
        objects, _paths, _unresolved, _legacy = self.validator.load_relation_graph()
        themes = self.validator.load_themes()

        grouped = {}
        for oid, obj in objects.items():
            if obj.get("type") != "objet-de-donnees":
                continue
            theme = sorted(obj.get("relations", {}).get("theme", set()))[0]
            grouped.setdefault(theme, set()).add(oid)

        # Le dictionnaire des données fonctionnelles classe déjà les objets
        # actifs en sept sections ; la propriété `theme` doit reproduire
        # exactement ce découpage.
        dictionary = (
            REPO_ROOT / "02_artsn/03_objets-de-donnees/index.md"
        ).read_text(encoding="utf-8")
        sections = re.split(r"\n## ", dictionary)
        expected = {}
        for section in sections:
            match = re.match(r"([1-7])\.\s", section)
            if not match:
                continue
            ids = {
                oid for oid in re.findall(r"\bDO-\d\d\b", section)
                if oid in grouped_objects(objects)
            }
            if ids:
                expected[int(match.group(1))] = ids

        self.assertEqual(7, len(expected))
        self.assertEqual(
            sorted(sorted(ids) for ids in expected.values()),
            sorted(sorted(ids) for ids in grouped.values()),
        )


def grouped_objects(objects):
    return {
        oid for oid, obj in objects.items()
        if obj.get("type") == "objet-de-donnees"
    }


class RetiredObjectTests(unittest.TestCase):
    def setUp(self):
        self.validator = load_validator()

    def test_retirement_trace_declares_the_eight_retirements(self):
        migration = self.validator.load_object_migration()

        self.assertEqual(
            {
                "BO-01", "BO-02", "BO-03", "BO-04", "BO-05", "BO-06",
                "BO-07", "CMP-09",
            },
            set(migration),
        )
        for legacy_id, entry in migration.items():
            self.assertTrue(
                entry["disposition"] in {"merged", "retired"}, legacy_id)
            self.assertTrue(entry["rationale"], legacy_id)

    def test_merged_component_names_its_primary_replacement(self):
        migration = self.validator.load_object_migration()

        self.assertEqual("CMP-10", migration["CMP-09"]["primary_replacement"])

    def test_repository_has_no_residual_reference_to_retired_objects(self):
        objects, _paths, _unresolved, _legacy = self.validator.load_relation_graph()
        migration = self.validator.load_object_migration()

        self.assertEqual([], self.validator.check_retired_objects(
            objects, migration))

    def test_object_type_business_object_no_longer_exists(self):
        objects, _paths, _unresolved, _legacy = self.validator.load_relation_graph()

        self.assertEqual([], [
            oid for oid, obj in objects.items()
            if obj.get("type") == "objet-metier"
        ])

class CanonicalMappingTests(unittest.TestCase):
    def setUp(self):
        self.validator = load_validator()

    def relation_values(self, relative_path, key):
        text = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
        frontmatter, _body = self.validator.parse_frontmatter(text)
        return set(self.validator.list_value(
            self.validator.fm_field(frontmatter, key)
        ))

    def test_one_health_covers_surveillance_and_governance(self):
        partition = Path(
            "04_architecture-repository/01_partitions/sectorielles/part-one-health.md"
        )
        self.assertEqual(
            {"CAP-08", "CAP-18", "VS-02", "VS-04"},
            self.relation_values(partition, "applies_to"),
        )
        pt15 = Path(
            "04_architecture-repository/05_building-blocks/sbb/legacy-profiles/pt-15.md"
        )
        self.assertTrue(
            {
                "ABB-ECHANGE-MEDIATION", "ABB-EXPOSITION-DONNEES-ANALYTIQUES",
                "CAP-05", "CAP-08", "CAP-18",
            } <= self.relation_values(pt15, "maps_to")
        )

    def test_pt_20_maps_eligibility_profile_to_architecture(self):
        pt20 = Path(
            "04_architecture-repository/05_building-blocks/sbb/legacy-profiles/pt-20.md"
        )
        self.assertEqual(
            {"ABB-ELIGIBILITE-COUVERTURE", "CAP-07"},
            self.relation_values(pt20, "maps_to"),
        )
        self.assertEqual({"CMP-12"}, self.relation_values(pt20, "applies_to"))
        self.assertEqual({"ART-4C", "ART-9"}, self.relation_values(pt20, "implements"))

    def test_legacy_services_realize_their_business_responsibility(self):
        expected = {
            "srv-03.md": {"ABB-SERVICE-TERMINOLOGIE"},
            "srv-04.md": {"ABB-ECHANGE-MEDIATION"},
            "srv-05.md": {"ABB-ECHANGE-LOGISTIQUE-LMIS"},
            "srv-06.md": {"ABB-EXPOSITION-DONNEES-ANALYTIQUES"},
        }
        base = Path(
            "04_architecture-repository/05_building-blocks/abb/legacy-services"
        )

        for filename, targets in expected.items():
            self.assertEqual(
                targets,
                self.relation_values(base / filename, "realizes"),
                filename,
            )

    def test_pt_01_maps_to_exchange_mediation(self):
        path = Path(
            "04_architecture-repository/05_building-blocks/sbb/legacy-profiles/pt-01.md"
        )

        targets = self.relation_values(path, "maps_to")

        self.assertIn("ABB-ECHANGE-MEDIATION", targets)
        self.assertFalse(any(target.startswith("CAP-INT-") for target in targets))

    def test_legacy_components_map_to_semantically_matching_targets(self):
        expected = {
            "cmp-10.md": {"ABB-SERVICE-TERMINOLOGIE"},
            "cmp-11.md": {"ABB-IDENTITE-BENEFICIAIRE"},
            "cmp-12.md": {"ABB-ELIGIBILITE-COUVERTURE"},
            "cmp-14.md": {
                "ABB-SERVICE-TERMINOLOGIE",
                "ABB-ECHANGE-LOGISTIQUE-LMIS",
            },
            "cmp-23.md": {"ABB-ECHANGE-LOGISTIQUE-LMIS"},
        }
        base = Path(
            "04_architecture-repository/05_building-blocks/abb/legacy-components"
        )

        for filename, targets in expected.items():
            self.assertEqual(
                targets,
                self.relation_values(base / filename, "maps_to"),
                filename,
            )

    def test_eligibility_is_separate_from_identity_and_consent(self):
        abb = Path("04_architecture-repository/05_building-blocks/abb/abb-eligibilite-couverture.md")
        self.assertEqual({"CAP-07"}, self.relation_values(abb, "maps_to"))
        self.assertEqual({"PART-VS-03"}, self.relation_values(abb, "partitions"))
        self.assertEqual({"ART-4C", "ART-9"}, self.relation_values(abb, "implements"))
        self.assertEqual(
            {"DO-14", "DO-16", "DO-17"},
            self.relation_values(abb, "accesses"),
        )

        professionals = Path("04_architecture-repository/05_building-blocks/abb/abb-registre-professionnels.md")
        pt05 = Path("04_architecture-repository/05_building-blocks/sbb/legacy-profiles/pt-05.md")
        pt11 = Path("04_architecture-repository/05_building-blocks/sbb/legacy-profiles/pt-11.md")
        self.assertNotIn("ART-4C", self.relation_values(professionals, "implements"))
        self.assertNotIn("ART-4C", self.relation_values(pt05, "implements"))
        self.assertNotIn("CMP-12", self.relation_values(pt11, "applies_to"))


if __name__ == "__main__":
    unittest.main()
