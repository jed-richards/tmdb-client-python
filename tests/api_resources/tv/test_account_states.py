# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from tmdb_client import TmdbClient, AsyncTmdbClient
from tmdb_client.types.tv import AccountStateRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccountStates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: TmdbClient) -> None:
        account_state = client.tv.account_states.retrieve(
            series_id=0,
        )
        assert_matches_type(AccountStateRetrieveResponse, account_state, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: TmdbClient) -> None:
        account_state = client.tv.account_states.retrieve(
            series_id=0,
            guest_session_id="guest_session_id",
            session_id="session_id",
        )
        assert_matches_type(AccountStateRetrieveResponse, account_state, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: TmdbClient) -> None:
        response = client.tv.account_states.with_raw_response.retrieve(
            series_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_state = response.parse()
        assert_matches_type(AccountStateRetrieveResponse, account_state, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: TmdbClient) -> None:
        with client.tv.account_states.with_streaming_response.retrieve(
            series_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_state = response.parse()
            assert_matches_type(AccountStateRetrieveResponse, account_state, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccountStates:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncTmdbClient) -> None:
        account_state = await async_client.tv.account_states.retrieve(
            series_id=0,
        )
        assert_matches_type(AccountStateRetrieveResponse, account_state, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncTmdbClient) -> None:
        account_state = await async_client.tv.account_states.retrieve(
            series_id=0,
            guest_session_id="guest_session_id",
            session_id="session_id",
        )
        assert_matches_type(AccountStateRetrieveResponse, account_state, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncTmdbClient) -> None:
        response = await async_client.tv.account_states.with_raw_response.retrieve(
            series_id=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account_state = await response.parse()
        assert_matches_type(AccountStateRetrieveResponse, account_state, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncTmdbClient) -> None:
        async with async_client.tv.account_states.with_streaming_response.retrieve(
            series_id=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account_state = await response.parse()
            assert_matches_type(AccountStateRetrieveResponse, account_state, path=["response"])

        assert cast(Any, response.is_closed) is True
