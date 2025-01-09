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
from ...types import tv_search_params, tv_retrieve_params
from .changes import (
    ChangesResource,
    AsyncChangesResource,
    ChangesResourceWithRawResponse,
    AsyncChangesResourceWithRawResponse,
    ChangesResourceWithStreamingResponse,
    AsyncChangesResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .episode_group import (
    EpisodeGroupResource,
    AsyncEpisodeGroupResource,
    EpisodeGroupResourceWithRawResponse,
    AsyncEpisodeGroupResourceWithRawResponse,
    EpisodeGroupResourceWithStreamingResponse,
    AsyncEpisodeGroupResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .account_states import (
    AccountStatesResource,
    AsyncAccountStatesResource,
    AccountStatesResourceWithRawResponse,
    AsyncAccountStatesResourceWithRawResponse,
    AccountStatesResourceWithStreamingResponse,
    AsyncAccountStatesResourceWithStreamingResponse,
)
from .episode.episode import (
    EpisodeResource,
    AsyncEpisodeResource,
    EpisodeResourceWithRawResponse,
    AsyncEpisodeResourceWithRawResponse,
    EpisodeResourceWithStreamingResponse,
    AsyncEpisodeResourceWithStreamingResponse,
)
from .seasons.seasons import (
    SeasonsResource,
    AsyncSeasonsResource,
    SeasonsResourceWithRawResponse,
    AsyncSeasonsResourceWithRawResponse,
    SeasonsResourceWithStreamingResponse,
    AsyncSeasonsResourceWithStreamingResponse,
)
from .episodes.episodes import (
    EpisodesResource,
    AsyncEpisodesResource,
    EpisodesResourceWithRawResponse,
    AsyncEpisodesResourceWithRawResponse,
    EpisodesResourceWithStreamingResponse,
    AsyncEpisodesResourceWithStreamingResponse,
)
from ...types.tv_search_response import TvSearchResponse
from ...types.tv_retrieve_response import TvRetrieveResponse

__all__ = ["TvResource", "AsyncTvResource"]


class TvResource(SyncAPIResource):
    @cached_property
    def seasons(self) -> SeasonsResource:
        return SeasonsResource(self._client)

    @cached_property
    def images(self) -> ImagesResource:
        return ImagesResource(self._client)

    @cached_property
    def account_states(self) -> AccountStatesResource:
        return AccountStatesResource(self._client)

    @cached_property
    def episodes(self) -> EpisodesResource:
        return EpisodesResource(self._client)

    @cached_property
    def changes(self) -> ChangesResource:
        return ChangesResource(self._client)

    @cached_property
    def episode(self) -> EpisodeResource:
        return EpisodeResource(self._client)

    @cached_property
    def episode_group(self) -> EpisodeGroupResource:
        return EpisodeGroupResource(self._client)

    @cached_property
    def with_raw_response(self) -> TvResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return TvResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TvResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return TvResourceWithStreamingResponse(self)

    def retrieve(
        self,
        series_id: int,
        *,
        append_to_response: str | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TvRetrieveResponse:
        """
        Get the details of a TV show.

        Args:
          append_to_response: comma separated list of endpoints within this namespace, 20 items max

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/3/tv/{series_id}",
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
                    tv_retrieve_params.TvRetrieveParams,
                ),
            ),
            cast_to=TvRetrieveResponse,
        )

    def search(
        self,
        *,
        query: str,
        first_air_date_year: int | NotGiven = NOT_GIVEN,
        include_adult: bool | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        year: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TvSearchResponse:
        """
        Search for TV shows by their original, translated and also known as names.

        Args:
          first_air_date_year: Search only the first air date. Valid values are: 1000..9999

          year:
              Search the first air date and all episode air dates. Valid values are:
              1000..9999

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/3/search/tv",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query": query,
                        "first_air_date_year": first_air_date_year,
                        "include_adult": include_adult,
                        "language": language,
                        "page": page,
                        "year": year,
                    },
                    tv_search_params.TvSearchParams,
                ),
            ),
            cast_to=TvSearchResponse,
        )


