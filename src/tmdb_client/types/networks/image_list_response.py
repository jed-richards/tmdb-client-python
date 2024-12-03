# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ImageListResponse", "Logo"]


class Logo(BaseModel):
    id: Optional[str] = None

    aspect_ratio: Optional[float] = None

    file_path: Optional[str] = None

    file_type: Optional[str] = None

    height: Optional[int] = None

    vote_average: Optional[float] = None

    vote_count: Optional[int] = None

    width: Optional[int] = None


class ImageListResponse(BaseModel):
    id: Optional[int] = None

    logos: Optional[List[Logo]] = None
