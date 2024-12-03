# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tmdb_client import TmdbClient, AsyncTmdbClient
from tmdb_client.types import DiscoverTvListResponse
from tmdb_client._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDiscoverTv:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: TmdbClient) -> None:
        discover_tv = client.discover_tv.list()
        assert_matches_type(DiscoverTvListResponse, discover_tv, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: TmdbClient) -> None:
        discover_tv = client.discover_tv.list(
            air_date={
                "gte": parse_date("2019-12-27"),
                "lte": parse_date("2019-12-27"),
            },
            first_air_date={
                "gte": parse_date("2019-12-27"),
                "lte": parse_date("2019-12-27"),
            },
            first_air_date_year=0,
            include_adult=True,
            include_null_first_air_dates=True,
            language="language",
            page=0,
            screened_theatrically=True,
            sort_by="first_air_date.asc",
            timezone="timezone",
            vote_average={
                "gte": 0,
                "lte": 0,
            },
            vote_count={
                "gte": 0,
                "lte": 0,
            },
            watch_region="watch_region",
            with_companies="with_companies",
            with_genres="with_genres",
            with_keywords="with_keywords",
            with_networks=0,
            with_origin_country="with_origin_country",
            with_original_language="with_original_language",
            with_runtime={
                "gte": 0,
                "lte": 0,
            },
            with_status="with_status",
            with_type="with_type",
            with_watch_monetization_types="with_watch_monetization_types",
            with_watch_providers="with_watch_providers",
            without_companies="without_companies",
            without_genres="without_genres",
            without_keywords="without_keywords",
            without_watch_providers="without_watch_providers",
        )
        assert_matches_type(DiscoverTvListResponse, discover_tv, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: TmdbClient) -> None:
        response = client.discover_tv.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discover_tv = response.parse()
        assert_matches_type(DiscoverTvListResponse, discover_tv, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: TmdbClient) -> None:
        with client.discover_tv.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discover_tv = response.parse()
            assert_matches_type(DiscoverTvListResponse, discover_tv, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDiscoverTv:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTmdbClient) -> None:
        discover_tv = await async_client.discover_tv.list()
        assert_matches_type(DiscoverTvListResponse, discover_tv, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        discover_tv = await async_client.discover_tv.list(
            air_date={
                "gte": parse_date("2019-12-27"),
                "lte": parse_date("2019-12-27"),
            },
            first_air_date={
                "gte": parse_date("2019-12-27"),
                "lte": parse_date("2019-12-27"),
            },
            first_air_date_year=0,
            include_adult=True,
            include_null_first_air_dates=True,
            language="language",
            page=0,
            screened_theatrically=True,
            sort_by="first_air_date.asc",
            timezone="timezone",
            vote_average={
                "gte": 0,
                "lte": 0,
            },
            vote_count={
                "gte": 0,
                "lte": 0,
            },
            watch_region="watch_region",
            with_companies="with_companies",
            with_genres="with_genres",
            with_keywords="with_keywords",
            with_networks=0,
            with_origin_country="with_origin_country",
            with_original_language="with_original_language",
            with_runtime={
                "gte": 0,
                "lte": 0,
            },
            with_status="with_status",
            with_type="with_type",
            with_watch_monetization_types="with_watch_monetization_types",
            with_watch_providers="with_watch_providers",
            without_companies="without_companies",
            without_genres="without_genres",
            without_keywords="without_keywords",
            without_watch_providers="without_watch_providers",
        )
        assert_matches_type(DiscoverTvListResponse, discover_tv, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.discover_tv.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        discover_tv = await response.parse()
        assert_matches_type(DiscoverTvListResponse, discover_tv, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.discover_tv.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            discover_tv = await response.parse()
            assert_matches_type(DiscoverTvListResponse, discover_tv, path=["response"])

        assert cast(Any, response.is_closed) is True
