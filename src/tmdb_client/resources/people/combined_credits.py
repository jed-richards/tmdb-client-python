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
from ...types.people import combined_credit_list_params
from ...types.people.combined_credit_list_response import CombinedCreditListResponse

__all__ = ["CombinedCreditsResource", "AsyncCombinedCreditsResource"]


class CombinedCreditsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CombinedCreditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return CombinedCreditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CombinedCreditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return CombinedCreditsResourceWithStreamingResponse(self)

    def list(
        self,
        person_id: str,
        *,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CombinedCreditListResponse:
        """
        Get the combined movie and TV credits that belong to a person.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not person_id:
            raise ValueError(f"Expected a non-empty value for `person_id` but received {person_id!r}")
        return self._get(
            f"/3/person/{person_id}/combined_credits",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"language": language}, combined_credit_list_params.CombinedCreditListParams),
            ),
            cast_to=CombinedCreditListResponse,
        )


class AsyncCombinedCreditsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCombinedCreditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCombinedCreditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCombinedCreditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncCombinedCreditsResourceWithStreamingResponse(self)

    async def list(
        self,
        person_id: str,
        *,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CombinedCreditListResponse:
        """
        Get the combined movie and TV credits that belong to a person.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not person_id:
            raise ValueError(f"Expected a non-empty value for `person_id` but received {person_id!r}")
        return await self._get(
            f"/3/person/{person_id}/combined_credits",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"language": language}, combined_credit_list_params.CombinedCreditListParams
                ),
            ),
            cast_to=CombinedCreditListResponse,
        )


class CombinedCreditsResourceWithRawResponse:
    def __init__(self, combined_credits: CombinedCreditsResource) -> None:
        self._combined_credits = combined_credits

        self.list = to_raw_response_wrapper(
            combined_credits.list,
        )


class AsyncCombinedCreditsResourceWithRawResponse:
    def __init__(self, combined_credits: AsyncCombinedCreditsResource) -> None:
        self._combined_credits = combined_credits

        self.list = async_to_raw_response_wrapper(
            combined_credits.list,
        )


class CombinedCreditsResourceWithStreamingResponse:
    def __init__(self, combined_credits: CombinedCreditsResource) -> None:
        self._combined_credits = combined_credits

        self.list = to_streamed_response_wrapper(
            combined_credits.list,
        )


class AsyncCombinedCreditsResourceWithStreamingResponse:
    def __init__(self, combined_credits: AsyncCombinedCreditsResource) -> None:
        self._combined_credits = combined_credits

        self.list = async_to_streamed_response_wrapper(
            combined_credits.list,
        )
