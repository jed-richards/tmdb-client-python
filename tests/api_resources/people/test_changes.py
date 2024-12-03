# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tmdb_client import TmdbClient, AsyncTmdbClient
from tmdb_client._utils import parse_date
from tmdb_client.types.people import ChangeListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChanges:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: TmdbClient) -> None:
        change = client.people.changes.list()
        assert_matches_type(ChangeListResponse, change, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: TmdbClient) -> None:
        change = client.people.changes.list(
            end_date=parse_date("2019-12-27"),
            page=0,
            start_date=parse_date("2019-12-27"),
        )
        assert_matches_type(ChangeListResponse, change, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: TmdbClient) -> None:
        response = client.people.changes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        change = response.parse()
        assert_matches_type(ChangeListResponse, change, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: TmdbClient) -> None:
        with client.people.changes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            change = response.parse()
            assert_matches_type(ChangeListResponse, change, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncChanges:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncTmdbClient) -> None:
        change = await async_client.people.changes.list()
        assert_matches_type(ChangeListResponse, change, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        change = await async_client.people.changes.list(
            end_date=parse_date("2019-12-27"),
            page=0,
            start_date=parse_date("2019-12-27"),
        )
        assert_matches_type(ChangeListResponse, change, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.people.changes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        change = await response.parse()
        assert_matches_type(ChangeListResponse, change, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.people.changes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            change = await response.parse()
            assert_matches_type(ChangeListResponse, change, path=["response"])

        assert cast(Any, response.is_closed) is True
