# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["PersonExternalIDsResponse"]


class PersonExternalIDsResponse(BaseModel):
    id: Optional[int] = None

    facebook_id: Optional[str] = None

    freebase_id: Optional[str] = None

    freebase_mid: Optional[str] = None

    imdb_id: Optional[str] = None

    instagram_id: Optional[str] = None

    tiktok_id: Optional[str] = None

    tvrage_id: Optional[int] = None

    twitter_id: Optional[str] = None

    wikidata_id: Optional[str] = None

    youtube_id: Optional[object] = None
