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


if __name__ == "__main__":
    unittest.main()
