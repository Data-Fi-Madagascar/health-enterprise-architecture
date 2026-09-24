import unittest
from scripts.compilers import compile_openapi


class EligibilityOpenApiTests(unittest.TestCase):
    def test_discovers_all_pt20_fhir_resources(self):
        text = (
            "FHIR R4 Coverage, CoverageEligibilityRequest, "
            "CoverageEligibilityResponse et InsurancePlan"
        )
        self.assertEqual(
            ["Coverage", "CoverageEligibilityRequest", "CoverageEligibilityResponse", "InsurancePlan"],
            compile_openapi.find_fhir_resources(text),
        )


if __name__ == "__main__":
    unittest.main()
