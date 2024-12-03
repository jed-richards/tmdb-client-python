# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["MovieRatingDeleteParams"]


class MovieRatingDeleteParams(TypedDict, total=False):
    guest_session_id: str

    session_id: str
