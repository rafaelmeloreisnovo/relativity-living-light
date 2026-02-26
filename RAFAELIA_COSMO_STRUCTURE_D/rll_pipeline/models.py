"""Compat wrapper for data.pipelines.structure_d.models (deprecated)."""

from data.pipelines.structure_d.models import (
    cs2_toy_eft,
    is_physically_stable,
    model_LCDM_fs8,
    model_LCDM_Hz,
    model_RLL_like_fs8,
    model_RLL_like_Hz,
    stability_flags_toy_eft,
)

__all__ = [
    "model_LCDM_Hz",
    "model_RLL_like_Hz",
    "model_LCDM_fs8",
    "model_RLL_like_fs8",
    "cs2_toy_eft",
    "stability_flags_toy_eft",
    "is_physically_stable",
]
