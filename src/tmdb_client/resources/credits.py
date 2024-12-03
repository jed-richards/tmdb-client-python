# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.credit_retrieve_response import CreditRetrieveResponse

__all__ = ["CreditsResource", "AsyncCreditsResource"]


class CreditsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CreditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return CreditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CreditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return CreditsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        credit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditRetrieveResponse:
        """
        Get a movie or TV credit details by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not credit_id:
            raise ValueError(f"Expected a non-empty value for `credit_id` but received {credit_id!r}")
        return self._get(
            f"/3/credit/{credit_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditRetrieveResponse,
        )


class AsyncCreditsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCreditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCreditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCreditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncCreditsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        credit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CreditRetrieveResponse:
        """
        Get a movie or TV credit details by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not credit_id:
            raise ValueError(f"Expected a non-empty value for `credit_id` but received {credit_id!r}")
        return await self._get(
            f"/3/credit/{credit_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CreditRetrieveResponse,
        )


class CreditsResourceWithRawResponse:
    def __init__(self, credits: CreditsResource) -> None:
        self._credits = credits

        self.retrieve = to_raw_response_wrapper(
            credits.retrieve,
        )


class AsyncCreditsResourceWithRawResponse:
    def __init__(self, credits: AsyncCreditsResource) -> None:
        self._credits = credits

        self.retrieve = async_to_raw_response_wrapper(
            credits.retrieve,
        )


class CreditsResourceWithStreamingResponse:
    def __init__(self, credits: CreditsResource) -> None:
        self._credits = credits

        self.retrieve = to_streamed_response_wrapper(
            credits.retrieve,
        )


class AsyncCreditsResourceWithStreamingResponse:
    def __init__(self, credits: AsyncCreditsResource) -> None:
        self._credits = credits

        self.retrieve = async_to_streamed_response_wrapper(
            credits.retrieve,
        )
