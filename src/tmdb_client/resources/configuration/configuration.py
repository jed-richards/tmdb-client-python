# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .jobs import (
    JobsResource,
    AsyncJobsResource,
    JobsResourceWithRawResponse,
    AsyncJobsResourceWithRawResponse,
    JobsResourceWithStreamingResponse,
    AsyncJobsResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from .countries import (
    CountriesResource,
    AsyncCountriesResource,
    CountriesResourceWithRawResponse,
    AsyncCountriesResourceWithRawResponse,
    CountriesResourceWithStreamingResponse,
    AsyncCountriesResourceWithStreamingResponse,
)
from .languages import (
    LanguagesResource,
    AsyncLanguagesResource,
    LanguagesResourceWithRawResponse,
    AsyncLanguagesResourceWithRawResponse,
    LanguagesResourceWithStreamingResponse,
    AsyncLanguagesResourceWithStreamingResponse,
)
from .timezones import (
    TimezonesResource,
    AsyncTimezonesResource,
    TimezonesResourceWithRawResponse,
    AsyncTimezonesResourceWithRawResponse,
    TimezonesResourceWithStreamingResponse,
    AsyncTimezonesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .primary_translations import (
    PrimaryTranslationsResource,
    AsyncPrimaryTranslationsResource,
    PrimaryTranslationsResourceWithRawResponse,
    AsyncPrimaryTranslationsResourceWithRawResponse,
    PrimaryTranslationsResourceWithStreamingResponse,
    AsyncPrimaryTranslationsResourceWithStreamingResponse,
)
from ...types.configuration_retrieve_response import ConfigurationRetrieveResponse

__all__ = ["ConfigurationResource", "AsyncConfigurationResource"]


class ConfigurationResource(SyncAPIResource):
    @cached_property
    def countries(self) -> CountriesResource:
        return CountriesResource(self._client)

    @cached_property
    def jobs(self) -> JobsResource:
        return JobsResource(self._client)

    @cached_property
    def languages(self) -> LanguagesResource:
        return LanguagesResource(self._client)

    @cached_property
    def primary_translations(self) -> PrimaryTranslationsResource:
        return PrimaryTranslationsResource(self._client)

    @cached_property
    def timezones(self) -> TimezonesResource:
        return TimezonesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConfigurationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return ConfigurationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigurationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return ConfigurationResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationRetrieveResponse:
        """Query the API configuration details."""
        return self._get(
            "/3/configuration",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigurationRetrieveResponse,
        )


class AsyncConfigurationResource(AsyncAPIResource):
    @cached_property
    def countries(self) -> AsyncCountriesResource:
        return AsyncCountriesResource(self._client)

    @cached_property
    def jobs(self) -> AsyncJobsResource:
        return AsyncJobsResource(self._client)

    @cached_property
    def languages(self) -> AsyncLanguagesResource:
        return AsyncLanguagesResource(self._client)

    @cached_property
    def primary_translations(self) -> AsyncPrimaryTranslationsResource:
        return AsyncPrimaryTranslationsResource(self._client)

    @cached_property
    def timezones(self) -> AsyncTimezonesResource:
        return AsyncTimezonesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConfigurationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigurationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigurationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jed-richards/tmdb-client-python#with_streaming_response
        """
        return AsyncConfigurationResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationRetrieveResponse:
        """Query the API configuration details."""
        return await self._get(
            "/3/configuration",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ConfigurationRetrieveResponse,
        )


class ConfigurationResourceWithRawResponse:
    def __init__(self, configuration: ConfigurationResource) -> None:
        self._configuration = configuration

        self.retrieve = to_raw_response_wrapper(
            configuration.retrieve,
        )

    @cached_property
    def countries(self) -> CountriesResourceWithRawResponse:
        return CountriesResourceWithRawResponse(self._configuration.countries)

    @cached_property
    def jobs(self) -> JobsResourceWithRawResponse:
        return JobsResourceWithRawResponse(self._configuration.jobs)

    @cached_property
    def languages(self) -> LanguagesResourceWithRawResponse:
        return LanguagesResourceWithRawResponse(self._configuration.languages)

    @cached_property
    def primary_translations(self) -> PrimaryTranslationsResourceWithRawResponse:
        return PrimaryTranslationsResourceWithRawResponse(self._configuration.primary_translations)

    @cached_property
    def timezones(self) -> TimezonesResourceWithRawResponse:
        return TimezonesResourceWithRawResponse(self._configuration.timezones)


class AsyncConfigurationResourceWithRawResponse:
    def __init__(self, configuration: AsyncConfigurationResource) -> None:
        self._configuration = configuration

        self.retrieve = async_to_raw_response_wrapper(
            configuration.retrieve,
        )

    @cached_property
    def countries(self) -> AsyncCountriesResourceWithRawResponse:
        return AsyncCountriesResourceWithRawResponse(self._configuration.countries)

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithRawResponse:
        return AsyncJobsResourceWithRawResponse(self._configuration.jobs)

    @cached_property
    def languages(self) -> AsyncLanguagesResourceWithRawResponse:
        return AsyncLanguagesResourceWithRawResponse(self._configuration.languages)

    @cached_property
    def primary_translations(self) -> AsyncPrimaryTranslationsResourceWithRawResponse:
        return AsyncPrimaryTranslationsResourceWithRawResponse(self._configuration.primary_translations)

    @cached_property
    def timezones(self) -> AsyncTimezonesResourceWithRawResponse:
        return AsyncTimezonesResourceWithRawResponse(self._configuration.timezones)


class ConfigurationResourceWithStreamingResponse:
    def __init__(self, configuration: ConfigurationResource) -> None:
        self._configuration = configuration

        self.retrieve = to_streamed_response_wrapper(
            configuration.retrieve,
        )

    @cached_property
    def countries(self) -> CountriesResourceWithStreamingResponse:
        return CountriesResourceWithStreamingResponse(self._configuration.countries)

    @cached_property
    def jobs(self) -> JobsResourceWithStreamingResponse:
        return JobsResourceWithStreamingResponse(self._configuration.jobs)

    @cached_property
    def languages(self) -> LanguagesResourceWithStreamingResponse:
        return LanguagesResourceWithStreamingResponse(self._configuration.languages)

    @cached_property
    def primary_translations(self) -> PrimaryTranslationsResourceWithStreamingResponse:
        return PrimaryTranslationsResourceWithStreamingResponse(self._configuration.primary_translations)

    @cached_property
    def timezones(self) -> TimezonesResourceWithStreamingResponse:
        return TimezonesResourceWithStreamingResponse(self._configuration.timezones)


class AsyncConfigurationResourceWithStreamingResponse:
    def __init__(self, configuration: AsyncConfigurationResource) -> None:
        self._configuration = configuration

        self.retrieve = async_to_streamed_response_wrapper(
            configuration.retrieve,
        )

    @cached_property
    def countries(self) -> AsyncCountriesResourceWithStreamingResponse:
        return AsyncCountriesResourceWithStreamingResponse(self._configuration.countries)

    @cached_property
    def jobs(self) -> AsyncJobsResourceWithStreamingResponse:
        return AsyncJobsResourceWithStreamingResponse(self._configuration.jobs)

    @cached_property
    def languages(self) -> AsyncLanguagesResourceWithStreamingResponse:
        return AsyncLanguagesResourceWithStreamingResponse(self._configuration.languages)

    @cached_property
    def primary_translations(self) -> AsyncPrimaryTranslationsResourceWithStreamingResponse:
        return AsyncPrimaryTranslationsResourceWithStreamingResponse(self._configuration.primary_translations)

    @cached_property
    def timezones(self) -> AsyncTimezonesResourceWithStreamingResponse:
        return AsyncTimezonesResourceWithStreamingResponse(self._configuration.timezones)
