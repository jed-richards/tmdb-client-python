# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["MovieRetrieveResponse", "Genre", "ProductionCompany", "ProductionCountry", "SpokenLanguage"]


class Genre(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None


class ProductionCompany(BaseModel):
    id: Optional[int] = None

    logo_path: Optional[str] = None

    name: Optional[str] = None

    origin_country: Optional[str] = None


class ProductionCountry(BaseModel):
    iso_3166_1: Optional[str] = None

    name: Optional[str] = None


class SpokenLanguage(BaseModel):
    english_name: Optional[str] = None

    iso_639_1: Optional[str] = None

    name: Optional[str] = None


class MovieRetrieveResponse(BaseModel):
    id: Optional[int] = None

    adult: Optional[bool] = None

    backdrop_path: Optional[str] = None

    belongs_to_collection: Optional[object] = None

    budget: Optional[int] = None

    genres: Optional[List[Genre]] = None

    homepage: Optional[str] = None

    imdb_id: Optional[str] = None

    original_language: Optional[str] = None

    original_title: Optional[str] = None

    overview: Optional[str] = None

    popularity: Optional[float] = None

    poster_path: Optional[str] = None

    production_companies: Optional[List[ProductionCompany]] = None

    production_countries: Optional[List[ProductionCountry]] = None

    release_date: Optional[str] = None

    revenue: Optional[int] = None

    runtime: Optional[int] = None

    spoken_languages: Optional[List[SpokenLanguage]] = None

    status: Optional[str] = None

    tagline: Optional[str] = None

    title: Optional[str] = None

    video: Optional[bool] = None

    vote_average: Optional[float] = None

    vote_count: Optional[int] = None
