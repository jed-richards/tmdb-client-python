# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

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
from ....types.accounts.rated import tv_episode_list_params
from ....types.accounts.rated.tv_episode_list_response import TvEpisodeListResponse

__all__ = ["TvEpisodesResource", "AsyncTvEpisodesResource"]


class TvEpisodesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TvEpisodesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return TvEpisodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TvEpisodesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return TvEpisodesResourceWithStreamingResponse(self)

    def list(
        self,
        account_id: int,
        *,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        sort_by: Literal["created_at.asc", "created_at.desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TvEpisodeListResponse:
        """
        Rated TV Episodes

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/3/account/{account_id}/rated/tv/episodes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "language": language,
                        "page": page,
                        "session_id": session_id,
                        "sort_by": sort_by,
                    },
                    tv_episode_list_params.TvEpisodeListParams,
                ),
            ),
            cast_to=TvEpisodeListResponse,
        )


class AsyncTvEpisodesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTvEpisodesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTvEpisodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTvEpisodesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncTvEpisodesResourceWithStreamingResponse(self)

    async def list(
        self,
        account_id: int,
        *,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        sort_by: Literal["created_at.asc", "created_at.desc"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TvEpisodeListResponse:
        """
        Rated TV Episodes

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/3/account/{account_id}/rated/tv/episodes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "language": language,
                        "page": page,
                        "session_id": session_id,
                        "sort_by": sort_by,
                    },
                    tv_episode_list_params.TvEpisodeListParams,
                ),
            ),
            cast_to=TvEpisodeListResponse,
        )


class TvEpisodesResourceWithRawResponse:
    def __init__(self, tv_episodes: TvEpisodesResource) -> None:
        self._tv_episodes = tv_episodes

        self.list = to_raw_response_wrapper(
            tv_episodes.list,
        )


class AsyncTvEpisodesResourceWithRawResponse:
    def __init__(self, tv_episodes: AsyncTvEpisodesResource) -> None:
        self._tv_episodes = tv_episodes

        self.list = async_to_raw_response_wrapper(
            tv_episodes.list,
        )


class TvEpisodesResourceWithStreamingResponse:
    def __init__(self, tv_episodes: TvEpisodesResource) -> None:
        self._tv_episodes = tv_episodes

        self.list = to_streamed_response_wrapper(
            tv_episodes.list,
        )


class AsyncTvEpisodesResourceWithStreamingResponse:
    def __init__(self, tv_episodes: AsyncTvEpisodesResource) -> None:
        self._tv_episodes = tv_episodes

        self.list = async_to_streamed_response_wrapper(
            tv_episodes.list,
        )
