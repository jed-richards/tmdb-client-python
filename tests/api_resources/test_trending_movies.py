# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tmdb_client import TmdbClient, AsyncTmdbClient
from tmdb_client.types import TrendingMovieListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTrendingMovies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: TmdbClient) -> None:
        trending_movie = client.trending_movies.list(
            time_window="day",
        )
        assert_matches_type(TrendingMovieListResponse, trending_movie, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: TmdbClient) -> None:
        trending_movie = client.trending_movies.list(
            time_window="day",
            language="language",
        )
        assert_matches_type(TrendingMovieListResponse, trending_movie, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: TmdbClient) -> None:
        response = client.trending_movies.with_raw_response.list(
            time_window="day",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trending_movie = response.parse()
        assert_matches_type(TrendingMovieListResponse, trending_movie, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: TmdbClient) -> None:
        with client.trending_movies.with_streaming_response.list(
            time_window="day",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trending_movie = response.parse()
            assert_matches_type(TrendingMovieListResponse, trending_movie, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTrendingMovies:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTmdbClient) -> None:
        trending_movie = await async_client.trending_movies.list(
            time_window="day",
        )
        assert_matches_type(TrendingMovieListResponse, trending_movie, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        trending_movie = await async_client.trending_movies.list(
            time_window="day",
            language="language",
        )
        assert_matches_type(TrendingMovieListResponse, trending_movie, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.trending_movies.with_raw_response.list(
            time_window="day",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trending_movie = await response.parse()
        assert_matches_type(TrendingMovieListResponse, trending_movie, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.trending_movies.with_streaming_response.list(
            time_window="day",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trending_movie = await response.parse()
            assert_matches_type(TrendingMovieListResponse, trending_movie, path=["response"])

        assert cast(Any, response.is_closed) is True