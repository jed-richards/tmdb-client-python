# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["GuestSessionNewResponse"]


class GuestSessionNewResponse(BaseModel):
    expires_at: Optional[str] = None

    guest_session_id: Optional[str] = None

    success: Optional[bool] = None
