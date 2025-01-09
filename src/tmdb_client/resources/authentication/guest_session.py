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
from ...types.authentication.guest_session_new_response import GuestSessionNewResponse

__all__ = ["GuestSessionResource", "AsyncGuestSessionResource"]


class GuestSessionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GuestSessionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return GuestSessionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GuestSessionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return GuestSessionResourceWithStreamingResponse(self)

    def new(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GuestSessionNewResponse:
        """Create Guest Session"""
        return self._get(
            "/3/authentication/guest_session/new",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GuestSessionNewResponse,
        )


class AsyncGuestSessionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGuestSessionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGuestSessionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGuestSessionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncGuestSessionResourceWithStreamingResponse(self)

    async def new(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GuestSessionNewResponse:
        """Create Guest Session"""
        return await self._get(
            "/3/authentication/guest_session/new",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GuestSessionNewResponse,
        )


class GuestSessionResourceWithRawResponse:
    def __init__(self, guest_session: GuestSessionResource) -> None:
        self._guest_session = guest_session

        self.new = to_raw_response_wrapper(
            guest_session.new,
        )


class AsyncGuestSessionResourceWithRawResponse:
    def __init__(self, guest_session: AsyncGuestSessionResource) -> None:
        self._guest_session = guest_session

        self.new = async_to_raw_response_wrapper(
            guest_session.new,
        )


class GuestSessionResourceWithStreamingResponse:
    def __init__(self, guest_session: GuestSessionResource) -> None:
        self._guest_session = guest_session

        self.new = to_streamed_response_wrapper(
            guest_session.new,
        )


class AsyncGuestSessionResourceWithStreamingResponse:
    def __init__(self, guest_session: AsyncGuestSessionResource) -> None:
        self._guest_session = guest_session

        self.new = async_to_streamed_response_wrapper(
            guest_session.new,
        )
