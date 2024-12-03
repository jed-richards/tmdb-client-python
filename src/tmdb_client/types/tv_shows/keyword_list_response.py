# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["KeywordListResponse", "Result"]


class Result(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None


class KeywordListResponse(BaseModel):
    id: Optional[int] = None

    results: Optional[List[Result]] = None
