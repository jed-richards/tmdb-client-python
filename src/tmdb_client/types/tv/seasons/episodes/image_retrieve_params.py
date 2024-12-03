# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ImageRetrieveParams"]


class ImageRetrieveParams(TypedDict, total=False):
    series_id: Required[int]

    season_number: Required[int]

    include_image_language: str
    """
    specify a comma separated list of ISO-639-1 values to query, for example:
    `en,null`
    """

    language: str
