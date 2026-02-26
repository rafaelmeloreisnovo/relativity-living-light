from copy import deepcopy


_H0_SCENARIOS = {
    "Planck_like": {
        "distribution": "gaussian",
        "mean": 67.4,
        "sigma": 0.5,
        "reference": "Planck 2018 baseline-like calibration",
    },
    "SH0ES_like": {
        "distribution": "gaussian",
        "mean": 73.0,
        "sigma": 1.0,
        "reference": "SH0ES late-universe distance-ladder-like calibration",
    },
    "flat_uninformative": {
        "distribution": "uniform",
        "min": 50.0,
        "max": 90.0,
        "reference": "Wide uninformative interval",
    },
}


_EXPERIMENT_SYSTEMATICS = {
    "Hz": {
        "active_systematics": ["cc_age_bias", "bao_calibration", "selection_bias"],
    },
    "fsigma8": {
        "active_systematics": ["rsd_modeling", "galaxy_bias", "redshift_failure"],
    },
}


def available_h0_scenarios():
    return tuple(sorted(_H0_SCENARIOS))


def get_h0_prior(h0_scenario):
    if h0_scenario not in _H0_SCENARIOS:
        options = ", ".join(available_h0_scenarios())
        raise ValueError(f"Unknown h0_scenario '{h0_scenario}'. Available: {options}")
    return deepcopy(_H0_SCENARIOS[h0_scenario])


def _build_experiment_config(experiments):
    experiment_config = {}
    for experiment in experiments:
        if experiment not in _EXPERIMENT_SYSTEMATICS:
            options = ", ".join(sorted(_EXPERIMENT_SYSTEMATICS))
            raise ValueError(
                f"Unknown experiment '{experiment}'. Available experiments: {options}"
            )
        experiment_config[experiment] = deepcopy(_EXPERIMENT_SYSTEMATICS[experiment])
    return experiment_config


def build_systematics_config(experiments, h0_scenario):
    ordered_experiments = tuple(dict.fromkeys(experiments))
    h0_prior = get_h0_prior(h0_scenario)
    by_experiment = _build_experiment_config(ordered_experiments)

    return {
        "experiments": ordered_experiments,
        "by_experiment": by_experiment,
        "h0": {
            "scenario": h0_scenario,
            "prior": h0_prior,
        },
        "traceability": {
            "h0_scenario": h0_scenario,
            "h0_prior_reference": h0_prior.get("reference", "n/a"),
            "experiments": ordered_experiments,
        },
    }
