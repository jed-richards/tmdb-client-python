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
from ...types.movies import recommendation_retrieve_params

__all__ = ["RecommendationsResource", "AsyncRecommendationsResource"]


class RecommendationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RecommendationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return RecommendationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecommendationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return RecommendationsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        movie_id: int,
        *,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Recommendations

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/3/movie/{movie_id}/recommendations",
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
                    recommendation_retrieve_params.RecommendationRetrieveParams,
                ),
            ),
            cast_to=object,
        )


class AsyncRecommendationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRecommendationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRecommendationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecommendationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return AsyncRecommendationsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        movie_id: int,
        *,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Recommendations

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/3/movie/{movie_id}/recommendations",
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
                    recommendation_retrieve_params.RecommendationRetrieveParams,
                ),
            ),
            cast_to=object,
        )


class RecommendationsResourceWithRawResponse:
    def __init__(self, recommendations: RecommendationsResource) -> None:
        self._recommendations = recommendations

        self.retrieve = to_raw_response_wrapper(
            recommendations.retrieve,
        )


class AsyncRecommendationsResourceWithRawResponse:
    def __init__(self, recommendations: AsyncRecommendationsResource) -> None:
        self._recommendations = recommendations

        self.retrieve = async_to_raw_response_wrapper(
            recommendations.retrieve,
        )


class RecommendationsResourceWithStreamingResponse:
    def __init__(self, recommendations: RecommendationsResource) -> None:
        self._recommendations = recommendations

        self.retrieve = to_streamed_response_wrapper(
            recommendations.retrieve,
        )


class AsyncRecommendationsResourceWithStreamingResponse:
    def __init__(self, recommendations: AsyncRecommendationsResource) -> None:
        self._recommendations = recommendations

        self.retrieve = async_to_streamed_response_wrapper(
            recommendations.retrieve,
        )
