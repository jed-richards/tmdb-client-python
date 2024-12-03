# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["TimezoneListResponse", "TimezoneListResponseItem"]


class TimezoneListResponseItem(BaseModel):
    iso_3166_1: Optional[str] = None

    zones: Optional[List[str]] = None


TimezoneListResponse: TypeAlias = List[TimezoneListResponseItem]
