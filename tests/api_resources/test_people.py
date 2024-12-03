# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tmdb_client import TmdbClient, AsyncTmdbClient
from tmdb_client.types import (
    PersonSearchResponse,
    PersonRetrieveResponse,
    PersonExternalIDsResponse,
    PersonTaggedImagesResponse,
    PersonTranslationsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPeople:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: TmdbClient) -> None:
        person = client.people.retrieve(
            person_id=0,
        )
        assert_matches_type(PersonRetrieveResponse, person, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: TmdbClient) -> None:
        person = client.people.retrieve(
            person_id=0,
            append_to_response="append_to_response",
            language="language",
        )
        assert_matches_type(PersonRetrieveResponse, person, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: TmdbClient) -> None:
        response = client.people.with_raw_response.retrieve(
            person_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = response.parse()
        assert_matches_type(PersonRetrieveResponse, person, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: TmdbClient) -> None:
        with client.people.with_streaming_response.retrieve(
            person_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = response.parse()
            assert_matches_type(PersonRetrieveResponse, person, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_external_ids(self, client: TmdbClient) -> None:
        person = client.people.external_ids(
            0,
        )
        assert_matches_type(PersonExternalIDsResponse, person, path=["response"])

    @parametrize
    def test_raw_response_external_ids(self, client: TmdbClient) -> None:
        response = client.people.with_raw_response.external_ids(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = response.parse()
        assert_matches_type(PersonExternalIDsResponse, person, path=["response"])

    @parametrize
    def test_streaming_response_external_ids(self, client: TmdbClient) -> None:
        with client.people.with_streaming_response.external_ids(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = response.parse()
            assert_matches_type(PersonExternalIDsResponse, person, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_search(self, client: TmdbClient) -> None:
        person = client.people.search(
            query="query",
        )
        assert_matches_type(PersonSearchResponse, person, path=["response"])

    @parametrize
    def test_method_search_with_all_params(self, client: TmdbClient) -> None:
        person = client.people.search(
            query="query",
            include_adult=True,
            language="language",
            page=0,
        )
        assert_matches_type(PersonSearchResponse, person, path=["response"])

    @parametrize
    def test_raw_response_search(self, client: TmdbClient) -> None:
        response = client.people.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = response.parse()
        assert_matches_type(PersonSearchResponse, person, path=["response"])

    @parametrize
    def test_streaming_response_search(self, client: TmdbClient) -> None:
        with client.people.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = response.parse()
            assert_matches_type(PersonSearchResponse, person, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tagged_images(self, client: TmdbClient) -> None:
        person = client.people.tagged_images(
            person_id=0,
        )
        assert_matches_type(PersonTaggedImagesResponse, person, path=["response"])

    @parametrize
    def test_method_tagged_images_with_all_params(self, client: TmdbClient) -> None:
        person = client.people.tagged_images(
            person_id=0,
            page=0,
        )
        assert_matches_type(PersonTaggedImagesResponse, person, path=["response"])

    @parametrize
    def test_raw_response_tagged_images(self, client: TmdbClient) -> None:
        response = client.people.with_raw_response.tagged_images(
            person_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = response.parse()
        assert_matches_type(PersonTaggedImagesResponse, person, path=["response"])

    @parametrize
    def test_streaming_response_tagged_images(self, client: TmdbClient) -> None:
        with client.people.with_streaming_response.tagged_images(
            person_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = response.parse()
            assert_matches_type(PersonTaggedImagesResponse, person, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_translations(self, client: TmdbClient) -> None:
        person = client.people.translations(
            0,
        )
        assert_matches_type(PersonTranslationsResponse, person, path=["response"])

    @parametrize
    def test_raw_response_translations(self, client: TmdbClient) -> None:
        response = client.people.with_raw_response.translations(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = response.parse()
        assert_matches_type(PersonTranslationsResponse, person, path=["response"])

    @parametrize
    def test_streaming_response_translations(self, client: TmdbClient) -> None:
        with client.people.with_streaming_response.translations(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = response.parse()
            assert_matches_type(PersonTranslationsResponse, person, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPeople:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTmdbClient) -> None:
        person = await async_client.people.retrieve(
            person_id=0,
        )
        assert_matches_type(PersonRetrieveResponse, person, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        person = await async_client.people.retrieve(
            person_id=0,
            append_to_response="append_to_response",
            language="language",
        )
        assert_matches_type(PersonRetrieveResponse, person, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.people.with_raw_response.retrieve(
            person_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = await response.parse()
        assert_matches_type(PersonRetrieveResponse, person, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.people.with_streaming_response.retrieve(
            person_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = await response.parse()
            assert_matches_type(PersonRetrieveResponse, person, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_external_ids(self, async_client: AsyncTmdbClient) -> None:
        person = await async_client.people.external_ids(
            0,
        )
        assert_matches_type(PersonExternalIDsResponse, person, path=["response"])

    @parametrize
    async def test_raw_response_external_ids(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.people.with_raw_response.external_ids(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = await response.parse()
        assert_matches_type(PersonExternalIDsResponse, person, path=["response"])

    @parametrize
    async def test_streaming_response_external_ids(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.people.with_streaming_response.external_ids(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = await response.parse()
            assert_matches_type(PersonExternalIDsResponse, person, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_search(self, async_client: AsyncTmdbClient) -> None:
        person = await async_client.people.search(
            query="query",
        )
        assert_matches_type(PersonSearchResponse, person, path=["response"])

    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        person = await async_client.people.search(
            query="query",
            include_adult=True,
            language="language",
            page=0,
        )
        assert_matches_type(PersonSearchResponse, person, path=["response"])

    @parametrize
    async def test_raw_response_search(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.people.with_raw_response.search(
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = await response.parse()
        assert_matches_type(PersonSearchResponse, person, path=["response"])

    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.people.with_streaming_response.search(
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = await response.parse()
            assert_matches_type(PersonSearchResponse, person, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tagged_images(self, async_client: AsyncTmdbClient) -> None:
        person = await async_client.people.tagged_images(
            person_id=0,
        )
        assert_matches_type(PersonTaggedImagesResponse, person, path=["response"])

    @parametrize
    async def test_method_tagged_images_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        person = await async_client.people.tagged_images(
            person_id=0,
            page=0,
        )
        assert_matches_type(PersonTaggedImagesResponse, person, path=["response"])

    @parametrize
    async def test_raw_response_tagged_images(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.people.with_raw_response.tagged_images(
            person_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = await response.parse()
        assert_matches_type(PersonTaggedImagesResponse, person, path=["response"])

    @parametrize
    async def test_streaming_response_tagged_images(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.people.with_streaming_response.tagged_images(
            person_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = await response.parse()
            assert_matches_type(PersonTaggedImagesResponse, person, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_translations(self, async_client: AsyncTmdbClient) -> None:
        person = await async_client.people.translations(
            0,
        )
        assert_matches_type(PersonTranslationsResponse, person, path=["response"])

    @parametrize
    async def test_raw_response_translations(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.people.with_raw_response.translations(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        person = await response.parse()
        assert_matches_type(PersonTranslationsResponse, person, path=["response"])

    @parametrize
    async def test_streaming_response_translations(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.people.with_streaming_response.translations(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            person = await response.parse()
            assert_matches_type(PersonTranslationsResponse, person, path=["response"])

        assert cast(Any, response.is_closed) is True
