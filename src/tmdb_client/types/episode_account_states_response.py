# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["EpisodeAccountStatesResponse", "Rated"]


class Rated(BaseModel):
    value: Optional[int] = None


class EpisodeAccountStatesResponse(BaseModel):
    id: Optional[int] = None

    favorite: Optional[bool] = None

    rated: Optional[Rated] = None

    watchlist: Optional[bool] = None
