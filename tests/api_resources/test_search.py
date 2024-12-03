# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tmdb_client import TmdbClient, AsyncTmdbClient
from tmdb_client.types import (
    SearchMultiResponse,
    SearchCompanyResponse,
    SearchCollectionResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_collection(self, client: TmdbClient) -> None:
        search = client.search.collection(
            query="query",
        )
        assert_matches_type(SearchCollectionResponse, search, path=["response"])

    @parametrize
    def test_method_collection_with_all_params(self, client: TmdbClient) -> None:
        search = client.search.collection(
            query="query",
            include_adult=True,
            language="language",
            page=0,
            region="region",
        )
        assert_matches_type(SearchCollectionResponse, search, path=["response"])

    @parametrize
    def test_raw_response_collection(self, client: TmdbClient) -> None:
        response = client.search.with_raw_response.collection(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchCollectionResponse, search, path=["response"])

    @parametrize
    def test_streaming_response_collection(self, client: TmdbClient) -> None:
        with client.search.with_streaming_response.collection(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchCollectionResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_company(self, client: TmdbClient) -> None:
        search = client.search.company(
            query="query",
        )
        assert_matches_type(SearchCompanyResponse, search, path=["response"])

    @parametrize
    def test_method_company_with_all_params(self, client: TmdbClient) -> None:
        search = client.search.company(
            query="query",
            page=0,
        )
        assert_matches_type(SearchCompanyResponse, search, path=["response"])

    @parametrize
    def test_raw_response_company(self, client: TmdbClient) -> None:
        response = client.search.with_raw_response.company(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchCompanyResponse, search, path=["response"])

    @parametrize
    def test_streaming_response_company(self, client: TmdbClient) -> None:
        with client.search.with_streaming_response.company(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchCompanyResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_multi(self, client: TmdbClient) -> None:
        search = client.search.multi(
            query="query",
        )
        assert_matches_type(SearchMultiResponse, search, path=["response"])

    @parametrize
    def test_method_multi_with_all_params(self, client: TmdbClient) -> None:
        search = client.search.multi(
            query="query",
            include_adult=True,
            language="language",
            page=0,
        )
        assert_matches_type(SearchMultiResponse, search, path=["response"])

    @parametrize
    def test_raw_response_multi(self, client: TmdbClient) -> None:
        response = client.search.with_raw_response.multi(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = response.parse()
        assert_matches_type(SearchMultiResponse, search, path=["response"])

    @parametrize
    def test_streaming_response_multi(self, client: TmdbClient) -> None:
        with client.search.with_streaming_response.multi(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = response.parse()
            assert_matches_type(SearchMultiResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSearch:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_collection(self, async_client: AsyncTmdbClient) -> None:
        search = await async_client.search.collection(
            query="query",
        )
        assert_matches_type(SearchCollectionResponse, search, path=["response"])

    @parametrize
    async def test_method_collection_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        search = await async_client.search.collection(
            query="query",
            include_adult=True,
            language="language",
            page=0,
            region="region",
        )
        assert_matches_type(SearchCollectionResponse, search, path=["response"])

    @parametrize
    async def test_raw_response_collection(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.search.with_raw_response.collection(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchCollectionResponse, search, path=["response"])

    @parametrize
    async def test_streaming_response_collection(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.search.with_streaming_response.collection(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchCollectionResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_company(self, async_client: AsyncTmdbClient) -> None:
        search = await async_client.search.company(
            query="query",
        )
        assert_matches_type(SearchCompanyResponse, search, path=["response"])

    @parametrize
    async def test_method_company_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        search = await async_client.search.company(
            query="query",
            page=0,
        )
        assert_matches_type(SearchCompanyResponse, search, path=["response"])

    @parametrize
    async def test_raw_response_company(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.search.with_raw_response.company(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchCompanyResponse, search, path=["response"])

    @parametrize
    async def test_streaming_response_company(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.search.with_streaming_response.company(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchCompanyResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_multi(self, async_client: AsyncTmdbClient) -> None:
        search = await async_client.search.multi(
            query="query",
        )
        assert_matches_type(SearchMultiResponse, search, path=["response"])

    @parametrize
    async def test_method_multi_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        search = await async_client.search.multi(
            query="query",
            include_adult=True,
            language="language",
            page=0,
        )
        assert_matches_type(SearchMultiResponse, search, path=["response"])

    @parametrize
    async def test_raw_response_multi(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.search.with_raw_response.multi(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search = await response.parse()
        assert_matches_type(SearchMultiResponse, search, path=["response"])

    @parametrize
    async def test_streaming_response_multi(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.search.with_streaming_response.multi(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search = await response.parse()
            assert_matches_type(SearchMultiResponse, search, path=["response"])

        assert cast(Any, response.is_closed) is True
