# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .rated import (
    RatedResource,
    AsyncRatedResource,
    RatedResourceWithRawResponse,
    AsyncRatedResourceWithRawResponse,
    RatedResourceWithStreamingResponse,
    AsyncRatedResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .rated.rated import RatedResource, AsyncRatedResource
from .tv_episodes import (
    TvEpisodesResource,
    AsyncTvEpisodesResource,
    TvEpisodesResourceWithRawResponse,
    AsyncTvEpisodesResourceWithRawResponse,
    TvEpisodesResourceWithStreamingResponse,
    AsyncTvEpisodesResourceWithStreamingResponse,
)

__all__ = ["GuestSessionsResource", "AsyncGuestSessionsResource"]


class GuestSessionsResource(SyncAPIResource):
    @cached_property
    def rated(self) -> RatedResource:
        return RatedResource(self._client)

    @cached_property
    def tv_episodes(self) -> TvEpisodesResource:
        return TvEpisodesResource(self._client)

    @cached_property
    def with_raw_response(self) -> GuestSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return GuestSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GuestSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return GuestSessionsResourceWithStreamingResponse(self)


class AsyncGuestSessionsResource(AsyncAPIResource):
    @cached_property
    def rated(self) -> AsyncRatedResource:
        return AsyncRatedResource(self._client)

    @cached_property
    def tv_episodes(self) -> AsyncTvEpisodesResource:
        return AsyncTvEpisodesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGuestSessionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGuestSessionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGuestSessionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncGuestSessionsResourceWithStreamingResponse(self)


class GuestSessionsResourceWithRawResponse:
    def __init__(self, guest_sessions: GuestSessionsResource) -> None:
        self._guest_sessions = guest_sessions

    @cached_property
    def rated(self) -> RatedResourceWithRawResponse:
        return RatedResourceWithRawResponse(self._guest_sessions.rated)

    @cached_property
    def tv_episodes(self) -> TvEpisodesResourceWithRawResponse:
        return TvEpisodesResourceWithRawResponse(self._guest_sessions.tv_episodes)


class AsyncGuestSessionsResourceWithRawResponse:
    def __init__(self, guest_sessions: AsyncGuestSessionsResource) -> None:
        self._guest_sessions = guest_sessions

    @cached_property
    def rated(self) -> AsyncRatedResourceWithRawResponse:
        return AsyncRatedResourceWithRawResponse(self._guest_sessions.rated)

    @cached_property
    def tv_episodes(self) -> AsyncTvEpisodesResourceWithRawResponse:
        return AsyncTvEpisodesResourceWithRawResponse(self._guest_sessions.tv_episodes)


class GuestSessionsResourceWithStreamingResponse:
    def __init__(self, guest_sessions: GuestSessionsResource) -> None:
        self._guest_sessions = guest_sessions

    @cached_property
    def rated(self) -> RatedResourceWithStreamingResponse:
        return RatedResourceWithStreamingResponse(self._guest_sessions.rated)

    @cached_property
    def tv_episodes(self) -> TvEpisodesResourceWithStreamingResponse:
        return TvEpisodesResourceWithStreamingResponse(self._guest_sessions.tv_episodes)


class AsyncGuestSessionsResourceWithStreamingResponse:
    def __init__(self, guest_sessions: AsyncGuestSessionsResource) -> None:
        self._guest_sessions = guest_sessions

    @cached_property
    def rated(self) -> AsyncRatedResourceWithStreamingResponse:
        return AsyncRatedResourceWithStreamingResponse(self._guest_sessions.rated)

    @cached_property
    def tv_episodes(self) -> AsyncTvEpisodesResourceWithStreamingResponse:
        return AsyncTvEpisodesResourceWithStreamingResponse(self._guest_sessions.tv_episodes)
