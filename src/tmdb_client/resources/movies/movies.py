# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from .lists import (
    ListsResource,
    AsyncListsResource,
    ListsResourceWithRawResponse,
    AsyncListsResourceWithRawResponse,
    ListsResourceWithStreamingResponse,
    AsyncListsResourceWithStreamingResponse,
)
from .images import (
    ImagesResource,
    AsyncImagesResource,
    ImagesResourceWithRawResponse,
    AsyncImagesResourceWithRawResponse,
    ImagesResourceWithStreamingResponse,
    AsyncImagesResourceWithStreamingResponse,
)
from .latest import (
    LatestResource,
    AsyncLatestResource,
    LatestResourceWithRawResponse,
    AsyncLatestResourceWithRawResponse,
    LatestResourceWithStreamingResponse,
    AsyncLatestResourceWithStreamingResponse,
)
from .videos import (
    VideosResource,
    AsyncVideosResource,
    VideosResourceWithRawResponse,
    AsyncVideosResourceWithRawResponse,
    VideosResourceWithStreamingResponse,
    AsyncVideosResourceWithStreamingResponse,
)
from ...types import (
    movie_rating_params,
    movie_search_params,
    movie_discover_params,
    movie_retrieve_params,
    movie_rating_delete_params,
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
from .popular import (
    PopularResource,
    AsyncPopularResource,
    PopularResourceWithRawResponse,
    AsyncPopularResourceWithRawResponse,
    PopularResourceWithStreamingResponse,
    AsyncPopularResourceWithStreamingResponse,
)
from .reviews import (
    ReviewsResource,
    AsyncReviewsResource,
    ReviewsResourceWithRawResponse,
    AsyncReviewsResourceWithRawResponse,
    ReviewsResourceWithStreamingResponse,
    AsyncReviewsResourceWithStreamingResponse,
)
from .similar import (
    SimilarResource,
    AsyncSimilarResource,
    SimilarResourceWithRawResponse,
    AsyncSimilarResourceWithRawResponse,
    SimilarResourceWithStreamingResponse,
    AsyncSimilarResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .keywords import (
    KeywordsResource,
    AsyncKeywordsResource,
    KeywordsResourceWithRawResponse,
    AsyncKeywordsResourceWithRawResponse,
    KeywordsResourceWithStreamingResponse,
    AsyncKeywordsResourceWithStreamingResponse,
)
from .upcoming import (
    UpcomingResource,
    AsyncUpcomingResource,
    UpcomingResourceWithRawResponse,
    AsyncUpcomingResourceWithRawResponse,
    UpcomingResourceWithStreamingResponse,
    AsyncUpcomingResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .top_rated import (
    TopRatedResource,
    AsyncTopRatedResource,
    TopRatedResourceWithRawResponse,
    AsyncTopRatedResourceWithRawResponse,
    TopRatedResourceWithStreamingResponse,
    AsyncTopRatedResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .now_playing import (
    NowPlayingResource,
    AsyncNowPlayingResource,
    NowPlayingResourceWithRawResponse,
    AsyncNowPlayingResourceWithRawResponse,
    NowPlayingResourceWithStreamingResponse,
    AsyncNowPlayingResourceWithStreamingResponse,
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
from .release_dates import (
    ReleaseDatesResource,
    AsyncReleaseDatesResource,
    ReleaseDatesResourceWithRawResponse,
    AsyncReleaseDatesResourceWithRawResponse,
    ReleaseDatesResourceWithStreamingResponse,
    AsyncReleaseDatesResourceWithStreamingResponse,
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
from .recommendations import (
    RecommendationsResource,
    AsyncRecommendationsResource,
    RecommendationsResourceWithRawResponse,
    AsyncRecommendationsResourceWithRawResponse,
    RecommendationsResourceWithStreamingResponse,
    AsyncRecommendationsResourceWithStreamingResponse,
)
from .watch_providers import (
    WatchProvidersResource,
    AsyncWatchProvidersResource,
    WatchProvidersResourceWithRawResponse,
    AsyncWatchProvidersResourceWithRawResponse,
    WatchProvidersResourceWithStreamingResponse,
    AsyncWatchProvidersResourceWithStreamingResponse,
)
from .alternative_titles import (
    AlternativeTitlesResource,
    AsyncAlternativeTitlesResource,
    AlternativeTitlesResourceWithRawResponse,
    AsyncAlternativeTitlesResourceWithRawResponse,
    AlternativeTitlesResourceWithStreamingResponse,
    AsyncAlternativeTitlesResourceWithStreamingResponse,
)
from ...types.movie_rating_response import MovieRatingResponse
from ...types.movie_search_response import MovieSearchResponse
from ...types.movie_discover_response import MovieDiscoverResponse
from ...types.movie_retrieve_response import MovieRetrieveResponse
from ...types.movie_rating_delete_response import MovieRatingDeleteResponse

__all__ = ["MoviesResource", "AsyncMoviesResource"]


class MoviesResource(SyncAPIResource):
    @cached_property
    def images(self) -> ImagesResource:
        return ImagesResource(self._client)

    @cached_property
    def account_states(self) -> AccountStatesResource:
        return AccountStatesResource(self._client)

    @cached_property
    def alternative_titles(self) -> AlternativeTitlesResource:
        return AlternativeTitlesResource(self._client)

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
    def keywords(self) -> KeywordsResource:
        return KeywordsResource(self._client)

    @cached_property
    def lists(self) -> ListsResource:
        return ListsResource(self._client)

    @cached_property
    def recommendations(self) -> RecommendationsResource:
        return RecommendationsResource(self._client)

    @cached_property
    def release_dates(self) -> ReleaseDatesResource:
        return ReleaseDatesResource(self._client)

    @cached_property
    def reviews(self) -> ReviewsResource:
        return ReviewsResource(self._client)

    @cached_property
    def similar(self) -> SimilarResource:
        return SimilarResource(self._client)

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
    def popular(self) -> PopularResource:
        return PopularResource(self._client)

    @cached_property
    def top_rated(self) -> TopRatedResource:
        return TopRatedResource(self._client)

    @cached_property
    def upcoming(self) -> UpcomingResource:
        return UpcomingResource(self._client)

    @cached_property
    def now_playing(self) -> NowPlayingResource:
        return NowPlayingResource(self._client)

    @cached_property
    def latest(self) -> LatestResource:
        return LatestResource(self._client)

    @cached_property
    def with_raw_response(self) -> MoviesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return MoviesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MoviesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return MoviesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        movie_id: int,
        *,
        append_to_response: str | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MovieRetrieveResponse:
        """
        Get the top level details of a movie by ID.

        Args:
          append_to_response: comma separated list of endpoints within this namespace, 20 items max

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/3/movie/{movie_id}",
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
                    movie_retrieve_params.MovieRetrieveParams,
                ),
            ),
            cast_to=MovieRetrieveResponse,
        )

    def discover(
        self,
        *,
        certification: movie_discover_params.Certification | NotGiven = NOT_GIVEN,
        certification_country: str | NotGiven = NOT_GIVEN,
        include_adult: bool | NotGiven = NOT_GIVEN,
        include_video: bool | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        primary_release_date: movie_discover_params.PrimaryReleaseDate | NotGiven = NOT_GIVEN,
        primary_release_year: int | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        release_date: movie_discover_params.ReleaseDate | NotGiven = NOT_GIVEN,
        sort_by: Literal[
            "original_title.asc",
            "original_title.desc",
            "popularity.asc",
            "popularity.desc",
            "revenue.asc",
            "revenue.desc",
            "primary_release_date.asc",
            "title.asc",
            "title.desc",
            "primary_release_date.desc",
            "vote_average.asc",
            "vote_average.desc",
            "vote_count.asc",
            "vote_count.desc",
        ]
        | NotGiven = NOT_GIVEN,
        vote_average: movie_discover_params.VoteAverage | NotGiven = NOT_GIVEN,
        vote_count: movie_discover_params.VoteCount | NotGiven = NOT_GIVEN,
        watch_region: str | NotGiven = NOT_GIVEN,
        with_cast: str | NotGiven = NOT_GIVEN,
        with_companies: str | NotGiven = NOT_GIVEN,
        with_crew: str | NotGiven = NOT_GIVEN,
        with_genres: str | NotGiven = NOT_GIVEN,
        with_keywords: str | NotGiven = NOT_GIVEN,
        with_origin_country: str | NotGiven = NOT_GIVEN,
        with_original_language: str | NotGiven = NOT_GIVEN,
        with_people: str | NotGiven = NOT_GIVEN,
        with_release_type: int | NotGiven = NOT_GIVEN,
        with_runtime: movie_discover_params.WithRuntime | NotGiven = NOT_GIVEN,
        with_watch_monetization_types: str | NotGiven = NOT_GIVEN,
        with_watch_providers: str | NotGiven = NOT_GIVEN,
        without_companies: str | NotGiven = NOT_GIVEN,
        without_genres: str | NotGiven = NOT_GIVEN,
        without_keywords: str | NotGiven = NOT_GIVEN,
        without_watch_providers: str | NotGiven = NOT_GIVEN,
        year: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MovieDiscoverResponse:
        """
        Find movies using over 30 filters and sort options.

        Args:
          certification_country: use in conjunction with the `certification`, `certification.gte` and
              `certification.lte` filters

          watch_region: use in conjunction with `with_watch_monetization_types ` or
              `with_watch_providers `

          with_cast: can be a comma (`AND`) or pipe (`OR`) separated query

          with_companies: can be a comma (`AND`) or pipe (`OR`) separated query

          with_crew: can be a comma (`AND`) or pipe (`OR`) separated query

          with_genres: can be a comma (`AND`) or pipe (`OR`) separated query

          with_keywords: can be a comma (`AND`) or pipe (`OR`) separated query

          with_people: can be a comma (`AND`) or pipe (`OR`) separated query

          with_release_type: possible values are: [1, 2, 3, 4, 5, 6] can be a comma (`AND`) or pipe (`OR`)
              separated query, can be used in conjunction with `region`

          with_watch_monetization_types: possible values are: [flatrate, free, ads, rent, buy] use in conjunction with
              `watch_region`, can be a comma (`AND`) or pipe (`OR`) separated query

          with_watch_providers: use in conjunction with `watch_region`, can be a comma (`AND`) or pipe (`OR`)
              separated query

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/3/discover/movie",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "certification": certification,
                        "certification_country": certification_country,
                        "include_adult": include_adult,
                        "include_video": include_video,
                        "language": language,
                        "page": page,
                        "primary_release_date": primary_release_date,
                        "primary_release_year": primary_release_year,
                        "region": region,
                        "release_date": release_date,
                        "sort_by": sort_by,
                        "vote_average": vote_average,
                        "vote_count": vote_count,
                        "watch_region": watch_region,
                        "with_cast": with_cast,
                        "with_companies": with_companies,
                        "with_crew": with_crew,
                        "with_genres": with_genres,
                        "with_keywords": with_keywords,
                        "with_origin_country": with_origin_country,
                        "with_original_language": with_original_language,
                        "with_people": with_people,
                        "with_release_type": with_release_type,
                        "with_runtime": with_runtime,
                        "with_watch_monetization_types": with_watch_monetization_types,
                        "with_watch_providers": with_watch_providers,
                        "without_companies": without_companies,
                        "without_genres": without_genres,
                        "without_keywords": without_keywords,
                        "without_watch_providers": without_watch_providers,
                        "year": year,
                    },
                    movie_discover_params.MovieDiscoverParams,
                ),
            ),
            cast_to=MovieDiscoverResponse,
        )

    def rating(
        self,
        movie_id: int,
        *,
        raw_body: str,
        guest_session_id: str | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MovieRatingResponse:
        """
        Rate a movie and save it to your rated list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/3/movie/{movie_id}/rating",
            body=maybe_transform({"raw_body": raw_body}, movie_rating_params.MovieRatingParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "guest_session_id": guest_session_id,
                        "session_id": session_id,
                    },
                    movie_rating_params.MovieRatingParams,
                ),
            ),
            cast_to=MovieRatingResponse,
        )

    def rating_delete(
        self,
        movie_id: int,
        *,
        guest_session_id: str | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MovieRatingDeleteResponse:
        """
        Delete a user rating.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/3/movie/{movie_id}/rating",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "guest_session_id": guest_session_id,
                        "session_id": session_id,
                    },
                    movie_rating_delete_params.MovieRatingDeleteParams,
                ),
            ),
            cast_to=MovieRatingDeleteResponse,
        )

    def search(
        self,
        *,
        query: str,
        include_adult: bool | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        primary_release_year: str | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        year: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MovieSearchResponse:
        """
        Search for movies by their original, translated and alternative titles.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/3/search/movie",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query": query,
                        "include_adult": include_adult,
                        "language": language,
                        "page": page,
                        "primary_release_year": primary_release_year,
                        "region": region,
                        "year": year,
                    },
                    movie_search_params.MovieSearchParams,
                ),
            ),
            cast_to=MovieSearchResponse,
        )


class AsyncMoviesResource(AsyncAPIResource):
    @cached_property
    def images(self) -> AsyncImagesResource:
        return AsyncImagesResource(self._client)

    @cached_property
    def account_states(self) -> AsyncAccountStatesResource:
        return AsyncAccountStatesResource(self._client)

    @cached_property
    def alternative_titles(self) -> AsyncAlternativeTitlesResource:
        return AsyncAlternativeTitlesResource(self._client)

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
    def keywords(self) -> AsyncKeywordsResource:
        return AsyncKeywordsResource(self._client)

    @cached_property
    def lists(self) -> AsyncListsResource:
        return AsyncListsResource(self._client)

    @cached_property
    def recommendations(self) -> AsyncRecommendationsResource:
        return AsyncRecommendationsResource(self._client)

    @cached_property
    def release_dates(self) -> AsyncReleaseDatesResource:
        return AsyncReleaseDatesResource(self._client)

    @cached_property
    def reviews(self) -> AsyncReviewsResource:
        return AsyncReviewsResource(self._client)

    @cached_property
    def similar(self) -> AsyncSimilarResource:
        return AsyncSimilarResource(self._client)

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
    def popular(self) -> AsyncPopularResource:
        return AsyncPopularResource(self._client)

    @cached_property
    def top_rated(self) -> AsyncTopRatedResource:
        return AsyncTopRatedResource(self._client)

    @cached_property
    def upcoming(self) -> AsyncUpcomingResource:
        return AsyncUpcomingResource(self._client)

    @cached_property
    def now_playing(self) -> AsyncNowPlayingResource:
        return AsyncNowPlayingResource(self._client)

    @cached_property
    def latest(self) -> AsyncLatestResource:
        return AsyncLatestResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMoviesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMoviesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMoviesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncMoviesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        movie_id: int,
        *,
        append_to_response: str | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MovieRetrieveResponse:
        """
        Get the top level details of a movie by ID.

        Args:
          append_to_response: comma separated list of endpoints within this namespace, 20 items max

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/3/movie/{movie_id}",
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
                    movie_retrieve_params.MovieRetrieveParams,
                ),
            ),
            cast_to=MovieRetrieveResponse,
        )

    async def discover(
        self,
        *,
        certification: movie_discover_params.Certification | NotGiven = NOT_GIVEN,
        certification_country: str | NotGiven = NOT_GIVEN,
        include_adult: bool | NotGiven = NOT_GIVEN,
        include_video: bool | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        primary_release_date: movie_discover_params.PrimaryReleaseDate | NotGiven = NOT_GIVEN,
        primary_release_year: int | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        release_date: movie_discover_params.ReleaseDate | NotGiven = NOT_GIVEN,
        sort_by: Literal[
            "original_title.asc",
            "original_title.desc",
            "popularity.asc",
            "popularity.desc",
            "revenue.asc",
            "revenue.desc",
            "primary_release_date.asc",
            "title.asc",
            "title.desc",
            "primary_release_date.desc",
            "vote_average.asc",
            "vote_average.desc",
            "vote_count.asc",
            "vote_count.desc",
        ]
        | NotGiven = NOT_GIVEN,
        vote_average: movie_discover_params.VoteAverage | NotGiven = NOT_GIVEN,
        vote_count: movie_discover_params.VoteCount | NotGiven = NOT_GIVEN,
        watch_region: str | NotGiven = NOT_GIVEN,
        with_cast: str | NotGiven = NOT_GIVEN,
        with_companies: str | NotGiven = NOT_GIVEN,
        with_crew: str | NotGiven = NOT_GIVEN,
        with_genres: str | NotGiven = NOT_GIVEN,
        with_keywords: str | NotGiven = NOT_GIVEN,
        with_origin_country: str | NotGiven = NOT_GIVEN,
        with_original_language: str | NotGiven = NOT_GIVEN,
        with_people: str | NotGiven = NOT_GIVEN,
        with_release_type: int | NotGiven = NOT_GIVEN,
        with_runtime: movie_discover_params.WithRuntime | NotGiven = NOT_GIVEN,
        with_watch_monetization_types: str | NotGiven = NOT_GIVEN,
        with_watch_providers: str | NotGiven = NOT_GIVEN,
        without_companies: str | NotGiven = NOT_GIVEN,
        without_genres: str | NotGiven = NOT_GIVEN,
        without_keywords: str | NotGiven = NOT_GIVEN,
        without_watch_providers: str | NotGiven = NOT_GIVEN,
        year: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MovieDiscoverResponse:
        """
        Find movies using over 30 filters and sort options.

        Args:
          certification_country: use in conjunction with the `certification`, `certification.gte` and
              `certification.lte` filters

          watch_region: use in conjunction with `with_watch_monetization_types ` or
              `with_watch_providers `

          with_cast: can be a comma (`AND`) or pipe (`OR`) separated query

          with_companies: can be a comma (`AND`) or pipe (`OR`) separated query

          with_crew: can be a comma (`AND`) or pipe (`OR`) separated query

          with_genres: can be a comma (`AND`) or pipe (`OR`) separated query

          with_keywords: can be a comma (`AND`) or pipe (`OR`) separated query

          with_people: can be a comma (`AND`) or pipe (`OR`) separated query

          with_release_type: possible values are: [1, 2, 3, 4, 5, 6] can be a comma (`AND`) or pipe (`OR`)
              separated query, can be used in conjunction with `region`

          with_watch_monetization_types: possible values are: [flatrate, free, ads, rent, buy] use in conjunction with
              `watch_region`, can be a comma (`AND`) or pipe (`OR`) separated query

          with_watch_providers: use in conjunction with `watch_region`, can be a comma (`AND`) or pipe (`OR`)
              separated query

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/3/discover/movie",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "certification": certification,
                        "certification_country": certification_country,
                        "include_adult": include_adult,
                        "include_video": include_video,
                        "language": language,
                        "page": page,
                        "primary_release_date": primary_release_date,
                        "primary_release_year": primary_release_year,
                        "region": region,
                        "release_date": release_date,
                        "sort_by": sort_by,
                        "vote_average": vote_average,
                        "vote_count": vote_count,
                        "watch_region": watch_region,
                        "with_cast": with_cast,
                        "with_companies": with_companies,
                        "with_crew": with_crew,
                        "with_genres": with_genres,
                        "with_keywords": with_keywords,
                        "with_origin_country": with_origin_country,
                        "with_original_language": with_original_language,
                        "with_people": with_people,
                        "with_release_type": with_release_type,
                        "with_runtime": with_runtime,
                        "with_watch_monetization_types": with_watch_monetization_types,
                        "with_watch_providers": with_watch_providers,
                        "without_companies": without_companies,
                        "without_genres": without_genres,
                        "without_keywords": without_keywords,
                        "without_watch_providers": without_watch_providers,
                        "year": year,
                    },
                    movie_discover_params.MovieDiscoverParams,
                ),
            ),
            cast_to=MovieDiscoverResponse,
        )

    async def rating(
        self,
        movie_id: int,
        *,
        raw_body: str,
        guest_session_id: str | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MovieRatingResponse:
        """
        Rate a movie and save it to your rated list.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/3/movie/{movie_id}/rating",
            body=await async_maybe_transform({"raw_body": raw_body}, movie_rating_params.MovieRatingParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "guest_session_id": guest_session_id,
                        "session_id": session_id,
                    },
                    movie_rating_params.MovieRatingParams,
                ),
            ),
            cast_to=MovieRatingResponse,
        )

    async def rating_delete(
        self,
        movie_id: int,
        *,
        guest_session_id: str | NotGiven = NOT_GIVEN,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MovieRatingDeleteResponse:
        """
        Delete a user rating.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/3/movie/{movie_id}/rating",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "guest_session_id": guest_session_id,
                        "session_id": session_id,
                    },
                    movie_rating_delete_params.MovieRatingDeleteParams,
                ),
            ),
            cast_to=MovieRatingDeleteResponse,
        )

    async def search(
        self,
        *,
        query: str,
        include_adult: bool | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        primary_release_year: str | NotGiven = NOT_GIVEN,
        region: str | NotGiven = NOT_GIVEN,
        year: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> MovieSearchResponse:
        """
        Search for movies by their original, translated and alternative titles.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/3/search/movie",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query": query,
                        "include_adult": include_adult,
                        "language": language,
                        "page": page,
                        "primary_release_year": primary_release_year,
                        "region": region,
                        "year": year,
                    },
                    movie_search_params.MovieSearchParams,
                ),
            ),
            cast_to=MovieSearchResponse,
        )


