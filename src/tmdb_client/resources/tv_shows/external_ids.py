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
from ...types.tv_shows.external_id_list_response import ExternalIDListResponse

__all__ = ["ExternalIDsResource", "AsyncExternalIDsResource"]


class ExternalIDsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExternalIDsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return ExternalIDsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExternalIDsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return ExternalIDsResourceWithStreamingResponse(self)

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
    ) -> ExternalIDListResponse:
        """
        Get a list of external IDs that have been added to a TV show.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/3/tv/{series_id}/external_ids",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalIDListResponse,
        )


class AsyncExternalIDsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExternalIDsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExternalIDsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExternalIDsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncExternalIDsResourceWithStreamingResponse(self)

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
    ) -> ExternalIDListResponse:
        """
        Get a list of external IDs that have been added to a TV show.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/3/tv/{series_id}/external_ids",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ExternalIDListResponse,
        )


class ExternalIDsResourceWithRawResponse:
    def __init__(self, external_ids: ExternalIDsResource) -> None:
        self._external_ids = external_ids

        self.list = to_raw_response_wrapper(
            external_ids.list,
        )


class AsyncExternalIDsResourceWithRawResponse:
    def __init__(self, external_ids: AsyncExternalIDsResource) -> None:
        self._external_ids = external_ids

        self.list = async_to_raw_response_wrapper(
            external_ids.list,
        )


class ExternalIDsResourceWithStreamingResponse:
    def __init__(self, external_ids: ExternalIDsResource) -> None:
        self._external_ids = external_ids

        self.list = to_streamed_response_wrapper(
            external_ids.list,
        )


class AsyncExternalIDsResourceWithStreamingResponse:
    def __init__(self, external_ids: AsyncExternalIDsResource) -> None:
        self._external_ids = external_ids

        self.list = async_to_streamed_response_wrapper(
            external_ids.list,
        )
