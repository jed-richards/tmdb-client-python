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
from ...types.people import tv_credit_list_params
from ...types.people.tv_credit_list_response import TvCreditListResponse

__all__ = ["TvCreditsResource", "AsyncTvCreditsResource"]


class TvCreditsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TvCreditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return TvCreditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TvCreditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return TvCreditsResourceWithStreamingResponse(self)

    def list(
        self,
        person_id: int,
        *,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TvCreditListResponse:
        """
        Get the TV credits that belong to a person.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/3/person/{person_id}/tv_credits",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"language": language}, tv_credit_list_params.TvCreditListParams),
            ),
            cast_to=TvCreditListResponse,
        )


class AsyncTvCreditsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTvCreditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTvCreditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTvCreditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncTvCreditsResourceWithStreamingResponse(self)

    async def list(
        self,
        person_id: int,
        *,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TvCreditListResponse:
        """
        Get the TV credits that belong to a person.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/3/person/{person_id}/tv_credits",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"language": language}, tv_credit_list_params.TvCreditListParams),
            ),
            cast_to=TvCreditListResponse,
        )


class TvCreditsResourceWithRawResponse:
    def __init__(self, tv_credits: TvCreditsResource) -> None:
        self._tv_credits = tv_credits

        self.list = to_raw_response_wrapper(
            tv_credits.list,
        )


class AsyncTvCreditsResourceWithRawResponse:
    def __init__(self, tv_credits: AsyncTvCreditsResource) -> None:
        self._tv_credits = tv_credits

        self.list = async_to_raw_response_wrapper(
            tv_credits.list,
        )


class TvCreditsResourceWithStreamingResponse:
    def __init__(self, tv_credits: TvCreditsResource) -> None:
        self._tv_credits = tv_credits

        self.list = to_streamed_response_wrapper(
            tv_credits.list,
        )


class AsyncTvCreditsResourceWithStreamingResponse:
    def __init__(self, tv_credits: AsyncTvCreditsResource) -> None:
        self._tv_credits = tv_credits

        self.list = async_to_streamed_response_wrapper(
            tv_credits.list,
        )
