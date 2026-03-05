import csv
import json
import os
import shutil
import tempfile
import unittest
from unittest import mock

import numpy as np
import pandas as pd

from data.pipelines.structure_d import make_example_data, run_all
from data.pipelines.structure_d.data_access import load_active_datasets
from to_Add.RAFAELIA_COSMO_STRUCTURE_D.rll_pipeline import run_all as compat_run_all


class StructureDDefaultRegressionTest(unittest.TestCase):
    def setUp(self):
        self.generated_paths = [
            os.path.join(run_all.BASE_DIR, "data", "inputs", "structure_d", "Hz.csv"),
            os.path.join(run_all.BASE_DIR, "data", "inputs", "structure_d", "fsigma8.csv"),
            os.path.join(run_all.BASE_DIR, "data", "inputs", "structure_d", "mock_data_contract.json"),
            os.path.join(run_all.RESULTS, "model_comparison.csv"),
            os.path.join(run_all.RESULTS, "covariance_usage.csv"),
            os.path.join(run_all.RESULTS, "rll_regime_summary.csv"),
            os.path.join(run_all.RESULTS, "reproduction_contract.json"),
            os.path.join(run_all.RESULTS, "bayes_evidence_bic_proxy.csv"),
            os.path.join(run_all.RESULTS, "bayes_evidence_inference.csv"),
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
        allowed_covariance_modes = {"full", "diagonal"}
        for row in rows:
            self.assertIn(
                row["covariance_mode"],
                allowed_covariance_modes,
                "covariance_mode must be one of {full, diagonal}",
            )

        contract_path = os.path.join(run_all.RESULTS, "reproduction_contract.json")
        with open(contract_path, "r", encoding="utf-8") as fp:
            contract = json.load(fp)

        self.assertEqual(
            contract.get("mock_data_contract"),
            "data/inputs/structure_d/mock_data_contract.json",
        )
        self.assertTrue(
            os.path.exists(
                os.path.join(run_all.BASE_DIR, contract.get("mock_data_contract"))
            ),
            "mock_data_contract.json must exist when using generated example data",
        )

        self.assertTrue(
            contract.get("covariance_usage_non_empty"),
            "reproduction contract must register covariance_usage_non_empty=true",
        )
        self.assertIsNone(
            contract.get("bayes_mode"),
            "reproduction contract must set bayes_mode to null when --bayes is disabled",
        )
        self.assertIn("dirty_worktree", contract)
        self.assertIn("git_commit", contract)

    def test_structure_d_bayes_bic_proxy_writes_mode_specific_output(self):
        make_example_data.main(seed=42)
        run_all.main(profile_name="structure_d_default", bayes=True, bayes_mode="bic_proxy")

        evidence_path = os.path.join(run_all.RESULTS, "bayes_evidence_bic_proxy.csv")
        self.assertTrue(os.path.exists(evidence_path), "bayes_evidence_bic_proxy.csv was not generated")
        evidence_df = pd.read_csv(evidence_path)

        self.assertIn("bic_proxy", evidence_df["source"].unique())
        self.assertIn("log_evidence_std_defined", evidence_df.columns)
        self.assertFalse(evidence_df["log_evidence_std_defined"].any())

        contract_path = os.path.join(run_all.RESULTS, "reproduction_contract.json")
        with open(contract_path, "r", encoding="utf-8") as fp:
            contract = json.load(fp)

        self.assertEqual(contract.get("bayes_mode"), "bic_proxy")
        self.assertIn("bayes_factor_interpretation_contract", contract)

    def test_structure_d_bayes_contract_tracks_optional_outputs(self):
        make_example_data.main(seed=42)
        run_all.main(profile_name="structure_d_default", bayes=True)

        contract_path = os.path.join(run_all.RESULTS, "reproduction_contract.json")
        with open(contract_path, "r", encoding="utf-8") as fp:
            contract = json.load(fp)

        self.assertTrue(contract.get("bayes_enabled"))
        self.assertEqual(contract.get("bayes_mode"), "bic_proxy")

        optional_outputs = {entry["file"]: bool(entry["produced"]) for entry in contract.get("optional_outputs", [])}
        self.assertEqual(optional_outputs.get("bayes_evidence_bic_proxy.csv"), True)
        self.assertEqual(optional_outputs.get("bayes_factor_interpretation.csv"), True)
        self.assertEqual(optional_outputs.get("bayes_evidence_inference.csv"), False)

        for filename, was_produced in optional_outputs.items():
            path = os.path.join(run_all.RESULTS, filename)
            self.assertEqual(
                os.path.exists(path),
                was_produced,
                f"contract produced flag mismatch for optional artifact {filename}",
            )



    def test_structure_d_bayes_inference_uses_inference_routines_and_persists_metadata(self):
        make_example_data.main(seed=42)

        fake_lcdm = {
            "row": {
                "model": "LCDM",
                "logZ": -10.0,
                "logZ_err": 0.5,
                "seed": 7,
                "nwalkers": 16,
                "nsteps": 100,
                "nlive": 50,
            }
        }
        fake_rll = {
            "row": {
                "model": "RLL_like+AGN",
                "logZ": -9.0,
                "logZ_err": 0.7,
                "seed": 7,
                "nwalkers": 16,
                "nsteps": 100,
                "nlive": 50,
            }
        }

        with mock.patch.object(run_all, "run_lcdm_bayes", return_value=fake_lcdm) as lcdm_mock, mock.patch.object(
            run_all,
            "run_rll_like_agn_bayes",
            return_value=fake_rll,
        ) as rll_mock:
            run_all.main(
                profile_name="structure_d_default",
                bayes=True,
                bayes_mode="inference",
                bayes_seed=7,
                bayes_nwalkers=16,
                bayes_nsteps=100,
                bayes_nlive=50,
            )

        self.assertEqual(lcdm_mock.call_count, 1)
        self.assertEqual(rll_mock.call_count, 1)

        evidence_path = os.path.join(run_all.RESULTS, "bayes_evidence_inference.csv")
        self.assertTrue(os.path.exists(evidence_path), "bayes_evidence_inference.csv was not generated")

        contract_path = os.path.join(run_all.RESULTS, "reproduction_contract.json")
        with open(contract_path, "r", encoding="utf-8") as fp:
            contract = json.load(fp)

        self.assertEqual(contract.get("bayes_mode"), "inference")
        self.assertEqual(
            contract.get("bayes_runtime_metadata"),
            {"seed": 7, "nwalkers": 16, "nsteps": 100, "nlive": 50},
        )

class StructureDCovariancePolicyRegressionTest(unittest.TestCase):
    def test_run_classic_metrics_supports_lookup_fallback_by_normalized_observable(self):
        datasets = {
            "hz_renamed": {
                "dataset_id": "hz_renamed",
                "observable": " H(z) ",
                "z": np.array([0.1, 0.3, 0.5]),
                "values": np.array([71.0, 79.0, 89.0]),
                "errors": np.array([2.0, 2.0, 3.0]),
                "metadata": {"reference": "unit-test"},
            },
            "fs8_renamed": {
                "dataset_id": "fs8_renamed",
                "observable": "fσ8",
                "z": np.array([0.2, 0.6, 1.0]),
                "values": np.array([0.47, 0.41, 0.36]),
                "errors": np.array([0.03, 0.04, 0.05]),
                "metadata": {"reference": "unit-test"},
            },
        }
        cfg_meta = {
            "run_name": "renamed_dataset_ids",
            "profile_name": "renamed_dataset_ids",
            "active_datasets": ["hz_renamed", "fs8_renamed"],
        }

        df_model, _, out_cov, _ = run_all.run_classic_metrics(cfg_meta, datasets, "prefer_full")
        self.addCleanup(os.remove, out_cov)
        self.addCleanup(os.remove, os.path.join(run_all.RESULTS, "model_comparison.csv"))

        self.assertEqual(set(df_model["model"]), {"LCDM", "RLL_like+AGN"})
        self.assertTrue((df_model["N"] > 0).all())

    def test_mock_real_like_profile_generates_required_artifacts(self):
        generated_paths = [
            os.path.join(run_all.RESULTS, "model_comparison.csv"),
            os.path.join(run_all.RESULTS, "covariance_usage.csv"),
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

    def test_synthetic_advanced_profile_with_covariance_inputs_runs(self):
        generated_paths = [
            os.path.join(run_all.BASE_DIR, "data", "inputs", "structure_d", "Hz_cov.csv"),
            os.path.join(run_all.BASE_DIR, "data", "inputs", "structure_d", "Hz_cov_matrix.csv"),
            os.path.join(run_all.BASE_DIR, "data", "inputs", "structure_d", "fsigma8_cov.csv"),
            os.path.join(run_all.BASE_DIR, "data", "inputs", "structure_d", "fsigma8_cov_matrix.csv"),
            os.path.join(run_all.RESULTS, "model_comparison.csv"),
            os.path.join(run_all.RESULTS, "covariance_usage.csv"),
            os.path.join(run_all.RESULTS, "reproduction_contract.json"),
        ]

        def _cleanup_generated_files():
            for path in generated_paths:
                if os.path.exists(path):
                    os.remove(path)

        self.addCleanup(_cleanup_generated_files)

        make_example_data.main(seed=321, generate_covariance=True)
        run_all.main(profile_name="structure_d_synthetic_advanced")

        cov_usage_path = os.path.join(run_all.RESULTS, "covariance_usage.csv")
        cov_usage = pd.read_csv(cov_usage_path)
        self.assertTrue((cov_usage["covariance_mode"] == "full").all())

    def test_covariance_policy_diagonal_only_converts_covariance_to_sigma(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            data_dir = os.path.join(temp_dir, "data")
            os.makedirs(data_dir, exist_ok=True)

            hz_path = os.path.join(data_dir, "hz_cov.csv")
            hz_cov_path = os.path.join(data_dir, "hz_cov_matrix.csv")
            fs8_path = os.path.join(data_dir, "fsigma8.csv")
            cfg_path = os.path.join(temp_dir, "config.json")

            pd.DataFrame(
                {
                    "z": [0.1, 0.3, 0.6],
                    "Hz": [72.0, 78.5, 91.3],
                }
            ).to_csv(hz_path, index=False)

            covariance = np.array(
                [
                    [4.0, 0.8, 0.2],
                    [0.8, 9.0, 0.5],
                    [0.2, 0.5, 16.0],
                ]
            )
            np.savetxt(hz_cov_path, covariance, delimiter=",")

            pd.DataFrame(
                {
                    "z": [0.2, 0.5, 0.9],
                    "fs8": [0.45, 0.42, 0.38],
                    "sigma": [0.03, 0.04, 0.05],
                }
            ).to_csv(fs8_path, index=False)

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
            self.assertEqual(hz_row["dataset_source"], f"path={hz_path}; reference=unit-test")
            self.assertEqual(hz_row["covariance_mode"], "diagonal")
            self.assertEqual(hz_row["effective_decision"], "diag")
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

            with self.assertRaisesRegex(ValueError, "full_required") as ctx:
                run_all.main(
                    config_path=cfg_path,
                    profile_name="full_required_policy",
                    covariance_policy="full_required",
                )

            message = str(ctx.exception)
            self.assertIn("incompatible datasets", message)
            self.assertIn("hz", message)
            self.assertIn("fsigma8", message)

class StructureDProfileMetadataPropagationTest(unittest.TestCase):
    def test_load_active_datasets_preserves_legacy_policy_field(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            data_dir = os.path.join(temp_dir, "data")
            os.makedirs(data_dir, exist_ok=True)

            hz_path = os.path.join(data_dir, "hz.csv")
            pd.DataFrame({"z": [0.1, 0.3], "Hz": [70.0, 75.0], "sigma": [2.0, 2.5]}).to_csv(hz_path, index=False)

            cfg_path = os.path.join(temp_dir, "legacy_config.json")
            config = {
                "run_name": "legacy_profile",
                "active_datasets": ["hz"],
                "covariance_policy": "diagonal_only",
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
                        "metadata": {"survey": "synthetic", "redshift_range": "[0.1,0.3]", "reference": "unit-test"},
                    }
                },
            }
            with open(cfg_path, "w", encoding="utf-8") as fp:
                json.dump(config, fp)

            meta, _ = load_active_datasets(cfg_path)
            self.assertEqual(meta["covariance_policy"], "diagonal_only")

    def test_run_all_uses_profile_covariance_policy_from_metadata(self):
        generated_paths = [
            os.path.join(run_all.RESULTS, "model_comparison.csv"),
            os.path.join(run_all.RESULTS, "covariance_usage.csv"),
            os.path.join(run_all.RESULTS, "rll_regime_summary.csv"),
            os.path.join(run_all.RESULTS, "reproduction_contract.json"),
        ]

        with tempfile.TemporaryDirectory() as temp_dir:
            self.addCleanup(
                lambda: [shutil.rmtree(path) if os.path.isdir(path) else os.remove(path) for path in generated_paths if os.path.exists(path)]
            )

            data_dir = os.path.join(temp_dir, "data")
            os.makedirs(data_dir, exist_ok=True)

            hz_path = os.path.join(data_dir, "hz_cov.csv")
            cov_path = os.path.join(data_dir, "hz_cov.csv.matrix")
            fs8_path = os.path.join(data_dir, "fs8.csv")
            cfg_path = os.path.join(temp_dir, "profile_config.json")

            pd.DataFrame({"z": [0.1, 0.3, 0.7], "Hz": [72.0, 79.0, 96.0]}).to_csv(hz_path, index=False)
            np.savetxt(cov_path, np.array([[4.0, 0.5, 0.2], [0.5, 9.0, 0.3], [0.2, 0.3, 16.0]]), delimiter=",")
            pd.DataFrame({"z": [0.2, 0.5, 0.9], "fs8": [0.45, 0.42, 0.39], "sigma": [0.03, 0.04, 0.05]}).to_csv(fs8_path, index=False)

            config = {
                "default_profile": "diag_profile",
                "profiles": {
                    "diag_profile": {
                        "run_name": "diag_profile",
                        "active_datasets": ["hz", "fsigma8"],
                        "covariance_policy": "diagonal_only",
                    }
                },
                "datasets": {
                    "hz": {
                        "format": "csv",
                        "path": hz_path,
                        "observable": "Hz",
                        "error_model": "covariance",
                        "columns": {"z": "z", "value": "Hz", "covariance": None},
                        "covariance_path": cov_path,
                        "metadata": {"survey": "synthetic", "redshift_range": "[0.1,0.7]", "reference": "unit-test"},
                    },
                    "fsigma8": {
                        "format": "csv",
                        "path": fs8_path,
                        "observable": "fs8",
                        "error_model": "errors",
                        "columns": {"z": "z", "value": "fs8", "error": "sigma"},
                        "metadata": {"survey": "synthetic", "redshift_range": "[0.2,0.9]", "reference": "unit-test"},
                    },
                },
            }
            with open(cfg_path, "w", encoding="utf-8") as fp:
                json.dump(config, fp)

            run_all.main(config_path=cfg_path, profile_name="diag_profile")

            model_df = pd.read_csv(os.path.join(run_all.RESULTS, "model_comparison.csv"))
            self.assertTrue((model_df["covariance_policy"] == "diagonal_only").all())

            cov_df = pd.read_csv(os.path.join(run_all.RESULTS, "covariance_usage.csv"))
            hz_row = cov_df[cov_df["dataset_id"] == "hz"].iloc[0]
            self.assertEqual(hz_row["covariance_mode"], "diagonal")


class StructureDCovariancePolicyRegressionTest(unittest.TestCase):
    def test_mock_real_like_profile_generates_required_artifacts(self):
        generated_paths = [
            os.path.join(run_all.RESULTS, "model_comparison.csv"),
            os.path.join(run_all.RESULTS, "covariance_usage.csv"),
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

    def test_non_monotonic_z_raises_by_default(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            data_path = os.path.join(temp_dir, "hz.csv")
            cfg_path = os.path.join(temp_dir, "config.json")

            pd.DataFrame(
                {
                    "z": [0.3, 0.1, 0.2],
                    "Hz": [78.0, 70.0, 74.0],
                    "sigma": [2.5, 2.0, 2.2],
                }
            ).to_csv(data_path, index=False)

            config = {
                "default_profile": "z_validation",
                "profiles": {
                    "z_validation": {
                        "run_name": "z_validation",
                        "active_datasets": ["hz"],
                    }
                },
                "datasets": {
                    "hz": {
                        "format": "csv",
                        "path": data_path,
                        "observable": "Hz",
                        "error_model": "errors",
                        "columns": {
                            "z": "z",
                            "value": "Hz",
                            "error": "sigma",
                        },
                        "metadata": {
                            "survey": "synthetic",
                            "redshift_range": "[0.1,0.3]",
                            "reference": "unit-test",
                        },
                    }
                },
            }

            with open(cfg_path, "w", encoding="utf-8") as fp:
                json.dump(config, fp)

            with self.assertRaisesRegex(ValueError, "non-monotonic z"):
                load_active_datasets(cfg_path, profile_name="z_validation")

    def test_non_monotonic_z_can_be_sorted_and_records_metadata(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            data_path = os.path.join(temp_dir, "hz.csv")
            cfg_path = os.path.join(temp_dir, "config.json")

            pd.DataFrame(
                {
                    "z": [0.3, 0.1, 0.2],
                    "Hz": [78.0, 70.0, 74.0],
                    "sigma": [2.5, 2.0, 2.2],
                }
            ).to_csv(data_path, index=False)

            config = {
                "default_profile": "z_sorted",
                "profiles": {
                    "z_sorted": {
                        "run_name": "z_sorted",
                        "active_datasets": ["hz"],
                    }
                },
                "datasets": {
                    "hz": {
                        "format": "csv",
                        "path": data_path,
                        "observable": "Hz",
                        "error_model": "errors",
                        "z_order_policy": "sort",
                        "columns": {
                            "z": "z",
                            "value": "Hz",
                            "error": "sigma",
                        },
                        "metadata": {
                            "survey": "synthetic",
                            "redshift_range": "[0.1,0.3]",
                            "reference": "unit-test",
                        },
                    }
                },
            }

            with open(cfg_path, "w", encoding="utf-8") as fp:
                json.dump(config, fp)

            _, datasets = load_active_datasets(cfg_path, profile_name="z_sorted")
            hz_entry = datasets["hz"]

            np.testing.assert_allclose(hz_entry["z"], np.array([0.1, 0.2, 0.3]))
            np.testing.assert_allclose(hz_entry["values"], np.array([70.0, 74.0, 78.0]))
            np.testing.assert_allclose(hz_entry["errors"], np.array([2.0, 2.2, 2.5]))
            self.assertTrue(hz_entry["metadata"]["z_reordered"])

            cov_usage = pd.read_csv(out_cov)
            hz_row = cov_usage[cov_usage["dataset_id"] == "hz"].iloc[0]
            self.assertEqual(hz_row["dataset_source"], f"path={hz_path}; reference=unit-test")
            self.assertEqual(hz_row["covariance_mode"], "diagonal")
            self.assertFalse(bool(hz_row["has_full_covariance"]))
            self.assertTrue(bool(hz_row["has_diagonal_sigma"]))

    def test_covariance_policy_full_required_raises_for_dataset_without_full_matrix(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            data_path = os.path.join(temp_dir, "hz.csv")
            cfg_path = os.path.join(temp_dir, "config.json")

            pd.DataFrame(
                {
                    "z": [0.1, 0.2, 0.3],
                    "Hz": [70.0, 74.0, 78.0],
                    "sigma": [2.0, 2.2, 2.5],
                }
            ).to_csv(data_path, index=False)

            config = {
                "default_profile": "z_monotonic",
                "profiles": {
                    "z_monotonic": {
                        "run_name": "z_monotonic",
                        "active_datasets": ["hz"],
                    }
                },
                "datasets": {
                    "hz": {
                        "format": "csv",
                        "path": data_path,
                        "observable": "Hz",
                        "error_model": "errors",
                        "columns": {
                            "z": "z",
                            "value": "Hz",
                            "error": "sigma",
                        },
                        "metadata": {
                            "survey": "synthetic",
                            "redshift_range": "[0.1,0.3]",
                            "reference": "unit-test",
                        },
                    }
                },
            }

            with open(cfg_path, "w", encoding="utf-8") as fp:
                json.dump(config, fp)

            _, datasets = load_active_datasets(cfg_path, profile_name="z_monotonic")
            self.assertFalse(datasets["hz"]["metadata"]["z_reordered"])


class StructureDEntrypointParityTest(unittest.TestCase):
    def test_compat_entrypoint_matches_authoritative_output(self):
        make_example_data.main(seed=42)
        self.addCleanup(os.remove, os.path.join(run_all.BASE_DIR, "data", "inputs", "structure_d", "Hz.csv"))
        self.addCleanup(os.remove, os.path.join(run_all.BASE_DIR, "data", "inputs", "structure_d", "fsigma8.csv"))

        original_results = run_all.RESULTS
        original_required_outputs = list(run_all.REQUIRED_OUTPUTS)
        temp_results = tempfile.mkdtemp(prefix="structure_d_entrypoint_")
        self.addCleanup(shutil.rmtree, temp_results)
        self.addCleanup(setattr, run_all, "RESULTS", original_results)
        self.addCleanup(setattr, compat_run_all, "RESULTS", original_results)
        self.addCleanup(setattr, run_all, "REQUIRED_OUTPUTS", original_required_outputs)

        run_all.RESULTS = temp_results
        compat_run_all.RESULTS = temp_results
        run_all.REQUIRED_OUTPUTS = ["model_comparison.csv", "covariance_usage.csv", "reproduction_contract.json"]

        run_all.main(profile_name="structure_d_default")
        expected = pd.read_csv(os.path.join(temp_results, "model_comparison.csv")).sort_values("model").reset_index(drop=True)

        compat_run_all.main(profile_name="structure_d_default")
        observed = pd.read_csv(os.path.join(temp_results, "model_comparison.csv")).sort_values("model").reset_index(drop=True)

        pd.testing.assert_frame_equal(expected, observed, check_exact=False, rtol=0.0, atol=1e-12)


if __name__ == "__main__":
    unittest.main()
