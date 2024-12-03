# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "WatchProviderListResponse",
    "Results",
    "ResultsAe",
    "ResultsAeBuy",
    "ResultsAeFlatrate",
    "ResultsAeRent",
    "ResultsAl",
    "ResultsAlBuy",
    "ResultsAr",
    "ResultsArBuy",
    "ResultsArFlatrate",
    "ResultsArRent",
    "ResultsAt",
    "ResultsAtBuy",
    "ResultsAtFlatrate",
    "ResultsAtRent",
    "ResultsAu",
    "ResultsAuBuy",
    "ResultsAuFlatrate",
    "ResultsBa",
    "ResultsBaBuy",
    "ResultsBaFlatrate",
    "ResultsBb",
    "ResultsBbFlatrate",
    "ResultsBe",
    "ResultsBeBuy",
    "ResultsBeFlatrate",
    "ResultsBeRent",
    "ResultsBg",
    "ResultsBgBuy",
    "ResultsBgFlatrate",
    "ResultsBgRent",
    "ResultsBh",
    "ResultsBhBuy",
    "ResultsBo",
    "ResultsBoFlatrate",
    "ResultsBr",
    "ResultsBrFlatrate",
    "ResultsBs",
    "ResultsBsFlatrate",
    "ResultsCa",
    "ResultsCaBuy",
    "ResultsCaFlatrate",
    "ResultsCaRent",
    "ResultsCh",
    "ResultsChBuy",
    "ResultsChFlatrate",
    "ResultsChRent",
    "ResultsCl",
    "ResultsClBuy",
    "ResultsClFlatrate",
    "ResultsClRent",
    "ResultsCo",
    "ResultsCoBuy",
    "ResultsCoFlatrate",
    "ResultsCoRent",
    "ResultsCr",
    "ResultsCrFlatrate",
    "ResultsCv",
    "ResultsCvBuy",
    "ResultsCvRent",
    "ResultsCz",
    "ResultsCzBuy",
    "ResultsCzFlatrate",
    "ResultsCzRent",
    "ResultsDe",
    "ResultsDeBuy",
    "ResultsDeFlatrate",
    "ResultsDeRent",
    "ResultsDk",
    "ResultsDkBuy",
    "ResultsDkFlatrate",
    "ResultsDkRent",
    "ResultsDo",
    "ResultsDoFlatrate",
    "ResultsEc",
    "ResultsEcBuy",
    "ResultsEcFlatrate",
    "ResultsEcRent",
    "ResultsEe",
    "ResultsEeBuy",
    "ResultsEeFlatrate",
    "ResultsEeRent",
    "ResultsEg",
    "ResultsEgBuy",
    "ResultsEgRent",
    "ResultsEs",
    "ResultsEsAd",
    "ResultsEsBuy",
    "ResultsEsFlatrate",
    "ResultsEsRent",
    "ResultsFi",
    "ResultsFiBuy",
    "ResultsFiFlatrate",
    "ResultsFiRent",
    "ResultsFj",
    "ResultsFjBuy",
    "ResultsFr",
    "ResultsFrBuy",
    "ResultsFrFlatrate",
    "ResultsFrRent",
    "ResultsGB",
    "ResultsGBBuy",
    "ResultsGBFlatrate",
    "ResultsGBRent",
    "ResultsGf",
    "ResultsGfFlatrate",
    "ResultsGi",
    "ResultsGiFlatrate",
    "ResultsGr",
    "ResultsGrBuy",
    "ResultsGrFlatrate",
    "ResultsGrRent",
    "ResultsGt",
    "ResultsGtFlatrate",
    "ResultsHk",
    "ResultsHkFlatrate",
    "ResultsHn",
    "ResultsHnFlatrate",
    "ResultsHr",
    "ResultsHrAd",
    "ResultsHrBuy",
    "ResultsHrFlatrate",
    "ResultsHu",
    "ResultsHuBuy",
    "ResultsHuFlatrate",
    "ResultsHuRent",
    "ResultsID",
    "ResultsIDFlatrate",
    "ResultsIe",
    "ResultsIeBuy",
    "ResultsIeFlatrate",
    "ResultsIeRent",
    "ResultsIl",
    "ResultsIlBuy",
    "ResultsIlFlatrate",
    "ResultsIn",
    "ResultsInBuy",
    "ResultsInFlatrate",
    "ResultsInRent",
    "ResultsIq",
    "ResultsIqFlatrate",
    "ResultsIs",
    "ResultsIsBuy",
    "ResultsIsFlatrate",
    "ResultsIt",
    "ResultsItBuy",
    "ResultsItFlatrate",
    "ResultsItRent",
    "ResultsJm",
    "ResultsJmFlatrate",
    "ResultsJo",
    "ResultsJoBuy",
    "ResultsJoFlatrate",
    "ResultsJp",
    "ResultsJpBuy",
    "ResultsJpFlatrate",
    "ResultsJpRent",
    "ResultsKr",
    "ResultsKrBuy",
    "ResultsKrFlatrate",
    "ResultsKw",
    "ResultsKwBuy",
    "ResultsKwFlatrate",
    "ResultsLb",
    "ResultsLbBuy",
    "ResultsLbFlatrate",
    "ResultsLi",
    "ResultsLiFlatrate",
    "ResultsLt",
    "ResultsLtBuy",
    "ResultsLtFlatrate",
    "ResultsLtRent",
    "ResultsLv",
    "ResultsLvBuy",
    "ResultsLvFlatrate",
    "ResultsMd",
    "ResultsMdBuy",
    "ResultsMdFlatrate",
    "ResultsMk",
    "ResultsMkBuy",
    "ResultsMkFlatrate",
    "ResultsMt",
    "ResultsMtBuy",
    "ResultsMtFlatrate",
    "ResultsMtRent",
    "ResultsMu",
    "ResultsMuBuy",
    "ResultsMuRent",
    "ResultsMx",
    "ResultsMxFlatrate",
    "ResultsMy",
    "ResultsMyFlatrate",
    "ResultsMz",
    "ResultsMzBuy",
    "ResultsMzRent",
    "ResultsNl",
    "ResultsNlBuy",
    "ResultsNlFlatrate",
    "ResultsNlRent",
    "ResultsNo",
    "ResultsNoBuy",
    "ResultsNoFlatrate",
    "ResultsNoRent",
    "ResultsNz",
    "ResultsNzBuy",
    "ResultsNzFlatrate",
    "ResultsOm",
    "ResultsOmBuy",
    "ResultsOmFlatrate",
    "ResultsOmRent",
    "ResultsPa",
    "ResultsPaFlatrate",
    "ResultsPe",
    "ResultsPeBuy",
    "ResultsPeFlatrate",
    "ResultsPeRent",
    "ResultsPh",
    "ResultsPhFlatrate",
    "ResultsPk",
    "ResultsPkFlatrate",
    "ResultsPl",
    "ResultsPlBuy",
    "ResultsPlFlatrate",
    "ResultsPlRent",
    "ResultsPs",
    "ResultsPsFlatrate",
    "ResultsPt",
    "ResultsPtBuy",
    "ResultsPtFlatrate",
    "ResultsPtRent",
    "ResultsPy",
    "ResultsPyFlatrate",
    "ResultsQa",
    "ResultsQaBuy",
    "ResultsQaFlatrate",
    "ResultsRo",
    "ResultsRoFlatrate",
    "ResultsRs",
    "ResultsRsBuy",
    "ResultsRsFlatrate",
    "ResultsRu",
    "ResultsRuBuy",
    "ResultsRuFlatrate",
    "ResultsRuRent",
    "ResultsSa",
    "ResultsSaBuy",
    "ResultsSaFlatrate",
    "ResultsSaRent",
    "ResultsSe",
    "ResultsSeBuy",
    "ResultsSeFlatrate",
    "ResultsSeRent",
    "ResultsSg",
    "ResultsSgFlatrate",
    "ResultsSi",
    "ResultsSiBuy",
    "ResultsSiFlatrate",
    "ResultsSk",
    "ResultsSkBuy",
    "ResultsSkFlatrate",
    "ResultsSkRent",
    "ResultsSm",
    "ResultsSmFlatrate",
    "ResultsSv",
    "ResultsSvFlatrate",
    "ResultsTh",
    "ResultsThFlatrate",
    "ResultsTr",
    "ResultsTrBuy",
    "ResultsTrFlatrate",
    "ResultsTrRent",
    "ResultsTt",
    "ResultsTtFlatrate",
    "ResultsTw",
    "ResultsTwFlatrate",
    "ResultsUg",
    "ResultsUgBuy",
    "ResultsUgRent",
    "ResultsUs",
    "ResultsUsBuy",
    "ResultsUsFlatrate",
    "ResultsUsRent",
    "ResultsUy",
    "ResultsUyFlatrate",
    "ResultsVe",
    "ResultsVeBuy",
    "ResultsVeFlatrate",
    "ResultsVeRent",
    "ResultsYe",
    "ResultsYeFlatrate",
    "ResultsZa",
    "ResultsZaBuy",
    "ResultsZaFlatrate",
    "ResultsZaRent",
]


class ResultsAeBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsAeFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsAeRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsAe(BaseModel):
    buy: Optional[List[ResultsAeBuy]] = None

    flatrate: Optional[List[ResultsAeFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsAeRent]] = None


class ResultsAlBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsAl(BaseModel):
    buy: Optional[List[ResultsAlBuy]] = None

    link: Optional[str] = None


class ResultsArBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsArFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsArRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsAr(BaseModel):
    buy: Optional[List[ResultsArBuy]] = None

    flatrate: Optional[List[ResultsArFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsArRent]] = None


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


class ResultsAtRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsAt(BaseModel):
    buy: Optional[List[ResultsAtBuy]] = None

    flatrate: Optional[List[ResultsAtFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsAtRent]] = None


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


class ResultsBaBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsBaFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsBa(BaseModel):
    buy: Optional[List[ResultsBaBuy]] = None

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


class ResultsBeBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsBeFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsBeRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsBe(BaseModel):
    buy: Optional[List[ResultsBeBuy]] = None

    flatrate: Optional[List[ResultsBeFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsBeRent]] = None


class ResultsBgBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsBgFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsBgRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsBg(BaseModel):
    buy: Optional[List[ResultsBgBuy]] = None

    flatrate: Optional[List[ResultsBgFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsBgRent]] = None


class ResultsBhBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsBh(BaseModel):
    buy: Optional[List[ResultsBhBuy]] = None

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


class ResultsCaRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsCa(BaseModel):
    buy: Optional[List[ResultsCaBuy]] = None

    flatrate: Optional[List[ResultsCaFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsCaRent]] = None


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


class ResultsChRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsCh(BaseModel):
    buy: Optional[List[ResultsChBuy]] = None

    flatrate: Optional[List[ResultsChFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsChRent]] = None


class ResultsClBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsClFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsClRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsCl(BaseModel):
    buy: Optional[List[ResultsClBuy]] = None

    flatrate: Optional[List[ResultsClFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsClRent]] = None


class ResultsCoBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsCoFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsCoRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsCo(BaseModel):
    buy: Optional[List[ResultsCoBuy]] = None

    flatrate: Optional[List[ResultsCoFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsCoRent]] = None


class ResultsCrFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsCr(BaseModel):
    flatrate: Optional[List[ResultsCrFlatrate]] = None

    link: Optional[str] = None


class ResultsCvBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsCvRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsCv(BaseModel):
    buy: Optional[List[ResultsCvBuy]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsCvRent]] = None


class ResultsCzBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsCzFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsCzRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsCz(BaseModel):
    buy: Optional[List[ResultsCzBuy]] = None

    flatrate: Optional[List[ResultsCzFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsCzRent]] = None


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


class ResultsDeRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsDe(BaseModel):
    buy: Optional[List[ResultsDeBuy]] = None

    flatrate: Optional[List[ResultsDeFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsDeRent]] = None


class ResultsDkBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsDkFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsDkRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsDk(BaseModel):
    buy: Optional[List[ResultsDkBuy]] = None

    flatrate: Optional[List[ResultsDkFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsDkRent]] = None


class ResultsDoFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsDo(BaseModel):
    flatrate: Optional[List[ResultsDoFlatrate]] = None

    link: Optional[str] = None


class ResultsEcBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsEcFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsEcRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsEc(BaseModel):
    buy: Optional[List[ResultsEcBuy]] = None

    flatrate: Optional[List[ResultsEcFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsEcRent]] = None


class ResultsEeBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsEeFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsEeRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsEe(BaseModel):
    buy: Optional[List[ResultsEeBuy]] = None

    flatrate: Optional[List[ResultsEeFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsEeRent]] = None


class ResultsEgBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsEgRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsEg(BaseModel):
    buy: Optional[List[ResultsEgBuy]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsEgRent]] = None


class ResultsEsAd(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsEsBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsEsFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsEsRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsEs(BaseModel):
    ads: Optional[List[ResultsEsAd]] = None

    buy: Optional[List[ResultsEsBuy]] = None

    flatrate: Optional[List[ResultsEsFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsEsRent]] = None


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


class ResultsFiRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsFi(BaseModel):
    buy: Optional[List[ResultsFiBuy]] = None

    flatrate: Optional[List[ResultsFiFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsFiRent]] = None


class ResultsFjBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsFj(BaseModel):
    buy: Optional[List[ResultsFjBuy]] = None

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


class ResultsFrRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsFr(BaseModel):
    buy: Optional[List[ResultsFrBuy]] = None

    flatrate: Optional[List[ResultsFrFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsFrRent]] = None


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


class ResultsGBRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsGB(BaseModel):
    buy: Optional[List[ResultsGBBuy]] = None

    flatrate: Optional[List[ResultsGBFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsGBRent]] = None


class ResultsGfFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsGf(BaseModel):
    flatrate: Optional[List[ResultsGfFlatrate]] = None

    link: Optional[str] = None


class ResultsGiFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsGi(BaseModel):
    flatrate: Optional[List[ResultsGiFlatrate]] = None

    link: Optional[str] = None


class ResultsGrBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsGrFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsGrRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsGr(BaseModel):
    buy: Optional[List[ResultsGrBuy]] = None

    flatrate: Optional[List[ResultsGrFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsGrRent]] = None


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


class ResultsHrAd(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsHrBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsHrFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsHr(BaseModel):
    ads: Optional[List[ResultsHrAd]] = None

    buy: Optional[List[ResultsHrBuy]] = None

    flatrate: Optional[List[ResultsHrFlatrate]] = None

    link: Optional[str] = None


class ResultsHuBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsHuFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsHuRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsHu(BaseModel):
    buy: Optional[List[ResultsHuBuy]] = None

    flatrate: Optional[List[ResultsHuFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsHuRent]] = None


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


class ResultsIeRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsIe(BaseModel):
    buy: Optional[List[ResultsIeBuy]] = None

    flatrate: Optional[List[ResultsIeFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsIeRent]] = None


class ResultsIlBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsIlFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsIl(BaseModel):
    buy: Optional[List[ResultsIlBuy]] = None

    flatrate: Optional[List[ResultsIlFlatrate]] = None

    link: Optional[str] = None


class ResultsInBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsInFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsInRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsIn(BaseModel):
    buy: Optional[List[ResultsInBuy]] = None

    flatrate: Optional[List[ResultsInFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsInRent]] = None


class ResultsIqFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsIq(BaseModel):
    flatrate: Optional[List[ResultsIqFlatrate]] = None

    link: Optional[str] = None


class ResultsIsBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsIsFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsIs(BaseModel):
    buy: Optional[List[ResultsIsBuy]] = None

    flatrate: Optional[List[ResultsIsFlatrate]] = None

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


class ResultsItRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsIt(BaseModel):
    buy: Optional[List[ResultsItBuy]] = None

    flatrate: Optional[List[ResultsItFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsItRent]] = None


class ResultsJmFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsJm(BaseModel):
    flatrate: Optional[List[ResultsJmFlatrate]] = None

    link: Optional[str] = None


class ResultsJoBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsJoFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsJo(BaseModel):
    buy: Optional[List[ResultsJoBuy]] = None

    flatrate: Optional[List[ResultsJoFlatrate]] = None

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


class ResultsKrBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsKrFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsKr(BaseModel):
    buy: Optional[List[ResultsKrBuy]] = None

    flatrate: Optional[List[ResultsKrFlatrate]] = None

    link: Optional[str] = None


class ResultsKwBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsKwFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsKw(BaseModel):
    buy: Optional[List[ResultsKwBuy]] = None

    flatrate: Optional[List[ResultsKwFlatrate]] = None

    link: Optional[str] = None


class ResultsLbBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsLbFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsLb(BaseModel):
    buy: Optional[List[ResultsLbBuy]] = None

    flatrate: Optional[List[ResultsLbFlatrate]] = None

    link: Optional[str] = None


class ResultsLiFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsLi(BaseModel):
    flatrate: Optional[List[ResultsLiFlatrate]] = None

    link: Optional[str] = None


class ResultsLtBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsLtFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsLtRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsLt(BaseModel):
    buy: Optional[List[ResultsLtBuy]] = None

    flatrate: Optional[List[ResultsLtFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsLtRent]] = None


class ResultsLvBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsLvFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsLv(BaseModel):
    buy: Optional[List[ResultsLvBuy]] = None

    flatrate: Optional[List[ResultsLvFlatrate]] = None

    link: Optional[str] = None


class ResultsMdBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsMdFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsMd(BaseModel):
    buy: Optional[List[ResultsMdBuy]] = None

    flatrate: Optional[List[ResultsMdFlatrate]] = None

    link: Optional[str] = None


class ResultsMkBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsMkFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsMk(BaseModel):
    buy: Optional[List[ResultsMkBuy]] = None

    flatrate: Optional[List[ResultsMkFlatrate]] = None

    link: Optional[str] = None


class ResultsMtBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsMtFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsMtRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsMt(BaseModel):
    buy: Optional[List[ResultsMtBuy]] = None

    flatrate: Optional[List[ResultsMtFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsMtRent]] = None


class ResultsMuBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsMuRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsMu(BaseModel):
    buy: Optional[List[ResultsMuBuy]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsMuRent]] = None


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


class ResultsMzBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsMzRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsMz(BaseModel):
    buy: Optional[List[ResultsMzBuy]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsMzRent]] = None


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


class ResultsNlRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsNl(BaseModel):
    buy: Optional[List[ResultsNlBuy]] = None

    flatrate: Optional[List[ResultsNlFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsNlRent]] = None


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


class ResultsNoRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsNo(BaseModel):
    buy: Optional[List[ResultsNoBuy]] = None

    flatrate: Optional[List[ResultsNoFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsNoRent]] = None


class ResultsNzBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsNzFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsNz(BaseModel):
    buy: Optional[List[ResultsNzBuy]] = None

    flatrate: Optional[List[ResultsNzFlatrate]] = None

    link: Optional[str] = None


class ResultsOmBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsOmFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsOmRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsOm(BaseModel):
    buy: Optional[List[ResultsOmBuy]] = None

    flatrate: Optional[List[ResultsOmFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsOmRent]] = None


class ResultsPaFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsPa(BaseModel):
    flatrate: Optional[List[ResultsPaFlatrate]] = None

    link: Optional[str] = None


class ResultsPeBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsPeFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsPeRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsPe(BaseModel):
    buy: Optional[List[ResultsPeBuy]] = None

    flatrate: Optional[List[ResultsPeFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsPeRent]] = None


class ResultsPhFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsPh(BaseModel):
    flatrate: Optional[List[ResultsPhFlatrate]] = None

    link: Optional[str] = None


class ResultsPkFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsPk(BaseModel):
    flatrate: Optional[List[ResultsPkFlatrate]] = None

    link: Optional[str] = None


class ResultsPlBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


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
    buy: Optional[List[ResultsPlBuy]] = None

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


class ResultsPtBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsPtFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsPtRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsPt(BaseModel):
    buy: Optional[List[ResultsPtBuy]] = None

    flatrate: Optional[List[ResultsPtFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsPtRent]] = None


class ResultsPyFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsPy(BaseModel):
    flatrate: Optional[List[ResultsPyFlatrate]] = None

    link: Optional[str] = None


class ResultsQaBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsQaFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsQa(BaseModel):
    buy: Optional[List[ResultsQaBuy]] = None

    flatrate: Optional[List[ResultsQaFlatrate]] = None

    link: Optional[str] = None


class ResultsRoFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsRo(BaseModel):
    flatrate: Optional[List[ResultsRoFlatrate]] = None

    link: Optional[str] = None


class ResultsRsBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsRsFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsRs(BaseModel):
    buy: Optional[List[ResultsRsBuy]] = None

    flatrate: Optional[List[ResultsRsFlatrate]] = None

    link: Optional[str] = None


class ResultsRuBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsRuFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsRuRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsRu(BaseModel):
    buy: Optional[List[ResultsRuBuy]] = None

    flatrate: Optional[List[ResultsRuFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsRuRent]] = None


class ResultsSaBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsSaFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsSaRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsSa(BaseModel):
    buy: Optional[List[ResultsSaBuy]] = None

    flatrate: Optional[List[ResultsSaFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsSaRent]] = None


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


class ResultsSeRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsSe(BaseModel):
    buy: Optional[List[ResultsSeBuy]] = None

    flatrate: Optional[List[ResultsSeFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsSeRent]] = None


class ResultsSgFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsSg(BaseModel):
    flatrate: Optional[List[ResultsSgFlatrate]] = None

    link: Optional[str] = None


class ResultsSiBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsSiFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsSi(BaseModel):
    buy: Optional[List[ResultsSiBuy]] = None

    flatrate: Optional[List[ResultsSiFlatrate]] = None

    link: Optional[str] = None


class ResultsSkBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsSkFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsSkRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsSk(BaseModel):
    buy: Optional[List[ResultsSkBuy]] = None

    flatrate: Optional[List[ResultsSkFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsSkRent]] = None


class ResultsSmFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsSm(BaseModel):
    flatrate: Optional[List[ResultsSmFlatrate]] = None

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


class ResultsTrBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsTrFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsTrRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsTr(BaseModel):
    buy: Optional[List[ResultsTrBuy]] = None

    flatrate: Optional[List[ResultsTrFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsTrRent]] = None


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


class ResultsUgBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsUgRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsUg(BaseModel):
    buy: Optional[List[ResultsUgBuy]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsUgRent]] = None


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


class ResultsUsRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsUs(BaseModel):
    buy: Optional[List[ResultsUsBuy]] = None

    flatrate: Optional[List[ResultsUsFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsUsRent]] = None


class ResultsUyFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsUy(BaseModel):
    flatrate: Optional[List[ResultsUyFlatrate]] = None

    link: Optional[str] = None


class ResultsVeBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsVeFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsVeRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsVe(BaseModel):
    buy: Optional[List[ResultsVeBuy]] = None

    flatrate: Optional[List[ResultsVeFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsVeRent]] = None


class ResultsYeFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsYe(BaseModel):
    flatrate: Optional[List[ResultsYeFlatrate]] = None

    link: Optional[str] = None


