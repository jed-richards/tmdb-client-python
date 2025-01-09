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
from ...types.tv_shows.content_rating_retrieve_response import ContentRatingRetrieveResponse

__all__ = ["ContentRatingsResource", "AsyncContentRatingsResource"]


class ContentRatingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContentRatingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return ContentRatingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContentRatingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return ContentRatingsResourceWithStreamingResponse(self)

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
    ) -> ContentRatingRetrieveResponse:
        """
        Get the content ratings that have been added to a TV show.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/3/tv/{series_id}/content_ratings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContentRatingRetrieveResponse,
        )


class AsyncContentRatingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContentRatingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContentRatingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContentRatingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncContentRatingsResourceWithStreamingResponse(self)

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
    ) -> ContentRatingRetrieveResponse:
        """
        Get the content ratings that have been added to a TV show.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/3/tv/{series_id}/content_ratings",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContentRatingRetrieveResponse,
        )


class ContentRatingsResourceWithRawResponse:
    def __init__(self, content_ratings: ContentRatingsResource) -> None:
        self._content_ratings = content_ratings

        self.retrieve = to_raw_response_wrapper(
            content_ratings.retrieve,
        )


class AsyncContentRatingsResourceWithRawResponse:
    def __init__(self, content_ratings: AsyncContentRatingsResource) -> None:
        self._content_ratings = content_ratings

        self.retrieve = async_to_raw_response_wrapper(
            content_ratings.retrieve,
        )


class ContentRatingsResourceWithStreamingResponse:
    def __init__(self, content_ratings: ContentRatingsResource) -> None:
        self._content_ratings = content_ratings

        self.retrieve = to_streamed_response_wrapper(
            content_ratings.retrieve,
        )


class AsyncContentRatingsResourceWithStreamingResponse:
    def __init__(self, content_ratings: AsyncContentRatingsResource) -> None:
        self._content_ratings = content_ratings

        self.retrieve = async_to_streamed_response_wrapper(
            content_ratings.retrieve,
        )
