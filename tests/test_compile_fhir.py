import json
import os
import unittest
from tempfile import TemporaryDirectory

from scripts.compilers import compile_fhir


def data_object(object_id, resources, fhir_block=None, file_name=None):
    """Construit un objet de données synthétique, au format du compilateur."""
    return {
        "id": object_id,
        "type": "objet-de-donnees",
        "file": file_name or "do-%s.md" % object_id.lower(),
        "body": "# %s\n\nDescription." % object_id,
        "fhir_resources": list(resources),
        "fhir_block": fhir_block,
    }


class FhirVocabularyTests(unittest.TestCase):
    def test_vocabulary_covers_the_r4_core_package(self):
        self.assertEqual(149, len(compile_fhir.FHIR_R4_RESOURCE_TYPES))
        for resource in ("Patient", "Encounter", "Condition", "Medication",
                         "SupplyDelivery", "Claim", "ClaimResponse", "Endpoint",
                         "Provenance", "Binary", "Composition", "Bundle"):
            with self.subTest(resource=resource):
                self.assertIn(resource, compile_fhir.FHIR_R4_RESOURCE_TYPES)

    def test_r5_only_resources_are_absent_from_the_vocabulary(self):
        for resource in ("InventoryItem", "Certificate", "InvoiceItem"):
            with self.subTest(resource=resource):
                self.assertNotIn(resource, compile_fhir.FHIR_R4_RESOURCE_TYPES)

    def test_maturity_level_distinguishes_drafts_from_stable_resources(self):
        self.assertEqual(0, compile_fhir.fmm_level("Invoice"))
        self.assertEqual(0, compile_fhir.fmm_level("MedicationKnowledge"))
        self.assertEqual(3, compile_fhir.fmm_level("Patient".replace("Patient", "Condition")))
        self.assertEqual("N", compile_fhir.fmm_level("Patient"))
        self.assertIsNone(compile_fhir.fmm_level("InventoryItem"))


class DeclarationGateTests(unittest.TestCase):
    def test_accepts_a_valid_declaration(self):
        errors = compile_fhir.check_fhir_declarations(
            [data_object("DO-01", ["Patient"])])
        self.assertEqual([], errors)

    def test_rejects_an_object_without_declaration(self):
        errors = compile_fhir.check_fhir_declarations(
            [data_object("DO-01", [])])
        self.assertEqual(1, len(errors))
        self.assertIn("fhir_resources vide", errors[0][2])

    def test_rejects_a_resource_absent_from_r4(self):
        errors = compile_fhir.check_fhir_declarations(
            [data_object("DO-12", ["InventoryItem"])])
        self.assertEqual(1, len(errors))
        self.assertIn("absente du paquet R4", errors[0][2])

    def test_rejects_a_draft_resource_that_is_not_ready_for_implementation(self):
        errors = compile_fhir.check_fhir_declarations(
            [data_object("DO-16", ["Claim", "Invoice"])])
        self.assertEqual(1, len(errors))
        self.assertIn("FMM 0", errors[0][2])

    def test_rejects_a_duplicate_declaration(self):
        errors = compile_fhir.check_fhir_declarations(
            [data_object("DO-05", ["Encounter", "Encounter"])])
        self.assertEqual(1, len(errors))
        self.assertIn("en double", errors[0][2])

    def test_rejects_a_block_whose_base_is_not_declared(self):
        block = {"base": "http://hl7.org/fhir/StructureDefinition/Patient"}
        errors = compile_fhir.check_fhir_declarations(
            [data_object("DO-01", ["Encounter"], fhir_block=block)])
        self.assertEqual(1, len(errors))
        self.assertIn("absente de fhir_resources", errors[0][2])

    def test_accepts_a_block_whose_base_is_declared(self):
        block = {"base": "http://hl7.org/fhir/StructureDefinition/Patient"}
        errors = compile_fhir.check_fhir_declarations(
            [data_object("DO-01", ["Patient"], fhir_block=block)])
        self.assertEqual([], errors)


