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
from ...types.movies import account_state_retrieve_params
from ...types.movies.account_state_retrieve_response import AccountStateRetrieveResponse

__all__ = ["AccountStatesResource", "AsyncAccountStatesResource"]


class AccountStatesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountStatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AccountStatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountStatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AccountStatesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        movie_id: int,
        *,
        guest_session_id: str | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountStateRetrieveResponse:
        """
        Get the rating, watchlist and favourite status of an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/3/movie/{movie_id}/account_states",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "guest_session_id": guest_session_id,
                        "session_id": session_id,
                    },
                    account_state_retrieve_params.AccountStateRetrieveParams,
                ),
            ),
            cast_to=AccountStateRetrieveResponse,
        )


class AsyncAccountStatesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountStatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountStatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountStatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncAccountStatesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        movie_id: int,
        *,
        guest_session_id: str | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountStateRetrieveResponse:
        """
        Get the rating, watchlist and favourite status of an account.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/3/movie/{movie_id}/account_states",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "guest_session_id": guest_session_id,
                        "session_id": session_id,
                    },
                    account_state_retrieve_params.AccountStateRetrieveParams,
                ),
            ),
            cast_to=AccountStateRetrieveResponse,
        )


class AccountStatesResourceWithRawResponse:
    def __init__(self, account_states: AccountStatesResource) -> None:
        self._account_states = account_states

        self.retrieve = to_raw_response_wrapper(
            account_states.retrieve,
        )


class AsyncAccountStatesResourceWithRawResponse:
    def __init__(self, account_states: AsyncAccountStatesResource) -> None:
        self._account_states = account_states

        self.retrieve = async_to_raw_response_wrapper(
            account_states.retrieve,
        )


class AccountStatesResourceWithStreamingResponse:
    def __init__(self, account_states: AccountStatesResource) -> None:
        self._account_states = account_states

        self.retrieve = to_streamed_response_wrapper(
            account_states.retrieve,
        )


class AsyncAccountStatesResourceWithStreamingResponse:
    def __init__(self, account_states: AsyncAccountStatesResource) -> None:
        self._account_states = account_states

        self.retrieve = async_to_streamed_response_wrapper(
            account_states.retrieve,
        )