class AsyncTvResource(AsyncAPIResource):
    @cached_property
    def seasons(self) -> AsyncSeasonsResource:
        return AsyncSeasonsResource(self._client)

    @cached_property
    def images(self) -> AsyncImagesResource:
        return AsyncImagesResource(self._client)

    @cached_property
    def account_states(self) -> AsyncAccountStatesResource:
        return AsyncAccountStatesResource(self._client)

    @cached_property
    def episodes(self) -> AsyncEpisodesResource:
        return AsyncEpisodesResource(self._client)

    @cached_property
    def changes(self) -> AsyncChangesResource:
        return AsyncChangesResource(self._client)

    @cached_property
    def episode(self) -> AsyncEpisodeResource:
        return AsyncEpisodeResource(self._client)

    @cached_property
    def episode_group(self) -> AsyncEpisodeGroupResource:
        return AsyncEpisodeGroupResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTvResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTvResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTvResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncTvResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        series_id: int,
        *,
        append_to_response: str | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TvRetrieveResponse:
        """
        Get the details of a TV show.

        Args:
          append_to_response: comma separated list of endpoints within this namespace, 20 items max

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/3/tv/{series_id}",
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
                    tv_retrieve_params.TvRetrieveParams,
                ),
            ),
            cast_to=TvRetrieveResponse,
        )

    async def search(
        self,
        *,
        query: str,
        first_air_date_year: int | NotGiven = NOT_GIVEN,
        include_adult: bool | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        year: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TvSearchResponse:
        """
        Search for TV shows by their original, translated and also known as names.

        Args:
          first_air_date_year: Search only the first air date. Valid values are: 1000..9999

          year:
              Search the first air date and all episode air dates. Valid values are:
              1000..9999

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/3/search/tv",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query": query,
                        "first_air_date_year": first_air_date_year,
                        "include_adult": include_adult,
                        "language": language,
                        "page": page,
                        "year": year,
                    },
                    tv_search_params.TvSearchParams,
                ),
            ),
            cast_to=TvSearchResponse,
        )


class TvResourceWithRawResponse:
    def __init__(self, tv: TvResource) -> None:
        self._tv = tv

        self.retrieve = to_raw_response_wrapper(
            tv.retrieve,
        )
        self.search = to_raw_response_wrapper(
            tv.search,
        )

    @cached_property
    def seasons(self) -> SeasonsResourceWithRawResponse:
        return SeasonsResourceWithRawResponse(self._tv.seasons)

    @cached_property
    def images(self) -> ImagesResourceWithRawResponse:
        return ImagesResourceWithRawResponse(self._tv.images)

    @cached_property
    def account_states(self) -> AccountStatesResourceWithRawResponse:
        return AccountStatesResourceWithRawResponse(self._tv.account_states)

    @cached_property
    def episodes(self) -> EpisodesResourceWithRawResponse:
        return EpisodesResourceWithRawResponse(self._tv.episodes)

    @cached_property
    def changes(self) -> ChangesResourceWithRawResponse:
        return ChangesResourceWithRawResponse(self._tv.changes)

    @cached_property
    def episode(self) -> EpisodeResourceWithRawResponse:
        return EpisodeResourceWithRawResponse(self._tv.episode)

    @cached_property
    def episode_group(self) -> EpisodeGroupResourceWithRawResponse:
        return EpisodeGroupResourceWithRawResponse(self._tv.episode_group)


