# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TvSearchParams"]


class TvSearchParams(TypedDict, total=False):
    query: Required[str]

    first_air_date_year: int
    """Search only the first air date. Valid values are: 1000..9999"""

    include_adult: bool

    language: str

    page: int

    year: int
    """Search the first air date and all episode air dates.

    Valid values are: 1000..9999
    """
