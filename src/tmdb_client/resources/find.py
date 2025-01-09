# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import find_retrieve_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.find_retrieve_response import FindRetrieveResponse

__all__ = ["FindResource", "AsyncFindResource"]


class FindResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FindResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return FindResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FindResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return FindResourceWithStreamingResponse(self)

    def retrieve(
        self,
        external_id: str,
        *,
        external_source: Literal[
            "",
            "imdb_id",
            "facebook_id",
            "instagram_id",
            "tvdb_id",
            "tiktok_id",
            "twitter_id",
            "wikidata_id",
            "youtube_id",
        ],
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FindRetrieveResponse:
        """
        Find data by external ID's.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_id:
            raise ValueError(f"Expected a non-empty value for `external_id` but received {external_id!r}")
        return self._get(
            f"/3/find/{external_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "external_source": external_source,
                        "language": language,
                    },
                    find_retrieve_params.FindRetrieveParams,
                ),
            ),
            cast_to=FindRetrieveResponse,
        )


class AsyncFindResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFindResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFindResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFindResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncFindResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        external_id: str,
        *,
        external_source: Literal[
            "",
            "imdb_id",
            "facebook_id",
            "instagram_id",
            "tvdb_id",
            "tiktok_id",
            "twitter_id",
            "wikidata_id",
            "youtube_id",
        ],
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FindRetrieveResponse:
        """
        Find data by external ID's.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not external_id:
            raise ValueError(f"Expected a non-empty value for `external_id` but received {external_id!r}")
        return await self._get(
            f"/3/find/{external_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "external_source": external_source,
                        "language": language,
                    },
                    find_retrieve_params.FindRetrieveParams,
                ),
            ),
            cast_to=FindRetrieveResponse,
        )


class FindResourceWithRawResponse:
    def __init__(self, find: FindResource) -> None:
        self._find = find

        self.retrieve = to_raw_response_wrapper(
            find.retrieve,
        )


class AsyncFindResourceWithRawResponse:
    def __init__(self, find: AsyncFindResource) -> None:
        self._find = find

        self.retrieve = async_to_raw_response_wrapper(
            find.retrieve,
        )


class FindResourceWithStreamingResponse:
    def __init__(self, find: FindResource) -> None:
        self._find = find

        self.retrieve = to_streamed_response_wrapper(
            find.retrieve,
        )


class AsyncFindResourceWithStreamingResponse:
    def __init__(self, find: AsyncFindResource) -> None:
        self._find = find

        self.retrieve = async_to_streamed_response_wrapper(
            find.retrieve,
        )
