# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TokenNewResponse"]


class TokenNewResponse(BaseModel):
    expires_at: Optional[str] = None

    request_token: Optional[str] = None

    success: Optional[bool] = None
