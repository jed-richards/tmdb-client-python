# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["ConfigurationRetrieveResponse", "Images"]


class Images(BaseModel):
    backdrop_sizes: Optional[List[str]] = None

    base_url: Optional[str] = None

    logo_sizes: Optional[List[str]] = None

    poster_sizes: Optional[List[str]] = None

    profile_sizes: Optional[List[str]] = None

    secure_base_url: Optional[str] = None

    still_sizes: Optional[List[str]] = None


class ConfigurationRetrieveResponse(BaseModel):
    change_keys: Optional[List[str]] = None

    images: Optional[Images] = None
