import unittest

import numpy as np

from data.pipelines.structure_d.schema import validate_observable_schema


class ObservableSchemaCovarianceValidationTest(unittest.TestCase):
    def _base_entry(self):
        return {
            "dataset_id": "test_dataset",
            "observable": "Hz",
            "values": [70.0, 75.0],
            "covariance": [[1.0, 0.2], [0.2, 1.5]],
            "metadata": {
                "survey": "synthetic",
                "redshift_range": "[0.0,1.0]",
                "reference": "unit-test",
            },
        }

    def test_rejects_non_symmetric_covariance(self):
        entry = self._base_entry()
        entry["covariance"] = [[1.0, 0.9], [0.2, 1.5]]

        with self.assertRaisesRegex(ValueError, "matrix must be symmetric"):
            validate_observable_schema(entry)

    def test_rejects_non_positive_semidefinite_covariance(self):
        entry = self._base_entry()
        entry["covariance"] = [[1.0, 2.0], [2.0, 1.0]]

        with self.assertRaisesRegex(ValueError, "positive semidefinite"):
            validate_observable_schema(entry)

    def test_accepts_positive_semidefinite_covariance(self):
        entry = self._base_entry()
        entry["covariance"] = np.array([[1.0, 1.0], [1.0, 1.0]])

        normalized = validate_observable_schema(entry)

        self.assertIsNotNone(normalized["covariance"])


if __name__ == "__main__":
    unittest.main()