class MoviesResourceWithRawResponse:
    def __init__(self, movies: MoviesResource) -> None:
        self._movies = movies

        self.retrieve = to_raw_response_wrapper(
            movies.retrieve,
        )
        self.discover = to_raw_response_wrapper(
            movies.discover,
        )
        self.rating = to_raw_response_wrapper(
            movies.rating,
        )
        self.rating_delete = to_raw_response_wrapper(
            movies.rating_delete,
        )
        self.search = to_raw_response_wrapper(
            movies.search,
        )

    @cached_property
    def images(self) -> ImagesResourceWithRawResponse:
        return ImagesResourceWithRawResponse(self._movies.images)

    @cached_property
    def account_states(self) -> AccountStatesResourceWithRawResponse:
        return AccountStatesResourceWithRawResponse(self._movies.account_states)

    @cached_property
    def alternative_titles(self) -> AlternativeTitlesResourceWithRawResponse:
        return AlternativeTitlesResourceWithRawResponse(self._movies.alternative_titles)

    @cached_property
    def changes(self) -> ChangesResourceWithRawResponse:
        return ChangesResourceWithRawResponse(self._movies.changes)

    @cached_property
    def credits(self) -> CreditsResourceWithRawResponse:
        return CreditsResourceWithRawResponse(self._movies.credits)

    @cached_property
    def external_ids(self) -> ExternalIDsResourceWithRawResponse:
        return ExternalIDsResourceWithRawResponse(self._movies.external_ids)

    @cached_property
    def keywords(self) -> KeywordsResourceWithRawResponse:
        return KeywordsResourceWithRawResponse(self._movies.keywords)

    @cached_property
    def lists(self) -> ListsResourceWithRawResponse:
        return ListsResourceWithRawResponse(self._movies.lists)

    @cached_property
    def recommendations(self) -> RecommendationsResourceWithRawResponse:
        return RecommendationsResourceWithRawResponse(self._movies.recommendations)

    @cached_property
    def release_dates(self) -> ReleaseDatesResourceWithRawResponse:
        return ReleaseDatesResourceWithRawResponse(self._movies.release_dates)

    @cached_property
    def reviews(self) -> ReviewsResourceWithRawResponse:
        return ReviewsResourceWithRawResponse(self._movies.reviews)

    @cached_property
    def similar(self) -> SimilarResourceWithRawResponse:
        return SimilarResourceWithRawResponse(self._movies.similar)

    @cached_property
    def translations(self) -> TranslationsResourceWithRawResponse:
        return TranslationsResourceWithRawResponse(self._movies.translations)

    @cached_property
    def videos(self) -> VideosResourceWithRawResponse:
        return VideosResourceWithRawResponse(self._movies.videos)

    @cached_property
    def watch_providers(self) -> WatchProvidersResourceWithRawResponse:
        return WatchProvidersResourceWithRawResponse(self._movies.watch_providers)

    @cached_property
    def popular(self) -> PopularResourceWithRawResponse:
        return PopularResourceWithRawResponse(self._movies.popular)

    @cached_property
    def top_rated(self) -> TopRatedResourceWithRawResponse:
        return TopRatedResourceWithRawResponse(self._movies.top_rated)

    @cached_property
    def upcoming(self) -> UpcomingResourceWithRawResponse:
        return UpcomingResourceWithRawResponse(self._movies.upcoming)

    @cached_property
    def now_playing(self) -> NowPlayingResourceWithRawResponse:
        return NowPlayingResourceWithRawResponse(self._movies.now_playing)

    @cached_property
    def latest(self) -> LatestResourceWithRawResponse:
        return LatestResourceWithRawResponse(self._movies.latest)


