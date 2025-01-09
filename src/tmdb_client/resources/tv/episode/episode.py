# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .changes import (
    ChangesResource,
    AsyncChangesResource,
    ChangesResourceWithRawResponse,
    AsyncChangesResourceWithRawResponse,
    ChangesResourceWithStreamingResponse,
    AsyncChangesResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["EpisodeResource", "AsyncEpisodeResource"]


class EpisodeResource(SyncAPIResource):
    @cached_property
    def changes(self) -> ChangesResource:
        return ChangesResource(self._client)

    @cached_property
    def with_raw_response(self) -> EpisodeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return EpisodeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EpisodeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return EpisodeResourceWithStreamingResponse(self)


class AsyncEpisodeResource(AsyncAPIResource):
    @cached_property
    def changes(self) -> AsyncChangesResource:
        return AsyncChangesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEpisodeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEpisodeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEpisodeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncEpisodeResourceWithStreamingResponse(self)


class EpisodeResourceWithRawResponse:
    def __init__(self, episode: EpisodeResource) -> None:
        self._episode = episode

    @cached_property
    def changes(self) -> ChangesResourceWithRawResponse:
        return ChangesResourceWithRawResponse(self._episode.changes)


class AsyncEpisodeResourceWithRawResponse:
    def __init__(self, episode: AsyncEpisodeResource) -> None:
        self._episode = episode

    @cached_property
    def changes(self) -> AsyncChangesResourceWithRawResponse:
        return AsyncChangesResourceWithRawResponse(self._episode.changes)


class EpisodeResourceWithStreamingResponse:
    def __init__(self, episode: EpisodeResource) -> None:
        self._episode = episode

    @cached_property
    def changes(self) -> ChangesResourceWithStreamingResponse:
        return ChangesResourceWithStreamingResponse(self._episode.changes)


class AsyncEpisodeResourceWithStreamingResponse:
    def __init__(self, episode: AsyncEpisodeResource) -> None:
        self._episode = episode

    @cached_property
    def changes(self) -> AsyncChangesResourceWithStreamingResponse:
        return AsyncChangesResourceWithStreamingResponse(self._episode.changes)
