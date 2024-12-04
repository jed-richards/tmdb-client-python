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
from ...types.tv_shows import popular_list_params
from ...types.tv_shows.popular_list_response import PopularListResponse

__all__ = ["PopularResource", "AsyncPopularResource"]


class PopularResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PopularResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return PopularResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PopularResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return PopularResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PopularListResponse:
        """
        Get a list of TV shows ordered by popularity.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/3/tv/popular",
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
                    popular_list_params.PopularListParams,
                ),
            ),
            cast_to=PopularListResponse,
        )


class AsyncPopularResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPopularResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPopularResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPopularResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncPopularResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PopularListResponse:
        """
        Get a list of TV shows ordered by popularity.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/3/tv/popular",
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
                    popular_list_params.PopularListParams,
                ),
            ),
            cast_to=PopularListResponse,
        )


class PopularResourceWithRawResponse:
    def __init__(self, popular: PopularResource) -> None:
        self._popular = popular

        self.list = to_raw_response_wrapper(
            popular.list,
        )


class AsyncPopularResourceWithRawResponse:
    def __init__(self, popular: AsyncPopularResource) -> None:
        self._popular = popular

        self.list = async_to_raw_response_wrapper(
            popular.list,
        )


class PopularResourceWithStreamingResponse:
    def __init__(self, popular: PopularResource) -> None:
        self._popular = popular

        self.list = to_streamed_response_wrapper(
            popular.list,
        )


class AsyncPopularResourceWithStreamingResponse:
    def __init__(self, popular: AsyncPopularResource) -> None:
        self._popular = popular

        self.list = async_to_streamed_response_wrapper(
            popular.list,
        )
