# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["EpisodeRetrieveResponse", "Crew", "GuestStar"]


class Crew(BaseModel):
    id: Optional[int] = None

    adult: Optional[bool] = None

    credit_id: Optional[str] = None

    department: Optional[str] = None

    gender: Optional[int] = None

    job: Optional[str] = None

    known_for_department: Optional[str] = None

    name: Optional[str] = None

    original_name: Optional[str] = None

    popularity: Optional[float] = None

    profile_path: Optional[str] = None


class GuestStar(BaseModel):
    id: Optional[int] = None

    adult: Optional[bool] = None

    character: Optional[str] = None

    credit_id: Optional[str] = None

    gender: Optional[int] = None

    known_for_department: Optional[str] = None

    name: Optional[str] = None

    order: Optional[int] = None

    original_name: Optional[str] = None

    popularity: Optional[float] = None

    profile_path: Optional[str] = None


class EpisodeRetrieveResponse(BaseModel):
    id: Optional[int] = None

    air_date: Optional[str] = None

    crew: Optional[List[Crew]] = None

    episode_number: Optional[int] = None

    guest_stars: Optional[List[GuestStar]] = None

    name: Optional[str] = None

    overview: Optional[str] = None

    production_code: Optional[str] = None

    runtime: Optional[int] = None

    season_number: Optional[int] = None

    still_path: Optional[str] = None

    vote_average: Optional[float] = None

    vote_count: Optional[int] = None
