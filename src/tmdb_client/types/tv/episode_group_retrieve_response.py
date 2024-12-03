# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["EpisodeGroupRetrieveResponse", "Group", "GroupEpisode", "Network"]


class GroupEpisode(BaseModel):
    id: Optional[int] = None

    air_date: Optional[str] = None

    episode_number: Optional[int] = None

    name: Optional[str] = None

    order: Optional[int] = None

    overview: Optional[str] = None

    production_code: Optional[str] = None

    runtime: Optional[object] = None

    season_number: Optional[int] = None

    show_id: Optional[int] = None

    still_path: Optional[str] = None

    vote_average: Optional[float] = None

    vote_count: Optional[int] = None


class Group(BaseModel):
    id: Optional[str] = None

    episodes: Optional[List[GroupEpisode]] = None

    locked: Optional[bool] = None

    name: Optional[str] = None

    order: Optional[int] = None


class Network(BaseModel):
    id: Optional[int] = None

    logo_path: Optional[str] = None

    name: Optional[str] = None

    origin_country: Optional[str] = None


class EpisodeGroupRetrieveResponse(BaseModel):
    id: Optional[str] = None

    description: Optional[str] = None

    episode_count: Optional[int] = None

    group_count: Optional[int] = None

    groups: Optional[List[Group]] = None

    name: Optional[str] = None

    network: Optional[Network] = None

    type: Optional[int] = None
