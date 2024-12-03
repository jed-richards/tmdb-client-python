# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SearchCollectionParams"]


class SearchCollectionParams(TypedDict, total=False):
    query: Required[str]

    include_adult: bool

    language: str

    page: int

    region: str
