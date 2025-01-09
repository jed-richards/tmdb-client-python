# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

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
from ...types.people import change_list_params
from ...types.people.change_list_response import ChangeListResponse

__all__ = ["ChangesResource", "AsyncChangesResource"]


class ChangesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ChangesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return ChangesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChangesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return ChangesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        start_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChangeListResponse:
        """
        People List

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/3/person/changes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "page": page,
                        "start_date": start_date,
                    },
                    change_list_params.ChangeListParams,
                ),
            ),
            cast_to=ChangeListResponse,
        )


class AsyncChangesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncChangesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChangesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChangesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncChangesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        start_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ChangeListResponse:
        """
        People List

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/3/person/changes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "page": page,
                        "start_date": start_date,
                    },
                    change_list_params.ChangeListParams,
                ),
            ),
            cast_to=ChangeListResponse,
        )


class ChangesResourceWithRawResponse:
    def __init__(self, changes: ChangesResource) -> None:
        self._changes = changes

        self.list = to_raw_response_wrapper(
            changes.list,
        )


class AsyncChangesResourceWithRawResponse:
    def __init__(self, changes: AsyncChangesResource) -> None:
        self._changes = changes

        self.list = async_to_raw_response_wrapper(
            changes.list,
        )


class ChangesResourceWithStreamingResponse:
    def __init__(self, changes: ChangesResource) -> None:
        self._changes = changes

        self.list = to_streamed_response_wrapper(
            changes.list,
        )


class AsyncChangesResourceWithStreamingResponse:
    def __init__(self, changes: AsyncChangesResource) -> None:
        self._changes = changes

        self.list = async_to_streamed_response_wrapper(
            changes.list,
        )
