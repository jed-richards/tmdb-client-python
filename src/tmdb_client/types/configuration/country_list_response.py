# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["CountryListResponse", "CountryListResponseItem"]


class CountryListResponseItem(BaseModel):
    english_name: Optional[str] = None

    iso_3166_1: Optional[str] = None

    native_name: Optional[str] = None


CountryListResponse: TypeAlias = List[CountryListResponseItem]
