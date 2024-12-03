# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["MovieRatingResponse"]


class MovieRatingResponse(BaseModel):
    status_code: Optional[int] = None

    status_message: Optional[str] = None
