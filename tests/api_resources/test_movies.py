# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tmdb_client import TmdbClient, AsyncTmdbClient
from tmdb_client.types import (
    MovieRatingResponse,
    MovieSearchResponse,
    MovieDiscoverResponse,
    MovieRetrieveResponse,
    MovieRatingDeleteResponse,
)
from tmdb_client._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMovies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: TmdbClient) -> None:
        movie = client.movies.retrieve(
            movie_id=0,
        )
        assert_matches_type(MovieRetrieveResponse, movie, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: TmdbClient) -> None:
        movie = client.movies.retrieve(
            movie_id=0,
            append_to_response="append_to_response",
            language="language",
        )
        assert_matches_type(MovieRetrieveResponse, movie, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: TmdbClient) -> None:
        response = client.movies.with_raw_response.retrieve(
            movie_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        movie = response.parse()
        assert_matches_type(MovieRetrieveResponse, movie, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: TmdbClient) -> None:
        with client.movies.with_streaming_response.retrieve(
            movie_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            movie = response.parse()
            assert_matches_type(MovieRetrieveResponse, movie, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_discover(self, client: TmdbClient) -> None:
        movie = client.movies.discover()
        assert_matches_type(MovieDiscoverResponse, movie, path=["response"])

    @parametrize
    def test_method_discover_with_all_params(self, client: TmdbClient) -> None:
        movie = client.movies.discover(
            certification={
                "gte": "gte",
                "lte": "lte",
            },
            certification_country="certification_country",
            include_adult=True,
            include_video=True,
            language="language",
            page=0,
            primary_release_date={
                "gte": parse_date("2019-12-27"),
                "lte": parse_date("2019-12-27"),
            },
            primary_release_year=0,
            region="region",
            release_date={
                "gte": parse_date("2019-12-27"),
                "lte": parse_date("2019-12-27"),
            },
            sort_by="original_title.asc",
            vote_average={
                "gte": 0,
                "lte": 0,
            },
            vote_count={
                "gte": 0,
                "lte": 0,
            },
            watch_region="watch_region",
            with_cast="with_cast",
            with_companies="with_companies",
            with_crew="with_crew",
            with_genres="with_genres",
            with_keywords="with_keywords",
            with_origin_country="with_origin_country",
            with_original_language="with_original_language",
            with_people="with_people",
            with_release_type=0,
            with_runtime={
                "gte": 0,
                "lte": 0,
            },
            with_watch_monetization_types="with_watch_monetization_types",
            with_watch_providers="with_watch_providers",
            without_companies="without_companies",
            without_genres="without_genres",
            without_keywords="without_keywords",
            without_watch_providers="without_watch_providers",
            year=0,
        )
        assert_matches_type(MovieDiscoverResponse, movie, path=["response"])

    @parametrize
    def test_raw_response_discover(self, client: TmdbClient) -> None:
        response = client.movies.with_raw_response.discover()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        movie = response.parse()
        assert_matches_type(MovieDiscoverResponse, movie, path=["response"])

    @parametrize
    def test_streaming_response_discover(self, client: TmdbClient) -> None:
        with client.movies.with_streaming_response.discover() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            movie = response.parse()
            assert_matches_type(MovieDiscoverResponse, movie, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_rating(self, client: TmdbClient) -> None:
        movie = client.movies.rating(
            movie_id=0,
            raw_body="RAW_BODY",
        )
        assert_matches_type(MovieRatingResponse, movie, path=["response"])

    @parametrize
    def test_method_rating_with_all_params(self, client: TmdbClient) -> None:
        movie = client.movies.rating(
            movie_id=0,
            raw_body="RAW_BODY",
            guest_session_id="guest_session_id",
            session_id="session_id",
        )
        assert_matches_type(MovieRatingResponse, movie, path=["response"])

    @parametrize
    def test_raw_response_rating(self, client: TmdbClient) -> None:
        response = client.movies.with_raw_response.rating(
            movie_id=0,
            raw_body="RAW_BODY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        movie = response.parse()
        assert_matches_type(MovieRatingResponse, movie, path=["response"])

    @parametrize
    def test_streaming_response_rating(self, client: TmdbClient) -> None:
        with client.movies.with_streaming_response.rating(
            movie_id=0,
            raw_body="RAW_BODY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            movie = response.parse()
            assert_matches_type(MovieRatingResponse, movie, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_rating_delete(self, client: TmdbClient) -> None:
        movie = client.movies.rating_delete(
            movie_id=0,
        )
        assert_matches_type(MovieRatingDeleteResponse, movie, path=["response"])

    @parametrize
    def test_method_rating_delete_with_all_params(self, client: TmdbClient) -> None:
        movie = client.movies.rating_delete(
            movie_id=0,
            guest_session_id="guest_session_id",
            session_id="session_id",
        )
        assert_matches_type(MovieRatingDeleteResponse, movie, path=["response"])

    @parametrize
    def test_raw_response_rating_delete(self, client: TmdbClient) -> None:
        response = client.movies.with_raw_response.rating_delete(
            movie_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        movie = response.parse()
        assert_matches_type(MovieRatingDeleteResponse, movie, path=["response"])

    @parametrize
    def test_streaming_response_rating_delete(self, client: TmdbClient) -> None:
        with client.movies.with_streaming_response.rating_delete(
            movie_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            movie = response.parse()
            assert_matches_type(MovieRatingDeleteResponse, movie, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search(self, client: TmdbClient) -> None:
        movie = client.movies.search(
            query="query",
        )
        assert_matches_type(MovieSearchResponse, movie, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: TmdbClient) -> None:
        movie = client.movies.search(
            query="query",
            include_adult=True,
            language="language",
            page=0,
            primary_release_year="primary_release_year",
            region="region",
            year="year",
        )
        assert_matches_type(MovieSearchResponse, movie, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: TmdbClient) -> None:
        response = client.movies.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        movie = response.parse()
        assert_matches_type(MovieSearchResponse, movie, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: TmdbClient) -> None:
        with client.movies.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            movie = response.parse()
            assert_matches_type(MovieSearchResponse, movie, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMovies:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTmdbClient) -> None:
        movie = await async_client.movies.retrieve(
            movie_id=0,
        )
        assert_matches_type(MovieRetrieveResponse, movie, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        movie = await async_client.movies.retrieve(
            movie_id=0,
            append_to_response="append_to_response",
            language="language",
        )
        assert_matches_type(MovieRetrieveResponse, movie, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.movies.with_raw_response.retrieve(
            movie_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        movie = await response.parse()
        assert_matches_type(MovieRetrieveResponse, movie, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.movies.with_streaming_response.retrieve(
            movie_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            movie = await response.parse()
            assert_matches_type(MovieRetrieveResponse, movie, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_discover(self, async_client: AsyncTmdbClient) -> None:
        movie = await async_client.movies.discover()
        assert_matches_type(MovieDiscoverResponse, movie, path=["response"])

    @parametrize
    async def test_method_discover_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        movie = await async_client.movies.discover(
            certification={
                "gte": "gte",
                "lte": "lte",
            },
            certification_country="certification_country",
            include_adult=True,
            include_video=True,
            language="language",
            page=0,
            primary_release_date={
                "gte": parse_date("2019-12-27"),
                "lte": parse_date("2019-12-27"),
            },
            primary_release_year=0,
            region="region",
            release_date={
                "gte": parse_date("2019-12-27"),
                "lte": parse_date("2019-12-27"),
            },
            sort_by="original_title.asc",
            vote_average={
                "gte": 0,
                "lte": 0,
            },
            vote_count={
                "gte": 0,
                "lte": 0,
            },
            watch_region="watch_region",
            with_cast="with_cast",
            with_companies="with_companies",
            with_crew="with_crew",
            with_genres="with_genres",
            with_keywords="with_keywords",
            with_origin_country="with_origin_country",
            with_original_language="with_original_language",
            with_people="with_people",
            with_release_type=0,
            with_runtime={
                "gte": 0,
                "lte": 0,
            },
            with_watch_monetization_types="with_watch_monetization_types",
            with_watch_providers="with_watch_providers",
            without_companies="without_companies",
            without_genres="without_genres",
            without_keywords="without_keywords",
            without_watch_providers="without_watch_providers",
            year=0,
        )
        assert_matches_type(MovieDiscoverResponse, movie, path=["response"])

    @parametrize
    async def test_raw_response_discover(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.movies.with_raw_response.discover()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        movie = await response.parse()
        assert_matches_type(MovieDiscoverResponse, movie, path=["response"])

    @parametrize
    async def test_streaming_response_discover(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.movies.with_streaming_response.discover() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            movie = await response.parse()
            assert_matches_type(MovieDiscoverResponse, movie, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_rating(self, async_client: AsyncTmdbClient) -> None:
        movie = await async_client.movies.rating(
            movie_id=0,
            raw_body="RAW_BODY",
        )
        assert_matches_type(MovieRatingResponse, movie, path=["response"])

    @parametrize
    async def test_method_rating_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        movie = await async_client.movies.rating(
            movie_id=0,
            raw_body="RAW_BODY",
            guest_session_id="guest_session_id",
            session_id="session_id",
        )
        assert_matches_type(MovieRatingResponse, movie, path=["response"])

    @parametrize
    async def test_raw_response_rating(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.movies.with_raw_response.rating(
            movie_id=0,
            raw_body="RAW_BODY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        movie = await response.parse()
        assert_matches_type(MovieRatingResponse, movie, path=["response"])

    @parametrize
    async def test_streaming_response_rating(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.movies.with_streaming_response.rating(
            movie_id=0,
            raw_body="RAW_BODY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            movie = await response.parse()
            assert_matches_type(MovieRatingResponse, movie, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_rating_delete(self, async_client: AsyncTmdbClient) -> None:
        movie = await async_client.movies.rating_delete(
            movie_id=0,
        )
        assert_matches_type(MovieRatingDeleteResponse, movie, path=["response"])

    @parametrize
    async def test_method_rating_delete_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        movie = await async_client.movies.rating_delete(
            movie_id=0,
            guest_session_id="guest_session_id",
            session_id="session_id",
        )
        assert_matches_type(MovieRatingDeleteResponse, movie, path=["response"])

    @parametrize
    async def test_raw_response_rating_delete(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.movies.with_raw_response.rating_delete(
            movie_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        movie = await response.parse()
        assert_matches_type(MovieRatingDeleteResponse, movie, path=["response"])

    @parametrize
    async def test_streaming_response_rating_delete(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.movies.with_streaming_response.rating_delete(
            movie_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            movie = await response.parse()
            assert_matches_type(MovieRatingDeleteResponse, movie, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search(self, async_client: AsyncTmdbClient) -> None:
        movie = await async_client.movies.search(
            query="query",
        )
        assert_matches_type(MovieSearchResponse, movie, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        movie = await async_client.movies.search(
            query="query",
            include_adult=True,
            language="language",
            page=0,
            primary_release_year="primary_release_year",
            region="region",
            year="year",
        )
        assert_matches_type(MovieSearchResponse, movie, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.movies.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        movie = await response.parse()
        assert_matches_type(MovieSearchResponse, movie, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.movies.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            movie = await response.parse()
            assert_matches_type(MovieSearchResponse, movie, path=["response"])

        assert cast(Any, response.is_closed) is True