class AsyncMoviesResourceWithRawResponse:
    def __init__(self, movies: AsyncMoviesResource) -> None:
        self._movies = movies

        self.retrieve = async_to_raw_response_wrapper(
            movies.retrieve,
        )
        self.discover = async_to_raw_response_wrapper(
            movies.discover,
        )
        self.rating = async_to_raw_response_wrapper(
            movies.rating,
        )
        self.rating_delete = async_to_raw_response_wrapper(
            movies.rating_delete,
        )
        self.search = async_to_raw_response_wrapper(
            movies.search,
        )

    @cached_property
    def images(self) -> AsyncImagesResourceWithRawResponse:
        return AsyncImagesResourceWithRawResponse(self._movies.images)

    @cached_property
    def account_states(self) -> AsyncAccountStatesResourceWithRawResponse:
        return AsyncAccountStatesResourceWithRawResponse(self._movies.account_states)

    @cached_property
    def alternative_titles(self) -> AsyncAlternativeTitlesResourceWithRawResponse:
        return AsyncAlternativeTitlesResourceWithRawResponse(self._movies.alternative_titles)

    @cached_property
    def changes(self) -> AsyncChangesResourceWithRawResponse:
        return AsyncChangesResourceWithRawResponse(self._movies.changes)

    @cached_property
    def credits(self) -> AsyncCreditsResourceWithRawResponse:
        return AsyncCreditsResourceWithRawResponse(self._movies.credits)

    @cached_property
    def external_ids(self) -> AsyncExternalIDsResourceWithRawResponse:
        return AsyncExternalIDsResourceWithRawResponse(self._movies.external_ids)

    @cached_property
    def keywords(self) -> AsyncKeywordsResourceWithRawResponse:
        return AsyncKeywordsResourceWithRawResponse(self._movies.keywords)

    @cached_property
    def lists(self) -> AsyncListsResourceWithRawResponse:
        return AsyncListsResourceWithRawResponse(self._movies.lists)

    @cached_property
    def recommendations(self) -> AsyncRecommendationsResourceWithRawResponse:
        return AsyncRecommendationsResourceWithRawResponse(self._movies.recommendations)

    @cached_property
    def release_dates(self) -> AsyncReleaseDatesResourceWithRawResponse:
        return AsyncReleaseDatesResourceWithRawResponse(self._movies.release_dates)

    @cached_property
    def reviews(self) -> AsyncReviewsResourceWithRawResponse:
        return AsyncReviewsResourceWithRawResponse(self._movies.reviews)

    @cached_property
    def similar(self) -> AsyncSimilarResourceWithRawResponse:
        return AsyncSimilarResourceWithRawResponse(self._movies.similar)

    @cached_property
    def translations(self) -> AsyncTranslationsResourceWithRawResponse:
        return AsyncTranslationsResourceWithRawResponse(self._movies.translations)

    @cached_property
    def videos(self) -> AsyncVideosResourceWithRawResponse:
        return AsyncVideosResourceWithRawResponse(self._movies.videos)

    @cached_property
    def watch_providers(self) -> AsyncWatchProvidersResourceWithRawResponse:
        return AsyncWatchProvidersResourceWithRawResponse(self._movies.watch_providers)

    @cached_property
    def popular(self) -> AsyncPopularResourceWithRawResponse:
        return AsyncPopularResourceWithRawResponse(self._movies.popular)

    @cached_property
    def top_rated(self) -> AsyncTopRatedResourceWithRawResponse:
        return AsyncTopRatedResourceWithRawResponse(self._movies.top_rated)

    @cached_property
    def upcoming(self) -> AsyncUpcomingResourceWithRawResponse:
        return AsyncUpcomingResourceWithRawResponse(self._movies.upcoming)

    @cached_property
    def now_playing(self) -> AsyncNowPlayingResourceWithRawResponse:
        return AsyncNowPlayingResourceWithRawResponse(self._movies.now_playing)

    @cached_property
    def latest(self) -> AsyncLatestResourceWithRawResponse:
        return AsyncLatestResourceWithRawResponse(self._movies.latest)


