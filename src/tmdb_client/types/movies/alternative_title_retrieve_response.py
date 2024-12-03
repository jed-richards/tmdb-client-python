# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["AlternativeTitleRetrieveResponse", "Title"]


class Title(BaseModel):
    iso_3166_1: Optional[str] = None

    title: Optional[str] = None

    type: Optional[str] = None


class AlternativeTitleRetrieveResponse(BaseModel):
    id: Optional[int] = None

    titles: Optional[List[Title]] = None
