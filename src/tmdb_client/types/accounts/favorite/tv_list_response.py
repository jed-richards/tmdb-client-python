# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["TvListResponse", "Result"]


class Result(BaseModel):
    id: Optional[int] = None

    adult: Optional[bool] = None

    backdrop_path: Optional[str] = None

    first_air_date: Optional[str] = None

    genre_ids: Optional[List[int]] = None

    name: Optional[str] = None

    origin_country: Optional[List[str]] = None

    original_language: Optional[str] = None

    original_name: Optional[str] = None

    overview: Optional[str] = None

    popularity: Optional[float] = None

    poster_path: Optional[str] = None

    vote_average: Optional[float] = None

    vote_count: Optional[int] = None


class TvListResponse(BaseModel):
    page: Optional[int] = None

    results: Optional[List[Result]] = None

    total_pages: Optional[int] = None

    total_results: Optional[int] = None
