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


def obj(object_id, object_type, **relations):
    defaults = {
        "id": object_id,
        "type": object_type,
        "rel": "04_architecture-repository/%s.md" % object_id.lower(),
        "applies_to": [],
        "related": [],
        "maps_to": [],
        "accesses": [],
        "partitions": [],
    }
    defaults.update(relations)
    return defaults


class PartitionTraceabilityViewTests(unittest.TestCase):
    def test_renders_partition_to_solution_chain_from_relations(self):
        builder = load_builder()
        objects = {
            "partition": obj(
                "PART-VS-01", "architecture-partition", applies_to=["VS-01"]
            ),
            "value-stream": obj(
                "VS-01",
                "flux-valeur",
                applies_to=["CAP-01"],
                related=["PRC-01"],
            ),
            "capability": obj("CAP-01", "capabilite"),
            "process": obj(
                "PRC-01",
                "processus-metier",
                applies_to=["CAP-01"],
                related=["VS-01"],
                accesses=["DO-01"],
            ),
            "data": obj("DO-01", "objet-de-donnees"),
            "abb": obj(
                "ABB-EXEMPLE",
                "architecture-building-block",
                maps_to=["CAP-01"],
                partitions=["PART-VS-01"],
            ),
            "profile": obj(
                "PT-01", "profil", maps_to=["ABB-EXEMPLE", "CAP-01"]
            ),
        }
        path_by_id = {
            item["id"]: item["rel"] for item in objects.values()
        }

        rendered = builder.render_partition_traceability(
            objects, path_by_id, str(REPO_ROOT)
        )

        for expected_id in (
            "PART-VS-01",
            "VS-01",
            "CAP-01",
            "PRC-01",
            "DO-01",
            "ABB-EXEMPLE",
            "PT-01",
        ):
            self.assertIn(expected_id, rendered)
        self.assertEqual(1, rendered.count("| PART-VS-01 |"))


if __name__ == "__main__":
    unittest.main()
