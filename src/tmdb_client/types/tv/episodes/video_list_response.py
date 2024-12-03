# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["VideoListResponse", "Result"]


class Result(BaseModel):
    id: Optional[str] = None

    iso_3166_1: Optional[str] = None

    iso_639_1: Optional[str] = None

    key: Optional[str] = None

    name: Optional[str] = None

    official: Optional[bool] = None

    published_at: Optional[str] = None

    site: Optional[str] = None

    size: Optional[int] = None

    type: Optional[str] = None


class VideoListResponse(BaseModel):
    id: Optional[int] = None

    results: Optional[List[Result]] = None
