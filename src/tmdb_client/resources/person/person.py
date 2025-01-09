# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .latest import (
    LatestResource,
    AsyncLatestResource,
    LatestResourceWithRawResponse,
    AsyncLatestResourceWithRawResponse,
    LatestResourceWithStreamingResponse,
    AsyncLatestResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["PersonResource", "AsyncPersonResource"]


class PersonResource(SyncAPIResource):
    @cached_property
    def latest(self) -> LatestResource:
        return LatestResource(self._client)

    @cached_property
    def with_raw_response(self) -> PersonResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return PersonResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PersonResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return PersonResourceWithStreamingResponse(self)


class AsyncPersonResource(AsyncAPIResource):
    @cached_property
    def latest(self) -> AsyncLatestResource:
        return AsyncLatestResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPersonResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPersonResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPersonResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncPersonResourceWithStreamingResponse(self)


class PersonResourceWithRawResponse:
    def __init__(self, person: PersonResource) -> None:
        self._person = person

    @cached_property
    def latest(self) -> LatestResourceWithRawResponse:
        return LatestResourceWithRawResponse(self._person.latest)


class AsyncPersonResourceWithRawResponse:
    def __init__(self, person: AsyncPersonResource) -> None:
        self._person = person

    @cached_property
    def latest(self) -> AsyncLatestResourceWithRawResponse:
        return AsyncLatestResourceWithRawResponse(self._person.latest)


class PersonResourceWithStreamingResponse:
    def __init__(self, person: PersonResource) -> None:
        self._person = person

    @cached_property
    def latest(self) -> LatestResourceWithStreamingResponse:
        return LatestResourceWithStreamingResponse(self._person.latest)


class AsyncPersonResourceWithStreamingResponse:
    def __init__(self, person: AsyncPersonResource) -> None:
        self._person = person

    @cached_property
    def latest(self) -> AsyncLatestResourceWithStreamingResponse:
        return AsyncLatestResourceWithStreamingResponse(self._person.latest)
