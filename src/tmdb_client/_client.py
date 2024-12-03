# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
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
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, TmdbClientError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "TmdbClient",
    "AsyncTmdbClient",
    "Client",
    "AsyncClient",
]


class TmdbClient(SyncAPIClient):
    movies: resources.MoviesResource
    tv: resources.TvResource
    search: resources.SearchResource
    people: resources.PeopleResource
    configuration: resources.ConfigurationResource
    discover_tv: resources.DiscoverTvResource
    trending: resources.TrendingResource
    trending_movies: resources.TrendingMoviesResource
    trending_tv_shows: resources.TrendingTvShowsResource
    episodes: resources.EpisodesResource
    trending_people: resources.TrendingPeopleResource
    authentication: resources.AuthenticationResource
    find: resources.FindResource
    tv_shows: resources.TvShowsResource
    accounts: resources.AccountsResource
    certifications: resources.CertificationsResource
    collections: resources.CollectionsResource
    companies: resources.CompaniesResource
    credits: resources.CreditsResource
    genres: resources.GenresResource
    guest_sessions: resources.GuestSessionsResource
    watch_providers: resources.WatchProvidersResource
    keywords: resources.KeywordsResource
    lists: resources.ListsResource
    networks: resources.NetworksResource
    reviews: resources.ReviewsResource
    person: resources.PersonResource
    tv_series: resources.TvSeriesResource
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

        self.movies = resources.MoviesResource(self)
        self.tv = resources.TvResource(self)
        self.search = resources.SearchResource(self)
        self.people = resources.PeopleResource(self)
        self.configuration = resources.ConfigurationResource(self)
        self.discover_tv = resources.DiscoverTvResource(self)
        self.trending = resources.TrendingResource(self)
        self.trending_movies = resources.TrendingMoviesResource(self)
        self.trending_tv_shows = resources.TrendingTvShowsResource(self)
        self.episodes = resources.EpisodesResource(self)
        self.trending_people = resources.TrendingPeopleResource(self)
        self.authentication = resources.AuthenticationResource(self)
        self.find = resources.FindResource(self)
        self.tv_shows = resources.TvShowsResource(self)
        self.accounts = resources.AccountsResource(self)
        self.certifications = resources.CertificationsResource(self)
        self.collections = resources.CollectionsResource(self)
        self.companies = resources.CompaniesResource(self)
        self.credits = resources.CreditsResource(self)
        self.genres = resources.GenresResource(self)
        self.guest_sessions = resources.GuestSessionsResource(self)
        self.watch_providers = resources.WatchProvidersResource(self)
        self.keywords = resources.KeywordsResource(self)
        self.lists = resources.ListsResource(self)
        self.networks = resources.NetworksResource(self)
        self.reviews = resources.ReviewsResource(self)
        self.person = resources.PersonResource(self)
        self.tv_series = resources.TvSeriesResource(self)
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
    movies: resources.AsyncMoviesResource
    tv: resources.AsyncTvResource
    search: resources.AsyncSearchResource
    people: resources.AsyncPeopleResource
    configuration: resources.AsyncConfigurationResource
    discover_tv: resources.AsyncDiscoverTvResource
    trending: resources.AsyncTrendingResource
    trending_movies: resources.AsyncTrendingMoviesResource
    trending_tv_shows: resources.AsyncTrendingTvShowsResource
    episodes: resources.AsyncEpisodesResource
    trending_people: resources.AsyncTrendingPeopleResource
    authentication: resources.AsyncAuthenticationResource
    find: resources.AsyncFindResource
    tv_shows: resources.AsyncTvShowsResource
    accounts: resources.AsyncAccountsResource
    certifications: resources.AsyncCertificationsResource
    collections: resources.AsyncCollectionsResource
    companies: resources.AsyncCompaniesResource
    credits: resources.AsyncCreditsResource
    genres: resources.AsyncGenresResource
    guest_sessions: resources.AsyncGuestSessionsResource
    watch_providers: resources.AsyncWatchProvidersResource
    keywords: resources.AsyncKeywordsResource
    lists: resources.AsyncListsResource
    networks: resources.AsyncNetworksResource
    reviews: resources.AsyncReviewsResource
    person: resources.AsyncPersonResource
    tv_series: resources.AsyncTvSeriesResource
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

        self.movies = resources.AsyncMoviesResource(self)
        self.tv = resources.AsyncTvResource(self)
        self.search = resources.AsyncSearchResource(self)
        self.people = resources.AsyncPeopleResource(self)
        self.configuration = resources.AsyncConfigurationResource(self)
        self.discover_tv = resources.AsyncDiscoverTvResource(self)
        self.trending = resources.AsyncTrendingResource(self)
        self.trending_movies = resources.AsyncTrendingMoviesResource(self)
        self.trending_tv_shows = resources.AsyncTrendingTvShowsResource(self)
        self.episodes = resources.AsyncEpisodesResource(self)
        self.trending_people = resources.AsyncTrendingPeopleResource(self)
        self.authentication = resources.AsyncAuthenticationResource(self)
        self.find = resources.AsyncFindResource(self)
        self.tv_shows = resources.AsyncTvShowsResource(self)
        self.accounts = resources.AsyncAccountsResource(self)
        self.certifications = resources.AsyncCertificationsResource(self)
        self.collections = resources.AsyncCollectionsResource(self)
        self.companies = resources.AsyncCompaniesResource(self)
        self.credits = resources.AsyncCreditsResource(self)
        self.genres = resources.AsyncGenresResource(self)
        self.guest_sessions = resources.AsyncGuestSessionsResource(self)
        self.watch_providers = resources.AsyncWatchProvidersResource(self)
        self.keywords = resources.AsyncKeywordsResource(self)
        self.lists = resources.AsyncListsResource(self)
        self.networks = resources.AsyncNetworksResource(self)
        self.reviews = resources.AsyncReviewsResource(self)
        self.person = resources.AsyncPersonResource(self)
        self.tv_series = resources.AsyncTvSeriesResource(self)
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
        self.movies = resources.MoviesResourceWithRawResponse(client.movies)
        self.tv = resources.TvResourceWithRawResponse(client.tv)
        self.search = resources.SearchResourceWithRawResponse(client.search)
        self.people = resources.PeopleResourceWithRawResponse(client.people)
        self.configuration = resources.ConfigurationResourceWithRawResponse(client.configuration)
        self.discover_tv = resources.DiscoverTvResourceWithRawResponse(client.discover_tv)
        self.trending = resources.TrendingResourceWithRawResponse(client.trending)
        self.trending_movies = resources.TrendingMoviesResourceWithRawResponse(client.trending_movies)
        self.trending_tv_shows = resources.TrendingTvShowsResourceWithRawResponse(client.trending_tv_shows)
        self.episodes = resources.EpisodesResourceWithRawResponse(client.episodes)
        self.trending_people = resources.TrendingPeopleResourceWithRawResponse(client.trending_people)
        self.authentication = resources.AuthenticationResourceWithRawResponse(client.authentication)
        self.find = resources.FindResourceWithRawResponse(client.find)
        self.tv_shows = resources.TvShowsResourceWithRawResponse(client.tv_shows)
        self.accounts = resources.AccountsResourceWithRawResponse(client.accounts)
        self.certifications = resources.CertificationsResourceWithRawResponse(client.certifications)
        self.collections = resources.CollectionsResourceWithRawResponse(client.collections)
        self.companies = resources.CompaniesResourceWithRawResponse(client.companies)
        self.credits = resources.CreditsResourceWithRawResponse(client.credits)
        self.genres = resources.GenresResourceWithRawResponse(client.genres)
        self.guest_sessions = resources.GuestSessionsResourceWithRawResponse(client.guest_sessions)
        self.watch_providers = resources.WatchProvidersResourceWithRawResponse(client.watch_providers)
        self.keywords = resources.KeywordsResourceWithRawResponse(client.keywords)
        self.lists = resources.ListsResourceWithRawResponse(client.lists)
        self.networks = resources.NetworksResourceWithRawResponse(client.networks)
        self.reviews = resources.ReviewsResourceWithRawResponse(client.reviews)
        self.person = resources.PersonResourceWithRawResponse(client.person)
        self.tv_series = resources.TvSeriesResourceWithRawResponse(client.tv_series)


