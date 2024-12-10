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
from ...types.tv_shows import aggregate_credit_retrieve_params
from ...types.tv_shows.aggregate_credit_retrieve_response import AggregateCreditRetrieveResponse

__all__ = ["AggregateCreditsResource", "AsyncAggregateCreditsResource"]


class AggregateCreditsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AggregateCreditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AggregateCreditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AggregateCreditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AggregateCreditsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        series_id: int,
        *,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AggregateCreditRetrieveResponse:
        """
        Get the aggregate credits (cast and crew) that have been added to a TV show.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/3/tv/{series_id}/aggregate_credits",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"language": language}, aggregate_credit_retrieve_params.AggregateCreditRetrieveParams
                ),
            ),
            cast_to=AggregateCreditRetrieveResponse,
        )


class AsyncAggregateCreditsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAggregateCreditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAggregateCreditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAggregateCreditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncAggregateCreditsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        series_id: int,
        *,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AggregateCreditRetrieveResponse:
        """
        Get the aggregate credits (cast and crew) that have been added to a TV show.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/3/tv/{series_id}/aggregate_credits",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"language": language}, aggregate_credit_retrieve_params.AggregateCreditRetrieveParams
                ),
            ),
            cast_to=AggregateCreditRetrieveResponse,
        )


class AggregateCreditsResourceWithRawResponse:
    def __init__(self, aggregate_credits: AggregateCreditsResource) -> None:
        self._aggregate_credits = aggregate_credits

        self.retrieve = to_raw_response_wrapper(
            aggregate_credits.retrieve,
        )


class AsyncAggregateCreditsResourceWithRawResponse:
    def __init__(self, aggregate_credits: AsyncAggregateCreditsResource) -> None:
        self._aggregate_credits = aggregate_credits

        self.retrieve = async_to_raw_response_wrapper(
            aggregate_credits.retrieve,
        )


class AggregateCreditsResourceWithStreamingResponse:
    def __init__(self, aggregate_credits: AggregateCreditsResource) -> None:
        self._aggregate_credits = aggregate_credits

        self.retrieve = to_streamed_response_wrapper(
            aggregate_credits.retrieve,
        )


class AsyncAggregateCreditsResourceWithStreamingResponse:
    def __init__(self, aggregate_credits: AsyncAggregateCreditsResource) -> None:
        self._aggregate_credits = aggregate_credits

        self.retrieve = async_to_streamed_response_wrapper(
            aggregate_credits.retrieve,
        )
