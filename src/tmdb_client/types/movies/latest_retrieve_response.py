# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["LatestRetrieveResponse"]


class LatestRetrieveResponse(BaseModel):
    id: Optional[int] = None

    adult: Optional[bool] = None

    backdrop_path: Optional[object] = None

    belongs_to_collection: Optional[object] = None

    budget: Optional[int] = None

    genres: Optional[List[object]] = None

    homepage: Optional[str] = None

    imdb_id: Optional[object] = None

    original_language: Optional[str] = None

    original_title: Optional[str] = None

    overview: Optional[str] = None

    popularity: Optional[int] = None

    poster_path: Optional[object] = None

    production_companies: Optional[List[object]] = None

    production_countries: Optional[List[object]] = None

    release_date: Optional[str] = None

    revenue: Optional[int] = None

    runtime: Optional[int] = None

    spoken_languages: Optional[List[object]] = None

    status: Optional[str] = None

    tagline: Optional[str] = None

    title: Optional[str] = None

    video: Optional[bool] = None

    vote_average: Optional[int] = None

    vote_count: Optional[int] = None
