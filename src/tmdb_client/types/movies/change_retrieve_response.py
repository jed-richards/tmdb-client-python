# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ChangeRetrieveResponse", "Change", "ChangeItem", "ChangeItemValue", "ChangeItemValuePoster"]


class ChangeItemValuePoster(BaseModel):
    file_path: Optional[str] = None


class ChangeItemValue(BaseModel):
    poster: Optional[ChangeItemValuePoster] = None


class ChangeItem(BaseModel):
    id: Optional[str] = None

    action: Optional[str] = None

    iso_3166_1: Optional[str] = None

    iso_639_1: Optional[str] = None

    time: Optional[str] = None

    value: Optional[ChangeItemValue] = None


class Change(BaseModel):
    items: Optional[List[ChangeItem]] = None

    key: Optional[str] = None


class ChangeRetrieveResponse(BaseModel):
    changes: Optional[List[Change]] = None
