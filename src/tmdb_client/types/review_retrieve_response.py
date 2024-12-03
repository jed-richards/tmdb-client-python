# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ReviewRetrieveResponse", "AuthorDetails"]


class AuthorDetails(BaseModel):
    avatar_path: Optional[str] = None

    name: Optional[str] = None

    rating: Optional[int] = None

    username: Optional[str] = None


class ReviewRetrieveResponse(BaseModel):
    id: Optional[str] = None

    author: Optional[str] = None

    author_details: Optional[AuthorDetails] = None

    content: Optional[str] = None

    created_at: Optional[str] = None

    iso_639_1: Optional[str] = None

    media_id: Optional[int] = None

    media_title: Optional[str] = None

    media_type: Optional[str] = None

    updated_at: Optional[str] = None

    url: Optional[str] = None
