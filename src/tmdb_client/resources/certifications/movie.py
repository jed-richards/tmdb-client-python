# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.certifications.movie_list_response import MovieListResponse

__all__ = ["MovieResource", "AsyncMovieResource"]


class MovieResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MovieResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return MovieResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MovieResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return MovieResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MovieListResponse:
        """
        Get an up to date list of the officially supported movie certifications on TMDB.
        """
        return self._get(
            "/3/certification/movie/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MovieListResponse,
        )


class AsyncMovieResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMovieResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMovieResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMovieResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return AsyncMovieResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MovieListResponse:
        """
        Get an up to date list of the officially supported movie certifications on TMDB.
        """
        return await self._get(
            "/3/certification/movie/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=MovieListResponse,
        )


class MovieResourceWithRawResponse:
    def __init__(self, movie: MovieResource) -> None:
        self._movie = movie

        self.list = to_raw_response_wrapper(
            movie.list,
        )


class AsyncMovieResourceWithRawResponse:
    def __init__(self, movie: AsyncMovieResource) -> None:
        self._movie = movie

        self.list = async_to_raw_response_wrapper(
            movie.list,
        )


class MovieResourceWithStreamingResponse:
    def __init__(self, movie: MovieResource) -> None:
        self._movie = movie

        self.list = to_streamed_response_wrapper(
            movie.list,
        )


class AsyncMovieResourceWithStreamingResponse:
    def __init__(self, movie: AsyncMovieResource) -> None:
        self._movie = movie

        self.list = async_to_streamed_response_wrapper(
            movie.list,
        )
