# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["RegionListResponse", "Result"]


class Result(BaseModel):
    english_name: Optional[str] = None

    iso_3166_1: Optional[str] = None

    native_name: Optional[str] = None


class RegionListResponse(BaseModel):
    results: Optional[List[Result]] = None
