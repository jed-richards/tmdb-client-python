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
from .movie import (
    MovieResource,
    AsyncMovieResource,
    MovieResourceWithRawResponse,
    AsyncMovieResourceWithRawResponse,
    MovieResourceWithStreamingResponse,
    AsyncMovieResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["CertificationsResource", "AsyncCertificationsResource"]


class CertificationsResource(SyncAPIResource):
    @cached_property
    def movie(self) -> MovieResource:
        return MovieResource(self._client)

    @cached_property
    def tv(self) -> TvResource:
        return TvResource(self._client)

    @cached_property
    def with_raw_response(self) -> CertificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return CertificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CertificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return CertificationsResourceWithStreamingResponse(self)


class AsyncCertificationsResource(AsyncAPIResource):
    @cached_property
    def movie(self) -> AsyncMovieResource:
        return AsyncMovieResource(self._client)

    @cached_property
    def tv(self) -> AsyncTvResource:
        return AsyncTvResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCertificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCertificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCertificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return AsyncCertificationsResourceWithStreamingResponse(self)


class CertificationsResourceWithRawResponse:
    def __init__(self, certifications: CertificationsResource) -> None:
        self._certifications = certifications

    @cached_property
    def movie(self) -> MovieResourceWithRawResponse:
        return MovieResourceWithRawResponse(self._certifications.movie)

    @cached_property
    def tv(self) -> TvResourceWithRawResponse:
        return TvResourceWithRawResponse(self._certifications.tv)


class AsyncCertificationsResourceWithRawResponse:
    def __init__(self, certifications: AsyncCertificationsResource) -> None:
        self._certifications = certifications

    @cached_property
    def movie(self) -> AsyncMovieResourceWithRawResponse:
        return AsyncMovieResourceWithRawResponse(self._certifications.movie)

    @cached_property
    def tv(self) -> AsyncTvResourceWithRawResponse:
        return AsyncTvResourceWithRawResponse(self._certifications.tv)


class CertificationsResourceWithStreamingResponse:
    def __init__(self, certifications: CertificationsResource) -> None:
        self._certifications = certifications

    @cached_property
    def movie(self) -> MovieResourceWithStreamingResponse:
        return MovieResourceWithStreamingResponse(self._certifications.movie)

    @cached_property
    def tv(self) -> TvResourceWithStreamingResponse:
        return TvResourceWithStreamingResponse(self._certifications.tv)


class AsyncCertificationsResourceWithStreamingResponse:
    def __init__(self, certifications: AsyncCertificationsResource) -> None:
        self._certifications = certifications

    @cached_property
    def movie(self) -> AsyncMovieResourceWithStreamingResponse:
        return AsyncMovieResourceWithStreamingResponse(self._certifications.movie)

    @cached_property
    def tv(self) -> AsyncTvResourceWithStreamingResponse:
        return AsyncTvResourceWithStreamingResponse(self._certifications.tv)
