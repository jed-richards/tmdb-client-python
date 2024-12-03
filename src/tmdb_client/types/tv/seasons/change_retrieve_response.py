# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["ChangeRetrieveResponse", "Change", "ChangeItem", "ChangeItemValue"]


class ChangeItemValue(BaseModel):
    episode_id: Optional[int] = None

    episode_number: Optional[int] = None


class ChangeItem(BaseModel):
    id: Optional[str] = None

    action: Optional[str] = None

    time: Optional[str] = None

    value: Optional[ChangeItemValue] = None


class Change(BaseModel):
    items: Optional[List[ChangeItem]] = None

    key: Optional[str] = None


class ChangeRetrieveResponse(BaseModel):
    changes: Optional[List[Change]] = None
