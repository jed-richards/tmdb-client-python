# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tmdb_client import TmdbClient, AsyncTmdbClient
from tmdb_client.types import TvSeryListsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTvSeries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_lists(self, client: TmdbClient) -> None:
        tv_sery = client.tv_series.lists(
            series_id=0,
        )
        assert_matches_type(TvSeryListsResponse, tv_sery, path=["response"])

    @parametrize
    def test_method_lists_with_all_params(self, client: TmdbClient) -> None:
        tv_sery = client.tv_series.lists(
            series_id=0,
            language="language",
            page=0,
        )
        assert_matches_type(TvSeryListsResponse, tv_sery, path=["response"])

    @parametrize
    def test_raw_response_lists(self, client: TmdbClient) -> None:
        response = client.tv_series.with_raw_response.lists(
            series_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tv_sery = response.parse()
        assert_matches_type(TvSeryListsResponse, tv_sery, path=["response"])

    @parametrize
    def test_streaming_response_lists(self, client: TmdbClient) -> None:
        with client.tv_series.with_streaming_response.lists(
            series_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tv_sery = response.parse()
            assert_matches_type(TvSeryListsResponse, tv_sery, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTvSeries:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_lists(self, async_client: AsyncTmdbClient) -> None:
        tv_sery = await async_client.tv_series.lists(
            series_id=0,
        )
        assert_matches_type(TvSeryListsResponse, tv_sery, path=["response"])

    @parametrize
    async def test_method_lists_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        tv_sery = await async_client.tv_series.lists(
            series_id=0,
            language="language",
            page=0,
        )
        assert_matches_type(TvSeryListsResponse, tv_sery, path=["response"])

    @parametrize
    async def test_raw_response_lists(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.tv_series.with_raw_response.lists(
            series_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tv_sery = await response.parse()
        assert_matches_type(TvSeryListsResponse, tv_sery, path=["response"])

    @parametrize
    async def test_streaming_response_lists(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.tv_series.with_streaming_response.lists(
            series_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tv_sery = await response.parse()
            assert_matches_type(TvSeryListsResponse, tv_sery, path=["response"])

        assert cast(Any, response.is_closed) is True
