import unittest

from data.pipelines.structure_d.schema import validate_observable_schema


class ValidateObservableSchemaErrorsTest(unittest.TestCase):
    def _base_entry(self):
        return {
            "dataset_id": "hz",
            "observable": "Hz",
            "values": [70.0, 75.0, 80.0],
            "covariance": [
                [4.0, 0.1, 0.2],
                [0.1, 9.0, 0.3],
                [0.2, 0.3, 16.0],
            ],
            "metadata": {
                "survey": "synthetic",
                "redshift_range": "[0.1, 0.6]",
                "reference": "unit-test",
            },
        }

    def test_covariance_non_square_raises_specific_message(self):
        entry = self._base_entry()
        entry["covariance"] = [
            [4.0, 0.1],
            [0.1, 9.0],
            [0.2, 0.3],
        ]

        with self.assertRaisesRegex(ValueError, "^covariance must be square$"):
            validate_observable_schema(entry)

    def test_covariance_non_positive_diagonal_raises_specific_message(self):
        entry = self._base_entry()
        entry["covariance"] = [
            [4.0, 0.1, 0.2],
            [0.1, 0.0, 0.3],
            [0.2, 0.3, 16.0],
        ]

        with self.assertRaisesRegex(
            ValueError,
            "^covariance diagonal must be strictly positive$",
        ):
            validate_observable_schema(entry)

    def test_metadata_incomplete_raises_specific_message(self):
        entry = self._base_entry()
        entry["metadata"] = {
            "survey": "synthetic",
            "reference": "unit-test",
        }

        with self.assertRaisesRegex(ValueError, "^metadata missing key: redshift_range$"):
            validate_observable_schema(entry)

    def test_covariance_dimension_mismatch_raises_specific_message(self):
        entry = self._base_entry()
        entry["covariance"] = [
            [4.0, 0.1],
            [0.1, 9.0],
        ]

        with self.assertRaisesRegex(
            ValueError,
            "^covariance dimension must match values length$",
        ):
            validate_observable_schema(entry)


if __name__ == "__main__":
    unittest.main()
