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
from ...types.movies import upcoming_list_params
from ...types.movies.upcoming_list_response import UpcomingListResponse

__all__ = ["UpcomingResource", "AsyncUpcomingResource"]


class UpcomingResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UpcomingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return UpcomingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UpcomingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return UpcomingResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UpcomingListResponse:
        """
        Get a list of movies that are being released soon.

        Args:
          region: ISO-3166-1 code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/3/movie/upcoming",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "language": language,
                        "page": page,
                        "region": region,
                    },
                    upcoming_list_params.UpcomingListParams,
                ),
            ),
            cast_to=UpcomingListResponse,
        )


class AsyncUpcomingResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUpcomingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUpcomingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUpcomingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return AsyncUpcomingResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UpcomingListResponse:
        """
        Get a list of movies that are being released soon.

        Args:
          region: ISO-3166-1 code

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/3/movie/upcoming",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "language": language,
                        "page": page,
                        "region": region,
                    },
                    upcoming_list_params.UpcomingListParams,
                ),
            ),
            cast_to=UpcomingListResponse,
        )


class UpcomingResourceWithRawResponse:
    def __init__(self, upcoming: UpcomingResource) -> None:
        self._upcoming = upcoming

        self.list = to_raw_response_wrapper(
            upcoming.list,
        )


class AsyncUpcomingResourceWithRawResponse:
    def __init__(self, upcoming: AsyncUpcomingResource) -> None:
        self._upcoming = upcoming

        self.list = async_to_raw_response_wrapper(
            upcoming.list,
        )


class UpcomingResourceWithStreamingResponse:
    def __init__(self, upcoming: UpcomingResource) -> None:
        self._upcoming = upcoming

        self.list = to_streamed_response_wrapper(
            upcoming.list,
        )


class AsyncUpcomingResourceWithStreamingResponse:
    def __init__(self, upcoming: AsyncUpcomingResource) -> None:
        self._upcoming = upcoming

        self.list = async_to_streamed_response_wrapper(
            upcoming.list,
        )
