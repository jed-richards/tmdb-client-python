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
from ...types.movies.release_date_retrieve_response import ReleaseDateRetrieveResponse

__all__ = ["ReleaseDatesResource", "AsyncReleaseDatesResource"]


class ReleaseDatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReleaseDatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return ReleaseDatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReleaseDatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return ReleaseDatesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        movie_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReleaseDateRetrieveResponse:
        """
        Get the release dates and certifications for a movie.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/3/movie/{movie_id}/release_dates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReleaseDateRetrieveResponse,
        )


class AsyncReleaseDatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReleaseDatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReleaseDatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReleaseDatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncReleaseDatesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        movie_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReleaseDateRetrieveResponse:
        """
        Get the release dates and certifications for a movie.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/3/movie/{movie_id}/release_dates",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReleaseDateRetrieveResponse,
        )


class ReleaseDatesResourceWithRawResponse:
    def __init__(self, release_dates: ReleaseDatesResource) -> None:
        self._release_dates = release_dates

        self.retrieve = to_raw_response_wrapper(
            release_dates.retrieve,
        )


class AsyncReleaseDatesResourceWithRawResponse:
    def __init__(self, release_dates: AsyncReleaseDatesResource) -> None:
        self._release_dates = release_dates

        self.retrieve = async_to_raw_response_wrapper(
            release_dates.retrieve,
        )


class ReleaseDatesResourceWithStreamingResponse:
    def __init__(self, release_dates: ReleaseDatesResource) -> None:
        self._release_dates = release_dates

        self.retrieve = to_streamed_response_wrapper(
            release_dates.retrieve,
        )


class AsyncReleaseDatesResourceWithStreamingResponse:
    def __init__(self, release_dates: AsyncReleaseDatesResource) -> None:
        self._release_dates = release_dates

        self.retrieve = async_to_streamed_response_wrapper(
            release_dates.retrieve,
        )
