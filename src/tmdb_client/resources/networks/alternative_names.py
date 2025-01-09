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
from ...types.networks.alternative_name_list_response import AlternativeNameListResponse

__all__ = ["AlternativeNamesResource", "AsyncAlternativeNamesResource"]


class AlternativeNamesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AlternativeNamesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AlternativeNamesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AlternativeNamesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AlternativeNamesResourceWithStreamingResponse(self)

    def list(
        self,
        network_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AlternativeNameListResponse:
        """
        Get the alternative names of a network.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/3/network/{network_id}/alternative_names",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlternativeNameListResponse,
        )


class AsyncAlternativeNamesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAlternativeNamesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAlternativeNamesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAlternativeNamesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncAlternativeNamesResourceWithStreamingResponse(self)

    async def list(
        self,
        network_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AlternativeNameListResponse:
        """
        Get the alternative names of a network.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/3/network/{network_id}/alternative_names",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlternativeNameListResponse,
        )


class AlternativeNamesResourceWithRawResponse:
    def __init__(self, alternative_names: AlternativeNamesResource) -> None:
        self._alternative_names = alternative_names

        self.list = to_raw_response_wrapper(
            alternative_names.list,
        )


class AsyncAlternativeNamesResourceWithRawResponse:
    def __init__(self, alternative_names: AsyncAlternativeNamesResource) -> None:
        self._alternative_names = alternative_names

        self.list = async_to_raw_response_wrapper(
            alternative_names.list,
        )


class AlternativeNamesResourceWithStreamingResponse:
    def __init__(self, alternative_names: AlternativeNamesResource) -> None:
        self._alternative_names = alternative_names

        self.list = to_streamed_response_wrapper(
            alternative_names.list,
        )


class AsyncAlternativeNamesResourceWithStreamingResponse:
    def __init__(self, alternative_names: AsyncAlternativeNamesResource) -> None:
        self._alternative_names = alternative_names

        self.list = async_to_streamed_response_wrapper(
            alternative_names.list,
        )
