import csv
import json
import os
import shutil
import tempfile
import unittest

import numpy as np
import pandas as pd

from data.pipelines.structure_d import make_example_data, run_all
from data.pipelines.structure_d.data_access import load_active_datasets


class StructureDDefaultRegressionTest(unittest.TestCase):
    def setUp(self):
        self.generated_paths = [
            os.path.join(run_all.BASE_DIR, "data", "inputs", "structure_d", "Hz.csv"),
            os.path.join(run_all.BASE_DIR, "data", "inputs", "structure_d", "fsigma8.csv"),
            os.path.join(run_all.RESULTS, "model_comparison.csv"),
            os.path.join(run_all.RESULTS, "reproduction_contract.json"),
            os.path.join(run_all.RESULTS, "bayes_evidence_bic_proxy.csv"),
            os.path.join(run_all.RESULTS, "bayes_factor_interpretation.csv"),
            os.path.join(run_all.RESULTS, "degeneracy_corr_bin_00.csv"),
            os.path.join(run_all.RESULTS, "degeneracy_corr_bin_01.csv"),
            os.path.join(run_all.RESULTS, "degeneracy_corr_bin_02.csv"),
            os.path.join(run_all.RESULTS, "degeneracy_corr_bin_04.csv"),
            os.path.join(run_all.RESULTS, "degeneracy_corr_bin_05.csv"),
            os.path.join(run_all.RESULTS, "dominance_by_z.csv"),
            os.path.join(run_all.RESULTS, "sensitivity_long.csv"),
            os.path.join(run_all.RESULTS, "figs"),
        ]

    def tearDown(self):
        for path in self.generated_paths:
            if os.path.isdir(path):
                shutil.rmtree(path)
            elif os.path.exists(path):
                os.remove(path)

    def test_structure_d_default_writes_non_empty_covariance_usage(self):
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
        self.assertIsNone(
            contract.get("bayes_mode"),
            "reproduction contract must set bayes_mode to null when --bayes is disabled",
        )

    def test_structure_d_bayes_bic_proxy_writes_mode_specific_output(self):
        make_example_data.main(seed=42)
        run_all.main(profile_name="structure_d_default", bayes=True, bayes_mode="bic_proxy")

        evidence_path = os.path.join(run_all.RESULTS, "bayes_evidence_bic_proxy.csv")
        self.assertTrue(os.path.exists(evidence_path), "bayes_evidence_bic_proxy.csv was not generated")

        contract_path = os.path.join(run_all.RESULTS, "reproduction_contract.json")
        with open(contract_path, "r", encoding="utf-8") as fp:
            contract = json.load(fp)

        self.assertEqual(contract.get("bayes_mode"), "bic_proxy")