class MoviesResourceWithStreamingResponse:
    def __init__(self, movies: MoviesResource) -> None:
        self._movies = movies

        self.retrieve = to_streamed_response_wrapper(
            movies.retrieve,
        )
        self.discover = to_streamed_response_wrapper(
            movies.discover,
        )
        self.rating = to_streamed_response_wrapper(
            movies.rating,
        )
        self.rating_delete = to_streamed_response_wrapper(
            movies.rating_delete,
        )
        self.search = to_streamed_response_wrapper(
            movies.search,
        )

    @cached_property
    def images(self) -> ImagesResourceWithStreamingResponse:
        return ImagesResourceWithStreamingResponse(self._movies.images)

    @cached_property
    def account_states(self) -> AccountStatesResourceWithStreamingResponse:
        return AccountStatesResourceWithStreamingResponse(self._movies.account_states)

    @cached_property
    def alternative_titles(self) -> AlternativeTitlesResourceWithStreamingResponse:
        return AlternativeTitlesResourceWithStreamingResponse(self._movies.alternative_titles)

    @cached_property
    def changes(self) -> ChangesResourceWithStreamingResponse:
        return ChangesResourceWithStreamingResponse(self._movies.changes)

    @cached_property
    def credits(self) -> CreditsResourceWithStreamingResponse:
        return CreditsResourceWithStreamingResponse(self._movies.credits)

    @cached_property
    def external_ids(self) -> ExternalIDsResourceWithStreamingResponse:
        return ExternalIDsResourceWithStreamingResponse(self._movies.external_ids)

    @cached_property
    def keywords(self) -> KeywordsResourceWithStreamingResponse:
        return KeywordsResourceWithStreamingResponse(self._movies.keywords)

    @cached_property
    def lists(self) -> ListsResourceWithStreamingResponse:
        return ListsResourceWithStreamingResponse(self._movies.lists)

    @cached_property
    def recommendations(self) -> RecommendationsResourceWithStreamingResponse:
        return RecommendationsResourceWithStreamingResponse(self._movies.recommendations)

    @cached_property
    def release_dates(self) -> ReleaseDatesResourceWithStreamingResponse:
        return ReleaseDatesResourceWithStreamingResponse(self._movies.release_dates)

    @cached_property
    def reviews(self) -> ReviewsResourceWithStreamingResponse:
        return ReviewsResourceWithStreamingResponse(self._movies.reviews)

    @cached_property
    def similar(self) -> SimilarResourceWithStreamingResponse:
        return SimilarResourceWithStreamingResponse(self._movies.similar)

    @cached_property
    def translations(self) -> TranslationsResourceWithStreamingResponse:
        return TranslationsResourceWithStreamingResponse(self._movies.translations)

    @cached_property
    def videos(self) -> VideosResourceWithStreamingResponse:
        return VideosResourceWithStreamingResponse(self._movies.videos)

    @cached_property
    def watch_providers(self) -> WatchProvidersResourceWithStreamingResponse:
        return WatchProvidersResourceWithStreamingResponse(self._movies.watch_providers)

    @cached_property
    def popular(self) -> PopularResourceWithStreamingResponse:
        return PopularResourceWithStreamingResponse(self._movies.popular)

    @cached_property
    def top_rated(self) -> TopRatedResourceWithStreamingResponse:
        return TopRatedResourceWithStreamingResponse(self._movies.top_rated)

    @cached_property
    def upcoming(self) -> UpcomingResourceWithStreamingResponse:
        return UpcomingResourceWithStreamingResponse(self._movies.upcoming)

    @cached_property
    def now_playing(self) -> NowPlayingResourceWithStreamingResponse:
        return NowPlayingResourceWithStreamingResponse(self._movies.now_playing)

    @cached_property
    def latest(self) -> LatestResourceWithStreamingResponse:
        return LatestResourceWithStreamingResponse(self._movies.latest)


