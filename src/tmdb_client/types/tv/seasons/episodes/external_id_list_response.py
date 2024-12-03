# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ....._models import BaseModel

__all__ = ["ExternalIDListResponse"]


class ExternalIDListResponse(BaseModel):
    id: Optional[int] = None

    freebase_id: Optional[str] = None

    freebase_mid: Optional[str] = None

    imdb_id: Optional[str] = None

    tvdb_id: Optional[int] = None

    tvrage_id: Optional[int] = None

    wikidata_id: Optional[str] = None
