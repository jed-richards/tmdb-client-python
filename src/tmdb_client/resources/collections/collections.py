# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .images import (
    ImagesResource,
    AsyncImagesResource,
    ImagesResourceWithRawResponse,
    AsyncImagesResourceWithRawResponse,
    ImagesResourceWithStreamingResponse,
    AsyncImagesResourceWithStreamingResponse,
)
from ...types import collection_retrieve_params
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
from .translations import (
    TranslationsResource,
    AsyncTranslationsResource,
    TranslationsResourceWithRawResponse,
    AsyncTranslationsResourceWithRawResponse,
    TranslationsResourceWithStreamingResponse,
    AsyncTranslationsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.collection_retrieve_response import CollectionRetrieveResponse

__all__ = ["CollectionsResource", "AsyncCollectionsResource"]


class CollectionsResource(SyncAPIResource):
    @cached_property
    def images(self) -> ImagesResource:
        return ImagesResource(self._client)

    @cached_property
    def translations(self) -> TranslationsResource:
        return TranslationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CollectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return CollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CollectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return CollectionsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        collection_id: int,
        *,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionRetrieveResponse:
        """
        Get collection details by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/3/collection/{collection_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"language": language}, collection_retrieve_params.CollectionRetrieveParams),
            ),
            cast_to=CollectionRetrieveResponse,
        )


class AsyncCollectionsResource(AsyncAPIResource):
    @cached_property
    def images(self) -> AsyncImagesResource:
        return AsyncImagesResource(self._client)

    @cached_property
    def translations(self) -> AsyncTranslationsResource:
        return AsyncTranslationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCollectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCollectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return AsyncCollectionsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        collection_id: int,
        *,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionRetrieveResponse:
        """
        Get collection details by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/3/collection/{collection_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"language": language}, collection_retrieve_params.CollectionRetrieveParams
                ),
            ),
            cast_to=CollectionRetrieveResponse,
        )


class CollectionsResourceWithRawResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.retrieve = to_raw_response_wrapper(
            collections.retrieve,
        )

    @cached_property
    def images(self) -> ImagesResourceWithRawResponse:
        return ImagesResourceWithRawResponse(self._collections.images)

    @cached_property
    def translations(self) -> TranslationsResourceWithRawResponse:
        return TranslationsResourceWithRawResponse(self._collections.translations)


class AsyncCollectionsResourceWithRawResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.retrieve = async_to_raw_response_wrapper(
            collections.retrieve,
        )

    @cached_property
    def images(self) -> AsyncImagesResourceWithRawResponse:
        return AsyncImagesResourceWithRawResponse(self._collections.images)

    @cached_property
    def translations(self) -> AsyncTranslationsResourceWithRawResponse:
        return AsyncTranslationsResourceWithRawResponse(self._collections.translations)


class CollectionsResourceWithStreamingResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.retrieve = to_streamed_response_wrapper(
            collections.retrieve,
        )

    @cached_property
    def images(self) -> ImagesResourceWithStreamingResponse:
        return ImagesResourceWithStreamingResponse(self._collections.images)

    @cached_property
    def translations(self) -> TranslationsResourceWithStreamingResponse:
        return TranslationsResourceWithStreamingResponse(self._collections.translations)


class AsyncCollectionsResourceWithStreamingResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.retrieve = async_to_streamed_response_wrapper(
            collections.retrieve,
        )

    @cached_property
    def images(self) -> AsyncImagesResourceWithStreamingResponse:
        return AsyncImagesResourceWithStreamingResponse(self._collections.images)

    @cached_property
    def translations(self) -> AsyncTranslationsResourceWithStreamingResponse:
        return AsyncTranslationsResourceWithStreamingResponse(self._collections.translations)
