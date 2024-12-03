# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["JobListResponse", "JobListResponseItem"]


class JobListResponseItem(BaseModel):
    department: Optional[str] = None

    jobs: Optional[List[str]] = None


JobListResponse: TypeAlias = List[JobListResponseItem]
