# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import trending_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.trending_list_response import TrendingListResponse

__all__ = ["TrendingResource", "AsyncTrendingResource"]


class TrendingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TrendingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return TrendingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrendingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return TrendingResourceWithStreamingResponse(self)

    def list(
        self,
        time_window: Literal["day", "week"],
        *,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrendingListResponse:
        """
        Get the trending movies, TV shows and people.

        Args:
          language: `ISO-639-1`-`ISO-3166-1` code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not time_window:
            raise ValueError(f"Expected a non-empty value for `time_window` but received {time_window!r}")
        return self._get(
            f"/3/trending/all/{time_window}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"language": language}, trending_list_params.TrendingListParams),
            ),
            cast_to=TrendingListResponse,
        )


class AsyncTrendingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTrendingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTrendingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrendingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncTrendingResourceWithStreamingResponse(self)

    async def list(
        self,
        time_window: Literal["day", "week"],
        *,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TrendingListResponse:
        """
        Get the trending movies, TV shows and people.

        Args:
          language: `ISO-639-1`-`ISO-3166-1` code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not time_window:
            raise ValueError(f"Expected a non-empty value for `time_window` but received {time_window!r}")
        return await self._get(
            f"/3/trending/all/{time_window}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"language": language}, trending_list_params.TrendingListParams),
            ),
            cast_to=TrendingListResponse,
        )


class TrendingResourceWithRawResponse:
    def __init__(self, trending: TrendingResource) -> None:
        self._trending = trending

        self.list = to_raw_response_wrapper(
            trending.list,
        )


class AsyncTrendingResourceWithRawResponse:
    def __init__(self, trending: AsyncTrendingResource) -> None:
        self._trending = trending

        self.list = async_to_raw_response_wrapper(
            trending.list,
        )


class TrendingResourceWithStreamingResponse:
    def __init__(self, trending: TrendingResource) -> None:
        self._trending = trending

        self.list = to_streamed_response_wrapper(
            trending.list,
        )


class AsyncTrendingResourceWithStreamingResponse:
    def __init__(self, trending: AsyncTrendingResource) -> None:
        self._trending = trending

        self.list = async_to_streamed_response_wrapper(
            trending.list,
        )
