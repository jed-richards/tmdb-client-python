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
from ...types.configuration.primary_translation_list_response import PrimaryTranslationListResponse

__all__ = ["PrimaryTranslationsResource", "AsyncPrimaryTranslationsResource"]


class PrimaryTranslationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PrimaryTranslationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return PrimaryTranslationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrimaryTranslationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return PrimaryTranslationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PrimaryTranslationListResponse:
        """Get a list of the officially supported translations on TMDB."""
        return self._get(
            "/3/configuration/primary_translations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrimaryTranslationListResponse,
        )


class AsyncPrimaryTranslationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPrimaryTranslationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPrimaryTranslationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrimaryTranslationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncPrimaryTranslationsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PrimaryTranslationListResponse:
        """Get a list of the officially supported translations on TMDB."""
        return await self._get(
            "/3/configuration/primary_translations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PrimaryTranslationListResponse,
        )


class PrimaryTranslationsResourceWithRawResponse:
    def __init__(self, primary_translations: PrimaryTranslationsResource) -> None:
        self._primary_translations = primary_translations

        self.list = to_raw_response_wrapper(
            primary_translations.list,
        )


class AsyncPrimaryTranslationsResourceWithRawResponse:
    def __init__(self, primary_translations: AsyncPrimaryTranslationsResource) -> None:
        self._primary_translations = primary_translations

        self.list = async_to_raw_response_wrapper(
            primary_translations.list,
        )


class PrimaryTranslationsResourceWithStreamingResponse:
    def __init__(self, primary_translations: PrimaryTranslationsResource) -> None:
        self._primary_translations = primary_translations

        self.list = to_streamed_response_wrapper(
            primary_translations.list,
        )


class AsyncPrimaryTranslationsResourceWithStreamingResponse:
    def __init__(self, primary_translations: AsyncPrimaryTranslationsResource) -> None:
        self._primary_translations = primary_translations

        self.list = async_to_streamed_response_wrapper(
            primary_translations.list,
        )