class AsyncTmdbClientWithRawResponse:
    def __init__(self, client: AsyncTmdbClient) -> None:
        self.movies = resources.AsyncMoviesResourceWithRawResponse(client.movies)
        self.tv = resources.AsyncTvResourceWithRawResponse(client.tv)
        self.search = resources.AsyncSearchResourceWithRawResponse(client.search)
        self.people = resources.AsyncPeopleResourceWithRawResponse(client.people)
        self.configuration = resources.AsyncConfigurationResourceWithRawResponse(client.configuration)
        self.discover_tv = resources.AsyncDiscoverTvResourceWithRawResponse(client.discover_tv)
        self.trending = resources.AsyncTrendingResourceWithRawResponse(client.trending)
        self.trending_movies = resources.AsyncTrendingMoviesResourceWithRawResponse(client.trending_movies)
        self.trending_tv_shows = resources.AsyncTrendingTvShowsResourceWithRawResponse(client.trending_tv_shows)
        self.episodes = resources.AsyncEpisodesResourceWithRawResponse(client.episodes)
        self.trending_people = resources.AsyncTrendingPeopleResourceWithRawResponse(client.trending_people)
        self.authentication = resources.AsyncAuthenticationResourceWithRawResponse(client.authentication)
        self.find = resources.AsyncFindResourceWithRawResponse(client.find)
        self.tv_shows = resources.AsyncTvShowsResourceWithRawResponse(client.tv_shows)
        self.accounts = resources.AsyncAccountsResourceWithRawResponse(client.accounts)
        self.certifications = resources.AsyncCertificationsResourceWithRawResponse(client.certifications)
        self.collections = resources.AsyncCollectionsResourceWithRawResponse(client.collections)
        self.companies = resources.AsyncCompaniesResourceWithRawResponse(client.companies)
        self.credits = resources.AsyncCreditsResourceWithRawResponse(client.credits)
        self.genres = resources.AsyncGenresResourceWithRawResponse(client.genres)
        self.guest_sessions = resources.AsyncGuestSessionsResourceWithRawResponse(client.guest_sessions)
        self.watch_providers = resources.AsyncWatchProvidersResourceWithRawResponse(client.watch_providers)
        self.keywords = resources.AsyncKeywordsResourceWithRawResponse(client.keywords)
        self.lists = resources.AsyncListsResourceWithRawResponse(client.lists)
        self.networks = resources.AsyncNetworksResourceWithRawResponse(client.networks)
        self.reviews = resources.AsyncReviewsResourceWithRawResponse(client.reviews)
        self.person = resources.AsyncPersonResourceWithRawResponse(client.person)
        self.tv_series = resources.AsyncTvSeriesResourceWithRawResponse(client.tv_series)


