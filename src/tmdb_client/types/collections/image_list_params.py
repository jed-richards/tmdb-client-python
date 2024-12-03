# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ImageListParams"]


class ImageListParams(TypedDict, total=False):
    include_image_language: str
    """
    specify a comma separated list of ISO-639-1 values to query, for example:
    `en,null`
    """

    language: str
