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
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["GenresResource", "AsyncGenresResource"]


class GenresResource(SyncAPIResource):
    @cached_property
    def movies(self) -> MoviesResource:
        return MoviesResource(self._client)

    @cached_property
    def tv(self) -> TvResource:
        return TvResource(self._client)

    @cached_property
    def with_raw_response(self) -> GenresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return GenresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return GenresResourceWithStreamingResponse(self)


class AsyncGenresResource(AsyncAPIResource):
    @cached_property
    def movies(self) -> AsyncMoviesResource:
        return AsyncMoviesResource(self._client)

    @cached_property
    def tv(self) -> AsyncTvResource:
        return AsyncTvResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGenresResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGenresResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenresResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncGenresResourceWithStreamingResponse(self)


class GenresResourceWithRawResponse:
    def __init__(self, genres: GenresResource) -> None:
        self._genres = genres

    @cached_property
    def movies(self) -> MoviesResourceWithRawResponse:
        return MoviesResourceWithRawResponse(self._genres.movies)

    @cached_property
    def tv(self) -> TvResourceWithRawResponse:
        return TvResourceWithRawResponse(self._genres.tv)


class AsyncGenresResourceWithRawResponse:
    def __init__(self, genres: AsyncGenresResource) -> None:
        self._genres = genres

    @cached_property
    def movies(self) -> AsyncMoviesResourceWithRawResponse:
        return AsyncMoviesResourceWithRawResponse(self._genres.movies)

    @cached_property
    def tv(self) -> AsyncTvResourceWithRawResponse:
        return AsyncTvResourceWithRawResponse(self._genres.tv)


class GenresResourceWithStreamingResponse:
    def __init__(self, genres: GenresResource) -> None:
        self._genres = genres

    @cached_property
    def movies(self) -> MoviesResourceWithStreamingResponse:
        return MoviesResourceWithStreamingResponse(self._genres.movies)

    @cached_property
    def tv(self) -> TvResourceWithStreamingResponse:
        return TvResourceWithStreamingResponse(self._genres.tv)


class AsyncGenresResourceWithStreamingResponse:
    def __init__(self, genres: AsyncGenresResource) -> None:
        self._genres = genres

    @cached_property
    def movies(self) -> AsyncMoviesResourceWithStreamingResponse:
        return AsyncMoviesResourceWithStreamingResponse(self._genres.movies)

    @cached_property
    def tv(self) -> AsyncTvResourceWithStreamingResponse:
        return AsyncTvResourceWithStreamingResponse(self._genres.tv)
