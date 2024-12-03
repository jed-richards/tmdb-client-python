# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["AlternativeNameListResponse", "Result"]


class Result(BaseModel):
    name: Optional[str] = None

    type: Optional[str] = None


class AlternativeNameListResponse(BaseModel):
    id: Optional[int] = None

    results: Optional[List[Result]] = None
