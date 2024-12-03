# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["AccountStateRetrieveResponse", "Result", "ResultRated"]


class ResultRated(BaseModel):
    value: Optional[int] = None


class Result(BaseModel):
    id: Optional[int] = None

    episode_number: Optional[int] = None

    rated: Optional[ResultRated] = None


class AccountStateRetrieveResponse(BaseModel):
    id: Optional[int] = None

    results: Optional[List[Result]] = None
