# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .movies import (
    MoviesResource,
    AsyncMoviesResource,
    MoviesResourceWithRawResponse,
    AsyncMoviesResourceWithRawResponse,
    MoviesResourceWithStreamingResponse,
    AsyncMoviesResourceWithStreamingResponse,
)
from .regions import (
    RegionsResource,
    AsyncRegionsResource,
    RegionsResourceWithRawResponse,
    AsyncRegionsResourceWithRawResponse,
    RegionsResourceWithStreamingResponse,
    AsyncRegionsResourceWithStreamingResponse,
)
from .tv_shows import (
    TvShowsResource,
    AsyncTvShowsResource,
    TvShowsResourceWithRawResponse,
    AsyncTvShowsResourceWithRawResponse,
    TvShowsResourceWithStreamingResponse,
    AsyncTvShowsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["WatchProvidersResource", "AsyncWatchProvidersResource"]


class WatchProvidersResource(SyncAPIResource):
    @cached_property
    def regions(self) -> RegionsResource:
        return RegionsResource(self._client)

    @cached_property
    def movies(self) -> MoviesResource:
        return MoviesResource(self._client)

    @cached_property
    def tv_shows(self) -> TvShowsResource:
        return TvShowsResource(self._client)

    @cached_property
    def with_raw_response(self) -> WatchProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return WatchProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WatchProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return WatchProvidersResourceWithStreamingResponse(self)


class AsyncWatchProvidersResource(AsyncAPIResource):
    @cached_property
    def regions(self) -> AsyncRegionsResource:
        return AsyncRegionsResource(self._client)

    @cached_property
    def movies(self) -> AsyncMoviesResource:
        return AsyncMoviesResource(self._client)

    @cached_property
    def tv_shows(self) -> AsyncTvShowsResource:
        return AsyncTvShowsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWatchProvidersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncWatchProvidersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWatchProvidersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncWatchProvidersResourceWithStreamingResponse(self)


class WatchProvidersResourceWithRawResponse:
    def __init__(self, watch_providers: WatchProvidersResource) -> None:
        self._watch_providers = watch_providers

    @cached_property
    def regions(self) -> RegionsResourceWithRawResponse:
        return RegionsResourceWithRawResponse(self._watch_providers.regions)

    @cached_property
    def movies(self) -> MoviesResourceWithRawResponse:
        return MoviesResourceWithRawResponse(self._watch_providers.movies)

    @cached_property
    def tv_shows(self) -> TvShowsResourceWithRawResponse:
        return TvShowsResourceWithRawResponse(self._watch_providers.tv_shows)


class AsyncWatchProvidersResourceWithRawResponse:
    def __init__(self, watch_providers: AsyncWatchProvidersResource) -> None:
        self._watch_providers = watch_providers

    @cached_property
    def regions(self) -> AsyncRegionsResourceWithRawResponse:
        return AsyncRegionsResourceWithRawResponse(self._watch_providers.regions)

    @cached_property
    def movies(self) -> AsyncMoviesResourceWithRawResponse:
        return AsyncMoviesResourceWithRawResponse(self._watch_providers.movies)

    @cached_property
    def tv_shows(self) -> AsyncTvShowsResourceWithRawResponse:
        return AsyncTvShowsResourceWithRawResponse(self._watch_providers.tv_shows)


class WatchProvidersResourceWithStreamingResponse:
    def __init__(self, watch_providers: WatchProvidersResource) -> None:
        self._watch_providers = watch_providers

    @cached_property
    def regions(self) -> RegionsResourceWithStreamingResponse:
        return RegionsResourceWithStreamingResponse(self._watch_providers.regions)

    @cached_property
    def movies(self) -> MoviesResourceWithStreamingResponse:
        return MoviesResourceWithStreamingResponse(self._watch_providers.movies)

    @cached_property
    def tv_shows(self) -> TvShowsResourceWithStreamingResponse:
        return TvShowsResourceWithStreamingResponse(self._watch_providers.tv_shows)


class AsyncWatchProvidersResourceWithStreamingResponse:
    def __init__(self, watch_providers: AsyncWatchProvidersResource) -> None:
        self._watch_providers = watch_providers

    @cached_property
    def regions(self) -> AsyncRegionsResourceWithStreamingResponse:
        return AsyncRegionsResourceWithStreamingResponse(self._watch_providers.regions)

    @cached_property
    def movies(self) -> AsyncMoviesResourceWithStreamingResponse:
        return AsyncMoviesResourceWithStreamingResponse(self._watch_providers.movies)

    @cached_property
    def tv_shows(self) -> AsyncTvShowsResourceWithStreamingResponse:
        return AsyncTvShowsResourceWithStreamingResponse(self._watch_providers.tv_shows)
