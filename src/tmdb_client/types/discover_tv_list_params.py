# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DiscoverTvListParams", "AirDate", "FirstAirDate", "VoteAverage", "VoteCount", "WithRuntime"]


class DiscoverTvListParams(TypedDict, total=False):
    air_date: AirDate

    first_air_date: FirstAirDate

    first_air_date_year: int

    include_adult: bool

    include_null_first_air_dates: bool

    language: str

    page: int

    screened_theatrically: bool

    sort_by: Literal[
        "first_air_date.asc",
        "first_air_date.desc",
        "name.asc",
        "name.desc",
        "original_name.asc",
        "original_name.desc",
        "popularity.asc",
        "popularity.desc",
        "vote_average.asc",
        "vote_average.desc",
        "vote_count.asc",
        "vote_count.desc",
    ]

    timezone: str

    vote_average: VoteAverage

    vote_count: VoteCount

    watch_region: str
    """
    use in conjunction with `with_watch_monetization_types ` or
    `with_watch_providers `
    """

    with_companies: str
    """can be a comma (`AND`) or pipe (`OR`) separated query"""

    with_genres: str
    """can be a comma (`AND`) or pipe (`OR`) separated query"""

    with_keywords: str
    """can be a comma (`AND`) or pipe (`OR`) separated query"""

    with_networks: int

    with_origin_country: str

    with_original_language: str

    with_runtime: WithRuntime

    with_status: str
    """
    possible values are: [0, 1, 2, 3, 4, 5], can be a comma (`AND`) or pipe (`OR`)
    separated query
    """

    with_type: str
    """
    possible values are: [0, 1, 2, 3, 4, 5, 6], can be a comma (`AND`) or pipe
    (`OR`) separated query
    """

    with_watch_monetization_types: str
    """
    possible values are: [flatrate, free, ads, rent, buy] use in conjunction with
    `watch_region`, can be a comma (`AND`) or pipe (`OR`) separated query
    """

    with_watch_providers: str
    """
    use in conjunction with `watch_region`, can be a comma (`AND`) or pipe (`OR`)
    separated query
    """

    without_companies: str

    without_genres: str

    without_keywords: str

    without_watch_providers: str


class AirDate(TypedDict, total=False):
    gte: Annotated[Union[str, date], PropertyInfo(format="iso8601")]

    lte: Annotated[Union[str, date], PropertyInfo(format="iso8601")]


class FirstAirDate(TypedDict, total=False):
    gte: Annotated[Union[str, date], PropertyInfo(format="iso8601")]

    lte: Annotated[Union[str, date], PropertyInfo(format="iso8601")]


class VoteAverage(TypedDict, total=False):
    gte: float

    lte: float


class VoteCount(TypedDict, total=False):
    gte: float

    lte: float


class WithRuntime(TypedDict, total=False):
    gte: int

    lte: int
