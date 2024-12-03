# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ListRemoveItemParams"]


class ListRemoveItemParams(TypedDict, total=False):
    session_id: Required[str]

    raw_body: Required[Annotated[str, PropertyInfo(alias="RAW_BODY")]]
