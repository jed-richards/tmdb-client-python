# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tmdb_client import TmdbClient, AsyncTmdbClient
from tmdb_client.types.tv_shows import (
    RatingRateResponse,
    RatingDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRating:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: TmdbClient) -> None:
        rating = client.tv_shows.rating.delete(
            series_id=0,
        )
        assert_matches_type(RatingDeleteResponse, rating, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: TmdbClient) -> None:
        rating = client.tv_shows.rating.delete(
            series_id=0,
            guest_session_id="guest_session_id",
            session_id="session_id",
        )
        assert_matches_type(RatingDeleteResponse, rating, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: TmdbClient) -> None:
        response = client.tv_shows.rating.with_raw_response.delete(
            series_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rating = response.parse()
        assert_matches_type(RatingDeleteResponse, rating, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: TmdbClient) -> None:
        with client.tv_shows.rating.with_streaming_response.delete(
            series_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rating = response.parse()
            assert_matches_type(RatingDeleteResponse, rating, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_rate(self, client: TmdbClient) -> None:
        rating = client.tv_shows.rating.rate(
            series_id=0,
            raw_body="RAW_BODY",
        )
        assert_matches_type(RatingRateResponse, rating, path=["response"])

    @parametrize
    def test_method_rate_with_all_params(self, client: TmdbClient) -> None:
        rating = client.tv_shows.rating.rate(
            series_id=0,
            raw_body="RAW_BODY",
            guest_session_id="guest_session_id",
            session_id="session_id",
        )
        assert_matches_type(RatingRateResponse, rating, path=["response"])

    @parametrize
    def test_raw_response_rate(self, client: TmdbClient) -> None:
        response = client.tv_shows.rating.with_raw_response.rate(
            series_id=0,
            raw_body="RAW_BODY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rating = response.parse()
        assert_matches_type(RatingRateResponse, rating, path=["response"])

    @parametrize
    def test_streaming_response_rate(self, client: TmdbClient) -> None:
        with client.tv_shows.rating.with_streaming_response.rate(
            series_id=0,
            raw_body="RAW_BODY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rating = response.parse()
            assert_matches_type(RatingRateResponse, rating, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRating:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_delete(self, async_client: AsyncTmdbClient) -> None:
        rating = await async_client.tv_shows.rating.delete(
            series_id=0,
        )
        assert_matches_type(RatingDeleteResponse, rating, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        rating = await async_client.tv_shows.rating.delete(
            series_id=0,
            guest_session_id="guest_session_id",
            session_id="session_id",
        )
        assert_matches_type(RatingDeleteResponse, rating, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.tv_shows.rating.with_raw_response.delete(
            series_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rating = await response.parse()
        assert_matches_type(RatingDeleteResponse, rating, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.tv_shows.rating.with_streaming_response.delete(
            series_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rating = await response.parse()
            assert_matches_type(RatingDeleteResponse, rating, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_rate(self, async_client: AsyncTmdbClient) -> None:
        rating = await async_client.tv_shows.rating.rate(
            series_id=0,
            raw_body="RAW_BODY",
        )
        assert_matches_type(RatingRateResponse, rating, path=["response"])

    @parametrize
    async def test_method_rate_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        rating = await async_client.tv_shows.rating.rate(
            series_id=0,
            raw_body="RAW_BODY",
            guest_session_id="guest_session_id",
            session_id="session_id",
        )
        assert_matches_type(RatingRateResponse, rating, path=["response"])

    @parametrize
    async def test_raw_response_rate(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.tv_shows.rating.with_raw_response.rate(
            series_id=0,
            raw_body="RAW_BODY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        rating = await response.parse()
        assert_matches_type(RatingRateResponse, rating, path=["response"])

    @parametrize
    async def test_streaming_response_rate(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.tv_shows.rating.with_streaming_response.rate(
            series_id=0,
            raw_body="RAW_BODY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            rating = await response.parse()
            assert_matches_type(RatingRateResponse, rating, path=["response"])

        assert cast(Any, response.is_closed) is True
