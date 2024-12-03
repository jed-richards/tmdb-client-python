# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FindRetrieveParams"]


class FindRetrieveParams(TypedDict, total=False):
    external_source: Required[
        Literal[
            "",
            "imdb_id",
            "facebook_id",
            "instagram_id",
            "tvdb_id",
            "tiktok_id",
            "twitter_id",
            "wikidata_id",
            "youtube_id",
        ]
    ]

    language: str