class ArtifactGateTests(unittest.TestCase):
    def setUp(self):
        self._tmp = TemporaryDirectory()
        self.output = self._tmp.name

    def tearDown(self):
        self._tmp.cleanup()

    def write_artifact(self, obj, resource, **overrides):
        """Écrit l'artefact d'un objet isolé, sans compiler tout le corpus."""
        sd = compile_fhir.generate_structuredefinition(
            obj, resource, fhir_block=obj["fhir_block"])
        sd.update(overrides)
        path = os.path.join(
            self.output, compile_fhir.artifact_filename(obj["id"], resource))
        with open(path, "w", encoding="utf-8") as handle:
            json.dump(sd, handle)
        return path

    def test_reports_an_artifact_missing_for_a_declared_resource(self):
        errors = compile_fhir.check_fhir_artifacts(
            [data_object("DO-01", ["Patient"])], self.output)
        self.assertEqual(1, len(errors))
        self.assertIn("Artefact FHIR absent", errors[0][2])

    def test_reports_an_artifact_whose_type_does_not_match_the_declaration(self):
        obj = data_object("DO-01", ["Patient"])
        self.write_artifact(obj, "Patient", type="Practitioner")

        errors = compile_fhir.check_fhir_artifacts([obj], self.output)
        self.assertEqual(1, len(errors))
        self.assertIn("porte le type Practitioner", errors[0][2])

    def test_reports_an_orphan_artifact(self):
        obj = data_object("DO-01", ["Patient"])
        self.write_artifact(obj, "Patient")
        orphan = os.path.join(self.output, "hea-do-99-obsolete-sd.json")
        with open(orphan, "w", encoding="utf-8") as handle:
            json.dump({"resourceType": "StructureDefinition", "id": "hea-do-99-obsolete",
                       "url": "x"}, handle)

        errors = compile_fhir.check_fhir_artifacts([obj], self.output)
        self.assertEqual(1, len(errors))
        self.assertIn("sans declaration de ressource", errors[0][2])

    def test_compilation_removes_the_artifacts_of_retired_objects(self):
        compile_fhir.compile_fhir_resources(self.output)
        stale = os.path.join(self.output, "hea-do-02-identifiant-sd.json")
        with open(stale, "w", encoding="utf-8") as handle:
            json.dump({"resourceType": "StructureDefinition"}, handle)
        self.assertTrue(os.path.exists(stale))

        compile_fhir.compile_fhir_resources(self.output)
        self.assertFalse(os.path.exists(stale))

    def test_one_artifact_is_produced_per_declared_resource(self):
        objects = compile_fhir.collect_data_objects()
        with TemporaryDirectory() as output:
            compile_fhir.compile_fhir_resources(output)
            declared = sum(len(obj["fhir_resources"]) for obj in objects)
            produced = [name for name in os.listdir(output)
                        if name.startswith(compile_fhir.GENERATED_PREFIX)
                        and name.endswith("-sd.json")]
            self.assertEqual(declared, len(produced))


class RepositoryProjectionTests(unittest.TestCase):
    """Contrôles sur le corpus réel, pas sur des objets synthétiques."""

    @classmethod
    def setUpClass(cls):
        cls.objects = compile_fhir.collect_data_objects()

    def test_every_data_object_declares_at_least_one_resource(self):
        for obj in self.objects:
            with self.subTest(object=obj["id"]):
                self.assertTrue(obj["fhir_resources"],
                                "%s ne declare aucune ressource FHIR" % obj["id"])

    def test_every_declared_resource_exists_in_r4_and_is_implementable(self):
        for obj in self.objects:
            for resource in obj["fhir_resources"]:
                with self.subTest(object=obj["id"], resource=resource):
                    level = compile_fhir.fmm_level(resource)
                    self.assertIsNotNone(
                        level, "%s declare %s, absente du paquet R4"
                               % (obj["id"], resource))
                    self.assertNotEqual(
                        0, level,
                        "%s declare %s, ressource FMM 0 (non prete pour "
                        "l'implementation)" % (obj["id"], resource))

    def test_no_object_declares_the_same_resource_twice(self):
        for obj in self.objects:
            with self.subTest(object=obj["id"]):
                self.assertEqual(len(obj["fhir_resources"]),
                                 len(set(obj["fhir_resources"])))

    def test_corpus_passes_the_declaration_gate(self):
        self.assertEqual([], compile_fhir.check_fhir_declarations(self.objects))

    def test_each_declared_resource_maps_to_a_distinct_artifact_name(self):
        names = {}
        for obj in self.objects:
            for resource in obj["fhir_resources"]:
                name = compile_fhir.artifact_filename(obj["id"], resource)
                with self.subTest(object=obj["id"], resource=resource):
                    self.assertNotIn(name, names)
                    names[name] = (obj["id"], resource)
        self.assertEqual(36, len(names))

    def test_patient_profile_is_derived_from_its_fhir_block(self):
        patient = next(obj for obj in self.objects if obj["id"] == "DO-01")
        self.assertEqual("Patient", patient["fhir_block"]["base"].split("/")[-1])

        sd = compile_fhir.generate_structuredefinition(
            patient, "Patient", fhir_block=patient["fhir_block"])
        self.assertEqual("http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient",
                         sd["baseDefinition"])
        slices = [element.get("sliceName")
                  for element in sd["differential"]["element"]
                  if element.get("sliceName")]
        self.assertIn("NIN", slices)
        self.assertIn("provisional", slices)


if __name__ == "__main__":
    unittest.main()
