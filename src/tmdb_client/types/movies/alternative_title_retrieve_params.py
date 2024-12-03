# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AlternativeTitleRetrieveParams"]


class AlternativeTitleRetrieveParams(TypedDict, total=False):
    country: str
    """specify a ISO-3166-1 value to filter the results"""
