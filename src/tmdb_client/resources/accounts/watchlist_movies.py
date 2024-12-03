# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.accounts import watchlist_movie_list_params
from ...types.accounts.watchlist_movie_list_response import WatchlistMovieListResponse

__all__ = ["WatchlistMoviesResource", "AsyncWatchlistMoviesResource"]


class WatchlistMoviesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WatchlistMoviesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return WatchlistMoviesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WatchlistMoviesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return WatchlistMoviesResourceWithStreamingResponse(self)

    def list(
        self,
        account_id: int,
        *,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        sort_by: Literal["created_at.asc", "created_at.desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WatchlistMovieListResponse:
        """
        Watchlist Movies

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/3/account/{account_id}/watchlist/movies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "language": language,
                        "page": page,
                        "session_id": session_id,
                        "sort_by": sort_by,
                    },
                    watchlist_movie_list_params.WatchlistMovieListParams,
                ),
            ),
            cast_to=WatchlistMovieListResponse,
        )


class AsyncWatchlistMoviesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWatchlistMoviesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWatchlistMoviesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWatchlistMoviesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return AsyncWatchlistMoviesResourceWithStreamingResponse(self)

    async def list(
        self,
        account_id: int,
        *,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        sort_by: Literal["created_at.asc", "created_at.desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WatchlistMovieListResponse:
        """
        Watchlist Movies

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/3/account/{account_id}/watchlist/movies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "language": language,
                        "page": page,
                        "session_id": session_id,
                        "sort_by": sort_by,
                    },
                    watchlist_movie_list_params.WatchlistMovieListParams,
                ),
            ),
            cast_to=WatchlistMovieListResponse,
        )


class WatchlistMoviesResourceWithRawResponse:
    def __init__(self, watchlist_movies: WatchlistMoviesResource) -> None:
        self._watchlist_movies = watchlist_movies

        self.list = to_raw_response_wrapper(
            watchlist_movies.list,
        )


class AsyncWatchlistMoviesResourceWithRawResponse:
    def __init__(self, watchlist_movies: AsyncWatchlistMoviesResource) -> None:
        self._watchlist_movies = watchlist_movies

        self.list = async_to_raw_response_wrapper(
            watchlist_movies.list,
        )


class WatchlistMoviesResourceWithStreamingResponse:
    def __init__(self, watchlist_movies: WatchlistMoviesResource) -> None:
        self._watchlist_movies = watchlist_movies

        self.list = to_streamed_response_wrapper(
            watchlist_movies.list,
        )


class AsyncWatchlistMoviesResourceWithStreamingResponse:
    def __init__(self, watchlist_movies: AsyncWatchlistMoviesResource) -> None:
        self._watchlist_movies = watchlist_movies

        self.list = async_to_streamed_response_wrapper(
            watchlist_movies.list,
        )
