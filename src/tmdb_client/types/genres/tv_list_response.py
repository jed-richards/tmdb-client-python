# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["TvListResponse", "Genre"]


class Genre(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None


class TvListResponse(BaseModel):
    genres: Optional[List[Genre]] = None
