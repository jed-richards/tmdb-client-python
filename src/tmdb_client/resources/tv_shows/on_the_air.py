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
from ...types.tv_shows import on_the_air_list_params
from ...types.tv_shows.on_the_air_list_response import OnTheAirListResponse

__all__ = ["OnTheAirResource", "AsyncOnTheAirResource"]


class OnTheAirResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OnTheAirResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return OnTheAirResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OnTheAirResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return OnTheAirResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        timezone: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OnTheAirListResponse:
        """
        Get a list of TV shows that air in the next 7 days.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/3/tv/on_the_air",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "language": language,
                        "page": page,
                        "timezone": timezone,
                    },
                    on_the_air_list_params.OnTheAirListParams,
                ),
            ),
            cast_to=OnTheAirListResponse,
        )


class AsyncOnTheAirResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOnTheAirResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOnTheAirResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOnTheAirResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncOnTheAirResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        timezone: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OnTheAirListResponse:
        """
        Get a list of TV shows that air in the next 7 days.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/3/tv/on_the_air",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "language": language,
                        "page": page,
                        "timezone": timezone,
                    },
                    on_the_air_list_params.OnTheAirListParams,
                ),
            ),
            cast_to=OnTheAirListResponse,
        )


class OnTheAirResourceWithRawResponse:
    def __init__(self, on_the_air: OnTheAirResource) -> None:
        self._on_the_air = on_the_air

        self.list = to_raw_response_wrapper(
            on_the_air.list,
        )


class AsyncOnTheAirResourceWithRawResponse:
    def __init__(self, on_the_air: AsyncOnTheAirResource) -> None:
        self._on_the_air = on_the_air

        self.list = async_to_raw_response_wrapper(
            on_the_air.list,
        )


class OnTheAirResourceWithStreamingResponse:
    def __init__(self, on_the_air: OnTheAirResource) -> None:
        self._on_the_air = on_the_air

        self.list = to_streamed_response_wrapper(
            on_the_air.list,
        )


class AsyncOnTheAirResourceWithStreamingResponse:
    def __init__(self, on_the_air: AsyncOnTheAirResource) -> None:
        self._on_the_air = on_the_air

        self.list = async_to_streamed_response_wrapper(
            on_the_air.list,
        )
