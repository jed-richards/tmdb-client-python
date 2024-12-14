# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from .resources import (
    find,
    lists,
    search,
    credits,
    reviews,
    episodes,
    trending,
    tv_series,
    discover_tv,
    trending_movies,
    trending_people,
    trending_tv_shows,
)
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, TmdbClientError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.tv import tv
from .resources.genres import genres
from .resources.movies import movies
from .resources.people import people
from .resources.person import person
from .resources.accounts import accounts
from .resources.keywords import keywords
from .resources.networks import networks
from .resources.tv_shows import tv_shows
from .resources.companies import companies
from .resources.collections import collections
from .resources.configuration import configuration
from .resources.authentication import authentication
from .resources.certifications import certifications
from .resources.guest_sessions import guest_sessions
from .resources.watch_providers import watch_providers

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "TmdbClient",
    "AsyncTmdbClient",
    "Client",
    "AsyncClient",
]


class TmdbClient(SyncAPIClient):
    movies: movies.MoviesResource
    tv: tv.TvResource
    search: search.SearchResource
    people: people.PeopleResource
    configuration: configuration.ConfigurationResource
    discover_tv: discover_tv.DiscoverTvResource
    trending: trending.TrendingResource
    trending_movies: trending_movies.TrendingMoviesResource
    trending_tv_shows: trending_tv_shows.TrendingTvShowsResource
    episodes: episodes.EpisodesResource
    trending_people: trending_people.TrendingPeopleResource
    authentication: authentication.AuthenticationResource
    find: find.FindResource
    tv_shows: tv_shows.TvShowsResource
    accounts: accounts.AccountsResource
    certifications: certifications.CertificationsResource
    collections: collections.CollectionsResource
    companies: companies.CompaniesResource
    credits: credits.CreditsResource
    genres: genres.GenresResource
    guest_sessions: guest_sessions.GuestSessionsResource
    watch_providers: watch_providers.WatchProvidersResource
    keywords: keywords.KeywordsResource
    lists: lists.ListsResource
    networks: networks.NetworksResource
    reviews: reviews.ReviewsResource
    person: person.PersonResource
    tv_series: tv_series.TvSeriesResource
    with_raw_response: TmdbClientWithRawResponse
    with_streaming_response: TmdbClientWithStreamedResponse

    # client options
    bearer_token: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous tmdb-client client instance.

        This automatically infers the `bearer_token` argument from the `TMDB_API_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("TMDB_API_BEARER_TOKEN")
        if bearer_token is None:
            raise TmdbClientError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the TMDB_API_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("TMDB_CLIENT_BASE_URL")
        if base_url is None:
            base_url = f"https://api.themoviedb.org"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.movies = movies.MoviesResource(self)
        self.tv = tv.TvResource(self)
        self.search = search.SearchResource(self)
        self.people = people.PeopleResource(self)
        self.configuration = configuration.ConfigurationResource(self)
        self.discover_tv = discover_tv.DiscoverTvResource(self)
        self.trending = trending.TrendingResource(self)
        self.trending_movies = trending_movies.TrendingMoviesResource(self)
        self.trending_tv_shows = trending_tv_shows.TrendingTvShowsResource(self)
        self.episodes = episodes.EpisodesResource(self)
        self.trending_people = trending_people.TrendingPeopleResource(self)
        self.authentication = authentication.AuthenticationResource(self)
        self.find = find.FindResource(self)
        self.tv_shows = tv_shows.TvShowsResource(self)
        self.accounts = accounts.AccountsResource(self)
        self.certifications = certifications.CertificationsResource(self)
        self.collections = collections.CollectionsResource(self)
        self.companies = companies.CompaniesResource(self)
        self.credits = credits.CreditsResource(self)
        self.genres = genres.GenresResource(self)
        self.guest_sessions = guest_sessions.GuestSessionsResource(self)
        self.watch_providers = watch_providers.WatchProvidersResource(self)
        self.keywords = keywords.KeywordsResource(self)
        self.lists = lists.ListsResource(self)
        self.networks = networks.NetworksResource(self)
        self.reviews = reviews.ReviewsResource(self)
        self.person = person.PersonResource(self)
        self.tv_series = tv_series.TvSeriesResource(self)
        self.with_raw_response = TmdbClientWithRawResponse(self)
        self.with_streaming_response = TmdbClientWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": bearer_token}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncTmdbClient(AsyncAPIClient):
    movies: movies.AsyncMoviesResource
    tv: tv.AsyncTvResource
    search: search.AsyncSearchResource
    people: people.AsyncPeopleResource
    configuration: configuration.AsyncConfigurationResource
    discover_tv: discover_tv.AsyncDiscoverTvResource
    trending: trending.AsyncTrendingResource
    trending_movies: trending_movies.AsyncTrendingMoviesResource
    trending_tv_shows: trending_tv_shows.AsyncTrendingTvShowsResource
    episodes: episodes.AsyncEpisodesResource
    trending_people: trending_people.AsyncTrendingPeopleResource
    authentication: authentication.AsyncAuthenticationResource
    find: find.AsyncFindResource
    tv_shows: tv_shows.AsyncTvShowsResource
    accounts: accounts.AsyncAccountsResource
    certifications: certifications.AsyncCertificationsResource
    collections: collections.AsyncCollectionsResource
    companies: companies.AsyncCompaniesResource
    credits: credits.AsyncCreditsResource
    genres: genres.AsyncGenresResource
    guest_sessions: guest_sessions.AsyncGuestSessionsResource
    watch_providers: watch_providers.AsyncWatchProvidersResource
    keywords: keywords.AsyncKeywordsResource
    lists: lists.AsyncListsResource
    networks: networks.AsyncNetworksResource
    reviews: reviews.AsyncReviewsResource
    person: person.AsyncPersonResource
    tv_series: tv_series.AsyncTvSeriesResource
    with_raw_response: AsyncTmdbClientWithRawResponse
    with_streaming_response: AsyncTmdbClientWithStreamedResponse

    # client options
    bearer_token: str

    def __init__(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async tmdb-client client instance.

        This automatically infers the `bearer_token` argument from the `TMDB_API_BEARER_TOKEN` environment variable if it is not provided.
        """
        if bearer_token is None:
            bearer_token = os.environ.get("TMDB_API_BEARER_TOKEN")
        if bearer_token is None:
            raise TmdbClientError(
                "The bearer_token client option must be set either by passing bearer_token to the client or by setting the TMDB_API_BEARER_TOKEN environment variable"
            )
        self.bearer_token = bearer_token

        if base_url is None:
            base_url = os.environ.get("TMDB_CLIENT_BASE_URL")
        if base_url is None:
            base_url = f"https://api.themoviedb.org"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.movies = movies.AsyncMoviesResource(self)
        self.tv = tv.AsyncTvResource(self)
        self.search = search.AsyncSearchResource(self)
        self.people = people.AsyncPeopleResource(self)
        self.configuration = configuration.AsyncConfigurationResource(self)
        self.discover_tv = discover_tv.AsyncDiscoverTvResource(self)
        self.trending = trending.AsyncTrendingResource(self)
        self.trending_movies = trending_movies.AsyncTrendingMoviesResource(self)
        self.trending_tv_shows = trending_tv_shows.AsyncTrendingTvShowsResource(self)
        self.episodes = episodes.AsyncEpisodesResource(self)
        self.trending_people = trending_people.AsyncTrendingPeopleResource(self)
        self.authentication = authentication.AsyncAuthenticationResource(self)
        self.find = find.AsyncFindResource(self)
        self.tv_shows = tv_shows.AsyncTvShowsResource(self)
        self.accounts = accounts.AsyncAccountsResource(self)
        self.certifications = certifications.AsyncCertificationsResource(self)
        self.collections = collections.AsyncCollectionsResource(self)
        self.companies = companies.AsyncCompaniesResource(self)
        self.credits = credits.AsyncCreditsResource(self)
        self.genres = genres.AsyncGenresResource(self)
        self.guest_sessions = guest_sessions.AsyncGuestSessionsResource(self)
        self.watch_providers = watch_providers.AsyncWatchProvidersResource(self)
        self.keywords = keywords.AsyncKeywordsResource(self)
        self.lists = lists.AsyncListsResource(self)
        self.networks = networks.AsyncNetworksResource(self)
        self.reviews = reviews.AsyncReviewsResource(self)
        self.person = person.AsyncPersonResource(self)
        self.tv_series = tv_series.AsyncTvSeriesResource(self)
        self.with_raw_response = AsyncTmdbClientWithRawResponse(self)
        self.with_streaming_response = AsyncTmdbClientWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        bearer_token = self.bearer_token
        return {"Authorization": bearer_token}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        bearer_token: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            bearer_token=bearer_token or self.bearer_token,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class TmdbClientWithRawResponse:
    def __init__(self, client: TmdbClient) -> None:
        self.movies = movies.MoviesResourceWithRawResponse(client.movies)
        self.tv = tv.TvResourceWithRawResponse(client.tv)
        self.search = search.SearchResourceWithRawResponse(client.search)
        self.people = people.PeopleResourceWithRawResponse(client.people)
        self.configuration = configuration.ConfigurationResourceWithRawResponse(client.configuration)
        self.discover_tv = discover_tv.DiscoverTvResourceWithRawResponse(client.discover_tv)
        self.trending = trending.TrendingResourceWithRawResponse(client.trending)
        self.trending_movies = trending_movies.TrendingMoviesResourceWithRawResponse(client.trending_movies)
        self.trending_tv_shows = trending_tv_shows.TrendingTvShowsResourceWithRawResponse(client.trending_tv_shows)
        self.episodes = episodes.EpisodesResourceWithRawResponse(client.episodes)
        self.trending_people = trending_people.TrendingPeopleResourceWithRawResponse(client.trending_people)
        self.authentication = authentication.AuthenticationResourceWithRawResponse(client.authentication)
        self.find = find.FindResourceWithRawResponse(client.find)
        self.tv_shows = tv_shows.TvShowsResourceWithRawResponse(client.tv_shows)
        self.accounts = accounts.AccountsResourceWithRawResponse(client.accounts)
        self.certifications = certifications.CertificationsResourceWithRawResponse(client.certifications)
        self.collections = collections.CollectionsResourceWithRawResponse(client.collections)
        self.companies = companies.CompaniesResourceWithRawResponse(client.companies)
        self.credits = credits.CreditsResourceWithRawResponse(client.credits)
        self.genres = genres.GenresResourceWithRawResponse(client.genres)
        self.guest_sessions = guest_sessions.GuestSessionsResourceWithRawResponse(client.guest_sessions)
        self.watch_providers = watch_providers.WatchProvidersResourceWithRawResponse(client.watch_providers)
        self.keywords = keywords.KeywordsResourceWithRawResponse(client.keywords)
        self.lists = lists.ListsResourceWithRawResponse(client.lists)
        self.networks = networks.NetworksResourceWithRawResponse(client.networks)
        self.reviews = reviews.ReviewsResourceWithRawResponse(client.reviews)
        self.person = person.PersonResourceWithRawResponse(client.person)
        self.tv_series = tv_series.TvSeriesResourceWithRawResponse(client.tv_series)


class AsyncTmdbClientWithRawResponse:
    def __init__(self, client: AsyncTmdbClient) -> None:
        self.movies = movies.AsyncMoviesResourceWithRawResponse(client.movies)
        self.tv = tv.AsyncTvResourceWithRawResponse(client.tv)
        self.search = search.AsyncSearchResourceWithRawResponse(client.search)
        self.people = people.AsyncPeopleResourceWithRawResponse(client.people)
        self.configuration = configuration.AsyncConfigurationResourceWithRawResponse(client.configuration)
        self.discover_tv = discover_tv.AsyncDiscoverTvResourceWithRawResponse(client.discover_tv)
        self.trending = trending.AsyncTrendingResourceWithRawResponse(client.trending)
        self.trending_movies = trending_movies.AsyncTrendingMoviesResourceWithRawResponse(client.trending_movies)
        self.trending_tv_shows = trending_tv_shows.AsyncTrendingTvShowsResourceWithRawResponse(client.trending_tv_shows)
        self.episodes = episodes.AsyncEpisodesResourceWithRawResponse(client.episodes)
        self.trending_people = trending_people.AsyncTrendingPeopleResourceWithRawResponse(client.trending_people)
        self.authentication = authentication.AsyncAuthenticationResourceWithRawResponse(client.authentication)
        self.find = find.AsyncFindResourceWithRawResponse(client.find)
        self.tv_shows = tv_shows.AsyncTvShowsResourceWithRawResponse(client.tv_shows)
        self.accounts = accounts.AsyncAccountsResourceWithRawResponse(client.accounts)
        self.certifications = certifications.AsyncCertificationsResourceWithRawResponse(client.certifications)
        self.collections = collections.AsyncCollectionsResourceWithRawResponse(client.collections)
        self.companies = companies.AsyncCompaniesResourceWithRawResponse(client.companies)
        self.credits = credits.AsyncCreditsResourceWithRawResponse(client.credits)
        self.genres = genres.AsyncGenresResourceWithRawResponse(client.genres)
        self.guest_sessions = guest_sessions.AsyncGuestSessionsResourceWithRawResponse(client.guest_sessions)
        self.watch_providers = watch_providers.AsyncWatchProvidersResourceWithRawResponse(client.watch_providers)
        self.keywords = keywords.AsyncKeywordsResourceWithRawResponse(client.keywords)
        self.lists = lists.AsyncListsResourceWithRawResponse(client.lists)
        self.networks = networks.AsyncNetworksResourceWithRawResponse(client.networks)
        self.reviews = reviews.AsyncReviewsResourceWithRawResponse(client.reviews)
        self.person = person.AsyncPersonResourceWithRawResponse(client.person)
        self.tv_series = tv_series.AsyncTvSeriesResourceWithRawResponse(client.tv_series)


class TmdbClientWithStreamedResponse:
    def __init__(self, client: TmdbClient) -> None:
        self.movies = movies.MoviesResourceWithStreamingResponse(client.movies)
        self.tv = tv.TvResourceWithStreamingResponse(client.tv)
        self.search = search.SearchResourceWithStreamingResponse(client.search)
        self.people = people.PeopleResourceWithStreamingResponse(client.people)
        self.configuration = configuration.ConfigurationResourceWithStreamingResponse(client.configuration)
        self.discover_tv = discover_tv.DiscoverTvResourceWithStreamingResponse(client.discover_tv)
        self.trending = trending.TrendingResourceWithStreamingResponse(client.trending)
        self.trending_movies = trending_movies.TrendingMoviesResourceWithStreamingResponse(client.trending_movies)
        self.trending_tv_shows = trending_tv_shows.TrendingTvShowsResourceWithStreamingResponse(
            client.trending_tv_shows
        )
        self.episodes = episodes.EpisodesResourceWithStreamingResponse(client.episodes)
        self.trending_people = trending_people.TrendingPeopleResourceWithStreamingResponse(client.trending_people)
        self.authentication = authentication.AuthenticationResourceWithStreamingResponse(client.authentication)
        self.find = find.FindResourceWithStreamingResponse(client.find)
        self.tv_shows = tv_shows.TvShowsResourceWithStreamingResponse(client.tv_shows)
        self.accounts = accounts.AccountsResourceWithStreamingResponse(client.accounts)
        self.certifications = certifications.CertificationsResourceWithStreamingResponse(client.certifications)
        self.collections = collections.CollectionsResourceWithStreamingResponse(client.collections)
        self.companies = companies.CompaniesResourceWithStreamingResponse(client.companies)
        self.credits = credits.CreditsResourceWithStreamingResponse(client.credits)
        self.genres = genres.GenresResourceWithStreamingResponse(client.genres)
        self.guest_sessions = guest_sessions.GuestSessionsResourceWithStreamingResponse(client.guest_sessions)
        self.watch_providers = watch_providers.WatchProvidersResourceWithStreamingResponse(client.watch_providers)
        self.keywords = keywords.KeywordsResourceWithStreamingResponse(client.keywords)
        self.lists = lists.ListsResourceWithStreamingResponse(client.lists)
        self.networks = networks.NetworksResourceWithStreamingResponse(client.networks)
        self.reviews = reviews.ReviewsResourceWithStreamingResponse(client.reviews)
        self.person = person.PersonResourceWithStreamingResponse(client.person)
        self.tv_series = tv_series.TvSeriesResourceWithStreamingResponse(client.tv_series)


class AsyncTmdbClientWithStreamedResponse:
    def __init__(self, client: AsyncTmdbClient) -> None:
        self.movies = movies.AsyncMoviesResourceWithStreamingResponse(client.movies)
        self.tv = tv.AsyncTvResourceWithStreamingResponse(client.tv)
        self.search = search.AsyncSearchResourceWithStreamingResponse(client.search)
        self.people = people.AsyncPeopleResourceWithStreamingResponse(client.people)
        self.configuration = configuration.AsyncConfigurationResourceWithStreamingResponse(client.configuration)
        self.discover_tv = discover_tv.AsyncDiscoverTvResourceWithStreamingResponse(client.discover_tv)
        self.trending = trending.AsyncTrendingResourceWithStreamingResponse(client.trending)
        self.trending_movies = trending_movies.AsyncTrendingMoviesResourceWithStreamingResponse(client.trending_movies)
        self.trending_tv_shows = trending_tv_shows.AsyncTrendingTvShowsResourceWithStreamingResponse(
            client.trending_tv_shows
        )
        self.episodes = episodes.AsyncEpisodesResourceWithStreamingResponse(client.episodes)
        self.trending_people = trending_people.AsyncTrendingPeopleResourceWithStreamingResponse(client.trending_people)
        self.authentication = authentication.AsyncAuthenticationResourceWithStreamingResponse(client.authentication)
        self.find = find.AsyncFindResourceWithStreamingResponse(client.find)
        self.tv_shows = tv_shows.AsyncTvShowsResourceWithStreamingResponse(client.tv_shows)
        self.accounts = accounts.AsyncAccountsResourceWithStreamingResponse(client.accounts)
        self.certifications = certifications.AsyncCertificationsResourceWithStreamingResponse(client.certifications)
        self.collections = collections.AsyncCollectionsResourceWithStreamingResponse(client.collections)
        self.companies = companies.AsyncCompaniesResourceWithStreamingResponse(client.companies)
        self.credits = credits.AsyncCreditsResourceWithStreamingResponse(client.credits)
        self.genres = genres.AsyncGenresResourceWithStreamingResponse(client.genres)
        self.guest_sessions = guest_sessions.AsyncGuestSessionsResourceWithStreamingResponse(client.guest_sessions)
        self.watch_providers = watch_providers.AsyncWatchProvidersResourceWithStreamingResponse(client.watch_providers)
        self.keywords = keywords.AsyncKeywordsResourceWithStreamingResponse(client.keywords)
        self.lists = lists.AsyncListsResourceWithStreamingResponse(client.lists)
        self.networks = networks.AsyncNetworksResourceWithStreamingResponse(client.networks)
        self.reviews = reviews.AsyncReviewsResourceWithStreamingResponse(client.reviews)
        self.person = person.AsyncPersonResourceWithStreamingResponse(client.person)
        self.tv_series = tv_series.AsyncTvSeriesResourceWithStreamingResponse(client.tv_series)


Client = TmdbClient

AsyncClient = AsyncTmdbClient
