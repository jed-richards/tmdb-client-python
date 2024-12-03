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
from ...types.collections import image_list_params
from ...types.collections.image_list_response import ImageListResponse

__all__ = ["ImagesResource", "AsyncImagesResource"]


class ImagesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ImagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return ImagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return ImagesResourceWithStreamingResponse(self)

    def list(
        self,
        collection_id: int,
        *,
        include_image_language: str | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImageListResponse:
        """
        Get the images that belong to a collection.

        Args:
          include_image_language:
              specify a comma separated list of ISO-639-1 values to query, for example:
              `en,null`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/3/collection/{collection_id}/images",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_image_language": include_image_language,
                        "language": language,
                    },
                    image_list_params.ImageListParams,
                ),
            ),
            cast_to=ImageListResponse,
        )


class AsyncImagesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncImagesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncImagesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImagesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return AsyncImagesResourceWithStreamingResponse(self)

    async def list(
        self,
        collection_id: int,
        *,
        include_image_language: str | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ImageListResponse:
        """
        Get the images that belong to a collection.

        Args:
          include_image_language:
              specify a comma separated list of ISO-639-1 values to query, for example:
              `en,null`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/3/collection/{collection_id}/images",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_image_language": include_image_language,
                        "language": language,
                    },
                    image_list_params.ImageListParams,
                ),
            ),
            cast_to=ImageListResponse,
        )


class ImagesResourceWithRawResponse:
    def __init__(self, images: ImagesResource) -> None:
        self._images = images

        self.list = to_raw_response_wrapper(
            images.list,
        )


class AsyncImagesResourceWithRawResponse:
    def __init__(self, images: AsyncImagesResource) -> None:
        self._images = images

        self.list = async_to_raw_response_wrapper(
            images.list,
        )


class ImagesResourceWithStreamingResponse:
    def __init__(self, images: ImagesResource) -> None:
        self._images = images

        self.list = to_streamed_response_wrapper(
            images.list,
        )


class AsyncImagesResourceWithStreamingResponse:
    def __init__(self, images: AsyncImagesResource) -> None:
        self._images = images

        self.list = async_to_streamed_response_wrapper(
            images.list,
        )