class TmdbClientWithStreamedResponse:
    def __init__(self, client: TmdbClient) -> None:
        self.movies = resources.MoviesResourceWithStreamingResponse(client.movies)
        self.tv = resources.TvResourceWithStreamingResponse(client.tv)
        self.search = resources.SearchResourceWithStreamingResponse(client.search)
        self.people = resources.PeopleResourceWithStreamingResponse(client.people)
        self.configuration = resources.ConfigurationResourceWithStreamingResponse(client.configuration)
        self.discover_tv = resources.DiscoverTvResourceWithStreamingResponse(client.discover_tv)
        self.trending = resources.TrendingResourceWithStreamingResponse(client.trending)
        self.trending_movies = resources.TrendingMoviesResourceWithStreamingResponse(client.trending_movies)
        self.trending_tv_shows = resources.TrendingTvShowsResourceWithStreamingResponse(client.trending_tv_shows)
        self.episodes = resources.EpisodesResourceWithStreamingResponse(client.episodes)
        self.trending_people = resources.TrendingPeopleResourceWithStreamingResponse(client.trending_people)
        self.authentication = resources.AuthenticationResourceWithStreamingResponse(client.authentication)
        self.find = resources.FindResourceWithStreamingResponse(client.find)
        self.tv_shows = resources.TvShowsResourceWithStreamingResponse(client.tv_shows)
        self.accounts = resources.AccountsResourceWithStreamingResponse(client.accounts)
        self.certifications = resources.CertificationsResourceWithStreamingResponse(client.certifications)
        self.collections = resources.CollectionsResourceWithStreamingResponse(client.collections)
        self.companies = resources.CompaniesResourceWithStreamingResponse(client.companies)
        self.credits = resources.CreditsResourceWithStreamingResponse(client.credits)
        self.genres = resources.GenresResourceWithStreamingResponse(client.genres)
        self.guest_sessions = resources.GuestSessionsResourceWithStreamingResponse(client.guest_sessions)
        self.watch_providers = resources.WatchProvidersResourceWithStreamingResponse(client.watch_providers)
        self.keywords = resources.KeywordsResourceWithStreamingResponse(client.keywords)
        self.lists = resources.ListsResourceWithStreamingResponse(client.lists)
        self.networks = resources.NetworksResourceWithStreamingResponse(client.networks)
        self.reviews = resources.ReviewsResourceWithStreamingResponse(client.reviews)
        self.person = resources.PersonResourceWithStreamingResponse(client.person)
        self.tv_series = resources.TvSeriesResourceWithStreamingResponse(client.tv_series)


