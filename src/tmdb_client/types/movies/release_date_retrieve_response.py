# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ReleaseDateRetrieveResponse", "Result", "ResultReleaseDate"]


class ResultReleaseDate(BaseModel):
    certification: Optional[str] = None

    descriptors: Optional[List[object]] = None

    iso_639_1: Optional[str] = None

    note: Optional[str] = None

    release_date: Optional[str] = None

    type: Optional[int] = None


class Result(BaseModel):
    iso_3166_1: Optional[str] = None

    release_dates: Optional[List[ResultReleaseDate]] = None


class ReleaseDateRetrieveResponse(BaseModel):
    id: Optional[int] = None

    results: Optional[List[Result]] = None
