# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tmdb_client import TmdbClient, AsyncTmdbClient
from tmdb_client.types.accounts import WatchlistMovieListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWatchlistMovies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: TmdbClient) -> None:
        watchlist_movie = client.accounts.watchlist_movies.list(
            account_id=0,
        )
        assert_matches_type(WatchlistMovieListResponse, watchlist_movie, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: TmdbClient) -> None:
        watchlist_movie = client.accounts.watchlist_movies.list(
            account_id=0,
            language="language",
            page=0,
            session_id="session_id",
            sort_by="created_at.asc",
        )
        assert_matches_type(WatchlistMovieListResponse, watchlist_movie, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: TmdbClient) -> None:
        response = client.accounts.watchlist_movies.with_raw_response.list(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watchlist_movie = response.parse()
        assert_matches_type(WatchlistMovieListResponse, watchlist_movie, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: TmdbClient) -> None:
        with client.accounts.watchlist_movies.with_streaming_response.list(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watchlist_movie = response.parse()
            assert_matches_type(WatchlistMovieListResponse, watchlist_movie, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWatchlistMovies:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTmdbClient) -> None:
        watchlist_movie = await async_client.accounts.watchlist_movies.list(
            account_id=0,
        )
        assert_matches_type(WatchlistMovieListResponse, watchlist_movie, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        watchlist_movie = await async_client.accounts.watchlist_movies.list(
            account_id=0,
            language="language",
            page=0,
            session_id="session_id",
            sort_by="created_at.asc",
        )
        assert_matches_type(WatchlistMovieListResponse, watchlist_movie, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.accounts.watchlist_movies.with_raw_response.list(
            account_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        watchlist_movie = await response.parse()
        assert_matches_type(WatchlistMovieListResponse, watchlist_movie, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.accounts.watchlist_movies.with_streaming_response.list(
            account_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            watchlist_movie = await response.parse()
            assert_matches_type(WatchlistMovieListResponse, watchlist_movie, path=["response"])

        assert cast(Any, response.is_closed) is True