# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .lists import (
    ListsResource,
    AsyncListsResource,
    ListsResourceWithRawResponse,
    AsyncListsResourceWithRawResponse,
    ListsResourceWithStreamingResponse,
    AsyncListsResourceWithStreamingResponse,
)
from ...types import account_retrieve_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from .watchlist import (
    WatchlistResource,
    AsyncWatchlistResource,
    WatchlistResourceWithRawResponse,
    AsyncWatchlistResourceWithRawResponse,
    WatchlistResourceWithStreamingResponse,
    AsyncWatchlistResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .rated.rated import (
    RatedResource,
    AsyncRatedResource,
    RatedResourceWithRawResponse,
    AsyncRatedResourceWithRawResponse,
    RatedResourceWithStreamingResponse,
    AsyncRatedResourceWithStreamingResponse,
)
from .watchlist_tv import (
    WatchlistTvResource,
    AsyncWatchlistTvResource,
    WatchlistTvResourceWithRawResponse,
    AsyncWatchlistTvResourceWithRawResponse,
    WatchlistTvResourceWithStreamingResponse,
    AsyncWatchlistTvResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .watchlist_movies import (
    WatchlistMoviesResource,
    AsyncWatchlistMoviesResource,
    WatchlistMoviesResourceWithRawResponse,
    AsyncWatchlistMoviesResourceWithRawResponse,
    WatchlistMoviesResourceWithStreamingResponse,
    AsyncWatchlistMoviesResourceWithStreamingResponse,
)
from .favorite.favorite import (
    FavoriteResource,
    AsyncFavoriteResource,
    FavoriteResourceWithRawResponse,
    AsyncFavoriteResourceWithRawResponse,
    FavoriteResourceWithStreamingResponse,
    AsyncFavoriteResourceWithStreamingResponse,
)
from ...types.account_retrieve_response import AccountRetrieveResponse

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    @cached_property
    def lists(self) -> ListsResource:
        return ListsResource(self._client)

    @cached_property
    def favorite(self) -> FavoriteResource:
        return FavoriteResource(self._client)

    @cached_property
    def rated(self) -> RatedResource:
        return RatedResource(self._client)

    @cached_property
    def watchlist_movies(self) -> WatchlistMoviesResource:
        return WatchlistMoviesResource(self._client)

    @cached_property
    def watchlist_tv(self) -> WatchlistTvResource:
        return WatchlistTvResource(self._client)

    @cached_property
    def watchlist(self) -> WatchlistResource:
        return WatchlistResource(self._client)

    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AccountsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        account_id: int,
        *,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountRetrieveResponse:
        """
        Details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/3/account/{account_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"session_id": session_id}, account_retrieve_params.AccountRetrieveParams),
            ),
            cast_to=AccountRetrieveResponse,
        )


class AsyncAccountsResource(AsyncAPIResource):
    @cached_property
    def lists(self) -> AsyncListsResource:
        return AsyncListsResource(self._client)

    @cached_property
    def favorite(self) -> AsyncFavoriteResource:
        return AsyncFavoriteResource(self._client)

    @cached_property
    def rated(self) -> AsyncRatedResource:
        return AsyncRatedResource(self._client)

    @cached_property
    def watchlist_movies(self) -> AsyncWatchlistMoviesResource:
        return AsyncWatchlistMoviesResource(self._client)

    @cached_property
    def watchlist_tv(self) -> AsyncWatchlistTvResource:
        return AsyncWatchlistTvResource(self._client)

    @cached_property
    def watchlist(self) -> AsyncWatchlistResource:
        return AsyncWatchlistResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncAccountsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        account_id: int,
        *,
        session_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AccountRetrieveResponse:
        """
        Details

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/3/account/{account_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"session_id": session_id}, account_retrieve_params.AccountRetrieveParams
                ),
            ),
            cast_to=AccountRetrieveResponse,
        )


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = to_raw_response_wrapper(
            accounts.retrieve,
        )

    @cached_property
    def lists(self) -> ListsResourceWithRawResponse:
        return ListsResourceWithRawResponse(self._accounts.lists)

    @cached_property
    def favorite(self) -> FavoriteResourceWithRawResponse:
        return FavoriteResourceWithRawResponse(self._accounts.favorite)

    @cached_property
    def rated(self) -> RatedResourceWithRawResponse:
        return RatedResourceWithRawResponse(self._accounts.rated)

    @cached_property
    def watchlist_movies(self) -> WatchlistMoviesResourceWithRawResponse:
        return WatchlistMoviesResourceWithRawResponse(self._accounts.watchlist_movies)

    @cached_property
    def watchlist_tv(self) -> WatchlistTvResourceWithRawResponse:
        return WatchlistTvResourceWithRawResponse(self._accounts.watchlist_tv)

    @cached_property
    def watchlist(self) -> WatchlistResourceWithRawResponse:
        return WatchlistResourceWithRawResponse(self._accounts.watchlist)


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = async_to_raw_response_wrapper(
            accounts.retrieve,
        )

    @cached_property
    def lists(self) -> AsyncListsResourceWithRawResponse:
        return AsyncListsResourceWithRawResponse(self._accounts.lists)

    @cached_property
    def favorite(self) -> AsyncFavoriteResourceWithRawResponse:
        return AsyncFavoriteResourceWithRawResponse(self._accounts.favorite)

    @cached_property
    def rated(self) -> AsyncRatedResourceWithRawResponse:
        return AsyncRatedResourceWithRawResponse(self._accounts.rated)

    @cached_property
    def watchlist_movies(self) -> AsyncWatchlistMoviesResourceWithRawResponse:
        return AsyncWatchlistMoviesResourceWithRawResponse(self._accounts.watchlist_movies)

    @cached_property
    def watchlist_tv(self) -> AsyncWatchlistTvResourceWithRawResponse:
        return AsyncWatchlistTvResourceWithRawResponse(self._accounts.watchlist_tv)

    @cached_property
    def watchlist(self) -> AsyncWatchlistResourceWithRawResponse:
        return AsyncWatchlistResourceWithRawResponse(self._accounts.watchlist)


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = to_streamed_response_wrapper(
            accounts.retrieve,
        )

    @cached_property
    def lists(self) -> ListsResourceWithStreamingResponse:
        return ListsResourceWithStreamingResponse(self._accounts.lists)

    @cached_property
    def favorite(self) -> FavoriteResourceWithStreamingResponse:
        return FavoriteResourceWithStreamingResponse(self._accounts.favorite)

    @cached_property
    def rated(self) -> RatedResourceWithStreamingResponse:
        return RatedResourceWithStreamingResponse(self._accounts.rated)

    @cached_property
    def watchlist_movies(self) -> WatchlistMoviesResourceWithStreamingResponse:
        return WatchlistMoviesResourceWithStreamingResponse(self._accounts.watchlist_movies)

    @cached_property
    def watchlist_tv(self) -> WatchlistTvResourceWithStreamingResponse:
        return WatchlistTvResourceWithStreamingResponse(self._accounts.watchlist_tv)

    @cached_property
    def watchlist(self) -> WatchlistResourceWithStreamingResponse:
        return WatchlistResourceWithStreamingResponse(self._accounts.watchlist)


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.retrieve = async_to_streamed_response_wrapper(
            accounts.retrieve,
        )

    @cached_property
    def lists(self) -> AsyncListsResourceWithStreamingResponse:
        return AsyncListsResourceWithStreamingResponse(self._accounts.lists)

    @cached_property
    def favorite(self) -> AsyncFavoriteResourceWithStreamingResponse:
        return AsyncFavoriteResourceWithStreamingResponse(self._accounts.favorite)

    @cached_property
    def rated(self) -> AsyncRatedResourceWithStreamingResponse:
        return AsyncRatedResourceWithStreamingResponse(self._accounts.rated)

    @cached_property
    def watchlist_movies(self) -> AsyncWatchlistMoviesResourceWithStreamingResponse:
        return AsyncWatchlistMoviesResourceWithStreamingResponse(self._accounts.watchlist_movies)

    @cached_property
    def watchlist_tv(self) -> AsyncWatchlistTvResourceWithStreamingResponse:
        return AsyncWatchlistTvResourceWithStreamingResponse(self._accounts.watchlist_tv)

    @cached_property
    def watchlist(self) -> AsyncWatchlistResourceWithStreamingResponse:
        return AsyncWatchlistResourceWithStreamingResponse(self._accounts.watchlist)
