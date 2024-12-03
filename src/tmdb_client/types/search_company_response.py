# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["SearchCompanyResponse", "Result"]


class Result(BaseModel):
    id: Optional[int] = None

    logo_path: Optional[str] = None

    name: Optional[str] = None

    origin_country: Optional[str] = None


class SearchCompanyResponse(BaseModel):
    page: Optional[int] = None

    results: Optional[List[Result]] = None

    total_pages: Optional[int] = None

    total_results: Optional[int] = None
