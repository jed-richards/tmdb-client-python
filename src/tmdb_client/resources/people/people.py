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
from ...types import person_search_params, person_retrieve_params, person_tagged_images_params
from .changes import (
    ChangesResource,
    AsyncChangesResource,
    ChangesResourceWithRawResponse,
    AsyncChangesResourceWithRawResponse,
    ChangesResourceWithStreamingResponse,
    AsyncChangesResourceWithStreamingResponse,
)
from .popular import (
    PopularResource,
    AsyncPopularResource,
    PopularResourceWithRawResponse,
    AsyncPopularResourceWithRawResponse,
    PopularResourceWithStreamingResponse,
    AsyncPopularResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from .tv_credits import (
    TvCreditsResource,
    AsyncTvCreditsResource,
    TvCreditsResourceWithRawResponse,
    AsyncTvCreditsResourceWithRawResponse,
    TvCreditsResourceWithStreamingResponse,
    AsyncTvCreditsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .movie_credits import (
    MovieCreditsResource,
    AsyncMovieCreditsResource,
    MovieCreditsResourceWithRawResponse,
    AsyncMovieCreditsResourceWithRawResponse,
    MovieCreditsResourceWithStreamingResponse,
    AsyncMovieCreditsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .combined_credits import (
    CombinedCreditsResource,
    AsyncCombinedCreditsResource,
    CombinedCreditsResourceWithRawResponse,
    AsyncCombinedCreditsResourceWithRawResponse,
    CombinedCreditsResourceWithStreamingResponse,
    AsyncCombinedCreditsResourceWithStreamingResponse,
)
from ...types.person_search_response import PersonSearchResponse
from ...types.person_retrieve_response import PersonRetrieveResponse
from ...types.person_external_ids_response import PersonExternalIDsResponse
from ...types.person_translations_response import PersonTranslationsResponse
from ...types.person_tagged_images_response import PersonTaggedImagesResponse

__all__ = ["PeopleResource", "AsyncPeopleResource"]


class PeopleResource(SyncAPIResource):
    @cached_property
    def changes(self) -> ChangesResource:
        return ChangesResource(self._client)

    @cached_property
    def images(self) -> ImagesResource:
        return ImagesResource(self._client)

    @cached_property
    def movie_credits(self) -> MovieCreditsResource:
        return MovieCreditsResource(self._client)

    @cached_property
    def tv_credits(self) -> TvCreditsResource:
        return TvCreditsResource(self._client)

    @cached_property
    def combined_credits(self) -> CombinedCreditsResource:
        return CombinedCreditsResource(self._client)

    @cached_property
    def popular(self) -> PopularResource:
        return PopularResource(self._client)

    @cached_property
    def with_raw_response(self) -> PeopleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return PeopleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PeopleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return PeopleResourceWithStreamingResponse(self)

    def retrieve(
        self,
        person_id: int,
        *,
        append_to_response: str | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonRetrieveResponse:
        """
        Query the top level details of a person.

        Args:
          append_to_response: comma separated list of endpoints within this namespace, 20 items max

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/3/person/{person_id}",
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
                    person_retrieve_params.PersonRetrieveParams,
                ),
            ),
            cast_to=PersonRetrieveResponse,
        )

    def external_ids(
        self,
        person_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonExternalIDsResponse:
        """
        Get the external ID's that belong to a person.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/3/person/{person_id}/external_ids",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PersonExternalIDsResponse,
        )

    def search(
        self,
        *,
        query: str,
        include_adult: bool | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonSearchResponse:
        """
        Search for people by their name and also known as names.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/3/search/person",
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
                    },
                    person_search_params.PersonSearchParams,
                ),
            ),
            cast_to=PersonSearchResponse,
        )

    def tagged_images(
        self,
        person_id: int,
        *,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonTaggedImagesResponse:
        """
        Get the tagged images for a person.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/3/person/{person_id}/tagged_images",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"page": page}, person_tagged_images_params.PersonTaggedImagesParams),
            ),
            cast_to=PersonTaggedImagesResponse,
        )

    def translations(
        self,
        person_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonTranslationsResponse:
        """
        Get the translations that belong to a person.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/3/person/{person_id}/translations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PersonTranslationsResponse,
        )


class AsyncPeopleResource(AsyncAPIResource):
    @cached_property
    def changes(self) -> AsyncChangesResource:
        return AsyncChangesResource(self._client)

    @cached_property
    def images(self) -> AsyncImagesResource:
        return AsyncImagesResource(self._client)

    @cached_property
    def movie_credits(self) -> AsyncMovieCreditsResource:
        return AsyncMovieCreditsResource(self._client)

    @cached_property
    def tv_credits(self) -> AsyncTvCreditsResource:
        return AsyncTvCreditsResource(self._client)

    @cached_property
    def combined_credits(self) -> AsyncCombinedCreditsResource:
        return AsyncCombinedCreditsResource(self._client)

    @cached_property
    def popular(self) -> AsyncPopularResource:
        return AsyncPopularResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPeopleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPeopleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPeopleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncPeopleResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        person_id: int,
        *,
        append_to_response: str | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonRetrieveResponse:
        """
        Query the top level details of a person.

        Args:
          append_to_response: comma separated list of endpoints within this namespace, 20 items max

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/3/person/{person_id}",
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
                    person_retrieve_params.PersonRetrieveParams,
                ),
            ),
            cast_to=PersonRetrieveResponse,
        )

    async def external_ids(
        self,
        person_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonExternalIDsResponse:
        """
        Get the external ID's that belong to a person.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/3/person/{person_id}/external_ids",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PersonExternalIDsResponse,
        )

    async def search(
        self,
        *,
        query: str,
        include_adult: bool | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonSearchResponse:
        """
        Search for people by their name and also known as names.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/3/search/person",
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
                    },
                    person_search_params.PersonSearchParams,
                ),
            ),
            cast_to=PersonSearchResponse,
        )

    async def tagged_images(
        self,
        person_id: int,
        *,
        page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonTaggedImagesResponse:
        """
        Get the tagged images for a person.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/3/person/{person_id}/tagged_images",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"page": page}, person_tagged_images_params.PersonTaggedImagesParams),
            ),
            cast_to=PersonTaggedImagesResponse,
        )

    async def translations(
        self,
        person_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PersonTranslationsResponse:
        """
        Get the translations that belong to a person.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/3/person/{person_id}/translations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PersonTranslationsResponse,
        )