class AsyncTvResourceWithRawResponse:
    def __init__(self, tv: AsyncTvResource) -> None:
        self._tv = tv

        self.retrieve = async_to_raw_response_wrapper(
            tv.retrieve,
        )
        self.search = async_to_raw_response_wrapper(
            tv.search,
        )

    @cached_property
    def seasons(self) -> AsyncSeasonsResourceWithRawResponse:
        return AsyncSeasonsResourceWithRawResponse(self._tv.seasons)

    @cached_property
    def images(self) -> AsyncImagesResourceWithRawResponse:
        return AsyncImagesResourceWithRawResponse(self._tv.images)

    @cached_property
    def account_states(self) -> AsyncAccountStatesResourceWithRawResponse:
        return AsyncAccountStatesResourceWithRawResponse(self._tv.account_states)

    @cached_property
    def episodes(self) -> AsyncEpisodesResourceWithRawResponse:
        return AsyncEpisodesResourceWithRawResponse(self._tv.episodes)

    @cached_property
    def changes(self) -> AsyncChangesResourceWithRawResponse:
        return AsyncChangesResourceWithRawResponse(self._tv.changes)

    @cached_property
    def episode(self) -> AsyncEpisodeResourceWithRawResponse:
        return AsyncEpisodeResourceWithRawResponse(self._tv.episode)

    @cached_property
    def episode_group(self) -> AsyncEpisodeGroupResourceWithRawResponse:
        return AsyncEpisodeGroupResourceWithRawResponse(self._tv.episode_group)


class TvResourceWithStreamingResponse:
    def __init__(self, tv: TvResource) -> None:
        self._tv = tv

        self.retrieve = to_streamed_response_wrapper(
            tv.retrieve,
        )
        self.search = to_streamed_response_wrapper(
            tv.search,
        )

    @cached_property
    def seasons(self) -> SeasonsResourceWithStreamingResponse:
        return SeasonsResourceWithStreamingResponse(self._tv.seasons)

    @cached_property
    def images(self) -> ImagesResourceWithStreamingResponse:
        return ImagesResourceWithStreamingResponse(self._tv.images)

    @cached_property
    def account_states(self) -> AccountStatesResourceWithStreamingResponse:
        return AccountStatesResourceWithStreamingResponse(self._tv.account_states)

    @cached_property
    def episodes(self) -> EpisodesResourceWithStreamingResponse:
        return EpisodesResourceWithStreamingResponse(self._tv.episodes)

    @cached_property
    def changes(self) -> ChangesResourceWithStreamingResponse:
        return ChangesResourceWithStreamingResponse(self._tv.changes)

    @cached_property
    def episode(self) -> EpisodeResourceWithStreamingResponse:
        return EpisodeResourceWithStreamingResponse(self._tv.episode)

    @cached_property
    def episode_group(self) -> EpisodeGroupResourceWithStreamingResponse:
        return EpisodeGroupResourceWithStreamingResponse(self._tv.episode_group)


class AsyncTvResourceWithStreamingResponse:
    def __init__(self, tv: AsyncTvResource) -> None:
        self._tv = tv

        self.retrieve = async_to_streamed_response_wrapper(
            tv.retrieve,
        )
        self.search = async_to_streamed_response_wrapper(
            tv.search,
        )

    @cached_property
    def seasons(self) -> AsyncSeasonsResourceWithStreamingResponse:
        return AsyncSeasonsResourceWithStreamingResponse(self._tv.seasons)

    @cached_property
    def images(self) -> AsyncImagesResourceWithStreamingResponse:
        return AsyncImagesResourceWithStreamingResponse(self._tv.images)

    @cached_property
    def account_states(self) -> AsyncAccountStatesResourceWithStreamingResponse:
        return AsyncAccountStatesResourceWithStreamingResponse(self._tv.account_states)

    @cached_property
    def episodes(self) -> AsyncEpisodesResourceWithStreamingResponse:
        return AsyncEpisodesResourceWithStreamingResponse(self._tv.episodes)

    @cached_property
    def changes(self) -> AsyncChangesResourceWithStreamingResponse:
        return AsyncChangesResourceWithStreamingResponse(self._tv.changes)

    @cached_property
    def episode(self) -> AsyncEpisodeResourceWithStreamingResponse:
        return AsyncEpisodeResourceWithStreamingResponse(self._tv.episode)

    @cached_property
    def episode_group(self) -> AsyncEpisodeGroupResourceWithStreamingResponse:
        return AsyncEpisodeGroupResourceWithStreamingResponse(self._tv.episode_group)
