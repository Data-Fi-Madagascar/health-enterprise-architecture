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
    def test_financial_protection_retains_full_stream_scope_with_eligibility(self):
        builder = load_builder()
        objects = builder.load_objects()
        rendered = builder.render_partition_traceability(
            objects, builder.id_to_path(objects), str(REPO_ROOT)
        )
        rows = [row for row in rendered.splitlines()
                if row.startswith("| PART-VS-03 |")]
        self.assertEqual(1, len(rows))
        cells = [cell.strip() for cell in rows[0].split("|")[1:-1]]
        self.assertEqual("VS-03", cells[1])
        self.assertEqual(
            {"CAP-07", "CAP-08", "CAP-12", "CAP-13", "CAP-14", "CAP-15", "CAP-16"},
            set(cells[2].split(", ")),
        )
        self.assertEqual({"PRC-07", "PRC-08", "PRC-09"}, set(cells[3].split(", ")))
        self.assertTrue({"ABB-ELIGIBILITE-COUVERTURE", "ABB-IDENTITE-BENEFICIAIRE",
                         "ABB-CONFIANCE-AUTORISATION", "ABB-AUDIT-PROVENANCE"}
                        <= set(cells[5].split(", ")))
        self.assertTrue({"PT-04", "PT-10", "PT-12", "PT-18", "PT-20"}
                        <= set(cells[6].split(", ")))

    def test_assigned_abb_augments_stream_but_preserves_sectoral_scope(self):
        builder = load_builder()
        objects = {
            "partition": obj("PART-VS-03", "architecture-partition",
                             partition_kind="value-stream", applies_to=["VS-03"]),
            "sector": obj("PART-SECTOR", "architecture-partition",
                          partition_kind="sectorielle", applies_to=["VS-03", "CAP-07"]),
            "stream": obj("VS-03", "flux-valeur", applies_to=["CAP-07", "CAP-08"]),
            "eligibility-cap": obj("CAP-07", "capabilite"),
            "shared-cap": obj("CAP-08", "capabilite"),
            "eligibility": obj("ABB-ELIGIBILITE", "architecture-building-block",
                               maps_to=["CAP-07"], partitions=["PART-VS-03", "PART-SECTOR"]),
            "shared": obj("ABB-CONFIANCE", "architecture-building-block", maps_to=["CAP-08"]),
            "eligibility-profile": obj("PT-20", "profil", maps_to=["ABB-ELIGIBILITE"]),
            "shared-profile": obj("PT-10", "profil", maps_to=["ABB-CONFIANCE"]),
        }
        rendered = builder.render_partition_traceability(objects, {}, str(REPO_ROOT))
        rows = {row.split("|")[1].strip(): [cell.strip() for cell in row.split("|")[1:-1]]
                for row in rendered.splitlines() if row.startswith("| PART-")}
        self.assertEqual("CAP-07, CAP-08", rows["PART-VS-03"][2])
        self.assertEqual("ABB-CONFIANCE, ABB-ELIGIBILITE", rows["PART-VS-03"][5])
        self.assertEqual("PT-10, PT-20", rows["PART-VS-03"][6])
        self.assertEqual("CAP-07", rows["PART-SECTOR"][2])
        self.assertEqual("ABB-ELIGIBILITE", rows["PART-SECTOR"][5])
        self.assertEqual("PT-20", rows["PART-SECTOR"][6])

    def test_one_health_renders_complete_surveillance_and_governance_chains(self):
        builder = load_builder()
        objects = builder.load_objects()
        rendered = builder.render_partition_traceability(
            objects, builder.id_to_path(objects), str(REPO_ROOT)
        )
        rows = [
            row for row in rendered.splitlines()
            if row.startswith("| PART-ONE-HEALTH |")
        ]

        self.assertEqual(2, len(rows))
        self.assertEqual(
            {"VS-02", "VS-04"},
            {row.split("|")[2].strip() for row in rows},
        )
        for row in rows:
            with self.subTest(row=row):
                cells = [cell.strip() for cell in row.split("|")[1:-1]]
                self.assertNotEqual("n/a", cells[2])
                self.assertNotEqual("n/a", cells[3])
                self.assertIn("ABB-ECHANGE-MEDIATION", cells[5])
                self.assertIn("ABB-EXPOSITION-DONNEES-ANALYTIQUES", cells[5])
                self.assertIn("PT-15", cells[6])
                self.assertNotIn("ABB-IDENTITE-BENEFICIAIRE", cells[5])
                self.assertNotIn("PT-04", cells[6])

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