class ResultsZaBuy(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsZaFlatrate(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsZaRent(BaseModel):
    display_priority: Optional[int] = None

    logo_path: Optional[str] = None

    provider_id: Optional[int] = None

    provider_name: Optional[str] = None


class ResultsZa(BaseModel):
    buy: Optional[List[ResultsZaBuy]] = None

    flatrate: Optional[List[ResultsZaFlatrate]] = None

    link: Optional[str] = None

    rent: Optional[List[ResultsZaRent]] = None


class Results(BaseModel):
    ae: Optional[ResultsAe] = FieldInfo(alias="AE", default=None)

    al: Optional[ResultsAl] = FieldInfo(alias="AL", default=None)

    ar: Optional[ResultsAr] = FieldInfo(alias="AR", default=None)

    at: Optional[ResultsAt] = FieldInfo(alias="AT", default=None)

    au: Optional[ResultsAu] = FieldInfo(alias="AU", default=None)

    ba: Optional[ResultsBa] = FieldInfo(alias="BA", default=None)

    bb: Optional[ResultsBb] = FieldInfo(alias="BB", default=None)

    be: Optional[ResultsBe] = FieldInfo(alias="BE", default=None)

    bg: Optional[ResultsBg] = FieldInfo(alias="BG", default=None)

    bh: Optional[ResultsBh] = FieldInfo(alias="BH", default=None)

    bo: Optional[ResultsBo] = FieldInfo(alias="BO", default=None)

    br: Optional[ResultsBr] = FieldInfo(alias="BR", default=None)

    bs: Optional[ResultsBs] = FieldInfo(alias="BS", default=None)

    ca: Optional[ResultsCa] = FieldInfo(alias="CA", default=None)

    ch: Optional[ResultsCh] = FieldInfo(alias="CH", default=None)

    cl: Optional[ResultsCl] = FieldInfo(alias="CL", default=None)

    co: Optional[ResultsCo] = FieldInfo(alias="CO", default=None)

    cr: Optional[ResultsCr] = FieldInfo(alias="CR", default=None)

    cv: Optional[ResultsCv] = FieldInfo(alias="CV", default=None)

    cz: Optional[ResultsCz] = FieldInfo(alias="CZ", default=None)

    de: Optional[ResultsDe] = FieldInfo(alias="DE", default=None)

    dk: Optional[ResultsDk] = FieldInfo(alias="DK", default=None)

    do: Optional[ResultsDo] = FieldInfo(alias="DO", default=None)

    ec: Optional[ResultsEc] = FieldInfo(alias="EC", default=None)

    ee: Optional[ResultsEe] = FieldInfo(alias="EE", default=None)

    eg: Optional[ResultsEg] = FieldInfo(alias="EG", default=None)

    es: Optional[ResultsEs] = FieldInfo(alias="ES", default=None)

    fi: Optional[ResultsFi] = FieldInfo(alias="FI", default=None)

    fj: Optional[ResultsFj] = FieldInfo(alias="FJ", default=None)

    fr: Optional[ResultsFr] = FieldInfo(alias="FR", default=None)

    gb: Optional[ResultsGB] = FieldInfo(alias="GB", default=None)

    gf: Optional[ResultsGf] = FieldInfo(alias="GF", default=None)

    gi: Optional[ResultsGi] = FieldInfo(alias="GI", default=None)

    gr: Optional[ResultsGr] = FieldInfo(alias="GR", default=None)

    gt: Optional[ResultsGt] = FieldInfo(alias="GT", default=None)

    hk: Optional[ResultsHk] = FieldInfo(alias="HK", default=None)

    hn: Optional[ResultsHn] = FieldInfo(alias="HN", default=None)

    hr: Optional[ResultsHr] = FieldInfo(alias="HR", default=None)

    hu: Optional[ResultsHu] = FieldInfo(alias="HU", default=None)

    id: Optional[ResultsID] = FieldInfo(alias="ID", default=None)

    ie: Optional[ResultsIe] = FieldInfo(alias="IE", default=None)

    il: Optional[ResultsIl] = FieldInfo(alias="IL", default=None)

    in_: Optional[ResultsIn] = FieldInfo(alias="IN", default=None)

    iq: Optional[ResultsIq] = FieldInfo(alias="IQ", default=None)

    is_: Optional[ResultsIs] = FieldInfo(alias="IS", default=None)

    it: Optional[ResultsIt] = FieldInfo(alias="IT", default=None)

    jm: Optional[ResultsJm] = FieldInfo(alias="JM", default=None)

    jo: Optional[ResultsJo] = FieldInfo(alias="JO", default=None)

    jp: Optional[ResultsJp] = FieldInfo(alias="JP", default=None)

    kr: Optional[ResultsKr] = FieldInfo(alias="KR", default=None)

    kw: Optional[ResultsKw] = FieldInfo(alias="KW", default=None)

    lb: Optional[ResultsLb] = FieldInfo(alias="LB", default=None)

    li: Optional[ResultsLi] = FieldInfo(alias="LI", default=None)

    lt: Optional[ResultsLt] = FieldInfo(alias="LT", default=None)

    lv: Optional[ResultsLv] = FieldInfo(alias="LV", default=None)

    md: Optional[ResultsMd] = FieldInfo(alias="MD", default=None)

    mk: Optional[ResultsMk] = FieldInfo(alias="MK", default=None)

    mt: Optional[ResultsMt] = FieldInfo(alias="MT", default=None)

    mu: Optional[ResultsMu] = FieldInfo(alias="MU", default=None)

    mx: Optional[ResultsMx] = FieldInfo(alias="MX", default=None)

    my: Optional[ResultsMy] = FieldInfo(alias="MY", default=None)

    mz: Optional[ResultsMz] = FieldInfo(alias="MZ", default=None)

    nl: Optional[ResultsNl] = FieldInfo(alias="NL", default=None)

    no: Optional[ResultsNo] = FieldInfo(alias="NO", default=None)

    nz: Optional[ResultsNz] = FieldInfo(alias="NZ", default=None)

    om: Optional[ResultsOm] = FieldInfo(alias="OM", default=None)

    pa: Optional[ResultsPa] = FieldInfo(alias="PA", default=None)

    pe: Optional[ResultsPe] = FieldInfo(alias="PE", default=None)

    ph: Optional[ResultsPh] = FieldInfo(alias="PH", default=None)

    pk: Optional[ResultsPk] = FieldInfo(alias="PK", default=None)

    pl: Optional[ResultsPl] = FieldInfo(alias="PL", default=None)

    ps: Optional[ResultsPs] = FieldInfo(alias="PS", default=None)

    pt: Optional[ResultsPt] = FieldInfo(alias="PT", default=None)

    py: Optional[ResultsPy] = FieldInfo(alias="PY", default=None)

    qa: Optional[ResultsQa] = FieldInfo(alias="QA", default=None)

    ro: Optional[ResultsRo] = FieldInfo(alias="RO", default=None)

    rs: Optional[ResultsRs] = FieldInfo(alias="RS", default=None)

    ru: Optional[ResultsRu] = FieldInfo(alias="RU", default=None)

    sa: Optional[ResultsSa] = FieldInfo(alias="SA", default=None)

    se: Optional[ResultsSe] = FieldInfo(alias="SE", default=None)

    sg: Optional[ResultsSg] = FieldInfo(alias="SG", default=None)

    si: Optional[ResultsSi] = FieldInfo(alias="SI", default=None)

    sk: Optional[ResultsSk] = FieldInfo(alias="SK", default=None)

    sm: Optional[ResultsSm] = FieldInfo(alias="SM", default=None)

    sv: Optional[ResultsSv] = FieldInfo(alias="SV", default=None)

    th: Optional[ResultsTh] = FieldInfo(alias="TH", default=None)

    tr: Optional[ResultsTr] = FieldInfo(alias="TR", default=None)

    tt: Optional[ResultsTt] = FieldInfo(alias="TT", default=None)

    tw: Optional[ResultsTw] = FieldInfo(alias="TW", default=None)

    ug: Optional[ResultsUg] = FieldInfo(alias="UG", default=None)

    us: Optional[ResultsUs] = FieldInfo(alias="US", default=None)

    uy: Optional[ResultsUy] = FieldInfo(alias="UY", default=None)

    ve: Optional[ResultsVe] = FieldInfo(alias="VE", default=None)

    ye: Optional[ResultsYe] = FieldInfo(alias="YE", default=None)

    za: Optional[ResultsZa] = FieldInfo(alias="ZA", default=None)


class WatchProviderListResponse(BaseModel):
    id: Optional[int] = None

    results: Optional[Results] = None
