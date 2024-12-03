# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tmdb_client import TmdbClient, AsyncTmdbClient
from tmdb_client.types.tv_shows import AiringTodayListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAiringToday:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: TmdbClient) -> None:
        airing_today = client.tv_shows.airing_today.list()
        assert_matches_type(AiringTodayListResponse, airing_today, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: TmdbClient) -> None:
        airing_today = client.tv_shows.airing_today.list(
            language="language",
            page=0,
            timezone="timezone",
        )
        assert_matches_type(AiringTodayListResponse, airing_today, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: TmdbClient) -> None:
        response = client.tv_shows.airing_today.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airing_today = response.parse()
        assert_matches_type(AiringTodayListResponse, airing_today, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: TmdbClient) -> None:
        with client.tv_shows.airing_today.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airing_today = response.parse()
            assert_matches_type(AiringTodayListResponse, airing_today, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAiringToday:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTmdbClient) -> None:
        airing_today = await async_client.tv_shows.airing_today.list()
        assert_matches_type(AiringTodayListResponse, airing_today, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        airing_today = await async_client.tv_shows.airing_today.list(
            language="language",
            page=0,
            timezone="timezone",
        )
        assert_matches_type(AiringTodayListResponse, airing_today, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.tv_shows.airing_today.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        airing_today = await response.parse()
        assert_matches_type(AiringTodayListResponse, airing_today, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.tv_shows.airing_today.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            airing_today = await response.parse()
            assert_matches_type(AiringTodayListResponse, airing_today, path=["response"])

        assert cast(Any, response.is_closed) is True
