"""Compat wrapper for data.pipelines.structure_d.run_all (deprecated)."""

import runpy


if __name__ == "__main__":
    runpy.run_module("data.pipelines.structure_d.run_all", run_name="__main__")
else:
    from data.pipelines.structure_d.run_all import *  # noqa: F401,F403
