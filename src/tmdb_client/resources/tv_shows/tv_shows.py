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
from .rating import (
    RatingResource,
    AsyncRatingResource,
    RatingResourceWithRawResponse,
    AsyncRatingResourceWithRawResponse,
    RatingResourceWithStreamingResponse,
    AsyncRatingResourceWithStreamingResponse,
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
from .keywords import (
    KeywordsResource,
    AsyncKeywordsResource,
    KeywordsResourceWithRawResponse,
    AsyncKeywordsResourceWithRawResponse,
    KeywordsResourceWithStreamingResponse,
    AsyncKeywordsResourceWithStreamingResponse,
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
from .on_the_air import (
    OnTheAirResource,
    AsyncOnTheAirResource,
    OnTheAirResourceWithRawResponse,
    AsyncOnTheAirResourceWithRawResponse,
    OnTheAirResourceWithStreamingResponse,
    AsyncOnTheAirResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from .airing_today import (
    AiringTodayResource,
    AsyncAiringTodayResource,
    AiringTodayResourceWithRawResponse,
    AsyncAiringTodayResourceWithRawResponse,
    AiringTodayResourceWithStreamingResponse,
    AsyncAiringTodayResourceWithStreamingResponse,
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
from .episode_groups import (
    EpisodeGroupsResource,
    AsyncEpisodeGroupsResource,
    EpisodeGroupsResourceWithRawResponse,
    AsyncEpisodeGroupsResourceWithRawResponse,
    EpisodeGroupsResourceWithStreamingResponse,
    AsyncEpisodeGroupsResourceWithStreamingResponse,
)
from .content_ratings import (
    ContentRatingsResource,
    AsyncContentRatingsResource,
    ContentRatingsResourceWithRawResponse,
    AsyncContentRatingsResourceWithRawResponse,
    ContentRatingsResourceWithStreamingResponse,
    AsyncContentRatingsResourceWithStreamingResponse,
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
from .aggregate_credits import (
    AggregateCreditsResource,
    AsyncAggregateCreditsResource,
    AggregateCreditsResourceWithRawResponse,
    AsyncAggregateCreditsResourceWithRawResponse,
    AggregateCreditsResourceWithStreamingResponse,
    AsyncAggregateCreditsResourceWithStreamingResponse,
)
from .alternative_titles import (
    AlternativeTitlesResource,
    AsyncAlternativeTitlesResource,
    AlternativeTitlesResourceWithRawResponse,
    AsyncAlternativeTitlesResourceWithRawResponse,
    AlternativeTitlesResourceWithStreamingResponse,
    AsyncAlternativeTitlesResourceWithStreamingResponse,
)
from .screened_theatrically import (
    ScreenedTheatricallyResource,
    AsyncScreenedTheatricallyResource,
    ScreenedTheatricallyResourceWithRawResponse,
    AsyncScreenedTheatricallyResourceWithRawResponse,
    ScreenedTheatricallyResourceWithStreamingResponse,
    AsyncScreenedTheatricallyResourceWithStreamingResponse,
)

__all__ = ["TvShowsResource", "AsyncTvShowsResource"]


class TvShowsResource(SyncAPIResource):
    @cached_property
    def changes(self) -> ChangesResource:
        return ChangesResource(self._client)

    @cached_property
    def airing_today(self) -> AiringTodayResource:
        return AiringTodayResource(self._client)

    @cached_property
    def on_the_air(self) -> OnTheAirResource:
        return OnTheAirResource(self._client)

    @cached_property
    def popular(self) -> PopularResource:
        return PopularResource(self._client)

    @cached_property
    def top_rated(self) -> TopRatedResource:
        return TopRatedResource(self._client)

    @cached_property
    def latest(self) -> LatestResource:
        return LatestResource(self._client)

    @cached_property
    def aggregate_credits(self) -> AggregateCreditsResource:
        return AggregateCreditsResource(self._client)

    @cached_property
    def alternative_titles(self) -> AlternativeTitlesResource:
        return AlternativeTitlesResource(self._client)

    @cached_property
    def content_ratings(self) -> ContentRatingsResource:
        return ContentRatingsResource(self._client)

    @cached_property
    def credits(self) -> CreditsResource:
        return CreditsResource(self._client)

    @cached_property
    def episode_groups(self) -> EpisodeGroupsResource:
        return EpisodeGroupsResource(self._client)

    @cached_property
    def external_ids(self) -> ExternalIDsResource:
        return ExternalIDsResource(self._client)

    @cached_property
    def keywords(self) -> KeywordsResource:
        return KeywordsResource(self._client)

    @cached_property
    def recommendations(self) -> RecommendationsResource:
        return RecommendationsResource(self._client)

    @cached_property
    def reviews(self) -> ReviewsResource:
        return ReviewsResource(self._client)

    @cached_property
    def screened_theatrically(self) -> ScreenedTheatricallyResource:
        return ScreenedTheatricallyResource(self._client)

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
    def rating(self) -> RatingResource:
        return RatingResource(self._client)

    @cached_property
    def with_raw_response(self) -> TvShowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return TvShowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TvShowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return TvShowsResourceWithStreamingResponse(self)


class AsyncTvShowsResource(AsyncAPIResource):
    @cached_property
    def changes(self) -> AsyncChangesResource:
        return AsyncChangesResource(self._client)

    @cached_property
    def airing_today(self) -> AsyncAiringTodayResource:
        return AsyncAiringTodayResource(self._client)

    @cached_property
    def on_the_air(self) -> AsyncOnTheAirResource:
        return AsyncOnTheAirResource(self._client)

    @cached_property
    def popular(self) -> AsyncPopularResource:
        return AsyncPopularResource(self._client)

    @cached_property
    def top_rated(self) -> AsyncTopRatedResource:
        return AsyncTopRatedResource(self._client)

    @cached_property
    def latest(self) -> AsyncLatestResource:
        return AsyncLatestResource(self._client)

    @cached_property
    def aggregate_credits(self) -> AsyncAggregateCreditsResource:
        return AsyncAggregateCreditsResource(self._client)

    @cached_property
    def alternative_titles(self) -> AsyncAlternativeTitlesResource:
        return AsyncAlternativeTitlesResource(self._client)

    @cached_property
    def content_ratings(self) -> AsyncContentRatingsResource:
        return AsyncContentRatingsResource(self._client)

    @cached_property
    def credits(self) -> AsyncCreditsResource:
        return AsyncCreditsResource(self._client)

    @cached_property
    def episode_groups(self) -> AsyncEpisodeGroupsResource:
        return AsyncEpisodeGroupsResource(self._client)

    @cached_property
    def external_ids(self) -> AsyncExternalIDsResource:
        return AsyncExternalIDsResource(self._client)

    @cached_property
    def keywords(self) -> AsyncKeywordsResource:
        return AsyncKeywordsResource(self._client)

    @cached_property
    def recommendations(self) -> AsyncRecommendationsResource:
        return AsyncRecommendationsResource(self._client)

    @cached_property
    def reviews(self) -> AsyncReviewsResource:
        return AsyncReviewsResource(self._client)

    @cached_property
    def screened_theatrically(self) -> AsyncScreenedTheatricallyResource:
        return AsyncScreenedTheatricallyResource(self._client)

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
    def rating(self) -> AsyncRatingResource:
        return AsyncRatingResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTvShowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTvShowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTvShowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return AsyncTvShowsResourceWithStreamingResponse(self)


class TvShowsResourceWithRawResponse:
    def __init__(self, tv_shows: TvShowsResource) -> None:
        self._tv_shows = tv_shows

    @cached_property
    def changes(self) -> ChangesResourceWithRawResponse:
        return ChangesResourceWithRawResponse(self._tv_shows.changes)

    @cached_property
    def airing_today(self) -> AiringTodayResourceWithRawResponse:
        return AiringTodayResourceWithRawResponse(self._tv_shows.airing_today)

    @cached_property
    def on_the_air(self) -> OnTheAirResourceWithRawResponse:
        return OnTheAirResourceWithRawResponse(self._tv_shows.on_the_air)

    @cached_property
    def popular(self) -> PopularResourceWithRawResponse:
        return PopularResourceWithRawResponse(self._tv_shows.popular)

    @cached_property
    def top_rated(self) -> TopRatedResourceWithRawResponse:
        return TopRatedResourceWithRawResponse(self._tv_shows.top_rated)

    @cached_property
    def latest(self) -> LatestResourceWithRawResponse:
        return LatestResourceWithRawResponse(self._tv_shows.latest)

    @cached_property
    def aggregate_credits(self) -> AggregateCreditsResourceWithRawResponse:
        return AggregateCreditsResourceWithRawResponse(self._tv_shows.aggregate_credits)

    @cached_property
    def alternative_titles(self) -> AlternativeTitlesResourceWithRawResponse:
        return AlternativeTitlesResourceWithRawResponse(self._tv_shows.alternative_titles)

    @cached_property
    def content_ratings(self) -> ContentRatingsResourceWithRawResponse:
        return ContentRatingsResourceWithRawResponse(self._tv_shows.content_ratings)

    @cached_property
    def credits(self) -> CreditsResourceWithRawResponse:
        return CreditsResourceWithRawResponse(self._tv_shows.credits)

    @cached_property
    def episode_groups(self) -> EpisodeGroupsResourceWithRawResponse:
        return EpisodeGroupsResourceWithRawResponse(self._tv_shows.episode_groups)

    @cached_property
    def external_ids(self) -> ExternalIDsResourceWithRawResponse:
        return ExternalIDsResourceWithRawResponse(self._tv_shows.external_ids)

    @cached_property
    def keywords(self) -> KeywordsResourceWithRawResponse:
        return KeywordsResourceWithRawResponse(self._tv_shows.keywords)

    @cached_property
    def recommendations(self) -> RecommendationsResourceWithRawResponse:
        return RecommendationsResourceWithRawResponse(self._tv_shows.recommendations)

    @cached_property
    def reviews(self) -> ReviewsResourceWithRawResponse:
        return ReviewsResourceWithRawResponse(self._tv_shows.reviews)

    @cached_property
    def screened_theatrically(self) -> ScreenedTheatricallyResourceWithRawResponse:
        return ScreenedTheatricallyResourceWithRawResponse(self._tv_shows.screened_theatrically)

    @cached_property
    def similar(self) -> SimilarResourceWithRawResponse:
        return SimilarResourceWithRawResponse(self._tv_shows.similar)

    @cached_property
    def translations(self) -> TranslationsResourceWithRawResponse:
        return TranslationsResourceWithRawResponse(self._tv_shows.translations)

    @cached_property
    def videos(self) -> VideosResourceWithRawResponse:
        return VideosResourceWithRawResponse(self._tv_shows.videos)

    @cached_property
    def watch_providers(self) -> WatchProvidersResourceWithRawResponse:
        return WatchProvidersResourceWithRawResponse(self._tv_shows.watch_providers)

    @cached_property
    def rating(self) -> RatingResourceWithRawResponse:
        return RatingResourceWithRawResponse(self._tv_shows.rating)


class AsyncTvShowsResourceWithRawResponse:
    def __init__(self, tv_shows: AsyncTvShowsResource) -> None:
        self._tv_shows = tv_shows

    @cached_property
    def changes(self) -> AsyncChangesResourceWithRawResponse:
        return AsyncChangesResourceWithRawResponse(self._tv_shows.changes)

    @cached_property
    def airing_today(self) -> AsyncAiringTodayResourceWithRawResponse:
        return AsyncAiringTodayResourceWithRawResponse(self._tv_shows.airing_today)

    @cached_property
    def on_the_air(self) -> AsyncOnTheAirResourceWithRawResponse:
        return AsyncOnTheAirResourceWithRawResponse(self._tv_shows.on_the_air)

    @cached_property
    def popular(self) -> AsyncPopularResourceWithRawResponse:
        return AsyncPopularResourceWithRawResponse(self._tv_shows.popular)

    @cached_property
    def top_rated(self) -> AsyncTopRatedResourceWithRawResponse:
        return AsyncTopRatedResourceWithRawResponse(self._tv_shows.top_rated)

    @cached_property
    def latest(self) -> AsyncLatestResourceWithRawResponse:
        return AsyncLatestResourceWithRawResponse(self._tv_shows.latest)

    @cached_property
    def aggregate_credits(self) -> AsyncAggregateCreditsResourceWithRawResponse:
        return AsyncAggregateCreditsResourceWithRawResponse(self._tv_shows.aggregate_credits)

    @cached_property
    def alternative_titles(self) -> AsyncAlternativeTitlesResourceWithRawResponse:
        return AsyncAlternativeTitlesResourceWithRawResponse(self._tv_shows.alternative_titles)

    @cached_property
    def content_ratings(self) -> AsyncContentRatingsResourceWithRawResponse:
        return AsyncContentRatingsResourceWithRawResponse(self._tv_shows.content_ratings)

    @cached_property
    def credits(self) -> AsyncCreditsResourceWithRawResponse:
        return AsyncCreditsResourceWithRawResponse(self._tv_shows.credits)

    @cached_property
    def episode_groups(self) -> AsyncEpisodeGroupsResourceWithRawResponse:
        return AsyncEpisodeGroupsResourceWithRawResponse(self._tv_shows.episode_groups)

    @cached_property
    def external_ids(self) -> AsyncExternalIDsResourceWithRawResponse:
        return AsyncExternalIDsResourceWithRawResponse(self._tv_shows.external_ids)

    @cached_property
    def keywords(self) -> AsyncKeywordsResourceWithRawResponse:
        return AsyncKeywordsResourceWithRawResponse(self._tv_shows.keywords)

    @cached_property
    def recommendations(self) -> AsyncRecommendationsResourceWithRawResponse:
        return AsyncRecommendationsResourceWithRawResponse(self._tv_shows.recommendations)

    @cached_property
    def reviews(self) -> AsyncReviewsResourceWithRawResponse:
        return AsyncReviewsResourceWithRawResponse(self._tv_shows.reviews)

    @cached_property
    def screened_theatrically(self) -> AsyncScreenedTheatricallyResourceWithRawResponse:
        return AsyncScreenedTheatricallyResourceWithRawResponse(self._tv_shows.screened_theatrically)

    @cached_property
    def similar(self) -> AsyncSimilarResourceWithRawResponse:
        return AsyncSimilarResourceWithRawResponse(self._tv_shows.similar)

    @cached_property
    def translations(self) -> AsyncTranslationsResourceWithRawResponse:
        return AsyncTranslationsResourceWithRawResponse(self._tv_shows.translations)

    @cached_property
    def videos(self) -> AsyncVideosResourceWithRawResponse:
        return AsyncVideosResourceWithRawResponse(self._tv_shows.videos)

    @cached_property
    def watch_providers(self) -> AsyncWatchProvidersResourceWithRawResponse:
        return AsyncWatchProvidersResourceWithRawResponse(self._tv_shows.watch_providers)

    @cached_property
    def rating(self) -> AsyncRatingResourceWithRawResponse:
        return AsyncRatingResourceWithRawResponse(self._tv_shows.rating)


class TvShowsResourceWithStreamingResponse:
    def __init__(self, tv_shows: TvShowsResource) -> None:
        self._tv_shows = tv_shows

    @cached_property
    def changes(self) -> ChangesResourceWithStreamingResponse:
        return ChangesResourceWithStreamingResponse(self._tv_shows.changes)

    @cached_property
    def airing_today(self) -> AiringTodayResourceWithStreamingResponse:
        return AiringTodayResourceWithStreamingResponse(self._tv_shows.airing_today)

    @cached_property
    def on_the_air(self) -> OnTheAirResourceWithStreamingResponse:
        return OnTheAirResourceWithStreamingResponse(self._tv_shows.on_the_air)

    @cached_property
    def popular(self) -> PopularResourceWithStreamingResponse:
        return PopularResourceWithStreamingResponse(self._tv_shows.popular)

    @cached_property
    def top_rated(self) -> TopRatedResourceWithStreamingResponse:
        return TopRatedResourceWithStreamingResponse(self._tv_shows.top_rated)

    @cached_property
    def latest(self) -> LatestResourceWithStreamingResponse:
        return LatestResourceWithStreamingResponse(self._tv_shows.latest)

    @cached_property
    def aggregate_credits(self) -> AggregateCreditsResourceWithStreamingResponse:
        return AggregateCreditsResourceWithStreamingResponse(self._tv_shows.aggregate_credits)

    @cached_property
    def alternative_titles(self) -> AlternativeTitlesResourceWithStreamingResponse:
        return AlternativeTitlesResourceWithStreamingResponse(self._tv_shows.alternative_titles)

    @cached_property
    def content_ratings(self) -> ContentRatingsResourceWithStreamingResponse:
        return ContentRatingsResourceWithStreamingResponse(self._tv_shows.content_ratings)

    @cached_property
    def credits(self) -> CreditsResourceWithStreamingResponse:
        return CreditsResourceWithStreamingResponse(self._tv_shows.credits)

    @cached_property
    def episode_groups(self) -> EpisodeGroupsResourceWithStreamingResponse:
        return EpisodeGroupsResourceWithStreamingResponse(self._tv_shows.episode_groups)

    @cached_property
    def external_ids(self) -> ExternalIDsResourceWithStreamingResponse:
        return ExternalIDsResourceWithStreamingResponse(self._tv_shows.external_ids)

    @cached_property
    def keywords(self) -> KeywordsResourceWithStreamingResponse:
        return KeywordsResourceWithStreamingResponse(self._tv_shows.keywords)

    @cached_property
    def recommendations(self) -> RecommendationsResourceWithStreamingResponse:
        return RecommendationsResourceWithStreamingResponse(self._tv_shows.recommendations)

    @cached_property
    def reviews(self) -> ReviewsResourceWithStreamingResponse:
        return ReviewsResourceWithStreamingResponse(self._tv_shows.reviews)

    @cached_property
    def screened_theatrically(self) -> ScreenedTheatricallyResourceWithStreamingResponse:
        return ScreenedTheatricallyResourceWithStreamingResponse(self._tv_shows.screened_theatrically)

    @cached_property
    def similar(self) -> SimilarResourceWithStreamingResponse:
        return SimilarResourceWithStreamingResponse(self._tv_shows.similar)

    @cached_property
    def translations(self) -> TranslationsResourceWithStreamingResponse:
        return TranslationsResourceWithStreamingResponse(self._tv_shows.translations)

    @cached_property
    def videos(self) -> VideosResourceWithStreamingResponse:
        return VideosResourceWithStreamingResponse(self._tv_shows.videos)

    @cached_property
    def watch_providers(self) -> WatchProvidersResourceWithStreamingResponse:
        return WatchProvidersResourceWithStreamingResponse(self._tv_shows.watch_providers)

    @cached_property
    def rating(self) -> RatingResourceWithStreamingResponse:
        return RatingResourceWithStreamingResponse(self._tv_shows.rating)


class AsyncTvShowsResourceWithStreamingResponse:
    def __init__(self, tv_shows: AsyncTvShowsResource) -> None:
        self._tv_shows = tv_shows

    @cached_property
    def changes(self) -> AsyncChangesResourceWithStreamingResponse:
        return AsyncChangesResourceWithStreamingResponse(self._tv_shows.changes)

    @cached_property
    def airing_today(self) -> AsyncAiringTodayResourceWithStreamingResponse:
        return AsyncAiringTodayResourceWithStreamingResponse(self._tv_shows.airing_today)

    @cached_property
    def on_the_air(self) -> AsyncOnTheAirResourceWithStreamingResponse:
        return AsyncOnTheAirResourceWithStreamingResponse(self._tv_shows.on_the_air)

    @cached_property
    def popular(self) -> AsyncPopularResourceWithStreamingResponse:
        return AsyncPopularResourceWithStreamingResponse(self._tv_shows.popular)

    @cached_property
    def top_rated(self) -> AsyncTopRatedResourceWithStreamingResponse:
        return AsyncTopRatedResourceWithStreamingResponse(self._tv_shows.top_rated)

    @cached_property
    def latest(self) -> AsyncLatestResourceWithStreamingResponse:
        return AsyncLatestResourceWithStreamingResponse(self._tv_shows.latest)

    @cached_property
    def aggregate_credits(self) -> AsyncAggregateCreditsResourceWithStreamingResponse:
        return AsyncAggregateCreditsResourceWithStreamingResponse(self._tv_shows.aggregate_credits)

    @cached_property
    def alternative_titles(self) -> AsyncAlternativeTitlesResourceWithStreamingResponse:
        return AsyncAlternativeTitlesResourceWithStreamingResponse(self._tv_shows.alternative_titles)

    @cached_property
    def content_ratings(self) -> AsyncContentRatingsResourceWithStreamingResponse:
        return AsyncContentRatingsResourceWithStreamingResponse(self._tv_shows.content_ratings)

    @cached_property
    def credits(self) -> AsyncCreditsResourceWithStreamingResponse:
        return AsyncCreditsResourceWithStreamingResponse(self._tv_shows.credits)

    @cached_property
    def episode_groups(self) -> AsyncEpisodeGroupsResourceWithStreamingResponse:
        return AsyncEpisodeGroupsResourceWithStreamingResponse(self._tv_shows.episode_groups)

    @cached_property
    def external_ids(self) -> AsyncExternalIDsResourceWithStreamingResponse:
        return AsyncExternalIDsResourceWithStreamingResponse(self._tv_shows.external_ids)

    @cached_property
    def keywords(self) -> AsyncKeywordsResourceWithStreamingResponse:
        return AsyncKeywordsResourceWithStreamingResponse(self._tv_shows.keywords)

    @cached_property
    def recommendations(self) -> AsyncRecommendationsResourceWithStreamingResponse:
        return AsyncRecommendationsResourceWithStreamingResponse(self._tv_shows.recommendations)

    @cached_property
    def reviews(self) -> AsyncReviewsResourceWithStreamingResponse:
        return AsyncReviewsResourceWithStreamingResponse(self._tv_shows.reviews)

    @cached_property
    def screened_theatrically(self) -> AsyncScreenedTheatricallyResourceWithStreamingResponse:
        return AsyncScreenedTheatricallyResourceWithStreamingResponse(self._tv_shows.screened_theatrically)

    @cached_property
    def similar(self) -> AsyncSimilarResourceWithStreamingResponse:
        return AsyncSimilarResourceWithStreamingResponse(self._tv_shows.similar)

    @cached_property
    def translations(self) -> AsyncTranslationsResourceWithStreamingResponse:
        return AsyncTranslationsResourceWithStreamingResponse(self._tv_shows.translations)

    @cached_property
    def videos(self) -> AsyncVideosResourceWithStreamingResponse:
        return AsyncVideosResourceWithStreamingResponse(self._tv_shows.videos)

    @cached_property
    def watch_providers(self) -> AsyncWatchProvidersResourceWithStreamingResponse:
        return AsyncWatchProvidersResourceWithStreamingResponse(self._tv_shows.watch_providers)

    @cached_property
    def rating(self) -> AsyncRatingResourceWithStreamingResponse:
        return AsyncRatingResourceWithStreamingResponse(self._tv_shows.rating)
