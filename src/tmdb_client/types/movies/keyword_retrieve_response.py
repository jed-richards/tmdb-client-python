# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["KeywordRetrieveResponse", "Keyword"]


class Keyword(BaseModel):
    id: Optional[int] = None

    name: Optional[str] = None


class KeywordRetrieveResponse(BaseModel):
    id: Optional[int] = None

    keywords: Optional[List[Keyword]] = None