class PeopleResourceWithRawResponse:
    def __init__(self, people: PeopleResource) -> None:
        self._people = people

        self.retrieve = to_raw_response_wrapper(
            people.retrieve,
        )
        self.external_ids = to_raw_response_wrapper(
            people.external_ids,
        )
        self.search = to_raw_response_wrapper(
            people.search,
        )
        self.tagged_images = to_raw_response_wrapper(
            people.tagged_images,
        )
        self.translations = to_raw_response_wrapper(
            people.translations,
        )

    @cached_property
    def changes(self) -> ChangesResourceWithRawResponse:
        return ChangesResourceWithRawResponse(self._people.changes)

    @cached_property
    def images(self) -> ImagesResourceWithRawResponse:
        return ImagesResourceWithRawResponse(self._people.images)

    @cached_property
    def movie_credits(self) -> MovieCreditsResourceWithRawResponse:
        return MovieCreditsResourceWithRawResponse(self._people.movie_credits)

    @cached_property
    def tv_credits(self) -> TvCreditsResourceWithRawResponse:
        return TvCreditsResourceWithRawResponse(self._people.tv_credits)

    @cached_property
    def combined_credits(self) -> CombinedCreditsResourceWithRawResponse:
        return CombinedCreditsResourceWithRawResponse(self._people.combined_credits)

    @cached_property
    def popular(self) -> PopularResourceWithRawResponse:
        return PopularResourceWithRawResponse(self._people.popular)


