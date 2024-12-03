# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ListClearParams"]


class ListClearParams(TypedDict, total=False):
    confirm: Required[bool]

    session_id: Required[str]
