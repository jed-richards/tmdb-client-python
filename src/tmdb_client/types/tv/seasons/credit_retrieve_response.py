# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["CreditRetrieveResponse", "Cast", "Crew"]


class Cast(BaseModel):
    id: Optional[int] = None

    adult: Optional[bool] = None

    character: Optional[str] = None

    credit_id: Optional[str] = None

    gender: Optional[int] = None

    known_for_department: Optional[str] = None

    name: Optional[str] = None

    order: Optional[int] = None

    original_name: Optional[str] = None

    popularity: Optional[float] = None

    profile_path: Optional[str] = None


class Crew(BaseModel):
    id: Optional[int] = None

    adult: Optional[bool] = None

    credit_id: Optional[str] = None

    department: Optional[str] = None

    gender: Optional[int] = None

    job: Optional[str] = None

    known_for_department: Optional[str] = None

    name: Optional[str] = None

    original_name: Optional[str] = None

    popularity: Optional[float] = None

    profile_path: Optional[object] = None


class CreditRetrieveResponse(BaseModel):
    id: Optional[int] = None

    cast: Optional[List[Cast]] = None

    crew: Optional[List[Crew]] = None
