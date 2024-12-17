# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tmdb_client import TmdbClient, AsyncTmdbClient
from tmdb_client.types.authentication import (
    SessionNewResponse,
    SessionDeleteResponse,
    SessionConvertResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSession:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: TmdbClient) -> None:
        session = client.authentication.session.delete(
            raw_body="RAW_BODY",
        )
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: TmdbClient) -> None:
        response = client.authentication.session.with_raw_response.delete(
            raw_body="RAW_BODY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: TmdbClient) -> None:
        with client.authentication.session.with_streaming_response.delete(
            raw_body="RAW_BODY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionDeleteResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_convert(self, client: TmdbClient) -> None:
        session = client.authentication.session.convert(
            raw_body="RAW_BODY",
        )
        assert_matches_type(SessionConvertResponse, session, path=["response"])

    @parametrize
    def test_raw_response_convert(self, client: TmdbClient) -> None:
        response = client.authentication.session.with_raw_response.convert(
            raw_body="RAW_BODY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionConvertResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_convert(self, client: TmdbClient) -> None:
        with client.authentication.session.with_streaming_response.convert(
            raw_body="RAW_BODY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionConvertResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_new(self, client: TmdbClient) -> None:
        session = client.authentication.session.new(
            raw_body="RAW_BODY",
        )
        assert_matches_type(SessionNewResponse, session, path=["response"])

    @parametrize
    def test_raw_response_new(self, client: TmdbClient) -> None:
        response = client.authentication.session.with_raw_response.new(
            raw_body="RAW_BODY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SessionNewResponse, session, path=["response"])

    @parametrize
    def test_streaming_response_new(self, client: TmdbClient) -> None:
        with client.authentication.session.with_streaming_response.new(
            raw_body="RAW_BODY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SessionNewResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSession:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_delete(self, async_client: AsyncTmdbClient) -> None:
        session = await async_client.authentication.session.delete(
            raw_body="RAW_BODY",
        )
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.authentication.session.with_raw_response.delete(
            raw_body="RAW_BODY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionDeleteResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.authentication.session.with_streaming_response.delete(
            raw_body="RAW_BODY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionDeleteResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_convert(self, async_client: AsyncTmdbClient) -> None:
        session = await async_client.authentication.session.convert(
            raw_body="RAW_BODY",
        )
        assert_matches_type(SessionConvertResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_convert(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.authentication.session.with_raw_response.convert(
            raw_body="RAW_BODY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionConvertResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_convert(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.authentication.session.with_streaming_response.convert(
            raw_body="RAW_BODY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionConvertResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_new(self, async_client: AsyncTmdbClient) -> None:
        session = await async_client.authentication.session.new(
            raw_body="RAW_BODY",
        )
        assert_matches_type(SessionNewResponse, session, path=["response"])

    @parametrize
    async def test_raw_response_new(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.authentication.session.with_raw_response.new(
            raw_body="RAW_BODY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(SessionNewResponse, session, path=["response"])

    @parametrize
    async def test_streaming_response_new(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.authentication.session.with_streaming_response.new(
            raw_body="RAW_BODY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(SessionNewResponse, session, path=["response"])

        assert cast(Any, response.is_closed) is True