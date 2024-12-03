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
from ...types.tv_shows.episode_group_retrieve_response import EpisodeGroupRetrieveResponse

__all__ = ["EpisodeGroupsResource", "AsyncEpisodeGroupsResource"]


class EpisodeGroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EpisodeGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return EpisodeGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EpisodeGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return EpisodeGroupsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        series_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EpisodeGroupRetrieveResponse:
        """
        Get the episode groups that have been added to a TV show.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/3/tv/{series_id}/episode_groups",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EpisodeGroupRetrieveResponse,
        )


class AsyncEpisodeGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEpisodeGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEpisodeGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEpisodeGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return AsyncEpisodeGroupsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        series_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EpisodeGroupRetrieveResponse:
        """
        Get the episode groups that have been added to a TV show.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/3/tv/{series_id}/episode_groups",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EpisodeGroupRetrieveResponse,
        )


class EpisodeGroupsResourceWithRawResponse:
    def __init__(self, episode_groups: EpisodeGroupsResource) -> None:
        self._episode_groups = episode_groups

        self.retrieve = to_raw_response_wrapper(
            episode_groups.retrieve,
        )


class AsyncEpisodeGroupsResourceWithRawResponse:
    def __init__(self, episode_groups: AsyncEpisodeGroupsResource) -> None:
        self._episode_groups = episode_groups

        self.retrieve = async_to_raw_response_wrapper(
            episode_groups.retrieve,
        )


class EpisodeGroupsResourceWithStreamingResponse:
    def __init__(self, episode_groups: EpisodeGroupsResource) -> None:
        self._episode_groups = episode_groups

        self.retrieve = to_streamed_response_wrapper(
            episode_groups.retrieve,
        )


class AsyncEpisodeGroupsResourceWithStreamingResponse:
    def __init__(self, episode_groups: AsyncEpisodeGroupsResource) -> None:
        self._episode_groups = episode_groups

        self.retrieve = async_to_streamed_response_wrapper(
            episode_groups.retrieve,
        )
