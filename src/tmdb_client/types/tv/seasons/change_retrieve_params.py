# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ChangeRetrieveParams"]


class ChangeRetrieveParams(TypedDict, total=False):
    end_date: str

    page: int

    start_date: str
