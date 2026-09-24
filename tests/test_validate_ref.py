import importlib.util
from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = REPO_ROOT / "scripts" / "validate_ref.py"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_ref", VALIDATOR_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ValidatorConfigurationTests(unittest.TestCase):
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


class CanonicalMappingTests(unittest.TestCase):
    def setUp(self):
        self.validator = load_validator()

    def relation_values(self, relative_path, key):
        text = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
        frontmatter, _body = self.validator.parse_frontmatter(text)
        return set(self.validator.list_value(
            self.validator.fm_field(frontmatter, key)
        ))

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
            "cmp-12.md": {"CAP-07"},
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


if __name__ == "__main__":
    unittest.main()
