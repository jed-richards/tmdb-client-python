# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ContentRatingRetrieveResponse", "Result"]


class Result(BaseModel):
    descriptors: Optional[List[object]] = None

    iso_3166_1: Optional[str] = None

    rating: Optional[str] = None


class ContentRatingRetrieveResponse(BaseModel):
    id: Optional[int] = None

    results: Optional[List[Result]] = None
