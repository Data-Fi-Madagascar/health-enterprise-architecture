import importlib.util
from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
BUILDER_PATH = REPO_ROOT / "scripts" / "build_wrappers.py"
VIEW_DIR = REPO_ROOT / "04_architecture-repository" / "08_views" / "togaf"


def load_builder():
    spec = importlib.util.spec_from_file_location("build_wrappers", BUILDER_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def obj(object_id, object_type, **fields):
    defaults = {
        "id": object_id,
        "type": object_type,
        "title": object_id,
        "owner": "DNS",
        "rel": "04_architecture-repository/test/%s.md" % object_id.lower(),
        "between": [],
        "gap_state": "",
        "target_plateau": [],
        "addressed_by": [],
        "evidenced_by": [],
        "closure_criteria": [],
        "related": [],
    }
    defaults.update(fields)
    return defaults


class GapClosureRoadmapTests(unittest.TestCase):
    def test_renders_linked_closure_chains_in_natural_gap_order(self):
        builder = load_builder()
        objects = {
            "gap-10": obj(
                "GAP-10", "gap", title="Gap dix", gap_state="identified",
                between=["PL-02", "PL-10"], target_plateau=["PL-10"],
                addressed_by=["WP-10"], evidenced_by=["EVID-GAP-10"],
                closure_criteria=["Critère dix"], related=["CAP-10"],
            ),
            "evidence-2": obj("EVID-GAP-02", "evidence"),
            "plateau-10": obj("PL-10", "plateau"),
            "work-2": obj("WP-02", "work-package"),
            "gap-2": obj(
                "GAP-02", "gap", title="Gap deux | prioritaire",
                owner="Direction | Architecture", gap_state="planned",
                between=["PL-01", "PL-02"], target_plateau=["PL-02"],
                addressed_by=["WP-02"], evidenced_by=["EVID-GAP-02"],
                closure_criteria=["Critère A", "Critère B"],
                related=["PL-01", "PL-02", "CAP-02"],
            ),
            "plateau-1": obj("PL-01", "plateau"),
            "capability-2": obj("CAP-02", "capabilite"),
            "plateau-2": obj("PL-02", "plateau"),
            "work-10": obj("WP-10", "work-package"),
            "evidence-10": obj("EVID-GAP-10", "evidence"),
            "capability-10": obj("CAP-10", "capabilite"),
        }
        path_by_id = {item["id"]: item["rel"] for item in objects.values()}

        rendered = builder.render_gap_closure_roadmap(
            objects, path_by_id, str(VIEW_DIR)
        )

        rows = [line for line in rendered.splitlines() if line.startswith("| [GAP-")]
        self.assertEqual(2, len(rows))
        self.assertIn("[GAP-02]", rows[0])
        self.assertIn("[GAP-10]", rows[1])
        self.assertIn("[PL-01]", rows[0])
        self.assertIn("[PL-02]", rows[0])
        self.assertIn("[WP-02]", rows[0])
        self.assertIn("[CAP-02]", rows[0])
        self.assertIn("[EVID-GAP-02]", rows[0])
        self.assertIn("planned", rows[0])
        self.assertIn("Direction \\| Architecture", rows[0])
        self.assertIn("Critère A<br>Critère B", rows[0])
        self.assertNotIn("CAP-10", rows[0])
        self.assertIn("../../test/gap-02.md", rows[0])

    def test_real_repository_renders_each_approved_closure_chain(self):
        builder = load_builder()
        objects = builder.load_objects()

        rendered = builder.render_gap_closure_roadmap(
            objects, builder.id_to_path(objects), str(VIEW_DIR)
        )

        rows = {
            gap_id: next(
                line for line in rendered.splitlines()
                if line.startswith("| [%s]" % gap_id)
            )
            for gap_id in ("GAP-01", "GAP-02", "GAP-03")
        }
        expected_ids = {
            "GAP-01": {"PL-02", "WP-02", "EVID-GAP-01-QUALIFICATION-OFFLINE"},
            "GAP-02": {
                "PL-03", "WP-06", "WP-07",
                "EVID-GAP-02-INTEROPERABILITE-ETENDUE",
            },
            "GAP-03": {"PL-01", "WP-01", "EVID-GAP-03-CADRE-LEGAL"},
        }
        for gap_id, identifiers in expected_ids.items():
            with self.subTest(gap_id=gap_id):
                self.assertIn("planned", rows[gap_id])
                for identifier in identifiers:
                    self.assertIn("[%s]" % identifier, rows[gap_id])


if __name__ == "__main__":
    unittest.main()
