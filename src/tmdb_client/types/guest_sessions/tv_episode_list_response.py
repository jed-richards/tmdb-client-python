# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["TvEpisodeListResponse", "Result"]


class Result(BaseModel):
    id: Optional[int] = None

    air_date: Optional[str] = None

    episode_number: Optional[int] = None

    name: Optional[str] = None

    overview: Optional[str] = None

    production_code: Optional[str] = None

    rating: Optional[float] = None

    runtime: Optional[int] = None

    season_number: Optional[int] = None

    show_id: Optional[int] = None

    still_path: Optional[str] = None

    vote_average: Optional[float] = None

    vote_count: Optional[int] = None


class TvEpisodeListResponse(BaseModel):
    page: Optional[int] = None

    results: Optional[List[Result]] = None

    total_pages: Optional[int] = None

    total_results: Optional[int] = None
