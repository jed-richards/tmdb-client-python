# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["LatestRetrieveResponse", "LastEpisodeToAir", "Season"]


class LastEpisodeToAir(BaseModel):
    id: Optional[int] = None

    air_date: Optional[str] = None

    episode_number: Optional[int] = None

    name: Optional[str] = None

    overview: Optional[str] = None

    production_code: Optional[str] = None

    runtime: Optional[object] = None

    season_number: Optional[int] = None

    show_id: Optional[int] = None

    still_path: Optional[object] = None

    vote_average: Optional[int] = None

    vote_count: Optional[int] = None


class Season(BaseModel):
    id: Optional[int] = None

    air_date: Optional[object] = None

    episode_count: Optional[int] = None

    name: Optional[str] = None

    overview: Optional[str] = None

    poster_path: Optional[object] = None

    season_number: Optional[int] = None


class LatestRetrieveResponse(BaseModel):
    id: Optional[int] = None

    adult: Optional[bool] = None

    backdrop_path: Optional[object] = None

    created_by: Optional[List[object]] = None

    episode_run_time: Optional[List[object]] = None

    first_air_date: Optional[str] = None

    genres: Optional[List[object]] = None

    homepage: Optional[str] = None

    in_production: Optional[bool] = None

    languages: Optional[List[object]] = None

    last_air_date: Optional[str] = None

    last_episode_to_air: Optional[LastEpisodeToAir] = None

    name: Optional[str] = None

    networks: Optional[List[object]] = None

    next_episode_to_air: Optional[object] = None

    number_of_episodes: Optional[int] = None

    number_of_seasons: Optional[int] = None

    origin_country: Optional[List[str]] = None

    original_language: Optional[str] = None

    original_name: Optional[str] = None

    overview: Optional[str] = None

    popularity: Optional[int] = None

    poster_path: Optional[object] = None

    production_companies: Optional[List[object]] = None

    production_countries: Optional[List[object]] = None

    seasons: Optional[List[Season]] = None

    spoken_languages: Optional[List[object]] = None

    status: Optional[str] = None

    tagline: Optional[str] = None

    type: Optional[str] = None

    vote_average: Optional[int] = None

    vote_count: Optional[int] = None
