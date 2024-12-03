# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tmdb_client import TmdbClient, AsyncTmdbClient
from tmdb_client.types import TrendingListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrending:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: TmdbClient) -> None:
        trending = client.trending.list(
            time_window="day",
        )
        assert_matches_type(TrendingListResponse, trending, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: TmdbClient) -> None:
        trending = client.trending.list(
            time_window="day",
            language="language",
        )
        assert_matches_type(TrendingListResponse, trending, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: TmdbClient) -> None:
        response = client.trending.with_raw_response.list(
            time_window="day",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trending = response.parse()
        assert_matches_type(TrendingListResponse, trending, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: TmdbClient) -> None:
        with client.trending.with_streaming_response.list(
            time_window="day",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trending = response.parse()
            assert_matches_type(TrendingListResponse, trending, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTrending:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTmdbClient) -> None:
        trending = await async_client.trending.list(
            time_window="day",
        )
        assert_matches_type(TrendingListResponse, trending, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        trending = await async_client.trending.list(
            time_window="day",
            language="language",
        )
        assert_matches_type(TrendingListResponse, trending, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.trending.with_raw_response.list(
            time_window="day",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trending = await response.parse()
        assert_matches_type(TrendingListResponse, trending, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.trending.with_streaming_response.list(
            time_window="day",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trending = await response.parse()
            assert_matches_type(TrendingListResponse, trending, path=["response"])

        assert cast(Any, response.is_closed) is True
