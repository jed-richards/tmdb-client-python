# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["ChangeListResponse", "Change", "ChangeItem"]


class ChangeItem(BaseModel):
    id: Optional[str] = None

    action: Optional[str] = None

    time: Optional[str] = None

    value: Optional[str] = None


class Change(BaseModel):
    items: Optional[List[ChangeItem]] = None

    key: Optional[str] = None


class ChangeListResponse(BaseModel):
    changes: Optional[List[Change]] = None
