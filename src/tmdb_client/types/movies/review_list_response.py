# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ReviewListResponse", "Result", "ResultAuthorDetails"]


class ResultAuthorDetails(BaseModel):
    avatar_path: Optional[str] = None

    name: Optional[str] = None

    rating: Optional[object] = None

    username: Optional[str] = None


class Result(BaseModel):
    id: Optional[str] = None

    author: Optional[str] = None

    author_details: Optional[ResultAuthorDetails] = None

    content: Optional[str] = None

    created_at: Optional[str] = None

    updated_at: Optional[str] = None

    url: Optional[str] = None


class ReviewListResponse(BaseModel):
    id: Optional[int] = None

    page: Optional[int] = None

    results: Optional[List[Result]] = None

    total_pages: Optional[int] = None

    total_results: Optional[int] = None
