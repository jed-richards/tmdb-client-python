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
from ...types.accounts import watchlist_create_params
from ...types.accounts.watchlist_create_response import WatchlistCreateResponse

__all__ = ["WatchlistResource", "AsyncWatchlistResource"]


class WatchlistResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WatchlistResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return WatchlistResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WatchlistResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return WatchlistResourceWithStreamingResponse(self)

    def create(
        self,
        account_id: int,
        *,
        raw_body: str,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WatchlistCreateResponse:
        """
        Add To Watchlist

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/3/account/{account_id}/watchlist",
            body=maybe_transform({"raw_body": raw_body}, watchlist_create_params.WatchlistCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"session_id": session_id}, watchlist_create_params.WatchlistCreateParams),
            ),
            cast_to=WatchlistCreateResponse,
        )


class AsyncWatchlistResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWatchlistResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWatchlistResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWatchlistResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return AsyncWatchlistResourceWithStreamingResponse(self)

    async def create(
        self,
        account_id: int,
        *,
        raw_body: str,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WatchlistCreateResponse:
        """
        Add To Watchlist

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/3/account/{account_id}/watchlist",
            body=await async_maybe_transform({"raw_body": raw_body}, watchlist_create_params.WatchlistCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"session_id": session_id}, watchlist_create_params.WatchlistCreateParams
                ),
            ),
            cast_to=WatchlistCreateResponse,
        )


class WatchlistResourceWithRawResponse:
    def __init__(self, watchlist: WatchlistResource) -> None:
        self._watchlist = watchlist

        self.create = to_raw_response_wrapper(
            watchlist.create,
        )


class AsyncWatchlistResourceWithRawResponse:
    def __init__(self, watchlist: AsyncWatchlistResource) -> None:
        self._watchlist = watchlist

        self.create = async_to_raw_response_wrapper(
            watchlist.create,
        )


class WatchlistResourceWithStreamingResponse:
    def __init__(self, watchlist: WatchlistResource) -> None:
        self._watchlist = watchlist

        self.create = to_streamed_response_wrapper(
            watchlist.create,
        )


class AsyncWatchlistResourceWithStreamingResponse:
    def __init__(self, watchlist: AsyncWatchlistResource) -> None:
        self._watchlist = watchlist

        self.create = async_to_streamed_response_wrapper(
            watchlist.create,
        )
