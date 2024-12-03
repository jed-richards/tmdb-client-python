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
from ...types.configuration.language_list_response import LanguageListResponse

__all__ = ["LanguagesResource", "AsyncLanguagesResource"]


class LanguagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LanguagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return LanguagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LanguagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return LanguagesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LanguageListResponse:
        """Get the list of languages (ISO 639-1 tags) used throughout TMDB."""
        return self._get(
            "/3/configuration/languages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LanguageListResponse,
        )


class AsyncLanguagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLanguagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLanguagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLanguagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return AsyncLanguagesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LanguageListResponse:
        """Get the list of languages (ISO 639-1 tags) used throughout TMDB."""
        return await self._get(
            "/3/configuration/languages",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LanguageListResponse,
        )


class LanguagesResourceWithRawResponse:
    def __init__(self, languages: LanguagesResource) -> None:
        self._languages = languages

        self.list = to_raw_response_wrapper(
            languages.list,
        )


class AsyncLanguagesResourceWithRawResponse:
    def __init__(self, languages: AsyncLanguagesResource) -> None:
        self._languages = languages

        self.list = async_to_raw_response_wrapper(
            languages.list,
        )


class LanguagesResourceWithStreamingResponse:
    def __init__(self, languages: LanguagesResource) -> None:
        self._languages = languages

        self.list = to_streamed_response_wrapper(
            languages.list,
        )


class AsyncLanguagesResourceWithStreamingResponse:
    def __init__(self, languages: AsyncLanguagesResource) -> None:
        self._languages = languages

        self.list = async_to_streamed_response_wrapper(
            languages.list,
        )
