# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["EpisodeGroupRetrieveResponse", "Result", "ResultNetwork"]


class ResultNetwork(BaseModel):
    id: Optional[int] = None

    logo_path: Optional[str] = None

    name: Optional[str] = None

    origin_country: Optional[str] = None


class Result(BaseModel):
    id: Optional[str] = None

    description: Optional[str] = None

    episode_count: Optional[int] = None

    group_count: Optional[int] = None

    name: Optional[str] = None

    network: Optional[ResultNetwork] = None

    type: Optional[int] = None


class EpisodeGroupRetrieveResponse(BaseModel):
    id: Optional[int] = None

    results: Optional[List[Result]] = None
