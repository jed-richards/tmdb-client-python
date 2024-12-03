# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.tv_shows import rating_rate_params, rating_delete_params
from ...types.tv_shows.rating_rate_response import RatingRateResponse
from ...types.tv_shows.rating_delete_response import RatingDeleteResponse

__all__ = ["RatingResource", "AsyncRatingResource"]


class RatingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RatingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return RatingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RatingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return RatingResourceWithStreamingResponse(self)

    def delete(
        self,
        series_id: int,
        *,
        guest_session_id: str | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RatingDeleteResponse:
        """
        Delete Rating

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/3/tv/{series_id}/rating",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "guest_session_id": guest_session_id,
                        "session_id": session_id,
                    },
                    rating_delete_params.RatingDeleteParams,
                ),
            ),
            cast_to=RatingDeleteResponse,
        )

    def rate(
        self,
        series_id: int,
        *,
        raw_body: str,
        guest_session_id: str | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RatingRateResponse:
        """
        Rate a TV show and save it to your rated list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/3/tv/{series_id}/rating",
            body=maybe_transform({"raw_body": raw_body}, rating_rate_params.RatingRateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "guest_session_id": guest_session_id,
                        "session_id": session_id,
                    },
                    rating_rate_params.RatingRateParams,
                ),
            ),
            cast_to=RatingRateResponse,
        )


class AsyncRatingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRatingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRatingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRatingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return AsyncRatingResourceWithStreamingResponse(self)

    async def delete(
        self,
        series_id: int,
        *,
        guest_session_id: str | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RatingDeleteResponse:
        """
        Delete Rating

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/3/tv/{series_id}/rating",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "guest_session_id": guest_session_id,
                        "session_id": session_id,
                    },
                    rating_delete_params.RatingDeleteParams,
                ),
            ),
            cast_to=RatingDeleteResponse,
        )

    async def rate(
        self,
        series_id: int,
        *,
        raw_body: str,
        guest_session_id: str | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RatingRateResponse:
        """
        Rate a TV show and save it to your rated list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/3/tv/{series_id}/rating",
            body=await async_maybe_transform({"raw_body": raw_body}, rating_rate_params.RatingRateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "guest_session_id": guest_session_id,
                        "session_id": session_id,
                    },
                    rating_rate_params.RatingRateParams,
                ),
            ),
            cast_to=RatingRateResponse,
        )


class RatingResourceWithRawResponse:
    def __init__(self, rating: RatingResource) -> None:
        self._rating = rating

        self.delete = to_raw_response_wrapper(
            rating.delete,
        )
        self.rate = to_raw_response_wrapper(
            rating.rate,
        )


class AsyncRatingResourceWithRawResponse:
    def __init__(self, rating: AsyncRatingResource) -> None:
        self._rating = rating

        self.delete = async_to_raw_response_wrapper(
            rating.delete,
        )
        self.rate = async_to_raw_response_wrapper(
            rating.rate,
        )


class RatingResourceWithStreamingResponse:
    def __init__(self, rating: RatingResource) -> None:
        self._rating = rating

        self.delete = to_streamed_response_wrapper(
            rating.delete,
        )
        self.rate = to_streamed_response_wrapper(
            rating.rate,
        )


class AsyncRatingResourceWithStreamingResponse:
    def __init__(self, rating: AsyncRatingResource) -> None:
        self._rating = rating

        self.delete = async_to_streamed_response_wrapper(
            rating.delete,
        )
        self.rate = async_to_streamed_response_wrapper(
            rating.rate,
        )
