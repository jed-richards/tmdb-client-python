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
from ...types.authentication import session_new_params, session_delete_params, session_convert_params
from ...types.authentication.session_new_response import SessionNewResponse
from ...types.authentication.session_delete_response import SessionDeleteResponse
from ...types.authentication.session_convert_response import SessionConvertResponse

__all__ = ["SessionResource", "AsyncSessionResource"]


class SessionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SessionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return SessionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SessionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return SessionResourceWithStreamingResponse(self)

    def delete(
        self,
        *,
        raw_body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionDeleteResponse:
        """
        Delete Session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/3/authentication/session",
            body=maybe_transform({"raw_body": raw_body}, session_delete_params.SessionDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionDeleteResponse,
        )

    def convert(
        self,
        *,
        raw_body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionConvertResponse:
        """
        Create Session (from v4 token)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/3/authentication/session/convert/4",
            body=maybe_transform({"raw_body": raw_body}, session_convert_params.SessionConvertParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionConvertResponse,
        )

    def new(
        self,
        *,
        raw_body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionNewResponse:
        """
        Create Session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/3/authentication/session/new",
            body=maybe_transform({"raw_body": raw_body}, session_new_params.SessionNewParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionNewResponse,
        )


class AsyncSessionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSessionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSessionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSessionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return AsyncSessionResourceWithStreamingResponse(self)

    async def delete(
        self,
        *,
        raw_body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionDeleteResponse:
        """
        Delete Session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/3/authentication/session",
            body=await async_maybe_transform({"raw_body": raw_body}, session_delete_params.SessionDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionDeleteResponse,
        )

    async def convert(
        self,
        *,
        raw_body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionConvertResponse:
        """
        Create Session (from v4 token)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/3/authentication/session/convert/4",
            body=await async_maybe_transform({"raw_body": raw_body}, session_convert_params.SessionConvertParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionConvertResponse,
        )

    async def new(
        self,
        *,
        raw_body: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SessionNewResponse:
        """
        Create Session

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/3/authentication/session/new",
            body=await async_maybe_transform({"raw_body": raw_body}, session_new_params.SessionNewParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SessionNewResponse,
        )


class SessionResourceWithRawResponse:
    def __init__(self, session: SessionResource) -> None:
        self._session = session

        self.delete = to_raw_response_wrapper(
            session.delete,
        )
        self.convert = to_raw_response_wrapper(
            session.convert,
        )
        self.new = to_raw_response_wrapper(
            session.new,
        )


class AsyncSessionResourceWithRawResponse:
    def __init__(self, session: AsyncSessionResource) -> None:
        self._session = session

        self.delete = async_to_raw_response_wrapper(
            session.delete,
        )
        self.convert = async_to_raw_response_wrapper(
            session.convert,
        )
        self.new = async_to_raw_response_wrapper(
            session.new,
        )


class SessionResourceWithStreamingResponse:
    def __init__(self, session: SessionResource) -> None:
        self._session = session

        self.delete = to_streamed_response_wrapper(
            session.delete,
        )
        self.convert = to_streamed_response_wrapper(
            session.convert,
        )
        self.new = to_streamed_response_wrapper(
            session.new,
        )


class AsyncSessionResourceWithStreamingResponse:
    def __init__(self, session: AsyncSessionResource) -> None:
        self._session = session

        self.delete = async_to_streamed_response_wrapper(
            session.delete,
        )
        self.convert = async_to_streamed_response_wrapper(
            session.convert,
        )
        self.new = async_to_streamed_response_wrapper(
            session.new,
        )
