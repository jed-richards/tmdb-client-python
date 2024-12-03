# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["NowPlayingListParams"]


class NowPlayingListParams(TypedDict, total=False):
    language: str

    page: int

    region: str
    """ISO-3166-1 code"""
