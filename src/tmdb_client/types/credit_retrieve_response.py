# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["CreditRetrieveResponse", "Media", "MediaSeason", "Person"]


class MediaSeason(BaseModel):
    id: Optional[int] = None

    air_date: Optional[str] = None

    episode_count: Optional[int] = None

    name: Optional[str] = None

    overview: Optional[str] = None

    poster_path: Optional[str] = None

    season_number: Optional[int] = None

    show_id: Optional[int] = None


class Media(BaseModel):
    id: Optional[int] = None

    adult: Optional[bool] = None

    backdrop_path: Optional[str] = None

    character: Optional[str] = None

    episodes: Optional[List[object]] = None

    first_air_date: Optional[str] = None

    genre_ids: Optional[List[int]] = None

    media_type: Optional[str] = None

    name: Optional[str] = None

    origin_country: Optional[List[str]] = None

    original_language: Optional[str] = None

    original_name: Optional[str] = None

    overview: Optional[str] = None

    popularity: Optional[float] = None

    poster_path: Optional[str] = None

    seasons: Optional[List[MediaSeason]] = None

    vote_average: Optional[float] = None

    vote_count: Optional[int] = None


class Person(BaseModel):
    id: Optional[int] = None

    adult: Optional[bool] = None

    gender: Optional[int] = None

    known_for_department: Optional[str] = None

    media_type: Optional[str] = None

    name: Optional[str] = None

    original_name: Optional[str] = None

    popularity: Optional[float] = None

    profile_path: Optional[str] = None


class CreditRetrieveResponse(BaseModel):
    id: Optional[str] = None

    credit_type: Optional[str] = None

    department: Optional[str] = None

    job: Optional[str] = None

    media: Optional[Media] = None

    media_type: Optional[str] = None

    person: Optional[Person] = None
