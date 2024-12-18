# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import tv_sery_lists_params
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
from ..types.tv_sery_lists_response import TvSeryListsResponse

__all__ = ["TvSeriesResource", "AsyncTvSeriesResource"]


class TvSeriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TvSeriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return TvSeriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TvSeriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return TvSeriesResourceWithStreamingResponse(self)

    def lists(
        self,
        series_id: int,
        *,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TvSeryListsResponse:
        """
        Get the lists that a TV series has been added to.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/3/tv/{series_id}/lists",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "language": language,
                        "page": page,
                    },
                    tv_sery_lists_params.TvSeryListsParams,
                ),
            ),
            cast_to=TvSeryListsResponse,
        )


class AsyncTvSeriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTvSeriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTvSeriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTvSeriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncTvSeriesResourceWithStreamingResponse(self)

    async def lists(
        self,
        series_id: int,
        *,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TvSeryListsResponse:
        """
        Get the lists that a TV series has been added to.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/3/tv/{series_id}/lists",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "language": language,
                        "page": page,
                    },
                    tv_sery_lists_params.TvSeryListsParams,
                ),
            ),
            cast_to=TvSeryListsResponse,
        )


class TvSeriesResourceWithRawResponse:
    def __init__(self, tv_series: TvSeriesResource) -> None:
        self._tv_series = tv_series

        self.lists = to_raw_response_wrapper(
            tv_series.lists,
        )


class AsyncTvSeriesResourceWithRawResponse:
    def __init__(self, tv_series: AsyncTvSeriesResource) -> None:
        self._tv_series = tv_series

        self.lists = async_to_raw_response_wrapper(
            tv_series.lists,
        )


class TvSeriesResourceWithStreamingResponse:
    def __init__(self, tv_series: TvSeriesResource) -> None:
        self._tv_series = tv_series

        self.lists = to_streamed_response_wrapper(
            tv_series.lists,
        )


class AsyncTvSeriesResourceWithStreamingResponse:
    def __init__(self, tv_series: AsyncTvSeriesResource) -> None:
        self._tv_series = tv_series

        self.lists = async_to_streamed_response_wrapper(
            tv_series.lists,
        )
