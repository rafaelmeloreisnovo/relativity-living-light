"""Compat wrapper for data.pipelines.structure_d.run_all (deprecated)."""
from data.pipelines.structure_d.run_all import *  # noqa: F401,F403
from data.pipelines.structure_d.run_all import main as _authoritative_main


if __name__ == "__main__":
    _authoritative_main()
