# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "WatchProviderListResponse",
    "Results",
    "ResultsAe",
    "ResultsAeFlatrate",
    "ResultsAr",
    "ResultsArFlatrate",
    "ResultsAt",
    "ResultsAtBuy",
    "ResultsAtFlatrate",
    "ResultsAu",
    "ResultsAuBuy",
    "ResultsAuFlatrate",
    "ResultsBa",
    "ResultsBaFlatrate",
    "ResultsBb",
    "ResultsBbFlatrate",
    "ResultsBe",
    "ResultsBeFlatrate",
    "ResultsBg",
    "ResultsBgFlatrate",
    "ResultsBo",
    "ResultsBoFlatrate",
    "ResultsBr",
    "ResultsBrFlatrate",
    "ResultsBs",
    "ResultsBsFlatrate",
    "ResultsCa",
    "ResultsCaBuy",
    "ResultsCaFlatrate",
    "ResultsCh",
    "ResultsChBuy",
    "ResultsChFlatrate",
    "ResultsCi",
    "ResultsCiFlatrate",
    "ResultsCl",
    "ResultsClFlatrate",
    "ResultsCo",
    "ResultsCoFlatrate",
    "ResultsCr",
    "ResultsCrFlatrate",
    "ResultsCz",
    "ResultsCzFlatrate",
    "ResultsDe",
    "ResultsDeBuy",
    "ResultsDeFlatrate",
    "ResultsDk",
    "ResultsDkFlatrate",
    "ResultsDo",
    "ResultsDoFlatrate",
    "ResultsDz",
    "ResultsDzFlatrate",
    "ResultsEc",
    "ResultsEcFlatrate",
    "ResultsEg",
    "ResultsEgFlatrate",
    "ResultsEs",
    "ResultsEsFlatrate",
    "ResultsFi",
    "ResultsFiBuy",
    "ResultsFiFlatrate",
    "ResultsFr",
    "ResultsFrBuy",
    "ResultsFrFlatrate",
    "ResultsGB",
    "ResultsGBBuy",
    "ResultsGBFlatrate",
    "ResultsGf",
    "ResultsGfFlatrate",
    "ResultsGh",
    "ResultsGhFlatrate",
    "ResultsGq",
    "ResultsGqFlatrate",
    "ResultsGt",
    "ResultsGtFlatrate",
    "ResultsHk",
    "ResultsHkFlatrate",
    "ResultsHn",
    "ResultsHnFlatrate",
    "ResultsHr",
    "ResultsHrFlatrate",
    "ResultsHu",
    "ResultsHuFlatrate",
    "ResultsID",
    "ResultsIDFlatrate",
    "ResultsIe",
    "ResultsIeBuy",
    "ResultsIeFlatrate",
    "ResultsIl",
    "ResultsIlFlatrate",
    "ResultsIq",
    "ResultsIqFlatrate",
    "ResultsIt",
    "ResultsItBuy",
    "ResultsItFlatrate",
    "ResultsJm",
    "ResultsJmFlatrate",
    "ResultsJp",
    "ResultsJpBuy",
    "ResultsJpFlatrate",
    "ResultsJpRent",
    "ResultsKe",
    "ResultsKeFlatrate",
    "ResultsKr",
    "ResultsKrFlatrate",
    "ResultsLb",
    "ResultsLbFlatrate",
    "ResultsLy",
    "ResultsLyFlatrate",
    "ResultsMd",
    "ResultsMdFlatrate",
    "ResultsMk",
    "ResultsMkFlatrate",
    "ResultsMu",
    "ResultsMuFlatrate",
    "ResultsMx",
    "ResultsMxFlatrate",
    "ResultsMy",
    "ResultsMyFlatrate",
    "ResultsMz",
    "ResultsMzFlatrate",
    "ResultsNe",
    "ResultsNeFlatrate",
    "ResultsNg",
    "ResultsNgFlatrate",
    "ResultsNl",
    "ResultsNlBuy",
    "ResultsNlFlatrate",
    "ResultsNo",
    "ResultsNoBuy",
    "ResultsNoFlatrate",
    "ResultsNz",
    "ResultsNzFlatrate",
    "ResultsPa",
    "ResultsPaFlatrate",
    "ResultsPe",
    "ResultsPeFlatrate",
    "ResultsPh",
    "ResultsPhFlatrate",
    "ResultsPl",
    "ResultsPlFlatrate",
    "ResultsPlRent",
    "ResultsPs",
    "ResultsPsFlatrate",
    "ResultsPt",
    "ResultsPtFlatrate",
    "ResultsPy",
    "ResultsPyFlatrate",
    "ResultsRo",
    "ResultsRoFlatrate",
    "ResultsRs",
    "ResultsRsFlatrate",
    "ResultsRu",
    "ResultsRuFlatrate",
    "ResultsSa",
    "ResultsSaFlatrate",
    "ResultsSc",
    "ResultsScFlatrate",
    "ResultsSe",
    "ResultsSeBuy",
    "ResultsSeFlatrate",
    "ResultsSg",
    "ResultsSgFlatrate",
    "ResultsSi",
    "ResultsSiFlatrate",
    "ResultsSk",
    "ResultsSkFlatrate",
    "ResultsSn",
    "ResultsSnFlatrate",
    "ResultsSv",
    "ResultsSvFlatrate",
    "ResultsTh",
    "ResultsThFlatrate",
    "ResultsTr",
    "ResultsTrFlatrate",
    "ResultsTt",
    "ResultsTtFlatrate",
    "ResultsTw",
    "ResultsTwFlatrate",
    "ResultsTz",
    "ResultsTzFlatrate",
    "ResultsUg",
    "ResultsUgFlatrate",
    "ResultsUs",
    "ResultsUsBuy",
    "ResultsUsFlatrate",
    "ResultsUsFree",
    "ResultsUy",
    "ResultsUyFlatrate",
    "ResultsVe",
    "ResultsVeFlatrate",
    "ResultsZa",
    "ResultsZaFlatrate",
    "ResultsZm",
    "ResultsZmFlatrate",
]


class ResultsAeFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsAe(BaseModel):
    flatrate: Optional[List[ResultsAeFlatrate]] = None

    link: Optional[str] = None


class ResultsArFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsAr(BaseModel):
    flatrate: Optional[List[ResultsArFlatrate]] = None

    link: Optional[str] = None


class ResultsAtBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsAtFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsAt(BaseModel):
    buy: Optional[List[ResultsAtBuy]] = None

    flatrate: Optional[List[ResultsAtFlatrate]] = None

    link: Optional[str] = None


class ResultsAuBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsAuFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsAu(BaseModel):
    buy: Optional[List[ResultsAuBuy]] = None

    flatrate: Optional[List[ResultsAuFlatrate]] = None

    link: Optional[str] = None


class ResultsBaFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsBa(BaseModel):
    flatrate: Optional[List[ResultsBaFlatrate]] = None

    link: Optional[str] = None


class ResultsBbFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsBb(BaseModel):
    flatrate: Optional[List[ResultsBbFlatrate]] = None

    link: Optional[str] = None


class ResultsBeFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsBe(BaseModel):
    flatrate: Optional[List[ResultsBeFlatrate]] = None

    link: Optional[str] = None


class ResultsBgFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsBg(BaseModel):
    flatrate: Optional[List[ResultsBgFlatrate]] = None

    link: Optional[str] = None


class ResultsBoFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsBo(BaseModel):
    flatrate: Optional[List[ResultsBoFlatrate]] = None

    link: Optional[str] = None


class ResultsBrFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsBr(BaseModel):
    flatrate: Optional[List[ResultsBrFlatrate]] = None

    link: Optional[str] = None


class ResultsBsFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsBs(BaseModel):
    flatrate: Optional[List[ResultsBsFlatrate]] = None

    link: Optional[str] = None


class ResultsCaBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsCaFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsCa(BaseModel):
    buy: Optional[List[ResultsCaBuy]] = None

    flatrate: Optional[List[ResultsCaFlatrate]] = None

    link: Optional[str] = None


class ResultsChBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsChFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsCh(BaseModel):
    buy: Optional[List[ResultsChBuy]] = None

    flatrate: Optional[List[ResultsChFlatrate]] = None

    link: Optional[str] = None


class ResultsCiFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsCi(BaseModel):
    flatrate: Optional[List[ResultsCiFlatrate]] = None

    link: Optional[str] = None


class ResultsClFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsCl(BaseModel):
    flatrate: Optional[List[ResultsClFlatrate]] = None

    link: Optional[str] = None


class ResultsCoFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsCo(BaseModel):
    flatrate: Optional[List[ResultsCoFlatrate]] = None

    link: Optional[str] = None


class ResultsCrFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsCr(BaseModel):
    flatrate: Optional[List[ResultsCrFlatrate]] = None

    link: Optional[str] = None


class ResultsCzFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsCz(BaseModel):
    flatrate: Optional[List[ResultsCzFlatrate]] = None

    link: Optional[str] = None


class ResultsDeBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsDeFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsDe(BaseModel):
    buy: Optional[List[ResultsDeBuy]] = None

    flatrate: Optional[List[ResultsDeFlatrate]] = None

    link: Optional[str] = None


class ResultsDkFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsDk(BaseModel):
    flatrate: Optional[List[ResultsDkFlatrate]] = None

    link: Optional[str] = None


class ResultsDoFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsDo(BaseModel):
    flatrate: Optional[List[ResultsDoFlatrate]] = None

    link: Optional[str] = None


class ResultsDzFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsDz(BaseModel):
    flatrate: Optional[List[ResultsDzFlatrate]] = None

    link: Optional[str] = None


class ResultsEcFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsEc(BaseModel):
    flatrate: Optional[List[ResultsEcFlatrate]] = None

    link: Optional[str] = None


class ResultsEgFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsEg(BaseModel):
    flatrate: Optional[List[ResultsEgFlatrate]] = None

    link: Optional[str] = None


class ResultsEsFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsEs(BaseModel):
    flatrate: Optional[List[ResultsEsFlatrate]] = None

    link: Optional[str] = None


class ResultsFiBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsFiFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsFi(BaseModel):
    buy: Optional[List[ResultsFiBuy]] = None

    flatrate: Optional[List[ResultsFiFlatrate]] = None

    link: Optional[str] = None


class ResultsFrBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsFrFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsFr(BaseModel):
    buy: Optional[List[ResultsFrBuy]] = None

    flatrate: Optional[List[ResultsFrFlatrate]] = None

    link: Optional[str] = None


class ResultsGBBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsGBFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsGB(BaseModel):
    buy: Optional[List[ResultsGBBuy]] = None

    flatrate: Optional[List[ResultsGBFlatrate]] = None

    link: Optional[str] = None


class ResultsGfFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsGf(BaseModel):
    flatrate: Optional[List[ResultsGfFlatrate]] = None

    link: Optional[str] = None


class ResultsGhFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsGh(BaseModel):
    flatrate: Optional[List[ResultsGhFlatrate]] = None

    link: Optional[str] = None


class ResultsGqFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsGq(BaseModel):
    flatrate: Optional[List[ResultsGqFlatrate]] = None

    link: Optional[str] = None


class ResultsGtFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsGt(BaseModel):
    flatrate: Optional[List[ResultsGtFlatrate]] = None

    link: Optional[str] = None


class ResultsHkFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsHk(BaseModel):
    flatrate: Optional[List[ResultsHkFlatrate]] = None

    link: Optional[str] = None


class ResultsHnFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsHn(BaseModel):
    flatrate: Optional[List[ResultsHnFlatrate]] = None

    link: Optional[str] = None


class ResultsHrFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsHr(BaseModel):
    flatrate: Optional[List[ResultsHrFlatrate]] = None

    link: Optional[str] = None


class ResultsHuFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsHu(BaseModel):
    flatrate: Optional[List[ResultsHuFlatrate]] = None

    link: Optional[str] = None


class ResultsIDFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsID(BaseModel):
    flatrate: Optional[List[ResultsIDFlatrate]] = None

    link: Optional[str] = None


class ResultsIeBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsIeFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsIe(BaseModel):
    buy: Optional[List[ResultsIeBuy]] = None

    flatrate: Optional[List[ResultsIeFlatrate]] = None

    link: Optional[str] = None


class ResultsIlFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsIl(BaseModel):
    flatrate: Optional[List[ResultsIlFlatrate]] = None

    link: Optional[str] = None


class ResultsIqFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsIq(BaseModel):
    flatrate: Optional[List[ResultsIqFlatrate]] = None

    link: Optional[str] = None


class ResultsItBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsItFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsIt(BaseModel):
    buy: Optional[List[ResultsItBuy]] = None

    flatrate: Optional[List[ResultsItFlatrate]] = None

    link: Optional[str] = None


class ResultsJmFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsJm(BaseModel):
    flatrate: Optional[List[ResultsJmFlatrate]] = None

    link: Optional[str] = None


class ResultsJpBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsJpFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsJpRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsJp(BaseModel):
    buy: Optional[List[ResultsJpBuy]] = None

    flatrate: Optional[List[ResultsJpFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsJpRent]] = None


class ResultsKeFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsKe(BaseModel):
    flatrate: Optional[List[ResultsKeFlatrate]] = None

    link: Optional[str] = None


class ResultsKrFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsKr(BaseModel):
    flatrate: Optional[List[ResultsKrFlatrate]] = None

    link: Optional[str] = None


class ResultsLbFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsLb(BaseModel):
    flatrate: Optional[List[ResultsLbFlatrate]] = None

    link: Optional[str] = None


class ResultsLyFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsLy(BaseModel):
    flatrate: Optional[List[ResultsLyFlatrate]] = None

    link: Optional[str] = None


class ResultsMdFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsMd(BaseModel):
    flatrate: Optional[List[ResultsMdFlatrate]] = None

    link: Optional[str] = None


class ResultsMkFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsMk(BaseModel):
    flatrate: Optional[List[ResultsMkFlatrate]] = None

    link: Optional[str] = None


class ResultsMuFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsMu(BaseModel):
    flatrate: Optional[List[ResultsMuFlatrate]] = None

    link: Optional[str] = None


class ResultsMxFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsMx(BaseModel):
    flatrate: Optional[List[ResultsMxFlatrate]] = None

    link: Optional[str] = None


class ResultsMyFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsMy(BaseModel):
    flatrate: Optional[List[ResultsMyFlatrate]] = None

    link: Optional[str] = None


class ResultsMzFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsMz(BaseModel):
    flatrate: Optional[List[ResultsMzFlatrate]] = None

    link: Optional[str] = None


class ResultsNeFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsNe(BaseModel):
    flatrate: Optional[List[ResultsNeFlatrate]] = None

    link: Optional[str] = None


class ResultsNgFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsNg(BaseModel):
    flatrate: Optional[List[ResultsNgFlatrate]] = None

    link: Optional[str] = None


class ResultsNlBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsNlFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsNl(BaseModel):
    buy: Optional[List[ResultsNlBuy]] = None

    flatrate: Optional[List[ResultsNlFlatrate]] = None

    link: Optional[str] = None


class ResultsNoBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsNoFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsNo(BaseModel):
    buy: Optional[List[ResultsNoBuy]] = None

    flatrate: Optional[List[ResultsNoFlatrate]] = None

    link: Optional[str] = None


class ResultsNzFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsNz(BaseModel):
    flatrate: Optional[List[ResultsNzFlatrate]] = None

    link: Optional[str] = None


class ResultsPaFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsPa(BaseModel):
    flatrate: Optional[List[ResultsPaFlatrate]] = None

    link: Optional[str] = None


class ResultsPeFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsPe(BaseModel):
    flatrate: Optional[List[ResultsPeFlatrate]] = None

    link: Optional[str] = None


class ResultsPhFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsPh(BaseModel):
    flatrate: Optional[List[ResultsPhFlatrate]] = None

    link: Optional[str] = None


class ResultsPlFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsPlRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsPl(BaseModel):
    flatrate: Optional[List[ResultsPlFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsPlRent]] = None


class ResultsPsFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsPs(BaseModel):
    flatrate: Optional[List[ResultsPsFlatrate]] = None

    link: Optional[str] = None


class ResultsPtFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsPt(BaseModel):
    flatrate: Optional[List[ResultsPtFlatrate]] = None

    link: Optional[str] = None


class ResultsPyFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsPy(BaseModel):
    flatrate: Optional[List[ResultsPyFlatrate]] = None

    link: Optional[str] = None


class ResultsRoFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsRo(BaseModel):
    flatrate: Optional[List[ResultsRoFlatrate]] = None

    link: Optional[str] = None


class ResultsRsFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsRs(BaseModel):
    flatrate: Optional[List[ResultsRsFlatrate]] = None

    link: Optional[str] = None


class ResultsRuFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsRu(BaseModel):
    flatrate: Optional[List[ResultsRuFlatrate]] = None

    link: Optional[str] = None


class ResultsSaFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsSa(BaseModel):
    flatrate: Optional[List[ResultsSaFlatrate]] = None

    link: Optional[str] = None


class ResultsScFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsSc(BaseModel):
    flatrate: Optional[List[ResultsScFlatrate]] = None

    link: Optional[str] = None


class ResultsSeBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsSeFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsSe(BaseModel):
    buy: Optional[List[ResultsSeBuy]] = None

    flatrate: Optional[List[ResultsSeFlatrate]] = None

    link: Optional[str] = None


class ResultsSgFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsSg(BaseModel):
    flatrate: Optional[List[ResultsSgFlatrate]] = None

    link: Optional[str] = None


class ResultsSiFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsSi(BaseModel):
    flatrate: Optional[List[ResultsSiFlatrate]] = None

    link: Optional[str] = None


class ResultsSkFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsSk(BaseModel):
    flatrate: Optional[List[ResultsSkFlatrate]] = None

    link: Optional[str] = None


class ResultsSnFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsSn(BaseModel):
    flatrate: Optional[List[ResultsSnFlatrate]] = None

    link: Optional[str] = None


class ResultsSvFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsSv(BaseModel):
    flatrate: Optional[List[ResultsSvFlatrate]] = None

    link: Optional[str] = None


class ResultsThFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsTh(BaseModel):
    flatrate: Optional[List[ResultsThFlatrate]] = None

    link: Optional[str] = None


class ResultsTrFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsTr(BaseModel):
    flatrate: Optional[List[ResultsTrFlatrate]] = None

    link: Optional[str] = None


class ResultsTtFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsTt(BaseModel):
    flatrate: Optional[List[ResultsTtFlatrate]] = None

    link: Optional[str] = None


class ResultsTwFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsTw(BaseModel):
    flatrate: Optional[List[ResultsTwFlatrate]] = None

    link: Optional[str] = None


class ResultsTzFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsTz(BaseModel):
    flatrate: Optional[List[ResultsTzFlatrate]] = None

    link: Optional[str] = None


class ResultsUgFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsUg(BaseModel):
    flatrate: Optional[List[ResultsUgFlatrate]] = None

    link: Optional[str] = None


class ResultsUsBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsUsFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsUsFree(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsUs(BaseModel):
    buy: Optional[List[ResultsUsBuy]] = None

    flatrate: Optional[List[ResultsUsFlatrate]] = None

    free: Optional[List[ResultsUsFree]] = None

    link: Optional[str] = None


class ResultsUyFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsUy(BaseModel):
    flatrate: Optional[List[ResultsUyFlatrate]] = None

    link: Optional[str] = None


class ResultsVeFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsVe(BaseModel):
    flatrate: Optional[List[ResultsVeFlatrate]] = None

    link: Optional[str] = None


class ResultsZaFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsZa(BaseModel):
    flatrate: Optional[List[ResultsZaFlatrate]] = None

    link: Optional[str] = None


class ResultsZmFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsZm(BaseModel):
    flatrate: Optional[List[ResultsZmFlatrate]] = None

    link: Optional[str] = None


class Results(BaseModel):
    ae: Optional[ResultsAe] = FieldInfo(alias="AE", default=None)

    ar: Optional[ResultsAr] = FieldInfo(alias="AR", default=None)

    at: Optional[ResultsAt] = FieldInfo(alias="AT", default=None)

    au: Optional[ResultsAu] = FieldInfo(alias="AU", default=None)

    ba: Optional[ResultsBa] = FieldInfo(alias="BA", default=None)

    bb: Optional[ResultsBb] = FieldInfo(alias="BB", default=None)

    be: Optional[ResultsBe] = FieldInfo(alias="BE", default=None)

    bg: Optional[ResultsBg] = FieldInfo(alias="BG", default=None)

    bo: Optional[ResultsBo] = FieldInfo(alias="BO", default=None)

    br: Optional[ResultsBr] = FieldInfo(alias="BR", default=None)

    bs: Optional[ResultsBs] = FieldInfo(alias="BS", default=None)

    ca: Optional[ResultsCa] = FieldInfo(alias="CA", default=None)

    ch: Optional[ResultsCh] = FieldInfo(alias="CH", default=None)

    ci: Optional[ResultsCi] = FieldInfo(alias="CI", default=None)

    cl: Optional[ResultsCl] = FieldInfo(alias="CL", default=None)

    co: Optional[ResultsCo] = FieldInfo(alias="CO", default=None)

    cr: Optional[ResultsCr] = FieldInfo(alias="CR", default=None)

    cz: Optional[ResultsCz] = FieldInfo(alias="CZ", default=None)

    de: Optional[ResultsDe] = FieldInfo(alias="DE", default=None)

    dk: Optional[ResultsDk] = FieldInfo(alias="DK", default=None)

    do: Optional[ResultsDo] = FieldInfo(alias="DO", default=None)

    dz: Optional[ResultsDz] = FieldInfo(alias="DZ", default=None)

    ec: Optional[ResultsEc] = FieldInfo(alias="EC", default=None)

    eg: Optional[ResultsEg] = FieldInfo(alias="EG", default=None)

    es: Optional[ResultsEs] = FieldInfo(alias="ES", default=None)

    fi: Optional[ResultsFi] = FieldInfo(alias="FI", default=None)

    fr: Optional[ResultsFr] = FieldInfo(alias="FR", default=None)

    gb: Optional[ResultsGB] = FieldInfo(alias="GB", default=None)

    gf: Optional[ResultsGf] = FieldInfo(alias="GF", default=None)

    gh: Optional[ResultsGh] = FieldInfo(alias="GH", default=None)

    gq: Optional[ResultsGq] = FieldInfo(alias="GQ", default=None)

    gt: Optional[ResultsGt] = FieldInfo(alias="GT", default=None)

    hk: Optional[ResultsHk] = FieldInfo(alias="HK", default=None)

    hn: Optional[ResultsHn] = FieldInfo(alias="HN", default=None)

    hr: Optional[ResultsHr] = FieldInfo(alias="HR", default=None)

    hu: Optional[ResultsHu] = FieldInfo(alias="HU", default=None)

    id: Optional[ResultsID] = FieldInfo(alias="ID", default=None)

    ie: Optional[ResultsIe] = FieldInfo(alias="IE", default=None)

    il: Optional[ResultsIl] = FieldInfo(alias="IL", default=None)

    iq: Optional[ResultsIq] = FieldInfo(alias="IQ", default=None)

    it: Optional[ResultsIt] = FieldInfo(alias="IT", default=None)

    jm: Optional[ResultsJm] = FieldInfo(alias="JM", default=None)

    jp: Optional[ResultsJp] = FieldInfo(alias="JP", default=None)

    ke: Optional[ResultsKe] = FieldInfo(alias="KE", default=None)

    kr: Optional[ResultsKr] = FieldInfo(alias="KR", default=None)

    lb: Optional[ResultsLb] = FieldInfo(alias="LB", default=None)

    ly: Optional[ResultsLy] = FieldInfo(alias="LY", default=None)

    md: Optional[ResultsMd] = FieldInfo(alias="MD", default=None)

    mk: Optional[ResultsMk] = FieldInfo(alias="MK", default=None)

    mu: Optional[ResultsMu] = FieldInfo(alias="MU", default=None)

    mx: Optional[ResultsMx] = FieldInfo(alias="MX", default=None)

    my: Optional[ResultsMy] = FieldInfo(alias="MY", default=None)

    mz: Optional[ResultsMz] = FieldInfo(alias="MZ", default=None)

    ne: Optional[ResultsNe] = FieldInfo(alias="NE", default=None)

    ng: Optional[ResultsNg] = FieldInfo(alias="NG", default=None)

    nl: Optional[ResultsNl] = FieldInfo(alias="NL", default=None)

    no: Optional[ResultsNo] = FieldInfo(alias="NO", default=None)

    nz: Optional[ResultsNz] = FieldInfo(alias="NZ", default=None)

    pa: Optional[ResultsPa] = FieldInfo(alias="PA", default=None)

    pe: Optional[ResultsPe] = FieldInfo(alias="PE", default=None)

    ph: Optional[ResultsPh] = FieldInfo(alias="PH", default=None)

    pl: Optional[ResultsPl] = FieldInfo(alias="PL", default=None)

    ps: Optional[ResultsPs] = FieldInfo(alias="PS", default=None)

    pt: Optional[ResultsPt] = FieldInfo(alias="PT", default=None)

    py: Optional[ResultsPy] = FieldInfo(alias="PY", default=None)

    ro: Optional[ResultsRo] = FieldInfo(alias="RO", default=None)

    rs: Optional[ResultsRs] = FieldInfo(alias="RS", default=None)

    ru: Optional[ResultsRu] = FieldInfo(alias="RU", default=None)

    sa: Optional[ResultsSa] = FieldInfo(alias="SA", default=None)

    sc: Optional[ResultsSc] = FieldInfo(alias="SC", default=None)

    se: Optional[ResultsSe] = FieldInfo(alias="SE", default=None)

    sg: Optional[ResultsSg] = FieldInfo(alias="SG", default=None)

    si: Optional[ResultsSi] = FieldInfo(alias="SI", default=None)

    sk: Optional[ResultsSk] = FieldInfo(alias="SK", default=None)

    sn: Optional[ResultsSn] = FieldInfo(alias="SN", default=None)

    sv: Optional[ResultsSv] = FieldInfo(alias="SV", default=None)

    th: Optional[ResultsTh] = FieldInfo(alias="TH", default=None)

    tr: Optional[ResultsTr] = FieldInfo(alias="TR", default=None)

    tt: Optional[ResultsTt] = FieldInfo(alias="TT", default=None)

    tw: Optional[ResultsTw] = FieldInfo(alias="TW", default=None)

    tz: Optional[ResultsTz] = FieldInfo(alias="TZ", default=None)

    ug: Optional[ResultsUg] = FieldInfo(alias="UG", default=None)

    us: Optional[ResultsUs] = FieldInfo(alias="US", default=None)

    uy: Optional[ResultsUy] = FieldInfo(alias="UY", default=None)

    ve: Optional[ResultsVe] = FieldInfo(alias="VE", default=None)

    za: Optional[ResultsZa] = FieldInfo(alias="ZA", default=None)

    zm: Optional[ResultsZm] = FieldInfo(alias="ZM", default=None)


class WatchProviderListResponse(BaseModel):
    id: Optional[int] = None

    results: Optional[Results] = None
