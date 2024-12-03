# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "MovieDiscoverParams",
    "Certification",
    "PrimaryReleaseDate",
    "ReleaseDate",
    "VoteAverage",
    "VoteCount",
    "WithRuntime",
]


class MovieDiscoverParams(TypedDict, total=False):
    certification: Certification

    certification_country: str
    """
    use in conjunction with the `certification`, `certification.gte` and
    `certification.lte` filters
    """

    include_adult: bool

    include_video: bool

    language: str

    page: int

    primary_release_date: PrimaryReleaseDate

    primary_release_year: int

    region: str

    release_date: ReleaseDate

    sort_by: Literal[
        "original_title.asc",
        "original_title.desc",
        "popularity.asc",
        "popularity.desc",
        "revenue.asc",
        "revenue.desc",
        "primary_release_date.asc",
        "title.asc",
        "title.desc",
        "primary_release_date.desc",
        "vote_average.asc",
        "vote_average.desc",
        "vote_count.asc",
        "vote_count.desc",
    ]

    vote_average: VoteAverage

    vote_count: VoteCount

    watch_region: str
    """
    use in conjunction with `with_watch_monetization_types ` or
    `with_watch_providers `
    """

    with_cast: str
    """can be a comma (`AND`) or pipe (`OR`) separated query"""

    with_companies: str
    """can be a comma (`AND`) or pipe (`OR`) separated query"""

    with_crew: str
    """can be a comma (`AND`) or pipe (`OR`) separated query"""

    with_genres: str
    """can be a comma (`AND`) or pipe (`OR`) separated query"""

    with_keywords: str
    """can be a comma (`AND`) or pipe (`OR`) separated query"""

    with_origin_country: str

    with_original_language: str

    with_people: str
    """can be a comma (`AND`) or pipe (`OR`) separated query"""

    with_release_type: int
    """
    possible values are: [1, 2, 3, 4, 5, 6] can be a comma (`AND`) or pipe (`OR`)
    separated query, can be used in conjunction with `region`
    """

    with_runtime: WithRuntime

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

    year: int


class Certification(TypedDict, total=False):
    gte: str
    """use in conjunction with `region`"""

    lte: str
    """use in conjunction with `region`"""


class PrimaryReleaseDate(TypedDict, total=False):
    gte: Annotated[Union[str, date], PropertyInfo(format="iso8601")]

    lte: Annotated[Union[str, date], PropertyInfo(format="iso8601")]


class ReleaseDate(TypedDict, total=False):
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