class StructureDCovariancePolicyRegressionTest(unittest.TestCase):
    def test_mock_real_like_profile_generates_required_artifacts(self):
        generated_paths = [
            os.path.join(run_all.RESULTS, "model_comparison.csv"),
            os.path.join(run_all.RESULTS, "covariance_usage.csv"),
            os.path.join(run_all.RESULTS, "error_mode_usage.csv"),
            os.path.join(run_all.RESULTS, "rll_regime_summary.csv"),
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

        make_example_data.main(seed=123)
        run_all.main(profile_name="structure_d_default")

        for filename in run_all.REQUIRED_OUTPUTS:
            output_path = os.path.join(run_all.RESULTS, filename)
            self.assertTrue(
                os.path.exists(output_path),
                f"required output {filename} was not generated for mock real-like profile",
            )

    def test_covariance_policy_diagonal_only_converts_covariance_to_sigma(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            data_dir = os.path.join(temp_dir, "data")
            results_dir = os.path.join(temp_dir, "results")
            os.makedirs(data_dir, exist_ok=True)
            os.makedirs(results_dir, exist_ok=True)

            hz_path = os.path.join(data_dir, "hz_cov.csv")
            hz_cov_path = os.path.join(data_dir, "hz_cov_matrix.csv")
            fs8_path = os.path.join(data_dir, "fsigma8.csv")
            cfg_path = os.path.join(temp_dir, "config.json")

            hz_df = pd.DataFrame(
                {
                    "z": [0.1, 0.3, 0.6],
                    "Hz": [72.0, 78.5, 91.3],
                }
            )
            hz_df.to_csv(hz_path, index=False)

            covariance = np.array(
                [
                    [4.0, 0.8, 0.2],
                    [0.8, 9.0, 0.5],
                    [0.2, 0.5, 16.0],
                ]
            )
            np.savetxt(hz_cov_path, covariance, delimiter=",")

            fs8_df = pd.DataFrame(
                {
                    "z": [0.2, 0.5, 0.9],
                    "fs8": [0.45, 0.42, 0.38],
                    "sigma": [0.03, 0.04, 0.05],
                }
            )
            fs8_df.to_csv(fs8_path, index=False)

            config = {
                "default_profile": "diag_policy",
                "profiles": {
                    "diag_policy": {
                        "run_name": "diag_policy",
                        "active_datasets": ["hz", "fsigma8"],
                    }
                },
                "datasets": {
                    "hz": {
                        "format": "csv",
                        "path": hz_path,
                        "observable": "Hz",
                        "error_model": "covariance",
                        "columns": {
                            "z": "z",
                            "value": "Hz",
                            "covariance": None,
                        },
                        "covariance_path": hz_cov_path,
                        "metadata": {
                            "survey": "synthetic",
                            "redshift_range": "[0.1,0.6]",
                            "reference": "unit-test",
                        },
                    },
                    "fsigma8": {
                        "format": "csv",
                        "path": fs8_path,
                        "observable": "fs8",
                        "error_model": "errors",
                        "columns": {
                            "z": "z",
                            "value": "fs8",
                            "error": "sigma",
                        },
                        "metadata": {
                            "survey": "synthetic",
                            "redshift_range": "[0.2,0.9]",
                            "reference": "unit-test",
                        },
                    },
                },
            }
            with open(cfg_path, "w", encoding="utf-8") as fp:
                json.dump(config, fp)

            cfg_meta, datasets = load_active_datasets(cfg_path, profile_name="diag_policy")
            effective_policy = run_all._apply_covariance_policy(datasets, "diagonal_only")
            self.assertEqual(effective_policy, "diagonal_only")

            hz_entry = datasets["hz"]
            self.assertIsNone(hz_entry["covariance"])
            np.testing.assert_allclose(hz_entry["errors"], np.sqrt(np.diag(covariance)))

            _, _, out_cov, _ = run_all.run_classic_metrics(cfg_meta, datasets, effective_policy)
            self.addCleanup(os.remove, out_cov)
            self.addCleanup(os.remove, os.path.join(run_all.RESULTS, "model_comparison.csv"))

            cov_usage = pd.read_csv(out_cov)
            hz_row = cov_usage[cov_usage["dataset_id"] == "hz"].iloc[0]
            self.assertEqual(hz_row["covariance_mode"], "diagonal")
            self.assertFalse(bool(hz_row["has_full_covariance"]))
            self.assertTrue(bool(hz_row["has_diagonal_sigma"]))

    def test_covariance_policy_full_required_raises_for_dataset_without_full_matrix(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            data_dir = os.path.join(temp_dir, "data")
            os.makedirs(data_dir, exist_ok=True)

            hz_path = os.path.join(data_dir, "hz.csv")
            fs8_path = os.path.join(data_dir, "fsigma8.csv")
            cfg_path = os.path.join(temp_dir, "config.json")

            pd.DataFrame(
                {
                    "z": [0.1, 0.2, 0.4],
                    "Hz": [70.0, 76.0, 85.0],
                    "sigma": [2.0, 2.5, 3.0],
                }
            ).to_csv(hz_path, index=False)
            pd.DataFrame(
                {
                    "z": [0.1, 0.4, 0.8],
                    "fs8": [0.48, 0.44, 0.39],
                    "sigma": [0.03, 0.04, 0.05],
                }
            ).to_csv(fs8_path, index=False)

            config = {
                "default_profile": "full_required_policy",
                "profiles": {
                    "full_required_policy": {
                        "run_name": "full_required_policy",
                        "active_datasets": ["hz", "fsigma8"],
                    }
                },
                "datasets": {
                    "hz": {
                        "format": "csv",
                        "path": hz_path,
                        "observable": "Hz",
                        "error_model": "errors",
                        "columns": {
                            "z": "z",
                            "value": "Hz",
                            "error": "sigma",
                        },
                        "metadata": {
                            "survey": "synthetic",
                            "redshift_range": "[0.1,0.4]",
                            "reference": "unit-test",
                        },
                    },
                    "fsigma8": {
                        "format": "csv",
                        "path": fs8_path,
                        "observable": "fs8",
                        "error_model": "errors",
                        "columns": {
                            "z": "z",
                            "value": "fs8",
                            "error": "sigma",
                        },
                        "metadata": {
                            "survey": "synthetic",
                            "redshift_range": "[0.1,0.8]",
                            "reference": "unit-test",
                        },
                    },
                },
            }
            with open(cfg_path, "w", encoding="utf-8") as fp:
                json.dump(config, fp)

            with self.assertRaisesRegex(ValueError, "full_required"):
                run_all.main(
                    config_path=cfg_path,
                    profile_name="full_required_policy",
                    covariance_policy="full_required",
                )


class StructureDCovariancePolicyRegressionTest(unittest.TestCase):
    def test_mock_real_like_profile_generates_required_artifacts(self):
        generated_paths = [
            os.path.join(run_all.RESULTS, "model_comparison.csv"),
            os.path.join(run_all.RESULTS, "covariance_usage.csv"),
            os.path.join(run_all.RESULTS, "error_mode_usage.csv"),
            os.path.join(run_all.RESULTS, "rll_regime_summary.csv"),
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

        make_example_data.main(seed=123)
        run_all.main(profile_name="structure_d_default")

        for filename in run_all.REQUIRED_OUTPUTS:
            output_path = os.path.join(run_all.RESULTS, filename)
            self.assertTrue(
                os.path.exists(output_path),
                f"required output {filename} was not generated for mock real-like profile",
            )

    def test_covariance_policy_diagonal_only_converts_covariance_to_sigma(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            data_dir = os.path.join(temp_dir, "data")
            results_dir = os.path.join(temp_dir, "results")
            os.makedirs(data_dir, exist_ok=True)
            os.makedirs(results_dir, exist_ok=True)

            hz_path = os.path.join(data_dir, "hz_cov.csv")
            hz_cov_path = os.path.join(data_dir, "hz_cov_matrix.csv")
            fs8_path = os.path.join(data_dir, "fsigma8.csv")
            cfg_path = os.path.join(temp_dir, "config.json")

            hz_df = pd.DataFrame(
                {
                    "z": [0.1, 0.3, 0.6],
                    "Hz": [72.0, 78.5, 91.3],
                }
            )
            hz_df.to_csv(hz_path, index=False)

            covariance = np.array(
                [
                    [4.0, 0.8, 0.2],
                    [0.8, 9.0, 0.5],
                    [0.2, 0.5, 16.0],
                ]
            )
            np.savetxt(hz_cov_path, covariance, delimiter=",")

            fs8_df = pd.DataFrame(
                {
                    "z": [0.2, 0.5, 0.9],
                    "fs8": [0.45, 0.42, 0.38],
                    "sigma": [0.03, 0.04, 0.05],
                }
            )
            fs8_df.to_csv(fs8_path, index=False)

            config = {
                "default_profile": "diag_policy",
                "profiles": {
                    "diag_policy": {
                        "run_name": "diag_policy",
                        "active_datasets": ["hz", "fsigma8"],
                    }
                },
                "datasets": {
                    "hz": {
                        "format": "csv",
                        "path": hz_path,
                        "observable": "Hz",
                        "error_model": "covariance",
                        "columns": {
                            "z": "z",
                            "value": "Hz",
                            "covariance": None,
                        },
                        "covariance_path": hz_cov_path,
                        "metadata": {
                            "survey": "synthetic",
                            "redshift_range": "[0.1,0.6]",
                            "reference": "unit-test",
                        },
                    },
                    "fsigma8": {
                        "format": "csv",
                        "path": fs8_path,
                        "observable": "fs8",
                        "error_model": "errors",
                        "columns": {
                            "z": "z",
                            "value": "fs8",
                            "error": "sigma",
                        },
                        "metadata": {
                            "survey": "synthetic",
                            "redshift_range": "[0.2,0.9]",
                            "reference": "unit-test",
                        },
                    },
                },
            }
            with open(cfg_path, "w", encoding="utf-8") as fp:
                json.dump(config, fp)

            cfg_meta, datasets = load_active_datasets(cfg_path, profile_name="diag_policy")
            effective_policy = run_all._apply_covariance_policy(datasets, "diagonal_only")
            self.assertEqual(effective_policy, "diagonal_only")

            hz_entry = datasets["hz"]
            self.assertIsNone(hz_entry["covariance"])
            np.testing.assert_allclose(hz_entry["errors"], np.sqrt(np.diag(covariance)))

            _, _, out_cov, _ = run_all.run_classic_metrics(cfg_meta, datasets, effective_policy)
            self.addCleanup(os.remove, out_cov)
            self.addCleanup(os.remove, os.path.join(run_all.RESULTS, "model_comparison.csv"))

            cov_usage = pd.read_csv(out_cov)
            hz_row = cov_usage[cov_usage["dataset_id"] == "hz"].iloc[0]
            self.assertEqual(hz_row["covariance_mode"], "diagonal")
            self.assertFalse(bool(hz_row["has_full_covariance"]))
            self.assertTrue(bool(hz_row["has_diagonal_sigma"]))

    def test_covariance_policy_full_required_raises_for_dataset_without_full_matrix(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            data_dir = os.path.join(temp_dir, "data")
            os.makedirs(data_dir, exist_ok=True)

            hz_path = os.path.join(data_dir, "hz.csv")
            fs8_path = os.path.join(data_dir, "fsigma8.csv")
            cfg_path = os.path.join(temp_dir, "config.json")

            pd.DataFrame(
                {
                    "z": [0.1, 0.2, 0.4],
                    "Hz": [70.0, 76.0, 85.0],
                    "sigma": [2.0, 2.5, 3.0],
                }
            ).to_csv(hz_path, index=False)
            pd.DataFrame(
                {
                    "z": [0.1, 0.4, 0.8],
                    "fs8": [0.48, 0.44, 0.39],
                    "sigma": [0.03, 0.04, 0.05],
                }
            ).to_csv(fs8_path, index=False)

            config = {
                "default_profile": "full_required_policy",
                "profiles": {
                    "full_required_policy": {
                        "run_name": "full_required_policy",
                        "active_datasets": ["hz", "fsigma8"],
                    }
                },
                "datasets": {
                    "hz": {
                        "format": "csv",
                        "path": hz_path,
                        "observable": "Hz",
                        "error_model": "errors",
                        "columns": {
                            "z": "z",
                            "value": "Hz",
                            "error": "sigma",
                        },
                        "metadata": {
                            "survey": "synthetic",
                            "redshift_range": "[0.1,0.4]",
                            "reference": "unit-test",
                        },
                    },
                    "fsigma8": {
                        "format": "csv",
                        "path": fs8_path,
                        "observable": "fs8",
                        "error_model": "errors",
                        "columns": {
                            "z": "z",
                            "value": "fs8",
                            "error": "sigma",
                        },
                        "metadata": {
                            "survey": "synthetic",
                            "redshift_range": "[0.1,0.8]",
                            "reference": "unit-test",
                        },
                    },
                },
            }
            with open(cfg_path, "w", encoding="utf-8") as fp:
                json.dump(config, fp)

            with self.assertRaisesRegex(ValueError, "full_required"):
                run_all.main(
                    config_path=cfg_path,
                    profile_name="full_required_policy",
                    covariance_policy="full_required",
                )


if __name__ == "__main__":
    unittest.main()
