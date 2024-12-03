# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["MovieListParams"]


class MovieListParams(TypedDict, total=False):
    language: str

    page: int

    session_id: str

    sort_by: Literal["created_at.asc", "created_at.desc"]
