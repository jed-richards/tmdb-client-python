# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.watch_providers import movie_list_params
from ...types.watch_providers.movie_list_response import MovieListResponse

__all__ = ["MoviesResource", "AsyncMoviesResource"]


class MoviesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MoviesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return MoviesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MoviesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return MoviesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        language: str | NotGiven = NOT_GIVEN,
        watch_region: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MovieListResponse:
        """
        Get the list of streaming providers we have for movies.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/3/watch/providers/movie",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "language": language,
                        "watch_region": watch_region,
                    },
                    movie_list_params.MovieListParams,
                ),
            ),
            cast_to=MovieListResponse,
        )


class AsyncMoviesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMoviesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMoviesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMoviesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncMoviesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        language: str | NotGiven = NOT_GIVEN,
        watch_region: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MovieListResponse:
        """
        Get the list of streaming providers we have for movies.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/3/watch/providers/movie",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "language": language,
                        "watch_region": watch_region,
                    },
                    movie_list_params.MovieListParams,
                ),
            ),
            cast_to=MovieListResponse,
        )


class MoviesResourceWithRawResponse:
    def __init__(self, movies: MoviesResource) -> None:
        self._movies = movies

        self.list = to_raw_response_wrapper(
            movies.list,
        )


class AsyncMoviesResourceWithRawResponse:
    def __init__(self, movies: AsyncMoviesResource) -> None:
        self._movies = movies

        self.list = async_to_raw_response_wrapper(
            movies.list,
        )


class MoviesResourceWithStreamingResponse:
    def __init__(self, movies: MoviesResource) -> None:
        self._movies = movies

        self.list = to_streamed_response_wrapper(
            movies.list,
        )


class AsyncMoviesResourceWithStreamingResponse:
    def __init__(self, movies: AsyncMoviesResource) -> None:
        self._movies = movies

        self.list = async_to_streamed_response_wrapper(
            movies.list,
        )
