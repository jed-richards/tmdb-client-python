# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["PersonTranslationsResponse", "Translation", "TranslationData"]


class TranslationData(BaseModel):
    biography: Optional[str] = None

    name: Optional[str] = None


class Translation(BaseModel):
    data: Optional[TranslationData] = None

    english_name: Optional[str] = None

    iso_3166_1: Optional[str] = None

    iso_639_1: Optional[str] = None

    name: Optional[str] = None


class PersonTranslationsResponse(BaseModel):
    id: Optional[int] = None

    translations: Optional[List[Translation]] = None
