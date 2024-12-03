# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["CombinedCreditListResponse", "Cast", "Crew"]


class Cast(BaseModel):
    id: Optional[int] = None

    adult: Optional[bool] = None

    backdrop_path: Optional[str] = None

    character: Optional[str] = None

    credit_id: Optional[str] = None

    genre_ids: Optional[List[int]] = None

    media_type: Optional[str] = None

    order: Optional[int] = None

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


class Crew(BaseModel):
    id: Optional[int] = None

    adult: Optional[bool] = None

    backdrop_path: Optional[str] = None

    credit_id: Optional[str] = None

    department: Optional[str] = None

    genre_ids: Optional[List[int]] = None

    job: Optional[str] = None

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


class CombinedCreditListResponse(BaseModel):
    id: Optional[int] = None

    cast: Optional[List[Cast]] = None

    crew: Optional[List[Crew]] = None
