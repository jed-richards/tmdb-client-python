# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CompanyRetrieveResponse"]


class CompanyRetrieveResponse(BaseModel):
    id: Optional[int] = None

    description: Optional[str] = None

    headquarters: Optional[str] = None

    homepage: Optional[str] = None

    logo_path: Optional[str] = None

    name: Optional[str] = None

    origin_country: Optional[str] = None

    parent_company: Optional[object] = None
