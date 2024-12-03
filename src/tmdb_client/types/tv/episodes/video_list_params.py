# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VideoListParams"]


class VideoListParams(TypedDict, total=False):
    series_id: Required[int]

    season_number: Required[int]

    include_video_language: str
    """
    filter the list results by language, supports more than one value by using a
    comma
    """

    language: str
