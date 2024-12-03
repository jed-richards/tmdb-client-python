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
from ...types.configuration.timezone_list_response import TimezoneListResponse

__all__ = ["TimezonesResource", "AsyncTimezonesResource"]


class TimezonesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TimezonesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return TimezonesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TimezonesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return TimezonesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimezoneListResponse:
        """Get the list of timezones used throughout TMDB."""
        return self._get(
            "/3/configuration/timezones",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TimezoneListResponse,
        )


class AsyncTimezonesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTimezonesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTimezonesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTimezonesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return AsyncTimezonesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TimezoneListResponse:
        """Get the list of timezones used throughout TMDB."""
        return await self._get(
            "/3/configuration/timezones",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TimezoneListResponse,
        )


class TimezonesResourceWithRawResponse:
    def __init__(self, timezones: TimezonesResource) -> None:
        self._timezones = timezones

        self.list = to_raw_response_wrapper(
            timezones.list,
        )


class AsyncTimezonesResourceWithRawResponse:
    def __init__(self, timezones: AsyncTimezonesResource) -> None:
        self._timezones = timezones

        self.list = async_to_raw_response_wrapper(
            timezones.list,
        )


class TimezonesResourceWithStreamingResponse:
    def __init__(self, timezones: TimezonesResource) -> None:
        self._timezones = timezones

        self.list = to_streamed_response_wrapper(
            timezones.list,
        )


class AsyncTimezonesResourceWithStreamingResponse:
    def __init__(self, timezones: AsyncTimezonesResource) -> None:
        self._timezones = timezones

        self.list = async_to_streamed_response_wrapper(
            timezones.list,
        )
