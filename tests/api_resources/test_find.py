# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tmdb_client import TmdbClient, AsyncTmdbClient
from tmdb_client.types import FindRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFind:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: TmdbClient) -> None:
        find = client.find.retrieve(
            external_id="external_id",
            external_source="",
        )
        assert_matches_type(FindRetrieveResponse, find, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: TmdbClient) -> None:
        find = client.find.retrieve(
            external_id="external_id",
            external_source="",
            language="language",
        )
        assert_matches_type(FindRetrieveResponse, find, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: TmdbClient) -> None:
        response = client.find.with_raw_response.retrieve(
            external_id="external_id",
            external_source="",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        find = response.parse()
        assert_matches_type(FindRetrieveResponse, find, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: TmdbClient) -> None:
        with client.find.with_streaming_response.retrieve(
            external_id="external_id",
            external_source="",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            find = response.parse()
            assert_matches_type(FindRetrieveResponse, find, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: TmdbClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_id` but received ''"):
            client.find.with_raw_response.retrieve(
                external_id="",
                external_source="",
            )


class TestAsyncFind:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTmdbClient) -> None:
        find = await async_client.find.retrieve(
            external_id="external_id",
            external_source="",
        )
        assert_matches_type(FindRetrieveResponse, find, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        find = await async_client.find.retrieve(
            external_id="external_id",
            external_source="",
            language="language",
        )
        assert_matches_type(FindRetrieveResponse, find, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.find.with_raw_response.retrieve(
            external_id="external_id",
            external_source="",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        find = await response.parse()
        assert_matches_type(FindRetrieveResponse, find, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.find.with_streaming_response.retrieve(
            external_id="external_id",
            external_source="",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            find = await response.parse()
            assert_matches_type(FindRetrieveResponse, find, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncTmdbClient) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `external_id` but received ''"):
            await async_client.find.with_raw_response.retrieve(
                external_id="",
                external_source="",
            )
