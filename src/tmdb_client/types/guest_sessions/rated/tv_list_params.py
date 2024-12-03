# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["TvListParams"]


class TvListParams(TypedDict, total=False):
    language: str

    page: int

    sort_by: Literal["created_at.asc", "created_at.desc"]