class AsyncMoviesResourceWithStreamingResponse:
    def __init__(self, movies: AsyncMoviesResource) -> None:
        self._movies = movies

        self.retrieve = async_to_streamed_response_wrapper(
            movies.retrieve,
        )
        self.discover = async_to_streamed_response_wrapper(
            movies.discover,
        )
        self.rating = async_to_streamed_response_wrapper(
            movies.rating,
        )
        self.rating_delete = async_to_streamed_response_wrapper(
            movies.rating_delete,
        )
        self.search = async_to_streamed_response_wrapper(
            movies.search,
        )

    @cached_property
    def images(self) -> AsyncImagesResourceWithStreamingResponse:
        return AsyncImagesResourceWithStreamingResponse(self._movies.images)

    @cached_property
    def account_states(self) -> AsyncAccountStatesResourceWithStreamingResponse:
        return AsyncAccountStatesResourceWithStreamingResponse(self._movies.account_states)

    @cached_property
    def alternative_titles(self) -> AsyncAlternativeTitlesResourceWithStreamingResponse:
        return AsyncAlternativeTitlesResourceWithStreamingResponse(self._movies.alternative_titles)

    @cached_property
    def changes(self) -> AsyncChangesResourceWithStreamingResponse:
        return AsyncChangesResourceWithStreamingResponse(self._movies.changes)

    @cached_property
    def credits(self) -> AsyncCreditsResourceWithStreamingResponse:
        return AsyncCreditsResourceWithStreamingResponse(self._movies.credits)

    @cached_property
    def external_ids(self) -> AsyncExternalIDsResourceWithStreamingResponse:
        return AsyncExternalIDsResourceWithStreamingResponse(self._movies.external_ids)

    @cached_property
    def keywords(self) -> AsyncKeywordsResourceWithStreamingResponse:
        return AsyncKeywordsResourceWithStreamingResponse(self._movies.keywords)

    @cached_property
    def lists(self) -> AsyncListsResourceWithStreamingResponse:
        return AsyncListsResourceWithStreamingResponse(self._movies.lists)

    @cached_property
    def recommendations(self) -> AsyncRecommendationsResourceWithStreamingResponse:
        return AsyncRecommendationsResourceWithStreamingResponse(self._movies.recommendations)

    @cached_property
    def release_dates(self) -> AsyncReleaseDatesResourceWithStreamingResponse:
        return AsyncReleaseDatesResourceWithStreamingResponse(self._movies.release_dates)

    @cached_property
    def reviews(self) -> AsyncReviewsResourceWithStreamingResponse:
        return AsyncReviewsResourceWithStreamingResponse(self._movies.reviews)

    @cached_property
    def similar(self) -> AsyncSimilarResourceWithStreamingResponse:
        return AsyncSimilarResourceWithStreamingResponse(self._movies.similar)

    @cached_property
    def translations(self) -> AsyncTranslationsResourceWithStreamingResponse:
        return AsyncTranslationsResourceWithStreamingResponse(self._movies.translations)

    @cached_property
    def videos(self) -> AsyncVideosResourceWithStreamingResponse:
        return AsyncVideosResourceWithStreamingResponse(self._movies.videos)

    @cached_property
    def watch_providers(self) -> AsyncWatchProvidersResourceWithStreamingResponse:
        return AsyncWatchProvidersResourceWithStreamingResponse(self._movies.watch_providers)

    @cached_property
    def popular(self) -> AsyncPopularResourceWithStreamingResponse:
        return AsyncPopularResourceWithStreamingResponse(self._movies.popular)

    @cached_property
    def top_rated(self) -> AsyncTopRatedResourceWithStreamingResponse:
        return AsyncTopRatedResourceWithStreamingResponse(self._movies.top_rated)

    @cached_property
    def upcoming(self) -> AsyncUpcomingResourceWithStreamingResponse:
        return AsyncUpcomingResourceWithStreamingResponse(self._movies.upcoming)

    @cached_property
    def now_playing(self) -> AsyncNowPlayingResourceWithStreamingResponse:
        return AsyncNowPlayingResourceWithStreamingResponse(self._movies.now_playing)

    @cached_property
    def latest(self) -> AsyncLatestResourceWithStreamingResponse:
        return AsyncLatestResourceWithStreamingResponse(self._movies.latest)
