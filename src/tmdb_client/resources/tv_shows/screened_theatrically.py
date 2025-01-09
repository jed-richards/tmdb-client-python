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
from ...types.tv_shows.screened_theatrically_list_response import ScreenedTheatricallyListResponse

__all__ = ["ScreenedTheatricallyResource", "AsyncScreenedTheatricallyResource"]


class ScreenedTheatricallyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScreenedTheatricallyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return ScreenedTheatricallyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScreenedTheatricallyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return ScreenedTheatricallyResourceWithStreamingResponse(self)

    def list(
        self,
        series_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScreenedTheatricallyListResponse:
        """
        Get the seasons and episodes that have screened theatrically.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/3/tv/{series_id}/screened_theatrically",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScreenedTheatricallyListResponse,
        )


class AsyncScreenedTheatricallyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScreenedTheatricallyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncScreenedTheatricallyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScreenedTheatricallyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncScreenedTheatricallyResourceWithStreamingResponse(self)

    async def list(
        self,
        series_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScreenedTheatricallyListResponse:
        """
        Get the seasons and episodes that have screened theatrically.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/3/tv/{series_id}/screened_theatrically",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ScreenedTheatricallyListResponse,
        )


class ScreenedTheatricallyResourceWithRawResponse:
    def __init__(self, screened_theatrically: ScreenedTheatricallyResource) -> None:
        self._screened_theatrically = screened_theatrically

        self.list = to_raw_response_wrapper(
            screened_theatrically.list,
        )


class AsyncScreenedTheatricallyResourceWithRawResponse:
    def __init__(self, screened_theatrically: AsyncScreenedTheatricallyResource) -> None:
        self._screened_theatrically = screened_theatrically

        self.list = async_to_raw_response_wrapper(
            screened_theatrically.list,
        )


class ScreenedTheatricallyResourceWithStreamingResponse:
    def __init__(self, screened_theatrically: ScreenedTheatricallyResource) -> None:
        self._screened_theatrically = screened_theatrically

        self.list = to_streamed_response_wrapper(
            screened_theatrically.list,
        )


class AsyncScreenedTheatricallyResourceWithStreamingResponse:
    def __init__(self, screened_theatrically: AsyncScreenedTheatricallyResource) -> None:
        self._screened_theatrically = screened_theatrically

        self.list = async_to_streamed_response_wrapper(
            screened_theatrically.list,
        )
