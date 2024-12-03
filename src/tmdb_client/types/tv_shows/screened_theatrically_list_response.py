# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ScreenedTheatricallyListResponse", "Result"]


class Result(BaseModel):
    id: Optional[int] = None

    episode_number: Optional[int] = None

    season_number: Optional[int] = None


class ScreenedTheatricallyListResponse(BaseModel):
    id: Optional[int] = None

    results: Optional[List[Result]] = None
