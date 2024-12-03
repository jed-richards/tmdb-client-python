# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.review_retrieve_response import ReviewRetrieveResponse

__all__ = ["ReviewsResource", "AsyncReviewsResource"]


class ReviewsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReviewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return ReviewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReviewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return ReviewsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        review_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReviewRetrieveResponse:
        """
        Retrieve the details of a movie or TV show review.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not review_id:
            raise ValueError(f"Expected a non-empty value for `review_id` but received {review_id!r}")
        return self._get(
            f"/3/review/{review_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReviewRetrieveResponse,
        )


class AsyncReviewsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReviewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReviewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReviewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncReviewsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        review_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReviewRetrieveResponse:
        """
        Retrieve the details of a movie or TV show review.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not review_id:
            raise ValueError(f"Expected a non-empty value for `review_id` but received {review_id!r}")
        return await self._get(
            f"/3/review/{review_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ReviewRetrieveResponse,
        )


class ReviewsResourceWithRawResponse:
    def __init__(self, reviews: ReviewsResource) -> None:
        self._reviews = reviews

        self.retrieve = to_raw_response_wrapper(
            reviews.retrieve,
        )


class AsyncReviewsResourceWithRawResponse:
    def __init__(self, reviews: AsyncReviewsResource) -> None:
        self._reviews = reviews

        self.retrieve = async_to_raw_response_wrapper(
            reviews.retrieve,
        )


class ReviewsResourceWithStreamingResponse:
    def __init__(self, reviews: ReviewsResource) -> None:
        self._reviews = reviews

        self.retrieve = to_streamed_response_wrapper(
            reviews.retrieve,
        )


class AsyncReviewsResourceWithStreamingResponse:
    def __init__(self, reviews: AsyncReviewsResource) -> None:
        self._reviews = reviews

        self.retrieve = async_to_streamed_response_wrapper(
            reviews.retrieve,
        )
