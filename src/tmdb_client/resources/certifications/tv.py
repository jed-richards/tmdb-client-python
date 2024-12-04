# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.certifications.tv_list_response import TvListResponse

__all__ = ["TvResource", "AsyncTvResource"]


class TvResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TvResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return TvResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TvResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return TvResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TvListResponse:
        """TV Certifications"""
        return self._get(
            "/3/certification/tv/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TvListResponse,
        )


class AsyncTvResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTvResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTvResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTvResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncTvResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TvListResponse:
        """TV Certifications"""
        return await self._get(
            "/3/certification/tv/list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TvListResponse,
        )


class TvResourceWithRawResponse:
    def __init__(self, tv: TvResource) -> None:
        self._tv = tv

        self.list = to_raw_response_wrapper(
            tv.list,
        )


class AsyncTvResourceWithRawResponse:
    def __init__(self, tv: AsyncTvResource) -> None:
        self._tv = tv

        self.list = async_to_raw_response_wrapper(
            tv.list,
        )


class TvResourceWithStreamingResponse:
    def __init__(self, tv: TvResource) -> None:
        self._tv = tv

        self.list = to_streamed_response_wrapper(
            tv.list,
        )


class AsyncTvResourceWithStreamingResponse:
    def __init__(self, tv: AsyncTvResource) -> None:
        self._tv = tv

        self.list = async_to_streamed_response_wrapper(
            tv.list,
        )
