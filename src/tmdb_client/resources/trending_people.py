# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import trending_person_list_params
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
from ..types.trending_person_list_response import TrendingPersonListResponse

__all__ = ["TrendingPeopleResource", "AsyncTrendingPeopleResource"]


class TrendingPeopleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TrendingPeopleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return TrendingPeopleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TrendingPeopleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return TrendingPeopleResourceWithStreamingResponse(self)

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
    ) -> TrendingPersonListResponse:
        """
        Get the trending people on TMDB.

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
            f"/3/trending/person/{time_window}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"language": language}, trending_person_list_params.TrendingPersonListParams),
            ),
            cast_to=TrendingPersonListResponse,
        )


class AsyncTrendingPeopleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTrendingPeopleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTrendingPeopleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTrendingPeopleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return AsyncTrendingPeopleResourceWithStreamingResponse(self)

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
    ) -> TrendingPersonListResponse:
        """
        Get the trending people on TMDB.

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
            f"/3/trending/person/{time_window}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"language": language}, trending_person_list_params.TrendingPersonListParams
                ),
            ),
            cast_to=TrendingPersonListResponse,
        )


class TrendingPeopleResourceWithRawResponse:
    def __init__(self, trending_people: TrendingPeopleResource) -> None:
        self._trending_people = trending_people

        self.list = to_raw_response_wrapper(
            trending_people.list,
        )


class AsyncTrendingPeopleResourceWithRawResponse:
    def __init__(self, trending_people: AsyncTrendingPeopleResource) -> None:
        self._trending_people = trending_people

        self.list = async_to_raw_response_wrapper(
            trending_people.list,
        )


class TrendingPeopleResourceWithStreamingResponse:
    def __init__(self, trending_people: TrendingPeopleResource) -> None:
        self._trending_people = trending_people

        self.list = to_streamed_response_wrapper(
            trending_people.list,
        )


class AsyncTrendingPeopleResourceWithStreamingResponse:
    def __init__(self, trending_people: AsyncTrendingPeopleResource) -> None:
        self._trending_people = trending_people

        self.list = async_to_streamed_response_wrapper(
            trending_people.list,
        )
