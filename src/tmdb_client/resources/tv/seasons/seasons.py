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
from .videos import (
    VideosResource,
    AsyncVideosResource,
    VideosResourceWithRawResponse,
    AsyncVideosResourceWithRawResponse,
    VideosResourceWithStreamingResponse,
    AsyncVideosResourceWithStreamingResponse,
)
from .changes import (
    ChangesResource,
    AsyncChangesResource,
    ChangesResourceWithRawResponse,
    AsyncChangesResourceWithRawResponse,
    ChangesResourceWithStreamingResponse,
    AsyncChangesResourceWithStreamingResponse,
)
from .credits import (
    CreditsResource,
    AsyncCreditsResource,
    CreditsResourceWithRawResponse,
    AsyncCreditsResourceWithRawResponse,
    CreditsResourceWithStreamingResponse,
    AsyncCreditsResourceWithStreamingResponse,
)
from .episodes import (
    EpisodesResource,
    AsyncEpisodesResource,
    EpisodesResourceWithRawResponse,
    AsyncEpisodesResourceWithRawResponse,
    EpisodesResourceWithStreamingResponse,
    AsyncEpisodesResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ....types.tv import season_retrieve_params
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
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
from .account_states import (
    AccountStatesResource,
    AsyncAccountStatesResource,
    AccountStatesResourceWithRawResponse,
    AsyncAccountStatesResourceWithRawResponse,
    AccountStatesResourceWithStreamingResponse,
    AsyncAccountStatesResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from .watch_providers import (
    WatchProvidersResource,
    AsyncWatchProvidersResource,
    WatchProvidersResourceWithRawResponse,
    AsyncWatchProvidersResourceWithRawResponse,
    WatchProvidersResourceWithStreamingResponse,
    AsyncWatchProvidersResourceWithStreamingResponse,
)
from .aggregate_credits import (
    AggregateCreditsResource,
    AsyncAggregateCreditsResource,
    AggregateCreditsResourceWithRawResponse,
    AsyncAggregateCreditsResourceWithRawResponse,
    AggregateCreditsResourceWithStreamingResponse,
    AsyncAggregateCreditsResourceWithStreamingResponse,
)
from .episodes.episodes import EpisodesResource, AsyncEpisodesResource
from ....types.tv.season_retrieve_response import SeasonRetrieveResponse

__all__ = ["SeasonsResource", "AsyncSeasonsResource"]


class SeasonsResource(SyncAPIResource):
    @cached_property
    def episodes(self) -> EpisodesResource:
        return EpisodesResource(self._client)

    @cached_property
    def images(self) -> ImagesResource:
        return ImagesResource(self._client)

    @cached_property
    def account_states(self) -> AccountStatesResource:
        return AccountStatesResource(self._client)

    @cached_property
    def aggregate_credits(self) -> AggregateCreditsResource:
        return AggregateCreditsResource(self._client)

    @cached_property
    def changes(self) -> ChangesResource:
        return ChangesResource(self._client)

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
    def videos(self) -> VideosResource:
        return VideosResource(self._client)

    @cached_property
    def watch_providers(self) -> WatchProvidersResource:
        return WatchProvidersResource(self._client)

    @cached_property
    def with_raw_response(self) -> SeasonsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return SeasonsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SeasonsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return SeasonsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        season_number: int,
        *,
        series_id: int,
        append_to_response: str | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SeasonRetrieveResponse:
        """
        Query the details of a TV season.

        Args:
          append_to_response: comma separated list of endpoints within this namespace, 20 items max

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/3/tv/{series_id}/season/{season_number}",
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
                    season_retrieve_params.SeasonRetrieveParams,
                ),
            ),
            cast_to=SeasonRetrieveResponse,
        )


class AsyncSeasonsResource(AsyncAPIResource):
    @cached_property
    def episodes(self) -> AsyncEpisodesResource:
        return AsyncEpisodesResource(self._client)

    @cached_property
    def images(self) -> AsyncImagesResource:
        return AsyncImagesResource(self._client)

    @cached_property
    def account_states(self) -> AsyncAccountStatesResource:
        return AsyncAccountStatesResource(self._client)

    @cached_property
    def aggregate_credits(self) -> AsyncAggregateCreditsResource:
        return AsyncAggregateCreditsResource(self._client)

    @cached_property
    def changes(self) -> AsyncChangesResource:
        return AsyncChangesResource(self._client)

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
    def videos(self) -> AsyncVideosResource:
        return AsyncVideosResource(self._client)

    @cached_property
    def watch_providers(self) -> AsyncWatchProvidersResource:
        return AsyncWatchProvidersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSeasonsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSeasonsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSeasonsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncSeasonsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        season_number: int,
        *,
        series_id: int,
        append_to_response: str | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SeasonRetrieveResponse:
        """
        Query the details of a TV season.

        Args:
          append_to_response: comma separated list of endpoints within this namespace, 20 items max

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/3/tv/{series_id}/season/{season_number}",
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
                    season_retrieve_params.SeasonRetrieveParams,
                ),
            ),
            cast_to=SeasonRetrieveResponse,
        )


