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
from ...types.people import movie_credit_list_params
from ...types.people.movie_credit_list_response import MovieCreditListResponse

__all__ = ["MovieCreditsResource", "AsyncMovieCreditsResource"]


class MovieCreditsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MovieCreditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return MovieCreditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MovieCreditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return MovieCreditsResourceWithStreamingResponse(self)

    def list(
        self,
        person_id: int,
        *,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MovieCreditListResponse:
        """
        Get the movie credits for a person.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/3/person/{person_id}/movie_credits",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"language": language}, movie_credit_list_params.MovieCreditListParams),
            ),
            cast_to=MovieCreditListResponse,
        )


class AsyncMovieCreditsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMovieCreditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMovieCreditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMovieCreditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncMovieCreditsResourceWithStreamingResponse(self)

    async def list(
        self,
        person_id: int,
        *,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MovieCreditListResponse:
        """
        Get the movie credits for a person.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/3/person/{person_id}/movie_credits",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"language": language}, movie_credit_list_params.MovieCreditListParams
                ),
            ),
            cast_to=MovieCreditListResponse,
        )


class MovieCreditsResourceWithRawResponse:
    def __init__(self, movie_credits: MovieCreditsResource) -> None:
        self._movie_credits = movie_credits

        self.list = to_raw_response_wrapper(
            movie_credits.list,
        )


class AsyncMovieCreditsResourceWithRawResponse:
    def __init__(self, movie_credits: AsyncMovieCreditsResource) -> None:
        self._movie_credits = movie_credits

        self.list = async_to_raw_response_wrapper(
            movie_credits.list,
        )


class MovieCreditsResourceWithStreamingResponse:
    def __init__(self, movie_credits: MovieCreditsResource) -> None:
        self._movie_credits = movie_credits

        self.list = to_streamed_response_wrapper(
            movie_credits.list,
        )


class AsyncMovieCreditsResourceWithStreamingResponse:
    def __init__(self, movie_credits: AsyncMovieCreditsResource) -> None:
        self._movie_credits = movie_credits

        self.list = async_to_streamed_response_wrapper(
            movie_credits.list,
        )
