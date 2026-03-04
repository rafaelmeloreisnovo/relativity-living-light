"""Compat wrapper for data.pipelines.structure_d.run_all (deprecated)."""
from data.pipelines.structure_d.run_all import *  # noqa: F401,F403
from data.pipelines.structure_d.run_all import _build_parser

if __name__ == "__main__":
    args = _build_parser().parse_args()
    main(
        config_path=args.config,
        profile_name=args.profile,
        covariance_policy=args.covariance_policy,
        bayes=args.bayes,
        bayes_mode=args.bayes_mode,
        bayes_seed=args.bayes_seed,
        bayes_nwalkers=args.bayes_nwalkers,
        bayes_nsteps=args.bayes_nsteps,
        bayes_nlive=args.bayes_nlive,
    )
