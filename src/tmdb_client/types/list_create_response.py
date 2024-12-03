# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["ListCreateResponse"]


class ListCreateResponse(BaseModel):
    list_id: Optional[int] = None

    status_code: Optional[int] = None

    status_message: Optional[str] = None

    success: Optional[bool] = None
