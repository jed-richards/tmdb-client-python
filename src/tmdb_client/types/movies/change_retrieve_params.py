# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ChangeRetrieveParams"]


class ChangeRetrieveParams(TypedDict, total=False):
    end_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]

    page: int

    start_date: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
