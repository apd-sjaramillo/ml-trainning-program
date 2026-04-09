import unittest

from report_runner import run
from report_utils_everything import load_rows
from report_utils_everything import make_everything


class TestVeryLongLegacyFlow(unittest.TestCase):
    def test_default_run_contains_expected_sections_and_known_names_and_totals_are_consistent_and_the_report_is_not_empty_and_the_blob_contains_summary_numbers(self):
        result = run()
        self.assertTrue(result.startswith("UTILIZATION REPORT"))
        self.assertIn("Summary:", result)
        self.assertIn("TOP CLIENTS", result)
        self.assertIn("Apex Health", result)
        self.assertIn("Blue Ocean", result)
        self.assertIn("Northwind", result)
        self.assertIn("Ana", result)
        self.assertIn("Luis", result)
        self.assertIn("Mia", result)
        self.assertIn("Joel", result)
        self.assertIn("Sara", result)
        self.assertIn("Ivan", result)
        self.assertIn("Nora", result)
        self.assertIn("people=7", result)
        self.assertIn("hours=210", result)
        self.assertIn("capacity=280", result)
        self.assertIn("billable_hours=179", result)
        self.assertIn("non_billable_hours=31", result)
        self.assertTrue(len(result.splitlines()) > 10)

    def test_filtered_country_and_department_and_mode_and_sorting_still_work_even_though_everything_is_packed_into_big_functions(self):
        rows = load_rows()
        data = make_everything(
            rows,
            minimum_hours=20,
            country_filter="co",
            department_filter="data",
            include_non_billable=True,
            mode="aggressive",
            sort_by="utilization",
        )
        self.assertEqual(data["summary"]["people"], 1)
        self.assertEqual(data["summary"]["hours"], 36)
        self.assertEqual(data["summary"]["capacity"], 40)
        self.assertEqual(data["summary"]["billable_hours"], 36)
        self.assertEqual(data["summary"]["non_billable_hours"], 0)
        self.assertEqual(data["rows"][0]["consultant"], "Ana")
        self.assertEqual(data["rows"][0]["band"], "excellent")
        self.assertEqual(data["clients"][0]["client"], "Apex Health")
        self.assertEqual(data["countries"]["co"], 1)
        self.assertEqual(len(data["departments"]["data"]), 1)

    def test_excluding_non_billable_changes_summary_totals_and_people_count_and_produces_a_stable_report_shape(self):
        rows = load_rows()
        data = make_everything(rows, include_non_billable=False)
        report = run(include_non_billable=False)
        self.assertEqual(data["summary"]["people"], 5)
        self.assertEqual(data["summary"]["hours"], 179)
        self.assertEqual(data["summary"]["billable_hours"], 179)
        self.assertEqual(data["summary"]["non_billable_hours"], 0)
        self.assertNotIn("Mia", report)
        self.assertNotIn("Nora", report)
        self.assertIn("Luis", report)
        self.assertIn("Ivan", report)


if __name__ == "__main__":
    unittest.main()
