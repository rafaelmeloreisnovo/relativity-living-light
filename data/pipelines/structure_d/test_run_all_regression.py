import csv
import json
import os
import shutil
import unittest

from data.pipelines.structure_d import make_example_data, run_all


class StructureDDefaultRegressionTest(unittest.TestCase):
    def test_structure_d_default_writes_non_empty_covariance_usage(self):
        generated_paths = [
            os.path.join(run_all.BASE_DIR, "data", "inputs", "structure_d", "Hz.csv"),
            os.path.join(run_all.BASE_DIR, "data", "inputs", "structure_d", "fsigma8.csv"),
            os.path.join(run_all.RESULTS, "model_comparison.csv"),
            os.path.join(run_all.RESULTS, "reproduction_contract.json"),
            os.path.join(run_all.RESULTS, "degeneracy_corr_bin_00.csv"),
            os.path.join(run_all.RESULTS, "degeneracy_corr_bin_01.csv"),
            os.path.join(run_all.RESULTS, "degeneracy_corr_bin_02.csv"),
            os.path.join(run_all.RESULTS, "degeneracy_corr_bin_04.csv"),
            os.path.join(run_all.RESULTS, "degeneracy_corr_bin_05.csv"),
            os.path.join(run_all.RESULTS, "dominance_by_z.csv"),
            os.path.join(run_all.RESULTS, "sensitivity_long.csv"),
            os.path.join(run_all.RESULTS, "figs"),
        ]

        def _cleanup_generated_files():
            for path in generated_paths:
                if os.path.isdir(path):
                    shutil.rmtree(path)
                elif os.path.exists(path):
                    os.remove(path)

        self.addCleanup(_cleanup_generated_files)

        make_example_data.main(seed=42)
        run_all.main(profile_name="structure_d_default")

        cov_path = os.path.join(run_all.RESULTS, "covariance_usage.csv")
        self.assertTrue(os.path.exists(cov_path), "covariance_usage.csv was not generated")

        with open(cov_path, "r", encoding="utf-8", newline="") as fp:
            rows = list(csv.DictReader(fp))

        self.assertGreater(
            len(rows),
            0,
            "expected at least one covariance usage row for structure_d_default",
        )

        contract_path = os.path.join(run_all.RESULTS, "reproduction_contract.json")
        with open(contract_path, "r", encoding="utf-8") as fp:
            contract = json.load(fp)

        self.assertTrue(
            contract.get("covariance_usage_non_empty"),
            "reproduction contract must register covariance_usage_non_empty=true",
        )


if __name__ == "__main__":
    unittest.main()
