# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tmdb_client import TmdbClient, AsyncTmdbClient
from tmdb_client.types.people import MovieCreditListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMovieCredits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: TmdbClient) -> None:
        movie_credit = client.people.movie_credits.list(
            person_id=0,
        )
        assert_matches_type(MovieCreditListResponse, movie_credit, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: TmdbClient) -> None:
        movie_credit = client.people.movie_credits.list(
            person_id=0,
            language="language",
        )
        assert_matches_type(MovieCreditListResponse, movie_credit, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: TmdbClient) -> None:
        response = client.people.movie_credits.with_raw_response.list(
            person_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        movie_credit = response.parse()
        assert_matches_type(MovieCreditListResponse, movie_credit, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: TmdbClient) -> None:
        with client.people.movie_credits.with_streaming_response.list(
            person_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            movie_credit = response.parse()
            assert_matches_type(MovieCreditListResponse, movie_credit, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMovieCredits:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTmdbClient) -> None:
        movie_credit = await async_client.people.movie_credits.list(
            person_id=0,
        )
        assert_matches_type(MovieCreditListResponse, movie_credit, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        movie_credit = await async_client.people.movie_credits.list(
            person_id=0,
            language="language",
        )
        assert_matches_type(MovieCreditListResponse, movie_credit, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.people.movie_credits.with_raw_response.list(
            person_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        movie_credit = await response.parse()
        assert_matches_type(MovieCreditListResponse, movie_credit, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.people.movie_credits.with_streaming_response.list(
            person_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            movie_credit = await response.parse()
            assert_matches_type(MovieCreditListResponse, movie_credit, path=["response"])

        assert cast(Any, response.is_closed) is True
