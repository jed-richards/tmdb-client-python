# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EpisodeAccountStatesParams"]


class EpisodeAccountStatesParams(TypedDict, total=False):
    series_id: Required[int]

    season_number: Required[int]

    guest_session_id: str

    session_id: str
