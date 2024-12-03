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
from ...types.tv.episode_group_retrieve_response import EpisodeGroupRetrieveResponse

__all__ = ["EpisodeGroupResource", "AsyncEpisodeGroupResource"]


class EpisodeGroupResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EpisodeGroupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return EpisodeGroupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EpisodeGroupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return EpisodeGroupResourceWithStreamingResponse(self)

    def retrieve(
        self,
        tv_episode_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EpisodeGroupRetrieveResponse:
        """
        Get the details of a TV episode group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tv_episode_group_id:
            raise ValueError(
                f"Expected a non-empty value for `tv_episode_group_id` but received {tv_episode_group_id!r}"
            )
        return self._get(
            f"/3/tv/episode_group/{tv_episode_group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EpisodeGroupRetrieveResponse,
        )


class AsyncEpisodeGroupResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEpisodeGroupResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEpisodeGroupResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEpisodeGroupResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return AsyncEpisodeGroupResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        tv_episode_group_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EpisodeGroupRetrieveResponse:
        """
        Get the details of a TV episode group.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tv_episode_group_id:
            raise ValueError(
                f"Expected a non-empty value for `tv_episode_group_id` but received {tv_episode_group_id!r}"
            )
        return await self._get(
            f"/3/tv/episode_group/{tv_episode_group_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EpisodeGroupRetrieveResponse,
        )


class EpisodeGroupResourceWithRawResponse:
    def __init__(self, episode_group: EpisodeGroupResource) -> None:
        self._episode_group = episode_group

        self.retrieve = to_raw_response_wrapper(
            episode_group.retrieve,
        )


class AsyncEpisodeGroupResourceWithRawResponse:
    def __init__(self, episode_group: AsyncEpisodeGroupResource) -> None:
        self._episode_group = episode_group

        self.retrieve = async_to_raw_response_wrapper(
            episode_group.retrieve,
        )


class EpisodeGroupResourceWithStreamingResponse:
    def __init__(self, episode_group: EpisodeGroupResource) -> None:
        self._episode_group = episode_group

        self.retrieve = to_streamed_response_wrapper(
            episode_group.retrieve,
        )


class AsyncEpisodeGroupResourceWithStreamingResponse:
    def __init__(self, episode_group: AsyncEpisodeGroupResource) -> None:
        self._episode_group = episode_group

        self.retrieve = async_to_streamed_response_wrapper(
            episode_group.retrieve,
        )
