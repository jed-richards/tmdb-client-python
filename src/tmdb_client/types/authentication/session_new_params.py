# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SessionNewParams"]


class SessionNewParams(TypedDict, total=False):
    raw_body: Required[Annotated[str, PropertyInfo(alias="RAW_BODY")]]
