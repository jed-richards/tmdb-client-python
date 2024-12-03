# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tmdb_client import TmdbClient, AsyncTmdbClient
from tmdb_client.types import AuthenticationTestKeyResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuthentication:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_test_key(self, client: TmdbClient) -> None:
        authentication = client.authentication.test_key()
        assert_matches_type(AuthenticationTestKeyResponse, authentication, path=["response"])

    @parametrize
    def test_raw_response_test_key(self, client: TmdbClient) -> None:
        response = client.authentication.with_raw_response.test_key()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = response.parse()
        assert_matches_type(AuthenticationTestKeyResponse, authentication, path=["response"])

    @parametrize
    def test_streaming_response_test_key(self, client: TmdbClient) -> None:
        with client.authentication.with_streaming_response.test_key() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication = response.parse()
            assert_matches_type(AuthenticationTestKeyResponse, authentication, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAuthentication:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_test_key(self, async_client: AsyncTmdbClient) -> None:
        authentication = await async_client.authentication.test_key()
        assert_matches_type(AuthenticationTestKeyResponse, authentication, path=["response"])

    @parametrize
    async def test_raw_response_test_key(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.authentication.with_raw_response.test_key()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        authentication = await response.parse()
        assert_matches_type(AuthenticationTestKeyResponse, authentication, path=["response"])

    @parametrize
    async def test_streaming_response_test_key(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.authentication.with_streaming_response.test_key() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            authentication = await response.parse()
            assert_matches_type(AuthenticationTestKeyResponse, authentication, path=["response"])

        assert cast(Any, response.is_closed) is True
