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
from ...types.tv_shows import top_rated_list_params
from ...types.tv_shows.top_rated_list_response import TopRatedListResponse

__all__ = ["TopRatedResource", "AsyncTopRatedResource"]


class TopRatedResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TopRatedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return TopRatedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopRatedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return TopRatedResourceWithStreamingResponse(self)

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
    ) -> TopRatedListResponse:
        """
        Get a list of TV shows ordered by rating.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/3/tv/top_rated",
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
                    top_rated_list_params.TopRatedListParams,
                ),
            ),
            cast_to=TopRatedListResponse,
        )


class AsyncTopRatedResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTopRatedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTopRatedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopRatedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return AsyncTopRatedResourceWithStreamingResponse(self)

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
    ) -> TopRatedListResponse:
        """
        Get a list of TV shows ordered by rating.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/3/tv/top_rated",
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
                    top_rated_list_params.TopRatedListParams,
                ),
            ),
            cast_to=TopRatedListResponse,
        )


class TopRatedResourceWithRawResponse:
    def __init__(self, top_rated: TopRatedResource) -> None:
        self._top_rated = top_rated

        self.list = to_raw_response_wrapper(
            top_rated.list,
        )


class AsyncTopRatedResourceWithRawResponse:
    def __init__(self, top_rated: AsyncTopRatedResource) -> None:
        self._top_rated = top_rated

        self.list = async_to_raw_response_wrapper(
            top_rated.list,
        )


class TopRatedResourceWithStreamingResponse:
    def __init__(self, top_rated: TopRatedResource) -> None:
        self._top_rated = top_rated

        self.list = to_streamed_response_wrapper(
            top_rated.list,
        )


class AsyncTopRatedResourceWithStreamingResponse:
    def __init__(self, top_rated: AsyncTopRatedResource) -> None:
        self._top_rated = top_rated

        self.list = async_to_streamed_response_wrapper(
            top_rated.list,
        )
