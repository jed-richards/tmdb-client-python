# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["PersonRetrieveResponse"]


class PersonRetrieveResponse(BaseModel):
    id: Optional[int] = None

    adult: Optional[bool] = None

    also_known_as: Optional[List[str]] = None

    biography: Optional[str] = None

    birthday: Optional[str] = None

    deathday: Optional[object] = None

    gender: Optional[int] = None

    homepage: Optional[object] = None

    imdb_id: Optional[str] = None

    known_for_department: Optional[str] = None

    name: Optional[str] = None

    place_of_birth: Optional[str] = None

    popularity: Optional[float] = None

    profile_path: Optional[str] = None
