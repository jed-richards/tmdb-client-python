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
from ...types.tv_shows.alternative_title_retrieve_response import AlternativeTitleRetrieveResponse

__all__ = ["AlternativeTitlesResource", "AsyncAlternativeTitlesResource"]


class AlternativeTitlesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AlternativeTitlesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AlternativeTitlesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AlternativeTitlesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AlternativeTitlesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        series_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AlternativeTitleRetrieveResponse:
        """
        Get the alternative titles that have been added to a TV show.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/3/tv/{series_id}/alternative_titles",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlternativeTitleRetrieveResponse,
        )


class AsyncAlternativeTitlesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAlternativeTitlesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAlternativeTitlesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAlternativeTitlesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncAlternativeTitlesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        series_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AlternativeTitleRetrieveResponse:
        """
        Get the alternative titles that have been added to a TV show.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/3/tv/{series_id}/alternative_titles",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlternativeTitleRetrieveResponse,
        )


class AlternativeTitlesResourceWithRawResponse:
    def __init__(self, alternative_titles: AlternativeTitlesResource) -> None:
        self._alternative_titles = alternative_titles

        self.retrieve = to_raw_response_wrapper(
            alternative_titles.retrieve,
        )


class AsyncAlternativeTitlesResourceWithRawResponse:
    def __init__(self, alternative_titles: AsyncAlternativeTitlesResource) -> None:
        self._alternative_titles = alternative_titles

        self.retrieve = async_to_raw_response_wrapper(
            alternative_titles.retrieve,
        )


class AlternativeTitlesResourceWithStreamingResponse:
    def __init__(self, alternative_titles: AlternativeTitlesResource) -> None:
        self._alternative_titles = alternative_titles

        self.retrieve = to_streamed_response_wrapper(
            alternative_titles.retrieve,
        )


class AsyncAlternativeTitlesResourceWithStreamingResponse:
    def __init__(self, alternative_titles: AsyncAlternativeTitlesResource) -> None:
        self._alternative_titles = alternative_titles

        self.retrieve = async_to_streamed_response_wrapper(
            alternative_titles.retrieve,
        )