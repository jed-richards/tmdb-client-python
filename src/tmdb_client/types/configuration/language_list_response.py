# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["LanguageListResponse", "LanguageListResponseItem"]


class LanguageListResponseItem(BaseModel):
    english_name: Optional[str] = None

    iso_639_1: Optional[str] = None

    name: Optional[str] = None


LanguageListResponse: TypeAlias = List[LanguageListResponseItem]