class AsyncTmdbClientWithStreamedResponse:
    def __init__(self, client: AsyncTmdbClient) -> None:
        self.movies = resources.AsyncMoviesResourceWithStreamingResponse(client.movies)
        self.tv = resources.AsyncTvResourceWithStreamingResponse(client.tv)
        self.search = resources.AsyncSearchResourceWithStreamingResponse(client.search)
        self.people = resources.AsyncPeopleResourceWithStreamingResponse(client.people)
        self.configuration = resources.AsyncConfigurationResourceWithStreamingResponse(client.configuration)
        self.discover_tv = resources.AsyncDiscoverTvResourceWithStreamingResponse(client.discover_tv)
        self.trending = resources.AsyncTrendingResourceWithStreamingResponse(client.trending)
        self.trending_movies = resources.AsyncTrendingMoviesResourceWithStreamingResponse(client.trending_movies)
        self.trending_tv_shows = resources.AsyncTrendingTvShowsResourceWithStreamingResponse(client.trending_tv_shows)
        self.episodes = resources.AsyncEpisodesResourceWithStreamingResponse(client.episodes)
        self.trending_people = resources.AsyncTrendingPeopleResourceWithStreamingResponse(client.trending_people)
        self.authentication = resources.AsyncAuthenticationResourceWithStreamingResponse(client.authentication)
        self.find = resources.AsyncFindResourceWithStreamingResponse(client.find)
        self.tv_shows = resources.AsyncTvShowsResourceWithStreamingResponse(client.tv_shows)
        self.accounts = resources.AsyncAccountsResourceWithStreamingResponse(client.accounts)
        self.certifications = resources.AsyncCertificationsResourceWithStreamingResponse(client.certifications)
        self.collections = resources.AsyncCollectionsResourceWithStreamingResponse(client.collections)
        self.companies = resources.AsyncCompaniesResourceWithStreamingResponse(client.companies)
        self.credits = resources.AsyncCreditsResourceWithStreamingResponse(client.credits)
        self.genres = resources.AsyncGenresResourceWithStreamingResponse(client.genres)
        self.guest_sessions = resources.AsyncGuestSessionsResourceWithStreamingResponse(client.guest_sessions)
        self.watch_providers = resources.AsyncWatchProvidersResourceWithStreamingResponse(client.watch_providers)
        self.keywords = resources.AsyncKeywordsResourceWithStreamingResponse(client.keywords)
        self.lists = resources.AsyncListsResourceWithStreamingResponse(client.lists)
        self.networks = resources.AsyncNetworksResourceWithStreamingResponse(client.networks)
        self.reviews = resources.AsyncReviewsResourceWithStreamingResponse(client.reviews)
        self.person = resources.AsyncPersonResourceWithStreamingResponse(client.person)
        self.tv_series = resources.AsyncTvSeriesResourceWithStreamingResponse(client.tv_series)


Client = TmdbClient

AsyncClient = AsyncTmdbClient