class AsyncPeopleResourceWithRawResponse:
    def __init__(self, people: AsyncPeopleResource) -> None:
        self._people = people

        self.retrieve = async_to_raw_response_wrapper(
            people.retrieve,
        )
        self.external_ids = async_to_raw_response_wrapper(
            people.external_ids,
        )
        self.search = async_to_raw_response_wrapper(
            people.search,
        )
        self.tagged_images = async_to_raw_response_wrapper(
            people.tagged_images,
        )
        self.translations = async_to_raw_response_wrapper(
            people.translations,
        )

    @cached_property
    def changes(self) -> AsyncChangesResourceWithRawResponse:
        return AsyncChangesResourceWithRawResponse(self._people.changes)

    @cached_property
    def images(self) -> AsyncImagesResourceWithRawResponse:
        return AsyncImagesResourceWithRawResponse(self._people.images)

    @cached_property
    def movie_credits(self) -> AsyncMovieCreditsResourceWithRawResponse:
        return AsyncMovieCreditsResourceWithRawResponse(self._people.movie_credits)

    @cached_property
    def tv_credits(self) -> AsyncTvCreditsResourceWithRawResponse:
        return AsyncTvCreditsResourceWithRawResponse(self._people.tv_credits)

    @cached_property
    def combined_credits(self) -> AsyncCombinedCreditsResourceWithRawResponse:
        return AsyncCombinedCreditsResourceWithRawResponse(self._people.combined_credits)

    @cached_property
    def popular(self) -> AsyncPopularResourceWithRawResponse:
        return AsyncPopularResourceWithRawResponse(self._people.popular)


class PeopleResourceWithStreamingResponse:
    def __init__(self, people: PeopleResource) -> None:
        self._people = people

        self.retrieve = to_streamed_response_wrapper(
            people.retrieve,
        )
        self.external_ids = to_streamed_response_wrapper(
            people.external_ids,
        )
        self.search = to_streamed_response_wrapper(
            people.search,
        )
        self.tagged_images = to_streamed_response_wrapper(
            people.tagged_images,
        )
        self.translations = to_streamed_response_wrapper(
            people.translations,
        )

    @cached_property
    def changes(self) -> ChangesResourceWithStreamingResponse:
        return ChangesResourceWithStreamingResponse(self._people.changes)

    @cached_property
    def images(self) -> ImagesResourceWithStreamingResponse:
        return ImagesResourceWithStreamingResponse(self._people.images)

    @cached_property
    def movie_credits(self) -> MovieCreditsResourceWithStreamingResponse:
        return MovieCreditsResourceWithStreamingResponse(self._people.movie_credits)

    @cached_property
    def tv_credits(self) -> TvCreditsResourceWithStreamingResponse:
        return TvCreditsResourceWithStreamingResponse(self._people.tv_credits)

    @cached_property
    def combined_credits(self) -> CombinedCreditsResourceWithStreamingResponse:
        return CombinedCreditsResourceWithStreamingResponse(self._people.combined_credits)

    @cached_property
    def popular(self) -> PopularResourceWithStreamingResponse:
        return PopularResourceWithStreamingResponse(self._people.popular)


class AsyncPeopleResourceWithStreamingResponse:
    def __init__(self, people: AsyncPeopleResource) -> None:
        self._people = people

        self.retrieve = async_to_streamed_response_wrapper(
            people.retrieve,
        )
        self.external_ids = async_to_streamed_response_wrapper(
            people.external_ids,
        )
        self.search = async_to_streamed_response_wrapper(
            people.search,
        )
        self.tagged_images = async_to_streamed_response_wrapper(
            people.tagged_images,
        )
        self.translations = async_to_streamed_response_wrapper(
            people.translations,
        )

    @cached_property
    def changes(self) -> AsyncChangesResourceWithStreamingResponse:
        return AsyncChangesResourceWithStreamingResponse(self._people.changes)

    @cached_property
    def images(self) -> AsyncImagesResourceWithStreamingResponse:
        return AsyncImagesResourceWithStreamingResponse(self._people.images)

    @cached_property
    def movie_credits(self) -> AsyncMovieCreditsResourceWithStreamingResponse:
        return AsyncMovieCreditsResourceWithStreamingResponse(self._people.movie_credits)

    @cached_property
    def tv_credits(self) -> AsyncTvCreditsResourceWithStreamingResponse:
        return AsyncTvCreditsResourceWithStreamingResponse(self._people.tv_credits)

    @cached_property
    def combined_credits(self) -> AsyncCombinedCreditsResourceWithStreamingResponse:
        return AsyncCombinedCreditsResourceWithStreamingResponse(self._people.combined_credits)

    @cached_property
    def popular(self) -> AsyncPopularResourceWithStreamingResponse:
        return AsyncPopularResourceWithStreamingResponse(self._people.popular)
