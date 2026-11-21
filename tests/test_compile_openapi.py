import unittest
from scripts.compilers import compile_openapi


class EligibilityOpenApiTests(unittest.TestCase):
    def setUp(self):
        profile = next(profile for profile in compile_openapi.collect_profiles()
                       if profile["id"] == "PT-20")
        self.spec = compile_openapi.generate_spec(profile["id"], profile["fm"], profile["body"])

    def test_discovers_all_pt20_fhir_resources(self):
        text = (
            "FHIR R4 Coverage, CoverageEligibilityRequest, "
            "CoverageEligibilityResponse et InsurancePlan"
        )
        self.assertEqual(
            ["Coverage", "CoverageEligibilityRequest", "CoverageEligibilityResponse", "InsurancePlan"],
            compile_openapi.find_fhir_resources(text),
        )

    def test_coverage_search_selects_the_identified_beneficiary(self):
        operation = self.spec["paths"]["/Coverage"]["get"]
        parameters = {parameter["name"]: parameter for parameter in operation["parameters"]}
        self.assertEqual({"identifier", "beneficiary", "patient"}, set(parameters))
        for selector in ("beneficiary", "patient"):
            with self.subTest(selector=selector):
                self.assertEqual("query", parameters[selector]["in"])
                self.assertEqual("string", parameters[selector]["schema"]["type"])
                self.assertEqual("Patient/123", parameters[selector]["example"])
        self.assertEqual("#/components/schemas/Bundle",
                         operation["responses"]["200"]["content"]["application/json"]["schema"]["$ref"])

    def test_eligibility_request_creation_returns_reference_for_correlation(self):
        operation = self.spec["paths"]["/CoverageEligibilityRequest"]["post"]
        self.assertEqual("#/components/schemas/CoverageEligibilityRequest",
                         operation["requestBody"]["content"]["application/json"]["schema"]["$ref"])
        self.assertIn("201", operation["responses"])
        self.assertNotIn("200", operation["responses"])
        location = operation["responses"]["201"]["headers"]["Location"]
        self.assertEqual("string", location["schema"]["type"])
        self.assertTrue(location["required"])
        self.assertEqual("#/components/schemas/CoverageEligibilityRequest",
                         operation["responses"]["201"]["content"]["application/json"]["schema"]["$ref"])

    def test_eligibility_response_search_correlates_the_created_request(self):
        operation = self.spec["paths"]["/CoverageEligibilityResponse"]["get"]
        parameters = {parameter["name"]: parameter for parameter in operation["parameters"]}
        self.assertEqual({"identifier", "request", "patient"}, set(parameters))
        self.assertEqual("query", parameters["request"]["in"])
        self.assertEqual("string", parameters["request"]["schema"]["type"])
        self.assertEqual("CoverageEligibilityRequest/123", parameters["request"]["example"])
        self.assertEqual("#/components/schemas/Bundle",
                         operation["responses"]["200"]["content"]["application/json"]["schema"]["$ref"])

    def test_optional_plan_catalogue_keeps_valid_identifier_and_name_searches(self):
        operation = self.spec["paths"]["/InsurancePlan"]["get"]
        self.assertEqual({"identifier", "name"},
                         {parameter["name"] for parameter in operation["parameters"]})


class AggregateReportOpenApiTests(unittest.TestCase):
    def test_aggregate_profiles_acknowledge_completed_submission_without_creation_location(self):
        profiles = {profile["id"]: profile for profile in compile_openapi.collect_profiles()}
        for profile_id in ("PT-08", "PT-09", "PT-14"):
            with self.subTest(profile=profile_id):
                profile = profiles[profile_id]
                spec = compile_openapi.generate_spec(profile_id, profile["fm"], profile["body"])
                operation = spec["paths"]["/MeasureReport"]["post"]
                self.assertIn("200", operation["responses"])
                self.assertNotIn("201", operation["responses"])
                acknowledgement = operation["responses"]["200"]
                self.assertNotIn("Location", acknowledgement.get("headers", {}))
                self.assertNotIn("content", acknowledgement)
                self.assertEqual("#/components/schemas/MeasureReport",
                                 operation["requestBody"]["content"]["application/json"]["schema"]["$ref"])
                self.assertEqual("%smeasurereport_create" % profile_id.lower().replace("-", ""),
                                 operation["operationId"])

    def test_only_explicit_async_aggregate_transaction_has_accepted_response(self):
        profiles = {profile["id"]: profile for profile in compile_openapi.collect_profiles()}
        for profile_id, expected_successes in (
            ("PT-08", {"200"}), ("PT-09", {"200"}), ("PT-14", {"200", "202"}),
        ):
            with self.subTest(profile=profile_id):
                profile = profiles[profile_id]
                spec = compile_openapi.generate_spec(profile_id, profile["fm"], profile["body"])
                operation = spec["paths"]["/MeasureReport"]["post"]
                self.assertEqual(expected_successes,
                                 {code for code in operation["responses"] if code.startswith("2")})
                self.assertNotIn("303", operation["responses"])

    def test_aggregate_standard_takes_precedence_over_fhir_resource_discovery(self):
        transaction = {
            "name": "Soumission de rapport agrégé", "actors": "Déclarant → Récepteur",
            "ro": "R", "standard": "IHE mADX / FHIR R4 MeasureReport",
        }
        operations, _tag = compile_openapi.map_standard_to_operations(transaction, "PT-08", None)
        path, method, operation, resource = operations[0]
        self.assertEqual(("/MeasureReport", "post", "MeasureReport"), (path, method, resource))
        self.assertIn("200", operation["responses"])
        self.assertNotIn("201", operation["responses"])

    def test_plain_fhir_measure_report_creation_retains_created_location(self):
        transaction = {
            "name": "Création de rapport", "actors": "Client → Serveur",
            "ro": "R", "standard": "FHIR R4 MeasureReport",
        }
        operations, _tag = compile_openapi.map_standard_to_operations(transaction, "PT-08", None)
        path, method, operation, resource = operations[0]
        self.assertEqual(("/MeasureReport", "post", "MeasureReport"), (path, method, resource))
        self.assertIn("201", operation["responses"])
        self.assertNotIn("200", operation["responses"])
        self.assertTrue(operation["responses"]["201"]["headers"]["Location"]["required"])


class OpenApiSchemaCompatibilityTests(unittest.TestCase):
    def test_all_generated_specs_use_openapi_303_resource_type_enums(self):
        def assert_no_const(value, path):
            if isinstance(value, dict):
                self.assertNotIn("const", value, path)
                for key, item in value.items():
                    assert_no_const(item, "%s/%s" % (path, key))
            elif isinstance(value, list):
                for index, item in enumerate(value):
                    assert_no_const(item, "%s/%s" % (path, index))

        for profile in compile_openapi.collect_profiles():
            with self.subTest(profile=profile["id"]):
                spec = compile_openapi.generate_spec(profile["id"], profile["fm"], profile["body"])
                self.assertEqual("3.0.3", spec["openapi"])
                assert_no_const(spec, profile["id"])
                for resource, schema in spec["components"]["schemas"].items():
                    resource_type = schema.get("properties", {}).get("resourceType")
                    if resource_type:
                        self.assertEqual({"type": "string", "enum": [resource]}, resource_type)


if __name__ == "__main__":
    unittest.main()
