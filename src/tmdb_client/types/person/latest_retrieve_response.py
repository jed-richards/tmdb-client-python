# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["LatestRetrieveResponse"]


class LatestRetrieveResponse(BaseModel):
    id: Optional[int] = None

    adult: Optional[bool] = None

    also_known_as: Optional[List[object]] = None

    biography: Optional[str] = None

    birthday: Optional[object] = None

    deathday: Optional[object] = None

    gender: Optional[int] = None

    homepage: Optional[object] = None

    imdb_id: Optional[object] = None

    known_for_department: Optional[object] = None

    name: Optional[str] = None

    place_of_birth: Optional[object] = None

    popularity: Optional[int] = None

    profile_path: Optional[object] = None
