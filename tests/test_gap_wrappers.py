import importlib.util
from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
BUILDER_PATH = REPO_ROOT / "scripts" / "build_wrappers.py"


def load_builder():
    spec = importlib.util.spec_from_file_location("build_wrappers", BUILDER_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class GapWrapperTests(unittest.TestCase):
    def test_transclusion_derives_gap_closure_governance_from_frontmatter(self):
        builder = load_builder()
        obj = {
            "rel": "04_architecture-repository/07_migration/gaps/gap-01.md",
            "envelope": "02_artsn/09_feuille-de-route/gap-01.md",
            "status": "draft",
            "body": "# GAP-01\n\nDescription canonique.",
            "gap_state": "planned",
            "target_plateau": ["PL-02"],
            "addressed_by": ["WP-02"],
            "evidenced_by": ["EVID-GAP-01"],
            "closure_criteria": [
                "Qualification hors ligne acceptée",
                "Synchronisation sans perte démontrée",
            ],
        }

        rendered = builder.render_transclusion(obj, "monographie", {})

        self.assertIn("## Pilotage de la fermeture", rendered)
        self.assertIn("**État du gap :** planned", rendered)
        self.assertIn("**Plateau cible :** PL-02", rendered)
        self.assertIn("**Work package :** WP-02", rendered)
        self.assertIn("**Preuve attendue :** EVID-GAP-01", rendered)
        self.assertIn("## Critères de fermeture", rendered)
        self.assertIn("- Qualification hors ligne acceptée", rendered)
        self.assertIn("- Synchronisation sans perte démontrée", rendered)


if __name__ == "__main__":
    unittest.main()
