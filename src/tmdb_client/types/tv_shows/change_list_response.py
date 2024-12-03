# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = [
    "ChangeListResponse",
    "Change",
    "ChangeItem",
    "ChangeItemOriginalValue",
    "ChangeItemOriginalValuePoster",
    "ChangeItemValue",
    "ChangeItemValuePoster",
]


class ChangeItemOriginalValuePoster(BaseModel):
    file_path: Optional[str] = None

    iso_639_1: Optional[str] = None


class ChangeItemOriginalValue(BaseModel):
    poster: Optional[ChangeItemOriginalValuePoster] = None


class ChangeItemValuePoster(BaseModel):
    file_path: Optional[str] = None

    iso_639_1: Optional[str] = None


class ChangeItemValue(BaseModel):
    poster: Optional[ChangeItemValuePoster] = None


class ChangeItem(BaseModel):
    id: Optional[str] = None

    action: Optional[str] = None

    iso_3166_1: Optional[str] = None

    iso_639_1: Optional[str] = None

    original_value: Optional[ChangeItemOriginalValue] = None

    time: Optional[str] = None

    value: Optional[ChangeItemValue] = None


class Change(BaseModel):
    items: Optional[List[ChangeItem]] = None

    key: Optional[str] = None


class ChangeListResponse(BaseModel):
    changes: Optional[List[Change]] = None
