# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["TrendingMovieListResponse", "Result"]


class Result(BaseModel):
    id: Optional[int] = None

    adult: Optional[bool] = None

    backdrop_path: Optional[str] = None

    genre_ids: Optional[List[int]] = None

    media_type: Optional[str] = None

    original_language: Optional[str] = None

    original_title: Optional[str] = None

    overview: Optional[str] = None

    popularity: Optional[float] = None

    poster_path: Optional[str] = None

    release_date: Optional[str] = None

    title: Optional[str] = None

    video: Optional[bool] = None

    vote_average: Optional[float] = None

    vote_count: Optional[int] = None


class TrendingMovieListResponse(BaseModel):
    page: Optional[int] = None

    results: Optional[List[Result]] = None

    total_pages: Optional[int] = None

    total_results: Optional[int] = None