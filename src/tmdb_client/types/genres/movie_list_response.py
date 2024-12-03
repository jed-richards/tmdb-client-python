# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["MovieListResponse", "Genre"]


class Genre(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None


class MovieListResponse(BaseModel):
    genres: Optional[List[Genre]] = None
