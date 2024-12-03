# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ExternalIDRetrieveResponse"]


class ExternalIDRetrieveResponse(BaseModel):
    id: Optional[int] = None

    facebook_id: Optional[str] = None

    imdb_id: Optional[str] = None

    instagram_id: Optional[object] = None

    twitter_id: Optional[object] = None

    wikidata_id: Optional[object] = None
