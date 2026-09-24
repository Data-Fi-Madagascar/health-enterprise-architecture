import unittest

from scripts import build_adr_index, validate_adr


class AdrDiscoveryTests(unittest.TestCase):
    def test_non_adr_change_log_is_excluded_from_adr_discovery(self):
        validated_ids = set(validate_adr.load_all_adrs())
        indexed_ids = {adr["id"] for adr in build_adr_index.load_adrs()}

        self.assertNotIn("adr-change-log", validated_ids)
        self.assertNotIn("adr-change-log", indexed_ids)
        self.assertEqual(10, len(validated_ids))
        self.assertEqual(10, len(indexed_ids))


if __name__ == "__main__":
    unittest.main()