class SeasonsResourceWithRawResponse:
    def __init__(self, seasons: SeasonsResource) -> None:
        self._seasons = seasons

        self.retrieve = to_raw_response_wrapper(
            seasons.retrieve,
        )

    @cached_property
    def episodes(self) -> EpisodesResourceWithRawResponse:
        return EpisodesResourceWithRawResponse(self._seasons.episodes)

    @cached_property
    def images(self) -> ImagesResourceWithRawResponse:
        return ImagesResourceWithRawResponse(self._seasons.images)

    @cached_property
    def account_states(self) -> AccountStatesResourceWithRawResponse:
        return AccountStatesResourceWithRawResponse(self._seasons.account_states)

    @cached_property
    def aggregate_credits(self) -> AggregateCreditsResourceWithRawResponse:
        return AggregateCreditsResourceWithRawResponse(self._seasons.aggregate_credits)

    @cached_property
    def changes(self) -> ChangesResourceWithRawResponse:
        return ChangesResourceWithRawResponse(self._seasons.changes)

    @cached_property
    def credits(self) -> CreditsResourceWithRawResponse:
        return CreditsResourceWithRawResponse(self._seasons.credits)

    @cached_property
    def external_ids(self) -> ExternalIDsResourceWithRawResponse:
        return ExternalIDsResourceWithRawResponse(self._seasons.external_ids)

    @cached_property
    def translations(self) -> TranslationsResourceWithRawResponse:
        return TranslationsResourceWithRawResponse(self._seasons.translations)

    @cached_property
    def videos(self) -> VideosResourceWithRawResponse:
        return VideosResourceWithRawResponse(self._seasons.videos)

    @cached_property
    def watch_providers(self) -> WatchProvidersResourceWithRawResponse:
        return WatchProvidersResourceWithRawResponse(self._seasons.watch_providers)


class AsyncSeasonsResourceWithRawResponse:
    def __init__(self, seasons: AsyncSeasonsResource) -> None:
        self._seasons = seasons

        self.retrieve = async_to_raw_response_wrapper(
            seasons.retrieve,
        )

    @cached_property
    def episodes(self) -> AsyncEpisodesResourceWithRawResponse:
        return AsyncEpisodesResourceWithRawResponse(self._seasons.episodes)

    @cached_property
    def images(self) -> AsyncImagesResourceWithRawResponse:
        return AsyncImagesResourceWithRawResponse(self._seasons.images)

    @cached_property
    def account_states(self) -> AsyncAccountStatesResourceWithRawResponse:
        return AsyncAccountStatesResourceWithRawResponse(self._seasons.account_states)

    @cached_property
    def aggregate_credits(self) -> AsyncAggregateCreditsResourceWithRawResponse:
        return AsyncAggregateCreditsResourceWithRawResponse(self._seasons.aggregate_credits)

    @cached_property
    def changes(self) -> AsyncChangesResourceWithRawResponse:
        return AsyncChangesResourceWithRawResponse(self._seasons.changes)

    @cached_property
    def credits(self) -> AsyncCreditsResourceWithRawResponse:
        return AsyncCreditsResourceWithRawResponse(self._seasons.credits)

    @cached_property
    def external_ids(self) -> AsyncExternalIDsResourceWithRawResponse:
        return AsyncExternalIDsResourceWithRawResponse(self._seasons.external_ids)

    @cached_property
    def translations(self) -> AsyncTranslationsResourceWithRawResponse:
        return AsyncTranslationsResourceWithRawResponse(self._seasons.translations)

    @cached_property
    def videos(self) -> AsyncVideosResourceWithRawResponse:
        return AsyncVideosResourceWithRawResponse(self._seasons.videos)

    @cached_property
    def watch_providers(self) -> AsyncWatchProvidersResourceWithRawResponse:
        return AsyncWatchProvidersResourceWithRawResponse(self._seasons.watch_providers)


