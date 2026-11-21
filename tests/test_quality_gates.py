import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
UNIT_TEST_ARGS = "-m unittest discover -s tests -v"


def make_target_body(makefile: str, target: str) -> str:
    match = re.search(
        rf"(?m)^{re.escape(target)}:\s*\n(?P<body>(?:\t[^\n]*\n|\n)*)",
        makefile,
    )
    if not match:
        raise AssertionError(f"Cible Makefile absente : {target}")
    return match.group("body")


class QualityGateTests(unittest.TestCase):
    def test_make_check_runs_unit_tests(self):
        makefile = (ROOT / "Makefile").read_text(encoding="utf-8")

        self.assertIn(f"$(PY) {UNIT_TEST_ARGS}", make_target_body(makefile, "check"))

    def test_github_ci_runs_unit_tests(self):
        workflow = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")

        self.assertRegex(
            workflow,
            rf"(?m)^\s+- name: Run unit tests\n\s+run: python3 {re.escape(UNIT_TEST_ARGS)}$",
        )


if __name__ == "__main__":
    unittest.main()
