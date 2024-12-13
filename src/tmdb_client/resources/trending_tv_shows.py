# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import trending_tv_show_list_params
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
from ..types.trending_tv_show_list_response import TrendingTvShowListResponse

__all__ = ["TrendingTvShowsResource", "AsyncTrendingTvShowsResource"]


class TrendingTvShowsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TrendingTvShowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return TrendingTvShowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrendingTvShowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return TrendingTvShowsResourceWithStreamingResponse(self)

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
    ) -> TrendingTvShowListResponse:
        """
        Get the trending TV shows on TMDB.

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
            f"/3/trending/tv/{time_window}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"language": language}, trending_tv_show_list_params.TrendingTvShowListParams),
            ),
            cast_to=TrendingTvShowListResponse,
        )


class AsyncTrendingTvShowsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTrendingTvShowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTrendingTvShowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrendingTvShowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncTrendingTvShowsResourceWithStreamingResponse(self)

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
    ) -> TrendingTvShowListResponse:
        """
        Get the trending TV shows on TMDB.

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
            f"/3/trending/tv/{time_window}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"language": language}, trending_tv_show_list_params.TrendingTvShowListParams
                ),
            ),
            cast_to=TrendingTvShowListResponse,
        )


class TrendingTvShowsResourceWithRawResponse:
    def __init__(self, trending_tv_shows: TrendingTvShowsResource) -> None:
        self._trending_tv_shows = trending_tv_shows

        self.list = to_raw_response_wrapper(
            trending_tv_shows.list,
        )


class AsyncTrendingTvShowsResourceWithRawResponse:
    def __init__(self, trending_tv_shows: AsyncTrendingTvShowsResource) -> None:
        self._trending_tv_shows = trending_tv_shows

        self.list = async_to_raw_response_wrapper(
            trending_tv_shows.list,
        )


class TrendingTvShowsResourceWithStreamingResponse:
    def __init__(self, trending_tv_shows: TrendingTvShowsResource) -> None:
        self._trending_tv_shows = trending_tv_shows

        self.list = to_streamed_response_wrapper(
            trending_tv_shows.list,
        )


class AsyncTrendingTvShowsResourceWithStreamingResponse:
    def __init__(self, trending_tv_shows: AsyncTrendingTvShowsResource) -> None:
        self._trending_tv_shows = trending_tv_shows

        self.list = async_to_streamed_response_wrapper(
            trending_tv_shows.list,
        )