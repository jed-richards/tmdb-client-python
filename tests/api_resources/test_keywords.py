# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tmdb_client import TmdbClient, AsyncTmdbClient
from tmdb_client.types import KeywordSearchResponse, KeywordRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKeywords:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: TmdbClient) -> None:
        keyword = client.keywords.retrieve(
            0,
        )
        assert_matches_type(KeywordRetrieveResponse, keyword, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: TmdbClient) -> None:
        response = client.keywords.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        keyword = response.parse()
        assert_matches_type(KeywordRetrieveResponse, keyword, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: TmdbClient) -> None:
        with client.keywords.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            keyword = response.parse()
            assert_matches_type(KeywordRetrieveResponse, keyword, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search(self, client: TmdbClient) -> None:
        keyword = client.keywords.search(
            query="query",
        )
        assert_matches_type(KeywordSearchResponse, keyword, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: TmdbClient) -> None:
        keyword = client.keywords.search(
            query="query",
            page=0,
        )
        assert_matches_type(KeywordSearchResponse, keyword, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: TmdbClient) -> None:
        response = client.keywords.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        keyword = response.parse()
        assert_matches_type(KeywordSearchResponse, keyword, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: TmdbClient) -> None:
        with client.keywords.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            keyword = response.parse()
            assert_matches_type(KeywordSearchResponse, keyword, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncKeywords:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTmdbClient) -> None:
        keyword = await async_client.keywords.retrieve(
            0,
        )
        assert_matches_type(KeywordRetrieveResponse, keyword, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.keywords.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        keyword = await response.parse()
        assert_matches_type(KeywordRetrieveResponse, keyword, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.keywords.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            keyword = await response.parse()
            assert_matches_type(KeywordRetrieveResponse, keyword, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search(self, async_client: AsyncTmdbClient) -> None:
        keyword = await async_client.keywords.search(
            query="query",
        )
        assert_matches_type(KeywordSearchResponse, keyword, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        keyword = await async_client.keywords.search(
            query="query",
            page=0,
        )
        assert_matches_type(KeywordSearchResponse, keyword, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.keywords.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        keyword = await response.parse()
        assert_matches_type(KeywordSearchResponse, keyword, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.keywords.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            keyword = await response.parse()
            assert_matches_type(KeywordSearchResponse, keyword, path=["response"])

        assert cast(Any, response.is_closed) is True
