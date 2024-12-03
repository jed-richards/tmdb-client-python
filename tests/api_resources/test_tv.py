# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tmdb_client import TmdbClient, AsyncTmdbClient
from tmdb_client.types import TvSearchResponse, TvRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTv:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: TmdbClient) -> None:
        tv = client.tv.retrieve(
            series_id=0,
        )
        assert_matches_type(TvRetrieveResponse, tv, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: TmdbClient) -> None:
        tv = client.tv.retrieve(
            series_id=0,
            append_to_response="append_to_response",
            language="language",
        )
        assert_matches_type(TvRetrieveResponse, tv, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: TmdbClient) -> None:
        response = client.tv.with_raw_response.retrieve(
            series_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tv = response.parse()
        assert_matches_type(TvRetrieveResponse, tv, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: TmdbClient) -> None:
        with client.tv.with_streaming_response.retrieve(
            series_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tv = response.parse()
            assert_matches_type(TvRetrieveResponse, tv, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search(self, client: TmdbClient) -> None:
        tv = client.tv.search(
            query="query",
        )
        assert_matches_type(TvSearchResponse, tv, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: TmdbClient) -> None:
        tv = client.tv.search(
            query="query",
            first_air_date_year=0,
            include_adult=True,
            language="language",
            page=0,
            year=0,
        )
        assert_matches_type(TvSearchResponse, tv, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: TmdbClient) -> None:
        response = client.tv.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tv = response.parse()
        assert_matches_type(TvSearchResponse, tv, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: TmdbClient) -> None:
        with client.tv.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tv = response.parse()
            assert_matches_type(TvSearchResponse, tv, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTv:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTmdbClient) -> None:
        tv = await async_client.tv.retrieve(
            series_id=0,
        )
        assert_matches_type(TvRetrieveResponse, tv, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        tv = await async_client.tv.retrieve(
            series_id=0,
            append_to_response="append_to_response",
            language="language",
        )
        assert_matches_type(TvRetrieveResponse, tv, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.tv.with_raw_response.retrieve(
            series_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tv = await response.parse()
        assert_matches_type(TvRetrieveResponse, tv, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.tv.with_streaming_response.retrieve(
            series_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tv = await response.parse()
            assert_matches_type(TvRetrieveResponse, tv, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search(self, async_client: AsyncTmdbClient) -> None:
        tv = await async_client.tv.search(
            query="query",
        )
        assert_matches_type(TvSearchResponse, tv, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        tv = await async_client.tv.search(
            query="query",
            first_air_date_year=0,
            include_adult=True,
            language="language",
            page=0,
            year=0,
        )
        assert_matches_type(TvSearchResponse, tv, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.tv.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tv = await response.parse()
        assert_matches_type(TvSearchResponse, tv, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.tv.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tv = await response.parse()
            assert_matches_type(TvSearchResponse, tv, path=["response"])

        assert cast(Any, response.is_closed) is True
