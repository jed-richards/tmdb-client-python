# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .images import (
    ImagesResource,
    AsyncImagesResource,
    ImagesResourceWithRawResponse,
    AsyncImagesResourceWithRawResponse,
    ImagesResourceWithStreamingResponse,
    AsyncImagesResourceWithStreamingResponse,
)
from .credits import (
    CreditsResource,
    AsyncCreditsResource,
    CreditsResourceWithRawResponse,
    AsyncCreditsResourceWithRawResponse,
    CreditsResourceWithStreamingResponse,
    AsyncCreditsResourceWithStreamingResponse,
)
from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ....._compat import cached_property
from .external_ids import (
    ExternalIDsResource,
    AsyncExternalIDsResource,
    ExternalIDsResourceWithRawResponse,
    AsyncExternalIDsResourceWithRawResponse,
    ExternalIDsResourceWithStreamingResponse,
    AsyncExternalIDsResourceWithStreamingResponse,
)
from .translations import (
    TranslationsResource,
    AsyncTranslationsResource,
    TranslationsResourceWithRawResponse,
    AsyncTranslationsResourceWithRawResponse,
    TranslationsResourceWithStreamingResponse,
    AsyncTranslationsResourceWithStreamingResponse,
)
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.tv.seasons import episode_retrieve_params
from .....types.tv.seasons.episode_retrieve_response import EpisodeRetrieveResponse

__all__ = ["EpisodesResource", "AsyncEpisodesResource"]


class EpisodesResource(SyncAPIResource):
    @cached_property
    def images(self) -> ImagesResource:
        return ImagesResource(self._client)

    @cached_property
    def credits(self) -> CreditsResource:
        return CreditsResource(self._client)

    @cached_property
    def external_ids(self) -> ExternalIDsResource:
        return ExternalIDsResource(self._client)

    @cached_property
    def translations(self) -> TranslationsResource:
        return TranslationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> EpisodesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return EpisodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EpisodesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return EpisodesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        episode_number: int,
        *,
        series_id: int,
        season_number: int,
        append_to_response: str | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EpisodeRetrieveResponse:
        """
        Query the details of a TV episode.

        Args:
          append_to_response: comma separated list of endpoints within this namespace, 20 items max

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/3/tv/{series_id}/season/{season_number}/episode/{episode_number}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "append_to_response": append_to_response,
                        "language": language,
                    },
                    episode_retrieve_params.EpisodeRetrieveParams,
                ),
            ),
            cast_to=EpisodeRetrieveResponse,
        )


class AsyncEpisodesResource(AsyncAPIResource):
    @cached_property
    def images(self) -> AsyncImagesResource:
        return AsyncImagesResource(self._client)

    @cached_property
    def credits(self) -> AsyncCreditsResource:
        return AsyncCreditsResource(self._client)

    @cached_property
    def external_ids(self) -> AsyncExternalIDsResource:
        return AsyncExternalIDsResource(self._client)

    @cached_property
    def translations(self) -> AsyncTranslationsResource:
        return AsyncTranslationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEpisodesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEpisodesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEpisodesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncEpisodesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        episode_number: int,
        *,
        series_id: int,
        season_number: int,
        append_to_response: str | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EpisodeRetrieveResponse:
        """
        Query the details of a TV episode.

        Args:
          append_to_response: comma separated list of endpoints within this namespace, 20 items max

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/3/tv/{series_id}/season/{season_number}/episode/{episode_number}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "append_to_response": append_to_response,
                        "language": language,
                    },
                    episode_retrieve_params.EpisodeRetrieveParams,
                ),
            ),
            cast_to=EpisodeRetrieveResponse,
        )


class EpisodesResourceWithRawResponse:
    def __init__(self, episodes: EpisodesResource) -> None:
        self._episodes = episodes

        self.retrieve = to_raw_response_wrapper(
            episodes.retrieve,
        )

    @cached_property
    def images(self) -> ImagesResourceWithRawResponse:
        return ImagesResourceWithRawResponse(self._episodes.images)

    @cached_property
    def credits(self) -> CreditsResourceWithRawResponse:
        return CreditsResourceWithRawResponse(self._episodes.credits)

    @cached_property
    def external_ids(self) -> ExternalIDsResourceWithRawResponse:
        return ExternalIDsResourceWithRawResponse(self._episodes.external_ids)

    @cached_property
    def translations(self) -> TranslationsResourceWithRawResponse:
        return TranslationsResourceWithRawResponse(self._episodes.translations)


class AsyncEpisodesResourceWithRawResponse:
    def __init__(self, episodes: AsyncEpisodesResource) -> None:
        self._episodes = episodes

        self.retrieve = async_to_raw_response_wrapper(
            episodes.retrieve,
        )

    @cached_property
    def images(self) -> AsyncImagesResourceWithRawResponse:
        return AsyncImagesResourceWithRawResponse(self._episodes.images)

    @cached_property
    def credits(self) -> AsyncCreditsResourceWithRawResponse:
        return AsyncCreditsResourceWithRawResponse(self._episodes.credits)

    @cached_property
    def external_ids(self) -> AsyncExternalIDsResourceWithRawResponse:
        return AsyncExternalIDsResourceWithRawResponse(self._episodes.external_ids)

    @cached_property
    def translations(self) -> AsyncTranslationsResourceWithRawResponse:
        return AsyncTranslationsResourceWithRawResponse(self._episodes.translations)


class EpisodesResourceWithStreamingResponse:
    def __init__(self, episodes: EpisodesResource) -> None:
        self._episodes = episodes

        self.retrieve = to_streamed_response_wrapper(
            episodes.retrieve,
        )

    @cached_property
    def images(self) -> ImagesResourceWithStreamingResponse:
        return ImagesResourceWithStreamingResponse(self._episodes.images)

    @cached_property
    def credits(self) -> CreditsResourceWithStreamingResponse:
        return CreditsResourceWithStreamingResponse(self._episodes.credits)

    @cached_property
    def external_ids(self) -> ExternalIDsResourceWithStreamingResponse:
        return ExternalIDsResourceWithStreamingResponse(self._episodes.external_ids)

    @cached_property
    def translations(self) -> TranslationsResourceWithStreamingResponse:
        return TranslationsResourceWithStreamingResponse(self._episodes.translations)


class AsyncEpisodesResourceWithStreamingResponse:
    def __init__(self, episodes: AsyncEpisodesResource) -> None:
        self._episodes = episodes

        self.retrieve = async_to_streamed_response_wrapper(
            episodes.retrieve,
        )

    @cached_property
    def images(self) -> AsyncImagesResourceWithStreamingResponse:
        return AsyncImagesResourceWithStreamingResponse(self._episodes.images)

    @cached_property
    def credits(self) -> AsyncCreditsResourceWithStreamingResponse:
        return AsyncCreditsResourceWithStreamingResponse(self._episodes.credits)

    @cached_property
    def external_ids(self) -> AsyncExternalIDsResourceWithStreamingResponse:
        return AsyncExternalIDsResourceWithStreamingResponse(self._episodes.external_ids)

    @cached_property
    def translations(self) -> AsyncTranslationsResourceWithStreamingResponse:
        return AsyncTranslationsResourceWithStreamingResponse(self._episodes.translations)
