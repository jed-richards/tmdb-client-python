# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import discover_tv_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.discover_tv_list_response import DiscoverTvListResponse

__all__ = ["DiscoverTvResource", "AsyncDiscoverTvResource"]


class DiscoverTvResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DiscoverTvResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return DiscoverTvResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DiscoverTvResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return DiscoverTvResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        air_date: discover_tv_list_params.AirDate | NotGiven = NOT_GIVEN,
        first_air_date: discover_tv_list_params.FirstAirDate | NotGiven = NOT_GIVEN,
        first_air_date_year: int | NotGiven = NOT_GIVEN,
        include_adult: bool | NotGiven = NOT_GIVEN,
        include_null_first_air_dates: bool | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        screened_theatrically: bool | NotGiven = NOT_GIVEN,
        sort_by: Literal[
            "first_air_date.asc",
            "first_air_date.desc",
            "name.asc",
            "name.desc",
            "original_name.asc",
            "original_name.desc",
            "popularity.asc",
            "popularity.desc",
            "vote_average.asc",
            "vote_average.desc",
            "vote_count.asc",
            "vote_count.desc",
        ]
        | NotGiven = NOT_GIVEN,
        timezone: str | NotGiven = NOT_GIVEN,
        vote_average: discover_tv_list_params.VoteAverage | NotGiven = NOT_GIVEN,
        vote_count: discover_tv_list_params.VoteCount | NotGiven = NOT_GIVEN,
        watch_region: str | NotGiven = NOT_GIVEN,
        with_companies: str | NotGiven = NOT_GIVEN,
        with_genres: str | NotGiven = NOT_GIVEN,
        with_keywords: str | NotGiven = NOT_GIVEN,
        with_networks: int | NotGiven = NOT_GIVEN,
        with_origin_country: str | NotGiven = NOT_GIVEN,
        with_original_language: str | NotGiven = NOT_GIVEN,
        with_runtime: discover_tv_list_params.WithRuntime | NotGiven = NOT_GIVEN,
        with_status: str | NotGiven = NOT_GIVEN,
        with_type: str | NotGiven = NOT_GIVEN,
        with_watch_monetization_types: str | NotGiven = NOT_GIVEN,
        with_watch_providers: str | NotGiven = NOT_GIVEN,
        without_companies: str | NotGiven = NOT_GIVEN,
        without_genres: str | NotGiven = NOT_GIVEN,
        without_keywords: str | NotGiven = NOT_GIVEN,
        without_watch_providers: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DiscoverTvListResponse:
        """
        Find TV shows using over 30 filters and sort options.

        Args:
          watch_region: use in conjunction with `with_watch_monetization_types ` or
              `with_watch_providers `

          with_companies: can be a comma (`AND`) or pipe (`OR`) separated query

          with_genres: can be a comma (`AND`) or pipe (`OR`) separated query

          with_keywords: can be a comma (`AND`) or pipe (`OR`) separated query

          with_status: possible values are: [0, 1, 2, 3, 4, 5], can be a comma (`AND`) or pipe (`OR`)
              separated query

          with_type: possible values are: [0, 1, 2, 3, 4, 5, 6], can be a comma (`AND`) or pipe
              (`OR`) separated query

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
            "/3/discover/tv",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "air_date": air_date,
                        "first_air_date": first_air_date,
                        "first_air_date_year": first_air_date_year,
                        "include_adult": include_adult,
                        "include_null_first_air_dates": include_null_first_air_dates,
                        "language": language,
                        "page": page,
                        "screened_theatrically": screened_theatrically,
                        "sort_by": sort_by,
                        "timezone": timezone,
                        "vote_average": vote_average,
                        "vote_count": vote_count,
                        "watch_region": watch_region,
                        "with_companies": with_companies,
                        "with_genres": with_genres,
                        "with_keywords": with_keywords,
                        "with_networks": with_networks,
                        "with_origin_country": with_origin_country,
                        "with_original_language": with_original_language,
                        "with_runtime": with_runtime,
                        "with_status": with_status,
                        "with_type": with_type,
                        "with_watch_monetization_types": with_watch_monetization_types,
                        "with_watch_providers": with_watch_providers,
                        "without_companies": without_companies,
                        "without_genres": without_genres,
                        "without_keywords": without_keywords,
                        "without_watch_providers": without_watch_providers,
                    },
                    discover_tv_list_params.DiscoverTvListParams,
                ),
            ),
            cast_to=DiscoverTvListResponse,
        )


class AsyncDiscoverTvResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDiscoverTvResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDiscoverTvResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDiscoverTvResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/tmdb-client-python#with_streaming_response
        """
        return AsyncDiscoverTvResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        air_date: discover_tv_list_params.AirDate | NotGiven = NOT_GIVEN,
        first_air_date: discover_tv_list_params.FirstAirDate | NotGiven = NOT_GIVEN,
        first_air_date_year: int | NotGiven = NOT_GIVEN,
        include_adult: bool | NotGiven = NOT_GIVEN,
        include_null_first_air_dates: bool | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        screened_theatrically: bool | NotGiven = NOT_GIVEN,
        sort_by: Literal[
            "first_air_date.asc",
            "first_air_date.desc",
            "name.asc",
            "name.desc",
            "original_name.asc",
            "original_name.desc",
            "popularity.asc",
            "popularity.desc",
            "vote_average.asc",
            "vote_average.desc",
            "vote_count.asc",
            "vote_count.desc",
        ]
        | NotGiven = NOT_GIVEN,
        timezone: str | NotGiven = NOT_GIVEN,
        vote_average: discover_tv_list_params.VoteAverage | NotGiven = NOT_GIVEN,
        vote_count: discover_tv_list_params.VoteCount | NotGiven = NOT_GIVEN,
        watch_region: str | NotGiven = NOT_GIVEN,
        with_companies: str | NotGiven = NOT_GIVEN,
        with_genres: str | NotGiven = NOT_GIVEN,
        with_keywords: str | NotGiven = NOT_GIVEN,
        with_networks: int | NotGiven = NOT_GIVEN,
        with_origin_country: str | NotGiven = NOT_GIVEN,
        with_original_language: str | NotGiven = NOT_GIVEN,
        with_runtime: discover_tv_list_params.WithRuntime | NotGiven = NOT_GIVEN,
        with_status: str | NotGiven = NOT_GIVEN,
        with_type: str | NotGiven = NOT_GIVEN,
        with_watch_monetization_types: str | NotGiven = NOT_GIVEN,
        with_watch_providers: str | NotGiven = NOT_GIVEN,
        without_companies: str | NotGiven = NOT_GIVEN,
        without_genres: str | NotGiven = NOT_GIVEN,
        without_keywords: str | NotGiven = NOT_GIVEN,
        without_watch_providers: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DiscoverTvListResponse:
        """
        Find TV shows using over 30 filters and sort options.

        Args:
          watch_region: use in conjunction with `with_watch_monetization_types ` or
              `with_watch_providers `

          with_companies: can be a comma (`AND`) or pipe (`OR`) separated query

          with_genres: can be a comma (`AND`) or pipe (`OR`) separated query

          with_keywords: can be a comma (`AND`) or pipe (`OR`) separated query

          with_status: possible values are: [0, 1, 2, 3, 4, 5], can be a comma (`AND`) or pipe (`OR`)
              separated query

          with_type: possible values are: [0, 1, 2, 3, 4, 5, 6], can be a comma (`AND`) or pipe
              (`OR`) separated query

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
            "/3/discover/tv",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "air_date": air_date,
                        "first_air_date": first_air_date,
                        "first_air_date_year": first_air_date_year,
                        "include_adult": include_adult,
                        "include_null_first_air_dates": include_null_first_air_dates,
                        "language": language,
                        "page": page,
                        "screened_theatrically": screened_theatrically,
                        "sort_by": sort_by,
                        "timezone": timezone,
                        "vote_average": vote_average,
                        "vote_count": vote_count,
                        "watch_region": watch_region,
                        "with_companies": with_companies,
                        "with_genres": with_genres,
                        "with_keywords": with_keywords,
                        "with_networks": with_networks,
                        "with_origin_country": with_origin_country,
                        "with_original_language": with_original_language,
                        "with_runtime": with_runtime,
                        "with_status": with_status,
                        "with_type": with_type,
                        "with_watch_monetization_types": with_watch_monetization_types,
                        "with_watch_providers": with_watch_providers,
                        "without_companies": without_companies,
                        "without_genres": without_genres,
                        "without_keywords": without_keywords,
                        "without_watch_providers": without_watch_providers,
                    },
                    discover_tv_list_params.DiscoverTvListParams,
                ),
            ),
            cast_to=DiscoverTvListResponse,
        )


class DiscoverTvResourceWithRawResponse:
    def __init__(self, discover_tv: DiscoverTvResource) -> None:
        self._discover_tv = discover_tv

        self.list = to_raw_response_wrapper(
            discover_tv.list,
        )


class AsyncDiscoverTvResourceWithRawResponse:
    def __init__(self, discover_tv: AsyncDiscoverTvResource) -> None:
        self._discover_tv = discover_tv

        self.list = async_to_raw_response_wrapper(
            discover_tv.list,
        )


class DiscoverTvResourceWithStreamingResponse:
    def __init__(self, discover_tv: DiscoverTvResource) -> None:
        self._discover_tv = discover_tv

        self.list = to_streamed_response_wrapper(
            discover_tv.list,
        )


class AsyncDiscoverTvResourceWithStreamingResponse:
    def __init__(self, discover_tv: AsyncDiscoverTvResource) -> None:
        self._discover_tv = discover_tv

        self.list = async_to_streamed_response_wrapper(
            discover_tv.list,
        )
