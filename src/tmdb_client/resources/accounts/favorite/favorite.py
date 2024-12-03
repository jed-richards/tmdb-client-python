# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .tv import (
    TvResource,
    AsyncTvResource,
    TvResourceWithRawResponse,
    AsyncTvResourceWithRawResponse,
    TvResourceWithStreamingResponse,
    AsyncTvResourceWithStreamingResponse,
)
from .movies import (
    MoviesResource,
    AsyncMoviesResource,
    MoviesResourceWithRawResponse,
    AsyncMoviesResourceWithRawResponse,
    MoviesResourceWithStreamingResponse,
    AsyncMoviesResourceWithStreamingResponse,
)
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
from ....types.accounts import favorite_create_params
from ....types.accounts.favorite_create_response import FavoriteCreateResponse

__all__ = ["FavoriteResource", "AsyncFavoriteResource"]


class FavoriteResource(SyncAPIResource):
    @cached_property
    def movies(self) -> MoviesResource:
        return MoviesResource(self._client)

    @cached_property
    def tv(self) -> TvResource:
        return TvResource(self._client)

    @cached_property
    def with_raw_response(self) -> FavoriteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return FavoriteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FavoriteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return FavoriteResourceWithStreamingResponse(self)

    def create(
        self,
        account_id: int,
        *,
        raw_body: str,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FavoriteCreateResponse:
        """
        Add Favorite

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/3/account/{account_id}/favorite",
            body=maybe_transform({"raw_body": raw_body}, favorite_create_params.FavoriteCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"session_id": session_id}, favorite_create_params.FavoriteCreateParams),
            ),
            cast_to=FavoriteCreateResponse,
        )


class AsyncFavoriteResource(AsyncAPIResource):
    @cached_property
    def movies(self) -> AsyncMoviesResource:
        return AsyncMoviesResource(self._client)

    @cached_property
    def tv(self) -> AsyncTvResource:
        return AsyncTvResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFavoriteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFavoriteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFavoriteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return AsyncFavoriteResourceWithStreamingResponse(self)

    async def create(
        self,
        account_id: int,
        *,
        raw_body: str,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FavoriteCreateResponse:
        """
        Add Favorite

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/3/account/{account_id}/favorite",
            body=await async_maybe_transform({"raw_body": raw_body}, favorite_create_params.FavoriteCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"session_id": session_id}, favorite_create_params.FavoriteCreateParams
                ),
            ),
            cast_to=FavoriteCreateResponse,
        )


class FavoriteResourceWithRawResponse:
    def __init__(self, favorite: FavoriteResource) -> None:
        self._favorite = favorite

        self.create = to_raw_response_wrapper(
            favorite.create,
        )

    @cached_property
    def movies(self) -> MoviesResourceWithRawResponse:
        return MoviesResourceWithRawResponse(self._favorite.movies)

    @cached_property
    def tv(self) -> TvResourceWithRawResponse:
        return TvResourceWithRawResponse(self._favorite.tv)


class AsyncFavoriteResourceWithRawResponse:
    def __init__(self, favorite: AsyncFavoriteResource) -> None:
        self._favorite = favorite

        self.create = async_to_raw_response_wrapper(
            favorite.create,
        )

    @cached_property
    def movies(self) -> AsyncMoviesResourceWithRawResponse:
        return AsyncMoviesResourceWithRawResponse(self._favorite.movies)

    @cached_property
    def tv(self) -> AsyncTvResourceWithRawResponse:
        return AsyncTvResourceWithRawResponse(self._favorite.tv)


class FavoriteResourceWithStreamingResponse:
    def __init__(self, favorite: FavoriteResource) -> None:
        self._favorite = favorite

        self.create = to_streamed_response_wrapper(
            favorite.create,
        )

    @cached_property
    def movies(self) -> MoviesResourceWithStreamingResponse:
        return MoviesResourceWithStreamingResponse(self._favorite.movies)

    @cached_property
    def tv(self) -> TvResourceWithStreamingResponse:
        return TvResourceWithStreamingResponse(self._favorite.tv)


class AsyncFavoriteResourceWithStreamingResponse:
    def __init__(self, favorite: AsyncFavoriteResource) -> None:
        self._favorite = favorite

        self.create = async_to_streamed_response_wrapper(
            favorite.create,
        )

    @cached_property
    def movies(self) -> AsyncMoviesResourceWithStreamingResponse:
        return AsyncMoviesResourceWithStreamingResponse(self._favorite.movies)

    @cached_property
    def tv(self) -> AsyncTvResourceWithStreamingResponse:
        return AsyncTvResourceWithStreamingResponse(self._favorite.tv)
