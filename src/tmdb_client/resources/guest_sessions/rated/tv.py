# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.guest_sessions.rated import tv_list_params
from ....types.guest_sessions.rated.tv_list_response import TvListResponse

__all__ = ["TvResource", "AsyncTvResource"]


class TvResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TvResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return TvResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TvResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return TvResourceWithStreamingResponse(self)

    def list(
        self,
        guest_session_id: str,
        *,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        sort_by: Literal["created_at.asc", "created_at.desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TvListResponse:
        """
        Get the rated TV shows for a guest session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not guest_session_id:
            raise ValueError(f"Expected a non-empty value for `guest_session_id` but received {guest_session_id!r}")
        return self._get(
            f"/3/guest_session/{guest_session_id}/rated/tv",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "language": language,
                        "page": page,
                        "sort_by": sort_by,
                    },
                    tv_list_params.TvListParams,
                ),
            ),
            cast_to=TvListResponse,
        )


class AsyncTvResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTvResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTvResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTvResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return AsyncTvResourceWithStreamingResponse(self)

    async def list(
        self,
        guest_session_id: str,
        *,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        sort_by: Literal["created_at.asc", "created_at.desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TvListResponse:
        """
        Get the rated TV shows for a guest session.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not guest_session_id:
            raise ValueError(f"Expected a non-empty value for `guest_session_id` but received {guest_session_id!r}")
        return await self._get(
            f"/3/guest_session/{guest_session_id}/rated/tv",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "language": language,
                        "page": page,
                        "sort_by": sort_by,
                    },
                    tv_list_params.TvListParams,
                ),
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
