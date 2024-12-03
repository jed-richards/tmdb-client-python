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
from ...types.watch_providers import tv_show_list_params
from ...types.watch_providers.tv_show_list_response import TvShowListResponse

__all__ = ["TvShowsResource", "AsyncTvShowsResource"]


class TvShowsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TvShowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return TvShowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TvShowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return TvShowsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        language: str | NotGiven = NOT_GIVEN,
        watch_region: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TvShowListResponse:
        """
        Get the list of streaming providers we have for TV shows.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/3/watch/providers/tv",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "language": language,
                        "watch_region": watch_region,
                    },
                    tv_show_list_params.TvShowListParams,
                ),
            ),
            cast_to=TvShowListResponse,
        )


class AsyncTvShowsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTvShowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTvShowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTvShowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncTvShowsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        language: str | NotGiven = NOT_GIVEN,
        watch_region: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TvShowListResponse:
        """
        Get the list of streaming providers we have for TV shows.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/3/watch/providers/tv",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "language": language,
                        "watch_region": watch_region,
                    },
                    tv_show_list_params.TvShowListParams,
                ),
            ),
            cast_to=TvShowListResponse,
        )


class TvShowsResourceWithRawResponse:
    def __init__(self, tv_shows: TvShowsResource) -> None:
        self._tv_shows = tv_shows

        self.list = to_raw_response_wrapper(
            tv_shows.list,
        )


class AsyncTvShowsResourceWithRawResponse:
    def __init__(self, tv_shows: AsyncTvShowsResource) -> None:
        self._tv_shows = tv_shows

        self.list = async_to_raw_response_wrapper(
            tv_shows.list,
        )


class TvShowsResourceWithStreamingResponse:
    def __init__(self, tv_shows: TvShowsResource) -> None:
        self._tv_shows = tv_shows

        self.list = to_streamed_response_wrapper(
            tv_shows.list,
        )


class AsyncTvShowsResourceWithStreamingResponse:
    def __init__(self, tv_shows: AsyncTvShowsResource) -> None:
        self._tv_shows = tv_shows

        self.list = async_to_streamed_response_wrapper(
            tv_shows.list,
        )
