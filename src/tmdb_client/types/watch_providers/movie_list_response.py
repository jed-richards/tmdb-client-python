# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MovieListResponse", "Result", "ResultDisplayPriorities"]


class ResultDisplayPriorities(BaseModel):
    ae: Optional[int] = FieldInfo(alias="AE", default=None)

    ar: Optional[int] = FieldInfo(alias="AR", default=None)

    at: Optional[int] = FieldInfo(alias="AT", default=None)

    au: Optional[int] = FieldInfo(alias="AU", default=None)

    be: Optional[int] = FieldInfo(alias="BE", default=None)

    bg: Optional[int] = FieldInfo(alias="BG", default=None)

    bo: Optional[int] = FieldInfo(alias="BO", default=None)

    br: Optional[int] = FieldInfo(alias="BR", default=None)

    ca: Optional[int] = FieldInfo(alias="CA", default=None)

    ch: Optional[int] = FieldInfo(alias="CH", default=None)

    cl: Optional[int] = FieldInfo(alias="CL", default=None)

    co: Optional[int] = FieldInfo(alias="CO", default=None)

    cr: Optional[int] = FieldInfo(alias="CR", default=None)

    cv: Optional[int] = FieldInfo(alias="CV", default=None)

    cz: Optional[int] = FieldInfo(alias="CZ", default=None)

    de: Optional[int] = FieldInfo(alias="DE", default=None)

    dk: Optional[int] = FieldInfo(alias="DK", default=None)

    ec: Optional[int] = FieldInfo(alias="EC", default=None)

    ee: Optional[int] = FieldInfo(alias="EE", default=None)

    eg: Optional[int] = FieldInfo(alias="EG", default=None)

    es: Optional[int] = FieldInfo(alias="ES", default=None)

    fi: Optional[int] = FieldInfo(alias="FI", default=None)

    fr: Optional[int] = FieldInfo(alias="FR", default=None)

    gb: Optional[int] = FieldInfo(alias="GB", default=None)

    gh: Optional[int] = FieldInfo(alias="GH", default=None)

    gr: Optional[int] = FieldInfo(alias="GR", default=None)

    gt: Optional[int] = FieldInfo(alias="GT", default=None)

    hk: Optional[int] = FieldInfo(alias="HK", default=None)

    hn: Optional[int] = FieldInfo(alias="HN", default=None)

    hu: Optional[int] = FieldInfo(alias="HU", default=None)

    id: Optional[int] = FieldInfo(alias="ID", default=None)

    ie: Optional[int] = FieldInfo(alias="IE", default=None)

    il: Optional[int] = FieldInfo(alias="IL", default=None)

    in_: Optional[int] = FieldInfo(alias="IN", default=None)

    it: Optional[int] = FieldInfo(alias="IT", default=None)

    jp: Optional[int] = FieldInfo(alias="JP", default=None)

    lt: Optional[int] = FieldInfo(alias="LT", default=None)

    lv: Optional[int] = FieldInfo(alias="LV", default=None)

    mu: Optional[int] = FieldInfo(alias="MU", default=None)

    mx: Optional[int] = FieldInfo(alias="MX", default=None)

    my: Optional[int] = FieldInfo(alias="MY", default=None)

    mz: Optional[int] = FieldInfo(alias="MZ", default=None)

    nl: Optional[int] = FieldInfo(alias="NL", default=None)

    no: Optional[int] = FieldInfo(alias="NO", default=None)

    nz: Optional[int] = FieldInfo(alias="NZ", default=None)

    pe: Optional[int] = FieldInfo(alias="PE", default=None)

    ph: Optional[int] = FieldInfo(alias="PH", default=None)

    pl: Optional[int] = FieldInfo(alias="PL", default=None)

    pt: Optional[int] = FieldInfo(alias="PT", default=None)

    py: Optional[int] = FieldInfo(alias="PY", default=None)

    ru: Optional[int] = FieldInfo(alias="RU", default=None)

    sa: Optional[int] = FieldInfo(alias="SA", default=None)

    se: Optional[int] = FieldInfo(alias="SE", default=None)

    sg: Optional[int] = FieldInfo(alias="SG", default=None)

    si: Optional[int] = FieldInfo(alias="SI", default=None)

    sk: Optional[int] = FieldInfo(alias="SK", default=None)

    th: Optional[int] = FieldInfo(alias="TH", default=None)

    tr: Optional[int] = FieldInfo(alias="TR", default=None)

    tw: Optional[int] = FieldInfo(alias="TW", default=None)

    ug: Optional[int] = FieldInfo(alias="UG", default=None)

    us: Optional[int] = FieldInfo(alias="US", default=None)

    ve: Optional[int] = FieldInfo(alias="VE", default=None)

    za: Optional[int] = FieldInfo(alias="ZA", default=None)


class Result(BaseModel):
    display_priorities: Optional[ResultDisplayPriorities] = None

    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class MovieListResponse(BaseModel):
    results: Optional[List[Result]] = None
