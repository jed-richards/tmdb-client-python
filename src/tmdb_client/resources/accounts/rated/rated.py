# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...._compat import cached_property
from .tv_episodes import (
    TvEpisodesResource,
    AsyncTvEpisodesResource,
    TvEpisodesResourceWithRawResponse,
    AsyncTvEpisodesResourceWithRawResponse,
    TvEpisodesResourceWithStreamingResponse,
    AsyncTvEpisodesResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["RatedResource", "AsyncRatedResource"]


class RatedResource(SyncAPIResource):
    @cached_property
    def movies(self) -> MoviesResource:
        return MoviesResource(self._client)

    @cached_property
    def tv(self) -> TvResource:
        return TvResource(self._client)

    @cached_property
    def tv_episodes(self) -> TvEpisodesResource:
        return TvEpisodesResource(self._client)

    @cached_property
    def with_raw_response(self) -> RatedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return RatedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RatedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return RatedResourceWithStreamingResponse(self)


class AsyncRatedResource(AsyncAPIResource):
    @cached_property
    def movies(self) -> AsyncMoviesResource:
        return AsyncMoviesResource(self._client)

    @cached_property
    def tv(self) -> AsyncTvResource:
        return AsyncTvResource(self._client)

    @cached_property
    def tv_episodes(self) -> AsyncTvEpisodesResource:
        return AsyncTvEpisodesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRatedResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRatedResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRatedResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncRatedResourceWithStreamingResponse(self)


class RatedResourceWithRawResponse:
    def __init__(self, rated: RatedResource) -> None:
        self._rated = rated

    @cached_property
    def movies(self) -> MoviesResourceWithRawResponse:
        return MoviesResourceWithRawResponse(self._rated.movies)

    @cached_property
    def tv(self) -> TvResourceWithRawResponse:
        return TvResourceWithRawResponse(self._rated.tv)

    @cached_property
    def tv_episodes(self) -> TvEpisodesResourceWithRawResponse:
        return TvEpisodesResourceWithRawResponse(self._rated.tv_episodes)


class AsyncRatedResourceWithRawResponse:
    def __init__(self, rated: AsyncRatedResource) -> None:
        self._rated = rated

    @cached_property
    def movies(self) -> AsyncMoviesResourceWithRawResponse:
        return AsyncMoviesResourceWithRawResponse(self._rated.movies)

    @cached_property
    def tv(self) -> AsyncTvResourceWithRawResponse:
        return AsyncTvResourceWithRawResponse(self._rated.tv)

    @cached_property
    def tv_episodes(self) -> AsyncTvEpisodesResourceWithRawResponse:
        return AsyncTvEpisodesResourceWithRawResponse(self._rated.tv_episodes)


class RatedResourceWithStreamingResponse:
    def __init__(self, rated: RatedResource) -> None:
        self._rated = rated

    @cached_property
    def movies(self) -> MoviesResourceWithStreamingResponse:
        return MoviesResourceWithStreamingResponse(self._rated.movies)

    @cached_property
    def tv(self) -> TvResourceWithStreamingResponse:
        return TvResourceWithStreamingResponse(self._rated.tv)

    @cached_property
    def tv_episodes(self) -> TvEpisodesResourceWithStreamingResponse:
        return TvEpisodesResourceWithStreamingResponse(self._rated.tv_episodes)


class AsyncRatedResourceWithStreamingResponse:
    def __init__(self, rated: AsyncRatedResource) -> None:
        self._rated = rated

    @cached_property
    def movies(self) -> AsyncMoviesResourceWithStreamingResponse:
        return AsyncMoviesResourceWithStreamingResponse(self._rated.movies)

    @cached_property
    def tv(self) -> AsyncTvResourceWithStreamingResponse:
        return AsyncTvResourceWithStreamingResponse(self._rated.tv)

    @cached_property
    def tv_episodes(self) -> AsyncTvEpisodesResourceWithStreamingResponse:
        return AsyncTvEpisodesResourceWithStreamingResponse(self._rated.tv_episodes)
