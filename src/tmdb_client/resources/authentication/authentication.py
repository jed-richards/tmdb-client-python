# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .token import (
    TokenResource,
    AsyncTokenResource,
    TokenResourceWithRawResponse,
    AsyncTokenResourceWithRawResponse,
    TokenResourceWithStreamingResponse,
    AsyncTokenResourceWithStreamingResponse,
)
from .session import (
    SessionResource,
    AsyncSessionResource,
    SessionResourceWithRawResponse,
    AsyncSessionResourceWithRawResponse,
    SessionResourceWithStreamingResponse,
    AsyncSessionResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .guest_session import (
    GuestSessionResource,
    AsyncGuestSessionResource,
    GuestSessionResourceWithRawResponse,
    AsyncGuestSessionResourceWithRawResponse,
    GuestSessionResourceWithStreamingResponse,
    AsyncGuestSessionResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.authentication_test_key_response import AuthenticationTestKeyResponse

__all__ = ["AuthenticationResource", "AsyncAuthenticationResource"]


class AuthenticationResource(SyncAPIResource):
    @cached_property
    def guest_session(self) -> GuestSessionResource:
        return GuestSessionResource(self._client)

    @cached_property
    def token(self) -> TokenResource:
        return TokenResource(self._client)

    @cached_property
    def session(self) -> SessionResource:
        return SessionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AuthenticationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AuthenticationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthenticationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return AuthenticationResourceWithStreamingResponse(self)

    def test_key(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthenticationTestKeyResponse:
        """Test your API Key to see if it's valid."""
        return self._get(
            "/3/authentication",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationTestKeyResponse,
        )


class AsyncAuthenticationResource(AsyncAPIResource):
    @cached_property
    def guest_session(self) -> AsyncGuestSessionResource:
        return AsyncGuestSessionResource(self._client)

    @cached_property
    def token(self) -> AsyncTokenResource:
        return AsyncTokenResource(self._client)

    @cached_property
    def session(self) -> AsyncSessionResource:
        return AsyncSessionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAuthenticationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthenticationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthenticationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return AsyncAuthenticationResourceWithStreamingResponse(self)

    async def test_key(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AuthenticationTestKeyResponse:
        """Test your API Key to see if it's valid."""
        return await self._get(
            "/3/authentication",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthenticationTestKeyResponse,
        )


class AuthenticationResourceWithRawResponse:
    def __init__(self, authentication: AuthenticationResource) -> None:
        self._authentication = authentication

        self.test_key = to_raw_response_wrapper(
            authentication.test_key,
        )

    @cached_property
    def guest_session(self) -> GuestSessionResourceWithRawResponse:
        return GuestSessionResourceWithRawResponse(self._authentication.guest_session)

    @cached_property
    def token(self) -> TokenResourceWithRawResponse:
        return TokenResourceWithRawResponse(self._authentication.token)

    @cached_property
    def session(self) -> SessionResourceWithRawResponse:
        return SessionResourceWithRawResponse(self._authentication.session)


class AsyncAuthenticationResourceWithRawResponse:
    def __init__(self, authentication: AsyncAuthenticationResource) -> None:
        self._authentication = authentication

        self.test_key = async_to_raw_response_wrapper(
            authentication.test_key,
        )

    @cached_property
    def guest_session(self) -> AsyncGuestSessionResourceWithRawResponse:
        return AsyncGuestSessionResourceWithRawResponse(self._authentication.guest_session)

    @cached_property
    def token(self) -> AsyncTokenResourceWithRawResponse:
        return AsyncTokenResourceWithRawResponse(self._authentication.token)

    @cached_property
    def session(self) -> AsyncSessionResourceWithRawResponse:
        return AsyncSessionResourceWithRawResponse(self._authentication.session)


class AuthenticationResourceWithStreamingResponse:
    def __init__(self, authentication: AuthenticationResource) -> None:
        self._authentication = authentication

        self.test_key = to_streamed_response_wrapper(
            authentication.test_key,
        )

    @cached_property
    def guest_session(self) -> GuestSessionResourceWithStreamingResponse:
        return GuestSessionResourceWithStreamingResponse(self._authentication.guest_session)

    @cached_property
    def token(self) -> TokenResourceWithStreamingResponse:
        return TokenResourceWithStreamingResponse(self._authentication.token)

    @cached_property
    def session(self) -> SessionResourceWithStreamingResponse:
        return SessionResourceWithStreamingResponse(self._authentication.session)


class AsyncAuthenticationResourceWithStreamingResponse:
    def __init__(self, authentication: AsyncAuthenticationResource) -> None:
        self._authentication = authentication

        self.test_key = async_to_streamed_response_wrapper(
            authentication.test_key,
        )

    @cached_property
    def guest_session(self) -> AsyncGuestSessionResourceWithStreamingResponse:
        return AsyncGuestSessionResourceWithStreamingResponse(self._authentication.guest_session)

    @cached_property
    def token(self) -> AsyncTokenResourceWithStreamingResponse:
        return AsyncTokenResourceWithStreamingResponse(self._authentication.token)

    @cached_property
    def session(self) -> AsyncSessionResourceWithStreamingResponse:
        return AsyncSessionResourceWithStreamingResponse(self._authentication.session)
