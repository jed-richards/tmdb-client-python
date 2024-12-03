# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tmdb_client import TmdbClient, AsyncTmdbClient
from tmdb_client.types.authentication import GuestSessionNewResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGuestSession:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_new(self, client: TmdbClient) -> None:
        guest_session = client.authentication.guest_session.new()
        assert_matches_type(GuestSessionNewResponse, guest_session, path=["response"])

    @parametrize
    def test_raw_response_new(self, client: TmdbClient) -> None:
        response = client.authentication.guest_session.with_raw_response.new()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guest_session = response.parse()
        assert_matches_type(GuestSessionNewResponse, guest_session, path=["response"])

    @parametrize
    def test_streaming_response_new(self, client: TmdbClient) -> None:
        with client.authentication.guest_session.with_streaming_response.new() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guest_session = response.parse()
            assert_matches_type(GuestSessionNewResponse, guest_session, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGuestSession:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_new(self, async_client: AsyncTmdbClient) -> None:
        guest_session = await async_client.authentication.guest_session.new()
        assert_matches_type(GuestSessionNewResponse, guest_session, path=["response"])

    @parametrize
    async def test_raw_response_new(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.authentication.guest_session.with_raw_response.new()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        guest_session = await response.parse()
        assert_matches_type(GuestSessionNewResponse, guest_session, path=["response"])

    @parametrize
    async def test_streaming_response_new(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.authentication.guest_session.with_streaming_response.new() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            guest_session = await response.parse()
            assert_matches_type(GuestSessionNewResponse, guest_session, path=["response"])

        assert cast(Any, response.is_closed) is True
