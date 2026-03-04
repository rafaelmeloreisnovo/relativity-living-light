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
    )
