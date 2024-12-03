# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["PersonTaggedImagesResponse", "Result", "ResultMedia"]


class ResultMedia(BaseModel):
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


class Result(BaseModel):
    id: Optional[str] = None

    aspect_ratio: Optional[float] = None

    file_path: Optional[str] = None

    height: Optional[int] = None

    image_type: Optional[str] = None

    iso_639_1: Optional[str] = None

    media: Optional[ResultMedia] = None

    media_type: Optional[str] = None

    vote_average: Optional[float] = None

    vote_count: Optional[int] = None

    width: Optional[int] = None


class PersonTaggedImagesResponse(BaseModel):
    id: Optional[int] = None

    page: Optional[int] = None

    results: Optional[List[Result]] = None

    total_pages: Optional[int] = None

    total_results: Optional[int] = None
