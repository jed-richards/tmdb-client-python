# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = [
    "TvRetrieveResponse",
    "CreatedBy",
    "Genre",
    "LastEpisodeToAir",
    "Network",
    "ProductionCompany",
    "ProductionCountry",
    "Season",
    "SpokenLanguage",
]


class CreatedBy(BaseModel):
    id: Optional[int] = None

    credit_id: Optional[str] = None

    gender: Optional[int] = None

    name: Optional[str] = None

    profile_path: Optional[str] = None


class Genre(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None


class LastEpisodeToAir(BaseModel):
    id: Optional[int] = None

    air_date: Optional[str] = None

    episode_number: Optional[int] = None

    name: Optional[str] = None

    overview: Optional[str] = None

    production_code: Optional[str] = None

    runtime: Optional[int] = None

    season_number: Optional[int] = None

    show_id: Optional[int] = None

    still_path: Optional[str] = None

    vote_average: Optional[float] = None

    vote_count: Optional[int] = None


class Network(BaseModel):
    id: Optional[int] = None

    logo_path: Optional[str] = None

    name: Optional[str] = None

    origin_country: Optional[str] = None


class ProductionCompany(BaseModel):
    id: Optional[int] = None

    logo_path: Optional[str] = None

    name: Optional[str] = None

    origin_country: Optional[str] = None


class ProductionCountry(BaseModel):
    iso_3166_1: Optional[str] = None

    name: Optional[str] = None


class Season(BaseModel):
    id: Optional[int] = None

    air_date: Optional[str] = None

    episode_count: Optional[int] = None

    name: Optional[str] = None

    overview: Optional[str] = None

    poster_path: Optional[str] = None

    season_number: Optional[int] = None

    vote_average: Optional[int] = None


class SpokenLanguage(BaseModel):
    english_name: Optional[str] = None

    iso_639_1: Optional[str] = None

    name: Optional[str] = None


class TvRetrieveResponse(BaseModel):
    id: Optional[int] = None

    adult: Optional[bool] = None

    backdrop_path: Optional[str] = None

    created_by: Optional[List[CreatedBy]] = None

    episode_run_time: Optional[List[int]] = None

    first_air_date: Optional[str] = None

    genres: Optional[List[Genre]] = None

    homepage: Optional[str] = None

    in_production: Optional[bool] = None

    languages: Optional[List[str]] = None

    last_air_date: Optional[str] = None

    last_episode_to_air: Optional[LastEpisodeToAir] = None

    name: Optional[str] = None

    networks: Optional[List[Network]] = None

    next_episode_to_air: Optional[object] = None

    number_of_episodes: Optional[int] = None

    number_of_seasons: Optional[int] = None

    origin_country: Optional[List[str]] = None

    original_language: Optional[str] = None

    original_name: Optional[str] = None

    overview: Optional[str] = None

    popularity: Optional[float] = None

    poster_path: Optional[str] = None

    production_companies: Optional[List[ProductionCompany]] = None

    production_countries: Optional[List[ProductionCountry]] = None

    seasons: Optional[List[Season]] = None

    spoken_languages: Optional[List[SpokenLanguage]] = None

    status: Optional[str] = None

    tagline: Optional[str] = None

    type: Optional[str] = None

    vote_average: Optional[float] = None

    vote_count: Optional[int] = None
