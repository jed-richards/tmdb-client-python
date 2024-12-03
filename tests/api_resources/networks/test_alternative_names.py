# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tmdb_client import TmdbClient, AsyncTmdbClient
from tmdb_client.types.networks import AlternativeNameListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAlternativeNames:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: TmdbClient) -> None:
        alternative_name = client.networks.alternative_names.list(
            0,
        )
        assert_matches_type(AlternativeNameListResponse, alternative_name, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: TmdbClient) -> None:
        response = client.networks.alternative_names.with_raw_response.list(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alternative_name = response.parse()
        assert_matches_type(AlternativeNameListResponse, alternative_name, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: TmdbClient) -> None:
        with client.networks.alternative_names.with_streaming_response.list(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alternative_name = response.parse()
            assert_matches_type(AlternativeNameListResponse, alternative_name, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAlternativeNames:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTmdbClient) -> None:
        alternative_name = await async_client.networks.alternative_names.list(
            0,
        )
        assert_matches_type(AlternativeNameListResponse, alternative_name, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.networks.alternative_names.with_raw_response.list(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alternative_name = await response.parse()
        assert_matches_type(AlternativeNameListResponse, alternative_name, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.networks.alternative_names.with_streaming_response.list(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alternative_name = await response.parse()
            assert_matches_type(AlternativeNameListResponse, alternative_name, path=["response"])

        assert cast(Any, response.is_closed) is True
