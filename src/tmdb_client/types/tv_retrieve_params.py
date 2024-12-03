# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["TvRetrieveParams"]


class TvRetrieveParams(TypedDict, total=False):
    append_to_response: str
    """comma separated list of endpoints within this namespace, 20 items max"""

    language: str
