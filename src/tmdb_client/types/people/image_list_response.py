# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ImageListResponse", "Profile"]


class Profile(BaseModel):
    aspect_ratio: Optional[float] = None

    file_path: Optional[str] = None

    height: Optional[int] = None

    iso_639_1: Optional[object] = None

    vote_average: Optional[float] = None

    vote_count: Optional[int] = None

    width: Optional[int] = None


class ImageListResponse(BaseModel):
    id: Optional[int] = None

    profiles: Optional[List[Profile]] = None