# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AccountStateRetrieveParams"]


class AccountStateRetrieveParams(TypedDict, total=False):
    series_id: Required[int]

    guest_session_id: str

    session_id: str
