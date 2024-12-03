# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.tv.seasons import watch_provider_list_params
from ....types.tv.seasons.watch_provider_list_response import WatchProviderListResponse

__all__ = ["WatchProvidersResource", "AsyncWatchProvidersResource"]


class WatchProvidersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WatchProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return WatchProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WatchProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return WatchProvidersResourceWithStreamingResponse(self)

    def list(
        self,
        season_number: int,
        *,
        series_id: int,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WatchProviderListResponse:
        """
        Get the list of streaming providers we have for a TV season.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/3/tv/{series_id}/season/{season_number}/watch/providers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"language": language}, watch_provider_list_params.WatchProviderListParams),
            ),
            cast_to=WatchProviderListResponse,
        )


class AsyncWatchProvidersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWatchProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWatchProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWatchProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return AsyncWatchProvidersResourceWithStreamingResponse(self)

    async def list(
        self,
        season_number: int,
        *,
        series_id: int,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> WatchProviderListResponse:
        """
        Get the list of streaming providers we have for a TV season.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/3/tv/{series_id}/season/{season_number}/watch/providers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"language": language}, watch_provider_list_params.WatchProviderListParams
                ),
            ),
            cast_to=WatchProviderListResponse,
        )


class WatchProvidersResourceWithRawResponse:
    def __init__(self, watch_providers: WatchProvidersResource) -> None:
        self._watch_providers = watch_providers

        self.list = to_raw_response_wrapper(
            watch_providers.list,
        )


class AsyncWatchProvidersResourceWithRawResponse:
    def __init__(self, watch_providers: AsyncWatchProvidersResource) -> None:
        self._watch_providers = watch_providers

        self.list = async_to_raw_response_wrapper(
            watch_providers.list,
        )


class WatchProvidersResourceWithStreamingResponse:
    def __init__(self, watch_providers: WatchProvidersResource) -> None:
        self._watch_providers = watch_providers

        self.list = to_streamed_response_wrapper(
            watch_providers.list,
        )


class AsyncWatchProvidersResourceWithStreamingResponse:
    def __init__(self, watch_providers: AsyncWatchProvidersResource) -> None:
        self._watch_providers = watch_providers

        self.list = async_to_streamed_response_wrapper(
            watch_providers.list,
        )
