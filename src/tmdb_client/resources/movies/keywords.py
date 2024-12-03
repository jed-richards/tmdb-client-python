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
from ...types.movies.keyword_retrieve_response import KeywordRetrieveResponse

__all__ = ["KeywordsResource", "AsyncKeywordsResource"]


class KeywordsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KeywordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return KeywordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KeywordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return KeywordsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        movie_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeywordRetrieveResponse:
        """
        Keywords

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not movie_id:
            raise ValueError(f"Expected a non-empty value for `movie_id` but received {movie_id!r}")
        return self._get(
            f"/3/movie/{movie_id}/keywords",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeywordRetrieveResponse,
        )


class AsyncKeywordsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKeywordsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKeywordsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKeywordsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncKeywordsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        movie_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> KeywordRetrieveResponse:
        """
        Keywords

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not movie_id:
            raise ValueError(f"Expected a non-empty value for `movie_id` but received {movie_id!r}")
        return await self._get(
            f"/3/movie/{movie_id}/keywords",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KeywordRetrieveResponse,
        )


class KeywordsResourceWithRawResponse:
    def __init__(self, keywords: KeywordsResource) -> None:
        self._keywords = keywords

        self.retrieve = to_raw_response_wrapper(
            keywords.retrieve,
        )


class AsyncKeywordsResourceWithRawResponse:
    def __init__(self, keywords: AsyncKeywordsResource) -> None:
        self._keywords = keywords

        self.retrieve = async_to_raw_response_wrapper(
            keywords.retrieve,
        )


class KeywordsResourceWithStreamingResponse:
    def __init__(self, keywords: KeywordsResource) -> None:
        self._keywords = keywords

        self.retrieve = to_streamed_response_wrapper(
            keywords.retrieve,
        )


class AsyncKeywordsResourceWithStreamingResponse:
    def __init__(self, keywords: AsyncKeywordsResource) -> None:
        self._keywords = keywords

        self.retrieve = async_to_streamed_response_wrapper(
            keywords.retrieve,
        )
