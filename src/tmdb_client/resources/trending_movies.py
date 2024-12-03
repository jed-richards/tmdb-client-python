# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import trending_movie_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.trending_movie_list_response import TrendingMovieListResponse

__all__ = ["TrendingMoviesResource", "AsyncTrendingMoviesResource"]


class TrendingMoviesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TrendingMoviesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return TrendingMoviesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrendingMoviesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return TrendingMoviesResourceWithStreamingResponse(self)

    def list(
        self,
        time_window: Literal["day", "week"],
        *,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrendingMovieListResponse:
        """
        Get the trending movies on TMDB.

        Args:
          language: `ISO-639-1`-`ISO-3166-1` code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not time_window:
            raise ValueError(f"Expected a non-empty value for `time_window` but received {time_window!r}")
        return self._get(
            f"/3/trending/movie/{time_window}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"language": language}, trending_movie_list_params.TrendingMovieListParams),
            ),
            cast_to=TrendingMovieListResponse,
        )


class AsyncTrendingMoviesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTrendingMoviesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTrendingMoviesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrendingMoviesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return AsyncTrendingMoviesResourceWithStreamingResponse(self)

    async def list(
        self,
        time_window: Literal["day", "week"],
        *,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrendingMovieListResponse:
        """
        Get the trending movies on TMDB.

        Args:
          language: `ISO-639-1`-`ISO-3166-1` code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not time_window:
            raise ValueError(f"Expected a non-empty value for `time_window` but received {time_window!r}")
        return await self._get(
            f"/3/trending/movie/{time_window}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"language": language}, trending_movie_list_params.TrendingMovieListParams
                ),
            ),
            cast_to=TrendingMovieListResponse,
        )


class TrendingMoviesResourceWithRawResponse:
    def __init__(self, trending_movies: TrendingMoviesResource) -> None:
        self._trending_movies = trending_movies

        self.list = to_raw_response_wrapper(
            trending_movies.list,
        )


class AsyncTrendingMoviesResourceWithRawResponse:
    def __init__(self, trending_movies: AsyncTrendingMoviesResource) -> None:
        self._trending_movies = trending_movies

        self.list = async_to_raw_response_wrapper(
            trending_movies.list,
        )


class TrendingMoviesResourceWithStreamingResponse:
    def __init__(self, trending_movies: TrendingMoviesResource) -> None:
        self._trending_movies = trending_movies

        self.list = to_streamed_response_wrapper(
            trending_movies.list,
        )


class AsyncTrendingMoviesResourceWithStreamingResponse:
    def __init__(self, trending_movies: AsyncTrendingMoviesResource) -> None:
        self._trending_movies = trending_movies

        self.list = async_to_streamed_response_wrapper(
            trending_movies.list,
        )
