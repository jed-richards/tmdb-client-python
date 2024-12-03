# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["SearchCollectionResponse", "Result"]


class Result(BaseModel):
    id: Optional[int] = None

    adult: Optional[bool] = None

    backdrop_path: Optional[str] = None

    name: Optional[str] = None

    original_language: Optional[str] = None

    original_name: Optional[str] = None

    overview: Optional[str] = None

    poster_path: Optional[str] = None


class SearchCollectionResponse(BaseModel):
    page: Optional[int] = None

    results: Optional[List[Result]] = None

    total_pages: Optional[int] = None

    total_results: Optional[int] = None
