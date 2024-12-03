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
from ...types.tv_shows import similar_list_params
from ...types.tv_shows.similar_list_response import SimilarListResponse

__all__ = ["SimilarResource", "AsyncSimilarResource"]


class SimilarResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SimilarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return SimilarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimilarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return SimilarResourceWithStreamingResponse(self)

    def list(
        self,
        series_id: str,
        *,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimilarListResponse:
        """
        Get the similar TV shows.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not series_id:
            raise ValueError(f"Expected a non-empty value for `series_id` but received {series_id!r}")
        return self._get(
            f"/3/tv/{series_id}/similar",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "language": language,
                        "page": page,
                    },
                    similar_list_params.SimilarListParams,
                ),
            ),
            cast_to=SimilarListResponse,
        )


class AsyncSimilarResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSimilarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimilarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimilarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return AsyncSimilarResourceWithStreamingResponse(self)

    async def list(
        self,
        series_id: str,
        *,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SimilarListResponse:
        """
        Get the similar TV shows.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not series_id:
            raise ValueError(f"Expected a non-empty value for `series_id` but received {series_id!r}")
        return await self._get(
            f"/3/tv/{series_id}/similar",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "language": language,
                        "page": page,
                    },
                    similar_list_params.SimilarListParams,
                ),
            ),
            cast_to=SimilarListResponse,
        )


class SimilarResourceWithRawResponse:
    def __init__(self, similar: SimilarResource) -> None:
        self._similar = similar

        self.list = to_raw_response_wrapper(
            similar.list,
        )


class AsyncSimilarResourceWithRawResponse:
    def __init__(self, similar: AsyncSimilarResource) -> None:
        self._similar = similar

        self.list = async_to_raw_response_wrapper(
            similar.list,
        )


class SimilarResourceWithStreamingResponse:
    def __init__(self, similar: SimilarResource) -> None:
        self._similar = similar

        self.list = to_streamed_response_wrapper(
            similar.list,
        )


class AsyncSimilarResourceWithStreamingResponse:
    def __init__(self, similar: AsyncSimilarResource) -> None:
        self._similar = similar

        self.list = async_to_streamed_response_wrapper(
            similar.list,
        )
