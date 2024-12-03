# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["AccountRetrieveResponse", "Avatar", "AvatarGravatar", "AvatarTmdb"]


class AvatarGravatar(BaseModel):
    hash: Optional[str] = None


class AvatarTmdb(BaseModel):
    avatar_path: Optional[str] = None


class Avatar(BaseModel):
    gravatar: Optional[AvatarGravatar] = None

    tmdb: Optional[AvatarTmdb] = None


class AccountRetrieveResponse(BaseModel):
    id: Optional[int] = None

    avatar: Optional[Avatar] = None

    include_adult: Optional[bool] = None

    iso_3166_1: Optional[str] = None

    iso_639_1: Optional[str] = None

    name: Optional[str] = None

    username: Optional[str] = None
