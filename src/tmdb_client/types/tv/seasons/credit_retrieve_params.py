# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CreditRetrieveParams"]


class CreditRetrieveParams(TypedDict, total=False):
    series_id: Required[int]

    language: str
