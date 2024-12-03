# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tmdb_client import TmdbClient, AsyncTmdbClient
from tmdb_client.types import (
    ListClearResponse,
    ListCreateResponse,
    ListDeleteResponse,
    ListAddItemResponse,
    ListRetrieveResponse,
    ListItemStatusResponse,
    ListRemoveItemResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLists:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: TmdbClient) -> None:
        list_ = client.lists.create(
            session_id="session_id",
            raw_body="RAW_BODY",
        )
        assert_matches_type(ListCreateResponse, list_, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: TmdbClient) -> None:
        response = client.lists.with_raw_response.create(
            session_id="session_id",
            raw_body="RAW_BODY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListCreateResponse, list_, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: TmdbClient) -> None:
        with client.lists.with_streaming_response.create(
            session_id="session_id",
            raw_body="RAW_BODY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListCreateResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: TmdbClient) -> None:
        list_ = client.lists.retrieve(
            list_id=0,
        )
        assert_matches_type(ListRetrieveResponse, list_, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: TmdbClient) -> None:
        list_ = client.lists.retrieve(
            list_id=0,
            language="language",
            page=0,
        )
        assert_matches_type(ListRetrieveResponse, list_, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: TmdbClient) -> None:
        response = client.lists.with_raw_response.retrieve(
            list_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListRetrieveResponse, list_, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: TmdbClient) -> None:
        with client.lists.with_streaming_response.retrieve(
            list_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListRetrieveResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: TmdbClient) -> None:
        list_ = client.lists.delete(
            list_id=0,
            session_id="session_id",
        )
        assert_matches_type(ListDeleteResponse, list_, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: TmdbClient) -> None:
        response = client.lists.with_raw_response.delete(
            list_id=0,
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListDeleteResponse, list_, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: TmdbClient) -> None:
        with client.lists.with_streaming_response.delete(
            list_id=0,
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListDeleteResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_add_item(self, client: TmdbClient) -> None:
        list_ = client.lists.add_item(
            list_id=0,
            session_id="session_id",
        )
        assert_matches_type(ListAddItemResponse, list_, path=["response"])

    @parametrize
    def test_method_add_item_with_all_params(self, client: TmdbClient) -> None:
        list_ = client.lists.add_item(
            list_id=0,
            session_id="session_id",
            raw_body="RAW_BODY",
        )
        assert_matches_type(ListAddItemResponse, list_, path=["response"])

    @parametrize
    def test_raw_response_add_item(self, client: TmdbClient) -> None:
        response = client.lists.with_raw_response.add_item(
            list_id=0,
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListAddItemResponse, list_, path=["response"])

    @parametrize
    def test_streaming_response_add_item(self, client: TmdbClient) -> None:
        with client.lists.with_streaming_response.add_item(
            list_id=0,
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListAddItemResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_clear(self, client: TmdbClient) -> None:
        list_ = client.lists.clear(
            list_id=0,
            confirm=True,
            session_id="session_id",
        )
        assert_matches_type(ListClearResponse, list_, path=["response"])

    @parametrize
    def test_raw_response_clear(self, client: TmdbClient) -> None:
        response = client.lists.with_raw_response.clear(
            list_id=0,
            confirm=True,
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListClearResponse, list_, path=["response"])

    @parametrize
    def test_streaming_response_clear(self, client: TmdbClient) -> None:
        with client.lists.with_streaming_response.clear(
            list_id=0,
            confirm=True,
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListClearResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_item_status(self, client: TmdbClient) -> None:
        list_ = client.lists.item_status(
            list_id=0,
        )
        assert_matches_type(ListItemStatusResponse, list_, path=["response"])

    @parametrize
    def test_method_item_status_with_all_params(self, client: TmdbClient) -> None:
        list_ = client.lists.item_status(
            list_id=0,
            language="language",
            movie_id=0,
        )
        assert_matches_type(ListItemStatusResponse, list_, path=["response"])

    @parametrize
    def test_raw_response_item_status(self, client: TmdbClient) -> None:
        response = client.lists.with_raw_response.item_status(
            list_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListItemStatusResponse, list_, path=["response"])

    @parametrize
    def test_streaming_response_item_status(self, client: TmdbClient) -> None:
        with client.lists.with_streaming_response.item_status(
            list_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListItemStatusResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_remove_item(self, client: TmdbClient) -> None:
        list_ = client.lists.remove_item(
            list_id=0,
            session_id="session_id",
            raw_body="RAW_BODY",
        )
        assert_matches_type(ListRemoveItemResponse, list_, path=["response"])

    @parametrize
    def test_raw_response_remove_item(self, client: TmdbClient) -> None:
        response = client.lists.with_raw_response.remove_item(
            list_id=0,
            session_id="session_id",
            raw_body="RAW_BODY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = response.parse()
        assert_matches_type(ListRemoveItemResponse, list_, path=["response"])

    @parametrize
    def test_streaming_response_remove_item(self, client: TmdbClient) -> None:
        with client.lists.with_streaming_response.remove_item(
            list_id=0,
            session_id="session_id",
            raw_body="RAW_BODY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = response.parse()
            assert_matches_type(ListRemoveItemResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLists:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncTmdbClient) -> None:
        list_ = await async_client.lists.create(
            session_id="session_id",
            raw_body="RAW_BODY",
        )
        assert_matches_type(ListCreateResponse, list_, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.lists.with_raw_response.create(
            session_id="session_id",
            raw_body="RAW_BODY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListCreateResponse, list_, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.lists.with_streaming_response.create(
            session_id="session_id",
            raw_body="RAW_BODY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListCreateResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTmdbClient) -> None:
        list_ = await async_client.lists.retrieve(
            list_id=0,
        )
        assert_matches_type(ListRetrieveResponse, list_, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        list_ = await async_client.lists.retrieve(
            list_id=0,
            language="language",
            page=0,
        )
        assert_matches_type(ListRetrieveResponse, list_, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.lists.with_raw_response.retrieve(
            list_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListRetrieveResponse, list_, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.lists.with_streaming_response.retrieve(
            list_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListRetrieveResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncTmdbClient) -> None:
        list_ = await async_client.lists.delete(
            list_id=0,
            session_id="session_id",
        )
        assert_matches_type(ListDeleteResponse, list_, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.lists.with_raw_response.delete(
            list_id=0,
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListDeleteResponse, list_, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.lists.with_streaming_response.delete(
            list_id=0,
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListDeleteResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_add_item(self, async_client: AsyncTmdbClient) -> None:
        list_ = await async_client.lists.add_item(
            list_id=0,
            session_id="session_id",
        )
        assert_matches_type(ListAddItemResponse, list_, path=["response"])

    @parametrize
    async def test_method_add_item_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        list_ = await async_client.lists.add_item(
            list_id=0,
            session_id="session_id",
            raw_body="RAW_BODY",
        )
        assert_matches_type(ListAddItemResponse, list_, path=["response"])

    @parametrize
    async def test_raw_response_add_item(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.lists.with_raw_response.add_item(
            list_id=0,
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListAddItemResponse, list_, path=["response"])

    @parametrize
    async def test_streaming_response_add_item(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.lists.with_streaming_response.add_item(
            list_id=0,
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListAddItemResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_clear(self, async_client: AsyncTmdbClient) -> None:
        list_ = await async_client.lists.clear(
            list_id=0,
            confirm=True,
            session_id="session_id",
        )
        assert_matches_type(ListClearResponse, list_, path=["response"])

    @parametrize
    async def test_raw_response_clear(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.lists.with_raw_response.clear(
            list_id=0,
            confirm=True,
            session_id="session_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListClearResponse, list_, path=["response"])

    @parametrize
    async def test_streaming_response_clear(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.lists.with_streaming_response.clear(
            list_id=0,
            confirm=True,
            session_id="session_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListClearResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_item_status(self, async_client: AsyncTmdbClient) -> None:
        list_ = await async_client.lists.item_status(
            list_id=0,
        )
        assert_matches_type(ListItemStatusResponse, list_, path=["response"])

    @parametrize
    async def test_method_item_status_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        list_ = await async_client.lists.item_status(
            list_id=0,
            language="language",
            movie_id=0,
        )
        assert_matches_type(ListItemStatusResponse, list_, path=["response"])

    @parametrize
    async def test_raw_response_item_status(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.lists.with_raw_response.item_status(
            list_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListItemStatusResponse, list_, path=["response"])

    @parametrize
    async def test_streaming_response_item_status(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.lists.with_streaming_response.item_status(
            list_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListItemStatusResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_remove_item(self, async_client: AsyncTmdbClient) -> None:
        list_ = await async_client.lists.remove_item(
            list_id=0,
            session_id="session_id",
            raw_body="RAW_BODY",
        )
        assert_matches_type(ListRemoveItemResponse, list_, path=["response"])

    @parametrize
    async def test_raw_response_remove_item(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.lists.with_raw_response.remove_item(
            list_id=0,
            session_id="session_id",
            raw_body="RAW_BODY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        list_ = await response.parse()
        assert_matches_type(ListRemoveItemResponse, list_, path=["response"])

    @parametrize
    async def test_streaming_response_remove_item(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.lists.with_streaming_response.remove_item(
            list_id=0,
            session_id="session_id",
            raw_body="RAW_BODY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            list_ = await response.parse()
            assert_matches_type(ListRemoveItemResponse, list_, path=["response"])

        assert cast(Any, response.is_closed) is True