class SeasonsResourceWithStreamingResponse:
    def __init__(self, seasons: SeasonsResource) -> None:
        self._seasons = seasons

        self.retrieve = to_streamed_response_wrapper(
            seasons.retrieve,
        )

    @cached_property
    def episodes(self) -> EpisodesResourceWithStreamingResponse:
        return EpisodesResourceWithStreamingResponse(self._seasons.episodes)

    @cached_property
    def images(self) -> ImagesResourceWithStreamingResponse:
        return ImagesResourceWithStreamingResponse(self._seasons.images)

    @cached_property
    def account_states(self) -> AccountStatesResourceWithStreamingResponse:
        return AccountStatesResourceWithStreamingResponse(self._seasons.account_states)

    @cached_property
    def aggregate_credits(self) -> AggregateCreditsResourceWithStreamingResponse:
        return AggregateCreditsResourceWithStreamingResponse(self._seasons.aggregate_credits)

    @cached_property
    def changes(self) -> ChangesResourceWithStreamingResponse:
        return ChangesResourceWithStreamingResponse(self._seasons.changes)

    @cached_property
    def credits(self) -> CreditsResourceWithStreamingResponse:
        return CreditsResourceWithStreamingResponse(self._seasons.credits)

    @cached_property
    def external_ids(self) -> ExternalIDsResourceWithStreamingResponse:
        return ExternalIDsResourceWithStreamingResponse(self._seasons.external_ids)

    @cached_property
    def translations(self) -> TranslationsResourceWithStreamingResponse:
        return TranslationsResourceWithStreamingResponse(self._seasons.translations)

    @cached_property
    def videos(self) -> VideosResourceWithStreamingResponse:
        return VideosResourceWithStreamingResponse(self._seasons.videos)

    @cached_property
    def watch_providers(self) -> WatchProvidersResourceWithStreamingResponse:
        return WatchProvidersResourceWithStreamingResponse(self._seasons.watch_providers)


class AsyncSeasonsResourceWithStreamingResponse:
    def __init__(self, seasons: AsyncSeasonsResource) -> None:
        self._seasons = seasons

        self.retrieve = async_to_streamed_response_wrapper(
            seasons.retrieve,
        )

    @cached_property
    def episodes(self) -> AsyncEpisodesResourceWithStreamingResponse:
        return AsyncEpisodesResourceWithStreamingResponse(self._seasons.episodes)

    @cached_property
    def images(self) -> AsyncImagesResourceWithStreamingResponse:
        return AsyncImagesResourceWithStreamingResponse(self._seasons.images)

    @cached_property
    def account_states(self) -> AsyncAccountStatesResourceWithStreamingResponse:
        return AsyncAccountStatesResourceWithStreamingResponse(self._seasons.account_states)

    @cached_property
    def aggregate_credits(self) -> AsyncAggregateCreditsResourceWithStreamingResponse:
        return AsyncAggregateCreditsResourceWithStreamingResponse(self._seasons.aggregate_credits)

    @cached_property
    def changes(self) -> AsyncChangesResourceWithStreamingResponse:
        return AsyncChangesResourceWithStreamingResponse(self._seasons.changes)

    @cached_property
    def credits(self) -> AsyncCreditsResourceWithStreamingResponse:
        return AsyncCreditsResourceWithStreamingResponse(self._seasons.credits)

    @cached_property
    def external_ids(self) -> AsyncExternalIDsResourceWithStreamingResponse:
        return AsyncExternalIDsResourceWithStreamingResponse(self._seasons.external_ids)

    @cached_property
    def translations(self) -> AsyncTranslationsResourceWithStreamingResponse:
        return AsyncTranslationsResourceWithStreamingResponse(self._seasons.translations)

    @cached_property
    def videos(self) -> AsyncVideosResourceWithStreamingResponse:
        return AsyncVideosResourceWithStreamingResponse(self._seasons.videos)

    @cached_property
    def watch_providers(self) -> AsyncWatchProvidersResourceWithStreamingResponse:
        return AsyncWatchProvidersResourceWithStreamingResponse(self._seasons.watch_providers)
