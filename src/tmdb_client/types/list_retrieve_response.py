# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ListRetrieveResponse", "Item"]


class Item(BaseModel):
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

    vote_average: Optional[int] = None

    vote_count: Optional[int] = None


class ListRetrieveResponse(BaseModel):
    id: Optional[str] = None

    created_by: Optional[str] = None

    description: Optional[str] = None

    favorite_count: Optional[int] = None

    iso_639_1: Optional[str] = None

    item_count: Optional[int] = None

    items: Optional[List[Item]] = None

    name: Optional[str] = None

    poster_path: Optional[str] = None
